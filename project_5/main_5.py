import shutil
from pathlib import Path
import datetime
import sys

def create_backup(source_dir: str | Path) -> bool:
    source = Path(source_dir).resolve()
    if not source.is_dir():
        print(f"ошибка такрй директории нет")
        return False
    script_dir = Path(__file__).parent.resolve()
    backups_dir = script_dir / "backups"
    backups_dir.mkdir(exist_ok=True)
    today = datetime.date.today()
    archive_name = f"backup_{today.isoformat()}"
    archive_path = backups_dir / archive_name
    try:
        shutil.make_archive(
            base_name=str(archive_path),
            format='zip',
            root_dir=source.parent,
         base_dir=source.name
        ) 
        print(f"резервная копия создана: {archive_path}.zip")
        return True
    except Exception as e:
        print(f"ошибка при создании архива: {type(e).__name__}: {e}")
        return False
    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input(" укажи путь к папке для архивации: ").strip()
    create_backup(target)
       
        
