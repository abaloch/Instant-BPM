import os





def main(): 
    print("hello world")
    files = os.listdir()
    # print(files)
    # print(os.listdir())


    for file in files:
        with open(f"{file}", 'r') as f:
            data = f.read

main()