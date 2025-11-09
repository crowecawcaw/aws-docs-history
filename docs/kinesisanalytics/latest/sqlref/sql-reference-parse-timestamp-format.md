# Date and Time Patterns

Date and time formats are specified by date and time pattern strings. In these pattern
strings, unquoted letters from A to Z and from a to z represent components of a data or time
value. If a letter or text string is enclosed within a pair of single quotes, that letter or
text is not interpreted but rather used as is, as are all other characters in the pattern
string. During printing, that letter or text is copied as is to the output string; during
parsing, they are matched against the input string. "''" represents a single quote.

The following pattern letters are defined for the indicated Date or Time Component. All
other characters from 'A' to 'Z' and from 'a' to 'z' are reserved. For an alphabetic ordering of
the pattern letters, see
[Date and Time Pattern Letters in Alphabetic Order](#PATTERNSINALFAORDR "#PATTERNSINALFAORDR").

| Date or Time Component | Pattern Letter | Presentation as text or number                                                                  | Examples                              |
| ---------------------- | -------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------- |
| Era designator         | G              | [Text](#sql-reference-parse-timestamp-format-text "#sql-reference-parse-timestamp-format-text") | AD                                    |
| Year                   | y              | Year                                                                                            | 1996; 96                              |
| Month in year          | M              | Month                                                                                           | July; Jul; 07                         |
| Week in year           | w              | Number                                                                                          | 27                                    |
| Week in month          | W              | Number                                                                                          | 2                                     |
| Day in year            | D              | Number                                                                                          | 189                                   |
| Day in month           | d              | Number                                                                                          | 10                                    |
| Day of week in month   | F              | Number                                                                                          | 2                                     |
| Day in week            | E              | [Text](#sql-reference-parse-timestamp-format-text "#sql-reference-parse-timestamp-format-text") | EE=Tu; EEE=Tue; EEEE=Tuesday          |
| Am/pm marker           | a              | [Text](#sql-reference-parse-timestamp-format-text "#sql-reference-parse-timestamp-format-text") | PM                                    |
| Hour in day (0-23)     | H              | Number                                                                                          | 0                                     |
| Hour in day (1-24)     | k              | Number                                                                                          | 24                                    |
| Hour in am/pm (0-11)   | K              | Number                                                                                          | 0                                     |
| Hour in am/pm (1-12)   | h              | Number                                                                                          | 12                                    |
| Minute in hour         | m              | Number                                                                                          | 30                                    |
| Second in minute       | s              | Number                                                                                          | 55                                    |
| Millisecond            | S              | Number                                                                                          | 978                                   |
| Time zone              | z              | General                                                                                         | Pacific Standard Time; PST; GMT-08:00 |
| Time zone              | Z              | RFC                                                                                             | -0800                                 |

Pattern letters are usually repeated, as their number determines the exact
presentation:

## Text

For formatting, if the number of pattern letters is 4 or more, the full form is used;
otherwise a short or abbreviated form is used if available. For parsing, both forms are
accepted, independent of the number of pattern letters.

## Number

For formatting, the number of pattern letters is the minimum number of digits, and shorter
numbers are zero-padded to this amount. For parsing, the number of pattern letters is ignored
unless it's needed to separate two adjacent fields.

## Year

Time zones are interpreted as text if they have names. For time zones representing a GMT
offset value, the following syntax is used:

```
GMTOffsetTimeZone:
GMT Sign Hours : Minutes
Sign: one of
+ -
Hours:
Digit
Digit Digit
Minutes:
Digit Digit
Digit: one of
0 1 2 3 4 5 6 7 8 9

```

Hours must be between 0 and 23, and Minutes must be between 00 and 59. The format is
locale independent and digits must be taken from the Basic Latin block of the Unicode
standard.

For parsing, RFC 822 time zones are also accepted.

## RFC 822 time zone

For formatting, the RFC 822 4-digit time zone format is used:

```
RFC822TimeZone:
Sign TwoDigitHours Minutes
TwoDigitHours:
Digit Digit

```

TwoDigitHours must be between 00 and 23. Other definitions are as for
general time zones.

For parsing, general time zones
are also accepted.

SimpleDateFormat also supports ''localized date and time pattern'' strings. In these
strings, the pattern letters described above may be replaced with other, locale dependent,
pattern letters. SimpleDateFormat does not deal with the localization of text other than the
pattern letters; that's up to the client of the class.

## Examples

The following examples show how date and time patterns are interpreted in the U.S. locale.
The given date and time are 2001-07-04 12:08:56 local time in the U.S. Pacific time
zone.

| Date and Time Pattern          | Result                               |
| ------------------------------ | ------------------------------------ |
| "yyyy.MM.dd G 'at' HH:mm:ss z" | 2001.07.04 AD at 12:08:56 PDT        |
| "EEE, MMM d, ''yy"             | Wed, Jul 4, '01                      |
| "h:mm a"                       | 12:08 PM                             |
| "hh 'o''clock' a, zzzz"        | 12 o'clock PM, Pacific Daylight Time |
| "K:mm a, z"                    | 0:08 PM, PDT                         |
| "yyyyy.MMMMM.dd GGG hh:mm aaa" | 02001.July.04 AD 12:08 PM            |
| "EEE, d MMM yyyy HH:mm:ss Z"   | Wed, 4 Jul 2001 12:08:56 -0700       |
| "yyMMddHHmmssZ"                | 010704120856-0700                    |
| "yyyy-MM-dd'T'HH:mm:ss.SSSZ"   | 2001-07-04T12:08:56.235-0700         |

## Date and Time Pattern Letters in Alphabetic Order

The same pattern letters shown at first, above, in Date or Time Component order are shown
below in alphabetic order for easy reference.

| Pattern Letter | Date or Time Component | Presentation as text or number | Examples                              |
| -------------- | ---------------------- | ------------------------------ | ------------------------------------- |
| a              | Am/pm marker           | Text                           | PM                                    |
| D              | Day in year            | Number                         | 189                                   |
| d              | Day in month           | Number                         | 10                                    |
| E              | Day in week            | Text                           | EE=Tu; EEE=Tue; EEEE=Tuesday          |
| F              | Day of week in month   | Number                         | 2                                     |
| G              | Era designator         | Text                           | AD                                    |
| H              | Hour in day (0-23)     | Number                         | 0                                     |
| h              | Hour in am/pm (1-12)   | Number                         | 12                                    |
| k              | Hour in day (1-24)     | Number                         | 24                                    |
| K              | Hour in am/pm (0-11)   | Number                         | 0                                     |
| M              | Month in year          | Month                          | July; Jul; 07                         |
| m              | Minute in hour         | Number                         | 30                                    |
| s              | Second in minute       | Number                         | 55                                    |
| S              | Millisecond            | Number                         | 978                                   |
| w              | Week in year           | Number                         | 27                                    |
| W              | Week in month          | Number                         | 2                                     |
| y              | Year                   | Year                           | 1996; 96                              |
| z              | Time zone              | General                        | Pacific Standard Time; PST; GMT-08:00 |
| Z              | Time zone              | RFC                            | -0800                                 |
