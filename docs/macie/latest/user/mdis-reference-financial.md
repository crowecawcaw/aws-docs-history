# Managed data identifiers for financial

information

Amazon Macie can detect multiple types of sensitive financial information by using managed data
identifiers. The topics on this page list each type and provide information about the managed
data identifiers that are designed to detect the data. Each topic provides the following
information:

- Managed data identifier ID – Specifies the unique
  identifier (ID) for one or more managed data identifiers that are designed to detect the data.
  When you [create a sensitive data discovery job](discovery-jobs-create.md "discovery-jobs-create.md") or [configure settings for automated sensitive data discovery](discovery-asdd-account-configure.md "discovery-asdd-account-configure.md"), you can use these
  IDs to specify which managed data identifiers you want Macie to use when it analyzes
  data.
- Supported countries and regions – Indicates which
  countries and regions the applicable managed data identifiers are designed for. If the managed
  data identifiers aren't designed for particular countries or regions, this value is
  _Any_.
- Keyword required – Specifies whether detection
  requires a keyword to be in proximity of the data. If a keyword is required, the topic also
  provides examples of required keywords. For information about how Macie uses
  keywords when it analyzes data, see [Keyword requirements](managed-data-identifiers-keywords.md "managed-data-identifiers-keywords.md").
- Comments – Provides any relevant details that might
  affect your choice of managed data identifier or your investigation into reported occurrences of
  the sensitive data. The details include information such as supported standards, syntax
  requirements, and exceptions.
  The topics are listed in alphabetical order by sensitive data type.

###### Sensitive data types

