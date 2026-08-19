from client import ConversationalRecruiterNotetakerCompetencyScorerClient

def main():
    client = ConversationalRecruiterNotetakerCompetencyScorerClient()
    transcript = "Candidate explained distributed transaction locking with two-phase commit."
    res = client.score_interview(transcript)
    print(f"Recommendation: {res['hiring_recommendation']}")
    print("Scores:", res["competency_scores"])
    print("Notes:", res["structured_interview_notes"])

if __name__ == "__main__":
    main()
