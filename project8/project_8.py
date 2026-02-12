from pathlib import Path
import sys

def convert_txt_to_md(root_dir: str | Path, output_dir: str | Path | None = None) -> None:
    root = Path(root_dir).resolve()
    if not root.is_dir():
        print(f'ошибка: директория не существует: {root}')
        return
    
    if output_dir is None:
        output_dir = Path(__file__).parent / 'converted'
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    
    txt_files = list(root.rglob('*.txt'))
    
    if not txt_files:
        print(f'в директории {root} не найдено .txt файлов.')
        return
    
    print(f'найдено {len(txt_files)} .txt файлов. начинаю конвертацию...\n')
    
    converted = 0
    errors = 0
    
    for txt_path in txt_files:
        try:
            rel_path = txt_path.relative_to(root)
            md_rel_path = rel_path.with_suffix('.md')
            md_path = output_dir / md_rel_path
            md_path.parent.mkdir(parents=True, exist_ok=True)
            
            content = None
            for enc in ('utf-8', 'cp1251', 'latin-1'):
                try:
                    content = txt_path.read_text(encoding=enc)
                    break
                except UnicodeDecodeError:
                    continue
            
            if content is None:
                raise ValueError('не удалось определить кодировку файла')
            
            header = f'# {txt_path.stem}\n\n'
            md_content = header + content.strip() + '\n'
            
            md_path.write_text(md_content, encoding='utf-8')
            
            print(f'{rel_path} → {md_rel_path}')
            converted += 1
            
        except Exception as e:
            print(f'ошибка при обработке {txt_path}: {type(e).__name__}: {e}')
            errors += 1
    
    print(f'\n{"=" * 50}')
    print(f'успешно конвертировано: {converted}')
    print(f'ошибок: {errors}')
    print(f'результат сохранён в: {output_dir}')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        source = sys.argv[1]
    else:
        source = input('укажи путь к папке с .txt файлами: ').strip()
    
    convert_txt_to_md(source)