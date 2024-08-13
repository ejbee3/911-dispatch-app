
from playsound import playsound
from helpers import get_numbers_as_ints, make_tts_file, get_test_length
import time
import asyncio


# TODO: structure quiz so you pick random numbers in increasingly difficulty
#       make console ui to tell you not to type until you see the words GO! on the screen
#       number holding game -- title  
async def main():
      amt_correct = 0
      # instructions
      print()
      print('''       Welcome to the number holding game, 
            where you test your memory to see how 
            well you can remember numbers of different length!''')
      print()
      num_of_tests = int(input("~~Choose the number of tests (must be a whole number)~~ "))
      print()
      difficulty = input("~~Choose your difficulty: easy (e), medium (m), hard (h)~~")
      print()
      # main game loop
      for i in range(0, num_of_tests):
            test_id = i + 1
            numbers_as_int_arr = get_numbers_as_ints(get_test_length(difficulty))
            test_file = await make_tts_file(numbers_as_int_arr, test_id)
            playsound(test_file)
            time.sleep(5)
            number = input('GO! ')
            correct_in_number = 0
            for i, n in enumerate(number):
                  if n == str(numbers_as_int_arr[i]):
                        correct_in_number += 1
            if correct_in_number == len(numbers_as_int_arr):
                  amt_correct += 1
      print(f'correct percentage: {int((amt_correct / num_of_tests) * 100)}%')

      
      
      
      
            
    


if __name__ == '__main__':
    asyncio.run(main())