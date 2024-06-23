#question:answer

qna = {
    "Hi":"hey",
    "how are you":"I am fine",
    "what is your name":" My name is AI master",
    "how old are you":"I am on continue update loop",
    "can you help me":"Yes, please type your query below",
    "today's weather in delhi":"In Delhi today's temprature is 41 degree celcius",
    "bye":"Bye! Thankyou have a nice day",
}

while True:
    qs = input()

    if(qs == "quit"):
        break
    
    else:
        print(qna[qs])
        