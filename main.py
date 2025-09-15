"""
Friend Team Synergy Quiz
Activity 2 - CMPSC 100

This program analyzes how well two people work together based on their
preferences and habits. It uses conditional statements and boolean logic
to determine team synergy and collaboration potential.

Complete all TODO sections to create a working synergy quiz!
"""

# TODO 1: Display welcome message and get user names
print("🤝 FRIEND TEAM SYNERGY QUIZ 🤝")
print("=================================")
print()
print("Let's see how well you and your friend work together!")
print()

# TODO: Get both people's names and store them in variables
# Hint: Use input() to ask "Person 1, what's your name?" and "Person 2, what's your name?"
person1_name = "TODO"  # TODO: Replace with input() to get person 1's name
person2_name = "TODO"  # TODO: Replace with input() to get person 2's name

print(f"Hi {person1_name} and {person2_name}! Let's discover your teamwork potential.")
print()

# TODO 2: Collect activity preferences
print("🎯 ACTIVITY PREFERENCES")
print(f"{person1_name}, what's your favorite weekend activity?")
print("(a) outdoor adventures  (b) gaming/movies  (c) studying/reading  (d) social events")
person1_activity = input("Your choice: ").lower()

print(f"{person2_name}, what's your favorite weekend activity?")
print("(a) outdoor adventures  (b) gaming/movies  (c) studying/reading  (d) social events")
person2_activity = input("Your choice: ").lower()
print()

# TODO 3: Collect study habits
print("📚 STUDY HABITS")
print(f"{person1_name}, how do you prefer to study?")
print("(a) alone quietly  (b) with music  (c) in groups  (d) short bursts")
person1_study = "TODO"  # TODO: Replace with input() to get person 1's study preference

print(f"{person2_name}, how do you prefer to study?")
print("(a) alone quietly  (b) with music  (c) in groups  (d) short bursts")
person2_study = "TODO"  # TODO: Replace with input() to get person 2's study preference
print()

# TODO 4: Collect personality types
print("🎭 PERSONALITY TYPE")
print(f"{person1_name}, which describes you best?")
print("(a) outgoing leader  (b) creative thinker  (c) analytical planner  (d) supportive friend")
person1_personality = "TODO"  # TODO: Replace with input() to get person 1's personality type

print(f"{person2_name}, which describes you best?")
print("(a) outgoing leader  (b) creative thinker  (c) analytical planner  (d) supportive friend")
person2_personality = "TODO"  # TODO: Replace with input() to get person 2's personality type
print()

# TODO 5: Collect schedule preferences
print("⏰ DAILY SCHEDULE")
person1_morning = input(f"{person1_name}, are you more productive in the morning? (yes/no): ").lower()
person2_morning = "TODO"  # TODO: Ask person 2 the same question about morning productivity
print()

# TODO 6: Initialize synergy score
synergy_score = 0
total_categories = 4

# TODO 7: Analyze activity synergy using if/elif/else
print("🤝 SYNERGY ANALYSIS")
print("=================================")
print()

print("Activity Synergy: ", end="")
# TODO: Complete this if/elif/else chain for activity synergy
if person1_activity == person2_activity:
    print("PERFECT MATCH!")
    print(f"- You both love the same activities!")
    print("- Recommendation: Plan regular activities together!")
    synergy_score += 1
elif (person1_activity == "a" and person2_activity == "d") or (person1_activity == "d" and person2_activity == "a"):
    # TODO: Handle outdoor + social combination
    print("GREAT COMBINATION!")
    print("- Outdoor adventures and social events complement each other!")
    print("- Recommendation: Try outdoor group activities!")
    synergy_score += 0.8
elif False:  # TODO: Replace False with condition for gaming/movies + studying/reading using 'or'
    print("COMPLEMENTARY INTERESTS!")
    print("- You balance each other's interests well!")
    print("- Recommendation: Help each other try new activities!")
    synergy_score += 0.6
else:
    print("DIFFERENT INTERESTS")
    print(f"- {person1_name} and {person2_name} have different activity preferences")
    print("- Recommendation: Try alternating activities!")
    synergy_score += 0.3

print()

# TODO 8: Analyze study synergy
print("Study Synergy: ", end="")
# TODO: Create if/elif/else for study habits
# Use boolean logic (and/or) to check for collaborative study styles

if False:  # TODO: Replace False with condition to check if both prefer group study (person1_study == "c" and person2_study == "c")
    print("PERFECT MATCH!")
    print("- You both love group study sessions")
    print("- Recommendation: Form a study group together!")
    synergy_score += 1
elif False:  # TODO: Replace False with condition to check if both prefer quiet study (alone or with music) using 'or'
    print("COMPATIBLE STYLES!")
    print("- You both prefer quieter study environments")
    print("- Recommendation: Study in the same space quietly!")
    synergy_score += 0.7
elif False:  # TODO: Replace False with condition to check if one prefers groups and other prefers bursts using 'and'
    print("GOOD BALANCE!")
    print("- You can help each other with different study approaches")
    print("- Recommendation: Try alternating study methods!")
    synergy_score += 0.5
else:
    print("DIFFERENT APPROACHES")
    print("- You have different study preferences")
    print("- Recommendation: Respect each other's study styles!")
    synergy_score += 0.2

print()

