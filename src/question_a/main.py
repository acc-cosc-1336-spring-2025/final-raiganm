import question_a

def main():
    while True:
        while True:
            dna_string1 = input("Enter DNA string A, C, G, T (must have 8-16 characters): ")
            if 8 <= len(dna_string1) <= 17:
                break
            else:
                print("Invalid input. String must be between 8-16 characters.")

        while True:
            dna_string2 = input("Enter DNA substring A, C, G, T (must have 4 characters): ")
            if len(dna_string2) == 4:
                break
            else:
                print("Invalid input. Substring must contain 4 characters.")

        results = question_a.get_most_likely_ancestor_consensus(dna_string1, dna_string2)

        if results:
            print("Occurrences of", dna_string2, "found at positions: ", results)
        else:
            print("No occurrences of", dna_string2, "found in string.")

        while True:
            choice = input("Enter another DNA string? (Y/N): ")
            if choice == "Y" or choice == "y":
                print("")
                break
            elif choice == "N" or choice == "n":
                print("Exiting...")
                return
            else:
                print("Invalid input.")
            
main()

