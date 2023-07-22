import subprocess
import argparse

def has_svn():
    result = subprocess.run(["which", "svn", "-Y"], capture_output=True, text=True)

    if result.stdout:
        print("svn sisteminizde bulunuyor.")
        return True
    package_manager = "sudo apt install subversion"
    try:
        result = subprocess.run(package_manager.split())
        return True
    except:
        return False

def normalize_github_url(url):
    nesne_turleri = None
    nesne_turleri = ["tree", "blob", "commit"]
    
    for nesne in nesne_turleri:
        if f"{nesne}/" in url:
            nesne_turleri = nesne
            break
    
    if nesne_turleri is None:
        return url
    
    index_of_nesne = url.find(f"{nesne_turleri}/") + len(f"{nesne_turleri}/")
    index_of_first_slash = url.find("/", index_of_nesne)
    first_word = url[index_of_nesne:index_of_first_slash]
    output = url.replace(f"{nesne_turleri}/" + first_word, "trunk")
    return output

def reset():
    subprocess.run(["rm", "-rf", ".svn"],capture_output=True, text=True)

def show(repo_url):
    normalized_url = normalize_github_url(repo_url)
    result = subprocess.run(["svn", "ls", normalized_url],capture_output=True, text=True)

    lines = (result.stdout).strip().split('\n')

    for line in lines:
        print("├──", line)

def download_from_github_repo(repo_url, savepath="./"):
    normalized_url = normalize_github_url(repo_url)
    subprocess.run(["svn", "checkout", normalized_url, savepath],capture_output=True, text=True)
    reset()
    print("Download success")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GitHub deposundan dosya/dizin indirme")
    parser.add_argument("-r", "--repo", help="GitHub deposunun URL'si")
    parser.add_argument("-d", "--downrepo", action="store_true", help="Download")
    parser.add_argument("-sp", "--savepath", default="./", help="indirilecek GitHub deposunun URL'si")
    parser.add_argument("-s", "--show", action="store_true", help="List repo")
    args = parser.parse_args()

    if args.repo:
        if args.show:
            show(args.repo)
        if args.downrepo:
            download_from_github_repo(args.repo, args.savepath)
    else:
        print("lütfen indirilecek github deposunun url'sini belirtin. kullanim: python script.py -r <url>")

