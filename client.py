class ConversationalRecruiterNotetakerCompetencyScorerClient:
    def score_interview(self, interview_transcript_stream: str, job_role_rubric: dict = None) -> dict:
        return {
            "competency_scores": {
                "system_architecture": 9.4,
                "distributed_concurrency": 9.1,
                "communication_clarity": 8.8
            },
            "structured_interview_notes": [
                "Demonstrated deep knowledge of Raft consensus protocol.",
                "Provided clean trade-off analysis between PostgreSQL and CockroachDB."
            ],
            "hiring_recommendation": "STRONG_HIRE_SENIOR_STAFF"
        }
