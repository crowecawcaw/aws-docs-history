# Example of selective conversation log capture

Here is an example of a business use case for selective conversation log capture.

**Use case:**

A fintech company utilizes an Amazon Lex V2 bot to support their IVR system, which allows users to make bill payments. In order to meet compliance and auditing requirements, they must retain audio recordings of user-provided authorization consent. However, enabling general audio logs is not feasible as it would make them non-compliant, because it is not possible to obfuscate sensitive slots like CardNumber, CVV, and other information in the audio logs. Instead, they can enable selective conversation log capture for audio logs and set session attribute to only produce audio logs for utterance that has authorization consent.

**BotAlias Settings:**

- Text Logs Enabled : true
- Text Logs Selective Logging Enabled : false
- Audio Logs Enabled : true
- Audio Logs Selective Logging Enabled : true
  **Session Attributes:**

`x-amz-lex:enable-audio-logging:PayBill:AuthorizationConsent = "true"`

**Sample Conversation:**

- User (Audio Input): "I want to pay my bill with bill number 35XU68."
- Bot: "What is the due amount in dollars?"
- User (Audio Input): "235."
- Bot: "What is your credit card number?"
- User (Audio Input): "9239829722200348."
- Bot: "You're paying 235 dollars using your credit card number ending with 0348. Please say 'I authorize to pay 235 dollars.'"
- User (Audio Input): "I authorize to pay 235 dollars."
- Bot: "Your bill has been paid."
  **Conversation Logs output:**

In this situation, text logs will be produced for all turns. However, audio logs will only be recorded for the particular turn when the **AuthorizationConsent** slot within the **PayBill** intent was elicited, and no audio logs will be produced for any other turn.
