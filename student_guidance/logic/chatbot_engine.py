def generate_response(message):
    msg = message.lower()

    # Diploma related
    if "diploma" in msg:
        return (
            "After completing a diploma, you have several options:\n"
            "1️⃣ Lateral entry into Engineering (B.Tech)\n"
            "2️⃣ Apply for government jobs (JE, PSU, Railways)\n"
            "3️⃣ Join private jobs related to your diploma field\n"
            "4️⃣ Learn skill-based courses (Python, Web Dev, AutoCAD)\n\n"
            "Tell me your diploma branch for specific guidance."
        )

    # Degree related
    elif "degree" in msg or "graduation" in msg:
        return (
            "After degree, you can:\n"
            "✔ Pursue higher studies (M.Tech, MBA, MS)\n"
            "✔ Prepare for government exams (GATE, UPSC, SSC)\n"
            "✔ Enter IT jobs (Developer, Analyst, Tester)\n"
            "✔ Start freelancing or startups\n\n"
            "What is your degree and interest?"
        )

    # Career guidance
    elif "career" in msg:
        return (
            "Career selection depends on:\n"
            "🎯 Your interest\n"
            "🎓 Education background\n"
            "💼 Job market demand\n\n"
            "Tell me:\n"
            "• Your education\n"
            "• Your interests\n"
            "• Your strengths"
        )

    # IT / Software
    elif "software" in msg or "it" in msg:
        return (
            "To enter IT/software field, you should learn:\n"
            "✅ Programming (Python / Java)\n"
            "✅ Web development (HTML, CSS, JS)\n"
            "✅ Databases (MySQL)\n"
            "✅ Projects + GitHub\n\n"
            "Do you want a beginner roadmap?"
        )

    # Government jobs
    elif "government" in msg or "govt" in msg:
        return (
            "Popular government career options:\n"
            "🏛 UPSC (IAS, IPS)\n"
            "🧾 SSC (CGL, CHSL)\n"
            "🚆 Railways\n"
            "⚡ PSU via GATE\n\n"
            "Which exam are you interested in?"
        )

    # Skills
    elif "skills" in msg:
        return (
            "Top skills for 2025:\n"
            "🔥 Python\n"
            "🔥 Full Stack Development\n"
            "🔥 Data Analysis\n"
            "🔥 AI & ML basics\n"
            "🔥 Communication skills\n\n"
            "Tell me your field to suggest exact skills."
        )

    # Default fallback
    else:
        return (
            "I can help you with:\n"
            "🎓 Education guidance\n"
            "💼 Career options\n"
            "🛣 Roadmaps\n"
            "📚 Skills to learn\n\n"
            "Try asking:\n"
            "• What after diploma?\n"
            "• Best career after degree\n"
            "• Skills for IT jobs"
        )
