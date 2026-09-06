

# Types of PII that Amazon Bedrock Data Automation can detect and redact
<a name="bda-sensitive-data-types"></a>

The following table lists the PII entity types that BDA can detect and redact.


**PII entity types**  

| Entity type | Category | Description | 
| --- | --- | --- | 
| ALL | All | Redact or identify all PII types listed in this table. | 
| ADDRESS | General | A physical address, such as '100 Main Street, Anytown, USA' or 'Suite \#12, Building 123'. | 
| AGE | General | An individual's age, including the quantity and unit of time. | 
| NAME | General | An individual's name. Does not include titles such as Dr., Mr., Mrs., or Miss. | 
| EMAIL | General | An email address, such as marymajor@example.com. | 
| PHONE | General | A phone number. Also includes fax and pager numbers. | 
| USERNAME | General | A user name that identifies an account, such as a login name, screen name, nick name, or handle. | 
| PASSWORD | General | An alphanumeric string that is used as a password. | 
| DRIVER\_ID | General | The number assigned to a driver's license. | 
| LICENSE\_PLATE | General | A license plate for a vehicle issued by the state or country where the vehicle is registered. | 
| VEHICLE\_IDENTIFICATION\_NUMBER | General | A Vehicle Identification Number (VIN) that uniquely identifies a vehicle. | 
| CREDIT\_DEBIT\_CARD\_CVV | Finance | A three-digit card verification code (CVV) for VISA, MasterCard, and Discover cards, or four-digit for American Express. | 
| CREDIT\_DEBIT\_CARD\_EXPIRY | Finance | The expiration date for a credit or debit card. | 
| CREDIT\_DEBIT\_CARD\_NUMBER | Finance | The number for a credit or debit card. | 
| PIN | Finance | A four-digit personal identification number (PIN). | 
| INTERNATIONAL\_BANK\_ACCOUNT\_NUMBER | Finance | An International Bank Account Number with specific formats for each country. | 
| SWIFT\_CODE | Finance | A SWIFT code - standard format of Bank Identifier Code (BIC). | 
| IP\_ADDRESS | IT | An IPv4 address, such as 198.51.100.0. | 
| MAC\_ADDRESS | IT | A media access control (MAC) address - unique identifier for a network interface controller. | 
| URL | IT | A web address, such as www.example.com. | 
| AWS\_ACCESS\_KEY | IT | A unique identifier associated with an AWS secret access key. | 
| AWS\_SECRET\_KEY | IT | A unique identifier associated with an AWS access key for signing programmatic requests. | 
| US\_BANK\_ACCOUNT\_NUMBER | USA | A US bank account number, typically 10 to 12 digits long. | 
| US\_BANK\_ROUTING\_NUMBER | USA | A US bank account routing number, typically nine digits long. | 
| US\_INDIVIDUAL\_TAX\_IDENTIFICATION\_NUMBER | USA | A US Individual Taxpayer Identification Number (ITIN). | 
| US\_PASSPORT\_NUMBER | USA | A US passport number, ranging from six to nine alphanumeric characters. | 
| US\_SOCIAL\_SECURITY\_NUMBER | USA | A US Social Security Number (SSN) - a nine-digit number for US citizens and residents. | 
| CA\_HEALTH\_NUMBER | Canada | A Canadian Health Service Number - a 10-digit unique identifier for healthcare benefits. | 
| CA\_SOCIAL\_INSURANCE\_NUMBER | Canada | A Canadian Social Insurance Number (SIN) - a nine-digit unique identifier. | 
| UK\_NATIONAL\_HEALTH\_SERVICE\_NUMBER | UK | A UK National Health Service Number - a 10-17 digit number. | 
| UK\_NATIONAL\_INSURANCE\_NUMBER | UK | A UK National Insurance Number (NINO) for accessing National Insurance benefits. | 
| UK\_UNIQUE\_TAXPAYER\_REFERENCE\_NUMBER | UK | A UK Unique Taxpayer Reference (UTR) - a 10-digit number identifying a taxpayer or business. | 