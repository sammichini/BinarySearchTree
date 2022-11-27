import lab3
import unittest



class T0_tree__insert(unittest.TestCase):

    def test_balanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        #The following check is without using tree as an iterator (which uses inorder traversal)
        #So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.left.data, 2)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 6)
        self.assertEqual(t.root.right.left.data, 5)
        self.assertEqual(t.root.right.right.data, 7)

        print("\n")


class T1_min_and_max(unittest.TestCase):

    def test_min_and_max(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        minimum = t.min()
        self.assertEqual(minimum, 1)
        maximum = t.max()
        self.assertEqual(maximum, 7)

        print("\n")

class T2_Traversal(unittest.TestCase):

    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [1, 2, 3, 4, 5, 6, 7])
        print("inorder traversal")
        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6, 7])
        print("preorder traversal")
        self.assertEqual(preorder, [4, 2, 1, 3, 6, 5, 7])
        print("\n")




class T3_successor(unittest.TestCase):

    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)

        easy_success = tree_success.find_successor(8).data
        medium_success = tree_success.find_successor(10).data
        tough_success = tree_success.find_successor(7).data

        self.assertEqual(easy_success, 10)
        self.assertEqual(medium_success, 13)
        self.assertEqual(tough_success, 8)

        print("\n")


class T4_delete(unittest.TestCase):

    def test_delete(self):
        print("\n")
        print("delete function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)

        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(6)
        l3 = [node for node in t]
        t.delete(8)
        l4 = [node for node in t]
        t.delete(10)
        l5 = [node for node in t]



        self.assertEqual(l1, [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(l2, [1, 3, 4, 6, 8, 10, 13, 14])
        self.assertEqual(l3, [1, 3, 4, 8, 10, 13, 14])
        self.assertEqual(l4, [1, 3, 4, 10, 13, 14])
        self.assertEqual(l5, [1, 3, 4, 13, 14])

        print("\n")


class T5_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("contains function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), False)
        print("\n")

class T6_insert_num(unittest.TestCase):

    def test_numerical(self):
        print("\n")
        print("Test that only numerical input is valid")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)

        self.assertRaises(TypeError, t.insert, "Garlic Bread")
        print("\n")
        print("\n")

class T7_test_traverse_after_delete(unittest.TestCase):

    def test_traverse_delete(self):
        print("\n")
        print("traversals after deletion")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(5)
        t.insert(99)
        t.delete(99)
        list1 = [node for node in t.postorder()]
        list2 = [node for node in t.preorder()]
        self.assertEqual(list1, [5, 3, 8])
        self.assertEqual(list2, [8, 3, 5])
        print("\n")
        print("\n")

class T8_find_node_insert_successor_delete(unittest.TestCase):

    def test_find(self):
        print("\n")
        print("Check functions that use find node")
        t = lab3.Tree()
        t.insert(5)
        t.insert(9)
        t.insert(33)
        t.insert(108)
        t.delete(33)
        node = t.find_successor(9)

        self.assertEqual(node.data, 108)


        print("\n")

class T9_test_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("Check contains after inserts, delete, inserts")
        t = lab3.Tree()
        t.insert(5)
        t.insert(9)
        t.insert(33)
        t.insert(108)
        t.delete(33)
        list = [37, 55, 1290, 34290, 33, 20]
        for i in list:
            t.insert(i)
        boolean = t.contains(33)

        self.assertTrue(boolean)


        print("\n")

class T10_successor(unittest.TestCase):

    def test_success(self):
        print("\n")
        print("Check successor after inserts, delete, inserts")
        t = lab3.Tree()
        t.insert(5)
        t.insert(9)
        t.insert(33)
        t.insert(108)
        t.delete(33)
        list = [37, 55, 1290, 34290, 33, 20]
        for i in list:
            t.insert(i)
        node = t.find_successor(33)

        self.assertEqual(node.data, 37)


        print("\n")

class T11_delete_tree(unittest.TestCase):

    def test_delete_tree(self):
        print("\n")
        print("Delete whole tree")
        t = lab3.Tree()
        t.insert(5)
        t.insert(9)
        t.insert(33)
        t.insert(108)
        t.delete(33)
        list = [37, 55, 1290, 34290, 33, 20]
        for i in list:
            t.insert(i)
        for node in t:  # use iterator to pass in data arg for each node
            t.delete(node)

        self.assertIsNone(t.root)


        print("\n")


class T12_key_err_delete(unittest.TestCase):

    def test_key_delete(self):
        print("\n")
        print("Test key error is raised for delete on empty tree")
        t = lab3.Tree()

        self.assertRaises(KeyError, t.delete, 5)
        print("\n")
        print("\n")

class T13_key_err_successor(unittest.TestCase):

    def test_key_successor(self):
        print("\n")
        print("Test key error is raised for find successor on empty tree")
        t = lab3.Tree()

        self.assertRaises(KeyError, t.find_successor, 5)
        print("\n")
        print("\n")

if __name__ == '__main__' :
    unittest.main()