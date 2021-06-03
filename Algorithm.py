# -*- coding: utf-8 -*-
"""

@author: room 20
"""

# START OF THE ALGORITHM
def canAllPatientsBeSeen(doctors, patients):
    if sum(patient[1] for patient in patients) > sum(doctor[1] for doctor in doctors):
        return False
    schedule = {doctors[i][0] : [] for i in range(len(doctors))}
    return canAllPatientsBeSeenHelper(doctors, patients, schedule, 0)

def canAllPatientsBeSeenHelper(doctors, patients, schedule, iterator):
    if iterator == len(patients):
        return schedule
    for doc in doctors:
        if doc[1] >= patients[iterator][1]:
            doc[1] -= patients[iterator][1]
            if canAllPatientsBeSeenHelper(doctors, patients, schedule, iterator+1):
                schedule[doc[0]].append(patients[iterator][0])
                return schedule
            
            doc[1] += patients[iterator][1]
            
    return False
# END OF THE ALGORITHM

# Below are the testing part.
# For printing the the test results
def printTest(result):
    print("\nRESULT")
    if result != False:
        for key in result:    
            print(f"Doctor {key} sees Patients {result[key]}")
    else:
        print("No such appointment exists")
        

# TEST 1    
doctors = [
    ["Jonathan" , 10],
    ["Dimitris" , 8],
    ["Marcel" , 8],
    ["Samantha" , 8]
    ]

patients = [
    ["Mustapha" , 2],
    ["Gregor" , 3],
    ["Michael" , 3],
    ["Alicia" , 3],
    ["Martin" , 1],
    ["Wachowski" , 6],
    ["Mariam" , 8],
    ["Cisse" , 6]
    ]

result = canAllPatientsBeSeen(doctors, patients)
printTest(result)

# TEST 2
doctors = [
    ["doctor1" , 1],
    ["doctor2" , 1],
    ["doctor3" , 1],
    ["doctor4" , 3]
    ]

patients = [
    ["patient1" , 3],
    ["patient2" , 1],
    ["patient3" , 1],
    ["patient4" , 1]
    ]

result = canAllPatientsBeSeen(doctors, patients)
printTest(result)
    
# TEST 3
doctors = [
    ["doctor1" , 6],
    ["doctor2" , 12],
    ["doctor3" , 4],
    ["doctor4" , 3],
    ["doctor5", 7]
    ]

patients = [
    ["patient1" , 1],
    ["patient2" , 1],
    ["patient3" , 1],
    ["patient4" , 1],
    ["patient5" , 2],
    ["patient6" , 2],
    ["patient7" , 3],
    ["patient8" , 4],
    ["patient9" , 4],
    ["patient10" , 5]
    ]

result = canAllPatientsBeSeen(doctors, patients)
printTest(result)
    
# TEST 4
doctors = [
    ["doctor1" , 6],
    ["doctor2" , 5]
    ]

patients = [
    ["patient1" , 4],
    ["patient2" , 4],
    ["patient3" , 3]
    ]

result = canAllPatientsBeSeen(doctors, patients)
printTest(result)
    
