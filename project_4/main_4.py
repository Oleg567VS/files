import os
import hashlib
from collections import defaultdict
from pathlib import Path

def hash_file(path: Path, chunk_size: int = 4096) -> str:
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(root: Path) -> dict[str, list[Path]]:
    size_map = defaultdict(list)
    for file in root.rglob('*'):
        if file.is_file():
            size = file.stat().st_size
            size_map[size].append(file)
        duplicated = defaultdict(list)
        for size, files in size_map.items():
            if len(files) > 1:
                hash_map = defaultdict(list)
                for f in files:
                    try:
                        h = hash_file(f)
                        hash_map[h].append(f)
                    except (os.error, PermissionError) as e:
                        print(f"не удалось прочитать {f}: {e}")
                        continue
                    for h, group in hash_map.items():
                        if len(group) >1:
                            duplicated[h] = group
    return duplicated

if __name__ == "__main__":
    target_dir  = Path(__file__).parent
    if not target_dir.is_dir():
        print(f"ошибка: директория не существует: {target_dir}")
        exit(1)
    print(f"ищу дубликаты в: {target_dir.resolve()}\n")
    dups = find_duplicates(target_dir)
    
    if not dups:
        print("дубликатов не найдено.")
    else:
        print(f"найдено {len(dups)} групп дубликатов:\n")
        for i, (h, files) in enumerate(dups.items(), 1):
            print(f"группа #{i} (хеш: {h}):")
            for f in files:
                print(f"  • {f}")
            print()