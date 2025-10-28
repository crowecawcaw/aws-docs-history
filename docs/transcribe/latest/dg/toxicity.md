# Detecting toxic speech

Toxic speech detection is designed to help moderate social media platforms that involve
peer-to-peer dialogue, such as online gaming and social chat platforms. The use of toxic
speech can be deeply detrimental to individuals, peer groups, and communities. Flagging harmful
language helps organizations keep conversations civil and maintain a safe and inclusive online
environment for users to create, share and participate freely.

Amazon Transcribe Toxicity Detection leverages both audio and text-based cues to identify and
classify voice-based toxic content across seven categories including sexual harassment,
hate speech, threat, abuse, profanity, insult, and graphic. In addition to text,
Amazon Transcribe Toxicity Detection uses speech cues, such as tones and pitch to hone in
on toxic intent in speech. This is an improvement from standard content moderation systems
that are designed to focus only on specific terms, without accounting for intention.

Amazon Transcribe flags and categorizes toxic speech, which minimizes the volume of data that
must be manually processed. This enables content moderators to quickly and efficiently manage
the discourse on their platforms.

Toxic speech categories include:

- **Profanity**: Speech that contains words, phrases, or acronyms that are impolite, vulgar, or offensive.
- **Hate speech**: Speech that criticizes, insults, denounces, or dehumanizes a person or group on the basis of an identity (such as race, ethnicity, gender, religion, sexual orientation, ability, and national origin).
- **Sexual**: Speech that indicates sexual interest, activity, or arousal using direct or indirect references to body parts, physical traits, or sex.
- **Insults**: Speech that includes demeaning, humiliating, mocking, insulting, or belittling language. This type of language is also labeled as bullying.
- **Violence or threat**: Speech that includes threats seeking to inflict pain, injury, or hostility toward a person or group.
- **Graphic**: Speech that uses visually descriptive and unpleasantly vivid imagery. This type of language is often intentionally verbose to amplify a recipient's discomfort.
- **Harassment or abusive**: Speech intended to affect the psychological well-being of the recipient, including demeaning and objectifying terms. This type of language is also labeled as harassment.

Toxicity detection analyzes speech segments (the speech between natural pauses) and assigns
confidence scores to these segments. Confidence scores are values between 0 and 1. A larger
confidence score indicates a greater likelihood that the content is toxic speech in the associated
category. You can use these confidence scores to set the appropriate threshold of toxicity
detection for your use case.

###### Note

Toxicity detection is only available for batch transcriptions in US English `(en-US)`.

View [example output](toxicity-using.md#toxicity-using-output.title "toxicity-using.md#toxicity-using-output.title") in JSON format.
