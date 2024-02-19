# Initialize Personality List
personality1 = [0] * 8

# Introduction
print ("\n\x1B[51m BuzzFeed Personality Quiz! \x1B[0m")
print ("Take this quiz to figure out your personality type.")
print ("\nIn this world of people who have varying personalities because of different factors,\nit can be challenging to understand the type of people you face on an every day basis.\nHowever, no need to fret because through this quiz you will be able to assess not only\nyour personality, but also the personalities of other people as well.")

# Get User Input to Begin Quiz
userinput = input ("\nIf you want to begin the quiz, \x1B[35mtype anything\x1B[0m to start: ")
if not userinput:
    exit ()

def main ():
  # Question No. 0
  global name1
  name1 = input ("\n1. First, please enter your \x1B[35mname\x1B[0m: ")

  # Question No. 1
  question1 = input ("2. Are you (a) more \x1B[35moutwardly\x1B[0m focused, (b) more \x1B[35minwardly\x1B[0m focused, or (c) you are not sure? ")
  if question1 == "a":
    personality1 [0] = 1
  elif question1 == "b":
    personality1 [1] = 1
  elif question1 == "c":
    question1a = input ("   Are you (a) more \x1B[35mtalkative\x1B[0m and \x1B[35moutgoing\x1B[0m, or (b) more \x1B[35mreserved\x1B[0m and private? ")
    if question1a == "a":
      personality1 [0] = 1
    elif question1a == "b":
      personality1 [1] = 1
    else:
      if name1 == "":
        exit ("\nOops! Looks like something went wrong! Please try again later.")
      else:
        exit ("\nOops! Looks like something went wrong! Please try again later, " + name1.title () + ".")
  else:
    if name1 == "":
      exit ("\nOops! Looks like something went wrong! Please try again later.")
    else:
      exit ("\nOops! Looks like something went wrong! Please try again later, " + name1.title () + ".")

  # Question No. 2
  question2 = input ("3. Do you (a) like to take in information \x1B[35mrealistically\x1B[0m, \x1B[35mpractically\x1B[0m, and \x1B[35mliterally\x1B[0m,\n   (b) take in information more \x1B[35mimaginatively\x1B[0m, \x1B[35mconceptually\x1B[0m, and \x1B[35mfiguratively\x1B[0m, or (c)\n   you are not sure? ")
  if question2 == "a":
    personality1 [2] = 1
  elif question2 == "b":
    personality1 [3] = 1
  elif question2 == "c":
    question2a = input ("   Do you (a) pay attention to \x1B[35mfacts\x1B[0m and \x1B[35mdetails\x1B[0m, or (b) notice the \x1B[35mbig picture\x1B[0m and see\n   how \x1B[35meverything connects\x1B[0m? ")
    if question2a == "a":
      personality1 [2] = 1
    elif question2a == "b":
      personality1 [3] = 1
    else:
      if name1 == "":
        exit ("\nOops! Looks like something went wrong! Please try again later.")
      else:
        exit ("\nOops! Looks like something went wrong! Please try again later, " + name1.title () + ".")
  else:
    if name1 == "":
      exit ("\nOops! Looks like something went wrong! Please try again later.")
    else:
      exit ("\nOops! Looks like something went wrong! Please try again later, " + name1.title () + ".")

  # Question No. 3
  question3 = input ("4. Do you prefer to (a) make \x1B[35mdecisions\x1B[0m more \x1B[35mlogically\x1B[0m, \x1B[35mfairly\x1B[0m, and \x1B[35mreasonably\x1B[0m, (b)\n   base your \x1B[35mdecisions\x1B[0m on \x1B[35mpersonal values\x1B[0m, \x1B[35mharmoniously/forgiving\x1B[0m, and \x1B[35mempathetically\x1B[0m,\n   or (c) you are not sure? ")
  if question3 == "a":
    personality1 [4] = 1
  elif question3 == "b":
    personality1 [5] = 1
  elif question3 == "c":
    question3a = input ("   Do you (a) enjoy \x1B[35mfinding flaws\x1B[0m in an \x1B[35margument\x1B[0m, or (b) like to \x1B[35mplease others\x1B[0m and see\n   the \x1B[35mbest in people\x1B[0m? ")
    if question3a == "a":
      personality1 [4] = 1
    elif question3a == "b":
      personality1 [5] = 1
    else:
      if name1 == "":
        exit ("\nOops! Looks like something went wrong! Please try again later.")
      else:
        exit ("\nOops! Looks like something went wrong! Please try again later, " + name1.title () + ".")
  else:
    if name1 == "":
      exit ("\nOops! Looks like something went wrong! Please try again later.")
    else:
      exit ("\nOops! Looks like something went wrong! Please try again later, " + name1.title () + ".")

  # Question No. 4
  question4 = input ("5. Do you (a) stick to and \x1B[35mrespect deadlines\x1B[0m and rules, and \x1B[35mplan ahead\x1B[0m, (b) see rules\n   and \x1B[35mdeadlines as flexible\x1B[0m and are spontaneous, \x1B[35menjoying surprises\x1B[0m and \x1B[35mnew situations\x1B[0m,\n   or (c) you are not sure? ")
  if question4 == "a":
    personality1 [6] = 1
  elif question4 == "b":
    personality1 [7] = 1
  elif question4 == "c":
    question4a = input ("   Do you (a) prefer to have \x1B[35mdetailed step-by-step\x1B[0m instructions, or (b) like to \x1B[35mimprovise\x1B[0m\n   and \x1B[35mmake things up\x1B[0m as you go? ")
    if question4a == "a":
      personality1 [6] = 1
    elif question4a == "b":
      personality1 [7] = 1
    else:
      if name1 == "":
        exit ("\nOops! Looks like something went wrong! Please try again later.")
      else:
        exit ("\nOops! Looks like something went wrong! Please try again later, " + name1.title () + ".")
  else:
    if name1 == "":
      exit ("\nOops! Looks like something went wrong! Please try again later.")
    else:
      exit ("\nOops! Looks like something went wrong! Please try again later, " + name1.title () + ".")
  global newlist
  newlist = ""
  if personality1 [0] == 1:
    personality1 [0] = "E"
    newlist += personality1 [0]
  elif personality1 [0] == 0:
    pass
  if personality1 [1] == 1:
    personality1 [1] = "I"
    newlist += personality1 [1]
  elif personality1 [1] == 0:
    pass
  if personality1 [2] == 1:
    personality1 [2] = "S"
    newlist += personality1 [2]
  elif personality1 [2] == 0:
    pass
  if personality1 [3] == 1:
    personality1 [3] = "N"
    newlist += personality1 [3]
  elif personality1 [3] == 0:
    pass
  if personality1 [4] == 1:
    personality1 [4] = "T"
    newlist += personality1 [4]
  elif personality1 [4] == 0:
    pass
  if personality1 [5] == 1:
    personality1 [5] = "F"
    newlist += personality1 [5]
  elif personality1 [5] == 0:
    pass
  if personality1 [6] == 1:
    personality1 [6] = "J"
    newlist += personality1 [6]
  elif personality1 [6] == 0:
    pass
  if personality1 [7] == 1:
    personality1 [7] = "P"
    newlist += personality1 [7]
  elif personality1 [7] == 0:
    pass
  else:
    pass

  # Evaluation
  if name1 == "":
    print ("\nCongrats! I've been able to evaluate your true personality type.\nFrom what you've shown me, your personality type is " + "\x1B[4m" + newlist + "\x1B[0m" + "!")
  else:
    print ("\nCongrats, " + name1.title () + "! I've been able to evaluate your true personality type.\nFrom what you've shown me, your personality type is " + "\x1B[4m" + newlist + "\x1B[0m" + "!")
  if newlist == "INFP":
    print ("That means you are considered the \"Healer\" because you are a sensitive idealist, motivated by your deeper personal values.")
  if newlist == "INTJ":
    print ("That means you are considered the \"Mastermind\" because are a creative perfectionist, who prefers to do things your own way.")
  if newlist == "INFJ":
    print ("That means you are considered the \"Counseler\" because you are a thoughtful, and creative person, driven by firm principles and personal integrity.")
  if newlist == "INTP":
    print ("That means you are considered the \"Architect\" because you are an independent and creative problem solver.")
  if newlist == "ENFP":
    print ("That means you are considered the \"Champion\" because you are a curious and confident creative type of person, who sees possibilities everywhere.")
  if newlist == "ENTJ":
    print ("That means you are considered the \"Commander\" because you are a natural leader, who is logical, analytical, and a good strategic planner.")
  if newlist == "ENTP":
    print ("That means you are considered the \"Visionary\" because you are an enterprising creative person, who enjoys new challenges.")
  if newlist == "ENFJ":
    print ("That means you are considered the \"Teacher\" because you are a people-lover, who is energetic, articulate, and diplomatic.")
  if newlist == "ISFJ":
    print ("That means you are considered the \"Protector\" because you are a modest and determined worker, who enjoys helping others.")
  if newlist == "ISFP":
    print ("That means you are considered the \"Composer\" because you are a warm and sensitive type of person, who likes to help people in tangible ways.")
  if newlist == "ISTJ":
    print ("That means you are considered the \"Inspector\" because you are a hard worker, who values your responsibilities and commitments.")
  if newlist == "ISTP":
    print ("That means you are considered the \"Craftsperson\" because you are a straightforward and honest person, who prefers action to conversation.")
  if newlist == "ESFJ":
    print ("That means you are considered the \"Provider\" because you are a gregarious traditionalist motivated to help others.")
  if newlist == "ESFP":
    print ("That means you are considered the \"Performer\" because you are a lively and playful person, who values common sense.")
  if newlist == "ESTJ":
    print ("That means you are considered the \"Supervisor\" because you are a realistic person, who is quick to make practical decisions.")
  if newlist == "ESTP":
    print ("That means you are considered the \"Dynamo\" because you are a pragmatic person, who loves excitement and excels in a crisis.")
