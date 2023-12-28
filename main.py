# Import necessary classes and modules
import input_prompt as P
import input_keywords as K
import chat_manager as C
import sys

# Specify the folder path and chat name
program_path = "C:/Users/Chef/Desktop/GroupGPT/"
folder_path = "chats"
data_path = "data/keywords.gpt"

# Create an instance of the Prompt class
promptManager = P.Prompt()
keywordManager = K.Keyword(program_path + data_path)
ChatManager = C.ChatManager("training", program_path)

# Get Message
ChatManager.create_existing_chats(program_path + folder_path)
ChatManager.append_current_chat(promptManager.get_new_prompt(sys.argv))
