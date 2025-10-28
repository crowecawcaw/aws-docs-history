# AMAZON.LastName

Commonly used last names. For names that sound alike that are
spelled differently, Amazon Lex V2 sends your intent a single common
form.

The `AMAZON.LastName` slot type supports inputs using
spelling styles. You can use the spell-by-letter and spell-by-word
styles to help your customers enter names. For more information, see [Capturing slot values with spelling styles during the conversation](spelling-styles.md "spelling-styles.md").

Examples:

- Brosky
- Dasher
- Evers
- Parres
- Welt
  AMAZON.LastName also returns a list of closely related names based
  on the original value. You can use the list of resolved values to recover
  from typos, confirm the name with the user, or perform a database look-up for
  valid names in your user directory.

For example, the input "Smith" may result in returning additional related
names such as "Smyth" and "Smithe".

The following shows the response format for the `AMAZON.LastName` built-in
slot type:

```

"value": {
    "originalValue": "Smith",
    "interpretedValue": "Smith",
    "resolvedValues": [
        "Smith",
        "Smyth",
        "Smithe"
    ]
}
```
