## Githubtan Alt Dizinde Bulunan Dosyaları Silme

## Açıklama

Github'tan alt dizindeki dosyaları silmek istediğinizde bu Python betiği tam size göre! Sadece indirmek istediğiniz dizinin URL'sini yapıştırmanız yeterli.

Bu Python betiği, GitHub deposundan dosya veya dizin indirmek ve SVN ile işlemler gerçekleştirmek için kullanılabilir. 

## Kullanım:


```bash
git clone https://github.com/kerim47/useful_codes.git
cd useful_codes/DownloadSubDir
```

Betiği çalıştırırken aşağıdaki komut satırı argümanlarını kullanabilirsiniz:



```bash
python3 DownloadSubDirectory.py -r <github-repo-url> -d -s -sp <save-path> 
```

- `-r `  `--repo`     : GitHub deposunun URL'si
- `-d `  `--downrepo` : GitHub deposundan dosya veya dizin indirme işlemini belirtir (flag olarak kullanılır)
- `-sp`  `--savepath`: İndirilecek GitHub deposunun kaydedileceği yer (varsayılan kaydetme mevcut dizin)
- `-s `  `--show`     : GitHub deposundaki dosyaları ve dizinleri listeleyerek gösterir (flag olarak kullanılır)


---
*Eğer işinize yaradıysa lütfen projeyi ⭐️ ile işaretleyin!*
