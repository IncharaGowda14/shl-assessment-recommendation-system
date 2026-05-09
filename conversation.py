from recommender import recommend_assessments

VAGUE_KEYWORDS = [
    "assessment",
    "test",
    "hiring",
    "developer",
    "engineer"
]


def extract_latest_user_message(messages):
    for msg in reversed(messages):
        if msg["role"] == "user":
            return msg["content"]
    return ""


def needs_clarification(query):

    words = query.lower().split()

    if len(words) <= 3:
        return True

    vague_count = sum(
        1 for w in words if w in VAGUE_KEYWORDS
    )

    return vague_count >= 2


def compare_assessments(query):

    query_lower = query.lower()

    if "difference" in query_lower or "compare" in query_lower:

        return {
            "reply": (
                "OPQ focuses on personality and workplace "
                "behavior, while GSA focuses on cognitive "
                "and reasoning ability."
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    return None


def refuse_offtopic(query):

    off_topic = [
        "salary",
        "legal",
        "law",
        "politics",
        "weather"
    ]

    if any(word in query.lower() for word in off_topic):

        return {
            "reply": (
                "I can only help with SHL assessment "
                "recommendations."
            ),
            "recommendations": [],
            "end_of_conversation": True
        }

    return None


def chat_agent(messages):

    latest_query = extract_latest_user_message(messages)

    refusal = refuse_offtopic(latest_query)

    if refusal:
        return refusal

    comparison = compare_assessments(latest_query)

    if comparison:
        return comparison

    if needs_clarification(latest_query):

        return {
            "reply": (
                "Could you share more details such as "
                "role, skills, experience level, or "
                "assessment type?"
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    recommendations = recommend_assessments(
        latest_query,
        top_k=5
    )

    return {
        "reply": (
            f"Here are {len(recommendations)} "
            "recommended SHL assessments."
        ),
        "recommendations": recommendations,
        "end_of_conversation": True
    }