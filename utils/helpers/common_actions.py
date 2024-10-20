import os.path

from datetime import datetime, timedelta
from project_constants import project_path


class CommonActions(object):

    """
    All miscellaneous common actions
    """

    @staticmethod
    def strtobool(string):
        string = string.casefold()
        if string in ('y', 'yes', 't', 'true', 'on', '1'):
            return True
        elif string in ('n', 'no', 'f', 'false', 'off', '0'):
            return False
        else:
            raise ValueError(f"Invalid truth value: {string}")

    @staticmethod
    def get_time():
        """
        Returns the date and time
        @return: the date and time
        """
        return datetime.now()

    @staticmethod
    def get_date(date_format="%m/%d/%Y"):
        """
        Returns the date in format "%m/%d/%Y"
        @return: the date
        """
        today_date = datetime.now()
        return today_date.strftime(date_format)

    @staticmethod
    def get_new_year(date_format="%Y", time=365):
        """
        Returns the date in format "%Y"
        @return: the date
        """
        today_date = datetime.now()
        today_date.strftime(date_format)
        next_year = today_date + timedelta(days=time)
        return next_year.strftime(date_format)

    @staticmethod
    def get_path_to_file_names(file_names):
        full_path = ""
        if len(file_names) == 1:
            full_path = CommonActions.parse_file_extensions(file_names[0])
            return full_path
        list_paths = []
        for list_element in file_names:
            path_to_element = CommonActions.parse_file_extensions(list_element)
            list_paths.append(path_to_element)
            full_path = " \n ".join(list_paths)
        return full_path

    @staticmethod
    def parse_file_extensions(file_name):
        # Define the base test data folder
        path_to_test_data_folder = os.path.join(project_path, "test_data")

        # Extract file extension from the filename
        parsed_file_name = os.path.splitext(file_name)[1]

        # Dictionary mapping extensions to subfolder names
        extension_to_folder = {
            "pdf": "test_pdf",
            "png": "test_png"
        }

        # Use map to find the matching folder
        file_path = next(
            map(lambda ext: os.path.join(path_to_test_data_folder, extension_to_folder[ext], file_name),
                filter(lambda ext: ext in parsed_file_name, extension_to_folder)),
            ""
        )

        return file_path
