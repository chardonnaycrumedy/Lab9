############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.

counter = 1
keepLoopGoing = True
while(keepLoopGoing):
    print 'What is your temperature?'
    temp = int(raw_input())
    print 'Have you been sick in the last 24 hours?'
    sick = raw_input()
    print 'Have you recently traveled to West Africa?'
    travel = raw_input()
    counter = counter + 1
    
    if temp > 105:
        print 'The patient needs to be checked in.'
    elif temp >102 + sick == "yes": 
        print 'The patient needs to be checked in.'
    elif temp >100 + sick == "yes" + travel == "yes":
        print 'The patient needs to be checked in.'
            
    print 'Are all pateints entered?'
    userInput = raw_input()
    if userInput == 'yes':
        keepLoopGoing = False



