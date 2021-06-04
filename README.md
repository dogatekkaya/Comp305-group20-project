"# Comp305-group20-project

DOCTORS WITHOUT SCHEDULES

Our code is a python code.

Test Cases
Doctor A: 8
Doctor B: 8
Doctor C: 8
Patient 1: 4
Patient 2: 1
Patient 3: 4
Patient 4: 1
Patient 5: 4
Patient 6: 1
Patient 7: 4
Patient 8: 1
Time for first given test: 4.3699999999993744e-05

With the RESULT:
Doctor doctor1 sees Patients ['patient8', 'patient6', 'patient4', 'patient2', 'patient1']
Doctor doctor2 sees Patients ['patient5', 'patient3']
Doctor doctor3 sees Patients ['patient7']

Doctor A: 9
Doctor B: 9
Doctor C: 9
Patient 1: 2
Patient 2: 2
Patient 3: 2
Patient 4: 2
Patient 5: 2
Patient 6: 2
Patient 7: 2
Patient 8: 2
Patient 9: 2
Patient 10: 2
Patient 11: 2
Patient 12: 2
Patient 13: 2
Time for second given test: 7.84475e-02 
With no results since it is not applicable.


Test Cases give a result in a pattern of d^p (d being number of docs and p being number of patients) this is because any chosen patient has d number of alternatives for doctors. As can be seen from the runtimes. Time complexity is directly correlated with number of doctors and number of patients. As they increase required time also increases.


Our Attempts at the Solution 


Our first attempt was sorting patients in descending order (the patient with the longest time needed for visiting comes first). 
In the example:  patients (5,3,2,2) and doctors (7,3,2). The patient with 5 hours has only one choice while a patient with 3 hours has 3 choices. If patient with time t1 and doctor with time t1, we need to map them together. Therefore, we decided to change our algorithm. 

Our second attempts was to sort the patients in descending order and sorting doctors in ascending order, and then starting from the first patient and in a loop, finding the first doctor with the shortest time that can visit our current patient. The patient’s time is subtracted from the doctor’s time and it is started over with the next patient and continues until all patients are set to a doctor. 
But in the case of: doctors(5,6) and patients(4,3,2,2), the algorithm wouldn’t work. We also checked if sorting both patients and doctors in descending order and mapping the longest timed patient to the longest timed doctor would work, but it didn’t.  

We then decided on the final solution where nothing is sorted and starting from the first patient, it is mapped to the first doctor possible. The function is recalled and whenever we couldn’t set anymore patients to doctors, we undo our works and start from the beginning until we find out the answer. 
There are two inputs, doctors and patients. In a for loop, a doctor whose available hours are more than the patient’s hours are found. 
Recursion: We settled one patient to one doctor and we call the function again for the rest of the patients, then return true if it was successful.





