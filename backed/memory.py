memory_store = []

def store_memory(text):
    memory_store.append(text)

def get_memory():
    return memory_store[-3:]