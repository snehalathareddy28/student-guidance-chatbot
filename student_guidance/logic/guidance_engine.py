def get_guidance(education, stream, interest):
    if education == "12th" and stream == "Science":
        return {
            "careers": [
                "Software Developer",
                "Data Scientist",
                "AI Engineer"
            ],
            "courses": [
                "B.Tech Computer Science",
                "B.Sc Data Science"
            ],
            "skills": [
                "Python", "Java", "SQL", "Git"
            ]
        }

    elif education == "12th" and stream == "Commerce":
        return {
            "careers": [
                "Chartered Accountant",
                "Business Analyst",
                "Banking Professional"
            ],
            "courses": [
                "B.Com",
                "BBA",
                "CA"
            ],
            "skills": [
                "Accounting", "Excel", "Finance"
            ]
        }

    else:
        return {
            "careers": ["General Career Options"],
            "courses": ["Skill-based Courses"],
            "skills": ["Communication", "Problem Solving"]
        }
