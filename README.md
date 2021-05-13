# Online Shop

Users will be able to browse through a product catalog and add products to a shopping cart.

Finally, they will be able to check out the cart and place an order.

This project will cover the following functionalities of an online shop:

* Creating the product catalog models, adding them to the administration site, and building the basic views to display the catalog.


* Building a shopping cart system using Django sessions to allow users to keep selected products while they browse the site.


* Creating the form and functionality to place orders on the site.


* Sending an asynchronous email confirmation to users when they place 
an order
  

## How to run

To run Online Shop in development mode; Just use steps below:

1. Install python3, pip, virtualenv in your system:
2. Clone the project.
3. Make development environment ready using commands below;
```commandline
cd online-shop
python3 -m venv env/myshop
source env/myshop/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```
4. Run Online Shop using python manage.py runserver
5. Go to http://localhost:8000 to see your Online Shop version.
