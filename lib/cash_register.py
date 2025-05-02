#!/usr/bin/env python3

class CashRegister:
  #pass
  def __init__(self, discount = 0):
    #pass
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, title, price, quantity = 1):
    for num in range(quantity):
      self.items.append(title)

    self.last_transaction = (price * quantity)

    self.total += self.last_transaction

    return self.items

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total = self.total * (100 - self.discount) / 100
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total -= self.last_transaction

