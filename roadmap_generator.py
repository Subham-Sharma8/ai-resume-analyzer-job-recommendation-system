def generate_roadmap(missing_skills, skill_dictionary):
    lookup = {row["skill"].strip().lower(): row for row in skill_dictionary}
    roadmap = []
    for index, skill in enumerate(missing_skills, start=1):
        row = lookup.get(skill.lower(), {})
        topic = row.get("learning_topic", f"Study {skill} fundamentals and complete a small practical project.")
        roadmap.append({
            "week": index,
            "skill": skill,
            "topic": topic,
        })
    return roadmap
