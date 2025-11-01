
def search_loop(bst):
   
    print("=== Search Engine Autocomplete ===")
    print("Type '#' to exit.")
    while True:
        prefix = input("\nEnter prefix: ").strip()
        if prefix == "#":
            print("Goodbye!")
            break
        suggestions = bst.autocomplete(prefix)
        if suggestions:
            print(f"Suggestions for '{prefix}':")
            print(", ".join(suggestions[:10])) 
        else:
            print("No suggestions found.")

pass