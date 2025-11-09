# Customer Profiles standard

loyalty object fields

The following table lists all the fields in the Customer Profiles standard
loyalty object.

| Loyalty               | Standard loyalty field | Type                                                     | Description |
| --------------------- | ---------------------- | -------------------------------------------------------- | ----------- |
| LoyaltyId             | String                 | Unique identifier of the standard loyalty                |
| ProgramId             | String                 | Identifier for the loyalty program                       |
| MembershipId          | String                 | Alternate identifier within the program                  |
| ProgramName           | String                 | Name of the loyalty program                              |
| Group                 | String                 | Group or category of the loyalty program                 |
| Channel               | String                 | Channel through which the loyalty program is<br>accessed |
| CreatedDate           | String                 | Date the loyalty account was created                     |
| EnrollmentDate        | String                 | Date the customer enrolled in the program                |
| CreatedBy             | String                 | User or system that created the loyalty account          |
| UpdatedDate           | String                 | Date the loyalty account was last updated                |
| LastUpdatedBy         | String                 | User or system that last updated the loyalty<br>account  |
| UpgradeDate           | String                 | Date when the tier was last upgraded                     |
| RenewalDate           | String                 | Date of loyalty membership renewal                       |
| AdditionalInformation | String                 | Any additional information                               |
| EmailAddress          | String                 | Customer's email address                                 |
| EmailAddressVerified  | String                 | Flag indicating if email is verified                     |
| PhoneNumber           | String                 | Customer's phone number                                  |
| PhoneNumberVerified   | String                 | Flag indicating if phone number is verified              |
| Status                | String                 | Current status of the loyalty account                    |
| Tier                  | Tier                   | Tier details                                             |
| Points                | Points                 | Points details                                           |
| PointExpirations      | PointExpiration List   | Point expiration details                                 |
| Payment               | Payment                | Payment details                                          |
| PaymentInformation    | PaymentInformation     | Payment Information details                              |
| BillingAddress        | Loyalty Address        | Address details                                          |
| Attributes            | Map<String, String>    | Additional attributes not otherwise covered              |

| Standard Index Fields | Standard index name | Standard preference record field |
| --------------------- | ------------------- | -------------------------------- |
| \_loyaltyId           | LoyaltyId           |
| \_loyaltyMembershipId | membershipId        |

| Loyalty Address data type | Standard airPreference field | Data type                                 | Description |
| ------------------------- | ---------------------------- | ----------------------------------------- | ----------- |
| Address1                  | String                       | The first line of a customer address.     |
| Address2                  | String                       | The second line of a customer address.    |
| Address3                  | String                       | The third line of a customer address.     |
| Address4                  | String                       | The fourth line of a customer address.    |
| City                      | String                       | The city in which the customer lives.     |
| Country                   | String                       | The country in which the customer lives.  |
| County                    | String                       | The county in which the customer lives.   |
| PostalCode                | String                       | The postal code of the customer address.  |
| Province                  | String                       | The province in which the customer lives. |
| State                     | String                       | The state in which the customer lives.    |

| Tier data type   | Standard loyalty field | Type                                 | Description |
| ---------------- | ---------------------- | ------------------------------------ | ----------- |
| CurrentTier      | String                 | Customer's current loyalty tier      |
| NextTier         | String                 | Next possible tier for the customer  |
| PointsToNextTier | String                 | Points needed to reach the next tier |

| Points data type | Standard loyalty field | Type                           | Description |
| ---------------- | ---------------------- | ------------------------------ | ----------- |
| Points.Unit      | String                 | Unit of measurement for points |
| Points.Lifetime  | String                 | Total lifetime points earned   |
| Points.Balance   | String                 | Current points balance         |
| Points.Redeemed  | String                 | Total points redeemed          |

| PointExpiration data type | Standard loyalty field | Type                       | Description |
| ------------------------- | ---------------------- | -------------------------- | ----------- |
| Points                    | String                 | Points expiring            |
| Date                      | String                 | Expiration date for points |

| Payment data type    | Standard loyalty field | Type                               | Description |
| -------------------- | ---------------------- | ---------------------------------- | ----------- |
| Type                 | String                 | Type of payment                    |
| CreditCardToken      | String                 | Tokenized credit card reference    |
| CreditCardType       | String                 | Type of credit card (e.g., Visa)   |
| CreditCardExpiration | String                 | Expiration date of the credit card |
| Cvv                  | String                 | Card verification value            |
| NameOnCreditCard     | String                 | Name on the card                   |
| RoutingNumber        | String                 | Bank routing number                |
| AccountNumber        | String                 | Bank account number                |
| VoucherId            | String                 | Voucher identifier                 |

| PaymentInformation data type | Standard loyalty field | Type                      | Description |
| ---------------------------- | ---------------------- | ------------------------- | ----------- |
| Schedule                     | String                 | Schedule of payments      |
| LastPaymentDate              | String                 | Date of last payment      |
| NextPaymentDate              | String                 | Date of next payment      |
| NextBillAmount               | String                 | Amount for the next bill  |
| CurrencyCode                 | String                 | Currency code (e.g., USD) |
| CurrencyName                 | String                 | Full name of the currency |
| CurrencySymbol               | String                 | Currency symbol (e.g., $) |
