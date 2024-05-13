'''Problem: Planetary Weight Calculator  

Milestone #1: Mars Weight

A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter 
called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth. Interestingly, 
Ingenuity uses Python for some of its flight modeling software!

When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an Earthling's weight 
on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars. 

The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and 
the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14. 

Solution Problem 1:'''

MARS_MULTIPLE= 0.378

def main():
   Earth_Weight_str =  input('Enter a weight on Earth: ')
   Earth_Weight = float(Earth_Weight_str)

   Mars_Weight = MARS_MULTIPLE * Earth_Weight
   rounded_mars_weight = round(Mars_Weight , 2 )

   print ("The equivalent weight on Mars: " + str( rounded_mars_weight ))
 





'''Milestone #2: Adding in All Planets

Mars is not the only planet in our solar system with its own unique gravity. In fact, each planet has a different gravitational constant, which affects how much an object
would weigh on that planet. Below is a list of the constants for each planet compared to Earth's gravity:

- Mercury: 37.6%

- Venus: 88.9%

- Mars: 37.8%

- Jupiter: 236.0%

- Saturn: 108.1%

- Uranus: 81.5%

- Neptune: 114.0%

Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a planet in our solar system. The program should print the
equivalent weight on that planet rounded to 2 decimal places if necessary.

You can assume that the user will always type in a planet with the first letter capitalized and you do not need to worry about the case where they type in something other
than one of the above planets.

  # problem 2 solution (Planetary Weight Calculator)'''

def main():
   earth_weight_str = input('Enter a weight on Earth: ')
   earth_weight = float(earth_weight_str)

   planet = input('Enter a planet: ')

   if planet == "Mercury":
     final_weight =  earth_weight * 0.376
     rounded_weight   = round(final_weight, 2)

   elif  planet == "Venus":
     final_weight = earth_weight * 0.889
     rounded_weight   = round(final_weight, 2)

   elif  planet == "Mars":
    final_weight = earth_weight * 0.378
    rounded_weight   = round(final_weight, 2)

   elif  planet == "Jupiter":
     final_weight = earth_weight * 2.36 
     rounded_weight   = round(final_weight, 2)

   elif  planet == "Saturn":
     final_weight = earth_weight * 1.081
     rounded_weight   = round(final_weight, 2)

   elif  planet == "Uranus":
     final_weight = earth_weight * 0.815
     rounded_weight   = round(final_weight, 2)

   elif  planet == "Neptune":
     final_weight = earth_weight * 1.14
     rounded_weight   = round(final_weight, 2)
     
   else:
     print('Ivalid Planet Name ')

   print("The equivalent weight on " + planet + ":" + str(rounded_weight)  )


if __name__ == "__main__":
    main()
