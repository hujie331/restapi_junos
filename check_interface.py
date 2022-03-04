import sjca
import bp
import sys,time


def invalid_choice():
   print()
   print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   print_one_by_one("      ~ Invalid Choice. Please try again. Thank you! ~\n")
   print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   print()
   print()

def under_construction():
   print()
   print()
   print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   print_one_by_one("~ This site is under construction. Please select another site, Thank you! ~\n")
   print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   print()
   print()

def print_one_by_one(text):
   sys.stdout.write("\r " + " " * 60 + "\r")
   sys.stdout.flush()
   for c in text:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(0.01)

def site_choice_function():
   while True:
      site_choice = input ("""\nPlease choose which site you want to check: \n
           1:  SJCA
           2:  San Mateo
           3:  San Francisco\n       
       Your choice: """)

      if site_choice == '1':
         sjca.sjca()
      elif site_choice == '2':
         bp.bp()
      elif site_choice == '3':
         under_construction()
      else:
         invalid_choice()

site_choice_function()
