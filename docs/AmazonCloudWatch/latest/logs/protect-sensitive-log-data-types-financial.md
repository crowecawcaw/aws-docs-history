# Financial information

CloudWatch Logs data protection can find the following types of financial
information.

If you set a data protection policy, CloudWatch Logs scans for the data identifiers that
you specify no matter what geolocation the log group is located in. The
information in the **Countries and regions** column in this
table designates whether two-letter country codes must be appended to the
data identifier to detect the appropriate keywords for those countries and regions.

| Type of data                  | Data identifier ID       | Keyword required                                                                                                                                                                                                                                                                                                                                                                               | Countries and regions                                        | Notes                                                                                                                                                                                                                                                                                                                        |
| ----------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bank account number           | `BankAccountNumber`      | Yes. Different keywords apply to different countries. For details, see the<br>\*_Keywords for bank account numbers_<br>• table later in this<br>section.                                                                                                                                                                                                                                       | France, Germany, Italy, Spain, United Kingdom, United States | Includes International Bank Account Numbers (IBANs) that consist of up to 34 alphanumeric<br>characters, including elements such as country codes.                                                                                                                                                                           |
| Credit card expiration date   | `CreditCardExpiration`   | `exp d`, `exp m`,<br>`exp y`, `expiration`, `expiry`                                                                                                                                                                                                                                                                                                                                           | All                                                          |                                                                                                                                                                                                                                                                                                                              |
| Credit card number            | `CreditCardNumber`       | `account number`, `american express`,<br>`amex`, `bank card`, `card`,<br>`card number`, `card num`, `cc #`,<br>`ccn`, `check card`, `credit`,<br>`credit card#`, `dankort`, `debit`,<br>`debit card`, `diners club`, `discover`,<br>`electron`, `japanese card bureau`, `jcb`,<br>`mastercard`, `mc`, `pan`,<br>`payment account number`, `payment card number`, `pcn`,<br>`union pay`, `visa` | All                                                          | Detection requires the data to be a 13–19 digit sequence that adheres to the Luhn check<br>formula, and uses a standard card number prefix for any of<br>the following types of credit cards: American Express,<br>Dankort, Diner’s Club, Discover, Electron, Japanese Card<br>Bureau (JCB), Mastercard, UnionPay, and Visa. |
| Credit card verification code | `CreditCardSecurityCode` | `card id`, `card identification code`,<br>`card identification number`, `card security code`,<br>`card validation code`,<br>`card validation number`, `card verification data`,<br>`card verification value`,<br>`cvc`, `cvc2`, `cvv`,<br>`cvv2`, `elo verification code`                                                                                                                      | All                                                          |                                                                                                                                                                                                                                                                                                                              |

**Keywords for bank account numbers**

Use the following keywords to bank account numbers. This includes International Bank Account Numbers
(IBANs) that consist of up to 34 alphanumeric characters, including elements
such as country codes.

| Country        | Keywords                                                                                                                                                                                                                                                                                                 |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| France         | `account code`, `account number`, `accountno#`,<br>`accountnumber#`, `bban`, `code bancaire`,<br>`compte bancaire`, `customer account id`,<br>`customer account number`, `customer bank account id`,<br>`iban`, `numéro de compte`                                                                       |
| Germany        | `account code`, `account number`, `accountno#`,<br>`accountnumber#`, `bankleitzahl`, `bban`,<br>`customer account id`, `customer account number`,<br>`customer bank account id`, `geheimzahl`, `iban`,<br>`kartennummer`, `kontonummer`, `kreditkartennummer`,<br>`sepa`                                 |
| Italy          | `account code`, `account number`, `accountno#`,<br>`accountnumber#`, `bban`, `codice bancario`,<br>`conto bancario`, `customer account id`,<br>`customer account number`, `customer bank account id`, `iban`,<br>`numero di conto`                                                                       |
| Spain          | `account code`, `account number`, `accountno#`,<br>`accountnumber#`, `bban`, `código cuenta`,<br>`código cuenta bancaria`, `cuenta cliente id`,<br>`customer account ID`, `customer account number`,<br>`customer bank account id`, `iban`,<br>`número cuenta bancaria cliente`, `número cuenta cliente` |
| United Kingdom | `account code`, `account number`, `accountno#`,<br>`accountnumber#`, `bban`,<br>`customer account ID`, `customer account number`,<br>`customer bank account id`, `iban`,<br>`sepa`                                                                                                                       |
| United States  | `bank account`, `bank acct`, `checking account`,<br>`checking acct`, `deposit account`, `deposit acct`,<br>`savings account`, `savings acct`, `chequing account`,<br>`chequing acct`                                                                                                                     |

CloudWatch Logs doesn't report occurrences of the following sequences, which credit card issuers
have reserved for public testing.

```
122000000000003, 2222405343248877, 2222990905257051, 2223007648726984, 2223577120017656,
30569309025904, 34343434343434, 3528000700000000, 3530111333300000, 3566002020360505, 36148900647913,
36700102000000, 371449635398431, 378282246310005, 378734493671000, 38520000023237, 4012888888881881,
4111111111111111, 4222222222222, 4444333322221111, 4462030000000000, 4484070000000000, 4911830000000,
4917300800000000, 4917610000000000, 4917610000000000003, 5019717010103742, 5105105105105100,
5111010030175156, 5185540810000019, 5200828282828210, 5204230080000017, 5204740009900014, 5420923878724339,
5454545454545454, 5455330760000018, 5506900490000436, 5506900490000444, 5506900510000234, 5506920809243667,
5506922400634930, 5506927427317625, 5553042241984105, 5555553753048194, 5555555555554444, 5610591081018250,
6011000990139424, 6011000400000000, 6011111111111117, 630490017740292441, 630495060000000000,
6331101999990016, 6759649826438453, 6799990100000000019, and 76009244561.
```

## Data identifier ARNs for

financial data types

The following lists the Amazon Resource Names (ARNs) for the data identifiers that you
can add to your data protection policies.

| Financial data identifier ARNs                                       |
| -------------------------------------------------------------------- |
| `arn:aws:dataprotection::aws:data-identifier/BankAccountNumber-DE`   |
| `arn:aws:dataprotection::aws:data-identifier/BankAccountNumber-ES`   |
| `arn:aws:dataprotection::aws:data-identifier/BankAccountNumber-FR`   |
| `arn:aws:dataprotection::aws:data-identifier/BankAccountNumber-GB`   |
| `arn:aws:dataprotection::aws:data-identifier/BankAccountNumber-IT`   |
| `arn:aws:dataprotection::aws:data-identifier/BankAccountNumber-US`   |
| `arn:aws:dataprotection::aws:data-identifier/CreditCardExpiration`   |
| `arn:aws:dataprotection::aws:data-identifier/CreditCardNumber`       |
| `arn:aws:dataprotection::aws:data-identifier/CreditCardSecurityCode` |
