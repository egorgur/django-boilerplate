import yaml


def yaml_coerce(yaml_string: str):
    """Convert the yaml-settings to Python."""
    if isinstance(yaml_string, str):
        return yaml.load(f"dummy: {yaml_string}", Loader=yaml.SafeLoader)["dummy"]

    return yaml_string
