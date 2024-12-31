from pathlib import Path
import pandas as pd


def main():
    print("안녕하세요, GitHub Actions!")
    result = add_numbers(5, 7)
    print(f"5와 7을 더한 결과는: {result}")
    raise Exception()
    df = pd.DataFrame({"a": [1, 2, 3], "b": [5, 9, 8]})
    print(df)
    print(Path().cwd())
    print(Path().cwd())
    print(Path().cwd())


def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    main()
