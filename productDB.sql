-- Create database
create database datarep;
use datarep;

-- Create a product table
create table product_table (
id int AUTO_INCREMENT NOT NULL PRIMARY KEY, 
CoffeeName varchar(250), 
Origin varchar(250), 
Variety varchar (250),
Roast varchar(250),
Price float
);

-- Populate table with coffee
INSERT INTO product_table (CoffeeName, Origin, Variety, Roast, Price) VALUES ("GreeLion", "Columbia", "Arabica", "Dark Roast", 24.5);
INSERT INTO product_table (CoffeeName, Origin, Variety, Roast, Price) VALUES ("The Pure Cosmai", "Kenya", "Arabica", "Medium Roast", 29.3);
INSERT INTO product_table (CoffeeName, Origin, Variety, Roast, Price) VALUES ("Kawa", "Brazil", "Robusta", "Light Roast", 14.80);
INSERT INTO product_table (CoffeeName, Origin, Variety, Roast, Price) VALUES ("Pellini Organic", "Venezuela", "Arabica", "Dark Roast", 24.5);
INSERT INTO product_table (CoffeeName, Origin, Variety, Roast, Price) VALUES ("Cafes Lugat Moka", "Columbia", "Arabica", "Light Roast", 34);
INSERT INTO product_table (CoffeeName, Origin, Variety, Roast, Price) VALUES ("Les Petits Cherry", "Ecuador", "Arabica", "Dark Roast", 24.5);
INSERT INTO product_table (CoffeeName, Origin, Variety, Roast, Price) VALUES ("Caffe Raja", "India", "Robusta", "Dark Roast", 21.6);
INSERT INTO product_table (CoffeeName, Origin, Variety, Roast, Price) VALUES ("Perleo Espresso", "Guatemala", "Blend", "Medium Roast", 24.5);
INSERT INTO product_table (CoffeeName, Origin, Variety, Roast, Price) VALUES ("Caffe Vergnano", "Kenya", "Arabica", "Dark Roast", 29.9);
INSERT INTO product_table (CoffeeName, Origin, Variety, Roast, Price) VALUES ("Don Marco", "Brazil", "Blend", "Light Roast", 24.5);

