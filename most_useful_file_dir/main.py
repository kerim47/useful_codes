# Yazar  : Abdulkerim Akan
# Tarih  : Temmuz 2023
# E-posta: kerimakan77@gmail.com
# main.py: main.py

# description: Bu modul en cok kullanilan dizin ve dosyalarin autojump.txt dosyasında 
# saklanarak cdg anahtar kelimesi kullanarak hızlı erişimine yol açar.

import os
import subprocess
import argparse
import inspect

autojump_file = "/home/username/.autojump.txt"

def start(save_script):
    # Create the script file
    bash_profile_path = os.path.expanduser(save_script)
    with open(bash_profile_path, "a") as script_file:
        script_file.write('''
cdg() {
  local autojump_list="$HOME/.autojump.txt"
  local WIMHOME=$(wslpath "$(wslvar USERPROFILE)")
  local dest_dir=$(cat "$autojump_list" | sed "s|\$HOME|$HOME|g" |\
    sed "s|\$WINHOME|$WIMHOME|g"  | cut -d$'\t' -f 2 |\
    fzf --preview "if [[ -d {} ]]; then tree -L 1 {}; else less {}; fi")

  if [[ $dest_dir != '' ]]; then
    if [[ -d "$dest_dir" ]]; then
      cd "$dest_dir"
    else
      dir=$(dirname "$dest_dir")
      cd "$dir"
    fi
    if [[ "$1" == "l" ]]; then
      lvim "$dest_dir"
    fi

  fi
}

export -f cdg > /dev/null
    
    ''')

    # Execute the command in a new interactive shell
    cmd = 'source ' + save_script + ' && cdg'
    results = subprocess.run(["bash", "-i", "-c", cmd], universal_newlines=True, check=True)

def check_fzf_installed():
    try:
        subprocess.run(["fzf", "--version"], capture_output=True, text=True, check=True)
        return True
    except:
        return False



def main():
    parser = argparse.ArgumentParser(description="add bash script")
    parser.add_argument("-f", "--file", default="~/.bash_profile", help="Dosya adı")
    args = parser.parse_args()

    if not os.path.exists(autojump_file):
        with open(autojump_file, "w"):
            pass 

    if args.file:
        if  check_fzf_installed():
            start(args.file)
        else:
            raise subprocess.CalledProcessError("fzf not found on system")

    current_file_path = os.path.abspath(inspect.getfile(inspect.currentframe()))
    try:
        os.remove(current_file_path)
        print(f"File '{current_file_path}' has been successfully removed.")
    except FileNotFoundError:
        print(f"File '{current_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
   main()
