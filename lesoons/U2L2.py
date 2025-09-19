inches = 10 ** 12  # one trillion
(foot, inches) = divmod(inches, 12)
(yard, foot_) = divmod(foot, 3)
(miles, yard_) = divmod(yard, 1760)
(tothemoondogecoin, miles_) = divmod(miles, 238855) # why not 365.25?


print("One trillion inches is the same as going to the moon and back")
print(tothemoondogecoin, "times plus;", miles_, " miles, ", yard_,
      " yards, ", foot_, " feet; and ", inches, " inches")
