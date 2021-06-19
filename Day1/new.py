with open("file3.txt", 'w') as test_out:
    for line in open("file2.txt", "r"):
        test_out.write('My line:' + line)