# TODO 9: Analyze personality synergy using complex boolean logic
print("Personality Synergy: ", end="")
# TODO: Create if/elif/else chain with boolean operators

# Check for perfect leadership combinations
if (person1_personality == "a" and person2_personality == "d") or (person1_personality == "d" and person2_personality == "a"):
    # TODO: Handle leader + supportive friend combination
    print("GREAT TEAM!")
    print("- Leadership pairs well with supportive nature")
    print("- Recommendation: You'll complement each other perfectly!")
    synergy_score += 1
elif False:  # TODO: Replace False with condition to check if both are creative thinkers OR both are analytical planners
    print("SIMILAR MINDS!")
    print("- You think in similar ways")
    print("- Recommendation: Collaborate on creative or analytical projects!")
    synergy_score += 0.8
elif False:  # TODO: Replace False with condition to check for creative + analytical combination using boolean logic
    print("BALANCED TEAM!")
    print("- Creativity and analysis make a powerful combination")
    print("- Recommendation: Work together on complex projects!")
    synergy_score += 0.7
else:
    print("DIVERSE PERSONALITIES")
    print("- You bring different strengths to the partnership")
    print("- Recommendation: Learn from each other's approaches!")
    synergy_score += 0.4

print()

# TODO 10: Analyze schedule synergy
print("Schedule Synergy: ", end="")
# TODO: Use boolean logic to compare morning preferences

if False:  # TODO: Replace False with condition to check if both are morning people using 'and'
    print("EXCELLENT TIMING!")
    print("- You're both morning people")
    print("- Recommendation: Schedule activities for morning hours!")
    synergy_score += 1
elif False:  # TODO: Replace False with condition to check if both are NOT morning people using 'and' and comparing to "no"
    print("NIGHT OWLS UNITE!")
    print("- You both prefer later hours")
    print("- Recommendation: Plan evening study sessions and activities!")
    synergy_score += 1
else:
    print("DIFFERENT SCHEDULES")
    print("- You have different productive hours")
    print("- Recommendation: Find compromise times that work for both!")
    synergy_score += 0.3

print()

# TODO 11: Calculate final synergy percentage and display results
final_percentage = int((synergy_score / total_categories) * 100)

print("🎉 OVERALL TEAM SYNERGY: ", end="")
# TODO: Use if/elif/else to display synergy level based on percentage

if final_percentage >= 90:
    print(f"{final_percentage}% - PERFECT PARTNERSHIP MATCH!")
    message = "You two are destined to be an amazing team!"
elif False:  # TODO: Replace False with condition to check for 75-89% range
    print(f"{final_percentage}% - STRONG PARTNERSHIP POTENTIAL!")
    message = "You have great potential for working together effectively!"
elif False:  # TODO: Replace False with condition to check for 50-74% range  
    print(f"{final_percentage}% - GOOD TEAMWORK POTENTIAL!")
    message = "You could develop effective collaboration with some effort!"
elif False:  # TODO: Replace False with condition to check for 25-49% range
    print(f"{final_percentage}% - SOME COLLABORATION POTENTIAL!")
    message = "You have some common ground to build teamwork on!"
else:
    print(f"{final_percentage}% - DIFFERENT WORKING STYLES!")
    message = "You work quite differently, but diversity can strengthen teams!"

print()
print(f"{person1_name} and {person2_name}, {message}")

# TODO 12: Add final recommendations based on boolean combinations
print()
# TODO: Create a final if statement using boolean logic to give special recommendations

if False:  # TODO: Replace False with condition to check if they have high synergy (>= 80) AND similar schedules using 'and'
    print("BONUS RECOMMENDATION: You're extremely well-matched for teamwork!")
    print("Consider being study partners or project teammates!")
elif False:  # TODO: Replace False with condition to check if they have different activities BUT same study habits using 'and'
    print("BONUS RECOMMENDATION: Your study synergy is strong!")
    print("Focus on academic collaboration while exploring new activities!")
elif False:  # TODO: Replace False with condition using 'or' to check if either person is a leader OR supportive friend
    print("BONUS RECOMMENDATION: You have great leadership dynamics!")
    print("Consider working together on group projects or team activities!")

print("=================================")

# TODO 13: Extra challenge - ask if they want to compare with another pair
# TODO: Ask "Would you like to compare your score with another pair? (yes/no): "
# TODO: If yes, ask for the other pair's percentage and compare using if/elif/else

compare_choice = "TODO"  # TODO: Replace with input() to get user choice for comparison

if False:  # TODO: Replace False with condition to check if they want to compare scores
    other_score = 0  # TODO: Replace 0 with int(input()) to get the other pair's synergy percentage
    print()
    print("📊 COMPARISON RESULTS:")
    
    if False:  # TODO: Replace False with condition to check if current score is higher than other score
        print(f"Congratulations! Your {final_percentage}% beats their {other_score}%!")
        print("You two have stronger teamwork potential than the other pair!")
    elif False:  # TODO: Replace False with condition to check if scores are equal
        print(f"It's a tie! Both pairs scored {final_percentage}%!")
        print("You're equally well-matched for teamwork - that's awesome!")
    else:
        print(f"The other pair scored higher with {other_score}% vs your {final_percentage}%")
        print("But remember, every partnership brings unique strengths!")

print()
print("Thanks for taking the Friend Team Synergy Quiz! 🎉")
