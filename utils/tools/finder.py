import os

from project_constants import project_path


class Find:

    @staticmethod
    def file_folder(file_name):
        """
        Find folder name for given file
        :param file_name: Name of the file
        :return: folder name where the file_name is
        """

        abs_path_to_file = None

        for root, directory, files in os.walk(project_path):
            for file in files:
                if file == file_name:
                    abs_path_to_file = os.path.join(root)

        folder_path, folder_name = os.path.split(abs_path_to_file)

        return folder_name
