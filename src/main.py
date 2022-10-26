import sys

from aiogram import executor


def change_token(token):
    with open("config.py", "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith("API_TOKEN"):
                lines[i] = f"API_TOKEN = {token}\n"
    with open("config.py", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    try:
        is_test = sys.argv[1]
    except IndexError:
        is_test = ""

    if is_test == "test":
        change_token("TEST_TOKEN")
    else:
        change_token("PROD_TOKEN")

    import config
    import dialogs
    import handlers

    executor.start_polling(
        config.dp,
        skip_updates=True,
    )
