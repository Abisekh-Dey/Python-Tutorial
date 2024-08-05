class Data:
    def __init__(self,Name):
        self.name=Name
    def Name(self):
        return self.name
    
#file###   
def print_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("File not found.")

# Example usage:
filename = 'names.txt'  # Replace 'example.txt' with the path to your file
print_file(filename)