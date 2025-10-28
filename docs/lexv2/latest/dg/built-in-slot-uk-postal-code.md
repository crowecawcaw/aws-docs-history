# AMAZON.UKPostalCode

Converts words that represent a UK postal code to a standard
format for postal codes in the United Kingdom. The `AMAZON.UKPostalCode` slot type validates
and resolves the post code to a set of standardized formats, but
it doesn't check to make sure that the post code is valid. Your
application must validate the post code.

The `AMAZON.UKPostalCode` slot type is available
only in the English (UK) (en-GB) locale.

The `AMAZON.UKPostalCode` slot type supports inputs
using spelling styles. You can use the spell-by-letter and spell-by-word
styles to help your customers enter letters. For more information, see [Capturing slot values with spelling styles during the conversation](spelling-styles.md "spelling-styles.md").

The slot type recognizes only the valid post code formats listed below, used in the United Kingdom. The valid formats are ("A"
representis a letter, and "9" represents a digit):

- AA9A 9AA
- A9A 9AA
- A9 9AA
- A99 9AA
- AA9 9AA
- AA99 9AA
  For text input, the user can enter any mix of upper and lower
  case letters. The user can use or omit the space in the post
  code. The resolved value will always include the space in the
  proper location for the post code.

For spoken input, the user can speak the individual
characters, or they can use double letter pronunciations, such
as "double A" or "double 9". They can also use double-digit
pronunciations, such as "ninety-nine" for "99".

###### Note

Not all UK postal codes are recognized. Only the formats listed above are supported.
