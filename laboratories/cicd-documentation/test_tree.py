from tree import Tree
# Presupunând că ai clasa Tree în tree.py

def test_add_and_find():
    # 1. Pregătim datele
    t = Tree()
    t.add(5)
    t.add(3)
    t.add(7)

    # 2. Testăm dacă metoda 'find' găsește un nod existent
    found_node = t.find(3)
    assert found_node is not None, "Nodul ar trebui să fie găsit"
    assert found_node.data == 3, "Valoarea nodului ar trebui să fie 3"

    # 3. Testăm dacă metoda reacționează corect la un nod inexistent
    not_found = t.find(10)
    assert not_found is None, "Nodul nu ar trebui să existe"
