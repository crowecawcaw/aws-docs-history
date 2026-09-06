

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Variables
<a name="variables"></a>

Variables represent data elements that you want to use in a fraud prediction. These variables can be taken from the event dataset that you prepared for training your model, from your Amazon Fraud Detector model's risk score outputs, or from Amazon SageMaker AI models. For more information about variables taken from the event dataset, see [Get event dataset requirements using the Data models explorer](create-event-dataset.md#prepare-event-dataset).

The variables you want to use in your fraud prediction must first be created and then added to the event when creating your event type. Each variable you create must be assigned a datatype, a default value, and optionally a variable type. Amazon Fraud Detector enriches some of the variables that you provide such as IP addresses, bank identification numbers (BINs), and phone numbers, to create additional inputs and boost performance for the models that use these variables.

## Data types
<a name="data-types"></a>

Variables must have a data type for the data element that the variable represents and can optionally be assigned one of the predefined [Variable types](#variable-types). For variables that are assigned to a variable type, the data type is pre-selected. Possible data types include the following types :


| Data type | Description  | Default value | Example values | 
| --- | --- | --- | --- | 
| String | Any combination of letters, whole numbers, or both | <empty> | abc, 123, 1D3B | 
| Integer | Positive or negative whole numbers | 0 | 1, -1 | 
| Boolean | True or False | False | True, False | 
| DateTime | Date and time specified in the ISO 8601 standard UTC format only | <empty> | 2019-11-30T13:01:01Z | 
| Float | Numbers with decimal points | 0.0 | 4.01, 0.10 | 

## Default value
<a name="default-value"></a>

Variables must have a default value. When Amazon Fraud Detector generates fraud predictions, this default value is used to run a rule or model if Amazon Fraud Detector doesn't receive a value for a variable. Default values you provide must match the selected data type. In the AWS Console, Amazon Fraud Detector assigns the default value of `0` for integers, `false` for Booleans, `0.0` for floats, and (empty) for strings. You can set a custom default value for any of these data types. 

## Variable types
<a name="variable-types"></a>

When you create a variable, you can optionally assign the variable to a variable type. Variable type represents the common data elements that are used to train models and to generate fraud predictions. Only variables with an associated variable type can be used for model training. As part of the model training process, Amazon Fraud Detector uses the variable type associated with the variable to perform variable enrichments, feature engineering, and risk scoring.

Amazon Fraud Detector has pre-defined the following variable types that can be used to assign to your variables.



- **Session**
  - **Variable type:** IP\_ADDRESS / **Description:** The IP address that's collected during the event / **Data type:** String / **Example:** 192.0.2.0 **Note:** Amazon Fraud Detector enriches this data. For more information, see [Geolocation enrichment](#geolocation-enrichment)
  - **Variable type:** USERAGENT / **Description:** The user agent that's collected during the event / **Data type:** String / **Example:** Mozilla 5.0 (Windows NT 10.0, Win64, x64,rv:68.0) Gecko 20100101
  - **Variable type:** FINGERPRINT / **Description:** The unique identifier for a device used for the event / **Data type:** String / **Example:** sadfow987u234
  - **Variable type:** SESSION\_ID / **Description:** The session ID for the event's active session / **Data type:** String / **Example:** sid123456789
  - **Variable type:** ARE\_CREDENTIALS\_VALID / **Description:** Indicates if the credentials used for event login are valid / **Data type:** Boolean / **Example:** True

- **User**
  - **Variable type:** EMAIL\_ADDRESS / **Description:** The email address that's collected during the event / **Data type:** String / **Example:** abc@domain.com
  - **Variable type:** PHONE\_NUMBER / **Description:** The phone number collected during the event / **Data type:** String / **Example:** \+1 555-0100 **Note:** Amazon Fraud Detector enriches this data. For more information, see [Phone number enrichment](#phone-number-enrichment)

- **Billing**
  - **Variable type:** BILLING\_NAME / **Description:** The name that's associated with the billing address / **Data type:** String / **Example:** John Doe
  - **Variable type:** BILLING\_PHONE / **Description:** The phone number that's associated with the billing address  / **Data type:** String / **Example:** \+1 555-0100 **Note:** Amazon Fraud Detector enriches this data. For more information, see [Phone number enrichment](#phone-number-enrichment)
  - **Variable type:** BILLING\_ADDRESS\_L1 / **Description:** The first line of the billing address  / **Data type:** String / **Example:** Any street
  - **Variable type:** BILLING\_ADDRESS\_L2 / **Description:** The second line of the billing address / **Data type:** String / **Example:** Any unit 123
  - **Variable type:** BILLING\_CITY / **Description:** The city that's in the billing address / **Data type:** String / **Example:** Any City
  - **Variable type:** BILLING\_STATE / **Description:** The state or province that's in the billing address / **Data type:** String / **Example:** Any state or province
  - **Variable type:** BILLING\_COUNTRY / **Description:** The country that's in the billing address / **Data type:** String / **Example:** Any country **Note:** Amazon Fraud Detector enriches this data. For more information, see [Geolocation enrichment](#geolocation-enrichment)
  - **Variable type:** BILLING\_ZIP / **Description:** The postal code that's in the billing address / **Data type:** String / **Example:** 01234 **Note:** Amazon Fraud Detector enriches this data. For more information, see [Geolocation enrichment](#geolocation-enrichment)

- **Shipping**
  - **Variable type:** SHIPPING\_NAME / **Description:** The name that's associated with the shipping address / **Data type:** String / **Example:** John Doe
  - **Variable type:** SHIPPING\_PHONE / **Description:** The phone number that's associated with the shipping address / **Data type:** String / **Example:** \+1 555-0100 **Note:** Amazon Fraud Detector enriches this data. For more information, see [Phone number enrichment](#phone-number-enrichment)
  - **Variable type:** SHIPPING\_ADDRESS\_L1 / **Description:** The first line of the shipping address  / **Data type:** String / **Example:** 123 Any Street
  - **Variable type:** SHIPPING\_ADDRESS\_L2 / **Description:** The second line of the shipping address / **Data type:** String / **Example:** Unit 123
  - **Variable type:** SHIPPING\_CITY / **Description:** The city that's in the shipping address / **Data type:** String / **Example:** Any City
  - **Variable type:** SHIPPING\_STATE / **Description:** The state or province that's in the shipping address / **Data type:** String / **Example:** Any State
  - **Variable type:** SHIPPING\_COUNTRY / **Description:** The country that's in that's in the shipping address / **Data type:** String / **Example:** Any Country **Note:** Amazon Fraud Detector enriches this data. For more information, see [Geolocation enrichment](#geolocation-enrichment)
  - **Variable type:** SHIPPING\_ZIP / **Description:** The postal code that's in the shipping address / **Data type:** String / **Example:** 01234 **Note:** Amazon Fraud Detector enriches this data. For more information, see [Geolocation enrichment](#geolocation-enrichment)

- **Payment**
  - **Variable type:** ORDER\_ID / **Description:** The unique identifier for the transaction / **Data type:** String / **Example:** LUX60
  - **Variable type:** PRICE / **Description:** The total order price / **Data type:** String / **Example:** 560.00
  - **Variable type:** CURRENCY\_CODE / **Description:** The ISO 4217 currency code / **Data type:** String / **Example:** USD
  - **Variable type:** PAYMENT\_TYPE / **Description:** The payment method that's used for payment during the event / **Data type:** String / **Example:** Credit card
  - **Variable type:** AUTH\_CODE / **Description:** The alphanumerical code that's sent by a credit card issuer or issuing bank / **Data type:** String / **Example:** 0000
  - **Variable type:** AVS / **Description:** The address verification system (AVS) response code from the card processor / **Data type:** String / **Example:** Y

- **Product**
  - **Variable type:** PRODUCT\_CATEGORY
  - **Description:** The product category of order item
  - **Data type:** String
  - **Example:** Kitchen

- **Custom**
  - **Variable type:** NUMERIC / **Description:** Any variable that can be represented as a real number / **Data type:** Float / **Example:** 1.224
  - **Variable type:** CATEGORICAL / **Description:** Any variable that describes categories, segments, or groups / **Data type:** String / **Example:** Large
  - **Variable type:** FREE\_FORM\_TEXT / **Description:** Any free form text that's captured as part of the event (for example, a customer review or comment) / **Data type:** String / **Example:** Example of a free form text input



### Assigning variable to a variable type
<a name="assign-variable-to-variable-type"></a>

If you are planning to use a variable for training your model, it is important that you choose a right variable type to assign to the variable. Incorrect variable type assignment can negatively impact your model performance. It can also become very difficult for you change the assignment later, especially if multiple models and events have used the variable. 

You can assign your variable any one of the pre-defined variable types or one of the custom variable types – `FREE_FORM_TEXT`, `CATEGORICAL`, or `NUMERIC`.

**Important notes for assigning variables to the right variable types**

1. If the variable matches one of predefined variable types, use it. Make sure the variable type corresponds to the variable. For example, if you assign an *ip\_address* variable to `EMAIL_ADDRESS` variable type, the ip\_address variable will not get enriched with enrichments such as ASN, ISP, geo-location, and risk score. For more information, see [Variable enrichments](#variable-enrichments). 

1. If the variable doesn’t match any of predefined variable types, follow the recommendations listed below to assign one of the custom variable types. 

1. Assign `CATEGORICAL` variable type to variables that typically do not have natural ordering and can be put into categories, segments, or groups. The dataset you are using to train your model might have ID variables such as, *merchant\_id*, *campaign\_id*, or *policy\_id*. These variables represent groups (for example, all customers with same policy\_id represent a group). Variables that have the following data must be assigned CATEGORICAL variable type -
   + Variables that contain data such as *customer\_ID*, *segment\_ID*, *color\_ID*, *department\_code*, or *product\_ID*.
   + Variables that contain Boolean data with true, false, or null values.
   + Variables that can be put into groups or categories such as company name, product category, card type, or referral medium.
**Note**  
`ENTITY_ID` is a reserved variable type used by Amazon Fraud Detector to assign to ENTITY\_ID variable. The ENTITY\_ID variable is the ID of the entity initiating the action you want to evaluate. If you are creating a Transaction Fraud Insight (TFI) model type, you are required to provide ENTITY\_ID variable. You will need to decide which variable in your data uniquely identifies the entity initiating the action and pass it on as ENTITY\_ID variable. Assign CATEGORICAL variable type to all the other IDs in your dataset, if they are present and if you are using them for model training. Examples of other IDs that are not an entity in your dataset can be *merchant\_ID*, *policy\_ID*, and *campaign\_ID*.

1. Assign `FREE_FORM_TEXT` variable type to variables that contain a block of text. Examples of FREE\_FORM\_TEXT variable types are – *user reviews*, *comments*, *dates*, and *referral codes*. The FREE\_FORM\_TEXT data contains multiple tokens separated by a delimiter. The delimiters can be any character other than alpha-numeric and underscore symbol. For example, user reviews and comments can be separated by “space” delimiter, dates and referral codes can use hyphens as delimiters to separate out prefix, suffix, and intermediate parts. Amazon Fraud Detector uses the delimiters to extract data from FREE\_FORM\_TEXT variables.

1. Assign *NUMERIC* variable type to variables that are real numbers and have inherent ordering. Examples of NUMERIC variables include *day\_of\_the\_week*, *incident\_severity*, *customer\_rating*. Although, you can assign CATEGORICAL variable type to these variables, we strongly recommend to assign all real number variables with inherent order to NUMERIC variable type.

## Variable enrichments
<a name="variable-enrichments"></a>

Amazon Fraud Detector enriches some of the raw data elements that you provide such as IP addresses, bank identification numbers (BINs), and phone numbers, to create additional inputs and boost performance for the models that use these data elements. The enrichment helps identify potentially suspicious situations and help the models to capture more fraud.

### Phone number enrichment
<a name="phone-number-enrichment"></a>

Amazon Fraud Detector enriches phone number data with additional information that relates to geolocation, the original carrier, and the validity of the phone number. Phone number enrichment is automatically enabled for all the models that are trained on or after *December 13, 2021* and have a phone number that includes a country code (\+xxx). If you have included phone number variable in your model and have trained it before *December 13, 2021*, retrain your model so it can take advantage of this enrichment. 

We highly recommend that you use the following format for phone number variables to ensure that your data is enriched successfully.


| Variable | Format | Description | 
| --- | --- | --- | 
| PHONE\_NUMBER | The [E.164](https://en.wikipedia.org/wiki/E.164) standard | Make sure to include country code (\+xxx) with the phone number. | 
| BILLING\_PHONE and SHIPPING\_PHONE | The [E.164](https://en.wikipedia.org/wiki/E.164) standard | Make sure to include country code (\+xxx) with the phone number. | 

### Geolocation enrichment
<a name="geolocation-enrichment"></a>

Starting on *February 8, 2022* Amazon Fraud Detector calculates the physical distance between the IP\_ADDRESS, BILLING\_ZIP, and SHIPPING\_ZIP values that you provide for an event. The calculated distances are used as inputs to your fraud detection model.

To enable geolocation enrichment, your event data must include at least two of the three variables: IP\_ADDRESS, BILLING\_ZIP, or SHIPPING\_ZIP. In addition, each BILLING\_ZIP and SHIPPING\_ZIP value must have a valid BILLING\_COUNTRY code and SHIPPING\_COUNTRY code respectively. If you have a model that was trained before *February 8, 2022* and it includes these variables, you must retrain the model to enable the geolocation enrichment. 

If Amazon Fraud Detector can't determine the location that's associated with the IP\_ADDRESS, BILLING\_ZIP ,or SHIPPING\_ZIP values for an event due to the data being not valid, a special placeholder value is used instead. For example, suppose that an event has valid IP\_ADDRESS and BILLING\_ZIP values, but SHIPPING\_ZIP value isn't valid. In this case, enrichment is done only for IP\_ADDRESS–> BILLING\_ZIP. The enrichment isn't done for IP\_ADDRESS–>SHIPPING\_ZIP and BILLING\_ZIP–>SHIPPING\_ZIP . Instead, the placeholder values are used in their place. No matter if geolocation enrichment is enabled for your model or not, the performance of your model doesn't change. 

You can opt out of geolocation enrichment by mapping your BILLING\_ZIP and SHIPPING\_ZIP variables to the CUSTOM\_CATEGORICAL variable type. Changing the variable type doesn't affect your model's performance. 

**Geolocation variable format**

We highly recommend that you use the following format for geolocation variables to ensure that your location data is enriched successfully. 


| Variable | Format | Description | 
| --- | --- | --- | 
| IP\_ADDRESS | [IPv4](https://en.wikipedia.org/wiki/IP_address#IPv4_addresses) address | For example - 1.1.1.1 | 
| BILLING\_ZIP and SHIPPING\_ZIP | The [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) postal code for the specified country  | For more information, see the Country and territory codes  section in this topic. | 
| BILLING\_COUNTRY and SHIPPING\_COUNTRY | The [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) two-letter standard country code | For more information, see the Country and territory codes section in this topic. Amazon Fraud Detector tries to match all the common variations of a country's name to their ISO 3166-1 two-letter standard country code. However, we cannot guarantee they will be matched correctly.  | 

#### Country and territory codes
<a name="countries-code-format"></a>

The following table provides a complete list of the countries and territories that are supported by Amazon Fraud Detector for geolocation enrichment. Each country and territory has an assigned country code (specifically, the ISO 3166-1 alpha-2 two-letter country code) and a postal code.

**Postal code format**
+ 9 - number
+  a - letter
+ [X] - X is optional. For example, Guersney "GY9[9] 9aa" means both "GY9 9aa" and "GY99 9aa" are valid. Use one format.
+ [X/XX] - either X or XX can be used. For example, Bermuda "aa[aa/99]" means both "aa aa" and "aa 99" are valid. Use either one of these formats, but *do not* use both.
+ Some countries have fixed prefix. For example, the postal code for Andorra is AD999. This means the country code must start with letters *AD* followed by three numbers.


| Code | Name  | Postal code | 
| --- | --- | --- | 
| AD | Andorra | AD999 | 
| AR | Netherlands Antilles | 9999 | 
| AT | Austria | 9999 | 
| AU | Australia | 9999 | 
| AZ | Azerbaijan | AZ 9999 | 
| BD | Bangladesh | 9999 | 
| BE | Belgium | 9999 | 
| BG | Bulgaria | 9999 | 
| BM | Bermuda | aa[aa/99] | 
| BY | Belarus | 999999 | 
| CA | Canada | a9a 9a9 | 
| CH | Switzerland | 9999 | 
| CL | Chile | 9999999 | 
| CO | Colombia | 999999 | 
| CR | Costa Rica | 99999 | 
| CY | Cyprus | 9999 | 
| CZ | Czechia | 999 99 | 
| DE | Germany | 99999 | 
| DK | Denmark | 9999 | 
| DO | Dominican Republic | 99999 | 
| DZ | Algeria | 99999 | 
| EE | Estonia | 99999 | 
| ES | Spain | 99999 | 
| FI | Finland | 99999 | 
| FM | Federated States of Micronesia | 99999 | 
| FO | Faroe Islands | 999 | 
| FR | France | 99999 | 
| GB | United Kingdom | a[a]9[a/9] 9aa  | 
| GG | Guernsey | GY9[9] 9aa | 
| GL | Greenland | 9999 | 
| GP | Guadeloupe | 99999 | 
| GT | Guatemala | 99999 | 
| GU | Guam | 99999 | 
| HR | Croatia | 99999 | 
| HU | Hungary | 9999 | 
| IE | Ireland | a99[a/9][a/9][a/9][a/9] | 
| IM | Isle of Man | IM9[9]9aa | 
| IN | India | 999999 | 
| IS | Iceland | 999 | 
| IT | Italy | 99999 | 
| JE | Jersey | JE9[9]9aa | 
| JP | Japan | 999-9999 | 
| KR | Republic of Korea | 99999 | 
| LI | Liechtenstein | 9999 | 
| LK | Sri Lanka | 99999 | 
| LT | Lithuania | 99999 | 
| LU | Luxembourg | L-9999 | 
| LV | Latvia | LV-9999 | 
| MC | Monaco | 99999 | 
| MD | Republic of Moldova | 9999 | 
| MH | Marshall Islands | 99999 | 
| MK | North Macedonia | 9999 | 
| MP | North Mariana Islands | 99999 | 
| MQ | Matinique | 99999 | 
| MT | Malta | aaa 9999 | 
| MX | Mexico | 99999 | 
| MY | Malaysia | 99999 | 
| NL | Netherlands | 9999 aa | 
| NO | Norway | 9999 | 
| NZ | New Zealand | 9999 | 
| PH | Philippines | 9999 | 
| PK | Pakistan | 99999 | 
| PL | Poland | 99-999 | 
| PR | Puerto Rico | 99999 | 
| PT | Portugal | 9999-999 | 
| PW | Palau | 99999 | 
| RE | Reunion | 99999 | 
| RO | Romania | 999999 | 
| RU | Russian Federation | 999999 | 
| SE | Sweden | 999 99 | 
| SG | Singapore | 999999 | 
| SI | Slovenia | 9999 | 
| SK | Slovakia | 999 99 | 
| SM | San Marino | 99999 | 
| TH | Thailand | 99999 | 
| TR | Turkey | 99999 | 
| UA | Ukraine | 99999 | 
| US | United States | 99999 | 
| UY | Uruguay | 99999 | 
| VI | Virgin Islands, US | 99999 | 
| WF | Wallis and Futuna | 99999 | 
| YT | Mayotte | 99999 | 
| ZA | South Africa | 9999 | 

### Useragent enrichment
<a name="useragent-enrichment"></a>

If you create the Account Takeover Insights (ATI) model, you must provide a variable of the `useragent` variable type in your dataset. This variable contains the browser, device, and OS data of a login event. Amazon Fraud Detector enriches the useragent data with additional information such as `user_agent_family` `OS_family`, and `device_family`.