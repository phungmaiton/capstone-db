from app import app
from models import db, User, City, Price, UserCity


if __name__ == "__main__":
    with app.app_context():
        User.query.delete()
        City.query.delete()
        Price.query.delete()
        UserCity.query.delete()

        # user = User(
        #     username="TestUser",
        #     email="test@gmail.com",
        #     city="Chantilly",
        #     state="Virginia",
        #     zipcode="20152",
        #     country="United States",
        #     currency_code="USD",
        # )

        # user.password_hash = "123"

        # db.session.add(user)

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
        )

        db.session.add(city44)

        city45 = City(
            city_name="New York City",
            state_code="",
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
        )

        db.session.add(city45)

        city46 = City(
            city_name="Los Angeles",
            state_code="",
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
        )

        db.session.add(city46)

        city47 = City(
            city_name="Chicago",
            state_code="",
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
        )

        db.session.add(city65)

        city66 = City(
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
        )

        db.session.add(city66)

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

        db.session.commit()
