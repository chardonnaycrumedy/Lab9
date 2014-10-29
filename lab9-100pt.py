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

keepLoopGoing == True:

print 'What is your temperature?'
userInput = int(raw_input())
print 'Have you been sick in the last 24 hours?'
userInput = raw_input()
print 'Have you recently traveled to West Africa?'
userInput = raw_input()

    if userInput > 105:
        print 'The patient needs to be checked in.'
    elif userInput >102 + userInput == yes: 
        print 'The patient needs to be checked in.'
    elif userInput >100 + userInput == yes + userInput == yes:
        print 'The patient needs to be checked in.'
        
print 'Would you like to stop?'
keepLoopGoing == False



