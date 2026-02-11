# abusive-detects-on-chat-system
🛡️ Abuse Detection System
Overview

The Abuse Detection module identifies inappropriate, toxic, or harmful language in chat messages. It helps maintain a safe chat environment by monitoring user behavior and applying moderation rules automatically.

🎯 Key Features

Abusive Word Detection – Detects predefined offensive terms

Toxicity Scoring – Calculates severity based on abusive content

Progressive Warning System – Issues warnings before blocking users

Automatic User Blocking – Blocks repeated offenders

Message Logging – Records abusive messages for review

⚙️ How It Works

User sends a message

System scans message for abusive words

Toxicity score is calculated

Warning issued if abuse detected

User blocked after repeated violations

📊 Warning Levels
Warning Level	Action
Warning 1	Notify user
Warning 2	Strong warning
Warning 3	Final warning
Warning 4	🚫 User blocked
🧠 Detection Methods
Keyword Matching

Uses predefined abusive word list

Case-insensitive detection

Obfuscation Handling

Detects altered abusive words

Example: 1d10t → idiot

Toxicity Density

Calculates percentage of abusive words

Higher percentage = stronger action

💻 Example Python Code
abusive_words = ["idiot", "stupid", "hate"]

def detect_abuse(message):
    words = message.lower().split()
    abusive_count = sum(1 for w in words if w in abusive_words)

    if abusive_count > 0:
        print("⚠️ Abusive message detected")
    else:
        print("✅ Clean message")

detect_abuse("You are stupid")

🚨 Example Output
Input: "You are stupid"
Output: ⚠️ Abusive message detected

🔧 Configuration Example
WARNING_LIMIT = 3
BLOCK_LIMIT = 4

ABUSIVE_WORDS = {
    "idiot",
    "stupid",
    "hate"
}

📌 Best Practices

Keep abusive word list updated

Use AI sentiment analysis for accuracy

Log violations for admin review

Combine abuse detection with spam filtering
