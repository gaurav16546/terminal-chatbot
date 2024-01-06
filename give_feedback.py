from chatterbot.conversation import Statement

def get_feedback():

    text = input()

    if 'yes' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    else:
        print('Please type either "Yes" or "No"')
        return get_feedback()

def feedback_loop(bot,trainer):
    while True:
        try:
            print(">", end=" ")
            user_input = input()
            input_statement = Statement(text=user_input)
            response = bot.get_response(input_statement)

            print('\n Is "{}" a coherent response to "{}"? \n'.format(
                response.text,
                input_statement.text
            ))
            if get_feedback() is False:
                print(f"🤖 'please input the correct one'\n")
                correct_response = input()
                correct_response_statement= Statement(text=correct_response)
                # bot.learn_response(correct_response_statement, input_statement)
                trainer.train([input_statement.text,correct_response_statement.text])
                print(f"🤖 'Responses added to bot!'")

        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            print("\nExiting feedback loop...")
            break
