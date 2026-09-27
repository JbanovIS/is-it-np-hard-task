#!/usr/bin/env python3
import sys
import csv
from pathlib import Path


def fix_mojibake(text: str) -> str:
    """Восстанавливает русский текст при двойной кодировке UTF-8/CP1251."""
    if not isinstance(text, str):
        return text
    try:
        return text.encode("cp1251").decode("utf-8")
    except Exception:
        return text


def read_csv_safely(file_path: Path):
    encodings = ["utf-8-sig", "utf-8", "cp1251", "latin-1"]
    for enc in encodings:
        try:
            with open(file_path, mode="r", encoding=enc) as f:
                sample = f.read(4096)
                f.seek(0)
                delimiter = ";" if ";" in sample else ","
                reader = csv.DictReader(f, delimiter=delimiter)
                raw_rows = list(reader)
                fieldnames = reader.fieldnames or []

                if any("Р" in fld or "в„" in fld for fld in fieldnames):
                    fixed_fieldnames = [fix_mojibake(fld) for fld in fieldnames]
                    fixed_rows = []
                    for r in raw_rows:
                        fixed_r = {fix_mojibake(k): fix_mojibake(v) for k, v in r.items()}
                        fixed_rows.append(fixed_r)
                    return fixed_rows, fixed_fieldnames

                return raw_rows, fieldnames
        except UnicodeDecodeError:
            continue

    raise UnicodeDecodeError("utf-8", b"", 0, 1, f"Не удалось прочитать {file_path.name}")


def main():
    root = Path(__file__).resolve().parent.parent
    results_dir = root / "results"
    review_path = results_dir / "review.md"
    claims_path = results_dir / "claims.csv"

    # Проверка 0: наличие файлов в results/
    if not results_dir.is_dir():
        print(f"Ошибка: директория {results_dir.name} не найдена")
        sys.exit(1)

    if not review_path.is_file():
        print(f"Ошибка: файл results/{review_path.name} не найден")
        sys.exit(1)

    if not claims_path.is_file():
        print(f"Ошибка: файл results/{claims_path.name} не найден")
        sys.exit(1)

    if review_path.stat().st_size == 0:
        print("Ошибка: файл results/review.md пуст")
        sys.exit(1)

    # Чтение данных
    try:
        rows, fieldnames = read_csv_safely(claims_path)
    except Exception as e:
        print(f"Ошибка при чтении results/claims.csv: {e}")
        sys.exit(1)

    if not rows:
        print("Ошибка: в results/claims.csv отсутствуют строки с данными")
        sys.exit(1)

    # Привязка колонок строго по их индексам в структуре шаблона
    col_line = fieldnames[0]
    col_claim = fieldnames[1]
    col_claim_proof = fieldnames[2]
    col_ref_proof = fieldnames[5] if len(fieldnames) > 5 else fieldnames[-1]

    # 1. Поиск строки 299
    row_299 = None
    for r in rows:
        val = str(r.get(col_line, "")).strip()
        if val == "299":
            row_299 = r
            break

    if not row_299:
        print("Ошибка: строка с нужным номером не найдена в таблице")
        sys.exit(1)

    # Проверка значений в строке 299
    claim_299 = str(row_299.get(col_claim, ""))
    c_proof_299 = str(row_299.get(col_claim_proof, "")).strip().lower()
    r_proof_299 = str(row_299.get(col_ref_proof, "")).strip().lower()

    if "np-hard" not in claim_299.lower():
        print(f"Ошибка: в нужной строке в столбце утверждения нет подстроки 'NP-hard'. Значение: '{claim_299}'")
        sys.exit(1)

    if "нет" not in c_proof_299:
        print(f"Ошибка в нужной строке: доказательство в утверждении '{c_proof_299}', ожидалось 'нет'")
        sys.exit(1)

    if "нет" not in r_proof_299:
        print(f"Ошибка в нужной строке: доказательство в ссылках '{r_proof_299}', ожидалось 'нет'")
        sys.exit(1)

    # 2. Проверка, что во всех строках таблицы стоит строго "нет"
    for idx, row in enumerate(rows, start=1):
        line_num = row.get(col_line, f"#{idx}")
        c_proof = str(row.get(col_claim_proof, "")).strip().lower()
        r_proof = str(row.get(col_ref_proof, "")).strip().lower()

        if "нет" not in c_proof:
            print(f"Ошибка в строке {line_num}: в столбце доказательства утверждения указано '{c_proof}', ожидалось 'нет'")
            sys.exit(1)

        if "нет" not in r_proof:
            print(f"Ошибка в строке {line_num}: в столбце доказательства по ссылкам указано '{r_proof}', ожидалось 'нет'")
            sys.exit(1)

    print("Проверка пройдена успешно: все критерии соблюдены (код 0)")
    sys.exit(0)


if __name__ == "__main__":
    main()