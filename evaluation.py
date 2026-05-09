from recommender import recommend_assessments

# Sample evaluation test cases
TEST_CASES = [
    {
        "query": "Need a Python backend developer with SQL skills",
        "expected": [
            "Python Developer Test",
            "SQL Test"
        ]
    },

    {
        "query": (
            "Hiring AI engineer with machine "
            "learning experience"
        ),
        "expected": [
            "AI Engineer Assessment",
            "Machine Learning Engineer Test"
        ]
    },

    {
        "query": "Need React frontend developer",
        "expected": [
            "React Developer Test",
            "Frontend Developer Test"
        ]
    }
]


def recall_at_k(recommended, expected, k=5):

    recommended_names = [
        item['name']
        for item in recommended[:k]
    ]

    hits = sum(
        1 for item in expected
        if item in recommended_names
    )

    return hits / len(expected)


def evaluate_system():

    total_score = 0

    for idx, test in enumerate(
        TEST_CASES,
        start=1
    ):

        results = recommend_assessments(
            test['query'],
            top_k=5
        )

        score = recall_at_k(
            results,
            test['expected']
        )

        total_score += score

        print(f"Test Case {idx}")
        print(f"Query: {test['query']}")
        print(f"Recall@5: {score:.2f}")

        print("Recommendations:")

        for item in results:
            print(f"- {item['name']}")

        print("-" * 40)

    avg_score = total_score / len(TEST_CASES)

    print(
        f"Average Recall@5: "
        f"{avg_score:.2f}"
    )


if __name__ == "__main__":

    evaluate_system()