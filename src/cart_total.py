from typing import List, Dict, Union
"""
Problem Statement: Shopping Cart System
You are tasked with building a simple shopping cart system to calculate the total cost of items in the cart, including tax and any applicable discounts. 
Your goal is to create functions that compute the total cost, apply discounts, and add tax to the cart total. 
Additionally, all calculated prices need to be rounded to 2 decimal places.

Business Rules:
1. Item Prices: Each item in the shopping cart has a name, price, and quantity. 
2. Discounts: If the total price of the cart exceeds $100, a discount of 10% is applied to the total price.  
3. Tax Calculation: After the discount is applied (if any), an 8% sales tax is added to the total price.  
4. Rounding: Each calculation (total cost, discounted price, and final price) must be rounded to two decimal places.   

You need to implement the following functions:
Function Specifications:
1. calculate_total_cost(cart: List[Dict[str, Union[str, float]]]) -> float
    Input: 
        cart is a list of dictionaries, where each dictionary contains: 
            "name": A string representing the name of the item. 
            "price": A float representing the price of one unit of the item. 
            "quantity": An integer representing the quantity of that item in the cart.     
    Output: 
        The total cost of all items in the cart, calculated as the sum of price * quantity for each item. The result should be rounded to two decimal places.   
2. apply_discount(total_cost: float) -> float
    Input: 
        total_cost is a float representing the total cost of the cart before discount.   
    Output: 
        The total cost after applying a 10% discount if the total cost exceeds $100. The result should be rounded to two decimal places.   
3. apply_tax(total_cost: float) -> float
    Input: 
        total_cost is a float representing the total cost of the cart after applying any discounts.   
    Output: 
        The total cost after applying an 8% sales tax. The result should be rounded to two decimal places.   
4. calculate_final_price(cart: List[Dict[str, Union[str, float]]]) -> float
    Input: 
        cart is a list of dictionaries, where each dictionary represents an item.   
    Output: 
        The final price after calculating the total cost, applying any discount, and adding the tax. The result should be rounded to two decimal places.   
"""

def calculate_total_cost(cart: List[Dict[str, Union[str, float]]]) -> float:
    """
    Function to calculate the total cost of items in the cart.
    Each item is a dictionary with 'price' and 'quantity' keys.
    The result should be rounded to 2 decimal places.
    """
    total_cost = 0.0
    # Your code to calculate total cost goes here
    for item in cart:
        total_cost += item['price']*item['quantity']
    return round(total_cost, 2)

def apply_discount(total_cost: float) -> float:
    """
    Function to apply a 10% discount if the total cost exceeds $100.
    The result should be rounded to 2 decimal places.
    """
    discounted_cost = total_cost
    # Your code to apply discount goes here
    if total_cost > 100:
        discount=total_cost*0.1
        discounted_cost=total_cost - discount
    return round(discounted_cost, 2)

def apply_tax(total_cost: float) -> float:
    """
    Function to apply an 8% sales tax to the total cost.
    The result should be rounded to 2 decimal places.
    """

    total_with_tax = total_cost

    # Your code to apply tax goes here
    total_with_tax = total_cost + (total_cost*0.08)
    return round(total_with_tax, 2)

def calculate_final_price(cart: List[Dict[str, Union[str, float]]]) -> float:
    """
    Function to calculate the final price after calculating the total cost, applying discount, and tax.
    The result should be rounded to 2 decimal places.
    """
    # Use the above functions to calculate the final price
    final_price = 0.0
    tc= calculate_total_cost(cart)
    dis=apply_discount(tc)
    tax=apply_tax(dis)
    final_price=tax
    return round(final_price, 2)