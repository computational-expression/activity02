# Friend Team Synergy Quiz Activity

## Learning Objectives

By completing this activity, you will practice:
- Using `if`, `elif`, and `else` statements for complex decision making
- Combining conditions with boolean operators (`and`, `or`)
- Working with user input and string comparisons
- Creating interactive programs that respond to multiple conditions
- Writing a complete Python program with conditional logic

## Setup

After clicking the GitHub Classroom link and accepting the assignment:

1. **Clone your repository**:
   ```bash
   cd Desktop/cs100/activities    # or wherever you keep course files
   git clone [YOUR_REPOSITORY_URL]
   cd activity02
   ```

2. **Open the project in VS Code**:
   Use VS Code menu: File → Add Folder to Workspace → select your `activity02` folder

## Your Task

Create a **Friend Team Synergy Quiz** by completing the conditional logic in the `main.py` file. The input collection code is already provided - you just need to implement the `if`/`elif`/`else` chains with boolean logic!

**Interactive Element**: After completing your program, **team up with a classmate** and run the quiz on each other's preferences to see your synergy scores!

**Your Focus**: Complete the 6 TODO sections that implement conditional logic:

1. **Activity Synergy**: Complete the `elif` condition using `or` operators
2. **Study Synergy**: Create a complete `if`/`elif`/`else` chain with `and`/`or` logic
3. **Personality Synergy**: Implement complex boolean combinations
4. **Schedule Synergy**: Use `and` operators for morning preferences  
5. **Final Results**: Create percentage-based `if`/`elif`/`else` chain
6. **Bonus**: Advanced boolean logic combinations (optional challenge)

**Time Estimate: 20-30 minutes**

## Testing Your Program

Run your program to make sure it works:

```bash
python main.py
```

### Example Output
```
🤝 FRIEND TEAM SYNERGY QUIZ 🤝
=================================

Let's see how well you and your friend work together!

Person 1, what's your name? Amara
Person 2, what's your name? Jordan

Hi Amara and Jordan! Let's discover your teamwork potential.

🎯 ACTIVITY PREFERENCES
Amara, what's your favorite weekend activity?
(a) outdoor adventures  (b) gaming/movies  (c) studying/reading  (d) social events
Your choice: a

Jordan, what's your favorite weekend activity?
(a) outdoor adventures  (b) gaming/movies  (c) studying/reading  (d) social events  
Your choice: b

📚 STUDY HABITS
Amara, how do you prefer to study?
(a) alone quietly  (b) with music  (c) in groups  (d) short bursts
Your choice: c

Jordan, how do you prefer to study?
(a) alone quietly  (b) with music  (c) in groups  (d) short bursts
Your choice: c

🎭 PERSONALITY TYPE
Amara, which describes you best?
(a) outgoing leader  (b) creative thinker  (c) analytical planner  (d) supportive friend
Your choice: a

Jordan, which describes you best?
(a) outgoing leader  (b) creative thinker  (c) analytical planner  (d) supportive friend
Your choice: d

⏰ DAILY SCHEDULE
Amara, are you more productive in the morning? (yes/no): yes
Jordan, are you more productive in the morning? (yes/no): yes

🤝 SYNERGY ANALYSIS
=================================

Activity Synergy: DIFFERENT INTERESTS
- Amara loves outdoor adventures while Jordan prefers gaming/movies
- Recommendation: Try alternating activities!

Study Synergy: PERFECT MATCH!
- You both love group study sessions
- Recommendation: Form a study group together!

Personality Synergy: GREAT TEAM!
- Amara's leadership pairs well with Jordan's supportive nature
- Recommendation: You'll complement each other perfectly!

Schedule Synergy: EXCELLENT TIMING!
- You're both morning people
- Recommendation: Schedule activities for morning hours!

🎉 OVERALL TEAM SYNERGY: 85% - STRONG PARTNERSHIP POTENTIAL!

Amara and Jordan, you have great potential for working together effectively!
You complement each other well and share important values.
=================================
```

## Interactive Challenge

**After completing your program:**

1. **Find a classmate** who has also finished the activity
2. **Run the quiz together** - input both of your real preferences
3. **Compare your synergy scores** with other pairs in the class
4. **Discuss the results** - do you agree with the program's assessment?

**Extra Fun**: See which pair gets the highest synergy score in the class!

## Submission

**Submit your work**:
```bash
# Add your completed main.py file
git add main.py

# Commit your changes
git commit -m "Complete friend team synergy quiz"

# Push to GitHub
git push origin main
```

**Verify your submission**: Go to your repository on GitHub and make sure your completed `main.py` file is visible.

## Grading Rubric

This activity is assessed on a **pass/fail basis**:

- **1 point**: Awarded if 50% or more of the program functionality is completed
- **0 points**: Awarded if less than 50% of the program functionality is completed

The program functionality includes: user input, conditional statements (`if`/`elif`/`else`), boolean logic (`and`/`or`), string comparisons, and proper output display.

## Technical Requirements

Your program must demonstrate:

- **Multiple `if`/`elif`/`else` chains** for different synergy categories
- **Boolean logic** using `and` and `or` operators to combine conditions
- **String comparisons** for user input validation and preference matching
- **User input collection** for multiple questions and preferences
- **Formatted output** displaying synergy analysis
