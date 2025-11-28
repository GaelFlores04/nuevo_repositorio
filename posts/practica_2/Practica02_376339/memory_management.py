# memory_management.py
MEMORY_MANAGEMENT_DISPLAY = True
heap_allocations = 0
heap_deallocations = 0

heap_memory_records = {}

def displayMemoryUsage():
    if not MEMORY_MANAGEMENT_DISPLAY:
        return
    print("\n-------------------------------------------------")
    print("|                   Uso de Memoria              |")
    print("-------------------------------------------------")
    print(f"| Heap (Memoria Dinamica)                       |")
    print(f"|   Asignaciones: {heap_allocations:<28} |")
    print(f"|   Liberaciones: {heap_deallocations:<28} |")
    print("-------------------------------------------------")
    print("\nDetalles de Memoria Heap:")
    for ptr, size in heap_memory_records.items():
        print(f"  ObjID={ptr}, Tamaño={size} bytes")
    print("-------------------------------------------------\n")

def incrementHeapAllocations(obj, size):
    global heap_allocations
    heap_allocations += 1
    heap_memory_records[id(obj)] = size

def incrementHeapDeallocations(obj):
    global heap_deallocations
    heap_deallocations += 1
    if id(obj) in heap_memory_records:
        del heap_memory_records[id(obj)]
