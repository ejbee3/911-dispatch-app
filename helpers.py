from openai import OpenAI
import inflect
import random
from dotenv import dotenv_values


API_KEY = dotenv_values(".env")["api_key"]


def get_numbers_as_ints(length_of_test):
    num_arr = []
    for _ in range(0, length_of_test):
        num_arr.append(random.randint(0,9))
    return num_arr


async def make_tts_file(num_arr, test_num):
    word_arr = []
    p = inflect.engine()
    for n in num_arr:
        word_arr.append(p.number_to_words(n))
    word_str = ' '.join(word_arr)
    output_file = f"audio/test{test_num}.mp3"
    client = OpenAI(api_key=API_KEY)
    async with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="nova",
        input=word_str
      ) as response:
        await response.stream_to_file(output_file)
    return output_file


def get_test_length(difficulty_level):
    if difficulty_level == 'e':
        return 4
    elif difficulty_level == 'm':
        return 7
    elif difficulty_level == 'h':
        return 10
    else:
        raise ValueError


