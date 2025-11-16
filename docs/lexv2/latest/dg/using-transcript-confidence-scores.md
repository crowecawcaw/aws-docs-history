# Using voice transcription confidence scores to improve conversations with your Lex V2 bot

When a user makes a voice utterance, Amazon Lex V2 uses automatic speech
recognition (ASR) to transcribe the user's request before it is
interpreted. By default, Amazon Lex V2 uses the most likely transcription of
the audio for interpretation.

In some cases there might be more than one possible transcription of
the audio. For example, a user might make an utterance with an ambiguous
sound, such as "My name is John" that might be understood as "My name is
Juan." In this case, you can use disambiguation techniques or combine
your domain knowledge with the _transcription confidence
score_ to help determine which transcription in a list of
transcriptions is the correct one.

Amazon Lex V2 includes the top transcription and up to two alternate
transcriptions for user input in the request to your Lambda code hook
function. Each transcription contains a confidence score that it is the
correct transcription. Each transcription also includes any slot values
inferred from the user input.

You can compare the confidence scores of two transcriptions to
determine if there is ambiguity between them. For example, if one
transcription has a confidence score of 0.95 and the other has a
confidence score of 0.65, the first transcription is probably correct
and the ambiguity between them is low. If the two transcriptions have
confidence scores of 0.75 and 0.72, the ambiguity between them is high.
You may be able to discriminate between them using your domain
knowledge.

For example, if the inferred slot values in two transcripts with a
confidence score of 0.75 and 0.72 are "John" and "Juan", you can query
the users in your database for the existence of these names and
eliminate one of the transcriptions. If "John" isn't a user in your
database and "Juan" is, you can use the dialog code hook to change the
inferred slot value for the first name to "Juan."

The confidence scores that Amazon Lex V2 returns are comparative values.
Don't rely on them as an absolute score. The values may change based on
improvements to Amazon Lex V2.

Audio transcription confidence scores are available only in the
English (GB) (en_GB) and English (US) (en_US) languages. Confidence
scores are supported only for 8 kHz audio input. Transcription
confidence scores aren't provided for audio input from the [test
window](test-bot.md "test-bot.md") on the Amazon Lex V2 console because it uses 16 kHz audio
input.

###### Note

Before you can use audio transcription confidence scores with an
existing bot, you must first rebuild the bot. Existing versions of a
bot don't support transcription confidence scores. You must create a
new version of the bot to use them.

You can use confidence scores for multiple conversation design
patterns:

- If the highest confidence score falls below a threshold due to
  a noisy environment or poor signal quality, you can prompt the
  user with the same question to capture better quality
  audio.
- If multiple transcriptions have similar confidence scores for
  slot values, such as "John" and "Juan," you can compare the
  values with a pre-existing database to eliminate inputs, or you
  can prompt the user to select one of the two values. For
  example, "say 1 for John or say 2 for Juan."
