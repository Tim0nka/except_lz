import os
import pandas as pd

class Provero4ka:
    def __init__(self, file, columns, types):
        self.file = file
        self.columns = columns
        self.types = types

    def check(self):
        if not os.path.exists(self.file):
            raise FileNotFoundError(f"Ошибка: Файл {self.file} не найден.")

    def load(self):
        try:
            df = pd.read_csv(self.file)
            if df.empty:
                raise ValueError("Ошибка: Файл пуст.")
            return df
        except pd.errors.EmptyDataError:
            raise ValueError("Ошибка: Файл пуст.")
        except pd.errors.ParserError:
            raise RuntimeError("Ошибка: Неверный формат файла.")
        except Exception as e:
            raise RuntimeError(f"Ошибка загрузки: {str(e)}")

    def structure(self, df):
        actual_cols = df.columns.tolist()
        if actual_cols != self.columns:
            raise ValueError(f"Ошибка: Ожидались {self.columns}, получены {actual_cols}")

        for col, expected_type in self.types.items():
            if col in df.columns:
                actual_type = str(df[col].dtype)
                if actual_type != expected_type:
                    raise TypeError(f"Ошибка: Столбец '{col}' — ожидался {expected_type}, получен {actual_type}")

    def process(self):
        self.check()
        df = self.load()
        self.structure(df)
        print("Файл проверен успешно.")
