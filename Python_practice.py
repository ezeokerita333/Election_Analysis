
counties = ["Arapahoe", "Denver", "Jefferson"]
#if counties[1] == 'Denver':
    #print(counties[1])

#temperature = int(input("what is the temperature outside"))

#if temperature > 80:
    #print('turn on the AC.')
#else:
    #print("Open the window")

#score = int(input('what is your test score?'))

#if score >= 90:
    #print('your grade is an A.')
#else:
    #if score >= 80:
        #print('your grade is a B.')
    #else:
        #if score >= 70:
            #print('your grade is a C.')
        #else:
            #if score >= 60:
                #print('your grade is a D.')
            #else:
                #print('your grade is a F.')

#counties = ['Arapahoe','Denver','Jefferson']
#if "El paso" in counties:
    #print ('El paso is in the list of counties')
#else:
    #print('El paso is not in the list of counties.')

#x = 0
#while x <= 5:
    #print (x)
    #x = x + 1

#count = 7
#while count < 1:
    #print('hello world')

#for county in counties:
    #print(county)
    
#for num in range(5):
        #print(num)

#for i in range(len(counties)):
    #print(counties[i])

#counties_dict = {'Arapahoe':422829, 'Denver':463353,'Jefferson':432438}
#for county in counties_dict.keys():
    #print (county)

#for voters in counties_dict.values():
    #print (voters)

#for county, voters in counties_dict.items():
    #print('county' county has 'voters' registered voters)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
    #for value in county_dict.values():
         #print (value)

for  county_dict in voting_data:
    print (county_dict['registered_voters'])
