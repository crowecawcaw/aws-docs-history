# Standard profile definition in

the Amazon Connect Customer Profiles

The following table lists all the fields in the Customer Profiles standard
profile object.

| Standard profile field | Data type             | Description                                                                                            |
| ---------------------- | --------------------- | ------------------------------------------------------------------------------------------------------ | --------------- | --------- |
| ProfileId              | String                | The unique identifier of a customer profile.                                                           |
| AccountNumber          | String                | A unique account number that you have given to the<br>customer.                                        |
| AdditionalInformation  | String                | Any additional information relevant to the<br>customer's profile.                                      |
| PartyType              | String                | The type of profile used to describe the<br>customer.<br>Valid values: INDIVIDUAL                      | BUSINESS        | <br>OTHER |
| BusinessName           | String                | The name of the customer's business.                                                                   |
| FirstName              | String                | The customer's first name.                                                                             |
| MiddleName             | String                | The customer's middle name.                                                                            |
| LastName               | String                | The customer's last name.                                                                              |
| BirthDate              | String                | The customer's birth date.                                                                             |
| Gender                 | String                | The gender with which the customer<br>identifies.                                                      |
| PhoneNumber            | String                | The customer's phone number, which has not been<br>specified as a mobile, home, or business<br>number. |
| MobilePhoneNumber      | String                | The customer's mobile phone number.                                                                    |
| HomePhoneNumber        | String                | The customer's home phone number.                                                                      |
| BusinessPhoneNumber    | String                | The customer's business phone<br>number.                                                               |
| EmailAddress           | String                | The customer’s email address, which has not been<br>specified as a personal or business<br>address.    |
| PersonalEmailAddress   | String                | The customer’s personal email<br>address.                                                              |
| BusinessEmailAddress   | String                | The customer’s business email<br>address.                                                              |
| Address                | Address               | A generic address associated with the customer that<br>is not mailing, shipping, or billing.           |
| ShippingAddress        | Address               | The customer's shipping address.                                                                       |
| MailingAddress         | Address               | The customer's mailing address.                                                                        |
| BillingAddress         | Address               | The customer's billing address.                                                                        |
| Attributes             | String-to-string map  | Key-value pair of attributes of a customer<br>profile.                                                 |
| ProfileType            | String                | The type of the profile.<br>Valid values: PROFILE                                                      | ACCOUNT_PROFILE |
| EngagementPreferences  | EngagementPreferences | The customer or account’s engagement<br>preferences.                                                   |

The standard profile objects are indexed by the keys in the following
table.

| Standard index name | Standard profile field                                                     |
| ------------------- | -------------------------------------------------------------------------- |
| \_phone             | PhoneNumber, MobilePhoneNumber, HomePhoneNumber, or<br>BusinessPhoneNumber |
| \_email             | EmailAddress, PersonalEmailAddress, or<br>BusinessEmailAddress             |
| \_account           | AccountNumber                                                              |
| \_profileId         | ProfileId                                                                  |
| \_fullName          | "FirstName MiddleName LastName"                                            |

For example, you can use `_phone` as a key name with the [SearchProfiles API](../../../customerprofiles/latest/APIReference/API_SearchProfiles.md "../../../customerprofiles/latest/APIReference/API_SearchProfiles.md") to find a profile whose PhoneNumber,
MobilePhoneNumber, HomePhoneNumber, or BusinessPhoneNumber attribute matches
with the search value.

## Address data type

| Standard profile field | Data type | Description                                  |
| ---------------------- | --------- | -------------------------------------------- |
| Address1               | String    | The first line of a customer address.        |
| Address2               | String    | The second line of a customer address.       |
| Address3               | String    | The third line of a customer address.        |
| Address4               | String    | The fourth line of a customer address.       |
| City                   | String    | The city in which the customer lives.        |
| Country                | String    | The country in which the customer lives.     |
| County                 | String    | The county in which the customer lives.      |
| PostalCode             | String    | The postal code of the customer address.     |
| Province               | String    | The province in which the customer<br>lives. |
| State                  | String    | The state in which the customer lives.       |

## EngagementPreferences

data type

| Standard profile field | Data type                          | Description                                     |
| ---------------------- | ---------------------------------- | ----------------------------------------------- |
| Email                  | Array of ContactPreference objects | A list of email-related contact<br>preferences. |
| Phone                  | Array of ContactPreference objects | A list of phone-related contact<br>preferences. |

## ContactPreference data

type

| Standard profile field | Data type | Description                                                        |
| ---------------------- | --------- | ------------------------------------------------------------------ | ----------------- | ------------------- | ------------------- | ---------------- | -------------------- | -------------------- |
| KeyName                | String    | A searchable, unique identifier of a customer<br>profile.          |
| KeyValue               | String    | The key value used to look up profile based off<br>the keyName.    |
| ProfileId              | String    | The unique identifier of a customer<br>profile.                    |
| ContactType            | String    | The contact type used for engagement. Valid<br>Values: PhoneNumber | MobilePhoneNumber | <br>HomePhoneNumber | BusinessPhoneNumber | EmailAddress<br> | PersonalEmailAddress | BusinessEmailAddress |
