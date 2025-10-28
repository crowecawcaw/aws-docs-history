# Built-in slot types

Amazon Lex supports built-in slot types that define how data in the
slot is recognized and handled. You can create slots of these types
in your intents. This eliminates the need to create enumeration
values for commonly used slot data such as date, time, and location.
Built-in slot types do not have versions.

| Slot Type                                                                                | Short Description                                                                                                                   | Supported Locales              |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| [AMAZON.AlphaNumeric](built-in-slot-alphanumeric.md "built-in-slot-alphanumeric.md")     | Recognizes words made up of letters and numbers.                                                                                    |
| [AMAZON.City](built-in-slot-city.md "built-in-slot-city.md")                             | Recognizes words that represent a city.                                                                                             | All locales                    |
| [AMAZON.Confirmation](built-in-slot-confirmation.md "built-in-slot-confirmation.md")     | Recognizes words that mean 'Yes', 'No', 'Maybe', and 'Don't know' and converts them to a standard (Yes/No/Maybe/Don't know) format. | All locales                    |
| [AMAZON.Country](built-in-slot-country.md "built-in-slot-country.md")                    | Recognizes words that represent a country.                                                                                          | All locales                    |
| [AMAZON.Currency](built-in-slot-currency.md "built-in-slot-currency.md")                 | Recognizes words that represent a currency value and converts them into a standard currency abbreviation and value.                 | All locales                    |
| [AMAZON.Date](built-in-slot-date.md "built-in-slot-date.md")                             | Recognizes words that represent a date and converts them to a standard format.                                                      | All locales                    |
| [AMAZON.Duration](built-in-slot-duration.md "built-in-slot-duration.md")                 | Recognizes words that represent duration and converts them to a standard format.                                                    | All locales                    |
| [AMAZON.EmailAddress](built-in-slot-email.md "built-in-slot-email.md")                   | Recognizes words that represent an email address and converts them into a standard email address.                                   | All locales                    |
| [AMAZON.FirstName](built-in-slot-first-name.md "built-in-slot-first-name.md")            | Recognizes words that represent a first name.                                                                                       | All locales                    |
| [AMAZON.LastName](built-in-slot-last-name.md "built-in-slot-last-name.md")               | Recognizes words that represent a last name.                                                                                        | All locales                    |
| [AMAZON.Number](built-in-slot-number.md "built-in-slot-number.md")                       | Recognizes numeric words and converts them into digits.                                                                             | All locales                    |
| [AMAZON.Percentage](built-in-slot-percent.md "built-in-slot-percent.md")                 | Recognizes words that represent a percentage and converts them to a number and a percent sign (%).                                  | All locales                    |
| [AMAZON.PhoneNumber](built-in-slot-phone.md "built-in-slot-phone.md")                    | Recognizes words that represent a phone number and converts them into a numeric string.                                             | All locales                    |
| [AMAZON.State](built-in-slot-state.md "built-in-slot-state.md")                          | Recognizes words that represent a state.                                                                                            | All locales                    |
| [AMAZON.StreetName](built-in-slot-street-name.md "built-in-slot-street-name.md")         | Recognizes words that represent a street name.                                                                                      | All locales                    |
| [AMAZON.Time](built-in-slot-time.md "built-in-slot-time.md")                             | Recognizes words that indicate times and converts them into a time format.                                                          | All locales                    |
| [AMAZON.UKPostalCode](built-in-slot-uk-postal-code.md "built-in-slot-uk-postal-code.md") | Recognizes words that represent a UK post code and converts them to a standard form.                                                | English (British) (en-GB) only |
| [AMAZON.FreeFormInput](built-in-slot-free-form.md "built-in-slot-free-form.md")          | Recognizes strings that consist of any words or characters.                                                                         | All locales                    |