- If your business logic requires intent switching based on
  specific keywords in an alternative transcript with a confidence
  score close to the top transcript, you can change the intent
  using your dialog code hook Lambda function or using session
  management operations. For more information, see [Session management](#transcription-confidence-session-management "#transcription-confidence-session-management").
  Amazon Lex V2 sends the following JSON structure with up to three
  transcriptions for the user's input to your Lambda code hook
  function:

```

    "transcriptions": [
        {
            "transcription": "string",
            "rawTranscription": "string",
            "transcriptionConfidence": "number",
            },
            "resolvedContext": {
                "intent": "string"
            },
            "resolvedSlots": {
                "string": {
                    "shape": "List",
                    "value": {
                        "originalValue": "string",
                        "resolvedValues": [
                            "string"
                        ]
                    },
                    "values": [
                        {
                            "shape": "Scalar",
                            "value": {
                                "originalValue": "string",
                                "resolvedValues": [
                                    "string"
                                ]
                            }
                        },
                        {
                            "shape": "Scalar",
                            "value": {
                                "originalValue": "string",
                                "resolvedValues": [
                                    "string"
                                ]
                            }
                        }
                    ]
                }
            }
        }
    ]

```

The JSON structure contains transcription text, the intent that was
resolved for the utterance, and values for any slots detected in the
utterance. For text user input, the transcriptions contain a single
transcript with a confidence score of 1.0.

The contents of the transcripts depend on the turn of the conversation
and the recognized intent.

For the first turn, intent elicitation, Amazon Lex V2 determines the top
three transcriptions. For the top transcription, it returns the intent
and any inferred slot values in the transcription.

On subsequent turns, slot elicitation, the results depend on the
inferred intent for each of the transcriptions, as follows.

- If the inferred intent for the top transcript is the same as
  the previous turn and all other transcripts have the same
  intent, then
  - All transcripts contain inferred slot values.

- If the inferred intent for the top transcript is the different
  from the previous turn and all other transcripts have the
  previous intent, then
  - The top transcript contains the inferred slot values
    for the new intent.
  - Other transcripts have the previous intent and
    inferred slot values for the previous intent.

- If the inferred intent for the top transcript is different
  from the previous turn, one transcript is the same as the
  previous intent, and one transcript is a different intent,
  then
  - The top transcript contains the new inferred intent
    and any inferred slot values in the utterance.
  - The transcript that has the previous inferred intent
    contains inferred slot values for that intent.
  - The transcript with the different intent has no
    inferred intent name and no inferred slot values.

- If the inferred intent for the top transcript is the different
  from the previous turn and all other transcripts have different
  intents, then
  - The top transcript contains the new inferred intent
    and any inferred slot values in the utterance.
  - Other transcripts contain no inferred intents and no
    inferred slot values.

- If the inferred intent for the top two transcripts is the same
  and different from the previous turn, and the third transcript
  is a different intent, then
  - The top two transcripts contain the new inferred
    intent and any inferred slot values in the
    utterance.
  - The third transcript has no intent name and no
    resolved slot values.

## Session management

To change the intent that Amazon Lex V2 uses in a conversation with the
user, use the response from your dialog code hook Lambda function. Or
you can use the session management APIs in your custom
application.

### Using a Lambda function with your Lex V2 bot

When you use a Lambda function, Amazon Lex V2 calls it with a JSON
structure that contains the input to the function. The JSON
structure contains a field called `transcriptions`
that contains the possible transcriptions that Amazon Lex V2 has
determined for the utterance. The `transcriptions`
field contains one to three possible transcriptions, each with a
confidence score.

To use the intent from an alternative transcription, you
specify it in the `ConfirmIntent` or the
`ElicitSlot` dialog action in your Lambda
function. To use a slot value from an alternative transcription,
set the value in the `intent` field in your Lambda
function response. For more information, see [Integrating an AWS Lambda function into your Amazon Lex V2 bot](lambda.md "lambda.md").

#### Example code using Lambda with Lex V2

The following code example is a Python Lambda function that
uses audio transcriptions to improve the conversation
experience for the user.

To use the example code, you must have:

- A bot with one language, either English (GB)
  (en_GB) or English (US) (en_US).
- One intent, OrderBirthStone. Make sure that the
  **Use a Lambda function for
  initialization and validation** is
  selected in the **Code hooks**
  section of the intent definition.
- The intent should have two slots, "BirthMonth" and
  "Name," both of type `AMAZON.AlphaNumeric`.
- An alias with the Lambda function defined. For more
  information, see [Creating an AWS Lambda function for your Amazon Lex V2 bot](lambda-attach.md "lambda-attach.md").

```
import time
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# --- Helpers that build all of the responses ---

def elicit_slot(session_attributes, intent_request, slots, slot_to_elicit, message):
    return {
        'sessionState': {
            'dialogAction': {
                'type': 'ElicitSlot',
                'slotToElicit': slot_to_elicit
            },
            'intent': {
                'name': intent_request['sessionState']['intent']['name'],
                'slots': slots,
                'state': 'InProgress'
            },
            'sessionAttributes': session_attributes,
            'originatingRequestId': 'e3ab4d42-fb5f-4cc3-bb78-caaf6fc7cccd'
        },
        'sessionId': intent_request['sessionId'],
        'messages': [message],
        'requestAttributes': intent_request['requestAttributes'] if 'requestAttributes' in intent_request else None
    }


def close(intent_request, session_attributes, fulfillment_state, message):
    intent_request['sessionState']['intent']['state'] = fulfillment_state
    return {
        'sessionState': {
            'sessionAttributes': session_attributes,
            'dialogAction': {
                'type': 'Close'
            },
            'intent': intent_request['sessionState']['intent'],
            'originatingRequestId': '3ab4d42-fb5f-4cc3-bb78-caaf6fc7cccd'
        },
        'messages': [message],
        'sessionId': intent_request['sessionId'],
        'requestAttributes': intent_request['requestAttributes'] if 'requestAttributes' in intent_request else None
    }


def delegate(intent_request, session_attributes):
    return {
        'sessionState': {
            'dialogAction': {
                'type': 'Delegate'
            },
            'intent': intent_request['sessionState']['intent'],
            'sessionAttributes': session_attributes,
            'originatingRequestId': 'abc'
        },
        'sessionId': intent_request['sessionId'],
        'requestAttributes': intent_request['requestAttributes'] if 'requestAttributes' in intent_request else None
    }


def get_session_attributes(intent_request):
    sessionState = intent_request['sessionState']
    if 'sessionAttributes' in sessionState:
        return sessionState['sessionAttributes']

    return {}


def get_slots(intent_request):
    return intent_request['sessionState']['intent']['slots']


""" --- Functions that control the behavior of the bot --- """


def order_birth_stone(intent_request):
    """
    Performs dialog management and fulfillment for ordering a birth stone.
    Beyond fulfillment, the implementation for this intent demonstrates the following:
    1) Use of N best transcriptions to re prompt user when confidence for top transcript is below a threshold
    2) Overrides resolved slot for birth month from a known fixed list if the top transcript
    is not accurate.
    """

    transcriptions = intent_request['transcriptions']

    if intent_request['invocationSource'] == 'DialogCodeHook':
        # Disambiguate if there are multiple transcriptions and the top transcription
        # confidence is below a threshold (0.8 here)
        if len(transcriptions) > 1 and transcriptions[0]['transcriptionConfidence'] < 0.8:
            if transcriptions[0]['resolvedSlots'] is not {} and 'Name' in transcriptions[0]['resolvedSlots'] and \
                    transcriptions[0]['resolvedSlots']['Name'] is not None:
                return prompt_for_name(intent_request)
            elif transcriptions[0]['resolvedSlots'] is not {} and 'BirthMonth' in transcriptions[0]['resolvedSlots'] and \
                    transcriptions[0]['resolvedSlots']['BirthMonth'] is not None:
                return validate_month(intent_request)

    return continue_conversation(intent_request)


def prompt_for_name(intent_request):
    """
    If the confidence for the name is not high enough, re prompt the user with the recognized names
    so it can be confirmed.
    """
    resolved_names = []
    for transcription in intent_request['transcriptions']:
        if transcription['resolvedSlots'] is not {} and 'Name' in transcription['resolvedSlots'] and \
                transcription['resolvedSlots']['Name'] is not None:
            resolved_names.append(transcription['resolvedSlots']['Name']['value']['originalValue'])
    if len(resolved_names) > 1:
        session_attributes = get_session_attributes(intent_request)
        slots = get_slots(intent_request)
        return elicit_slot(session_attributes, intent_request, slots, 'Name',
                           {'contentType': 'PlainText',
                            'content': 'Sorry, did you say your name is {} ?'.format(" or ".join(resolved_names))})
    else:
        return continue_conversation(intent_request)


def validate_month(intent_request):
    """
    Validate month from an expected list, if not valid looks for other transcriptions and to see if the month
    recognized there has an expected value. If there is, replace with that and if not continue conversation.
    """

    expected_months = ['january', 'february', 'march']
    resolved_months = []
    for transcription in intent_request['transcriptions']:
        if transcription['resolvedSlots'] is not {} and 'BirthMonth' in transcription['resolvedSlots'] and \
                transcription['resolvedSlots']['BirthMonth'] is not None:
            resolved_months.append(transcription['resolvedSlots']['BirthMonth']['value']['originalValue'])

    for resolved_month in resolved_months:
        if resolved_month in expected_months:
            intent_request['sessionState']['intent']['slots']['BirthMonth']['resolvedValues'] = [resolved_month]
            break

    return continue_conversation(intent_request)


def continue_conversation(event):
    session_attributes = get_session_attributes(event)

    if event["invocationSource"] == "DialogCodeHook":
        return delegate(event, session_attributes)


# --- Intents ---


def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    logger.debug('dispatch sessionId={}, intentName={}'.format(intent_request['sessionId'],
                                                               intent_request['sessionState']['intent']['name']))

    intent_name = intent_request['sessionState']['intent']['name']

    # Dispatch to your bot's intent handlers
    if intent_name == 'OrderBirthStone':
        return order_birth_stone(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')


# --- Main handler ---


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.

    """
    # By default, treat the user request as coming from the America/New_York time zone.
    os.environ['TZ'] = 'America/New_York'
    time.tzset()
    logger.debug('event={}'.format(event))

    return dispatch(event)
```

### Using the session management API to choose a different intent or slot value

To use a different intent from the current intent, use the
[PutSession](../APIReference/API_runtime_PutSession.md "../APIReference/API_runtime_PutSession.md") operation. For
example, if you decide that the first alternative is preferable
to the intent that Amazon Lex V2 chose, you can use the
`PutSession` operation to change intents. That
way the next intent that the user interacts with will be the one
that you selected.

You can also use the `PutSession` operation to
change the slot value in the `intent` structure to
use a value from an alternative transcription.

For more information, see [Understanding Amazon Lex V2 bot sessions](managing-sessions.md "managing-sessions.md").
