import time
import sys

def delay_print(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def ddelay_print(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)

def beginning_text():
    delay_print("You wake up in a tavern with no previous memory of before.")

def beginning():
    beginning_text()
    action = int(input("1 To leave the tavern. \n2 To go get another drink. \n3 To go ask the bartender where you are. \n>"))
    if action == 1:
    	townsquare()
    elif action == 2:
        another_drink()
        death()
    elif action == 3:
	    bartender()

def townsquare():
    delay_print("\nYou walk out into the townsquare and are blinded by the sun.")
    delay_print("When your eyes adjust you find that there are people bustling \naround doing their morning chores.")
    action = int(input("1 Go help the lady who seems to be struggling to carry a sack. \n2 Take a drink from the fountain in the middle of the square. \n3 Go into the expensive building on your right for some shade. \n>"))
    if action == 1:
	    help_her()
    elif action == 2:
        fountain()
    elif action == 3:
	    doctor()

#townsquare
def help_her():
    delay_print("\nYou go up to the lady and ask her if she'd like any help with")
    delay_print("her sack. She gives you a look as if deciding if you're trustworthy ")
    delay_print("before she nods. You pick up the sack and ask her where she's ")
    delay_print("going. She tells you that she's going home and that her house ")
    delay_print("is on the other side of town.")
    action = int(input("1 THAT'S TOO FAR! You drop the sack and leave. \n2 You smile and start the treck together towards her house.\n>"))
    if action == 1:
        lady_leave()
    elif action == 2:
        happy_lady_end()

#townsquare
def lady_leave():
    delay_print("\nBecause you drop the sack, it opens and potatoes and vegetables")
    delay_print("roll into the street. The lady sighs, looking like she's about ")
    delay_print("to cry and starts to gather the food. She is very pointedly ")
    delay_print("not looking at you.")
    action = int(input("1 You help her pick up her food and apologize. \n2 You run into the fancy building.\n>"))
    if action == 1:
        lady_apologize()
    elif action == 2:
        doctor()

#townsquare
def fountain():
    delay_print("\nYou go to take a drink the fountain. The water is sparkling ")
    delay_print("and it's clear and cool looking. You scoop your hands into the ")
    delay_print("water and find that it really as cold as you thought it was. ")
    delay_print("The water slides down your throat deliciously and you feel as ")
    delay_print("if you've been cured of all sin in life.")
    action = int(input("1 That lady is still struggling with her sack. You decide to go help. \n2 You look back at the fancy building and decide that you really should go in there.\n>"))
    if action == 1:
        help_her_two()
    elif action == 2:
        doctor()

#townsquare
def help_her_two():
    delay_print("\nYou go up to the lady and ask her if she'd like any help with ")
    delay_print("her sack. She gives you a look as if deciding if you're trustworthy ")
    delay_print("before she nods. You pick up the sack and ask her where she's ")
    delay_print("going. She tells you that she's going home and that her house ")
    delay_print("is on the other side of town.")
    action = int(input("1 THAT'S TOO FAR! You drop the sack and leave. \n2 You smile and start the treck together towards her house.\n>"))
    if action == 1:
        lady_leave()
    elif action == 2:
        truly_happy_lady_end()

#ending
#townsquare
def truly_happy_lady_end():
    delay_print("\nShe smiles at you and takes the arm that's not weighed down ")
    delay_print("with the sack. Since it's such a long walk to her house, you learn ")
    delay_print("lots about her and find out that you really enjoy her company.")
    delay_print("You guys end up spending more and more time together before you ")
    delay_print("get married and have 3 kids who are the joy of your lives.")
    delay_print("You both live happily to an old age.")

#townsquare
def lady_apologize():
    delay_print("\nYou feel really bad for acting so ridiculously and help her. ")
    delay_print("Once you are done and everything is back in the sack, you apologize ")
    delay_print("profusely. She accepts your apology on the pretense that you ")
    delay_print("still walk her home. You accept.")
    happy_lady_end()

#ending
def happy_lady_end():
    delay_print("\nShe smiles at you and takes the arm that's not weighed down by")
    delay_print("the sack. Since it's such a long walk to her house, you learn ")
    delay_print("lots about her and find out that you really enjoy her company.")
    delay_print("You guys end up spending more and more time together before you ")
    delay_print("get married and have 3 kids who are the joy of your lives. You ")
    delay_print("have a happy ending, but you don't live long after 50 because")
    delay_print("of all the alcohol you consumed when you were younger. You ")
    delay_print("never remember your previous life.")

#doctor
def doctor():
    delay_print("\nYou go into the fancy building. There's a sign on the door")
    delay_print("that says Dr. Lavor. There doesn't seem to be anyone around.")
    action = int(input("1 Ring the bell on the counter in front of you. \n2 You stand around awkwardly. \n3 You decide to leave again.\n>"))
    if action == 1:
        ringbell()
    elif action == 2:
        awkwardly_stand()
    elif action == 3:
        townsquaretwo()

#doctor
def awkwardly_stand():
    delay_print("\nYou admire the things around you as you stand there. Awkwardly.")
    action = int(input("1 You get tired of waiting and leave. \n2 You contiue to wait.\n> "))
    if action == 1:
        townsquaretwo()
    elif action == 2:
        continuewaiting()

#doctor
def continuewaiting():
    delay_print("\nAs you're still waiting a very tall person comes in with ")
    delay_print("spectacles on his nose. He seems distracted by some type of paper")
    delay_print("in his hands, but you make a startled noise in the back of your ")
    delay_print("throat. He looks up at you.")
    action = int(input("1 You continue being awkward and say hi. \n2 You turn tail and LEAVE.\n>"))
    if action == 1:
        sayhiawk()
    elif action ==2:
        townsquaretwo()

#doctor
def sayhiawk():
    delay_print("\nHe nods to let you know that he heard you and gets back to ")
    delay_print("looking at his paper before putting it on the stack next to the")
    delay_print("bell. He motions you to follow him as he goes back through the ")
    delay_print("door he came in. ")
    action = int(input("1 You follow him back. \n2 You leave because that's ominious and he hasn't said anything to you yet.\n>"))
    if action ==1:
        followhim()
    elif action ==2:
        townsquaretwo()

#doctor
def followhimtwo():
    delay_print("\nYou go through a couple of sets of doors before you enter a")
    delay_print("smaller room with a padded table, a couple of chairs, and a desk.")
    delay_print("He motions you to sit down on the table. You do so because you're ")
    delay_print("not sure you could run anymore if you wanted to. He does various ")
    delay_print("things that you don't understand and uses many different types")
    delay_print("of instruments. He makes a noise, then sits down at his desk to ")
    delay_print("write down a couple of things. After a couple minutes of scribbling, ")
    delay_print("he turns around in his chair and takes off his glasses. He ")
    delay_print("informs you that you have amensia and that you are severely ")
    delay_print("dehydrated as well as suffering from a failing liver. He hands ")
    delay_print("you a couple of bottles and tells you to take them.")
    action = int(input("1 Thank him for the bottles and leave. \n2 Thank him for the bottles and ask him if you can stay the night there because you have nowhere else to go.\n>"))
    if action == 1:
        thankbottles()
    elif action == 2:
        stay()

#ending
#doctor
def stay():
    delay_print("\nThe man nods and introduces himself as Dr. Lavor. He seems ")
    delay_print("very pleased that you are going to stay. Although you had ")
    delay_print("decided to stay only one night, you end up staying every night ")
    delay_print("after that. Dr. Lavor takes you under his wing and teaches you ")
    delay_print("all about his research and job. After a couple of years, he tells ")
    delay_print("you his secert. ")
    ddelay_print("He kills people to do experiments on them.")
    delay_print("You are shocked and disgusted, but you go along with him and ")
    delay_print("begin to help him. You do have a debt to the man for saving you")
    delay_print("anyway. And that's what you do for the rest of your days, helping ")
    delay_print("Dr. Lavor with his research, UNTIL One day, you have had enough ")
    delay_print("and you kill him yourself. You inform the police and they take ")
    delay_print("you in because of your viligante justice. In trial, they try to ")
    delay_print("go easy on you. Giving you only 2 years in prison, instead of ")
    delay_print("the death sentence. You hone many skills in prison and when you ")
    delay_print("get out, you're ready to start out on a new adventure.")

#doctor
def thankbottles():
    delay_print("\nYou down one of the bottles when you leave and look around at ")
    delay_print("the townsquare. The lady has left and you do not want to return ")
    delay_print("back to the tavern after what the tall man told you. Before you ")
    delay_print("left, the man told you that it was going to be a very cold night ")
    delay_print("and that you should find some shelter. You look around for a ")
    delay_print("place to stay.")
    action = int(input("1 Go to the building that says 'inn' on it. \n2 Decide to sleep in the square.\n>"))
    if action == 1:
        inn()
    elif action == 2:
        death()

#ending
#inn
def inn():
    delay_print("\nYou ask to stay at the inn, promising that you'll pay back ")
    delay_print("the room you stay in with your hard labor. The lady at the front")
    delay_print("table nods and accepts your proposal. You stay at the inn for a ")
    delay_print("couple of weeks before you start to notice the lady who runs it ")
    delay_print("more. Because you do a lot of the hardwork for her, you get to ")
    delay_print("know her more. Before long you're asking her out on dates and ")
    delay_print("giving her small presents you pay for from other jobs outside the inn.")

#ending
#doctor
def followhim():
    delay_print("\nYou follow him apprehensively. You go through a couple sets ")
    delay_print("of doors befoer you enter a smaller room with a padded table, a ")
    delay_print("couple of chairs, and a desk. He motions you sit down on the table.")
    delay_print("You do so because you're not sure you could run anymore if you ")
    delay_print("wanted to. He brings out a syringe and pushes down on your arm, ")
    delay_print("holding you in place. You ask him what's in the syringe and he ")
    delay_print("mumbles a name before inserting it into your arm and pushing on ")
    delay_print("the back of it. You ask him to repeat what he said and he turns ")
    delay_print("to you and says that he needs more corpses for his research. ")
    delay_print("Your body begins to feel heavy and your eyelids droop closed.")
    delay_print("Before your eyes close completely, you catch him smirking at you.")
    death()

#doctor
def ringbell():
    delay_print("\nYou ring the bell and wait patiently. There's a stack of ")
    delay_print("papers next to bell and your curiousity gets the best of you.")
    delay_print("You shuffle through the papers a bit before a voice says hello, ")
    delay_print("startling you. You drop the papers creating a huge mess.")
    action = int(input("1 Pick up the papers and apologize. \n2 Say hello and act like you didn't just drop a stack of papers on the floor. \n3 RUN\n>"))
    if action == 1:
        paperapologize()
    elif action == 2:
        stackdrop()
    elif action == 3:
        townsquaretwo()

#doctor
def paperapologize():
    delay_print("\nThe tall man sighs and bends down to help you pick up the papers. ")
    delay_print("He does not answer to your apology, but instead nods. He stands ")
    delay_print("up and asks you if you have an appointment.")
    action = int(input("1 RUN \n2 Tell him you don't \n3 Tell him you do \n>"))
    if action == 1:
        townsquaretwo()
    elif action == 2:
        noappointment()
    elif action == 3:
        appointment()

#doctor
def noappointment():
    delay_print("\nA brief flash of surprise passes on his face before it's gone. ")
    delay_print("He admits that he didn't expect you to tell the truth and asks ")
    delay_print("you to follow him back anyway because you look worse for wear.")
    action = int(input("1 You follow him. \n2 RUN\n>"))
    if action == 1:
        followhimtwo()
    elif action == 2:
        townsquaretwo()

#doctor
def appointment():
    delay_print("\nThe man raises another eyebrow at you and asks you if you'd ")
    delay_print("follow him back because he has something he'd like to give you.")
    action = int(input("1 You follow him. \n2 RUN\n>"))
    if action == 1:
        followhim()
    elif action == 2:
        townsquaretwo()

#doctor
def stackdrop():
    delay_print("\nThe man looks at you questioningly and a little exasperated,")
    delay_print("but he says hello back and asks you if you have an appointment.")
    action = int(input("1 Tell him you don't \n2 Tell him you do \n3 RUN\n>"))
    if action == 1:
        noappointmenttwo()
    elif action == 2:
        appointmenttwo()
    elif action == 3:
        townsquaretwo()

#doctor
def noappointmenttwo():
    delay_print("\nThe man nods and asks you to follow him back.")
    action = int(input("1 You follow him. \n2 RUN\n>"))
    if action == 1:
        followhim()
    elif action ==2:
        townsquaretwo()
#doctor
def appointmenttwo():
    delay_print("\nHe raises his eyebrow and says 'oh really?' before asking you ")
    delay_print("to follow him back.")
    action = int(input("1 You follow him. \n2 RUN\n>"))
    if action == 1:
        followhim()
    elif action == 2:
        townsquaretwo()

#townsquare
def townsquaretwo():
    delay_print("\nIt appears that the lady struggling with her sack has left. ")
    delay_print("You have no where else to go, so you sit down in an alley and ")
    delay_print("go to sleep. Although, the weather is terrible that night and")
    delay_print("you freeze to death.")
    death()

#tavern
def another_drink():
    delay_print("\nYou decide to take another drink, but you've already drank ")
    delay_print("way too much.")

#tavern
def bartender():
    delay_print("\nThe bartender looks at you and smiles as he cleans a glass. ")
    delay_print("He seems very jolly and happy to help you. He tells you that you")
    delay_print("are at Angus's Tavern.")
    action = int(input("1 You ask him if he could give you a glass of water. \n2 You ask him if his name is Angus. \n3 You thank him and leave the tavern.\n>"))
    if action == 1:
        water()
    elif action == 2:
        tradenames()
    elif action == 3:
        townsquare()

#tavern
def water():
    delay_print("\nThe bartender seems very happy to help and he gives you a ")
    delay_print("glass of water. You feel as if you have saved yourself from ")
    delay_print("certain death by drinking this amazing wonderful water.")
    action = int(input("1 You thank him and leave the tavern. \n2 You ask the nice bartender if his name is Angus. \n3 You ask the bartender if he knows what happened last night. \n>"))
    if action == 1:
        townsquare()
    elif action == 2:
        tradenames()
    elif action == 3:
        whathappened()

#tavern
def tradenames():
    delay_print("\nThe bartender laughs a big belly laugh and confirms that his ")
    delay_print("name is indeed Angus. He asks you what your name is, but you ")
    delay_print("can not recall for the life of you what your name is.")
    action = int(input("1 Thank him and run out of the tavern. \n2 Make up a name. \n3 Explain that you, in fact, don't remember your name or know what it is. \n>"))
    if action == 1:
        townsquare()
    elif action == 2:
        madeupname()
    elif action == 3:
        explanation()

#tavern
def madeupname():
    delay_print("\nYou quickly proclaim that your name is James Hamilton. The ")
    delay_print("bartender looks at your strangely, but nods. You panick more ")
    delay_print("and run out of the tavern.")
    townsquare()

#tavern
def explanation():
    delay_print("\nYou explain that you really don't remember who you are or what")
    delay_print("your name is. The bartender gives you a sympathetic pat on your")
    delay_print("arm. He invites you to start working at the tavern since you ")
    delay_print("have no other place to go and don't remember anything.")
    action = int(input("1 You accept. \n2 You decline.\n>"))
    if action == 1:
        acceptwork()
    elif action == 2:
        declinework()

#ending
#tavern
def acceptwork():
    delay_print("\nSince you have accepted, you have found that working at the ")
    delay_print("tavern has given you a sense of fullfilment. Angus, the bartender,")
    delay_print("is very nice and fun to chat with during breaks. You meet all ")
    delay_print("types of people in the tavern and soon you have a gaggle of ")
    delay_print("stories that could wow anyone from all the people you've talked ")
    delay_print("to over the years. You write all their stories down in a book ")
    delay_print("and it's published. Your book becomes a bestseller and soon ")
    delay_print("you're a famous auhtor. You live a good life and Angus and you ")
    delay_print("continue to be good friends. You die of mysterious circumstances ")
    delay_print("one day though. A doctor supposes it is from the damage to your ")
    delay_print("liver from heavy drinking.")

#tavern
def declinework():
    delay_print("\nSince you declined, you decide that you should probably leave. ")
    delay_print("You thank the bartender for his hospitality and leave.")
    townsquare()

#tavern
def whathappened():
    delay_print("\nThe bartender tells you that you had one too many drinks and ")
    delay_print("ended up passing out on the table. He tells you that he didn't ")
    delay_print("have the heart to tell you to leave because you seemed really")
    delay_print("out of it. He gives you a couple of minutes to sink that in.")
    action = int(input("1 Ask him if you can have another drink. \n2 Thank him for telling you and leave. \n3 Start crying.\n> "))
    if action == 1:
        another_drink()
        death()
    elif action == 2:
        townsquare()
    elif action == 3:
        cry()

#tavern
def cry():
    delay_print("\nYou start to cry because life is hard. Although, you are ")
    delay_print("still severly dehydrated.")
    death()

#ending
def death():
    print("YOU DIE")

while True:
    beginning()
    while True:
        answer = input("Play again? (y/n): ")
        if answer in ("y", "n"):
            break
        print("Invalid input.")
    if answer == "y":
        continue
    else:
        delay_print("Thank you for playing!")
        sys.exit
        break
