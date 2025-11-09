# Datetime Conversion

Functions

You specify date and time formats using patterned letters. Date and time pattern strings use
unquoted letters from 'A' to 'Z' and from 'a' to 'z', with each letter representing a formatting
element.

For more information, see [Class
SimpleDateFormat](http://docs.oracle.com/javase/7/docs/api/index.html?java/text/SimpleDateFormat.html "http://docs.oracle.com/javase/7/docs/api/index.html?java/text/SimpleDateFormat.html") on the Oracle website.

###### Note

If you include other characters, they will be incorporated into the output string during
formatting or compared to the input string during parsing.

The pattern letters in the following table are defined (all other characters from 'A' to 'Z'
and from 'a' to 'z' are reserved).

| Letter | Date or Time Component                           | Presentation       | Examples                              |
| ------ | ------------------------------------------------ | ------------------ | ------------------------------------- |
| y      | Year                                             | Year               | yyyy; yy 2018;18                      |
| Y      | Week year                                        | Year               | YYYY; YY 2009; 09                     |
| M      | Month in year                                    | Month              | MMM;MM;MM July; Jul; 07               |
| w      | Week in year                                     | Number             | ww; 27                                |
| W      | Week in month                                    | Number             | W 2                                   |
| D      | Day in year                                      | Number             | DDD 321                               |
| d      | Day in month                                     | Number             | dd 10                                 |
| F      | Day of week in month                             | Number             | F 2                                   |
| E      | Day name in week                                 | Text               | Tuesday; Tue                          |
| u      | Day number of week (1 = Monday, ..., 7 = Sunday) | Number             | 1                                     |
| a      | Am/pm marker                                     | Text               | PM                                    |
| H      | Hour in day (0-23)                               | Number             | 0                                     |
| k      | Hour in day (1-24)                               | Number             | 24                                    |
| K      | Hour in am/pm (0-11)                             | Number             | 0                                     |
| h      | Hour in am/pm (1-12)                             | Number             | 12                                    |
| m      | Minute in hour                                   | Number             | 30                                    |
| s      | Second in minute                                 | Number             | 55                                    |
| S      | Millisecond                                      | Number             | 978                                   |
| z      | Time zone                                        | General time zone  | Pacific Standard Time; PST; GMT-08:00 |
| Z      | Time zone                                        | RFC 822 time zone  | -0800                                 |
| X      | Time zone                                        | ISO 8601 time zone | -08; -0800; -08:00                    |

You determine the exact presentation by repeating pattern letters, along the lines of
YYYY.

###### Text

If the number of repeated pattern letters is 4 or more, the full form is used; otherwise
a short or abbreviated form is used if available. For parsing, both forms are accepted,
independent of the number of pattern letters.

###### Number

For formatting, the number of pattern letters is the minimum number of digits, and shorter
numbers are zero-padded to this amount. For parsing, the number of pattern letters is ignored
unless it's needed to separate two adjacent fields.

###### Year

If the formatter's Calendar is the Gregorian calendar, the following rules are
applied.

- For formatting, if the number of pattern letters is 2, the year is truncated to 2
  digits; otherwise it is interpreted as a number.
- For parsing, if the number of pattern letters is more than 2, the year is interpreted
  literally, regardless of the number of digits. So using the pattern "MM/dd/yyyy", "01/11/12"
  parses to Jan 11, 12 A.D.
  For parsing with the abbreviated year pattern ("y" or "yy"), SimpleDateFormat must interpret
  the abbreviated year relative to some century. It does this by adjusting dates to be within 80
  years before and 20 years after the time the SimpleDateFormat instance is created. For example,
  using a pattern of "MM/dd/yy" and a SimpleDateFormat instance created on Jan 1, 2018, the string
  "01/11/12" would be interpreted as Jan 11, 2012 while the string "05/04/64" would be interpreted
  as May 4, 1964. During parsing, only strings consisting of exactly two digits, as defined by
  Character.isDigit(char), will be parsed into the default century. Any other numeric string, such
  as a one digit string, a three or more digit string, or a two digit string that isn't all digits
  (for example, "-1"), is interpreted literally. So "01/02/3" or "01/02/003" are parsed, using the
  same pattern, as Jan 2, 3 AD. Likewise, "01/02/-3" is parsed as Jan 2, 4 BC.

Otherwise, calendar system specific forms are applied. For both formatting and parsing, if
the number of pattern letters is 4 or more, a calendar specific long form is used. Otherwise, a
calendar specific short or abbreviated form is used.
