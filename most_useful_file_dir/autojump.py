import os
import toml
import argparse

from uniqueManager import UniqueListManager as ULM


class AutoJump:
    def __init__(self, save_file, files):

        self.config_manager  = ULM()
        self.autojump_file = save_file
        self.toml_file = "usernames.toml"
        self.unformatted_files = files
        self.formatted_files = []
        self.jump_files = []
        self.read_file_status = True

        if not os.path.exists(self.autojump_file):
            with open(save_file, "w"):
                pass 

        if not os.path.exists(self.toml_file):
            with open(self.toml_file, "w"):
                pass  

    def write_to_file(self, file, open_text_mode="w", message="", end = '\n'):
        with open(file, open_text_mode) as f:
            f.write(message + end)

    def read_file(self):
        lines = []
        with open(self.autojump_file, "r") as f:
            for line in f:
                lines.append(line.strip())
        return lines

    def get_formatted_files(self):
        return self.formatted_files

    def load_usernames(self):
        with open(self.toml_file, "r") as f:
            return toml.load(f)["usernames"]

    def format_path(self, path):
        for key, value in self.load_usernames().items():
            if path.startswith(value):
                if path.endswith("/"):
                    new_path = path.replace(value, f"${key}/")
                    return new_path
                else:
                    new_path = path.replace(value, f"${key}/") + "/"
                    return new_path

    def check_file_or_dir_exists(self, path):
        if os.path.isdir(path):
            return 1
        elif os.path.isfile(path):
            return -1
        return 0

    def check_in_path(self, file):
        if self.read_file_status:
            self.jump_files = self.read_file()
            self.read_file_status = False

        if file in self.jump_files:
            return True
        return False

    def is_equal(self, current_file, new_file)->bool:
        s_current_file = current_file.strip()
        s_new_file     = new_file.strip()

        return( (s_current_file == new_file or (s_current_file + "/") == new_file )
                (s_new_file     == new_file or (s_new_file     + "/") == new_file ))

    def check_and_add_to_autojump(self):
        for value in self.unformatted_files: 
            format_value_path = str(self.format_path(value))
            self.formatted_files.append(format_value_path)

            if self.check_in_path(value) or self.check_in_path(format_value_path):
                print("[[WARN]] " +  value + " zaten " + self.autojump_file +" dosyasında bulunuyor.")
                continue
            if self.check_file_or_dir_exists(value) == 1:
                self.write_to_file(self.autojump_file, "a", format_value_path)
            elif self.check_file_or_dir_exists(value) == -1:
                self.write_to_file(self.autojump_file, "a", format_value_path[:-1])
            else:
                print("[[WARN]] Boyle bir dosya veya yol bulunamadi.")

    def set_autojump_file_unique(self):
        unique_list = self.config_manager.run(self.toml_file, self.autojump_file)
        result = ""
        for value in unique_list:
            if not None:
                if self.check_file_or_dir_exists(value) == 1:
                    result += str(self.format_path(value)) + "\n"
                elif self.check_file_or_dir_exists(value) == -1:
                    result += str(self.format_path(value[:-1])) + "\n"

    def show_info(self):
        lines = self.config_manager.run(self.toml_file, self.autojump_file)
        for value in lines:
            if self.check_file_or_dir_exists(value) == 1:
                print(f"Directory : {value}")
            elif self.check_file_or_dir_exists(value) == -1:
                print(f"File      : {value}")
            else:
                print(f"None      : {value}")

def main():
    parser = argparse.ArgumentParser(description="Autojump tool")
    parser.add_argument("-f", "--file", default="_autojump.txt", help="Dosya adı")
    parser.add_argument("-p", "--path", nargs="+", help="Yolu girin")
    parser.add_argument("-s", "--show", action="store_true", help="Argumant dosyasını unique yap")
    parser.add_argument("-u", "--unique", action="store_true", help="Argumant dosyasını unique yap")
    args = parser.parse_args()

    autojump = AutoJump(args.file, args.path)
    if args.path:
        autojump.check_and_add_to_autojump()
    if args.unique:
        autojump.set_autojump_file_unique()
    if args.show:
        autojump.show_info()

if __name__ == "__main__":
    main()

