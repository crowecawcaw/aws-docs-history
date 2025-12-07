# Cross-modal input

Cross-modal input enables users to send text messages during an active voice
conversation. This feature is particularly useful for scenarios where typing is more
appropriate than speaking, such as sharing URLs or email addresses, providing
sensitive information like passwords or account numbers, sending structured data
like addresses or phone numbers, or clarifying spelling of names or technical
terms.

## How it works

To send cross-modal text input, you use the same event structure as other
content types, but with the `interactive` parameter set to
`true` in the `InputContentStartEvent`. This signals
to Amazon Nova 2 Sonic that the text input is being sent during an active voice
session.

## Event structure

Cross-modal input follows a three-event pattern:

1. **Content Start Event:** Set
   `interactive: true` and `role: "USER"`
2. **Text Input Event:** Provide the text
   content
3. **Content End Event:** Close the content
   segment
