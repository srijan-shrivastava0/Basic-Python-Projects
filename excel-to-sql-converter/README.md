# Excel to SQL Converter 🧾➡️💻

This script converts Excel `.xlsx` files into SQL `INSERT` statements using Python.

## Features
- Supports all Excel rows
- Outputs SQL file with `INSERT` statements
- Easy to modify table or sheet name

## Usage

```bash
pip install -r requirements.txt
python excel_to_sql.py
```

## Example

**Excel Input**:
| id | name   | age |
|----|--------|-----|
| 1  | Alice  | 22  |
| 2  | Bob    | 25  |
| 3  | Charlie | 30 |

**SQL Output**:
```sql
INSERT INTO students VALUES ('1', 'Alice', '22');
INSERT INTO students VALUES ('2', 'Bob', '25');
INSERT INTO students VALUES ('3', 'Charlie', '30');
```
