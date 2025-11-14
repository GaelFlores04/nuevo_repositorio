---
title: "Práctica 2: Programación Orientada a Objetos"
date: 2025-11-14
draft: false
---



# Diseño de clases (UML textual + explicación)

```
Library
 - items: Dict[str, Item]
 - users: Dict[str, User]
 + add_user(user)
 + add_item(item)
 + find_items(query) -> List[Item]
 + find_users(query) -> List[User]
 + borrow_item(item_id, user_id) -> bool
 + return_item(item_id, user_id) -> bool
 + save(), load()

Item (abstract)
 - _id: str
 - title: str
 - year: int
 - available: bool
 - borrower_id: Optional[str]
 - borrow_date: Optional[str]
 + item_type() -> str  (abstract)
 + borrow(user_id) -> bool
 + give_back() -> bool
 + to_dict() -> Dict

Book (Item)
 - author: str
 - isbn: Optional[str]

Magazine (Item)
 - issue: str

User
 - _id: str
 - name: str
 - email: Optional[str]
 - borrowed_items: List[str]

```

**Relaciones**:

- `Library` maneja colecciones de `Item` y `User`.
- `Book` y `Magazine` heredan de `Item` (IS-A).
- `Library` usa métodos de `Item` (polimorfismo) sin preocuparse por el tipo concreto.