# Customizing date formats

in Quick

In Quick, you can customize how dates are formatted in
your filter and parameter controls. For example, you can specify to
format the date in a control as 20-09-2021, or, if you'd rather, as
09-20-2021. You can also specify to shorten the month in your dates
(such as September) to three letters (Sep), among other
customizations.

Following is a list of tokens you can use to create custom date
formats. You can use them in combination with one another to control how
dates appear in your controls.

## List of supported

tokens for formatting dates

Use the following tokens to customize the format of dates in
Quick.

| Example           | Description                                                                               | Token  |
| ----------------- | ----------------------------------------------------------------------------------------- | ------ |
| 0–6               | Numeric representation of a particular day of<br>the week. 0 is Sunday and 6 is Saturday. | `d`    |
| Mo–Su             | A 2-character textual representation of a<br>particular day of the week.                  | `dd`   |
| Mon–Sun           | A 3-character textual representation of a<br>particular day of the week.                  | `ddd`  |
| Monday–Sunday     | A textual representation of a particular day<br>of the week.                              | `dddd` |
| 99 or 21          | A 2-digit representation of a year.                                                       | `YY`   |
| 1999 or 2021      | A full, 4-digit numeric representation of a<br>year.                                      | `YYYY` |
| 1–12              | Number of a month, without leading<br>zeros.                                              | `M`    |
| 1st, 2nd, to 12th | Number of a month without leading zeros and<br>with an ordinal suffix.                    | `Mo`   |
| 01–12             | Number of a month with leading zeros.                                                     | `MM`   |
| Jan–Dec           | A 3-digit textual representation of a<br>month.                                           | `MMM`  |
| January–December  | A full textual representation of a<br>month.                                              | `MMMM` |
| 1–4               | A numeric representation of a quarter.                                                    | `Q`    |
| 1st–4th           | A numeric representation of a quarter with an<br>ordinal suffix.                          | `Qo`   |
| 1–31              | Day of the month without leading zeros.                                                   | `D`    |
| 1st, 2nd, to 31st | Day of the month without leading zeros and an<br>ordinal suffix.                          | `Do`   |
| 01–31             | A 2-digit day of the month with leading<br>zeros.                                         | `DD`   |
| 1–365             | Day of the year without leading zeros.                                                    | `DDD`  |
| 001–365           | Day of the year with leading zeros.                                                       | `DDDD` |
| 1–53              | Week of the year without leading zeros.                                                   | `w`    |
| 1st–53rd          | The week of the year without leading zeros and<br>with an ordinal suffix.                 | `wo`   |
| 01–53rd           | Week of the year with leading zeros.                                                      | `ww`   |
| 1–23              | Hours, in 24-hour format, without leading<br>zeros.                                       | `H`    |
| 01–23             | Hours, in 24-hour format, with leading<br>zeros.                                          | `HH`   |
| 1–12              | Hours, in 12-hour format, without leading<br>zeros.                                       | `h`    |
| 01–12             | Hours, in 12-hour format, with leading<br>zeros.                                          | `hh`   |
| 0–59              | Minutes without leading zeros.                                                            | `m`    |
| 00–59             | Minutes with leading zeros.                                                               | `mm`   |
| 0–59              | Seconds without leading zeros.                                                            | `s`    |
| 00–59             | Seconds with leading zeros.                                                               | `ss`   |
| am or pm          | am/pm                                                                                     | `a`    |
| AM or PM          | AM/PM                                                                                     | `A`    |
| 1632184215        | Unix timestamp.                                                                           | `X`    |
| 1632184215000     | Millisecond Unix timestamp.                                                               | `x`    |
| Z                 | Zero UTC offset.                                                                          | `Z`    |

The following date types are not supported.

- Time zones offset with a colon. For example,
  +07:00.
- Time zones offset without a colon. For example,
  +0730.

### Preset date

formats

To quickly customize dates and times to appear as one of the
following example formats, you can use the following
Quick preset tokens.

| Example                          | Token  |
| -------------------------------- | ------ |
| 8:30 PM                          | `LT`   |
| 8:30:25 PM                       | `LTS`  |
| August 2 1985                    | `LL`   |
| Aug 2 1985                       | `ll`   |
| August 2 1985 08:30 PM           | `LLL`  |
| Aug 2 1985 08:30 PM              | `lll`  |
| Thursday, August 2 1985 08:30 PM | `LLLL` |
| Thu, Aug 2 1985 08:30 PM         | `llll` |

## Common date

formats

Following are three common date examples and their associated
token formats for your quick reference.

| Example                             | Token Format                      |
| ----------------------------------- | --------------------------------- |
| Sep 20, 2021                        | `MMM DD, YYYY`                    |
| 20-09-21 5pm                        | `DD-MM-YY ha`                     |
| Monday, September 20, 2021 17:30:15 | `dddd, MMMM DD, YYYY<br>HH:mm:ss` |

## Adding words to

dates

To include words in your date formats, such as the word "of" in
_20th of Sep, 2021_, enter backslashes (\)
before each character in the word. For example, for the 20th of Sep,
2021 date example, use the following token format: `Do \o\f
 MMM, YYYY`.

## Example:

Customizing the date format in a filter control

Use the following procedure to learn how to use date token formats
to customize dates for a filter control.

###### To learn to customize dates for a filter control with data

tokens

1. In a Quick analysis, choose the filter control
   that you want to customize.
2. On the filter control, choose the **Edit
   control** icon.
3. On the **Edit control** page that opens,
   for **Date format**, enter the custom date
   format that you want. Use the tokens listed previously in
   this topic.

For example, let's say that you want to customize your
dates using the following format: _Sep 3rd, 2020 at
5pm_. To do so, you can enter the following
token format:

`MMM Do, YYYY \a\t ha`

A preview of the date format appears below the input field
as you enter each token. 4. Choose **Apply**.

The dates in the control update to the format you
specified.
