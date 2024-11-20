import os

def create_dirs():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dirs = [
        'src',
        'src/gui',
        'src/core',
        'src/utils'
    ]
    
    for d in dirs:
        path = os.path.join(base_dir, d)
        os.makedirs(path, exist_ok=True)
        init_file = os.path.join(path, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                pass

if __name__ == '__main__':
    create_dirs()
