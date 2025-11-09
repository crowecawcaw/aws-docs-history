Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Variables

Variables represent data elements that you want to use in a fraud
prediction. These variables can be taken from the event dataset that you prepared for training your model, from your Amazon Fraud Detector model's risk score outputs, or from Amazon SageMaker AI models.
For more information about variables taken from the event dataset, see [Get event dataset requirements using the Data models explorer](create-event-dataset.md#prepare-event-dataset "create-event-dataset.md#prepare-event-dataset").

The variables you want to use in your fraud prediction must first be created and then added to the event when creating your event type. Each variable you create must
be assigned a datatype, a default value, and optionally a variable type. Amazon Fraud Detector enriches some of the variables that you provide such as
IP addresses, bank identification numbers (BINs), and phone numbers, to create additional inputs and boost performance for the models that use these variables.

## Data types

Variables must have a data type for the data element that the variable represents and can optionally be assigned one of the predefined [Variable types](#variable-types "#variable-types").
For variables that are assigned to a variable type, the data type is pre-selected. Possible data types
include the following types :

| Data type | Description                                                      | Default value | Example values       |
| --------- | ---------------------------------------------------------------- | ------------- | -------------------- |
| String    | Any combination of<br>letters, whole numbers, or both            | <empty>       | abc, 123, 1D3B       |
| Integer   | Positive or negative whole numbers                               | 0             | 1, -1                |
| Boolean   | True or False                                                    | False         | True, False          |
| DateTime  | Date and time specified in the ISO 8601 standard UTC format only | <empty>       | 2019-11-30T13:01:01Z |
| Float     | Numbers with decimal points                                      | 0.0           | 4.01, 0.10           |

## Default value

Variables must have a default value. When Amazon Fraud Detector generates fraud predictions, this default value is used to run a rule or model if Amazon Fraud Detector doesn't
receive a value for a variable. Default values you provide must match the selected data type. In the
AWS Console, Amazon Fraud Detector assigns the default value of `0` for integers, `false` for Booleans,
`0.0` for floats, and (empty) for strings. You can set a custom default value for any of these data types.

## Variable types

When you create a variable, you can optionally assign the variable to a variable type. Variable type represents
the common data elements that are used to train models and to generate fraud predictions. Only variables with an associated
variable type can be used for model training. As part of the model training process, Amazon Fraud Detector uses the variable type associated
with the variable to perform variable enrichments, feature engineering, and risk scoring.

Amazon Fraud Detector has pre-defined the following variable types that can be used to assign to your variables.

| Category              | Variable type                                                                                       | Description                                            | Data type                                                                                                                                                                        | Example                                                                                                                                                                     |
| --------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Session               | IP_ADDRESS                                                                                          | The IP address that's collected during the event       | String                                                                                                                                                                           | 192.0.2.0<br>\*_Note:_<br>• Amazon Fraud Detector enriches this data. For more information, see [Geolocation enrichment](#geolocation-enrichment "#geolocation-enrichment") |
| USERAGENT             | The user agent that's collected during the event                                                    | String                                                 | Mozilla 5.0 (Windows NT 10.0, Win64, x64,rv:68.0) Gecko 20100101                                                                                                                 |
| FINGERPRINT           | The unique identifier for a device used for the event                                               | String                                                 | sadfow987u234                                                                                                                                                                    |
| SESSION_ID            | The session ID for the event's active session                                                       | String                                                 | sid123456789                                                                                                                                                                     |
| ARE_CREDENTIALS_VALID | Indicates if the credentials used for event login are valid                                         | Boolean                                                | True                                                                                                                                                                             |
| User                  | EMAIL_ADDRESS                                                                                       | The email<br>address that's collected during the event | String                                                                                                                                                                           | abc@domain.com                                                                                                                                                              |
| PHONE_NUMBER          | The phone number collected during the event                                                         | String                                                 | +1 555-0100<br>\*_Note:_<br>• Amazon Fraud Detector enriches this data. For more information, see [Phone number enrichment](#phone-number-enrichment "#phone-number-enrichment") |
| Billing               | BILLING_NAME                                                                                        | The name that's associated with the billing address    | String                                                                                                                                                                           | John Doe                                                                                                                                                                    |
| BILLING_PHONE         | The phone number that's associated with the billing address                                         | String                                                 | +1 555-0100<br>\*_Note:_<br>• Amazon Fraud Detector enriches this data. For more information, see [Phone number enrichment](#phone-number-enrichment "#phone-number-enrichment") |
| BILLING_ADDRESS_L1    | The first line of the billing address                                                               | String                                                 | Any street                                                                                                                                                                       |
| BILLING_ADDRESS_L2    | The second line of the billing address                                                              | String                                                 | Any unit 123                                                                                                                                                                     |
| BILLING_CITY          | The city that's in the billing address                                                              | String                                                 | Any City                                                                                                                                                                         |
| BILLING_STATE         | The state or province that's in the billing address                                                 | String                                                 | Any state or province                                                                                                                                                            |
| BILLING_COUNTRY       | The country that's in the billing address                                                           | String                                                 | Any country<br>\*_Note:_<br>• Amazon Fraud Detector enriches this data. For more information, see [Geolocation enrichment](#geolocation-enrichment "#geolocation-enrichment")    |
| BILLING_ZIP           | The postal code that's in the billing address                                                       | String                                                 | 01234<br>\*_Note:_<br>• Amazon Fraud Detector enriches this data. For more information, see [Geolocation enrichment](#geolocation-enrichment "#geolocation-enrichment")          |
| Shipping              | SHIPPING_NAME                                                                                       | The name that's associated with the shipping address   | String                                                                                                                                                                           | John Doe                                                                                                                                                                    |
| SHIPPING_PHONE        | The phone number that's associated with the shipping address                                        | String                                                 | +1 555-0100<br>\*_Note:_<br>• Amazon Fraud Detector enriches this data. For more information, see [Phone number enrichment](#phone-number-enrichment "#phone-number-enrichment") |
| SHIPPING_ADDRESS_L1   | The first line of the shipping address                                                              | String                                                 | 123 Any Street                                                                                                                                                                   |
| SHIPPING_ADDRESS_L2   | The second line of the shipping address                                                             | String                                                 | Unit 123                                                                                                                                                                         |
| SHIPPING_CITY         | The city that's in the shipping address                                                             | String                                                 | Any City                                                                                                                                                                         |
| SHIPPING_STATE        | The state or province that's in the shipping<br>address                                             | String                                                 | Any State                                                                                                                                                                        |
| SHIPPING_COUNTRY      | The country that's in that's in the shipping address                                                | String                                                 | Any Country<br>\*_Note:_<br>• Amazon Fraud Detector enriches this data. For more information, see [Geolocation enrichment](#geolocation-enrichment "#geolocation-enrichment")    |
| SHIPPING_ZIP          | The postal code that's in the shipping address                                                      | String                                                 | 01234<br>\*_Note:_<br>• Amazon Fraud Detector enriches this data. For more information, see [Geolocation enrichment](#geolocation-enrichment "#geolocation-enrichment")          |
| Payment               | ORDER_ID                                                                                            | The unique identifier for the transaction              | String                                                                                                                                                                           | LUX60                                                                                                                                                                       |
| PRICE                 | The total order price                                                                               | String                                                 | 560.00                                                                                                                                                                           |
| CURRENCY_CODE         | The ISO 4217 currency code                                                                          | String                                                 | USD                                                                                                                                                                              |
| PAYMENT_TYPE          | The payment method that's used for payment during the event                                         | String                                                 | Credit card                                                                                                                                                                      |
| AUTH_CODE             | The alphanumerical code that's sent by a credit card issuer or issuing bank                         | String                                                 | 0000                                                                                                                                                                             |
| AVS                   | The address verification system (AVS) response code from the card processor                         | String                                                 | Y                                                                                                                                                                                |
| Product               | PRODUCT_CATEGORY                                                                                    | The product category of order item                     | String                                                                                                                                                                           | Kitchen                                                                                                                                                                     |
| Custom                | NUMERIC                                                                                             | Any variable that can be represented as a real number  | Float                                                                                                                                                                            | 1.224                                                                                                                                                                       |
| CATEGORICAL           | Any variable that describes categories, segments, or<br>groups                                      | String                                                 | Large                                                                                                                                                                            |
| FREE_FORM_TEXT        | Any free form text that's captured as part of the event (for example, a customer review or comment) | String                                                 | Example of a free form text input                                                                                                                                                |

### Assigning variable to a variable type

If you are planning to use a variable for training your model, it is important that you choose a right variable type to assign
to the variable. Incorrect variable type assignment can negatively impact your model performance. It can also become very difficult
for you change the assignment later, especially if multiple models and events have used the variable.

You can assign your variable any one of the pre-defined variable types or one of the custom variable types – `FREE_FORM_TEXT`,
`CATEGORICAL`, or `NUMERIC`.

**Important notes for assigning variables to the right variable types**

1. If the variable matches one of predefined variable types, use it.
   Make sure the variable type corresponds to the variable. For example, if you assign an _ip_address_ variable to `EMAIL_ADDRESS`
   variable type, the ip_address variable will not get enriched with enrichments such as ASN, ISP, geo-location, and risk score.
   For more information, see [Variable enrichments](#variable-enrichments "#variable-enrichments").
2. If the variable doesn’t match any of predefined variable types, follow the recommendations listed below to assign one of the custom variable types.
3. Assign `CATEGORICAL` variable type to variables that typically do not have natural ordering and can be put into categories, segments, or groups.
   The dataset you are using to train your model might have ID variables such as, _merchant_id_, _campaign_id_, or _policy_id_.
   These variables represent groups (for example, all customers with same policy_id represent a group). Variables that have the following data must be assigned
   CATEGORICAL variable type -
   - Variables that contain data such as _customer_ID_, _segment_ID_, _color_ID_, _department_code_, or _product_ID_.
   - Variables that contain Boolean data with true, false, or null values.
   - Variables that can be put into groups or categories such as company name, product category, card type, or referral medium.

###### Note

`ENTITY_ID` is a reserved variable type used by Amazon Fraud Detector to assign to ENTITY_ID variable. The ENTITY_ID variable is
the ID of the entity initiating the action you want to evaluate. If you are creating a Transaction Fraud Insight (TFI) model type,
you are required to provide ENTITY_ID variable. You will need to decide which variable in your data uniquely identifies the entity
initiating the action and pass it on as ENTITY_ID variable. Assign CATEGORICAL variable type to all the other IDs in your dataset,
if they are present and if you are using them for model training. Examples of other IDs that are not an entity in your dataset can be
_merchant_ID_, _policy_ID_, and _campaign_ID_. 4. Assign `FREE_FORM_TEXT` variable type to variables that contain a block of text. Examples of FREE_FORM_TEXT variable types are –
_user reviews_, _comments_, _dates_, and _referral codes_. The
FREE_FORM_TEXT data contains multiple tokens separated by a delimiter. The delimiters can be any character other than alpha-numeric and underscore
symbol. For example, user reviews and comments can be separated by “space” delimiter, dates and referral codes can use hyphens as delimiters to
separate out prefix, suffix, and intermediate parts. Amazon Fraud Detector uses the delimiters to extract data from FREE_FORM_TEXT variables. 5. Assign _NUMERIC_ variable type to variables that are real numbers and have inherent ordering. Examples of NUMERIC variables
include _day_of_the_week_, _incident_severity_, _customer_rating_. Although, you can
assign CATEGORICAL variable type to these variables, we strongly recommend to assign all real number variables with inherent order to NUMERIC
variable type.

## Variable enrichments

Amazon Fraud Detector enriches some of the raw data elements that you provide such as IP addresses, bank identification numbers (BINs), and phone numbers, to create
additional inputs and boost performance for the models that use these data elements. The enrichment helps identify potentially suspicious situations and help the models
to capture more fraud.

### Phone number enrichment

Amazon Fraud Detector enriches phone number data with additional information
that relates to geolocation, the original carrier, and the validity
of the phone number. Phone number enrichment is automatically enabled for all
the models that are trained on or after _December 13, 2021_
and have a phone number that includes a country code (+xxx). If you have included phone
number variable in your model and have trained it before _December 13,
2021_, retrain your model so it can take advantage of this enrichment.

We highly recommend that you use the following format for phone number variables to ensure that your data is enriched successfully.

| Variable                         | Format                                                                                          | Description                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| PHONE_NUMBER                     | The [E.164](https://en.wikipedia.org/wiki/E.164 "https://en.wikipedia.org/wiki/E.164") standard | Make sure to include country code (+xxx) with the phone number. |
| BILLING_PHONE and SHIPPING_PHONE | The [E.164](https://en.wikipedia.org/wiki/E.164 "https://en.wikipedia.org/wiki/E.164") standard | Make sure to include country code (+xxx) with the phone number. |

### Geolocation enrichment

Starting on _February 8, 2022_ Amazon Fraud Detector
calculates the physical distance between the IP_ADDRESS, BILLING_ZIP, and SHIPPING_ZIP
values that you provide for an event. The calculated distances are
used as inputs to your fraud detection model.

To enable geolocation enrichment, your event data must include at least two of
the three variables: IP_ADDRESS, BILLING_ZIP, or SHIPPING_ZIP. In addition, each BILLING_ZIP and
SHIPPING_ZIP value must have a valid BILLING_COUNTRY code and SHIPPING_COUNTRY
code respectively. If you have a model that was trained before _February 8, 2022_ and it
includes these variables, you must retrain the model to enable the geolocation
enrichment.

If Amazon Fraud Detector can't determine the location that's associated with the IP_ADDRESS, BILLING_ZIP ,or SHIPPING_ZIP values for an event due to the data
being not valid, a special placeholder value is used instead. For example, suppose that an event has valid IP_ADDRESS and BILLING_ZIP values, but SHIPPING_ZIP
value isn't valid. In this case, enrichment is done only for IP_ADDRESS–> BILLING_ZIP. The enrichment isn't
done for IP_ADDRESS–>SHIPPING_ZIP and BILLING_ZIP–>SHIPPING_ZIP . Instead, the placeholder values
are used in their place. No matter if geolocation enrichment is enabled for your model or not, the performance of your model doesn't
change.

You can opt out of geolocation enrichment by mapping your BILLING_ZIP and
SHIPPING_ZIP variables to the CUSTOM_CATEGORICAL variable type. Changing the
variable type doesn't affect your model's performance.

**Geolocation variable format**

We highly recommend that you use the following format for geolocation
variables to ensure that your location data is enriched successfully.

| Variable                             | Format                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                           |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IP_ADDRESS                           | [IPv4](https://en.wikipedia.org/wiki/IP_address#IPv4_addresses "https://en.wikipedia.org/wiki/IP_address#IPv4_addresses") address                                      | For example<br>• 1.1.1.1                                                                                                                                                                                                                                                                              |
| BILLING_ZIP and SHIPPING_ZIP         | The [ISO<br>3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 "https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2") postal code for the specified country | For more information, see the **Country and territory codes**<br>section in this topic.                                                                                                                                                                                                               |
| BILLING_COUNTRY and SHIPPING_COUNTRY | The [ISO<br>3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 "https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2") two-letter standard country code      | For more information, see the \*_Country and territory codes_<br>• section in this topic. Amazon Fraud Detector<br>tries to match all the common variations of a country's name to their ISO 3166-1 two-letter standard country code. However,<br>we cannot guarantee they will be matched correctly. |

The following table provides a complete list of the
countries and territories
that are supported by Amazon Fraud Detector for geolocation enrichment. Each country and territory has an assigned
country code (specifically, the ISO 3166-1 alpha-2 two-letter country code) and a postal code.

**Postal code format**

- 9 - number
- a - letter
- [x] - X is optional. For example, Guersney "GY9[9] 9aa" means both "GY9 9aa" and "GY99 9aa" are valid. Use one format.
- [X/XX] - either X or XX can be used. For example, Bermuda "aa[aa/99]" means both "aa aa" and
  "aa 99" are valid. Use either one of these formats, but _do not_ use both.
- Some countries have fixed prefix. For example, the postal code for Andorra is AD999. This
  means the country code must start with letters _AD_ followed by three numbers.

| Code | Name                           | Postal code             |
| ---- | ------------------------------ | ----------------------- |
| AD   | Andorra                        | AD999                   |
| AR   | Netherlands Antilles           | 9999                    |
| AT   | Austria                        | 9999                    |
| AU   | Australia                      | 9999                    |
| AZ   | Azerbaijan                     | AZ 9999                 |
| BD   | Bangladesh                     | 9999                    |
| BE   | Belgium                        | 9999                    |
| BG   | Bulgaria                       | 9999                    |
| BM   | Bermuda                        | aa[aa/99]               |
| BY   | Belarus                        | 999999                  |
| CA   | Canada                         | a9a 9a9                 |
| CH   | Switzerland                    | 9999                    |
| CL   | Chile                          | 9999999                 |
| CO   | Colombia                       | 999999                  |
| CR   | Costa Rica                     | 99999                   |
| CY   | Cyprus                         | 9999                    |
| CZ   | Czechia                        | 999 99                  |
| DE   | Germany                        | 99999                   |
| DK   | Denmark                        | 9999                    |
| DO   | Dominican Republic             | 99999                   |
| DZ   | Algeria                        | 99999                   |
| EE   | Estonia                        | 99999                   |
| ES   | Spain                          | 99999                   |
| FI   | Finland                        | 99999                   |
| FM   | Federated States of Micronesia | 99999                   |
| FO   | Faroe Islands                  | 999                     |
| FR   | France                         | 99999                   |
| GB   | United Kingdom                 | a[a]9[a/9] 9aa          |
| GG   | Guernsey                       | GY9[9] 9aa              |
| GL   | Greenland                      | 9999                    |
| GP   | Guadeloupe                     | 99999                   |
| GT   | Guatemala                      | 99999                   |
| GU   | Guam                           | 99999                   |
| HR   | Croatia                        | 99999                   |
| HU   | Hungary                        | 9999                    |
| IE   | Ireland                        | a99[a/9][a/9][a/9][a/9] |
| IM   | Isle of Man                    | IM9[9]9aa               |
| IN   | India                          | 999999                  |
| IS   | Iceland                        | 999                     |
| IT   | Italy                          | 99999                   |
| JE   | Jersey                         | JE9[9]9aa               |
| JP   | Japan                          | 999-9999                |
| KR   | Republic of Korea              | 99999                   |
| LI   | Liechtenstein                  | 9999                    |
| LK   | Sri Lanka                      | 99999                   |
| LT   | Lithuania                      | 99999                   |
| LU   | Luxembourg                     | L-9999                  |
| LV   | Latvia                         | LV-9999                 |
| MC   | Monaco                         | 99999                   |
| MD   | Republic of Moldova            | 9999                    |
| MH   | Marshall Islands               | 99999                   |
| MK   | North Macedonia                | 9999                    |
| MP   | North Mariana Islands          | 99999                   |
| MQ   | Matinique                      | 99999                   |
| MT   | Malta                          | aaa 9999                |
| MX   | Mexico                         | 99999                   |
| MY   | Malaysia                       | 99999                   |
| NL   | Netherlands                    | 9999 aa                 |
| NO   | Norway                         | 9999                    |
| NZ   | New Zealand                    | 9999                    |
| PH   | Philippines                    | 9999                    |
| PK   | Pakistan                       | 99999                   |
| PL   | Poland                         | 99-999                  |
| PR   | Puerto Rico                    | 99999                   |
| PT   | Portugal                       | 9999-999                |
| PW   | Palau                          | 99999                   |
| RE   | Reunion                        | 99999                   |
| RO   | Romania                        | 999999                  |
| RU   | Russian Federation             | 999999                  |
| SE   | Sweden                         | 999 99                  |
| SG   | Singapore                      | 999999                  |
| SI   | Slovenia                       | 9999                    |
| SK   | Slovakia                       | 999 99                  |
| SM   | San Marino                     | 99999                   |
| TH   | Thailand                       | 99999                   |
| TR   | Turkey                         | 99999                   |
| UA   | Ukraine                        | 99999                   |
| US   | United States                  | 99999                   |
| UY   | Uruguay                        | 99999                   |
| VI   | Virgin Islands, US             | 99999                   |
| WF   | Wallis and Futuna              | 99999                   |
| YT   | Mayotte                        | 99999                   |
| ZA   | South Africa                   | 9999                    |

### Useragent enrichment

If you create the Account Takeover Insights (ATI) model, you must provide a variable of the `useragent` variable type in your dataset.
This variable contains the browser, device, and OS data of a login event. Amazon Fraud Detector enriches the useragent data with additional information such as `user_agent_family`
`OS_family`, and `device_family`.
