from dotenv import find_dotenv, load_dotenv

__env_file = find_dotenv()
load_dotenv(__env_file)


def get_chromedriver_path():
    from os import environ

    return environ['CHROMEDRIVER_PATH']
