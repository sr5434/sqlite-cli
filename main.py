import sqlite3
import ai

ascii_logo = """
 ___________________________________________________________

   _____  ____  _      _ _               _____ _      _____ 
  / ____|/ __ \| |    (_) |             / ____| |    |_   _|
 | (___ | |  | | |     _| |_ ___ ______| |    | |      | |  
  \___ \| |  | | |    | | __/ _ \______| |    | |      | |  
  ____) | |__| | |____| | ||  __/      | |____| |____ _| |_ 
 |_____/ \___\_\______|_|\__\___|       \_____|______|_____|
                                                            
                                                            
 ___________________________________________________________
"""

print(ascii_logo)
print("Unofficial SQLite CLI")
print("""Commands: 
      - ENTER_NLI: Activate natural language mode
      - EXIT_NLI: Deactivate natural language mode
      - EXIT: Exit the CLI
You can also enter regular SQLite commands. When you are in natural language mode, you can have AI write commands for you.""")

db_name = input("Enter database filename: ")#Get the database filename
con = sqlite3.connect(db_name)#Conect to the database

cur = con.cursor()#Get the cursor

NLI = False#Initialize the NLI state as false
while True:
    query = input("> ")#Get the query from the user
    if query.lower() == "exit":
        con.close()#Close the connection
        break
    elif query.upper() == "ENTER_NLI":
        print("NLI mode activated.")
        NLI = True#Set the NLI state to true
        continue
    elif query.upper() == "EXIT_NLI":
        print("NLI mode deactivated.")
        NLI = False#Set the NLI state to false
        continue
    if not NLI:
        try:
            #Execute and commit
            res = cur.execute(query)
            con.commit()
        except BaseException as e:
            #Inform the user about the error
            print("The command could not be executed due to an error: ", str(e))
        else:
            print(res.fetchall())#Print the output
    else:
        command = ai.text2sql(query)
        print(command)
        if input("Continue? (y/n) ") == "y":
            try:
                res = cur.execute(command)
                con.commit()
            except BaseException as e:
                print("Error: ", str(e))
            else:
                print(res.fetchall())
