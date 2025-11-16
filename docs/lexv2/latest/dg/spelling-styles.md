# Capturing slot values with spelling styles during the conversation

Amazon Lex V2 provides built-in slots to capture user-specific information
such as first name, last name, email address or alphanumeric
identifiers. For example, you can use the `AMAZON.LastName` slot to
capture surnames such as "Jackson" or "Garcia." However, Amazon Lex V2 may get
confused with surnames that are difficult to pronounce or that are not
common in a locale, such as "Xiulan." To capture such names, you can ask
the user to provide input in _spell by letter_ or
_spell by word_ style.

Amazon Lex V2 provides three _slot elicitation styles_ for
you to use. When you set a slot elicitation style, it changes the way
Amazon Lex V2 interprets the input from the user.

**Spell by letter** – With this
style, you can instruct the bot to listen for spellings instead of the
whole phrase. For example, to capture a last name such as "Xiulan," you
can tell the user to spell out their last name one letter at a time. The
bot will capture the spelling and resolve the letters to a word. For
example, if the user says "x i u l a n," the bot captures the last name
as "xiulan."

**Spell by word** – In voice
conversations, especially using the telephone, there are a few letters,
such as "t," "b," "p", that sound similar. When capturing alphanumeric
values or spelling names results in an incorrect value, you can prompt
the user to provide an identifying word along with the letter. For
example, if the voice response to a request for a booking ID is
"abp123," your bot might instead recognize the phrase "ab**b**123" instead. If this is an incorrect value,
you can ask the user to provide the input as "a as in alpha b as in boy
p as in peter one two three." The bot will resolve the input to
"abp123."

When using spell by word, you can use the following formats:

- "as in" (a as in apple)
- "for" (a for apple)
- "like" (a like apple)
  **Default** – This is the natural
  style of slot capture using word pronunciation. For example, it can
  capture names such as "John Stiles" naturally. If a slot elicitation
  style isn't specified, the bot uses the default style. For the
  `AMAZON.AlphaNumeric` and `AMAZON.UKPostal` code slot types, the default
  style supports spell by letter input.

If the name "Xiulan" is spoken using a mix of letters and words , such
as "x as in x-ray i u l as in lion a n" the slot elicitation style must
be set to spell-by-word style. The spell-by-letter style won't recognize
it.

You should create a voice interface that captures slot values with
natural conversational style for a better experience. For inputs that
are not correctly captured using the natural style, you can re-prompt
the user and set the slot elicitation style to spell-by-letter or
spell-by-word.

You can use spell-by-word and spell-by-letter styles for the following
slot types in the English (US), English (UK), and English (Australia) languages:

- [AMAZON.AlphaNumeric](built-in-slot-alphanumeric.md "built-in-slot-alphanumeric.md")
- [AMAZON.EmailAddress](built-in-slot-email.md "built-in-slot-email.md")
- [AMAZON.FirstName](built-in-slot-first-name.md "built-in-slot-first-name.md")
- [AMAZON.LastName](built-in-slot-last-name.md "built-in-slot-last-name.md")
- [AMAZON.UKPostalCode](built-in-slot-uk-postal-code.md "built-in-slot-uk-postal-code.md")
- [Custom Slot Types](custom-slot-types.md "custom-slot-types.md")

## Enabling spelling

You enable spell-by-letter and spell-by-word at runtime when you
are eliciting slots from the user. You can set the spelling style
with the [PutSession](../APIReference/API_runtime_PutSession.md "../APIReference/API_runtime_PutSession.md"),
[RecognizeText](../APIReference/API_runtime_RecognizeText.md "../APIReference/API_runtime_RecognizeText.md"),
[RecognizeUtterance](../APIReference/API_runtime_RecognizeUtterance.md "../APIReference/API_runtime_RecognizeUtterance.md"), or
[StartConversation](../APIReference/API_runtime_StartConversation.md "../APIReference/API_runtime_StartConversation.md") operation. You
can also enable spell-by-letter and spell-by-word using a Lambda
function.

You set the spelling style using the `dialogAction`
field of the `sessionState` field in the request of one of the aforementioned API operations or when configuring the Lambda response (see [AWS Lambda response format for Lex V2](lambda-response-format.md "lambda-response-format.md") for more information). You can only set the style
when the dialog action type is `ElicitSlot` and when the
slot to elicit is one of the supported slot types.

The following JSON code shows the `dialogAction` field
set to use the spell-by-word style:

```
"dialogAction": {
    "slotElicitationStyle": "SpellByWord",
    "slotToElicit": "BookingId",
    "type": "ElicitSlot"
}
```

The `slotElicitationStyle` field can be set to
`SpellByLetter`, `SpellByWord`, or
`Default`. If you don't specify a value, then the
value is set to `Default`.

###### Note

You can't enable spell-by-letter or spell-by-word elicitation styles through the console.

## Example code using Lambda and Lex V2

Changing the spelling style is usually performed if the first
attempt to resolve a slot value that didn't work. The following code
example is a Python Lambda function that uses the spell-by-word style
on the second attempt to resolve a slot.

To use the example code, you must have:

