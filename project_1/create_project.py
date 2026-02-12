import os
import sys
import shutil
def main():
    cwd = os.getcwd()
    templates_dir = os.path.join(cwd, 'templates')
    

    if not os.path.isdir(templates_dir):
        print('Нет папки templates')
        sys.exit(1)
        

    readme_src = os.path.join(templates_dir, 'README_template.txt')
    main_src = os.path.join(templates_dir, 'main.py')


    if not os.path.isfile(readme_src):
        print('Нет файла readme')
        sys.exit(1)
    

    if not os.path.isfile(main_src):
        print('Нет файла main')

    
    project_name = input()
    if not project_name:
        print('Название проекта не может быть пустым')
        sys.exit(1)
    
    project_path = os.path.join(cwd, project_name)


    if os.path.isdir(project_path):
        print('Такая папка уже существует')
        sys.exit(1)


    os.makedirs(os.path.join(project_path, 'src'))
    os.makedirs(os.path.join(project_name, 'data'))
    os.makedirs(os.path.join(project_name, 'docs'))


    shutil.copy2(readme_src, os.path.join(project_path, 'README_template.txt'))
    shutil.copy2(main_src, os.path.join(project_path, 'src', 'main.py'))

    for root, dirs, files in os.walk(project_path):

        print(root)

        for f in files:
            print(os.path.join(root, f))
    
    print("\nПроект успешно создан!")

if __name__ == "__main__":
    main()