''' Question:- Write a Python program to find the alphabet character with the maximum occurrence in a given list of lowercase characters.
               If no character appears more than once, print "No Duplicates Present".'''


# Function to find character with maximum occurrence
def findMaxOcc(arr):

    count = [0] * 26  # Frequency array for a–z

    # Count frequency of each character
    for ch in arr:
        index = ord(ch) - ord('a')  # Convert char to index (0–25)
        count[index] += 1

    maxCount = 0
    result = ''

    # Find character with maximum frequency
    for i in range(26):
        if count[i] > maxCount:
            maxCount = count[i]
            result = chr(i + ord('a'))  # Convert index back to character

    # Print result
    if maxCount <= 1:
        print("No Duplicates Present")
    else:
        print("Character:", result)
        print("Frequency:", maxCount)


# ---------------- Main Program ----------------

if __name__ == "__main__":

    T = int(input("Enter number of test cases: "))

    while T > 0:
        n = int(input("Enter number of characters: "))

        arr = []  # Fresh array for each test case

        for _ in range(n):
            arr.append(input().strip())

        findMaxOcc(arr)

        T -= 1