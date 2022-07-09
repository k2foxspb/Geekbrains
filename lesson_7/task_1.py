import os


def add_dir(director, *args):
    directory_add = os.path.join(director, *args)
    if not os.path.exists(directory_add):
        os.makedirs(directory_add)


dict_add = ('my_project', 'settings', 'mainapp', 'admin_app', 'auth_app')

for i in range(len(dict_add)):
    add_dir(dict_add[0], dict_add[i])
    
