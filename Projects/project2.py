name =input ("hello whats your name")
print (f"hello {name} today u are answering questions to tell you what ur favorite season is") 
winter_points = 0
spring_point = 0
summer_points = 0
fall_points = 0
answer1 = input("would you rather have it A Rain B Snow C Cloudy D Be sunny")
if answer1 == "A":
    spring_point += 1 
elif answer1 =="B":
    winter_points += 1
elif answer1 == "C":
    fall_points += 1
elif answer1 == "D":
    summer_points += 1
 
answer2 = input("what is your favorite activity A jump in puddles B ski or snowboard C rake leaves D swim")
if answer2 == "A":
    spring_point+= 1
elif answer2 == "B":
        winter_points += 1
elif answer2 =="C":
        fall_points += 1
elif answer2 == "D":
        summer_points += 1

answer3 = input(" do you prefer A short sleeves B sweatshirt C long sleave D tank top")
if answer3 =="A":
        spring_point += 1
elif answer3 == "B":
        winter_points += 1
elif answer3 == "C":
         fall_points += 1
elif answer3 == "D":
        summer_points += 1 
answer4 = input("do you prefer A warm colors or B cold colors") 
if answer4 == "A":
      spring_point +=1
      summer_points +=1
elif answer4 == "C":
      winter_points += 1
      fall_points += 1
answer5 = input(" do you like A baseball B skiing C soccer D golf ")
if  answer5 == "A":
      spring_point += 1
elif answer5 == "B":
    winter_points += 1 
           