main ()

# Next Round/Job Type
replay1 = input ("\n\x1B[51m Would you like to (a) play again, or (b) figure out the best jobs for people with your personality type? \x1B[0m ")
if replay1 == "a":
  main ()
  print ("\nhttps://www.truity.com/page/16-personality-types-myers-briggs\nhttps://moodle.pamlicocc.edu/mod/resource/view.php?id=279837\nhttps://en.wikipedia.org/wiki/Myers%E2%80%93Briggs_Type_Indicator\nhttps://artofthinkingsmart.com/what-is-your-personality-type/")
elif replay1 == "b":
  if newlist == "INFP":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Graphic Designer\n• Psychologist/Therapist\n• Writer/Editor\n• Physical Therapist\n• HR Development Trainer\n")
  if newlist == "INTJ":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Investment Banker\n• Personal Financial Adviser\n• Software Developer\n• Economist\n• Executive\n")
  if newlist == "INFJ":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Therapist/Mental Health Counselor\n• Social Worker\n• HR Diversity Manager\n• Organizational Development Consultant\n• Customer Relations Manager\n")
  if newlist == "INTP":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Computer Programmer/Software Designer\n• Financial Analyst\n• Architect\n• College Professor\n• Economist\n")
  if newlist == "ENFP":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Journalist\n• Advertising Creative Director\n• Consultant\n• Restaurateur\n• Event Planner\n")
  if newlist == "ENTJ":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Executive\n• Lawyer\n• Market Research Analyst\n• Management/Business Consultant\n• Venture Capitalist\n")
  if newlist == "ENTP":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Entrepreneur, Real Estate Developer, Advertising Creative Director, Marketing Director, Politician/Political Consultant\n")
  if newlist == "ENFJ":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Advertising Executive\n• Public Relations Specialist\n• Corporate Coach/Trainer\n• Sales Manager\n• Employment Specialist/HR Professional\n")
  if newlist == "ISFJ":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Dentist\n• Elementary School Teacher\n• Librarian\n• Franchise Owner\n• Customer Service Representative\n")
  if newlist == "ISFP":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Fashion Designer\n• Physical Therapist\n• Massage Therapist\n• Landscape Architect\n• Storekeeper\n")
  if newlist == "ISTJ":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Auditor\n• Accountant\n• Chief Financial Officer\n• Web Development Engineer\n• Government Employee\n")
  if newlist == "ISTP":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Civil Engineer\n• Economist\n• Pilot\n• Data Communications Analyst\n• Emergency Room Physician\n")
  if newlist == "ESFJ":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Sales Representative\n• Nurse/Healthcare Worker\n• Social Worker\n• PR Account Executive\n• Loan Officer\n")
  if newlist == "ESFP":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Child Welfare Counselor\n• Primary Care Physician\n• Actor\n• Interior Designer\n• Environmental Scientist\n")
  if newlist == "ESTJ":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Insurance Sales Agent\n• Pharmacist\n• Lawyer\n• Project Manager\n• Judge\n")
  if newlist == "ESTP":
    print ("\x1B[4mBest Jobs for People with " + newlist + " Personality Type\x1B[0m:\n• Detective\n• Banker\n• Investor\n• Entertainment Agent\n• Sports Coach\n")
  print ("https://www.truity.com/page/16-personality-types-myers-briggs\nhttps://moodle.pamlicocc.edu/mod/resource/view.php?id=279837\nhttps://en.wikipedia.org/wiki/Myers%E2%80%93Briggs_Type_Indicator\nhttps://artofthinkingsmart.com/what-is-your-personality-type/")
else:
  if name1 == "":
    exit ("\nOops! Looks like something went wrong! Please try again later.")
  else:
    exit ("\nOops! Looks like something went wrong! Please try again later, " + name1.title () + ".")