- A bot with one language, English (GB) (en_GB).
- One intent, "CheckAccount" with one sample utterance, "I
  would like to check my account". Make sure that
  **Use a Lambda function for initialization and
  validation** is selected in the **Code
  hooks** section of the intent
  definition.
- The intent should have one slot, "PostalCode", of the
  `AMAZON.UKPostalCode` built-in type.
- An alias with the Lambda function defined. For more
  information, see [Creating an AWS Lambda function for your Amazon Lex V2 bot](lambda-attach.md "lambda-attach.md").

```
import json
import time
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# --- Helpers that build all of the responses ---

def get_slots(intent_request):
    return intent_request['sessionState']['intent']['slots']

def get_session_attributes(intent_request):
    sessionState = intent_request['sessionState']
    if 'sessionAttributes' in sessionState:
        return sessionState['sessionAttributes']
    return {}

def get_slot(intent_request, slotName):
    slots = get_slots(intent_request)
    if slots is not None and slotName in slots and slots[slotName] is not None:
        logger.debug('resolvedValue={}'.format(slots[slotName]['value']['resolvedValues']))
        return slots[slotName]['value']['resolvedValues']
    else:
        return None

def elicit_slot(session_attributes, intent_request, slots, slot_to_elicit, slot_elicitation_style, message):
    return {'sessionState': {'dialogAction': {'type': 'ElicitSlot',
                                              'slotToElicit': slot_to_elicit,
                                              'slotElicitationStyle': slot_elicitation_style
                                              },
                             'intent': {'name': intent_request['sessionState']['intent']['name'],
                                        'slots': slots,
                                        'state': 'InProgress'
                                        },
                             'sessionAttributes': session_attributes,
                             'originatingRequestId': 'REQUESTID'
                             },
            'sessionId': intent_request['sessionId'],
            'messages': [ message ],
            'requestAttributes': intent_request['requestAttributes']
            if 'requestAttributes' in intent_request else None
            }

def build_validation_result(isvalid, violated_slot, slot_elicitation_style, message_content):
    return {'isValid': isvalid,
            'violatedSlot': violated_slot,
            'slotElicitationStyle': slot_elicitation_style,
            'message': {'contentType': 'PlainText',
            'content': message_content}
            }

def GetItemInDatabase(postal_code):
    """
    Perform database check for transcribed postal code. This is a no-op
    check that shows that postal_code can't be found in the database.
    """
    return None

def validate_postal_code(intent_request):

    postal_code = get_slot(intent_request, 'PostalCode')

    if GetItemInDatabase(postal_code) is None:
        return build_validation_result(
            False,
            'PostalCode',
            'SpellByWord',
            "Sorry, I can't find your information. " +
            "To try again, spell out your postal " +
            "code using words, like a as in apple."
        )
    return {'isValid': True}

def check_account(intent_request):
    """
    Performs dialog management and fulfillment for checking an account
    with a postal code. Besides fulfillment, the implementation for this
    intent demonstrates the following:
    1) Use of elicitSlot in slot validation and re-prompting.
    2) Use of sessionAttributes to pass information that can be used to
        guide a conversation.
    """
    slots = get_slots(intent_request)
    postal_code = get_slot(intent_request, 'PostalCode')
    session_attributes = get_session_attributes(intent_request)

    if intent_request['invocationSource'] == 'DialogCodeHook':
        # Validate the PostalCode slot. If any aren't valid,
        # re-elicit for the value.
        validation_result = validate_postal_code(intent_request)
        if not validation_result['isValid']:
            slots[validation_result['violatedSlot']] = None
            return elicit_slot(
                session_attributes,
                intent_request,
                slots,
                validation_result['violatedSlot'],
                validation_result['slotElicitationStyle'],
                validation_result['message']
            )

        return close(
            intent_request,
            session_attributes,
            'Fulfilled',
            {'contentType': 'PlainText',
             'content': 'Thanks'
             }
        )

def close(intent_request, session_attributes, fulfillment_state, message):
    intent_request['sessionState']['intent']['state'] = fulfillment_state
    return {
        'sessionState': {
            'sessionAttributes': session_attributes,
            'dialogAction': {
                'type': 'Close'
            },
            'intent': intent_request['sessionState']['intent'],
            'originatingRequestId': 'xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
        },
        'messages': [ message ],
        'sessionId': intent_request['sessionId'],
        'requestAttributes': intent_request['requestAttributes'] if 'requestAttributes' in intent_request else None
    }

# --- Intents ---

def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """
    intent_name = intent_request['sessionState']['intent']['name']
    response = None

    # Dispatch to your bot's intent handlers
    if intent_name == 'CheckAccount':
        response = check_account(intent_request)

    return response

# --- Main handler ---

def lambda_handler(event, context):
    """
    Route the incoming request based on the intent.

    The JSON body of the request is provided in the event slot.
    """

    # By default, treat the user request as coming from
    # Eastern Standard Time.
    os.environ['TZ'] = 'America/New_York'
    time.tzset()

    logger.debug('event={}'.format(json.dumps(event)))
    response = dispatch(event)
    logger.debug("response={}".format(json.dumps(response)))

    return response
```
