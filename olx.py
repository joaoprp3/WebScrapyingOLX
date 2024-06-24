from parsel import Selector
import cloudscraper
import json

class OlxScraper:
    def __init__(self, carBrand = str, carModel = str, state = str, city=str):
        self.scraper = cloudscraper.create_scraper()
        self.carBrand = carBrand
        self.carModel = carModel
        self.state = state
        self.city = city

    def carfinder(self):
        i=0
        for page in range(1,11):
            r = self.scraper.get(f'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios{self.carBrand}{self.carModel}{self.state}?{self.city}o={page}')
            response = Selector(text = r.text)
            html = json.loads(response.xpath('//script[@id="__NEXT_DATA__"]/text()').get())
            cars = html.get('props').get('pageProps').get('ads')
            for car in cars:
                if 'subject' in car:
                    i +=1
                    print({
                        'title' : car.get('title'),
                        'price' : car.get('price'),
                        'locations' : car.get('location'),
                        'image' : car.get('images')[0].get('original')
                    })


dictStates = {
    "ac" : '/estado-ac',
    "al" : '/estado-al',
    "ap" : '/estado-ap',
    "am" : '/estado-am',
    "ba" : '/estado-ba',
    "ce" : '/estado-ce',
    "df" : '/estado-df',
    "es" : '/estado-es',
    "go" : '/estado-go',
    "ma" : '/estado-ma',
    "mt" : '/estado-mt',
    "ms" : '/estado-ms',
    "mg" : '/estado-mg',
    "pa" : '/estado-pa',
    "pb" : '/estado-pb',
    "pr" : '/estado-pr',
    "pe" : '/estado-pe',
    "pi" : '/estado-pi',
    "rj" : '/estado-rj',
    "rn" : '/estado-rn',
    "rs" : '/estado-rs',
    "ro" : '/estado-ro',
    "rr" : '/estado-rr',
    "sc" : '/estado-sc',
    "sp" : '/estado-sp',
    "se" : '/estado-se',
    "to" : '/estado-to'
}

dictBrands = {
    'Citroën' : "/citroen",
    'Fiat' : "/fiat",
    'Ford' : "/ford",
    'GM - Chevrolet' : "/gm-chevrolet",
    'Honda' : "/honda",
    'Hyundai' : "/hyundai",
    'JAC' : "/jac",
    'Kia Motors' : "/kia-motors",
    'Nissan' : "/nissan",
    'Peugeot' : "/peugeot",
    'Renault' : "/renault",
    'Toyota' : "/toyota",
    'VW - VolksWagen' : "/vw-volkswagen",
    'Acura' : "/acura",
    'Agrale' : "/agrale",
    'Alfa Romeo' : "/alfa-romeo",
    'AM Gen' : "/am-gen",
    'Asia Motors' : "/asia-motors",
    'ASTON MARTIN' : "/aston-martin",
    'Audi' : "/audi",
    'BMW' : "/bmw",
    'BRM' : "/brm",
    'Buggy' : "/buggy",
    'Bugre' : "/bugre",
    'Cadillac' : "/cadillac",
    'CBT Jipe' : "/cbt-jipe",
    'CHANA' : "/chana",
    'CHANGAN' : "/changan",
    'CHERY' : "/chery",
    'Chrysler' : "/chrysler",
    'Cross Lander' : "/cross-lander",
    'Daewoo' : "/daewoo",
    'Daihatsu' : "/daihatsu",
    'Dkw Vemag' : "/dkw-vemag",
    'Dodge' : "/dodge",
    'EFFA' : "/effa",
    'Engesa' : "/engesa",
    'Envemo' : "/envemo",
    'Ferrari' : "/ferrari",
    'Fibravan' : "/fibravan",
    'FOTON' : "/foton",
    'Fyber' : "/fyber",
    'GEELY' : "/geely",
    'GREAT WALL' : "/great-wall",
    'Gurgel' : "/gurgel",
    'HAFEI' : "/hafei",
    'Infiniti' : "/infiniti",
    'Isuzu' : "/isuzu",
    'Jaguar' : "/jaguar",
    'Jeep' : "/jeep",
    'JINBEI' : "/jinbei",
    'JPX' : "/jpx",
    'Lada' : "/lada",
    'LAMBORGHINI' : "/lamborghini",
    'Land Rover' : "/land-rover",
    'Landwind' : "/landwind",
    'Lexus' : "/lexus",
    'LIFAN' : "/lifan",
    'LOBINI' : "/lobini",
    'Lotus' : "/lotus",
    'Mahindra' : "/mahindra",
    'Maserati' : "/maserati",
    'Matra' : "/matra",
    'Mazda' : "/mazda",
    'Mercedes-Benz' : "/mercedes-benz",
    'Mercury' : "/mercury",
    'MG' : "/mg",
    'MINI' : "/mini",
    'Mitsubishi' : "/mitsubishi",
    'Miura' : "/miura",
    'Plymouth' : "/plymouth",
    'Pontiac' : "/pontiac",
    'Porsche' : "/porsche",
    'Puma' : "/puma",
    'RAM' : "/ram",
    'RELY' : "/rely",
    'Rolls-Royce' : "/rolls-royce",
    'Rover' : "/rover",
    'Saab' : "/saab",
    'Saturn' : "/saturn",
    'Seat' : "/seat",
    'SHINERAY' : "/shineray",
    'smart' : "/smart",
    'SSANGYONG' : "/ssangyong",
    'Subaru' : "/subaru",
    'Suzuki' : "/suzuki",
    'TAC' : "/tac",
    'Troller' : "/troller",
    'Volvo' : "/volvo",
    'Wake' : "/wake",
    'Walk' : "/walk",
    'Tesla' : "/tesla",
    'Bentley' : "/bentley",
    'MCLaren' : "/mclaren",
    'Iveco' : "/iveco"
}
carro = ""
find = OlxScraper(carro)
OlxScraper(carro).carfinder()