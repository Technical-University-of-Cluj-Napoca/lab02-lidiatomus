# main.py
from BST import BST
from search_engine import search_loop


def main():
    bst = BST(source="wordlist.txt", file=True)
    search_loop(bst)


if __name__ == "__main__":
    main()
