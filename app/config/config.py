import tomllib
from pathlib import Path



# TOML configuration
CONFIG_PATH = Path(__file__).resolve().parent / "mainConfig.toml"

try:
    with CONFIG_PATH.open("rb") as f:
        CONFIG = tomllib.load(f)

except FileNotFoundError:
    raise RuntimeError(f"Configuration file not found: {CONFIG_PATH}")

except tomllib.TOMLDecodeError as e:
    raise RuntimeError(f"Invalid TOML in '{CONFIG_PATH}': {e}")

except PermissionError:
    raise RuntimeError(f"Permission denied reading '{CONFIG_PATH}'")

except OSError as e:
    raise RuntimeError(f"Unable to load configuration: {e}")

