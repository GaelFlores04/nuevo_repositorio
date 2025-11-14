---
title: "Práctica 2: Programación Orientada a Objetos"
date: 2025-11-14
draft: false
---


# Codigo Migrado en python(POO)



Guarda este archivo en la raíz del proyecto o en una carpeta `biblioteca_python/`. Es autocontenido y usa JSON (`data.json`) para persistencia.

```python
#!/usr/bin/env python3
# biblioteca_poo.py
# Implementación POO de una Biblioteca (préstamos, usuarios, ítems) con persistencia JSON
# Requisitos: Python 3.7+

import json
from datetime import datetime
from typing import List, Dict, Optional
from abc import ABC, abstractmethod
import os

DATA_FILE = "biblioteca_data.json"

# -------------------------
# Modelos (POO)
# -------------------------

class Item(ABC):
    """Clase abstracta para ítems de la biblioteca."""
    def __init__(self, item_id: str, title: str, year: int):
        self._id = item_id            # encapsulado (protected)
        self.title = title
        self.year = year
        self.available = True
        self.borrower_id: Optional[str] = None
        self.borrow_date: Optional[str] = None

    @property
    def id(self):
        return self._id

    @abstractmethod
    def item_type(self) -> str:
        pass

    def to_dict(self) -> Dict:
        return {
            "id": self._id,
            "title": self.title,
            "year": self.year,
            "type": self.item_type(),
            "available": self.available,
            "borrower_id": self.borrower_id,
            "borrow_date": self.borrow_date
        }

    def borrow(self, user_id: str) -> bool:
        if not self.available:
            return False
        self.available = False
        self.borrower_id = user_id
        self.borrow_date = datetime.utcnow().isoformat()
        return True

    def give_back(self) -> bool:
        if self.available:
            return False
        self.available = True
        self.borrower_id = None
        self.borrow_date = None
        return True

class Book(Item):
    def __init__(self, item_id: str, title: str, author: str, year: int, isbn: Optional[str] = None):
        super().__init__(item_id, title, year)
        self.author = author
        self.isbn = isbn

    def item_type(self) -> str:
        return "book"

    def to_dict(self) -> Dict:
        d = super().to_dict()
        d.update({"author": self.author, "isbn": self.isbn})
        return d

class Magazine(Item):
    def __init__(self, item_id: str, title: str, issue: str, year: int):
        super().__init__(item_id, title, year)
        self.issue = issue

    def item_type(self) -> str:
        return "magazine"

    def to_dict(self) -> Dict:
        d = super().to_dict()
        d.update({"issue": self.issue})
        return d

class User:
    def __init__(self, user_id: str, name: str, email: Optional[str] = None):
        self._id = user_id     # encapsulación
        self.name = name
        self.email = email
        self.borrowed_items: List[str] = []  # lista de ids

    @property
    def id(self):
        return self._id

    def to_dict(self) -> Dict:
        return {
            "id": self._id,
            "name": self.name,
            "email": self.email,
            "borrowed_items": self.borrowed_items
        }

# -------------------------
# Biblioteca (gestor)
# -------------------------

class Library:
    def __init__(self):
        self.items: Dict[str, Item] = {}
        self.users: Dict[str, User] = {}
        self.load()

    # --- CRUD / operaciones ---
    def add_user(self, user: User) -> None:
        if user.id in self.users:
            raise ValueError("Usuario ya existe")
        self.users[user.id] = user
        self.save()

    def add_item(self, item: Item) -> None:
        if item.id in self.items:
            raise ValueError("Ítem ya existe")
        self.items[item.id] = item
        self.save()

    def find_items(self, query: str) -> List[Item]:
        q = query.lower()
        results = []
        for it in self.items.values():
            if q in it.title.lower() or q in it.item_type().lower():
                results.append(it)
            else:
                # campos específicos
                if isinstance(it, Book) and (q in it.author.lower() if it.author else False):
                    results.append(it)
        return results

    def find_users(self, query: str) -> List[User]:
        q = query.lower()
        return [u for u in self.users.values() if q in u.name.lower() or q in (u.email or "").lower() or q == u.id.lower()]

    def borrow_item(self, item_id: str, user_id: str) -> bool:
        if item_id not in self.items:
            raise ValueError("Ítem no encontrado")
        if user_id not in self.users:
            raise ValueError("Usuario no encontrado")
        item = self.items[item_id]
        user = self.users[user_id]
        if not item.available:
            return False
        ok = item.borrow(user_id)
        if ok:
            user.borrowed_items.append(item_id)
            self.save()
        return ok

    def return_item(self, item_id: str, user_id: str) -> bool:
        if item_id not in self.items:
            raise ValueError("Ítem no encontrado")
        if user_id not in self.users:
            raise ValueError("Usuario no encontrado")
        item = self.items[item_id]
        user = self.users[user_id]
        if item.available or item.borrower_id != user_id:
            return False
        ok = item.give_back()
        if ok:
            if item_id in user.borrowed_items:
                user.borrowed_items.remove(item_id)
            self.save()
        return ok

    # --- persistencia ---
    def save(self) -> None:
        payload = {
            "items": {iid: it.to_dict() for iid, it in self.items.items()},
            "users": {uid: u.to_dict() for uid, u in self.users.items()}
        }
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)

    def load(self) -> None:
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            payload = json.load(f)
        # Cargar users
        self.users = {}
        for uid, ud in payload.get("users", {}).items():
            u = User(uid, ud.get("name", ""), ud.get("email"))
            u.borrowed_items = ud.get("borrowed_items", [])
            self.users[uid] = u
        # Cargar items (reconstruir tipo concreto)
        self.items = {}
        for iid, idata in payload.get("items", {}).items():
            t = idata.get("type")
            if t == "book":
                it = Book(iid, idata.get("title", ""), idata.get("author", ""), idata.get("year", 0), idata.get("isbn"))
            elif t == "magazine":
                it = Magazine(iid, idata.get("title", ""), idata.get("issue", ""), idata.get("year", 0))
            else:
                # genérico fallback
                class GenericItem(Item):
                    def item_type(self): return "generic"
                it = GenericItem(iid, idata.get("title", ""), idata.get("year", 0))
            it.available = idata.get("available", True)
            it.borrower_id = idata.get("borrower_id")
            it.borrow_date = idata.get("borrow_date")
            self.items[iid] = it

    # Utility
    def list_items(self) -> List[Dict]:
        return [it.to_dict() for it in self.items.values()]

    def list_users(self) -> List[Dict]:
        return [u.to_dict() for u in self.users.values()]

# -------------------------
# Interfaz de consola (menú)
# -------------------------

def input_nonempty(prompt: str) -> str:
    while True:
        v = input(prompt).strip()
        if v:
            return v

def main_menu(lib: Library):
    while True:
        print("\n=== Biblioteca POO ===")
        print("1) Registrar usuario")
        print("2) Registrar ítem (libro/revista)")
        print("3) Buscar ítems")
        print("4) Buscar usuarios")
        print("5) Prestar ítem")
        print("6) Devolver ítem")
        print("7) Listar ítems")
        print("8) Listar usuarios")
        print("9) Salir")
        choice = input("Opción: ").strip()
        try:
            if choice == "1":
                uid = input_nonempty("ID usuario: ")
                name = input_nonempty("Nombre: ")
                email = input("Email (opcional): ").strip() or None
                lib.add_user(User(uid, name, email))
                print("Usuario registrado.")
            elif choice == "2":
                itype = input("Tipo (book/magazine): ").strip().lower()
                iid = input_nonempty("ID ítem: ")
                title = input_nonempty("Título: ")
                year = int(input("Año: ").strip() or 0)
                if itype == "book":
                    author = input_nonempty("Autor: ")
                    isbn = input("ISBN (opcional): ").strip() or None
                    lib.add_item(Book(iid, title, author, year, isbn))
                else:
                    issue = input("Número/Edición: ").strip() or "n/a"
                    lib.add_item(Magazine(iid, title, issue, year))
                print("Ítem registrado.")
            elif choice == "3":
                q = input_nonempty("Buscar (título/autor/tipo): ")
                res = lib.find_items(q)
                if not res:
                    print("No hay resultados.")
                else:
                    for it in res:
                        print(json.dumps(it.to_dict(), ensure_ascii=False, indent=2))
            elif choice == "4":
                q = input_nonempty("Buscar usuario (nombre/id/email): ")
                res = lib.find_users(q)
                if not res:
                    print("No hay resultados.")
                else:
                    for u in res:
                        print(json.dumps(u.to_dict(), ensure_ascii=False, indent=2))
            elif choice == "5":
                iid = input_nonempty("ID ítem a prestar: ")
                uid = input_nonempty("ID usuario: ")
                ok = lib.borrow_item(iid, uid)
                if ok:
                    print("Préstamo realizado.")
                else:
                    print("No fue posible prestar (puede que no esté disponible).")
            elif choice == "6":
                iid = input_nonempty("ID ítem a devolver: ")
                uid = input_nonempty("ID usuario que devuelve: ")
                ok = lib.return_item(iid, uid)
                if ok:
                    print("Devolución registrada.")
                else:
                    print("No se pudo procesar la devolución.")
            elif choice == "7":
                for it in lib.list_items():
                    print(json.dumps(it, ensure_ascii=False, indent=2))
            elif choice == "8":
                for u in lib.list_users():
                    print(json.dumps(u, ensure_ascii=False, indent=2))
            elif choice == "9":
                print("Saliendo.")
                break
            else:
                print("Opción inválida.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    library = Library()
    print("Datos cargados. Ítems:", len(library.items), " Usuarios:", len(library.users))
    main_menu(library)

```

**Qué hace** (resumen):

- `Item` es abstracto, con `Book` y `Magazine` como subclases (herencia + polimorfismo).
- Encapsulamiento: atributos `_id` privados/protegidos, propiedades públicas para acceder.
- Abstracción: `Item` oculta detalles concretos a la lógica de la `Library`.
- Polimorfismo: `item_type()` y `to_dict()` con comportamiento según la subclase.
- Persistencia: `biblioteca_data.json` guarda `items` y `users`.
- Menú: permite registrar usuarios/ítems, prestar, devolver, buscar y listar.