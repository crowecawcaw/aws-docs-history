

# Text rules

The following rules apply to the text of questions and options:
+ **Question text** – 1–256 characters, and no more than 256 bytes in UTF-8.
+ **Option text** – 1–16 characters, and no more than 16 bytes in UTF-8.
+ **Unique option text** – Option text must be unique within a question. Elemental Inference ignores case in this comparison, so `Red` and `red` conflict. Spaces count in the comparison.

Characters in some scripts use more than one byte each in UTF-8. Text in those scripts fits fewer characters than the character limit.

Question text and option text can contain the following characters:
+ Letters in any script
+ Combining marks
+ Digits
+ Spaces
+ The following punctuation marks: `.` `,` `?` `!` `(` `)` `-` `:` `;` `/` `&` `%`
+ Straight apostrophes (`'`) and straight quotation marks (`"`)
+ The right single quotation mark (U\+2019), and the left and right double quotation marks (U\+201C and U\+201D)

Elemental Inference rejects all other characters. For example, it rejects `<` `>` `[` `]` `{` `}` `_` `#` `*`, emoji, tabs, and line breaks. As a result, text such as `<start_of_turn>` or `[tag]` isn't allowed.