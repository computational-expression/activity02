"""
Friend Team Synergy Quiz
Activity 2 - CMPSC 100

This program analyzes how well two people work together based on their
preferences and habits. It uses conditional statements and boolean logic
to determine team synergy and collaboration potential.

Complete the TODO sections to implement the conditional logic!
"""

# Welcome message and input collection (COMPLETED FOR YOU)
print("🤝 FRIEND TEAM SYNERGY QUIZ 🤝")
print("=================================")
print()
print("Let's see how well you and your friend work together!")
print()

# Get both people's names
person1_name = input("Person 1, what's your name? ")
person2_name = input("Person 2, what's your name? ")
print(f"Hi {person1_name} and {person2_name}! Let's discover your teamwork potential.")
print()

# Collect activity preferences
print("🎯 ACTIVITY PREFERENCES")
print(f"{person1_name}, what's your favorite weekend activity?")
print("(a) outdoor adventures  (b) gaming/movies  (c) studying/reading  (d) social events")
person1_activity = input("Your choice: ").lower()

print(f"{person2_name}, what's your favorite weekend activity?")
print("(a) outdoor adventures  (b) gaming/movies  (c) studying/reading  (d) social events")
person2_activity = input("Your choice: ").lower()
print()

# Collect study habits
print("📚 STUDY HABITS")
print(f"{person1_name}, how do you prefer to study?")
print("(a) alone quietly  (b) with music  (c) in groups  (d) short bursts")
person1_study = input("Your choice: ").lower()

print(f"{person2_name}, how do you prefer to study?")
print("(a) alone quietly  (b) with music  (c) in groups  (d) short bursts")
person2_study = input("Your choice: ").lower()
print()

# Collect personality types
print("🎭 PERSONALITY TYPE")
print(f"{person1_name}, which describes you best?")
print("(a) outgoing leader  (b) creative thinker  (c) analytical planner  (d) supportive friend")
person1_personality = input("Your choice: ").lower()

print(f"{person2_name}, which describes you best?")
print("(a) outgoing leader  (b) creative thinker  (c) analytical planner  (d) supportive friend")
person2_personality = input("Your choice: ").lower()
print()

# Collect schedule preferences
print("⏰ DAILY SCHEDULE")
person1_morning = input(f"{person1_name}, are you more productive in the morning? (yes/no): ").lower()
person2_morning = input(f"{person2_name}, are you more productive in the morning? (yes/no): ").lower()
print()

# Initialize synergy score
synergy_score = 0
total_categories = 4

# =============================================================================
# YOUR TASK: Complete the conditional logic below!
# =============================================================================

print("🤝 SYNERGY ANALYSIS")
print("=================================")
print()

# 1: Activity Synergy Analysis
print("Activity Synergy: ", end="")

# TODO: Complete this if/elif/else chain
if person1_activity == person2_activity:
    print("PERFECT MATCH!")
    print("- You both love the same activities!")
    synergy_score += 1
elif (person1_activity == "a" and person2_activity == "d") or (person1_activity == "d" and person2_activity == "a"):
    print("GREAT COMBINATION!")
    print("- Outdoor adventures and social events work well together!")
    synergy_score += 0.8
elif False:  # TODO: Replace False with condition using 'or' - if one person likes gaming/movies ("b") OR studying/reading ("c")
             #       AND the other likes studying/reading ("c") OR gaming/movies ("b")
    print("COMPLEMENTARY INTERESTS!")
    print("- You balance entertainment and learning well!")
    synergy_score += 0.6
else:
    print("DIFFERENT INTERESTS")
    print("- You have different preferences, but that's okay!")
    synergy_score += 0.3

print()

# 2: Study Synergy Analysis
print("Study Synergy: ", end="")

# TODO: Create complete if/elif/else chain for study habits
if False:  # TODO: Replace False - Check if BOTH prefer group study ("c") using 'and'
    print("PERFECT MATCH!")
    print("- You both love group study sessions!")
    synergy_score += 1
elif False:  # TODO: Replace False - Check if BOTH prefer quiet study ("a" or "b") using 'and' and 'or'
    print("COMPATIBLE STYLES!")
    print("- You both prefer quieter study environments!")
    synergy_score += 0.7
