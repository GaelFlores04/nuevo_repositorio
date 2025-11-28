import json
from enum import Enum
from memory_management import incrementHeapAllocations, displayMemoryUsage

class Genre(Enum):
    FICTION = "Ficción"
    NON_FICTION = "No Ficción"
    SCIENCE = "Ciencia"
    HISTORY = "Historia"
    FANTASY = "Fantasía"
    BIOGRAPHY = "Biografía"
    OTHER = "Otro"

class Item:
    def __init__(self, id_, title, year, genre, quantity):
        self._id = id_
        self._title = title
        self._year = year
        self._genre = genre
        self._quantity = quantity
        incrementHeapAllocations(self, 1)  # Simulación de asignación de memoria

    def mostrar_info(self):
        raise NotImplementedError("Debe implementarse en la subclase")

    def get_id(self): return self._id
    def get_title(self): return self._title
    def get_quantity(self): return self._quantity

    def prestar(self):
        if self._quantity > 0:
            self._quantity -= 1
            return True
        return False

    def devolver(self): self._quantity += 1

    def to_dict(self):
        return {
            "id": self._id,
            "title": self._title,
            "year": self._year,
            "genre": self._genre.value,
            "quantity": self._quantity,
            "type": self.__class__.__name__
        }


class Book(Item):
    def __init__(self, id_, title, author, year, genre, quantity):
        super().__init__(id_, title, year, genre, quantity)
        self._author = author
        incrementHeapAllocations(self, 1)

    def mostrar_info(self):
        print(f"Libro: {self._title} ({self._year}) - Autor: {self._author} | Género: {self._genre.value} | Cantidad: {self._quantity}")

    def to_dict(self):
        data = super().to_dict()
        data["author"] = self._author
        return data

class Magazine(Item):
    def __init__(self, id_, title, edition, year, genre, quantity):
        super().__init__(id_, title, year, genre, quantity)
        self._edition = edition
        incrementHeapAllocations(self, 1)

    def mostrar_info(self):
        print(f"Revista: {self._title} - Edición {self._edition} ({self._year}) | Género: {self._genre.value} | Cantidad: {self._quantity}")

    def to_dict(self):
        data = super().to_dict()
        data["edition"] = self._edition
        return data


class Member:
    def __init__(self, id_, name):
        self._id = id_
        self._name = name
        self._borrowed_items = []
        incrementHeapAllocations(self, 1)

    def prestar_item(self, item):
        if item.prestar():
            self._borrowed_items.append(item.get_id())
            print(f"{self._name} ha tomado prestado: {item.get_title()}")
        else:
            print(f"No hay copias disponibles de {item.get_title()}")

    def devolver_item(self, item):
        if item.get_id() in self._borrowed_items:
            self._borrowed_items.remove(item.get_id())
            item.devolver()
            print(f"{self._name} devolvió: {item.get_title()}")
        else:
            print("Ese ítem no fue prestado por este miembro.")

    def mostrar_info(self):
        print(f"Miembro: {self._name} (ID: {self._id}) | Ítems prestados: {len(self._borrowed_items)}")

    def to_dict(self):
        return {"id": self._id, "name": self._name, "borrowed_items": self._borrowed_items}


class Library:
    def __init__(self):
        self._items = []
        self._members = []

    def agregar_item(self, item):
        self._items.append(item)
        print("Ítem agregado con éxito.")
        displayMemoryUsage()

    def agregar_miembro(self, member):
        self._members.append(member)
        print("Miembro agregado con éxito.")
        displayMemoryUsage()

    def mostrar_items(self):
        if not self._items:
            print("No hay ítems en la biblioteca.")
        else:
            for item in self._items:
                item.mostrar_info()
        displayMemoryUsage()

    def mostrar_miembros(self):
        if not self._members:
            print("No hay miembros registrados.")
        else:
            for m in self._members:
                m.mostrar_info()
        displayMemoryUsage()

    def prestar_item(self, member_id, item_id):
        m = next((x for x in self._members if x._id == member_id), None)
        i = next((x for x in self._items if x._id == item_id), None)
        if m and i:
            m.prestar_item(i)
        else:
            print("Miembro o ítem no encontrado.")
        displayMemoryUsage()

    def devolver_item(self, member_id, item_id):
        m = next((x for x in self._members if x._id == member_id), None)
        i = next((x for x in self._items if x._id == item_id), None)
        if m and i:
            m.devolver_item(i)
        else:
            print("Miembro o ítem no encontrado.")
        displayMemoryUsage()

    def buscar_item(self, title):
        encontrados = [i for i in self._items if title.lower() in i.get_title().lower()]
        if not encontrados:
            print("No se encontraron resultados.")
        else:
            for i in encontrados:
                i.mostrar_info()
        displayMemoryUsage()

    def buscar_miembro(self, name):
        encontrados = [m for m in self._members if name.lower() in m._name.lower()]
        if not encontrados:
            print("No se encontraron miembros.")
        else:
            for m in encontrados:
                m.mostrar_info()
        displayMemoryUsage()

    def guardar_datos(self, archivo="biblioteca.json"):
        data = {"items": [i.to_dict() for i in self._items], "members": [m.to_dict() for m in self._members]}
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Datos guardados en {archivo}")
        displayMemoryUsage()

    def cargar_datos(self, archivo="biblioteca.json"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
            for i in data["items"]:
                if i["type"] == "Book":
                    self._items.append(Book(i["id"], i["title"], i.get("author", ""), i["year"], Genre(i["genre"]), i["quantity"]))
                elif i["type"] == "Magazine":
                    self._items.append(Magazine(i["id"], i["title"], i.get("edition", ""), i["year"], Genre(i["genre"]), i["quantity"]))
            for m in data["members"]:
                member = Member(m["id"], m["name"])
                member._borrowed_items = m["borrowed_items"]
                self._members.append(member)
            print(f"Datos cargados desde {archivo}")
        except FileNotFoundError:
            print("Archivo no encontrado, iniciando biblioteca vacía.")
        displayMemoryUsage()
