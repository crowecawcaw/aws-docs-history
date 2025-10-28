# AMAZON.Confirmation

This slot type recognizes input phrases that corresponds to 'Yes', 'No',
'Maybe', and 'Don't know' phrases and words for Amazon Lex V2 and converts it one
of the four values. It can be used to capture confirmation or acknowledgement
from the user. Based on the final resolved value, you can create conditions
to design multiple conversation paths.

For example:

if {confirmation} = "Yes", fulfill the intent

else, elicit another slot

Examples:

- Yes: Yeah, Yep, Ok, Sure, I have it, I can agree...
- No: Nope, Negative, Naw, Forget it, I'll decline, No way...
- Maybe: It's possible, Perhaps, Sometimes, I might, That could be right...
- Don't know: Dunno, Unknown, No idea, Not sure about it, Who knows...
  As of August 17th, 2023, if there is an existing custom slot type named "Confirmation",
  the name must be changed to avoid conflict with the built-in slot Confirmation. In the left
  side navigation in the Lex console, go to the slot type (for an existing custom slot type
  named Confirmation) and update slot type name. The new slot type name must not be “Confirmation,”
  which is a reserved keyword for the built-in confirmation slot type.
