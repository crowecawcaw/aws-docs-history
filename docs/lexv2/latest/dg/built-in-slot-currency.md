# AMAZON.Currency

Converts words that represent a currency into a standard ISO
4217 alphabetic currency code and a number. Amazon Lex V2 recognizes
currencies but does not convert from one currency to
another.

For more information, see [Currency codes - ISO 4217](https://www.iso.org/iso-4217-currency-codes.html "https://www.iso.org/iso-4217-currency-codes.html") on the International
Organization for Standardization (ISO) website.

The currency represented is structured as follows: `{Unit} {Amount}`

- {Unit} refers to the specific currency unit (for example, USD).
- {Amount} denotes the monetary value, formatted to two decimal places (for example, 300.00).
  Examples (all examples below are using the en-US locale; different locales
  may yield different results):

- "3USD": USD 3.00
- "USD300": USD 300.00
- "3 dimes" : USD 0.30
- "$1.56": USD 1.56
- "5c": USD 0.05
- "1 dollar": USD 1.00
- "five fifteen": USD 515.00
- “five dollars fifteen cents”: USD 5.15
- "5 usd and 1/2": USD 5.50
