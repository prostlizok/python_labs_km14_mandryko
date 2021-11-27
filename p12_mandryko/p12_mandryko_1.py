dirs = [
    ( 'folder1',
        [
            'file1',
            ( 'folder2', 
                [
                    'file2',
                    'file3'
                ] 
            ),
            ( 'folder3', 
                [
                    'file3', 
                    'file4',
                    ('folder4', ['file3'])
                ] 
            ),
            'file5'
        ]
    )
]

a = []
def search(dirs, name):
    global a
    if name == "folder1":
        print(a)
    else:
        for i in range(len(dirs)):
            if type(dirs[i]) is tuple:
                a.append(f"/{dirs[i][0]}")
                search(dirs[i], name)  
            elif type(dirs[i]) is list:
                search(dirs[i], name)                   
            elif name == dirs[i]:
                a.append(name)
                a = "/".join(a)
                print(a, end=", ") 
                a=[]

search(dirs, "file1")

