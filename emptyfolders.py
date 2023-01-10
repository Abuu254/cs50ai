Import os

// get root folder

root = input("Provide directory to search: ")
save = input("Where to save the empty folder: ")

// storing empty directories

empty = []

for root, dirs, files in os.walk(root):

// check size
   if not len(dir) and not len(files):
      empty.append(root)


// Writing to file
file_name = 'empty.txt'
with open(os.path.join(save, file_name), 'w') as fp:
   fp.write('\n'.join(empty))




