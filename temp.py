
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

amount_of_purchase = float(input('enter the amount of purchase: '))
state_sales_tax = 0.05
county_sales_tax = 0.025
total_tax = state_sales_tax + county_sales_tax
total_sale = amount_of_purchase * (1+state_sales_tax + county_sales_tax)
print(total_tax)
print(total_sale)