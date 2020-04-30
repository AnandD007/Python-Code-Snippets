# # Kg to Pounds Converter:

kg = int(input("Enter your Weight : "))
# It converts that input value to kg value into pounds
pounds = 2.204623  # 1 Kg = 2.204623 Pounds
Weight = (kg * pounds)
print('Your Weight in Pounds is',Weight)
print(type(Weight))
print(type(kg))
print('--------------------------------------------------------------------------------------')

# # Pounds to Kg converter :

Weight_lbs= input('Enter  Your weight in Pounds(lbs):')
Weight_kg = float(Weight_lbs)*0.45359 # 1 Pounds = 0.45359 Pounds (float type casting to get precision)
print('Your Weight in Kilogram:',Weight_kg)
