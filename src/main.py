print(">>> main.py started")

from src.preprocess import load_projects
from src.recommender import recommend_projects

def main():
    print("Skill-Aware Project Recommendation System\n")

    user_skills = set(input("Enter your skills (comma separated): ").split(","))
    user_skills = set(skill.strip() for skill in user_skills)

    target_role = input("Enter your target role: ").strip()

    df = load_projects()
    results = recommend_projects(user_skills, target_role, df)

    print("\nRecommended Projects:\n")
    for r in results:
        print(f"📌 {r['project']} (Score: {r['score']})")
        print(f"   ✔ Matched skills: {', '.join(r['matched_skills'])}")
        if r['missing_skills']:
            print(f"   ❗ Skill gaps filled: {', '.join(r['missing_skills'])}")
        print()

if __name__ == "__main__":
    main()
