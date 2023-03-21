import random
import hashlib


with open('data.txt', 'r') as f:
    data = f.readlines()

PH = "None"  # Now the first step would be to begin initialisation of the previous block to none

for line in data:
    semester_number = line[1:3]
    courses = [line[i:i+9] for i in range(3, len(line), 9)]  # The courses that we have taken has to be extracted (such that 9 characters each)
    RN = random.randint(1, 1000000)  # This would be responsible for generating a random number anywhere between 1 to 1000000
    CH_data = " ".join(courses)  # The courses that are taken will be taken into a singular string through concatenation
    CH = hashlib.sha256(CH_data.encode()).hexdigest()  # Generation of SHA-256 will be done for the block data

    # Printing the information of block in the given format below:
    print("PH:", PH)
    print("D:", line.strip())
    print("RN:", RN)
    print("CH:", CH)
    print()

    PH = CH  # For the next iteration, this will set the previous block has to the current block hash. Hence, PH = CH