- [Bank account number](#mdis-reference-BAN "#mdis-reference-BAN")
- [Basic Bank Account
  Number (BBAN)](#mdis-reference-BBAN "#mdis-reference-BBAN")
- [Credit card expiration
  date](#mdis-reference-CC-expiration "#mdis-reference-CC-expiration")
- [Credit card magnetic stripe
  data](#mdis-reference-CC-stripe "#mdis-reference-CC-stripe")
- [Credit card number](#mdis-reference-CC-number "#mdis-reference-CC-number")
- [Credit card verification
  code](#mdis-reference-CC-verification-code "#mdis-reference-CC-verification-code")
- [International Bank Account
  Number (IBAN)](#mdis-reference-IBAN "#mdis-reference-IBAN")

## Bank account number

Macie can detect Canadian and US bank account numbers that consist of 9–17 digit
sequences and don't contain any spaces.

**Managed data identifier ID:** BANK_ACCOUNT_NUMBER

**Supported countries and regions:** Canada, US

**Keyword required:** Yes. Keywords include: _bank
account, bank acct, checking account, checking acct, deposit account, deposit acct,
savings account, savings acct, chequing account, chequing acct_

**Comments:** This managed data identifier is explicitly designed to detect
bank account numbers for Canada and the US. These countries don’t use the Basic Bank Account
Number (BBAN) or International Bank Account Number (IBAN) formats defined by the ISO
international standard for numbering bank accounts, as specified by [ISO 13616](https://www.iso.org/standard/81090.html "https://www.iso.org/standard/81090.html"). To detect bank account
numbers for other countries and regions, use the managed data identifiers that are designed
for those formats. For more information, see [Basic Bank Account Number (BBAN)](#mdis-reference-BBAN "#mdis-reference-BBAN") and [International Bank Account Number (IBAN)](#mdis-reference-IBAN "#mdis-reference-IBAN").

## Basic Bank Account Number (BBAN)

Macie can detect Basic Bank Account Numbers (BBANs) that conform to the BBAN structure
defined by the ISO international standard for numbering bank accounts, as specified by [ISO 13616](https://www.iso.org/standard/81090.html "https://www.iso.org/standard/81090.html"). This includes BBANs that
don't contain spaces, or use space or hyphen separators—for example,
`NWBK60161331926819`, `NWBK 6016 1331 9268 19`, and
`NWBK-6016-1331-9268-19`.

**Managed data identifier ID:** Depending on country or region, FRANCE_BANK_ACCOUNT_NUMBER,
GERMANY_BANK_ACCOUNT_NUMBER, ITALY_BANK_ACCOUNT_NUMBER, SPAIN_BANK_ACCOUNT_NUMBER,
UK_BANK_ACCOUNT_NUMBER

**Supported countries and regions:** France, Germany, Italy, Spain, UK

**Keyword required:** Yes. The following table lists the keywords that Macie recognizes
for specific countries and regions.

| Country or region | Keywords                                                                                                                                                                                                                                                               |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| France            | account code, account number, accountno#, accountnumber#, bban,<br>code bancaire, compte bancaire, customer account id, customer account number,<br>customer bank account id, iban, numéro de compte                                                                   |
| Germany           | account code, account number, accountno#, accountnumber#,<br>bankleitzahl, bban, customer account id, customer account number, customer bank<br>account id, geheimzahl, iban, kartennummer, kontonummer, kreditkartennummer,<br>sepa                                   |
| Italy             | account code, account number, accountno#, accountnumber#, bban,<br>codice bancario, conto bancario, customer account id, customer account number,<br>customer bank account id, iban, numero di conto                                                                   |
| Spain             | account code, account number, accountno#, accountnumber#, bban,<br>código cuenta, código cuenta bancaria, cuenta cliente id, customer account ID,<br>customer account number, customer bank account id, iban, número cuenta bancaria<br>cliente, número cuenta cliente |
| UK                | account code, account number, accountno#, accountnumber#, bban,<br>customer account id, customer account number, customer bank account id, iban,<br>sepa                                                                                                               |

**Comments:** These managed data identifiers can also detect International
Bank Account Numbers (IBANs) that comply with the ISO 13616 standard. For more information,
see [International Bank Account Number (IBAN)](#mdis-reference-IBAN "#mdis-reference-IBAN"). The managed
data identifier for the UK (UK_BANK_ACCOUNT_NUMBER) can also detect domestic
bank account numbers for the UK—for example, `60-16-13 31926819`.

## Credit card expiration date

**Managed data identifier ID:** CREDIT_CARD_EXPIRATION

**Supported countries and regions:** Any

**Keyword required:** Yes. Keywords include: _exp d, exp
m, exp y, expiration, expiry_

**Comments:** Support includes most date formats, such as all digits and
combinations of digits and names of months. Date components can be separated by slashes (/),
hyphens (‐), or applicable keywords. For example, Macie can detect dates such as
`02/26`, `02/2026`, `Feb 2026`, `26-Feb`, and
`expY=2026, expM=02`.

## Credit card magnetic stripe data

**Managed data identifier ID:** CREDIT_CARD_MAGNETIC_STRIPE

**Supported countries and regions:** Any

**Keyword required:** Yes. Keywords include: _card data,
iso7813, mag, magstripe, stripe, swipe_

**Comments:** Support includes tracks 1 and 2.

## Credit card number

**Managed data identifier ID:** CREDIT_CARD_NUMBER for credit card numbers that are
in proximity of a keyword, CREDIT_CARD_NUMBER\_(NO_KEYWORD) for credit card
numbers that aren't in proximity of a keyword

**Supported countries and regions:** Any

**Keyword required:** Varies. Keywords are required by the
CREDIT_CARD_NUMBER managed data identifier. Keywords include: _account number, american express, amex, bank card, c card, card, cc
#, ccn, check card, cred card, credit, credit card, credit cards, credit no, credit
num, dankort, debit, debit card, debit no, debit num, diners club, discover, electron,
japanese card bureau, jcb, mastercard, mc, pan, payment account number, payment card
number, pcn, pmnt #, pmnt card, pmnt no, pmnt number, union pay,
visa_. Keywords aren't required by the
CREDIT_CARD_NUMBER\_(NO_KEYWORD) managed data identifier.

**Comments:** Detection requires the data to be a 13–19 digit
sequence that adheres to the Luhn check formula and uses a standard card number prefix for any
of the following types of credit cards: American Express, Dankort, Diner’s Club, Discover,
Electron, Japanese Card Bureau (JCB), Mastercard, UnionPay, and Visa.

Macie doesn't report occurrences of the following sequences, which credit card issuers
have reserved for public testing: `122000000000003`, `2222405343248877`,
`2222990905257051`, `2223007648726984`, `2223577120017656`,
`30569309025904`, `34343434343434`, `3528000700000000`,
`3530111333300000`, `3566002020360505`, `36148900647913`,
`36700102000000`, `371449635398431`, `378282246310005`,
`378734493671000`, `38520000023237`, `4012888888881881`,
`4111111111111111`, `4222222222222`, `4444333322221111`,
`4462030000000000`, `4484070000000000`, `4911830000000`,
`4917300800000000`, `4917610000000000`,
`4917610000000000003`, `5019717010103742`,
`5105105105105100`, `5111010030175156`, `5185540810000019`,
`5200828282828210`, `5204230080000017`, `5204740009900014`,
`5420923878724339`, `5454545454545454`, `5455330760000018`,
`5506900490000436`, `5506900490000444`, `5506900510000234`,
`5506920809243667`, `5506922400634930`, `5506927427317625`,
`5553042241984105`, `5555553753048194`, `5555555555554444`,
`5610591081018250`, `6011000990139424`, `6011000400000000`,
`6011111111111117`, `630490017740292441`,
`630495060000000000`, `6331101999990016`,
`6759649826438453`, `6799990100000000019`, and
`76009244561`.

## Credit card verification code

**Managed data identifier ID:** CREDIT_CARD_SECURITY_CODE

**Supported countries and regions:** Any

**Keyword required:** Yes. Keywords include: _card id,
card identification code, card identification number, card security code, card validation
code, card validation number, card verification data, card verification value, cvc, cvc2,
cvv, cvv2, elo verification code_

**Comments:** None

## International Bank Account Number (IBAN)

Macie can detect International Bank Account Numbers (IBANs) that consist of up to 34
alphanumeric characters, including elements such as country code. More specifically, Macie can
detect IBANs that comply with the ISO international standard for numbering bank accounts, as
specified by [ISO 13616](https://www.iso.org/standard/81090.html "https://www.iso.org/standard/81090.html"). This
includes IBANs that don't contain spaces, or use space or hyphen separators—for
example, `GB29NWBK60161331926819`, `GB29 NWBK 6016 1331 9268 19`, and
`GB29-NWBK-6016-1331-9268-19`. Detection includes validation checks based on the
Modulus 97 scheme.

**Managed data identifier ID:** Depending on country or region, ALBANIA_BANK_ACCOUNT_NUMBER,
ANDORRA_BANK_ACCOUNT_NUMBER, BOSNIA_AND_HERZEGOVINA_BANK_ACCOUNT_NUMBER,
BRAZIL_BANK_ACCOUNT_NUMBER, BULGARIA_BANK_ACCOUNT_NUMBER, COSTA_RICA_BANK_ACCOUNT_NUMBER,
CROATIA_BANK_ACCOUNT_NUMBER, CYPRUS_BANK_ACCOUNT_NUMBER, CZECH_REPUBLIC_BANK_ACCOUNT_NUMBER,
DENMARK_BANK_ACCOUNT_NUMBER, DOMINICAN_REPUBLIC_BANK_ACCOUNT_NUMBER,
EGYPT_BANK_ACCOUNT_NUMBER, ESTONIA_BANK_ACCOUNT_NUMBER, FAROE_ISLANDS_BANK_ACCOUNT_NUMBER,
FINLAND_BANK_ACCOUNT_NUMBER, FRANCE_BANK_ACCOUNT_NUMBER, GEORGIA_BANK_ACCOUNT_NUMBER,
GERMANY_BANK_ACCOUNT_NUMBER, GREECE_BANK_ACCOUNT_NUMBER, GREENLAND_BANK_ACCOUNT_NUMBER,
HUNGARY_BANK_ACCOUNT_NUMBER, ICELAND_BANK_ACCOUNT_NUMBER, IRELAND_BANK_ACCOUNT_NUMBER,
ITALY_BANK_ACCOUNT_NUMBER, JORDAN_BANK_ACCOUNT_NUMBER, KOSOVO_BANK_ACCOUNT_NUMBER,
LIECHTENSTEIN_BANK_ACCOUNT_NUMBER, LITHUANIA_BANK_ACCOUNT_NUMBER, MALTA_BANK_ACCOUNT_NUMBER,
MAURITANIA_BANK_ACCOUNT_NUMBER, MAURITIUS_BANK_ACCOUNT_NUMBER, MONACO_BANK_ACCOUNT_NUMBER,
MONTENEGRO_BANK_ACCOUNT_NUMBER, NETHERLANDS_BANK_ACCOUNT_NUMBER,
NORTH_MACEDONIA_BANK_ACCOUNT_NUMBER, POLAND_BANK_ACCOUNT_NUMBER,
PORTUGAL_BANK_ACCOUNT_NUMBER, SAN_MARINO_BANK_ACCOUNT_NUMBER, SENEGAL_BANK_ACCOUNT_NUMBER,
SERBIA_BANK_ACCOUNT_NUMBER, SLOVAKIA_BANK_ACCOUNT_NUMBER, SLOVENIA_BANK_ACCOUNT_NUMBER,
SPAIN_BANK_ACCOUNT_NUMBER, SWEDEN_BANK_ACCOUNT_NUMBER, SWITZERLAND_BANK_ACCOUNT_NUMBER,
TIMOR_LESTE_BANK_ACCOUNT_NUMBER, TUNISIA_BANK_ACCOUNT_NUMBER, TURKIYE_BANK_ACCOUNT_NUMBER,
UK_BANK_ACCOUNT_NUMBER, UKRAINE_BANK_ACCOUNT_NUMBER,
UNITED_ARAB_EMIRATES_BANK_ACCOUNT_NUMBER, VIRGIN_ISLANDS_BANK_ACCOUNT_NUMBER (for
the British Virgin Islands)

**Supported countries and regions:** Albania, Andorra, Bosnia-Herzegovina, Brazil, Bulgaria, Costa Rica,
Croatia, Cyprus, Czech Republic, Denmark, Dominican Republic, Egypt, Estonia, Faroe Islands,
Finland, France, Georgia, Germany, Greece, Greenland, Hungary, Iceland, Ireland, Italy,
Jordan, Kosovo, Liechtenstein, Lithuania, Malta, Mauritania, Mauritius, Monaco, Montenegro,
Netherlands, North Macedonia, Poland, Portugal, San Marino, Senegal, Serbia, Slovakia,
Slovenia, Spain, Sweden, Switzerland, Timor-Leste, Tunisia, Türkiye, UK, Ukraine, United Arab
Emirates, Virgin Islands (British)

**Keyword required:** No

**Comments:** The managed data identifiers for France, Germany, Italy,
Spain, and the UK can also detect Basic Bank Account Numbers (BBANs) that conform to the BBAN
structure defined by the ISO 13616 standard, if the character sequence is in proximity of a
keyword. For more information, see [Basic Bank Account Number (BBAN)](#mdis-reference-BBAN "#mdis-reference-BBAN").
