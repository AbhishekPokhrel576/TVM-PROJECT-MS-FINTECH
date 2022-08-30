#!/usr/bin/env python
# coding: utf-8

# # TIME VALUE MONEY ASSIGNMENT

# # Question Number 1

# In[5]:


# Time below represents the time elapsed in Years
TIME = float(input("Enter Period of time: "))

# PRESENTV below represents the $$ Value of asset in the present time
PRESENTV = float(input("Enter your present value: "))

# FUTUREV below represents the $$ Value of asset in future time
FUTUREV = float(input("Enter your future value: ")) 


# Interest represents the Annual Increase in Selling Price in Percent
# To get to the formula below, Solve FV = PV x [ 1 + (i / n) ] (n x t) for i where n's \value is 1
Interest = ((FUTUREV/PRESENTV)**(1/TIME)-1)*100

print("The Annual Increase in Selling Price is %0.3f percent" % Interest)


# # Question Number 2 

# In[8]:


# Interest represents how much interest you are receiving from bank
Interest = float(input("Enter your annual interest rate given by bank in percent value: "))

# PRESENTV below represents $$ you have available for your investment
PRESENTV = float(input("Enter your starting principal for ferrari: "))

# FUTUREV below represents $$ Value of Asset to Purchase
FUTUREV = float(input("Enter the amount you are trying to save for ferrari: ")) 

import math

# time represent the amount of years you have to wait for the ferrari
# math.ceil() rounds up the time to mimimum number of years you have to wait
# because the interest is compounded annually. 
# To get to the formula below, Solve FV = PV x [ 1 + (i / n) ] (n x t) for time where n's \value is 1
# t = ln(FUTUREV/PRESENTV) / ln(1 + Interest/100)
# Divide the interest given by 100 to turn it from percent to decimal

time = math.ceil(math.log(FUTUREV/PRESENTV)/math.log(1 + Interest/100))

print("This is the number of years you need to wait to purchase the ferrari:%d " % time)


# # Question Number 3

# In[10]:


# FUTUREV below represents the company's Unfunded Future Liability in Dollars
FUTUREV = float(input("Enter Imprudential, Inc's Unfunded Future Liability in dollars: ")) 

# Interest below represents the Relevant Discount Rate given
Interest = float(input("Enter the relevant discount rate: "))

# Time below represents the total time you have to pay unfunded future liability
TIME = float(input("Enter the time you have in years to pay Unfunded Pension Liability: "))

# PRESENTV Represents Imprudential, INC's present liability amount 
# To get to the formula below, Solve FV = PV x [ 1 + (i / n) ] (n x t) for PV where n's \value is 1
# PRESENTV = FUTUREV/(1 + Interest/100)^TIME
# Divide the interest given by 100 to turn it from percent to decimal

PRESENTV = FUTUREV / ((1 + Interest/100)**TIME)

print("Imprudential, Inc has a liability that presently amounts to:%.2f " % PRESENTV)


# In[ ]:




