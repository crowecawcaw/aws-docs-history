# AMAZON.FirstName

Commonly used first names. This slot type recognizes
formal names, informal nicknames, and names consisting of
more than one word. The name sent to your
intent is the value sent by the user. Amazon Lex V2 doesn't convert
from the nickname to the formal name.

For first names that sound alike but are spelled differently,
Amazon Lex V2 sends your intent a single common form.

The `AMAZON.FirstName` slot type supports inputs
using spelling styles. You can use the spell-by-letter and
spell-by-word styles to help your customers enter names.
For more information, see [Capturing slot values with spelling styles during the conversation](spelling-styles.md "spelling-styles.md").

Examples:

- Emily
- John
- Sophie
- Anil Kumar
  AMAZON.FirstName also returns a list of closely related names based
  on the original value. You can use the list of resolved values to recover
  from typos, confirm the name with the user, or perform a database look-up for
  valid names in your user directory.

For example, the input "John" may result in returning additional related
names such as "John J" and "John-Paul".

The following shows the response format for the `AMAZON.FirstName` built-in
slot type:

```

"value": {
    "originalValue": "John",
    "interpretedValue": "John",
    "resolvedValues": [
        "John",
        "John J.",
        "John-Paul"
    ]
}
```
