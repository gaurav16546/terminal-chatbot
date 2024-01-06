def bot_program(bot):
    while True:
        try:
            print("> ",end=" ")
            user_input = input()

            bot_response = bot.get_response(user_input)

            print(f"🤖 {bot_response}")

        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
