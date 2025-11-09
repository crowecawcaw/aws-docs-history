End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Built-in Slot

Types

Amazon Lex supports built-in slot types that define how data in the
slot is recognized and handled. You can create slots of these types
in your intents. This eliminates the need to create enumeration
values for commonly used slot data such as date, time, and location.
Built-in slot types do not have versions.

| Slot Type                                                                            | Short Description                                                                                        | Supported Locales                       |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| [AMAZON.Airport](built-in-slot-airport.md "built-in-slot-airport.md")                | Recognizes words that represent an<br>airport.                                                           | All locales                             |
| [AMAZON.AlphaNumeric](built-in-slot-alphanumeric.md "built-in-slot-alphanumeric.md") | Recognizes words made up of letters and<br>numbers.                                                      | All locales except Korean (ko-KR)       |
| [AMAZON.City](built-in-slot-city.md "built-in-slot-city.md")                         | Recognizes words that represent a city.                                                                  | All locales                             |
| [AMAZON.Country](built-in-slot-country.md "built-in-slot-country.md")                | Recognizes words that represent a<br>country.                                                            | All locales                             |
| [AMAZON.DATE](built-in-slot-date.md "built-in-slot-date.md")                         | Recognizes words that represent a date and<br>converts them to a standard format.                        | All locales                             |
| [AMAZON.DURATION](built-in-slot-duration.md "built-in-slot-duration.md")             | Recognizes words that represent duration and<br>converts them to a standard format.                      | All locales                             |
| [AMAZON.EmailAddress](built-in-slot-email.md "built-in-slot-email.md")               | Recognizes words that represent an email address<br>and converts them into a standard email<br>address.  | All locales                             |
| [AMAZON.FirstName](built-in-slot-first-name.md "built-in-slot-first-name.md")        | Recognizes words that represent a first<br>name.                                                         | All locales                             |
| [AMAZON.LastName](built-in-slot-last-name.md "built-in-slot-last-name.md")           | Recognizes words that represent a last<br>name.                                                          | All locales                             |
| [AMAZON.NUMBER](built-in-slot-number.md "built-in-slot-number.md")                   | Recognizes numeric words and converts them into<br>digits.                                               | All locales                             |
| [AMAZON.Percentage](built-in-slot-percent.md "built-in-slot-percent.md")             | Recognizes words that represent a percentage and<br>converts them to a number and a percent sign<br>(%). | All locales                             |
| [AMAZON.PhoneNumber](built-in-slot-phone.md "built-in-slot-phone.md")                | Recognizes words that represent a phone number<br>and converts them into a numeric string.               | All locales                             |
| [AMAZON.SpeedUnit](built-in-slot-speed.md "built-in-slot-speed.md")                  | Recognizes words that represent a speed unit and<br>converts them into a standard abbreviation.          | English (US) (en-US)                    |
| [AMAZON.State](built-in-slot-state.md "built-in-slot-state.md")                      | Recognizes words that represent a state.                                                                 | All locales                             |
| [AMAZON.StreetName](built-in-slot-street-name.md "built-in-slot-street-name.md")     | Recognizes words that represent a street<br>name.                                                        | All locales except English (US) (en-US) |
| [AMAZON.TIME](built-in-slot-time.md "built-in-slot-time.md")                         | Recognizes words that indicate times and converts<br>them into a time format.                            | All locales                             |
| [AMAZON.WeightUnit](built-in-slot-weight.md "built-in-slot-weight.md")               | Recognizes words that represent a weight unit and<br>converts them into a standard abbreviation          | English (US) (en-US)                    |

###### Note

For the English (US) (en-US) locale, Amazon Lex supports slot types
from the Alexa Skill Kit. For a list of available built-in slot
types, see the [Slot Type Reference](https://developer.amazon.com/docs/custom-skills/slot-type-reference.html "https://developer.amazon.com/docs/custom-skills/slot-type-reference.html") in the Alexa Skills Kit
documentation.

- Amazon Lex doesn't support the
  `AMAZON.LITERAL` or the
  `AMAZON.SearchQuery` built-in slot types.
