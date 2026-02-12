import re
from datetime import datetime


class AbuseDetector:
    """
    Detects abusive words and calculates toxicity score
    """

    ABUSIVE_WORDS = {
        "idiot", "waste","stupid", "dumb", "fool",
        "bastard", "loser", "hate"
    }

    @staticmethod
    def normalize(text: str) -> str:
        return re.sub(r"[^\w\s]", "", text.lower())

    @classmethod
    def analyze(cls, message: str) -> dict:
        clean_text = cls.normalize(message)
        words = clean_text.split()

        detected = [w for w in words if w in cls.ABUSIVE_WORDS]
        toxicity_score = len(detected) / max(len(words), 1)

        return {
            "abusive": bool(detected),
            "detected_words": detected,
            "toxicity_score": round(toxicity_score, 2)
        }


class ChatModerator:
    """
    Handles warnings, blocking, and chat moderation
    """

    WARNING_LIMIT = 2
    BLOCK_LIMIT = 4

    def __init__(self):
        self.user_violations = {}

    def process_message(self, user: str, message: str) -> str:
        result = AbuseDetector.analyze(message)

        if result["abusive"]:
            self.user_violations[user] = self.user_violations.get(user, 0) + 1

            if self.user_violations[user] >= self.BLOCK_LIMIT:
                return "馃毇 User BLOCKED due to repeated abusive behavior"

            return (
                f"鈿狅笍 Warning {self.user_violations[user]}/{self.BLOCK_LIMIT}: "
                f"Abusive words detected {result['detected_words']} "
                f"(Toxicity Score: {result['toxicity_score']})"
            )

        return "鉁� Message sent successfully"


def run_demo():
    """
    Simulates a chat conversation
    """
    moderator = ChatModerator()

    chat_messages = [
        ("abhiram", "Hello everyone"),
        ("abhiram", "You are stupid"),
        ("abhiram", "Idiot person"),
        ("abhiram", "You are a dumb fool"),
        ("abhiram", "This is hate speech")
    ]

    print("\n--- CHAT MODERATION SYSTEM ---\n")
    for user, msg in chat_messages:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {user}: {msg}")
        print(moderator.process_message(user, msg))
        print("-" * 60)


if __name__ == "__main__":
    run_demo()
