import sys
def downcase_it(text):
    return text.lower()

def main():
    if len(sys.argv) == 1:
        print("none")
        return

    for param in sys.argv[1:]:
        print(downcase_it(param))

if __name__ == "__main__":
    main()