import os

# get root folder

given = input("Provide directory to search: ")
save = input("Where to save the empty folder: ")

# storing empty directories
empty = []

# check size of folders
for root, dirs, files in os.walk(given):
   if not len(dirs) and not len(files):
      empty.append(root)


# Writing to file
file_name = 'empty.txt'
with open(os.path.join(save, file_name), 'w') as fp:
   fp.write('\n'.join(empty))