elif False:  # TODO: Replace False - Check if ONE prefers group study ("c") AND the other prefers short bursts ("d")
             # Use 'and' and 'or' to check both combinations
    print("GOOD BALANCE!")
    print("- You can help each other with different approaches!")
    synergy_score += 0.5
else:
    print("DIFFERENT APPROACHES")
    print("- You have different study styles!")
    synergy_score += 0.2

print()

# 3: Personality Synergy Analysis  
print("Personality Synergy: ", end="")

# TODO: Create if/elif/else chain for personality combinations
if False:  # TODO: Replace False - Check for leader ("a") + supportive friend ("d") combination using 'and' and 'or'
    print("GREAT TEAM!")
    print("- Leadership pairs well with supportive nature!")
    synergy_score += 1
elif False:  # TODO: Replace False - Check if BOTH are creative ("b") OR BOTH are analytical ("c") using 'and' and 'or'
    print("SIMILAR MINDS!")
    print("- You think in similar ways!")
    synergy_score += 0.8
elif False:  # TODO: Replace False - Check for creative ("b") + analytical ("c") combination using boolean logic
    print("BALANCED TEAM!")
    print("- Creativity and analysis work well together!")
    synergy_score += 0.7
else:
    print("DIVERSE PERSONALITIES")
    print("- You bring different strengths!")
    synergy_score += 0.4

print()

# 4: Schedule Synergy Analysis
print("Schedule Synergy: ", end="")

# TODO: Create if/elif/else for morning preferences
if False:  # TODO: Replace False - Check if BOTH are morning people using 'and'
    print("EXCELLENT TIMING!")
    print("- You're both morning people!")
    synergy_score += 1
elif False:  # TODO: Replace False - Check if BOTH are NOT morning people using 'and'
             # Hint: person1_morning == "no" and person2_morning == "no"
    print("NIGHT OWLS UNITE!")
    print("- You both prefer later hours!")
    synergy_score += 1
else:
    print("DIFFERENT SCHEDULES")
    print("- You have different productive hours!")
    synergy_score += 0.3

print()

# 5: Calculate and Display Final Results
final_percentage = int((synergy_score / total_categories) * 100)
print("🎉 OVERALL TEAM SYNERGY: ", end="")

# TODO: Create if/elif/else chain for final percentage ranges
if False:  # TODO: Replace False - Check for 90% or higher
    print(f"{final_percentage}% - PERFECT PARTNERSHIP MATCH!")
    message = "You two are destined to be an amazing team!"
elif False:  # TODO: Replace False - Check for 75-89% range
    print(f"{final_percentage}% - STRONG PARTNERSHIP POTENTIAL!")
    message = "You have great potential for working together effectively!"
elif False:  # TODO: Replace False - Check for 50-74% range
    print(f"{final_percentage}% - GOOD TEAMWORK POTENTIAL!")
    message = "You could develop effective collaboration with some effort!"
elif False:  # TODO: Replace False - Check for 25-49% range
    print(f"{final_percentage}% - SOME COLLABORATION POTENTIAL!")
    message = "You have some common ground to build teamwork on!"
else:
    print(f"{final_percentage}% - DIFFERENT WORKING STYLES!")
    message = "You work quite differently, but diversity can strengthen teams!"

print()
print(f"{person1_name} and {person2_name}, {message}")

# TODO 6: BONUS - Advanced Boolean Logic (Optional Challenge)
print()
print("🎯 BONUS RECOMMENDATIONS:")

# TODO: Use complex boolean logic to give special recommendations
if False:  # TODO: Replace False - Check if high synergy (>= 80%) AND both are morning people
    print("BONUS: You're extremely well-matched for morning teamwork!")
elif False:  # TODO: Replace False - Check if same study habits BUT different activities
    print("BONUS: Your study synergy is strong!")
elif False:  # TODO: Replace False - Check if either person is a leader ("a") OR supportive ("d")
    print("BONUS: You have great leadership dynamics!")

print("=================================")
print("Thanks for taking the Friend Team Synergy Quiz! 🎉")
