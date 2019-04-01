import unittest
from unittest.mock import patch 

def main():
    # ...
    x = input("First: ")
    if x !="mtu":
        raise ValueError("Not the correct person")
    return x


class Additionhappycases(unittest.TestCase):
    def test_add(self):
        with patch('builtins.input') as mocked_input:
            main()
            self.assertEqual(main(),"mtu")
            
             
    


if __name__ == '__main__':
    unittest.main()




