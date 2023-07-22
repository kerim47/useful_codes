## En Çok Kullanılanlar Listesine Hızlı Ulaşma

Bu program FuzzyFinder (fzf) programı tarafından aranan dosyaların aranma sıklığı nedeniyle
aramayı daha kolaylaştırmak adına oluşturulmuştur.

Fzf sisteminizde her zaman tüm dosyaları tarama sebebiyle performans açısından azalma görülebilmektedir.

cdg kullanarak en çok aranan dosyalar eklenerek ulaşabilme hızını artırmakta ve izlenmesi daha pratik 
hale getirilmiştir. 
Ayrıca önizleme ile dosyaların durumu hakkında bilgi alınabilmektedir.

**ŞUANDA DESTEKLENENLER**
- UNIX
- WSL (Windows Subsystem Linux)

## Kullanım 

Sisteminizde `fzf` programı olmalıdır. fzf programına ihtiyaç duymaktadır.


**Adımlar**

```bash
git clone https://github.com/kerim47/useful_codes.git
cd useful_codes
```


En çok kullanılanlar listesi $HOME/.autojump.txt dizinine eklenmektedir.
--file ya da -f ekleyerek cdg fonksiyonunu bash dosyanıza ekleyebilirsiniz.
Varsayılan olarak ~/.bash_profile olarak kaydedilmiştir.

```bash
python3 main.py --file BASH_PATH
```

`main.py` tekrar edilmesini engellemek adına kendini imha etmesi sağlanmıştır.


----------
### En Çok Kullanılanlar Listesine Hizli Ulaşma

Bu program FuzzyFinder (fzf) programı tarafından aranan dosyaların aranma sıklığı nedeniyle
aramayı daha kolaylaştırmak adına olusturulmustur.

Fzf sisteminizde her zaman tum dosyaları tarama sebebiyle performans açısından azalma gorulebilmektedir.

cdg kullanarak en çok aranan dosyalar eklenerek ulasabilme hizini artirmakta ve izlenmesi daha pratik 
hale getirilmistir. 
Ayrıca onizleme ile dosyaların durumu hakkında bilgi alinabilmektedir.

SUANDA DESTEKLENENLER 
`UNIX` & `WSL(Windows Subsystem Linux)`

## Kullanım 

Sisteminizde `fzf` programi olmalidir. fzf programina ihtiyac duymaktadir.

Adimlar
en çok kullanılanlar listesi `$HOME/.autojump.txt` dizinine eklenmektedir.
--file yada -f ekleyerek cdg fonksiyonunu bash dosyanıza ekleyebilirsiniz. 
varsayılan olarak `~/.bash_profile` olarak kaydedilmistir.

```bash
python3 main.py --file BASH_PATH
```

`main.py` tekrar edilmesini engellemek adina kendini imha edilmesi saglanmistir.

```bash
source BASH_PATH
```


cdg birinci argumanı `(l)vim` olarak olusturulmustur.  Degistirmek icin BASH_PATH 'i  text editoru ile açıp
daha sonrasında text editorunu degistirip ozelleştirebilirsiniz. 
```bash
if [[ "$1" == "l" ]]; then
      lvim "$dest_dir"
    fi
```

cdg ($1) yazarak en cok kullanilan dizinine ulasabilirsiniz.


cdg fonksiyonun en onemli ve guzel ozelliklerinden bir tanesi. `$HOME` ve `/home/username` ' nin cdg fonksiyonu çalıştığı zaman aynı adla ifade edilmesidir.

autojump dosyasında `$HOME` cdg fonksiyonu tarafından çalıştırıldığı zaman `/home/username` olarak gozukmesi dosyalar arasi guvenliği sağlamaktadir.

En guzel ikincisi ise `WSL(Windows Subsystem Linux)` desteklemesidir. Herhangi bir islem yapmadan sadece `WINHOME` diyerek dizinlerini ekleyebilirsiniz.


Bazı durumlarda autojump dosyasında eklediğimiz dosyalar /.../ ../ şeklinde ola biliyor ve dosyalarımizi paylaştığımız zaman sistemimiz hakkında kucuk bir
açık veriyor. Bu durumda yardımımıza yetişen autojump.py python dosyası var.

autojump.py dosyası tekrarı olan dosyalari, açık olan isimleri gibi işlemlerde yardimci olmaktadir.



autojump.py 
    "-f", "--file", default="_autojump.txt"
    "-p", "--path", 
    "-s", "--show", 
    "-u", "--unique", 


```bash
usage: autojump.py [-h] [-f FILE] [-p PATH [PATH ...]] [-s] [-u]

Autojump tool

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Dosya adı
  -p PATH [PATH ...], --path PATH [PATH ...]
                        Yolu girin
  -s, --show            Argumant dosyasını unique yap
  -u, --unique          Argumant dosyasını unique yap

```

`-f` en cok kullanilan path dosyaya ekler. varsayılan autojump.txt
`-p` autojump.txt dosyasına eklencek dizinleri belirtir.
`-s`, --show            Dosyalarin dizin, dosya ve hicbiri olup olmadigina bakar.
`-u`, --unique          Argumant dosyasını unique yap

[Example](https://github.com/kerim47/useful_codes/blob/main/most_useful_file_dir/example.png)

Ayrıca usernames.toml dosyasi dizinlere yoluna ihtiyac duyacaktir.

cdg bu ihtiyaclari karşilar ama python karsilamadigindan dolayi eklenmesi gereklidir.


Eğer bir sorununuz varsa sormaktan çekinmeyin.

