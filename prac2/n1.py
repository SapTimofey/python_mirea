import pycodestyle

# E101 indentation contains mixed spaces and tabs
for _ in range(1):
    for _ in range(1):
        pass

# E111 indentation is not a multiple of four
for _ in range(1):
 pass

# E112 expected an indented block
if True:

# E121 continuation line under-indented for hanging indent
    print("err")

