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

def feedback_loop(bot):
    while True:
        try:
            print(">", end=" ")
            input_statement = Statement(text=input())
            response = bot.generate_response(
                input_statement
            )

            print('\n Is "{}" a coherent response to "{}"? \n'.format(
                response.text,
                input_statement.text
            ))
            if get_feedback() is False:
                print(f"🤖 'please input the correct one'\n")
                print("> ",end=" ")
                correct_response = Statement(text=input())
                bot.learn_response(correct_response, input_statement)
                print(f"🤖 'Responses added to bot!'")

        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
