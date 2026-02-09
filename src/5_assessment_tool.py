"""
Interactive Mental Health Self-Assessment Tool
Author: Sakhi Patel
"""

import sys


def get_valid_input(question, min_val=0, max_val=4):
    """Get and validate user input"""
    while True:
        try:
            response = int(input(question))
            if min_val <= response <= max_val:
                return response
            else:
                print(f"  ⚠ Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("  ⚠ Please enter a valid number")


def stress_assessment():
    """Conduct stress assessment"""
    
    questions = [
        "How often have you felt upset due to something in your academic affairs?",
        "How often you felt unable to control important things in your academic affairs?",
        "How often you felt nervous and stressed because of academic pressure?",
        "How often you felt you could not cope with all mandatory academic activities?",
        "How often you felt confident about your ability to handle academic problems? (reverse)",
        "How often you felt things in your academic life are going your way? (reverse)",
        "How often are you able to control irritations in your academic affairs? (reverse)",
        "How often you felt your academic performance was on top? (reverse)",
        "How often you got angered due to bad performance beyond your control?",
        "How often you felt academic difficulties are piling up too high to overcome?"
    ]
    
    print("\n" + "="*70)
    print("STRESS ASSESSMENT")
    print("="*70)
    print("\nRate each question on a scale of 0-4:")
    print("  0 = Never  |  1 = Rarely  |  2 = Sometimes  |  3 = Often  |  4 = Very Often")
    print("\n" + "-"*70)
    
    total_score = 0
    responses = []
    
    for i, question in enumerate(questions, 1):
        print(f"\n[Question {i}/10]")
        score = get_valid_input(f"{question}\nYour answer (0-4): ")
        responses.append(score)
        total_score += score
    
    # Interpret results
    print("\n" + "="*70)
    print("STRESS ASSESSMENT RESULTS")
    print("="*70)
    print(f"\nTotal Score: {total_score} / 40")
    
    if total_score < 18:
        level = "LOW STRESS"
        color = "✓"
        interpretation = "You appear to be managing academic stress well."
        recommendation = "Continue your current coping strategies and maintain work-life balance."
    elif total_score < 35:
        level = "MODERATE STRESS"
        color = "⚠"
        interpretation = "You're experiencing moderate levels of academic stress."
        recommendation = "Consider stress management techniques like time management, exercise, and talking to friends or counselors."
    else:
        level = "HIGH STRESS"
        color = "⚠⚠"
        interpretation = "You're experiencing high levels of academic stress."
        recommendation = "It's important to seek support. Consider talking to a counselor, academic advisor, or mental health professional."
    
    print(f"\nStress Level: {color} {level}")
    print(f"\nInterpretation: {interpretation}")
    print(f"\nRecommendation: {recommendation}")
    
    return total_score, level


def anxiety_assessment():
    """Conduct anxiety assessment"""
    
    questions = [
        "How often you felt nervous, anxious or on edge due to academic pressure?",
        "How often have you been unable to stop worrying about your academic affairs?",
        "How often have you had trouble relaxing due to academic pressure?",
        "How often have you been easily annoyed or irritated because of academic pressure?",
        "How often have you worried too much about academic affairs?",
        "How often have you been so restless that it is hard to sit still?",
        "How often have you felt afraid, as if something awful might happen?"
    ]
    
    print("\n" + "="*70)
    print("ANXIETY ASSESSMENT")
    print("="*70)
    print("\nRate each question on a scale of 0-4:")
    print("  0 = Never  |  1 = Rarely  |  2 = Sometimes  |  3 = Often  |  4 = Very Often")
    print("\n" + "-"*70)
    
    total_score = 0
    responses = []
    
    for i, question in enumerate(questions, 1):
        print(f"\n[Question {i}/7]")
        score = get_valid_input(f"{question}\nYour answer (0-4): ")
        responses.append(score)
        total_score += score
    
    # Interpret results
    print("\n" + "="*70)
    print("ANXIETY ASSESSMENT RESULTS")
    print("="*70)
    print(f"\nTotal Score: {total_score} / 28")
    
    if total_score < 18:
        level = "LOW ANXIETY"
        color = "✓"
        interpretation = "You appear to have minimal anxiety related to academics."
        recommendation = "Keep up your positive mindset and healthy habits."
    elif total_score < 35:
        level = "MODERATE ANXIETY"
        color = "⚠"
        interpretation = "You're experiencing moderate levels of academic anxiety."
        recommendation = "Try relaxation techniques, mindfulness, or breathing exercises. Consider talking to someone you trust."
    else:
        level = "HIGH ANXIETY"
        color = "⚠⚠"
        interpretation = "You're experiencing high levels of academic anxiety."
        recommendation = "Please consider seeking professional help from a counselor or mental health professional."
    
    print(f"\nAnxiety Level: {color} {level}")
    print(f"\nInterpretation: {interpretation}")
    print(f"\nRecommendation: {recommendation}")
    
    return total_score, level


def depression_assessment():
    """Conduct depression assessment"""
    
    questions = [
        "How often have you had little interest or pleasure in doing things?",
        "How often have you been feeling down, depressed or hopeless?",
        "How often have you had trouble falling or staying asleep, or sleeping too much?",
        "How often have you been feeling tired or having little energy?",
        "How often have you had poor appetite or overeating?",
        "How often have you been feeling bad about yourself or that you are a failure?",
        "How often have you been having trouble concentrating on things?",
        "How often have you moved or spoke too slowly for others to notice?",
        "How often have you had thoughts that you would be better off dead?"
    ]
    
    print("\n" + "="*70)
    print("DEPRESSION ASSESSMENT")
    print("="*70)
    print("\nRate each question on a scale of 0-4:")
    print("  0 = Never  |  1 = Rarely  |  2 = Sometimes  |  3 = Often  |  4 = Very Often")
    print("\n" + "-"*70)
    
    total_score = 0
    responses = []
    
    for i, question in enumerate(questions, 1):
        print(f"\n[Question {i}/9]")
        score = get_valid_input(f"{question}\nYour answer (0-4): ")
        responses.append(score)
        total_score += score
    
    # Interpret results
    print("\n" + "="*70)
    print("DEPRESSION ASSESSMENT RESULTS")
    print("="*70)
    print(f"\nTotal Score: {total_score} / 36")
    
    if total_score < 18:
        level = "LOW DEPRESSION"
        color = "✓"
        interpretation = "You appear to have minimal depressive symptoms."
        recommendation = "Continue taking care of your mental health through self-care and social connections."
    elif total_score < 35:
        level = "MODERATE DEPRESSION"
        color = "⚠"
        interpretation = "You're experiencing moderate depressive symptoms."
        recommendation = "Consider reaching out to a counselor, therapist, or trusted person. Professional support can be very helpful."
    else:
        level = "HIGH DEPRESSION"
        color = "⚠⚠"
        interpretation = "You're experiencing significant depressive symptoms."
        recommendation = "Please seek professional help immediately. Contact a mental health professional or crisis helpline."
    
    print(f"\nDepression Level: {color} {level}")
    print(f"\nInterpretation: {interpretation}")
    print(f"\nRecommendation: {recommendation}")
    
    # Special warning for suicidal thoughts
    if responses[-1] >= 2:
        print("\n" + "!"*70)
        print("IMPORTANT: You indicated thoughts of self-harm.")
        print("Please reach out for help immediately:")
        print("  • National Suicide Prevention Lifeline: 988")
        print("  • Crisis Text Line: Text HOME to 741741")
        print("  • Campus Counseling Center")
        print("!"*70)
    
    return total_score, level


def complete_assessment():
    """Conduct all three assessments"""
    
    print("\n" + "="*70)
    print("COMPLETE MENTAL HEALTH ASSESSMENT")
    print("="*70)
    print("\nYou will complete all three assessments: Stress, Anxiety, and Depression")
    
    input("\nPress Enter to begin...")
    
    # Conduct all assessments
    stress_score, stress_level = stress_assessment()
    input("\nPress Enter to continue to Anxiety Assessment...")
    
    anxiety_score, anxiety_level = anxiety_assessment()
    input("\nPress Enter to continue to Depression Assessment...")
    
    depression_score, depression_level = depression_assessment()
    
    # Summary
    print("\n" + "="*70)
    print("COMPLETE ASSESSMENT SUMMARY")
    print("="*70)
    print(f"\nStress:     {stress_level} (Score: {stress_score})")
    print(f"Anxiety:    {anxiety_level} (Score: {anxiety_score})")
    print(f"Depression: {depression_level} (Score: {depression_score})")
    print("\n" + "="*70)


def main():
    """Main menu for assessment tool"""
    
    print("\n" + "="*70)
    print(" "*15 + "STUDENT MENTAL HEALTH SELF-ASSESSMENT TOOL")
    print("="*70)
    
    print("\n" + "-"*70)
    print("DISCLAIMER")
    print("-"*70)
    print("This tool is for INFORMATIONAL PURPOSES ONLY.")
    print("It is NOT a clinical diagnosis and should not replace professional advice.")
    print("If you're experiencing mental health difficulties, please consult a")
    print("qualified mental health professional or counselor.")
    print("-"*70)
    
    while True:
        print("\n" + "="*70)
        print("MAIN MENU")
        print("="*70)
        print("\nSelect an assessment:")
        print("  1. Stress Assessment (10 questions)")
        print("  2. Anxiety Assessment (7 questions)")
        print("  3. Depression Assessment (9 questions)")
        print("  4. Complete Assessment (All Three)")
        print("  5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            stress_assessment()
        elif choice == '2':
            anxiety_assessment()
        elif choice == '3':
            depression_assessment()
        elif choice == '4':
            complete_assessment()
        elif choice == '5':
            print("\n" + "="*70)
            print("Thank you for using the Mental Health Assessment Tool.")
            print("Remember: Taking care of your mental health is important!")
            print("="*70 + "\n")
            break
        else:
            print("\n⚠ Invalid choice. Please enter a number between 1 and 5.")
        
        input("\nPress Enter to return to main menu...")


if __name__ == '__main__':
    main()
