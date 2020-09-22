print("""Daily Horroscope

Welcome to daily horroscope predictor.

There are 12 zodiac symbols:
1)Aries
2)Taurus
3)Gemini
4)Cancer
5)Leo
6)Virgo
7)Libra
8)Scorpio
9)Sagittarius
10)Capricorn
11)Aquarius
12)Pisces\n\n""")

d=int(input("enter today's date: "))
m=int(input("enter the month: "))
y=int(input("enter the year: "))

print("")

opt=True

while(opt is True):
    i=str(input("What's your zodiac sign(Enter the name of the zodic sign, or the number corresponding to the above list: \n"))
    i=i.lower()
    if (i=="aries" or i=='1'):
        print("Your Horroscope of",d,"/",m,"/",y,"is:\nAccidents are called accidents for a reason. They happen through no one person's concerted efforts. They just happen. If you are involved in a fender bender or any other type of collision (real or metaphorical), avoid taking it personally. Things happen, and every time you can let the stress roll off of your back, you grow and learn. Of course, if you are in a situation where you know someone is working against you, you should feel free to unsheath your claws.")
    elif (i=="taurus" or i=='2'):
        print("Your Horroscope of",d,"/",m,"/",y,"is:\nThe art of flirtation takes a lot of time to learn, but you are becoming quite an expert. It's time to stop holding back and start using those killer skills you have learned! If you have someone in your sights, romantically speaking, today is the day to make that connection. Ask a pertinent question or two and help them see you in a new light. If you are currently in a relationship, get ready for things to go to a much hotter level.")
    elif (i=="gemini" or i=='3'):
        print("Your Horroscope of",d,"/",m,"/",y,"is:\nYou need to know where to go for the information that will help you most in life. Instead of asking friends for advice on how to fatten up your rapidly thinning piggy bank, ask an expert. Friends are who you should talk to about your love life, work hassles, and other personal issues. But when it comes to credit, investments, and your savings account, you don't want to mix those two worlds. Sharing too much about how much money you make or have could also create unnecessary friction.")
    elif (i=="cancer" or i=='4'):
        print("Your Horroscope of",d,"/",m,"/",y,"is:\nGet out your finest fine-toothed comb because you'll need to go over some very fine print one more time. There are an awful lot of small details that could grow into big, embarrassing issues later on down the line if you don't nip them in the bud now. Probably the last thing you want to do is proofread or double-check your work one more time, but you should do it. It will save you a lot more of your time (and your pride) in the long run.")
    elif (i=="leo" or i=='5'):
        print("Your Horroscope of",d,"/",m,"/",y,"is:\nDespite the fact that you're feeling better than you have in a while, right now is not the time to go out and celebrate. You are not overly impulsive as a rule, but today you should behave even more conservatively than usual. Bide your time and the right opportunity to have a blast will present itself soon enough. Skip any splurges and stay close to home. You can have just as celebratory a time cuddled up with a good book or your partner as you can at a big party.")
    elif (i=="virgo" or i=='6'):
        print("Your Horroscope of",d,"/",m,"/",y,"is:\nToday is a great day to try a new food, hobby, sport, or adventure that you have always been just a little to scared to try before. Your fears are starting to vanish and your courage is growing, in part because your mind is hungry for new stimulation—even if that stimulation is based on fear! You will be totally fiery and full of energy, so put it to good use by pushing the envelope and pushing past one or two of the boundaries you've built for yourself.")
    elif (i=="libra" or i=='7'):
        print("Your Horroscope of",d,"/",m,"/",y,"is:\nIf you are stuck in the middle of a dilemma right now, doing something that you think is right (even if you aren't totally sure it's right) is better than doing nothing at all. Stop trying to nail down every single detail. You can't eliminate every potential problem. It's time to start acting! Things are never going to be perfect, so if you're waiting until they are, you will be waiting a very long time—too long, in fact. You need to keep moving even if you don't know exactly where you're going.")
    elif (i=="scorpio" or i=='8'):
        print("Your Horroscope of",d,"/",m,"/",y,"is:\nCan you have too many friends? The answer, you may be beginning to fear, is yes! There are only so many free hours in your week, and it might be getting tough to prioritize who gets to share them with you. Friendships take as much work as anything else does, but the payoff is truly rewarding. See what you can do to show your friends how much you care.")
    elif (i=="sagittarius" or i=='9'):
        print("Your Horroscope of",d,"/",m,"/",y,"is:\nThe people you associate with today will be very important. Some people will seem to be right on your wavelength, but others may drive you absolutely crazy! As soon as you feel that someone is rubbing you the wrong way, distance yourself from them. You aren't in the right frame of mind to deal with feeding people's egos or sacrificing your own desires. What you need now is to be surrounded by people who get you, the people who use the same shorthand you use.")
    elif (i=="capricorn" or i=='10'):
        print("Your Horroscope of",d,"/",m,"/",y,"is:\nAre you running the risk of getting too big for your britches? Just in case, you should give yourself a reality check today before someone else does! Make an effort to get more grounded. Spend time with people who live a different lifestyle. Get a glimpse of what their biggest issues, goals, and concerns are. Just a little bit of effort will wake you up to the reality of your situation and make you much more grateful for what you have.")
    elif (i=="aquarius" or i=='11'):
        print("Your Horroscope of",d,"/",m,"/",y,"is:\nThis might seem like a typical day early on, but as each hour goes by, you could start to see more and more mysterious actions and events cropping up. Who are the perpetrators? What are they up to!? If you look beneath the surface, you will start to see a pattern and an agenda. This is something exciting, and you should not ignore it. Try to get involved in their shenanigans and you will have a lot of fun. They could use a bright, witty person like you!")
    elif (i=="pisces" or i=='12'):
        print("Your Horroscope of",d,"/",m,"/",y,"is:\nA relationship that you thought was broken beyond all repair still has some life in it. Figure out how you can put it on the road to recovery. There are two people involved in this messy situation, and each of you has your own apologies to make. Be a hero and be the first one to extend an olive branch. Call or e-mail them today. Let them know you're thinking about them and be honest about how you feel. Let down your guard and speak from the heart.")

    else:
        print("please Enter a valid zodiac sign!! ")

    opt=True if input("\n\nwant to try again? (y/n): ")=='y' else False
                      
