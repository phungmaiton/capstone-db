from app import app
from models import db, User, City, Price, UserCity, BlogComment
import random


if __name__ == "__main__":
    with app.app_context():

        def generate_random_avg_usd():
            return round(random.uniform(1, 2000), 2)

        # Existing item names for city_id=1
        existing_item_names = [
            "One bedroom apartment in city centre",
            "One bedroom apartment outside of city centre",
            "Three bedroom apartment in city centre",
            "Three bedroom apartment outside of city centre",
            "Basic utilities for 85m2 Apartment including Electricity, Heating or Cooling, Water and Garbage",
            "Prepaid Mobile Tariff Local, price per 1 min, No Discounts or Plans",
            "Internet, 60 Mbps or More, Unlimited Data, Cable/ADSL",
            "Monthly Pass, Regular Price",
            "Gasoline, 1 liter",
            "Volkswagen Golf 1.4 90 KW Trendline (Or Equivalent New Car)",
            "Meal in Inexpensive Restaurant",
            "Meal for 2 People, Mid-range Restaurant, Three-course",
        ]

        # Create and add 12 Price records for city_id=2 with random avg_usd
        for i in range(13, 25):
            item_name = existing_item_names[i - 13]  # Use the existing item name
            avg_usd = generate_random_avg_usd()  # Generate random avg_usd
            price = Price(
                city_id=2,
                item_name=item_name,
                category_name="Rent Per Month",  # Assuming the category_name remains the same
                avg_usd=avg_usd,
            )
            db.session.add(price)

        # Commit the changes to the database
        db.session.commit()
