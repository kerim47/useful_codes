import toml

class UniqueListManager:
    def __init__(self):
        self.config_data = None

    def load_config_file(self, config_file):
        self.config_data = toml.load(config_file)["usernames"]

    def get_variable_value(self, variable_name):
        if not self.config_data:
            raise ValueError("Konfigürasyon dosyası henüz yüklenmedi. 'load_config_file' fonksiyonunu kullanın.")

        if variable_name in self.config_data:
            return self.config_data[variable_name]
        return None

    def get_unique_values(self, file_path):
        unique_values = set()

        with open(file_path, 'r') as file:
            for line in file:
                value = line.strip()
                unique_values.add(value)
        return unique_values


    def format(self, unique_values_file):
        unique_values = self.get_unique_values(unique_values_file)
        new_list = set()
        for value in unique_values:
            if value.startswith("$"):
                value = value[1:]
                for value_in in self.config_data:
                    if value.startswith(value_in):
                        index = value.find("/")        
                        kesilen_kisim = value[:index]
                        sonraki_deger = value[index+1:]
                        modified_path = self.get_variable_value(kesilen_kisim) + sonraki_deger
                        new_list.add(modified_path)
            elif value.startswith("/"):
                new_list.add(value)
        return new_list
        # list(set(my_list))
    

    def run(self, config_file, unique_values_file):
        self.load_config_file(config_file)
        unique_values_set = self.format(unique_values_file)
        return unique_values_set

# def main():
#     toml_file = "usernames.toml"
#     unique_values_file = '_autojump.txt'

#     config_manager = ConfigManager()
#     print(config_manager.run(toml_file, unique_values_file))

# if __name__ == "__main__":
#     main()

