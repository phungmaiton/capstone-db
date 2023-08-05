from app import app
from models import db, User, City, Price, UserCity


if __name__ == "__main__":
    with app.app_context():
        City.query.delete()
        Price.query.delete()

        city1 = City(
            city_name="Johannesburg",
            state_code="",
            country_name="South Africa",
            exchange_rate={
                "EUR": 0.050937,
                "AUD": 0.083646,
                "USD": 0.056364,
                "CAD": 0.074231,
                "GBP": 0.043953,
                "SGD": 0.075069,
            },
            currency_code="ZAR",
            img="https://www.andbeyond.com/wp-content/uploads/sites/5/Johannesburg-Skyline.jpg",
        )

        db.session.add(city1)

        city2 = City(
            city_name="Cape Town",
            state_code="",
            country_name="South Africa",
            exchange_rate={
                "EUR": 0.050937,
                "AUD": 0.083646,
                "USD": 0.056364,
                "CAD": 0.074231,
                "GBP": 0.043953,
                "SGD": 0.075069,
            },
            currency_code="ZAR",
            img="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Aerial_View_of_Sea_Point%2C_Cape_Town_South_Africa.jpg/1200px-Aerial_View_of_Sea_Point%2C_Cape_Town_South_Africa.jpg",
        )

        db.session.add(city2)

        city3 = City(
            city_name="Durban",
            state_code="",
            country_name="South Africa",
            exchange_rate={
                "EUR": 0.050937,
                "AUD": 0.083646,
                "USD": 0.056364,
                "CAD": 0.074231,
                "GBP": 0.043953,
                "SGD": 0.075069,
            },
            currency_code="ZAR",
            img="https://freedomdestinations.co.uk/wp-content/uploads/Durban3.jpg",
        )

        db.session.add(city3)

        city4 = City(
            city_name="Cairo",
            state_code="",
            country_name="Egypt",
            exchange_rate={
                "EUR": 0.029,
                "AUD": 0.048,
                "USD": 0.032,
                "CAD": 0.043,
                "GBP": 0.025,
                "SGD": 0.043,
            },
            currency_code="EGP",
            img="https://ychef.files.bbci.co.uk/976x549/p07zy3y6.jpg",
        )

        db.session.add(city4)

        city5 = City(
            city_name="Alexandria",
            state_code="",
            country_name="Egypt",
            exchange_rate={
                "EUR": 0.029,
                "AUD": 0.048,
                "USD": 0.032,
                "CAD": 0.043,
                "GBP": 0.025,
                "SGD": 0.043,
            },
            currency_code="EGP",
            img="https://www.celebritycruises.com/blog/content/uploads/2021/12/things-to-do-in-alexandria-egypt-harbor-hero.jpg",
        )

        db.session.add(city5)

        city6 = City(
            city_name="Luxor",
            state_code="",
            country_name="Egypt",
            exchange_rate={
                "EUR": 0.029,
                "AUD": 0.048,
                "USD": 0.032,
                "CAD": 0.043,
                "GBP": 0.025,
                "SGD": 0.043,
            },
            currency_code="EGP",
            img="https://d3dqioy2sca31t.cloudfront.net/Projects/cms/production/000/029/509/original/8b9fd6c6bff69cc84d5e6a4d6471be34/egypt-luxor-temple.jpg",
        )

        db.session.add(city6)

        city7 = City(
            city_name="Nairobi",
            state_code="",
            country_name="Kenya",
            exchange_rate={
                "EUR": 0.0064,
                "AUD": 0.010,
                "USD": 0.0070,
                "CAD": 0.0093,
                "GBP": 0.0055,
                "SGD": 0.0094,
            },
            currency_code="KES",
            img="https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Colors_of_nairobi.jpg/640px-Colors_of_nairobi.jpg",
        )

        db.session.add(city7)

        city8 = City(
            city_name="Mombasa",
            state_code="",
            country_name="Kenya",
            exchange_rate={
                "EUR": 0.0064,
                "AUD": 0.010,
                "USD": 0.0070,
                "CAD": 0.0093,
                "GBP": 0.0055,
                "SGD": 0.0094,
            },
            currency_code="KES",
            img="https://www.momondo.com/rimg/dimg/bb/df/1ee25cb1-city-10373-16d954c9c0e.jpg?width=1366&height=768&xhint=1096&yhint=854&crop=true",
        )

        db.session.add(city8)

        city9 = City(
            city_name="Kisumu",
            state_code="",
            country_name="Kenya",
            exchange_rate={
                "EUR": 0.0064,
                "AUD": 0.010,
                "USD": 0.0070,
                "CAD": 0.0093,
                "GBP": 0.0055,
                "SGD": 0.0094,
            },
            currency_code="KES",
            img="https://hapakenya.com/wp-content/uploads/2018/07/Kisumu-City.jpg",
        )

        db.session.add(city9)

        city10 = City(
            city_name="Lagos",
            state_code="",
            country_name="Nigeria",
            exchange_rate={
                "EUR": 0.0011,
                "AUD": 0.0019,
                "USD": 0.0013,
                "CAD": 0.0017,
                "GBP": 0.00098,
                "SGD": 0.0017,
            },
            currency_code="NGN",
            img="https://www.awaytoafrica.com/wp-content/uploads/2020/06/nigeria-lagos-1.jpg",
        )

        db.session.add(city10)

        city11 = City(
            city_name="Abuja",
            state_code="",
            country_name="Nigeria",
            exchange_rate={
                "EUR": 0.0011,
                "AUD": 0.0019,
                "USD": 0.0013,
                "CAD": 0.0017,
                "GBP": 0.00098,
                "SGD": 0.0017,
            },
            currency_code="NGN",
            img="https://media.cnn.com/api/v1/images/stellar/prod/221028070729-nigeria-abuja-city-view-file-restricted.jpg?c=original",
        )

        db.session.add(city11)

        city12 = City(
            city_name="Kano",
            state_code="",
            country_name="Nigeria",
            exchange_rate={
                "EUR": 0.0011,
                "AUD": 0.0019,
                "USD": 0.0013,
                "CAD": 0.0017,
                "GBP": 0.00098,
                "SGD": 0.0017,
            },
            currency_code="NGN",
            img="https://facts.net/wp-content/uploads/2023/06/44-facts-about-kano-1688122304.jpeg",
        )

        db.session.add(city12)

        city13 = City(
            city_name="Casablanca",
            state_code="",
            country_name="Morocco",
            exchange_rate={
                "EUR": 0.093,
                "AUD": 0.15,
                "USD": 0.10,
                "CAD": 0.13,
                "GBP": 0.080,
                "SGD": 61.61,
            },
            currency_code="MAD",
            img="https://www.heatheronhertravels.com/wp-content/uploads/2014/05/casablanca-2807439_1920.jpg.webp",
        )

        db.session.add(city13)

        city14 = City(
            city_name="Marrakech",
            state_code="",
            country_name="Morocco",
            exchange_rate={
                "EUR": 0.093,
                "AUD": 0.15,
                "USD": 0.10,
                "CAD": 0.13,
                "GBP": 0.080,
                "SGD": 61.61,
            },
            currency_code="MAD",
            img="https://img.theculturetrip.com/wp-content/uploads/2021/05/marrakech-medina-jemaa-el-fna-square-fb64hw.jpg",
        )

        db.session.add(city14)

        city15 = City(
            city_name="Rabat",
            state_code="",
            country_name="Morocco",
            exchange_rate={
                "EUR": 0.093,
                "AUD": 0.15,
                "USD": 0.10,
                "CAD": 0.13,
                "GBP": 0.080,
                "SGD": 61.61,
            },
            currency_code="MAD",
            img="https://content.r9cdn.net/rimg/dimg/d5/e5/012dfb42-city-12211-165b4a5fb55.jpg?width=1366&height=768&xhint=1405&yhint=1178&crop=true",
        )

        db.session.add(city15)

        city16 = City(
            city_name="Tokyo",
            state_code="",
            country_name="Japan",
            exchange_rate={
                "EUR": 0.0064,
                "AUD": 0.010,
                "USD": 0.0071,
                "CAD": 0.0093,
                "GBP": 0.0055,
                "SGD": 0.0094,
            },
            currency_code="JPY",
            img="https://media.cntraveler.com/photos/60341fbad7bd3b27823c9db2/16:9/w_2560%2Cc_limit/Tokyo-2021-GettyImages-1208124099.jpg",
        )

        db.session.add(city16)

        city17 = City(
            city_name="Kyoto",
            state_code="",
            country_name="Japan",
            exchange_rate={
                "EUR": 0.0064,
                "AUD": 0.010,
                "USD": 0.0071,
                "CAD": 0.0093,
                "GBP": 0.0055,
                "SGD": 0.0094,
            },
            currency_code="JPY",
            img="https://www.gotokyo.org/en/plan/tokyo-outline/images/main.jpg",
        )

        db.session.add(city17)

        city18 = City(
            city_name="Delhi",
            state_code="",
            country_name="India",
            exchange_rate={
                "EUR": 0.011,
                "AUD": 0.018,
                "USD": 0.012,
                "CAD": 0.016,
                "GBP": 0.0095,
                "SGD": 0.016,
            },
            currency_code="INR",
            img="https://www.travelandleisure.com/thmb/iAIrOVW7yWrDG8pZBpKMOvEGuNQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/new-delhi-india-NEWDELHITG0721-60d592e1603349298a0206d67d08582b.jpg",
        )

        db.session.add(city18)

        city19 = City(
            city_name="Mumbai",
            state_code="",
            country_name="India",
            exchange_rate={
                "EUR": 0.011,
                "AUD": 0.018,
                "USD": 0.012,
                "CAD": 0.016,
                "GBP": 0.0095,
                "SGD": 0.016,
            },
            currency_code="INR",
            img="https://cms.finnair.com/resource/blob/2573910/a14e037941fbe6646a68cd56a8fea9d0/mumbai-main-data.jpg",
        )

        db.session.add(city19)

        city20 = City(
            city_name="Bangalore",
            state_code="",
            country_name="India",
            exchange_rate={
                "EUR": 0.011,
                "AUD": 0.018,
                "USD": 0.012,
                "CAD": 0.016,
                "GBP": 0.0095,
                "SGD": 0.016,
            },
            currency_code="INR",
            img="https://lp-cms-production.imgix.net/2019-06/9483508eeee2b78a7356a15ed9c337a1-bengaluru-bangalore.jpg",
        )

        db.session.add(city20)

        city21 = City(
            city_name="Beijing",
            state_code="",
            country_name="China",
            exchange_rate={
                "EUR": 0.13,
                "AUD": 0.21,
                "USD": 0.14,
                "CAD": 0.18,
                "GBP": 0.11,
                "SGD": 0.19,
            },
            currency_code="CNY",
            img="https://i.natgeofe.com/n/2024d353-131c-4c29-a04f-5589c541e980/beijing_travel_16x9.jpg",
        )

        db.session.add(city21)

        city22 = City(
            city_name="Shanghai",
            state_code="",
            country_name="China",
            exchange_rate={
                "EUR": 0.13,
                "AUD": 0.22,
                "USD": 0.14,
                "CAD": 0.18,
                "GBP": 0.11,
                "SGD": 0.19,
            },
            currency_code="CNY",
            img="https://lp-cms-production.imgix.net/2023-02/GettyImages-1162611090.jpg",
        )

        db.session.add(city22)

        city23 = City(
            city_name="Guangzhou",
            state_code="",
            country_name="China",
            exchange_rate={
                "EUR": 0.13,
                "AUD": 0.22,
                "USD": 0.14,
                "CAD": 0.18,
                "GBP": 0.11,
                "SGD": 0.19,
            },
            currency_code="CNY",
            img="https://gba.investhk.gov.hk/sites/default/files/Guangzhou_5.jpg",
        )

        db.session.add(city23)

        city24 = City(
            city_name="Istanbul",
            state_code="",
            country_name="Turkey",
            exchange_rate={
                "EUR": 0.034,
                "AUD": 0.055,
                "USD": 0.037,
                "CAD": 0.049,
                "GBP": 0.029,
                "SGD": 0.049,
            },
            currency_code="TRY",
            img="https://a.cdn-hotels.com/gdcs/production6/d781/3bae040b-2afb-4b11-9542-859eeb8ebaf1.jpg",
        )

        db.session.add(city24)

        city25 = City(
            city_name="Ankara",
            state_code="",
            country_name="Turkey",
            exchange_rate={
                "EUR": 0.034,
                "AUD": 0.055,
                "USD": 0.037,
                "CAD": 0.049,
                "GBP": 0.029,
                "SGD": 0.049,
            },
            currency_code="TRY",
            img="https://www.nationsonline.org/gallery/Turkey/Kocatepe-mosque-Ankara.jpg",
        )

        db.session.add(city25)

        city26 = City(
            city_name="Izmir",
            state_code="",
            country_name="Turkey",
            exchange_rate={
                "EUR": 0.034,
                "AUD": 0.055,
                "USD": 0.037,
                "CAD": 0.049,
                "GBP": 0.029,
                "SGD": 0.049,
            },
            currency_code="TRY",
            img="https://media.cnn.com/api/v1/images/stellar/prod/220829115737-06-izmir-turkey-elevator.jpg?c=original&q=h_618,c_fill",
        )

        db.session.add(city26)

        city27 = City(
            city_name="Bangkok",
            state_code="",
            country_name="Thailand",
            exchange_rate={
                "EUR": 0.026,
                "AUD": 0.043,
                "USD": 0.029,
                "CAD": 0.038,
                "GBP": 0.023,
                "SGD": 0.039,
            },
            currency_code="THB",
            img="https://cdn.destguides.com/files/store/itinerary/1394/background_image/jpeg_medium_202112291737-4b9732c3c81e2136ccbce9e51ae6fc7f.jpeg",
        )

        db.session.add(city27)

        city28 = City(
            city_name="Chiang Mai",
            state_code="",
            country_name="Thailand",
            exchange_rate={
                "EUR": 0.026,
                "AUD": 0.043,
                "USD": 0.029,
                "CAD": 0.038,
                "GBP": 0.023,
                "SGD": 0.039,
            },
            currency_code="THB",
            img="https://res.klook.com/image/upload/Mobile/City/cswglxpstphljdourpfu.jpg",
        )

        db.session.add(city28)

        city29 = City(
            city_name="Phuket",
            state_code="",
            country_name="Thailand",
            exchange_rate={
                "EUR": 0.026,
                "AUD": 0.043,
                "USD": 0.029,
                "CAD": 0.038,
                "GBP": 0.023,
                "SGD": 0.039,
            },
            currency_code="THB",
            img="https://www.letsphuket.com/wp-content/uploads/phuket1.jpg",
        )

        db.session.add(city29)

        city30 = City(
            city_name="Paris",
            state_code="",
            country_name="France",
            exchange_rate={
                "EUR": 1.00,
                "AUD": 1.64,
                "USD": 1.11,
                "CAD": 1.46,
                "GBP": 0.86,
                "SGD": 1.47,
            },
            currency_code="EUR",
            img="https://res.klook.com/image/upload/Mobile/City/swox6wjsl5ndvkv5jvum.jpg",
        )

        db.session.add(city30)

        city31 = City(
            city_name="Marseille",
            state_code="",
            country_name="France",
            exchange_rate={
                "EUR": 1.00,
                "AUD": 1.64,
                "USD": 1.11,
                "CAD": 1.46,
                "GBP": 0.86,
                "SGD": 1.47,
            },
            currency_code="EUR",
            img="https://theplanetd.com/images/Best-Things-to-do-in-Marseille-France.jpg",
        )

        db.session.add(city31)

        city32 = City(
            city_name="Lyon",
            state_code="",
            country_name="France",
            exchange_rate={
                "EUR": 1.00,
                "AUD": 1.64,
                "USD": 1.11,
                "CAD": 1.46,
                "GBP": 0.86,
                "SGD": 1.47,
            },
            currency_code="EUR",
            img="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/14/da/01/47/vieux-lyon.jpg?w=1200&h=-1&s=1",
        )

        db.session.add(city32)

        city33 = City(
            city_name="Berlin",
            state_code="",
            country_name="Germany",
            exchange_rate={
                "EUR": 1.00,
                "AUD": 1.64,
                "USD": 1.11,
                "CAD": 1.46,
                "GBP": 0.86,
                "SGD": 1.47,
            },
            currency_code="EUR",
            img="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Museumsinsel_Berlin_Juli_2021_1_%28cropped%29.jpg/1200px-Museumsinsel_Berlin_Juli_2021_1_%28cropped%29.jpg",
        )

        db.session.add(city33)

        city34 = City(
            city_name="Munich",
            state_code="",
            country_name="Germany",
            exchange_rate={
                "EUR": 1.00,
                "AUD": 1.64,
                "USD": 1.11,
                "CAD": 1.46,
                "GBP": 0.86,
                "SGD": 1.47,
            },
            currency_code="EUR",
            img="https://www.theglobetrottingdetective.com/wp-content/uploads/2021/07/best-day-trips-from-Munich-Neuschwanstein-Castle-Germany.jpg",
        )

        db.session.add(city34)

        city35 = City(
            city_name="Hamburg",
            state_code="",
            country_name="Germany",
            exchange_rate={
                "EUR": 1.00,
                "AUD": 1.64,
                "USD": 1.11,
                "CAD": 1.46,
                "GBP": 0.86,
                "SGD": 1.47,
            },
            currency_code="EUR",
            img="https://img.theculturetrip.com/wp-content/uploads/2021/07/2ak0rm3-e1629218784273.jpg",
        )

        db.session.add(city35)

        city36 = City(
            city_name="Rome",
            state_code="",
            country_name="Italy",
            exchange_rate={
                "EUR": 1.00,
                "AUD": 1.64,
                "USD": 1.11,
                "CAD": 1.46,
                "GBP": 0.86,
                "SGD": 1.47,
            },
            currency_code="EUR",
            img="https://res.klook.com/image/upload/Mobile/City/afmqgg5h0jl9wnr1dfmf.jpg",
        )

        db.session.add(city36)

        city37 = City(
            city_name="Milan",
            state_code="",
            country_name="Italy",
            exchange_rate={
                "EUR": 1.00,
                "AUD": 1.64,
                "USD": 1.11,
                "CAD": 1.46,
                "GBP": 0.86,
                "SGD": 1.47,
            },
            currency_code="EUR",
            img="https://a.cdn-hotels.com/gdcs/production68/d1314/b12f79e7-bcce-4cac-96f8-33f98b9bfb88.jpg",
        )

        db.session.add(city37)

        city38 = City(
            city_name="Venice",
            state_code="",
            country_name="Italy",
            exchange_rate={
                "EUR": 1.00,
                "AUD": 1.64,
                "USD": 1.11,
                "CAD": 1.46,
                "GBP": 0.86,
                "SGD": 1.47,
            },
            currency_code="EUR",
            img="https://www.iwanderlista.com/wp-content/uploads/2020/09/Venice-Italy-67-1027x685.jpg",
        )

        db.session.add(city38)

        city39 = City(
            city_name="Madrid",
            state_code="",
            country_name="Spain",
            exchange_rate={
                "EUR": 1.00,
                "AUD": 1.64,
                "USD": 1.11,
                "CAD": 1.46,
                "GBP": 0.86,
                "SGD": 1.47,
            },
            currency_code="EUR",
            img="https://media.cntraveller.com/photos/611be916628f4910ed101d18/16:9/w_2992,h_1683,c_limit/parque-del-buen-retiro-gettyimages-873841648.jpg",
        )

        db.session.add(city39)

        city40 = City(
            city_name="Barcelona",
            state_code="",
            country_name="Spain",
            exchange_rate={
                "EUR": 1.00,
                "AUD": 1.64,
                "USD": 1.11,
                "CAD": 1.46,
                "GBP": 0.86,
                "SGD": 1.47,
            },
            currency_code="EUR",
            img="https://media.timeout.com/images/105827631/750/422/image.jpg",
        )

        db.session.add(city40)

        city41 = City(
            city_name="Seville",
            state_code="",
            country_name="Spain",
            exchange_rate={
                "EUR": 1.00,
                "AUD": 1.64,
                "USD": 1.11,
                "CAD": 1.46,
                "GBP": 0.86,
                "SGD": 1.47,
            },
            currency_code="EUR",
            img="https://cdn.britannica.com/79/102579-050-CD542D7F/Sevilla-Spain.jpg",
        )

        db.session.add(city41)

        city42 = City(
            city_name="Amsterdam",
            state_code="",
            country_name="Netherlands",
            exchange_rate={
                "EUR": 1.00,
                "AUD": 1.64,
                "USD": 1.11,
                "CAD": 1.46,
                "GBP": 0.86,
                "SGD": 1.47,
            },
            currency_code="EUR",
            img="https://www.travelandleisure.com/thmb/_3nQ1ivxrnTKVphdp9ZYvukADKQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/amsterdam-nl-AMSTERDAMTG0521-6d2bfaac29704667a950bcf219680640.jpg",
        )

        db.session.add(city42)

        city43 = City(
            city_name="Rotterdam",
            state_code="",
            country_name="Netherlands",
            exchange_rate={
                "EUR": 1.00,
                "AUD": 1.64,
                "USD": 1.11,
                "CAD": 1.46,
                "GBP": 0.86,
                "SGD": 1.47,
            },
            currency_code="EUR",
            img="https://media.cnn.com/api/v1/images/stellar/prod/170221114745-rotterdam-markthal-c-ossip-van-duivenbode1576-rotterdam-partners-editorial.jpg?q=w_1900,h_1069,x_0,y_0,c_fill/h_618",
        )

        db.session.add(city43)

        city44 = City(
            city_name="Utrecht",
            state_code="",
            country_name="Netherlands",
            exchange_rate={
                "EUR": 1.00,
                "AUD": 1.64,
                "USD": 1.11,
                "CAD": 1.46,
                "GBP": 0.86,
                "SGD": 1.47,
            },
            currency_code="EUR",
            img="https://s27363.pcdn.co/wp-content/uploads/2020/05/One-Day-in-Utrecht.jpg.optimal.jpg",
        )

        db.session.add(city44)

        city45 = City(
            city_name="New York City",
            state_code="NY",
            country_name="United States",
            exchange_rate={
                "EUR": 0.90,
                "AUD": 1.48,
                "USD": 1.00,
                "CAD": 1.32,
                "GBP": 0.78,
                "SGD": 1.33,
            },
            currency_code="USD",
            img="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/View_of_Empire_State_Building_from_Rockefeller_Center_New_York_City_dllu_%28cropped%29.jpg/1200px-View_of_Empire_State_Building_from_Rockefeller_Center_New_York_City_dllu_%28cropped%29.jpg",
        )

        db.session.add(city45)

        city46 = City(
            city_name="Los Angeles",
            state_code="CA",
            country_name="United States",
            exchange_rate={
                "EUR": 0.90,
                "AUD": 1.48,
                "USD": 1.00,
                "CAD": 1.32,
                "GBP": 0.78,
                "SGD": 1.33,
            },
            currency_code="USD",
            img="https://lacounty.gov/wp-content/uploads/2022/03/shutterstock_1418018357-scaled.jpg",
        )

        db.session.add(city46)

        city47 = City(
            city_name="Chicago",
            state_code="IL",
            country_name="United States",
            exchange_rate={
                "EUR": 0.90,
                "AUD": 1.48,
                "USD": 1.00,
                "CAD": 1.32,
                "GBP": 0.78,
                "SGD": 1.33,
            },
            currency_code="USD",
            img="https://www.travelandleisure.com/thmb/wwUPgdpCUuD5sAPFLQf4YasjH0M=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/chicago-illinois-CHITG0221-e448062fc5164da0bba639f9857987f6.jpg",
        )

        db.session.add(city47)

        city48 = City(
            city_name="Toronto",
            state_code="",
            country_name="Canada",
            exchange_rate={
                "EUR": 0.69,
                "AUD": 1.13,
                "USD": 0.76,
                "CAD": 1.00,
                "GBP": 0.59,
                "SGD": 1.01,
            },
            currency_code="CAD",
            img="https://www.prepareforcanada.com/wp-content/uploads/Torronto-Main-1024x576.jpg",
        )

        db.session.add(city48)

        city49 = City(
            city_name="Vancouver",
            state_code="",
            country_name="Canada",
            exchange_rate={
                "EUR": 0.69,
                "AUD": 1.13,
                "USD": 0.76,
                "CAD": 1.00,
                "GBP": 0.59,
                "SGD": 1.01,
            },
            currency_code="CAD",
            img="https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Concord_Pacific_Master_Plan_Area.jpg/1200px-Concord_Pacific_Master_Plan_Area.jpg",
        )

        db.session.add(city49)

        city50 = City(
            city_name="Montreal",
            state_code="",
            country_name="Canada",
            exchange_rate={
                "EUR": 0.69,
                "AUD": 1.13,
                "USD": 0.76,
                "CAD": 1.00,
                "GBP": 0.59,
                "SGD": 1.01,
            },
            currency_code="CAD",
        )

        db.session.add(city50)

        city51 = City(
            city_name="Mexico City",
            state_code="",
            country_name="Mexico",
            exchange_rate={
                "EUR": 0.054,
                "AUD": 0.088,
                "USD": 0.059,
                "CAD": 0.078,
                "GBP": 0.046,
                "SGD": 0.079,
            },
            currency_code="MXN",
            img="https://i.natgeofe.com/n/6c02ad5a-977b-4f12-b9c0-02ffb0736e07/metropolitan-cathedral-zocalo-mexico-city_2x1.JPG",
        )

        db.session.add(city51)

        city52 = City(
            city_name="Cancun",
            state_code="",
            country_name="Mexico",
            exchange_rate={
                "EUR": 0.054,
                "AUD": 0.088,
                "USD": 0.059,
                "CAD": 0.078,
                "GBP": 0.046,
                "SGD": 0.079,
            },
            currency_code="MXN",
            img="https://www.mexperience.com/wp-content/uploads/Cancun-Beaches-Aerial-NBS.jpg",
        )

        db.session.add(city52)

        city53 = City(
            city_name="Guadalajara",
            state_code="",
            country_name="Mexico",
            exchange_rate={
                "EUR": 0.054,
                "AUD": 0.088,
                "USD": 0.059,
                "CAD": 0.078,
                "GBP": 0.046,
                "SGD": 0.079,
            },
            currency_code="MXN",
            img="https://lp-cms-production.imgix.net/2019-06/79620207.jpg",
        )

        db.session.add(city53)

        city54 = City(
            city_name="Camagüey",
            state_code="",
            country_name="Cuba",
            exchange_rate={
                "EUR": 0.038,
                "AUD": 0.062,
                "USD": 0.042,
                "CAD": 0.055,
                "GBP": 0.033,
                "SGD": 0.056,
            },
            currency_code="CUP",
            img="https://lp-cms-production.imgix.net/2019-06/25d1c7f222441f0294bb535b3b460390-camaguey.jpg",
        )

        db.session.add(city54)

        city55 = City(
            city_name="Santiago de Cuba",
            state_code="",
            country_name="Cuba",
            exchange_rate={
                "EUR": 0.038,
                "AUD": 0.062,
                "USD": 0.042,
                "CAD": 0.055,
                "GBP": 0.033,
                "SGD": 0.056,
            },
            currency_code="CUP",
            img="https://www.iccaribbean.com/wp-content/uploads/2022/09/Santiago-de-Cuba.jpg",
        )

        db.session.add(city55)

        city56 = City(
            city_name="Havana",
            state_code="",
            country_name="Cuba",
            exchange_rate={
                "EUR": 0.038,
                "AUD": 0.062,
                "USD": 0.042,
                "CAD": 0.055,
                "GBP": 0.033,
                "SGD": 0.056,
            },
            currency_code="CUP",
            img="https://content.r9cdn.net/rimg/dimg/a3/1d/05f2b4a1-city-11020-1700c4dba73.jpg?crop=true&width=1020&height=498",
        )

        db.session.add(city56)

        city57 = City(
            city_name="San Jose",
            state_code="",
            country_name="Costa Rica",
            exchange_rate={
                "EUR": 0.0017,
                "AUD": 0.0028,
                "USD": 0.0019,
                "CAD": 0.0025,
                "GBP": 0.0015,
                "SGD": 0.0025,
            },
            currency_code="CRC",
            img="https://cdn.britannica.com/62/194162-050-C4D6DD9A/National-Theatre-San-Jose-Costa-Rica.jpg",
        )

        db.session.add(city57)

        city58 = City(
            city_name="Limon",
            state_code="",
            country_name="Costa Rica",
            exchange_rate={
                "EUR": 0.0017,
                "AUD": 0.0028,
                "USD": 0.0019,
                "CAD": 0.0025,
                "GBP": 0.0015,
                "SGD": 0.0025,
            },
            currency_code="CRC",
            img="https://costarica.org/wp-content/uploads/2017/09/Limon2.jpg",
        )

        db.session.add(city58)

        city59 = City(
            city_name="Alajuela",
            state_code="",
            country_name="Costa Rica",
            exchange_rate={
                "EUR": 0.0017,
                "AUD": 0.0028,
                "USD": 0.0019,
                "CAD": 0.0025,
                "GBP": 0.0015,
                "SGD": 0.0025,
            },
            currency_code="CRC",
            img="https://www.costaricavibes.com/wp-content/uploads/Copy-of-Packing-for-Costa-Rica.jpg",
        )

        db.session.add(city59)

        city60 = City(
            city_name="Rio de Janeiro",
            state_code="",
            country_name="Brazil",
            exchange_rate={
                "EUR": 0.19,
                "AUD": 0.31,
                "USD": 0.21,
                "CAD": 0.28,
                "GBP": 0.17,
                "SGD": 0.28,
            },
            currency_code="BRL",
            img="https://www.travelandleisure.com/thmb/x-LBqpaBsbUqGYtHu8gLnRMxPvg=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/rio-de-janeiro-RIOTG0721-c59c5e2f3a354e798587d5ef925b23e3.jpg",
        )

        db.session.add(city60)

        city61 = City(
            city_name="São Paulo",
            state_code="",
            country_name="Brazil",
            exchange_rate={
                "EUR": 0.19,
                "AUD": 0.31,
                "USD": 0.21,
                "CAD": 0.28,
                "GBP": 0.17,
                "SGD": 0.28,
            },
            currency_code="BRL",
            img="https://a.cdn-hotels.com/gdcs/production31/d1095/2a0c9319-6599-4c14-98e5-e74d13eab669.jpg",
        )

        db.session.add(city61)

        city62 = City(
            city_name="Brasília",
            state_code="",
            country_name="Brazil",
            exchange_rate={
                "EUR": 0.19,
                "AUD": 0.31,
                "USD": 0.21,
                "CAD": 0.28,
                "GBP": 0.17,
                "SGD": 0.28,
            },
            currency_code="BRL",
            img="https://www.cepal.org/sites/default/files/styles/1920x1080/public/regionaloffice/images/brasilia.jpg?itok=VuRo2Qua",
        )

        db.session.add(city62)

        city63 = City(
            city_name="Buenos Aires",
            state_code="",
            country_name="Argentina",
            exchange_rate={
                "EUR": 0.0033,
                "AUD": 0.0055,
                "USD": 0.0037,
                "CAD": 0.0049,
                "GBP": 0.0029,
                "SGD": 0.0049,
            },
            currency_code="ARS",
            img="https://cdn.britannica.com/40/195440-050-B3859318/Congressional-Plaza-building-National-Congress-Buenos-Aires.jpg",
        )

        db.session.add(city63)

        city64 = City(
            city_name="Cordoba",
            state_code="",
            country_name="Argentina",
            exchange_rate={
                "EUR": 0.0033,
                "AUD": 0.0055,
                "USD": 0.0037,
                "CAD": 0.0049,
                "GBP": 0.0029,
                "SGD": 0.0049,
            },
            currency_code="ARS",
            img="https://www.thewildlifediaries.com/wp-content/uploads/2021/11/Things-to-do-in-Cordoba-Roman-bridge-and-mosque-cathedral.jpg",
        )

        db.session.add(city64)

        city65 = City(
            city_name="Rosario",
            state_code="",
            country_name="Argentina",
            exchange_rate={
                "EUR": 0.0033,
                "AUD": 0.0055,
                "USD": 0.0037,
                "CAD": 0.0049,
                "GBP": 0.0029,
                "SGD": 0.0049,
            },
            currency_code="ARS",
            img="https://mediaim.expedia.com/destination/1/15c19af6d32f4bdb8f5f454dedd0554e.jpg",
        )

        db.session.add(city65)

        city67 = City(
            city_name="Lima",
            state_code="",
            country_name="Peru",
            exchange_rate={
                "EUR": 0.25,
                "AUD": 0.41,
                "USD": 0.28,
                "CAD": 0.37,
                "GBP": 0.22,
                "SGD": 0.37,
            },
            currency_code="PEN",
            img="https://a.cdn-hotels.com/gdcs/production9/d1622/a10657d4-4f58-47ad-a91b-deecfa200dd0.jpg",
        )

        db.session.add(city67)

        city68 = City(
            city_name="Arequipa",
            state_code="",
            country_name="Peru",
            exchange_rate={
                "EUR": 0.25,
                "AUD": 0.41,
                "USD": 0.28,
                "CAD": 0.37,
                "GBP": 0.22,
                "SGD": 0.37,
            },
            currency_code="PEN",
            img="https://www.peru.travel/Contenido/Destino/Imagen/en/16/1.1/Principal/Plaza%20de%20Armas%20Arequipa.jpg",
        )

        db.session.add(city68)

        city69 = City(
            city_name="Cusco",
            state_code="",
            country_name="Peru",
            exchange_rate={
                "EUR": 0.25,
                "AUD": 0.41,
                "USD": 0.28,
                "CAD": 0.37,
                "GBP": 0.22,
                "SGD": 0.37,
            },
            currency_code="PEN",
            img="https://deih43ym53wif.cloudfront.net/cusco-peru-shutterstock_346277210.jpg_45fc70bd52.jpg",
        )

        db.session.add(city69)

        city70 = City(
            city_name="Santiago",
            state_code="",
            country_name="Chile",
            exchange_rate={
                "EUR": 0.0011,
                "AUD": 0.0018,
                "USD": 0.0012,
                "CAD": 0.0016,
                "GBP": 0.00094,
                "SGD": 0.0016,
            },
            currency_code="CLP",
            img="https://www.andbeyond.com/wp-content/uploads/sites/5/Cable-car-in-Santiago-city-in-Chile.jpg",
        )

        db.session.add(city70)

        city71 = City(
            city_name="Valparaiso",
            state_code="",
            country_name="Chile",
            exchange_rate={
                "EUR": 0.0011,
                "AUD": 0.0018,
                "USD": 0.0012,
                "CAD": 0.0016,
                "GBP": 0.00094,
                "SGD": 0.0016,
            },
            currency_code="CLP",
            img="https://destinationlesstravel.com/wp-content/uploads/2022/08/View-of-Valparaiso-from-the-hills-behind-the-city.jpg.webp",
        )

        db.session.add(city71)

        city72 = City(
            city_name="Concepcion",
            state_code="",
            country_name="Chile",
            exchange_rate={
                "EUR": 0.0011,
                "AUD": 0.0018,
                "USD": 0.0012,
                "CAD": 0.0016,
                "GBP": 0.00094,
                "SGD": 0.0016,
            },
            currency_code="CLP",
            img="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Gran_Concepci%C3%B3n.jpg/1200px-Gran_Concepci%C3%B3n.jpg",
        )

        db.session.add(city72)

        city73 = City(
            city_name="Bogota",
            state_code="",
            country_name="Colombia",
            exchange_rate={
                "EUR": 0.00023,
                "AUD": 0.00037,
                "USD": 0.00025,
                "CAD": 0.00033,
                "GBP": 0.00020,
                "SGD": 0.00033,
            },
            currency_code="COP",
            img="https://www.cepal.org/sites/default/files/styles/1920x1080/public/regionaloffice/images/bogota.jpg?itok=o3kfQd06",
        )

        db.session.add(city73)

        city74 = City(
            city_name="Medellin",
            state_code="",
            country_name="Colombia",
            exchange_rate={
                "EUR": 0.00023,
                "AUD": 0.00037,
                "USD": 0.00025,
                "CAD": 0.00033,
                "GBP": 0.00020,
                "SGD": 0.00033,
            },
            currency_code="COP",
            img="https://i.natgeofe.com/n/c5f625f7-a459-4afb-85c6-673224306569/downtown-medellin-colombia.jpg?w=2880&h=1912",
        )

        db.session.add(city74)

        city75 = City(
            city_name="Cartagena",
            state_code="",
            country_name="Colombia",
            exchange_rate={
                "EUR": 0.00023,
                "AUD": 0.00037,
                "USD": 0.00025,
                "CAD": 0.00033,
                "GBP": 0.00020,
                "SGD": 0.00033,
            },
            currency_code="COP",
            img="https://media.cnn.com/api/v1/images/stellar/prod/190820104325-01-things-to-do-cartagena-colombia.jpg?q=x_0,y_0,h_2178,w_3870,c_fill",
        )

        db.session.add(city75)

        price1 = Price(
            city_id=1,
            item_name="One bedroom apartment in city centre",
            category_name="Rent Per Month",
            avg_usd=463.54,
        )

        db.session.add(price1)

        price2 = Price(
            city_id=1,
            item_name="One bedroom apartment outside of city centre",
            category_name="Rent Per Month",
            avg_usd=375.14,
        )

        db.session.add(price2)

        price3 = Price(
            city_id=1,
            item_name="Three bedroom apartment in city centre",
            category_name="Rent Per Month",
            avg_usd=909.68,
        )

        db.session.add(price3)

        price4 = Price(
            city_id=1,
            item_name="Three bedroom apartment outside of city centre",
            category_name="Rent Per Month",
            avg_usd=737.57,
        )

        price5 = Price(
            city_id=1,
            item_name="Basic utilities for 85m2 Apartment including Electricity, Heating or Cooling, Water and Garbage",
            category_name="Utilities Per Month",
            avg_usd=98.55,
        )

        db.session.add(price5)

        price6 = Price(
            city_id=1,
            item_name="Prepaid Mobile Tariff Local, price per 1 min, No Discounts or Plans",
            category_name="Utilities Per Month",
            avg_usd=0.12,
        )

        db.session.add(price6)

        price7 = Price(
            city_id=1,
            item_name="Internet, 60 Mbps or More, Unlimited Data, Cable/ADSL",
            category_name="Utilities Per Month",
            avg_usd=63.23,
        )

        db.session.add(price7)

        price8 = Price(
            city_id=1,
            item_name="Monthly Pass, Regular Price",
            category_name="Transportation",
            avg_usd=85.25,
        )

        db.session.add(price8)

        price9 = Price(
            city_id=1,
            item_name="Gasoline, 1 liter",
            category_name="Transportation",
            avg_usd=1.04,
        )

        db.session.add(price9)

        price10 = Price(
            city_id=1,
            item_name="Volkswagen Golf 1.4 90 KW Trendline (Or Equivalent New Car)",
            category_name="Transportation",
            avg_usd=22231.75,
        )

        db.session.add(price10)

        price11 = Price(
            city_id=1,
            item_name="Meal in Inexpensive Restaurant",
            category_name="Restaurants",
            avg_usd=10.38,
        )

        db.session.add(price11)

        price12 = Price(
            city_id=1,
            item_name="Meal for 2 People, Mid-range Restaurant, Three-course",
            category_name="Restaurants",
            avg_usd=40.17,
        )

        db.session.add(price12)

        price13 = Price(
            city_id=2,
            item_name="Meal in Inexpensive Restaurant",
            category_name="Restaurants",
            avg_usd=8.03,
        )

        db.session.add(price13)

        price14 = Price(
            city_id=2,
            item_name="Meal for 2 People, Mid-range Restaurant, Three-course",
            category_name="Restaurants",
            avg_usd=36.82,
        )

        db.session.add(price14)

        price15 = Price(
            city_id=2,
            item_name="Monthly Pass, Regular Price",
            category_name="Transportation",
            avg_usd=1.34,
        )

        db.session.add(price15)

        price16 = Price(
            city_id=2,
            item_name="Gasoline, 1 liter",
            category_name="Transportation",
            avg_usd=1.02,
        )

        db.session.add(price16)

        price17 = Price(
            city_id=2,
            item_name="Volkswagen Golf 1.4 90 KW Trendline (Or Equivalent New Car)",
            category_name="Transportation",
            avg_usd=20082.88,
        )

        db.session.add(price17)

        price18 = Price(
            city_id=2,
            item_name="Basic utilities for 85m2 Apartment including Electricity, Heating or Cooling, Water and Garbage",
            category_name="Utilities Per Month",
            avg_usd=81.58,
        )

        db.session.add(price18)

        price19 = Price(
            city_id=2,
            item_name="Prepaid Mobile Tariff Local, price per 1 min, No Discounts or Plans",
            category_name="Utilities Per Month",
            avg_usd=0.13,
        )

        db.session.add(price19)

        price20 = Price(
            city_id=2,
            item_name="Internet, 60 Mbps or More, Unlimited Data, Cable/ADSL",
            category_name="Utilities Per Month",
            avg_usd=61.61,
        )

        db.session.add(price20)

        price21 = Price(
            city_id=2,
            item_name="One bedroom apartment in city centre",
            category_name="Rent Per Month",
            avg_usd=706.43,
        )

        db.session.add(price21)

        price22 = Price(
            city_id=2,
            item_name="One bedroom apartment outside of city centre",
            category_name="Rent Per Month",
            avg_usd=506.58,
        )

        db.session.add(price22)

        price23 = Price(
            city_id=2,
            item_name="Three bedroom apartment in city centre",
            category_name="Rent Per Month",
            avg_usd=1453.23,
        )

        db.session.add(price23)

        price24 = Price(
            city_id=3,
            item_name="Meal in Inexpensive Restaurant",
            category_name="Restaurants",
            avg_usd=6.69,
        )

        db.session.add(price24)

        price25 = Price(
            city_id=3,
            item_name="Meal for 2 People, Mid-range Restaurant, Three-course",
            category_name="Restaurants",
            avg_usd=33.47,
        )

        db.session.add(price25)

        price26 = Price(
            city_id=3,
            item_name="Monthly Pass, Regular Price",
            category_name="Transportation",
            avg_usd=50.21,
        )

        db.session.add(price26)

        price25 = Price(
            city_id=3,
            item_name="Gasoline, 1 liter",
            category_name="Transportation",
            avg_usd=1.02,
        )

        db.session.add(price25)

        price26 = Price(
            city_id=3,
            item_name="Volkswagen Golf 1.4 90 KW Trendline (Or Equivalent New Car)",
            category_name="Transportation",
            avg_usd=20082.88,
        )

        db.session.add(price26)

        price27 = Price(
            city_id=3,
            item_name="Basic utilities for 85m2 Apartment including Electricity, Heating or Cooling, Water and Garbage",
            category_name="Utilities Per Month",
            avg_usd=81.58,
        )

        db.session.add(price27)

        price28 = Price(
            city_id=3,
            item_name="Prepaid Mobile Tariff Local, price per 1 min, No Discounts or Plans",
            category_name="Utilities Per Month",
            avg_usd=0.12,
        )

        db.session.add(price28)

        price29 = Price(
            city_id=3,
            item_name="Internet, 60 Mbps or More, Unlimited Data, Cable/ADSL",
            category_name="Utilities Per Month",
            avg_usd=65.08,
        )

        db.session.add(price29)

        price30 = Price(
            city_id=3,
            item_name="One bedroom apartment in city centre",
            category_name="Rent Per Month",
            avg_usd=348.64,
        )

        db.session.add(price30)

        price31 = Price(
            city_id=3,
            item_name="One bedroom apartment outside of city centre",
            category_name="Rent Per Month",
            avg_usd=331.24,
        )

        db.session.add(price31)

        price32 = Price(
            city_id=3,
            item_name="Three bedroom apartment in city centre",
            category_name="Rent Per Month",
            avg_usd=676.12,
        )

        db.session.add(price32)

        price24 = Price(
            city_id=3,
            item_name="Meal in Inexpensive Restaurant",
            category_name="Restaurants",
            avg_usd=6.69,
        )

        db.session.add(price24)

        price25 = Price(
            city_id=3,
            item_name="Meal for 2 People, Mid-range Restaurant, Three-course",
            category_name="Restaurants",
            avg_usd=33.47,
        )

        db.session.add(price25)

        price26 = Price(
            city_id=3,
            item_name="Monthly Pass, Regular Price",
            category_name="Transportation",
            avg_usd=50.21,
        )

        db.session.add(price26)

        price25 = Price(
            city_id=3,
            item_name="Gasoline, 1 liter",
            category_name="Transportation",
            avg_usd=1.02,
        )

        db.session.add(price25)

        price26 = Price(
            city_id=3,
            item_name="Volkswagen Golf 1.4 90 KW Trendline (Or Equivalent New Car)",
            category_name="Transportation",
            avg_usd=20082.88,
        )

        db.session.add(price26)

        price27 = Price(
            city_id=3,
            item_name="Basic utilities for 85m2 Apartment including Electricity, Heating or Cooling, Water and Garbage",
            category_name="Utilities Per Month",
            avg_usd=81.58,
        )

        db.session.add(price27)

        price28 = Price(
            city_id=3,
            item_name="Prepaid Mobile Tariff Local, price per 1 min, No Discounts or Plans",
            category_name="Utilities Per Month",
            avg_usd=0.12,
        )

        db.session.add(price28)

        price29 = Price(
            city_id=3,
            item_name="Internet, 60 Mbps or More, Unlimited Data, Cable/ADSL",
            category_name="Utilities Per Month",
            avg_usd=65.08,
        )

        db.session.add(price29)

        price30 = Price(
            city_id=3,
            item_name="One bedroom apartment in city centre",
            category_name="Rent Per Month",
            avg_usd=348.64,
        )

        db.session.add(price30)

        price31 = Price(
            city_id=3,
            item_name="One bedroom apartment outside of city centre",
            category_name="Rent Per Month",
            avg_usd=331.24,
        )

        db.session.add(price31)

        price32 = Price(
            city_id=3,
            item_name="Three bedroom apartment in city centre",
            category_name="Rent Per Month",
            avg_usd=676.12,
        )

        db.session.add(price32)

        db.session.commit()
