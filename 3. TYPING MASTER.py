import time

def typing_test():
    text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood? A woodchuck could chuck as much wood as a woodchuck could if a woodchuck could chuck wood.'
    print('Type the following text: \n')
    print(text + '\n')

    input('Press Enter when you are ready to start....')
    start_time = time.time()

    user_input = input('> ')

    end_time = time.time()
    elapsed_time = end_time - start_time

    correct_characters = 0
    for i in range (min(len(text), len(user_input))):
        if text[i] == user_input[i]:
            correct_characters +=1

        accuracy = (correct_characters / len(text)) * 100
        words_per_minute = len(user_input.split()) / (elapsed_time / 60)

        print('\n------ Typing Test Result ------')
        print('Time Elapsed: {:.2f} seconds'.format(elapsed_time))
        print('Accuracy: {:.2f}%'.format(accuracy))
        print('Words per minute: {:.2f}'.format(words_per_minute))

typing_test()