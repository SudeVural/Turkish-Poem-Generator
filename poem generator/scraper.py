from requests import get
from bs4 import BeautifulSoup

urls = ["https://www.antoloji.com/ozdemir-asaf/siirleri/",
        "https://www.antoloji.com/ozdemir-asaf/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/ozdemir-asaf/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/ozdemir-asaf/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/ozdemir-asaf/siirleri/ara-/sirala-/sayfa-5/",
        "https://www.antoloji.com/ozdemir-asaf/siirleri/ara-/sirala-/sayfa-6/",
        "https://www.antoloji.com/ozdemir-asaf/siirleri/ara-/sirala-/sayfa-7/",
        "https://www.antoloji.com/ozdemir-asaf/siirleri/ara-/sirala-/sayfa-8/",
        "https://www.antoloji.com/ozdemir-asaf/siirleri/ara-/sirala-/sayfa-9/",
        "https://www.antoloji.com/ozdemir-asaf/siirleri/ara-/sirala-/sayfa-10/",
        "https://www.antoloji.com/ozdemir-asaf/siirleri/ara-/sirala-/sayfa-11/",
        "https://www.antoloji.com/ozdemir-asaf/siirleri/ara-/sirala-/sayfa-12/",
        "https://www.antoloji.com/orhan-veli-kanik/siirleri/",
        "https://www.antoloji.com/orhan-veli-kanik/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/orhan-veli-kanik/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/orhan-veli-kanik/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/orhan-veli-kanik/siirleri/ara-/sirala-/sayfa-5/",
        "https://www.antoloji.com/didem-madak/siirleri/",
        "https://www.antoloji.com/ahmet-telli/siirleri/",
        "https://www.antoloji.com/ahmet-telli/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/ahmet-telli/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/ahmet-telli/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/ahmet-telli/siirleri/ara-/sirala-/sayfa-5/",
        "https://www.antoloji.com/ataol-behramoglu/siirleri/",
        "https://www.antoloji.com/can-yucel/siirleri/",
        "https://www.antoloji.com/can-yucel/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/can-yucel/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/can-yucel/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/can-yucel/siirleri/ara-/sirala-/sayfa-5/",
        "https://www.antoloji.com/can-yucel/siirleri/ara-/sirala-/sayfa-6/"
        "https://www.antoloji.com/arif-nihat-asya/siirleri/",
        "https://www.antoloji.com/arif-nihat-asya/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/melih-cevdet-anday/siirleri/",
        "https://www.antoloji.com/melih-cevdet-anday/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/melih-cevdet-anday/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/cahit-zarifoglu/siirleri/",
        "https://www.antoloji.com/cahit-zarifoglu/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/cahit-zarifoglu/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/cahit-zarifoglu/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/cahit-zarifoglu/siirleri/ara-/sirala-/sayfa-5/",
        "https://www.antoloji.com/nurullah-genc/siirleri/",
        "https://www.antoloji.com/sabahattin-ali/siirleri/",
        "https://www.antoloji.com/sabahattin-ali/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/serkan-okce/siirleri/",
        "https://www.antoloji.com/serkan-okce/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/serkan-okce/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/serkan-okce/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/serkan-okce/siirleri/ara-/sirala-/sayfa-5/",
        "https://www.antoloji.com/serkan-okce/siirleri/ara-/sirala-/sayfa-6/",
        "https://www.antoloji.com/serkan-okce/siirleri/ara-/sirala-/sayfa-7/",
        "https://www.antoloji.com/serkan-okce/siirleri/ara-/sirala-/sayfa-8/",
        "https://www.antoloji.com/ozan-deniz-saritop/siirleri/",
        "https://www.antoloji.com/ozan-deniz-saritop/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/ozan-deniz-saritop/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/ozan-deniz-saritop/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/ozan-deniz-saritop/siirleri/ara-/sirala-/sayfa-5/",
        "https://www.antoloji.com/ozan-deniz-saritop/siirleri/ara-/sirala-/sayfa-6/",
        "https://www.antoloji.com/ahmet-kutsi-tecer/siirleri/",
        "https://www.antoloji.com/ahmet-kutsi-tecer/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/cigdem-sezer/siirleri/",
        "https://www.antoloji.com/sennur-sezer/siirleri/",
        "https://www.antoloji.com/nilgun-marmara/siirleri/",
        "https://www.antoloji.com/can-dundar/siirleri/",
        "https://www.antoloji.com/can-dundar/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/birhan-keskin/siirleri/",
        "https://www.antoloji.com/birhan-keskin/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/birhan-keskin/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/inci-asena/siirleri/",
        "https://www.antoloji.com/melisa-gurpinar/siirleri/",
        "https://www.antoloji.com/zerrin-taspinar/siirleri/",
        "https://www.antoloji.com/ayten-mutlu/siirleri/",
        "https://www.antoloji.com/ayten-mutlu/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/leyla-sahin/siirleri/",
        "https://www.antoloji.com/arife-kalender/siirleri/",
        "https://www.antoloji.com/aysel-gurel/siirleri/",
        "https://www.antoloji.com/sunay-akin/siirleri/",
        "https://www.antoloji.com/orhan-veli-kanik/siirleri/",
        "https://www.antoloji.com/neset-ertas/siirleri/",
        "https://www.antoloji.com/ahmet-telli/siirleri/",
        "https://www.antoloji.com/ahmet-telli/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/ahmet-telli/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/ahmet-telli/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/ahmet-telli/siirleri/ara-/sirala-/sayfa-5/",
        "https://www.antoloji.com/nurten-isilak/siirleri/",
        "https://www.antoloji.com/zeynep-nilgun-gokceoz/siirleri/",
        "https://www.antoloji.com/zeynep-nilgun-gokceoz/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/zeynep-nilgun-gokceoz/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/zeynep-nilgun-gokceoz/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/zeynep-nilgun-gokceoz/siirleri/ara-/sirala-/sayfa-5/",
        "https://www.antoloji.com/zeynep-nilgun-gokceoz/siirleri/ara-/sirala-/sayfa-6/",
        "https://www.antoloji.com/zeynep-nilgun-gokceoz/siirleri/ara-/sirala-/sayfa-7/",
        "https://www.antoloji.com/zeynep-nilgun-gokceoz/siirleri/ara-/sirala-/sayfa-8/",
        "https://www.antoloji.com/zeynep-nilgun-gokceoz/siirleri/ara-/sirala-/sayfa-9/",
        "https://www.antoloji.com/zeynep-nilgun-gokceoz/siirleri/ara-/sirala-/sayfa-10/",
        "https://www.antoloji.com/zeynep-nilgun-gokceoz/siirleri/ara-/sirala-/sayfa-11/",
        "https://www.antoloji.com/zeynep-nilgun-gokceoz/siirleri/ara-/sirala-/sayfa-12/",
        "https://www.antoloji.com/hulya-arda/siirleri/",
        "https://www.antoloji.com/hulya-arda/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/emine-tokgoz/siirleri/ara-/sirala-/",
        "https://www.antoloji.com/canan-akpinar/siirleri/",
        "https://www.antoloji.com/canan-akpinar/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/canan-akpinar/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/canan-akpinar/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/saniye-sarsilmaz/siirleri/",
        "https://www.antoloji.com/selma-sengoren/siirleri/",
        "https://www.antoloji.com/selma-sengoren/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/selma-sengoren/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/selma-sengoren/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/selma-sengoren/siirleri/ara-/sirala-/sayfa-5/",
        "https://www.antoloji.com/selma-sengoren/siirleri/ara-/sirala-/sayfa-6/",
        "https://www.antoloji.com/yusuf-hayaloglu/siirleri/",
        "https://www.antoloji.com/yusuf-hayaloglu/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/yusuf-hayaloglu/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/cezmi-ersoz/siirleri/",
        "https://www.antoloji.com/cezmi-ersoz/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/cezmi-ersoz/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/cezmi-ersoz/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/cezmi-ersoz/siirleri/ara-/sirala-/sayfa-5/",
        "https://www.antoloji.com/erdem-bayazit/siirleri/",
        "https://www.antoloji.com/erdem-bayazit/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/mehmet-akif-inan/siirleri/",
        "https://www.antoloji.com/alaeddin-ozdenoren/siirleri/",
        "https://www.antoloji.com/gonca-ozmen/siirleri/",
        "https://www.antoloji.com/nilay-ozer/siirleri/",
        "https://www.antoloji.com/halim-yazici/siirleri/",
        "https://www.antoloji.com/ahmet-ada/siirleri/",
        "https://www.antoloji.com/ahmet-ada/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/ahmet-ada/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/ahmet-ada/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/salih-bolat/siirleri/",
        "https://www.antoloji.com/salih-bolat/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/feyzi-halici/siirleri/",
        "https://www.antoloji.com/abdullah-tukay/siirleri/",
        "https://www.antoloji.com/abdullah-tukay/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/sedat-umran-1/siirleri/",
        "https://www.antoloji.com/sedat-umran-1/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/asik-reyhani/siirleri/",
        "https://www.antoloji.com/asik-ihsani/siirleri/",
        "https://www.antoloji.com/sadettin-kaplan/siirleri/",
        "https://www.antoloji.com/sadettin-kaplan/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/sadettin-kaplan/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/sadettin-kaplan/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/sadettin-kaplan/siirleri/ara-/sirala-/sayfa-5/",
        "https://www.antoloji.com/sadettin-kaplan/siirleri/ara-/sirala-/sayfa-6/",
        "https://www.antoloji.com/sadettin-kaplan/siirleri/ara-/sirala-/sayfa-7/",
        "https://www.antoloji.com/ali-puskulluoglu/siirleri/",
        "https://www.antoloji.com/ferman-karacam/siirleri/",
        "https://www.antoloji.com/ferman-karacam/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/ferman-karacam/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/afsar-timucin/siirleri/",
        "https://www.antoloji.com/afsar-timucin/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/afsar-timucin/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/afsar-timucin/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/osman-konuk/siirleri/",
        "https://www.antoloji.com/akgun-akova/siirleri/",
        "https://www.antoloji.com/akgun-akova/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/akgun-akova/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/omer-bedrettin-usakli/siirleri/",
        "https://www.antoloji.com/naime-ozeren/siirleri/",
        "https://www.antoloji.com/naime-ozeren/siirleri/ara-/sirala-/sayfa-2/",
        "https://www.antoloji.com/naime-ozeren/siirleri/ara-/sirala-/sayfa-3/",
        "https://www.antoloji.com/naime-ozeren/siirleri/ara-/sirala-/sayfa-4/",
        "https://www.antoloji.com/naime-ozeren/siirleri/ara-/sirala-/sayfa-5/",
        "https://www.antoloji.com/ayten-ozgun/siirleri/",
        "https://www.antoloji.com/ayten-ozgun/siirleri/ara-/sirala-/sayfa-2/",




        ]
root = "https://www.antoloji.com"

scraped = {}
for url in urls:
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    poems_list = soup.find_all('div', attrs={'class': 'list-poem-1'})
    for poem in poems_list:
        scraped[poem.a['title']] = poem.a['href']

for title in scraped:
    page = get(f"{root}{scraped[title]}")
    soup = BeautifulSoup(page.text, 'html.parser')
    verse_list = soup.find('div', attrs={'class': 'pd-text'}).findAll('p')
    with open(f"all_poems.txt", 'a', encoding='utf-8') as f:
        for verse in verse_list:
            f.write(verse.getText() + "\n")

with open('all_poems.txt', 'r', encoding='utf-8') as fin, open('cleaned_poems.txt', 'a', encoding='utf-8') as fout:
    for line in fin:
        fout.write(line)
