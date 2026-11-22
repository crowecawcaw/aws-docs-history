

# Supported sensitive data entity types

When you configure sensitive data detection, `PiiEntitiesConfiguration.PiiEntityTypes` controls which entity types Amazon Textract Insights acts on. You can pass `ALL` to act on every supported type, or a list of specific type names. For how detection and redaction work, see [Detecting and redacting sensitive data](insights-detecting-redacting.md).

## Requesting entity types
<a name="insights-requesting-entity-types"></a>

Set `PiiEntityTypes` to one of:
+ `ALL` — detect and (if redaction is enabled) mask every supported entity type.
+ A list of specific type names — act only on those types.

```json
"PiiEntitiesConfiguration": {
  "PiiEntityTypes": ["US_SOCIAL_SECURITY_NUMBER", "NAME", "ADDRESS"],
  "RedactionMaskMode": "ENTITY_TYPE"
}
```

Passing a specific list rather than `ALL` reduces the chance of over-masking form boilerplate and labels that resemble sensitive values.

## Entity types
<a name="insights-entity-types"></a>

Pass `ALL`, or a list of 1 to 32 of the following values. Use these spellings exactly.


**General**  

| **Entity type** | **Description** | 
| --- | --- | 
| `ADDRESS` | A physical address, such as a street address, city, state, or ZIP code. | 
| `AGE` | An individual's age. | 
| `NAME` | An individual's name. | 
| `EMAIL` | An email address. | 
| `PHONE` | A phone number. | 
| `USERNAME` | A user name that identifies an account. | 
| `PASSWORD` | A password. | 
| `DRIVER_ID` | A driver's license number. | 
| `LICENSE_PLATE` | A vehicle license plate number. | 
| `VEHICLE_IDENTIFICATION_NUMBER` | A vehicle identification number (VIN). | 


**Finance**  

| **Entity type** | **Description** | 
| --- | --- | 
| `CREDIT_DEBIT_CARD_CVV` | A card verification value (CVV). | 
| `CREDIT_DEBIT_CARD_EXPIRY` | A card expiration date. | 
| `CREDIT_DEBIT_CARD_NUMBER` | A credit or debit card number. | 
| `PIN` | A personal identification number. | 
| `INTERNATIONAL_BANK_ACCOUNT_NUMBER` | An international bank account number (IBAN). | 
| `SWIFT_CODE` | A SWIFT/BIC bank identifier code. | 


**IT**  

| **Entity type** | **Description** | 
| --- | --- | 
| `IP_ADDRESS` | An IPv4 or IPv6 address. | 
| `MAC_ADDRESS` | A network interface MAC address. | 
| `URL` | A web address. | 
| `AWS_ACCESS_KEY` | An AWS access key ID. | 
| `AWS_SECRET_KEY` | An AWS secret access key. | 


**US-specific**  

| **Entity type** | **Description** | 
| --- | --- | 
| `US_BANK_ACCOUNT_NUMBER` | A US bank account number. | 
| `US_BANK_ROUTING_NUMBER` | A US bank routing number. | 
| `US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER` | A US Individual Taxpayer Identification Number (ITIN). | 
| `US_PASSPORT_NUMBER` | A US passport number. | 
| `US_SOCIAL_SECURITY_NUMBER` | A US Social Security number (SSN). | 


**Canada-specific**  

| **Entity type** | **Description** | 
| --- | --- | 
| `CA_HEALTH_NUMBER` | A Canadian health service number. | 
| `CA_SOCIAL_INSURANCE_NUMBER` | A Canadian Social Insurance Number (SIN). | 


**UK-specific**  

| **Entity type** | **Description** | 
| --- | --- | 
| `UK_NATIONAL_HEALTH_SERVICE_NUMBER` | A UK National Health Service (NHS) number. | 
| `UK_NATIONAL_INSURANCE_NUMBER` | A UK National Insurance number. | 
| `UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER` | A UK Unique Taxpayer Reference (UTR) number. | 

## Mask tokens
<a name="insights-mask-tokens"></a>

When redaction is enabled with `RedactionMaskMode` set to `ENTITY_TYPE`, each masked span is replaced with its type label in brackets — for example [NAME], [ADDRESS], [EMAIL], [PHONE], and [URL]. With `RedactionMaskMode` set to `PII`, spans are replaced with a single generic marker regardless of type.