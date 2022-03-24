def suffer(count):
    exec(f'from suffer import suffer as suffer{count}')
    exec(f'print(suffer.__name__)')
    exec(f'suffer{count}({count + 1})')


if __name__ == "__main__":
    suffer(0)
