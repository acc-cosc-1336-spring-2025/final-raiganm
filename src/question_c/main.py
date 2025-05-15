import question_c

def main():
    while True:
        num = input('Display Multiplication Table? (Y/N): ')

        if num == 'Y' or num == 'y':
            result = question_c.create_multiplication_table(5, 10)
            print("Multiplication Table:")
            question_c.display_multiplication_table(result)

            while True:
                repeat_table = input("Display multiplication table again? (Y/N): ")
            
                if repeat_table == 'Y' or repeat_table == 'y':
                    print("Multiplication Table:")
                    question_c.display_multiplication_table(result)
                elif repeat_table == 'N' or repeat_table == 'n':
                    print("Exiting...")
                    return
                else:
                    print("Invalid Input")
            
        elif num == 'N' or num == 'n':
            print("Exiting...")
            return
        else:
            print("Invalid Input")

main()
