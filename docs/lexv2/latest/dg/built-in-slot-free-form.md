# AMAZON.FreeFormInput

`AMAZON.FreeFormInput` can be used to capture free
form input from the end user. It recognizes strings that consist of
words or characters. The resolved value is the entire input
utterance.

Example:

Bot: Please provide feedback from your call experience.

User: I got the answers to all of my questions, and I
was able to complete the transaction.

Note:

- `AMAZON.FreeFormInput` can be used to capture free form input as-is
  from the end user.
- `AMAZON.FreeFormInput` cannot be used in intent sample utterances.
- `AMAZON.FreeFormInput` cannot have slot sample utterances.
- `AMAZON.FreeFormInput` is only recognized when elicited for.
- `AMAZON.FreeFormInput` does not support wait and continue.
- `AMAZON.FreeFormInput` is currently not supported in the Amazon Connect Chat
  channel.
- When a `AMAZON.FreeFormInput` slot is elicited, `FallbackIntent`
  will not be triggered.
- When a `AMAZON.FreeFormInput` slot is elicited, there will be no intent
  switch.
