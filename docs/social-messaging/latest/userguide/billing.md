# Understanding billing and usage reports for AWS End User Messaging Social

You are billed on a per message basis when you use AWS End User Messaging Social. This topic
explains the different types of `MetaTemplateMessageFee` and AWS `MessageFee`
charges that you can incur per message while using End User Messaging Social.

The `MetaTemplateMessageFees` are
set by Meta and subject to change by Meta. AWS will make reasonable efforts to notify you whenever Meta
increases the `MetaTemplateMessageFees`.

Effective February 1, 2026, AWS will charge the `MetaTemplateMessageFees` using the rates in Meta's INR rate card, including for volume-tiered pricing. AWS will charge the `MetaTemplateMessageFees` in USD by applying the INR to USD exchange rate as of February 1, 2026. On the first day of each quarter, AWS may update the USD price it charges for the `MetaTemplateMessageFees` to reflect changes to the INR to USD exchange rate.

## Charged per message

The AWS End User Messaging Social channel generates a usage type that contains five fields in the following
format:

```
`Region code`–`MessagingType`–`ISO`–`FeeDescription`–`FeeType`
```

There are two possible billing items for each WhatsApp message: the
`MetaTemplateMessageFee` charged by Meta, and the `MessageFee` charged by AWS.

When you send a template message, you are billed for one WhatsApp
`MetaTemplateMessageFee` and one AWS `MessageFee`.
The following table provides the descriptions and possible values for the fields in the
usage type. For more information about AWS End User Messaging Social pricing, see [WhatsApp](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/") in AWS End User Messaging
Pricing.

| Field            | Description                                                                                   | Possible values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Region code`    | The AWS Region prefix that indicates where the WhatsApp message was<br>sent or received from. | • **USE1** –<br>US East (N. Virginia) Region<br>• **USE2** –<br>US East (Ohio) Region<br>• **USW2** –<br>US West (Oregon) Region<br>• **APS3** –<br>Asia Pacific (Mumbai) Region<br>• **APS5** –<br>Asia Pacific (Hyderabad) Region<br>• **APS1** –<br>Asia Pacific (Singapore) Region<br>• **APS2** –<br>Asia Pacific (Sydney) Region<br>• **APS6** –<br>Asia Pacific (New Zealand) Region<br>• **EU** – Europe (Ireland) Region<br>• **EUW2** –<br>Europe (London) Region<br>• **APN1** –<br>Asia Pacific (Tokyo) Region<br>• **APN2** –<br>Asia Pacific (Seoul) Region<br>• **EUC1** –<br>Europe (Frankfurt) Region<br>• **EUN1** –<br>Europe (Stockholm) Region<br>• **EUS2** –<br>Europe (Spain) Region<br>• **MEC1** –<br>Middle East (UAE) Region<br>• **MES1** –<br>Middle East (Bahrain) Region<br>• **MXC1** –<br>Mexico (Central) Region<br>• **SAE1** –<br>South America (São Paulo) Region<br>• **AFS1** –<br>Africa (Cape Town) Region<br>• **CAN1** –<br>Canada (Central) Region<br>• **CAW1** –<br>Canada West (Calgary) Region                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `MessagingType`  | Identifies the message type that the charges are for.                                         | `WhatsApp`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `ISO`            | The two–digit ISO country code that the message was sent to.                                  | See [supported<br>countries](charged-per-conversation.md#supported-iso-codes "charged-per-conversation.md#supported-iso-codes") for possible values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `FeeDescription` | Describes the fee.                                                                            | • `MetaTemplateMessageFee` charged by Meta[1](#meta-note-1 "#meta-note-1")<br>• `MessageFee` charged by End User Messaging Social                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Meta `FeeType`   | This field displays the `MetaTemplateMessageFee` fee type for the message.                    | `MetaTemplateMessageFee` types for business-initiated messages<br>• `Authentication` – Used to authenticate<br>users with one-time passcodes, which could occur at multiple steps<br>in the login process. This can include account verification,<br>account recovery, and account integrity challenges.<br>• `Authentication-International` – Used the<br>same as `Authentication` but your business is<br>eligible for [Authentication-International](charged-per-conversation.md#billing-authentication-international "charged-per-conversation.md#billing-authentication-international") rates, based in<br>another country, and the message was sent on or after the<br>start time for the country.<br>• `Marketing` – Used to achieve a wide<br>range of goals, from generating awareness to driving sales<br>and retargeting customers. Examples include new product,<br>service, or feature announcements, targeted<br>promotions/offers, and cart abandonment reminders.<br>• `Service` – Used to resolve customer<br>inquiries.<br>• `Utility` – Used to follow up on user<br>actions or requests. Examples include opt-in confirmation,<br>order/delivery management (for example a delivery update);<br>account updates or alerts (for example a payment reminder);<br>or feedback surveys.<br>`MetaTemplateMessageFee` types for user-initiated messages<br>• `Service` – Used to resolve customer<br>inquiries.<br>Volume-tiered pricing is applicable on `Authentication`, `Authentication-International`, and `Utility` message types. For information about volume-tiered pricing, see [Volume-tiered pricing](#billing-volume-tiered-pricing "#billing-volume-tiered-pricing"). |
| AWS `FeeType`    | This field displays the AWS `MessageFee` type for the message.                                | AWS`MessageFee` types for business-initiated messages<br>• `Authentication` – Used to authenticate<br>users with one-time passcodes, which could occur at multiple steps<br>in the login process. This can include account verification,<br>account recovery, and account integrity challenges.<br>• `Authentication-International` – Used the<br>same as `Authentication` but your business is<br>eligible for [Authentication-International](charged-per-conversation.md#billing-authentication-international "charged-per-conversation.md#billing-authentication-international") rates, based in<br>another country, and the message was sent on or after the<br>start time for the country.<br>• `Marketing` – for messages used for marketing purposes,<br>from generating awareness to driving sales<br>and retargeting customers. Examples include new product,<br>service, or feature announcements, targeted<br>promotions/offers, and cart abandonment reminders.<br>• `Service` – for messages related to resolving customer<br>inquiries.<br>• `Standard` – for free-form messages<br>• `Utility` – Used to follow up on user<br>actions or requests. Examples include opt-in confirmation,<br>order/delivery management (for example a delivery update);<br>account updates or alerts (for example a payment reminder);<br>or feedback surveys.<br>`MessageFee` types for user-initiated messages<br>• `Inbound` – for user-initiated messages.                                                                                                                                                                                                                                      |

###### Note

1The `MetaTemplateMessageFees` are
set by Meta and subject to change by Meta. AWS will make reasonable efforts to notify you whenever Meta
increases the `MetaTemplateMessageFees`.

When you send a template message, you are billed for one
`MetaTemplateMessageFee` and one AWS `MessageFee`. When you send
free form text messages, or receive inbound messages, you are billed for one
`MessageFee`.

For example, if you send a marketing template message to a customer, you are billed for
one `MetaTemplateMessageFee` and one `MessageFee`.

### Example billing SKU names

The following are examples of actual billing SKU names. These examples show AWS MessageFee FeeTypes
for messages sent or received from the `APS3` region code (ap-south-1, Asia Pacific (Mumbai)), and sent to
the ISO code `IN` (India).

```
APS3-WhatsApp-IN-MessageFee-Authentication
APS3-WhatsApp-IN-MessageFee-Service
APS3-WhatsApp-IN-MessageFee-Authentication_International
APS3-WhatsApp-IN-MessageFee-Marketing
APS3-WhatsApp-IN-MessageFee-Inbound
APS3-WhatsApp-IN-MessageFee-Utility
APS3-WhatsApp-IN-MessageFee-Standard
```

### When does the

Authentication-International FeeType apply

For a list of countries with an `Authentication-International` FeeType, see
[WhatsApp](https://aws.amazon.com/end-user-messaging/pricing/#WhatsApp "https://aws.amazon.com/end-user-messaging/pricing/#WhatsApp") in AWS End User Messaging Pricing.

If you send an `Authentication` message to a WhatsApp user whose
country calling code has an `Authentication-International` FeeType, you will
be billed that country's `Authentication-International` rate if:

1. Your business opens more than 750K messages in a moving 30-day period across
   all of your WhatsApp Business Accounts with WhatsApp users whose country
   calling codes are for a country that has an
   `Authentication-International` rate. For more information,
   see [Eligibility](https://developers.facebook.com/docs/whatsapp/pricing/authentication-international-rates#eligibility "https://developers.facebook.com/docs/whatsapp/pricing/authentication-international-rates#eligibility") in the _WhatsApp Business Platform
   Developer Guide_.

###### Important

If Meta determines that your business is eligible for
`Authentication-International` then they will attempt to send
you an email notification with applicable countries and moving 30-day period
start times. 2. Your business is based in another country. For more information on managing
your business's location, see [Primary business location](https://developers.facebook.com/docs/whatsapp/pricing/authentication-international-rates#primary-business-location "https://developers.facebook.com/docs/whatsapp/pricing/authentication-international-rates#primary-business-location") in the _WhatsApp Business
Platform Developer Guide_. 3. The message was sent on or after your start time of the 30-day period for that
country.

### Example 1: Sending a Marketing template message

For example, if you send a marketing template message to a customer, you are billed for
one WhatsApp `MetaTemplateMessageFee` and one AWS
`MessageFee`.

```
Marketing Template Message 1: APS1-WhatsApp-CA-MetaTemplateMessageFee-Marketing
Marketing Template Message 1: APS1-WhatsApp-CA-MessageFee-Marketing
```

### Example 2: Opening a service conversation

A service conversation is created when a business responds to a user's inbound message
within 24 hours of receiving the user-initiated message. In this scenario, you are
billed one `MetaTemplateMessageFee-Service_Regular` fee and an AWS
`MessageFee-Service` for each outbound message, and billed one `MessageFee-Inbound`
for each user-initiated message. For example, if a
user initiated the first message, the business responded, and the user responded back, the
charges for the three messages would be the following:

```
User Initiated Message 1: APS1-WhatsApp-CA-MessageFee-Inbound
Business Initiated Message 2: APS1-WhatsApp-CA-MetaTemplateMessageFee-Service_Regular
Business Initiated Message 2: APS1-WhatsApp-CA-MessageFee-Service
User Initiated Message 3: APS1-WhatsApp-CA-MessageFee-Inbound
```

### Volume-tiered pricing

AWS End User Messaging Social uses Meta's volume tiered pricing for WhatsApp template messages. When your monthly volume crosses tier thresholds, you benefit from lower per-message rates for Meta message fees for the remainder of that billing period. Currently, volume tiers apply to authentication, authentication-international and utility template messages by country, and do not apply to marketing template messages. The volume-tiered prices, tier thresholds, and discounts are set by Meta, and subject to change by Meta. AWS will make reasonable efforts to notify you of changes to volume tiers.

Key pricing considerations include the following:

- Only template messages count toward volume calculations—non-template messages sent within customer service windows are always free.
- Tiers vary by country and message type (authentication versus utility), and reset monthly.
- Multiple WABAs in your account are aggregated together for tier determination.
- Mid-month tier changes apply discounted rates only to subsequent messages.

Volume tiers on ongoing monthly usage are determined solely by Meta. AWS applies the volume tiers to ongoing usage as and when Meta informs us of tier changes. For more information about tier thresholds and current rates, see [Meta's WhatsApp Business Platform pricing documentation](https://developers.facebook.com/docs/whatsapp/pricing/ "https://developers.facebook.com/docs/whatsapp/pricing/").

The following SKU examples show the volume-tiered pricing for `Authentication`, `Authentication-International`, and `Utility` message types.

The following are examples of actual billing SKU names. These examples show `Meta FeeType` for messages sent or received from the `APS3` Region code (ap-south-1, Asia Pacific (Mumbai) Region), and sent to the ISO code IN (India).

```
APS3-WhatsApp-IN-MetaTemplateMessageFee-Authentication_Regular
APS3-WhatsApp-IN-MetaTemplateMessageFee-Authentication_Regular_TIER_1
APS3-WhatsApp-IN-MetaTemplateMessageFee-Authentication_Regular_TIER_2
APS3-WhatsApp-IN-MetaTemplateMessageFee-Authentication_Regular_TIER_3
APS3-WhatsApp-IN-MetaTemplateMessageFee-Authentication_Regular_TIER_4
APS3-WhatsApp-IN-MetaTemplateMessageFee-Authentication_Regular_TIER_5
APS3-WhatsApp-IN-MetaTemplateMessageFee-Authentication_International_Regular
APS3-WhatsApp-IN-MetaTemplateMessageFee-Authentication_International_Regular_TIER_1
APS3-WhatsApp-IN-MetaTemplateMessageFee-Authentication_International_Regular_TIER_2
APS3-WhatsApp-IN-MetaTemplateMessageFee-Authentication_International_Regular_TIER_3
APS3-WhatsApp-IN-MetaTemplateMessageFee-Authentication_International_Regular_TIER_4
APS3-WhatsApp-IN-MetaTemplateMessageFee-Authentication_International_Regular_TIER_5
APS3-WhatsApp-IN-MetaTemplateMessageFee-Utility_Regular
APS3-WhatsApp-IN-MetaTemplateMessageFee-Utility_Regular_TIER_1
APS3-WhatsApp-IN-MetaTemplateMessageFee-Utility_Regular_TIER_2
APS3-WhatsApp-IN-MetaTemplateMessageFee-Utility_Regular_TIER_3
APS3-WhatsApp-IN-MetaTemplateMessageFee-Utility_Regular_TIER_4
APS3-WhatsApp-IN-MetaTemplateMessageFee-Utility_Regular_TIER_5

```

### AWS End User Messaging Social billing ISO codes and

MetaTemplateMessageFee mapping

| Supported countries | Two-digit ISO country code                   | Country name                     | WhatsApp conversation billing region |
| ------------------- | -------------------------------------------- | -------------------------------- | ------------------------------------ |
| AF                  | Afghanistan                                  | Rest of Asia Pacific             |
| AX                  | Aland Islands                                | Other                            |
| AL                  | Albania                                      | Rest of Central & Eastern Europe |
| DZ                  | Algeria                                      | Rest of Africa                   |
| AS                  | American Samoa                               | Other                            |
| AD                  | Andorra                                      | Other                            |
| AO                  | Angola                                       | Rest of Africa                   |
| AI                  | Anguilla                                     | Other                            |
| AQ                  | Antarctica                                   | Other                            |
| AG                  | Antigua and Barbuda                          | Other                            |
| AR                  | Argentina                                    | Argentina                        |
| AM                  | Armenia                                      | Rest of Central & Eastern Europe |
| AW                  | Aruba                                        | Other                            |
| AC                  | Ascension Island                             | Other                            |
| AU                  | Australia                                    | Rest of Asia Pacific             |
| AT                  | Austria                                      | Rest of Western Europe           |
| AZ                  | Azerbaijan                                   | Rest of Central & Eastern Europe |
| BS                  | Bahamas                                      | Other                            |
| BH                  | Bahrain                                      | Rest of Middle East              |
| BD                  | Bangladesh                                   | Rest of Asia Pacific             |
| BB                  | Barbados                                     | Other                            |
| BY                  | Belarus                                      | Rest of Central & Eastern Europe |
| BE                  | Belgium                                      | Rest of Western Europe           |
| BZ                  | Belize                                       | Other                            |
| BJ                  | Benin                                        | Rest of Africa                   |
| BM                  | Bermuda                                      | Other                            |
| BT                  | Bhutan                                       | Other                            |
| BO                  | Bolivia                                      | Rest of Latin America            |
| BQ                  | Bonaire                                      | Other                            |
| BA                  | Bosnia and Herzegovina                       | Other                            |
| BW                  | Botswana                                     | Rest of Africa                   |
| BV                  | Bouvet Island                                | Other                            |
| BR                  | Brazil                                       | Brazil                           |
| IO                  | British Indian Ocean Territory               | Other                            |
| VG                  | British Virgin Islands                       | Other                            |
| BN                  | Brunei Darussalam                            | Other                            |
| BG                  | Bulgaria                                     | Rest of Central & Eastern Europe |
| BF                  | BurkinaFaso                                  | Rest of Africa                   |
| BI                  | Burundi                                      | Rest of Africa                   |
| KH                  | Cambodia                                     | Rest of Asia Pacific             |
| CM                  | Cameroon                                     | Rest of Africa                   |
| CA                  | Canada                                       | North America                    |
| CV                  | Cape Verde                                   | Other                            |
| KY                  | Cayman Islands                               | Other                            |
| CF                  | Central African Republic                     | Other                            |
| TD                  | Chad                                         | Rest of Africa                   |
| CL                  | Chile                                        | Chile                            |
| CN                  | China                                        | Rest of Asia Pacific             |
| CX                  | Christmas Island                             | Other                            |
| CC                  | Cocos(Keeling) Islands                       | Other                            |
| CO                  | Colombia                                     | Colombia                         |
| KM                  | Comoros                                      | Other                            |
| CK                  | Cook Islands                                 | Other                            |
| CR                  | Costa Rica                                   | Rest of Latin America            |
| CI                  | Cote d'Ivoire                                | Rest of Africa                   |
| HR                  | Croatia                                      | Rest of Central & Eastern Europe |
| CW                  | Curacao                                      | Other                            |
| CY                  | Cyprus                                       | Other                            |
| CZ                  | Czech Republic                               | Rest of Central & Eastern Europe |
| CD                  | Democratic Republic of the Congo             | Rest of Africa                   |
| DK                  | Denmark                                      | Rest of Western Europe           |
| DJ                  | Djibouti                                     | Other                            |
| DM                  | Dominica                                     | Other                            |
| DO                  | Dominican Republic                           | Rest of Latin America            |
| EC                  | Ecuador                                      | Rest of Latin America            |
| EG                  | Egypt                                        | Egypt                            |
| SV                  | El Salvador                                  | Rest of Latin America            |
| GQ                  | Equatorial Guinea                            | Other                            |
| ER                  | Eritrea                                      | Rest of Africa                   |
| EE                  | Estonia                                      | Other                            |
| ET                  | Ethiopia                                     | Rest of Africa                   |
| SZ                  | Eswatini                                     | Rest of Africa                   |
| FK                  | Falkland Islands                             | Other                            |
| FO                  | Faroe Islands                                | Other                            |
| FJ                  | Fiji                                         | Other                            |
| FI                  | Finland                                      | Rest of Western Europe           |
| FR                  | France                                       | France                           |
| GF                  | French Guiana                                | Other                            |
| PF                  | French Polynesia                             | Other                            |
| TF                  | French Southern Territories                  | Other                            |
| GA                  | Gabon                                        | Rest of Africa                   |
| GM                  | Gambia                                       | Rest of Africa                   |
| GE                  | Georgia                                      | Rest of Central & Eastern Europe |
| DE                  | Germany                                      | Germany                          |
| GH                  | Ghana                                        | Rest of Africa                   |
| GI                  | Gibraltar                                    | Other                            |
| GR                  | Greece                                       | Rest of Central & Eastern Europe |
| GL                  | Greenland                                    | Other                            |
| GD                  | Grenada                                      | Other                            |
| GP                  | Guadeloupe                                   | Other                            |
| GU                  | Guam                                         | Other                            |
| GT                  | Guatemala                                    | Rest of Latin America            |
| GG                  | Guernsey                                     | Other                            |
| GN                  | Guinea                                       | Other                            |
| GW                  | Guinea-Bissau                                | Rest of Africa                   |
| GY                  | Guyana                                       | Other                            |
| HT                  | Haiti                                        | Rest of Latin America            |
| HM                  | Heard and McDonald Islands                   | Other                            |
| HN                  | Honduras                                     | Rest of Latin America            |
| HK                  | Hong Kong                                    | Rest of Asia Pacific             |
| HU                  | Hungary                                      | Rest of Central & Eastern Europe |
| IS                  | Iceland                                      | Other                            |
| IN                  | India                                        | India                            |
| ID                  | Indonesia                                    | Indonesia                        |
| IQ                  | Iraq                                         | Rest of Middle East              |
| IE                  | Ireland                                      | Rest of Western Europe           |
| IM                  | Isle of Man                                  | Other                            |
| IL                  | Israel                                       | Israel                           |
| IT                  | Italy                                        | Italy                            |
| JM                  | Jamaica                                      | Rest of Latin America            |
| JP                  | Japan                                        | Rest of Asia Pacific             |
| JE                  | Jersey                                       | Other                            |
| JO                  | Jordan                                       | Rest of Middle East              |
| KZ                  | Kazakhstan                                   | Other                            |
| KE                  | Kenya                                        | Rest of Africa                   |
| KI                  | Kiribati                                     | Other                            |
| XK                  | Kosovo                                       | Other                            |
| KW                  | Kuwait                                       | Rest of Middle East              |
| KG                  | Kyrgyzstan                                   | Other                            |
| LA                  | Lao PDR                                      | Rest of Asia Pacific             |
| LV                  | Latvia                                       | Rest of Central & Eastern Europe |
| LB                  | Lebanon                                      | Rest of Middle East              |
| LS                  | Lesotho                                      | Rest of Africa                   |
| LR                  | Liberia                                      | Rest of Africa                   |
| LY                  | Libya                                        | Rest of Africa                   |
| LI                  | Liechtenstein                                | Other                            |
| LT                  | Lithuania                                    | Rest of Central & Eastern Europe |
| LU                  | Luxembourg                                   | Other                            |
| MO                  | Macao                                        | Other                            |
| MK                  | Macedonia                                    | Rest of Central & Eastern Europe |
| MG                  | Madagascar                                   | Rest of Africa                   |
| MW                  | Malawi                                       | Rest of Africa                   |
| MY                  | Malaysia                                     | Malaysia                         |
| MV                  | Maldives                                     | Other                            |
| ML                  | Mali                                         | Rest of Africa                   |
| MT                  | Malta                                        | Other                            |
| MH                  | Marshall Islands                             | Other                            |
| MQ                  | Martinique                                   | Other                            |
| MR                  | Mauritania                                   | Rest of Africa                   |
| MU                  | Mauritius                                    | Other                            |
| YT                  | Mayotte                                      | Other                            |
| MX                  | Mexico                                       | Mexico                           |
| FM                  | Micronesia                                   | Other                            |
| MD                  | Moldova                                      | Rest of Central & Eastern Europe |
| MC                  | Monaco                                       | Other                            |
| MN                  | Mongolia                                     | Rest of Asia Pacific             |
| ME                  | Montenegro                                   | Other                            |
| MS                  | Montserrat                                   | Other                            |
| MA                  | Morocco                                      | Rest of Africa                   |
| MZ                  | Mozambique                                   | Rest of Africa                   |
| MM                  | Myanmar                                      | Other                            |
| NA                  | Namibia                                      | Rest of Africa                   |
| NR                  | Nauru                                        | Other                            |
| NP                  | Nepal                                        | Rest of Asia Pacific             |
| NL                  | Netherlands                                  | Netherlands                      |
| NC                  | New Caledonia                                | Other                            |
| NZ                  | New Zealand                                  | Rest of Asia Pacific             |
| NI                  | Nicaragua                                    | Rest of Latin America            |
| NE                  | Niger                                        | Rest of Africa                   |
| NG                  | Nigeria                                      | Nigeria                          |
| NU                  | Niue                                         | Other                            |
| NF                  | Norfolk Island                               | Other                            |
| MP                  | Northern Mariana Islands                     | Other                            |
| NO                  | Norway                                       | Rest of Western Europe           |
| OM                  | Oman                                         | Rest of Middle East              |
| PK                  | Pakistan                                     | Pakistan                         |
| PW                  | Palau                                        | Other                            |
| PS                  | Palestinian Territory                        | Other                            |
| PA                  | Panama                                       | Rest of Latin America            |
| PG                  | Papua New Guinea                             | Rest of Asia Pacific             |
| PY                  | Paraguay                                     | Rest of Latin America            |
| PE                  | Peru                                         | Peru                             |
| PH                  | Philippines                                  | Rest of Asia Pacific             |
| PN                  | Pitcairn                                     | Other                            |
| PL                  | Poland                                       | Rest of Central & Eastern Europe |
| PT                  | Portugal                                     | Rest of Western Europe           |
| PR                  | Puerto Rico                                  | Rest of Latin America            |
| QA                  | Qatar                                        | Rest of Middle East              |
| CG                  | Republic of Congo                            | Other                            |
| RE                  | Reunion                                      | Other                            |
| RO                  | Romania                                      | Rest of Central & Eastern Europe |
| RU                  | Russian Federation                           | Russia                           |
| RW                  | Rwanda                                       | Rest of Africa                   |
| SH                  | Saint Helena                                 | Other                            |
| KN                  | Saint Kitts and Nevis                        | Other                            |
| LC                  | Saint Lucia                                  | Other                            |
| PM                  | Saint Pierre and Miquelon                    | Other                            |
| VC                  | Saint Vincent and Grenadines                 | Other                            |
| BL                  | Saint-Barthelemy                             | Other                            |
| MF                  | Saint-Martin                                 | Other                            |
| WS                  | Samoa                                        | Other                            |
| SM                  | San Marino                                   | Other                            |
| ST                  | Sao Tome and Principe                        | Other                            |
| SA                  | Saudi Arabia                                 | Saudi Arabia                     |
| SN                  | Senegal                                      | Rest of Africa                   |
| RS                  | Serbia                                       | Rest of Central & Eastern Europe |
| SC                  | Seychelles                                   | Other                            |
| SL                  | Sierra Leone                                 | Rest of Africa                   |
| SG                  | Singapore                                    | Rest of Asia Pacific             |
| SX                  | Sint Maarten                                 | Other                            |
| SK                  | Slovakia                                     | Rest of Central & Eastern Europe |
| SI                  | Slovenia                                     | Rest of Central & Eastern Europe |
| SB                  | Solomon Islands                              | Other                            |
| SO                  | Somalia                                      | Rest of Africa                   |
| ZA                  | South Africa                                 | South Africa                     |
| GS                  | South Georgia and the South Sandwich Islands | Other                            |
| KR                  | South Korea                                  | Other                            |
| SS                  | South Sudan                                  | Rest of Africa                   |
| ES                  | Spain                                        | Spain                            |
| LK                  | Sri Lanka                                    | Rest of Asia Pacific             |
| SR                  | Suriname                                     | Other                            |
| SJ                  | Svalbard and Jan Mayen Islands               | Other                            |
| SE                  | Sweden                                       | Rest of Western Europe           |
| CH                  | Switzerland                                  | Rest of Western Europe           |
| TW                  | Taiwan                                       | Rest of Asia Pacific             |
| TJ                  | Tajikistan                                   | Rest of Asia Pacific             |
| TZ                  | Tanzania                                     | Rest of Africa                   |
| TH                  | Thailand                                     | Rest of Asia Pacific             |
| TL                  | Timor-Leste                                  | Other                            |
| TG                  | Togo                                         | Rest of Africa                   |
| TK                  | Tokelau                                      | Other                            |
| TO                  | Tonga                                        | Other                            |
| TT                  | Trinidad and Tobago                          | Other                            |
| TA                  | Tristan da Cunha                             | Other                            |
| TN                  | Tunisia                                      | Rest of Africa                   |
| TR                  | Turkey                                       | Turkey                           |
| TM                  | Turkmenistan                                 | Rest of Asia Pacific             |
| TC                  | Turks and Caicos Islands                     | Other                            |
| TV                  | Tuvalu                                       | Other                            |
| UG                  | Uganda                                       | Rest of Africa                   |
| UA                  | Ukraine                                      | Rest of Central & Eastern Europe |
| AE                  | United Arab Emirates                         | United Arab Emirates             |
| GB                  | United Kingdom                               | United Kingdom                   |
| US                  | United States                                | North America                    |
| UY                  | Uruguay                                      | Rest of Latin America            |
| UM                  | US Minor Outlying Islands                    | Other                            |
| UZ                  | Uzbekistan                                   | Rest of Asia Pacific             |
| VU                  | Vanuatu                                      | Other                            |
| VA                  | Vatican City State                           | Other                            |
| VE                  | Venezuela                                    | Rest of Latin America            |
| VN                  | Vietnam                                      | Rest of Asia Pacific             |
| VI                  | Virgin Islands                               | Other                            |
| WF                  | Wallis and Futuna Islands                    | Other                            |
| EH                  | Western Sahara                               | Other                            |
| YE                  | Yemen                                        | Rest of Middle East              |
| ZM                  | Zambia                                       | Rest of Africa                   |
| ZW                  | Zimbabwe                                     | Other                            |
