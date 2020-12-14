EMAIL = ""
PASS = ""

try:
    from config_local import EMAIL, PASS
except ModuleNotFoundError:
    print("No local settings")
