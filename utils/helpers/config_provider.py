import os
from configparser import ConfigParser
from project_constants import project_path


def __config_provider_builder(config_name):
    """
    Read all sections and values from ini file
    :param config_name: ini file name that stores in the project-directory
    :return: class with arguments (keys from ini file) and values (values from ini file)
    """
    config = ConfigParser()
    config_path = os.path.join(project_path, config_name)
    config.read(config_path)
    dictionary = {}
    # iterate over all sections in ini file, get all values from section
    for section in config:
        all_items = dict(config.items(section))
        for key, value in all_items.items():
            dictionary[key] = value

    dictionary["__setattr__"] = setattr
    return type("ConfigProvider", (), dictionary)


test_data_config = __config_provider_builder("test_data.ini")
settings_config = __config_provider_builder("config.ini")
