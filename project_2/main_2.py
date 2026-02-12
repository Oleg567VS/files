import os
from collections import defaultdict

def analyze_directory(path):
    if not os.path.isdir(path):
        print(f"Ошибка: '{path}' не является существующей директорией.")
        return

    total_files = 0
    total_dirs = 0
    file_sizes = []
    ext_counter = defaultdict(int)

    for root, dirs, files in os.walk(path):
        total_dirs += len(dirs)
        total_files += len(files)

        for file in files:
            filepath = os.path.join(root, file)
            try:
                size = os.path.getsize(filepath)
                file_sizes.append((size, filepath))

                _, ext = os.path.splitext(file)
                ext = ext.lower() if ext else "(без расширения)"
                ext_counter[ext] += 1
            except (OSError, FileNotFoundError):
                continue

    print(f"\nОбщее количество файлов: {total_files}")
    print(f"Общее количество папок: {total_dirs}")

    print("\nТоп-5 самых больших файлов:")
    file_sizes.sort(reverse=True, key=lambda x: x[0])
    if file_sizes:
        for i, (size, filepath) in enumerate(file_sizes[:5], 1):
            print(f"{i}. {filepath} — {size:,} байт")
    else:
        print("Нет файлов для отображения.")

    print("\nКоличество файлов по расширениям:")
    sorted_ext = sorted(ext_counter.items(), key=lambda x: x[1], reverse=True)
    for ext, count in sorted_ext:
        print(f"{ext} — {count}")

if __name__ == "__main__":
    path = input("Введите путь к директории: ").strip()
    if not path:
        print("Путь не может быть пустым.")
    else:
        analyze_directory(path)

