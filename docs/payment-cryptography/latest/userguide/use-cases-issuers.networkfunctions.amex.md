

# American Express specific functions
<a name="use-cases-issuers.networkfunctions.amex"></a>

**Topics**
+ [CSC1](#use-cases-issuers.networkfunctions.amex.csc)
+ [CSC2](#use-cases-issuers.networkfunctions.amex.csc2)
+ [iCSC](#use-cases-issuers.networkfunctions.amex.csc3)
+ [3DS AEVV](#use-cases-issuers.networkfunctions.amex.3dsaevv)

## CSC1
<a name="use-cases-issuers.networkfunctions.amex.csc"></a>

CSC Version 1 is also known as the Classic CSC Algorithm. The service can provide it as a 3,4 or 5 digit number.

For all available parameters see [AmexCardSecurityCodeVersion1](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_AmexCardSecurityCodeVersion1.html) in the API reference guide. 

### Create key
<a name="use-cases-issuers.networkfunctions.amex.csc.setup"></a>

```
$ aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=TDES_2KEY,KeyUsage=TR31_C0_CARD_VERIFICATION_KEY,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{Generate=true,Verify=true}' --tags='[{"Key":"KEY_PURPOSE","Value":"CSC1"},{"Key":"CARD_BIN","Value":"12345678"}]'
```

The response echoes back the request parameters, including an ARN for subsequent calls as well as a Key Check Value (KCV).

```
{
                "Key": {
                    "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/esh6hn7pxdtttzgq",
                    "KeyAttributes": {
                        "KeyUsage": "TR31_C0_CARD_VERIFICATION_KEY",
                        "KeyClass": "SYMMETRIC_KEY",
                        "KeyAlgorithm": "TDES_2KEY",
                        "KeyModesOfUse": {
                            "Encrypt": false,
                            "Decrypt": false,
                            "Wrap": false,
                            "Unwrap": false,
                            "Generate": true,
                            "Sign": false,
                            "Verify": true,
                            "DeriveKey": false,
                            "NoRestrictions": false
                        }
                    },
                    "KeyCheckValue": "8B5077",
                    "KeyCheckValueAlgorithm": "ANSI_X9_24",
                    "Enabled": true,
                    "Exportable": true,
                    "KeyState": "CREATE_COMPLETE",
                    "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
                    "CreateTimestamp": "2023-06-05T06:41:46.648000-07:00",
                    "UsageStartTimestamp": "2023-06-05T06:41:46.626000-07:00"
                }
            }
```

Take note of the `KeyArn` that represents the key, for example *arn:aws:payment-cryptography:us-east-2:111122223333:key/esh6hn7pxdtttzgq*. You need that in the next step.

### Generate a CSC1
<a name="use-cases-issuers.networkfunctions.amex.csc1.generate"></a>

**Example**  

```
$ aws payment-cryptography-data generate-card-validation-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/esh6hn7pxdtttzgq --primary-account-number=344131234567848 --generation-attributes AmexCardSecurityCodeVersion1='{CardExpiryDate=1224}' --validation-data-length 4
```

```
{
    "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/esh6hn7pxdtttzgq",
    "KeyCheckValue": "8B5077",
    "ValidationData": "3938"
  }
```

### Validate the CSC1
<a name="use-cases-issuers.networkfunctions.amex.csc1.validation"></a>

**Example**  
In this example, we will validate a CSC1.   
If AWS Payment Cryptography is able to validate, an http/200 is returned. If the value is not validated, it will return a http/400 response.  

```
$ aws payment-cryptography-data verify-card-validation-data  --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/esh6hn7pxdtttzgq --primary-account-number=344131234567848 --verification-attributes AmexCardSecurityCodeVersion1='{CardExpiryDate=1224}''  --validation-data 3938
```

```
{
    "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/esh6hn7pxdtttzgq",
    "KeyCheckValue": "8B5077"
  }
```

## CSC2
<a name="use-cases-issuers.networkfunctions.amex.csc2"></a>

CSC Version 2 is also known as the Enhanced CSC Algorithm. The service can provide it as a 3,4 or 5 digit number. The service code for CSC2 is typically 000.

For all available parameters see [AmexCardSecurityCodeVersion2](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_AmexCardSecurityCodeVersion2.html) in the API reference guide. 

### Create key
<a name="use-cases-issuers.networkfunctions.amex.csc2.setup"></a>

```
$ aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=TDES_2KEY,KeyUsage=TR31_C0_CARD_VERIFICATION_KEY,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{Generate=true,Verify=true}' --tags='[{"Key":"KEY_PURPOSE","Value":"CSC2"},{"Key":"CARD_BIN","Value":"12345678"}]'
```

The response echoes back the request parameters, including an ARN for subsequent calls as well as a Key Check Value (KCV).

```
{
            "Key": {
                "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/erlm445qvunmvoda",
                "KeyAttributes": {
                    "KeyUsage": "TR31_C0_CARD_VERIFICATION_KEY",
                    "KeyClass": "SYMMETRIC_KEY",
                    "KeyAlgorithm": "TDES_2KEY",
                    "KeyModesOfUse": {
                        "Encrypt": false,
                        "Decrypt": false,
                        "Wrap": false,
                        "Unwrap": false,
                        "Generate": true,
                        "Sign": false,
                        "Verify": true,
                        "DeriveKey": false,
                        "NoRestrictions": false
                    }
                },
                "KeyCheckValue": "BF1077",
                "KeyCheckValueAlgorithm": "ANSI_X9_24",
                "Enabled": true,
                "Exportable": true,
                "KeyState": "CREATE_COMPLETE",
                "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
                "CreateTimestamp": "2023-06-05T06:41:46.648000-07:00",
                "UsageStartTimestamp": "2023-06-05T06:41:46.626000-07:00"
            }
        }
```

Take note of the `KeyArn` that represents the key, for example *arn:aws:payment-cryptography:us-east-2:111122223333:key/erlm445qvunmvoda*. You need that in the next step.

### Generate a CSC2
<a name="use-cases-issuers.networkfunctions.amex.csc2.generate"></a>

In this example, we will generate a CSC2 with a length of 4. CSC can be generated with a length of 3,4 or 5. For American Express, PANs should be 15 digits and start with 34 or 37. Expiration date is typically formatted as YYMM. Service code may vary - review your manual but typical values are 000, 201 or 702

**Example**  

```
$ aws payment-cryptography-data generate-card-validation-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/erlm445qvunmvoda --primary-account-number=344131234567848 --generation-attributes AmexCardSecurityCodeVersion2='{CardExpiryDate=2412,ServiceCode=000}' --validation-data-length 4
```

```
{
"KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/erlm445qvunmvoda",
"KeyCheckValue": "BF1077",
"ValidationData": "3982"
}
```

### Validate the CSC2
<a name="use-cases-issuers.networkfunctions.amex.csc2.validation"></a>

**Example**  
In this example, we will validate a CSC2.   
If AWS Payment Cryptography is able to validate, an http/200 is returned. If the value is not validated, it will return a http/400 response.  

```
$ aws payment-cryptography-data verify-card-validation-data  --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/erlm445qvunmvoda --primary-account-number=344131234567848 --verification-attributes AmexCardSecurityCodeVersion2='{CardExpiryDate=2412,ServiceCode=000}' --validation-data 3982
```

```
{
"KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/erlm445qvunmvoda",
"KeyCheckValue": "BF1077"
}
```

## iCSC
<a name="use-cases-issuers.networkfunctions.amex.csc3"></a>

iCSC is also known as a static CSC Algorithm and is calculated using CSC Version 2. The service can provide it as a 3,4 or 5 digit number.

Use service code 999 to calculate iCSC for a contact card. Use service code 702 to calculate iCSC for a contactless card. 

For all available parameters see [AmexCardSecurityCodeVersion2](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_AmexCardSecurityCodeVersion2.html) in the API reference guide. 

### Create key
<a name="use-cases-issuers.networkfunctions.amex.csc3.setup"></a>

```
$ aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=TDES_2KEY,KeyUsage=TR31_C0_CARD_VERIFICATION_KEY,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{Generate=true,Verify=true}' --tags='[{"Key":"KEY_PURPOSE","Value":"CSC1"},{"Key":"CARD_BIN","Value":"12345678"}]'
```

The response echoes back the request parameters, including an ARN for subsequent calls as well as a Key Check Value (KCV).

```
{
        "Key": {
        "KeyArn": "arn:aws:payment-cryptography:us-east-1:111122223333:key/7vrybrbvjcvwtunv",
        "KeyAttributes": {
            "KeyUsage": "TR31_C0_CARD_VERIFICATION_KEY"
            "KeyAlgorithm": "TDES_2KEY",
            "KeyClass": "SYMMETRIC_KEY",
            "KeyModesOfUse": {
                "Decrypt": false,
                "DeriveKey": false,
                "Encrypt": false,
                "Generate": true,
                "NoRestrictions": false,
                "Sign": false,
                "Unwrap": false,
                "Verify": true,
                "Wrap": false
            },
        },
        "KeyCheckValue": "7121C7",
        "KeyCheckValueAlgorithm": "ANSI_X9_24",
        "Enabled": true,
        "Exportable": true,
        "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
        "KeyState": "CREATE_COMPLETE",
        "CreateTimestamp": "2025-01-29T09:19:21.209000-05:00",
        "UsageStartTimestamp": "2025-01-29T09:19:21.192000-05:00"
        }
     }
```

Take note of the `KeyArn` that represents the key, for example *arn:aws:payment-cryptography:us-east-1:111122223333:key/7vrybrbvjcvwtunv*. You need that in the next step.

### Generate a iCSC
<a name="use-cases-issuers.networkfunctions.amex.icsc.generate"></a>

In this example, we will generate a iCSC with a length of 4, for a contactless card using service code 702. CSC can be generated with a length of 3,4 or 5. For American Express, PANs should be 15 digits and start with 34 or 37.

**Example**  

```
$ aws payment-cryptography-data generate-card-validation-data --key-identifier arn:aws:payment-cryptography:us-east-1:111122223333:key/7vrybrbvjcvwtunv --primary-account-number=344131234567848 --generation-attributes AmexCardSecurityCodeVersion2='{CardExpiryDate=1224,ServiceCode=702}' --validation-data-length 4
```

```
{
    "KeyArn": arn:aws:payment-cryptography:us-east-1:111122223333:key/7vrybrbvjcvwtunv,
    "KeyCheckValue": 7121C7,
    "ValidationData": "2365"
}
```

### Validate the iCSC
<a name="use-cases-issuers.networkfunctions.amex.icsc.validation"></a>

**Example**  
In this example, we will validate a iCSC.   
If AWS Payment Cryptography is able to validate, an http/200 is returned. If the value is not validated, it will return a http/400 response.  

```
$ aws payment-cryptography-data verify-card-validation-data  --key-identifier arn:aws:payment-cryptography:us-east-1:111122223333:key/7vrybrbvjcvwtunv --primary-account-number=344131234567848 --verification-attributes AmexCardSecurityCodeVersion2='{CardExpiryDate=1224,ServiceCode=702}' --validation-data 2365
```

```
{
    "KeyArn": arn:aws:payment-cryptography:us-east-1:111122223333:key/7vrybrbvjcvwtunv,
    "KeyCheckValue": 7121C7
}
```

## 3DS AEVV
<a name="use-cases-issuers.networkfunctions.amex.3dsaevv"></a>

3DS AEVV (3-D Secure Account Verification Value) is used for American Express 3-D Secure authentication. It uses the same algorithm as CSC2 but with different input parameters. The expiration date field should be populated with an unpredictable (random) number, and the service code consists of the AEVV Authentication Results Code (1 digit) plus the Second Factor Authentication Code (2 digits). The output length should be 3-digits.

For all available parameters see [AmexCardSecurityCodeVersion2](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_AmexCardSecurityCodeVersion2.html) in the API reference guide. 

### Create key
<a name="use-cases-issuers.networkfunctions.amex.3dsaevv.setup"></a>

```
$ aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=TDES_2KEY,KeyUsage=TR31_C0_CARD_VERIFICATION_KEY,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{Generate=true,Verify=true}' --tags='[{"Key":"KEY_PURPOSE","Value":"3DS_AEVV"},{"Key":"CARD_BIN","Value":"12345678"}]'
```

The response echoes back the request parameters, including an ARN for subsequent calls as well as a Key Check Value (KCV).

```
{
        "Key": {
        "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/kw8djn5qxvfh3ztm",
        "KeyAttributes": {
            "KeyUsage": "TR31_C0_CARD_VERIFICATION_KEY"
            "KeyAlgorithm": "TDES_2KEY",
            "KeyClass": "SYMMETRIC_KEY",
            "KeyModesOfUse": {
                "Decrypt": false,
                "DeriveKey": false,
                "Encrypt": false,
                "Generate": true,
                "NoRestrictions": false,
                "Sign": false,
                "Unwrap": false,
                "Verify": true,
                "Wrap": false
            },
        },
        "KeyCheckValue": "8F3A21",
        "KeyCheckValueAlgorithm": "ANSI_X9_24",
        "Enabled": true,
        "Exportable": true,
        "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
        "KeyState": "CREATE_COMPLETE",
        "CreateTimestamp": "2025-02-02T10:30:15.209000-05:00",
        "UsageStartTimestamp": "2025-02-02T10:30:15.192000-05:00"
        }
     }
```

Take note of the `KeyArn` that represents the key, for example *arn:aws:payment-cryptography:us-east-2:111122223333:key/kw8djn5qxvfh3ztm*. You need that in the next step.

### Generate a 3DS AEVV
<a name="use-cases-issuers.networkfunctions.amex.3dsaevv.generate"></a>

In this example, we will generate a 3DS AEVV with a length of 3. The expiration date field contains an unpredictable (random) number (e.g., 1234), and the service code consists of the AEVV Authentication Results Code (1 digit) plus the Second Factor Authentication Code (2 digits), for example 543 where 5 is the Authentication Results Code and 43 is the Second Factor Authentication Code. For American Express, PANs should be 15 digits and start with 34 or 37.

**Example**  

```
$ aws payment-cryptography-data generate-card-validation-data --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/kw8djn5qxvfh3ztm --primary-account-number=344131234567848 --generation-attributes AmexCardSecurityCodeVersion2='{CardExpiryDate=1234,ServiceCode=543}' --validation-data-length 3
```

```
{
    "KeyArn": arn:aws:payment-cryptography:us-east-2:111122223333:key/kw8djn5qxvfh3ztm,
    "KeyCheckValue": 8F3A21,
    "ValidationData": "921"
}
```

### Validate the 3DS AEVV
<a name="use-cases-issuers.networkfunctions.amex.3dsaevv.validation"></a>

**Example**  
In this example, we will validate a 3DS AEVV.   
If AWS Payment Cryptography is able to validate, an http/200 is returned. If the value is not validated, it will return a http/400 response.  

```
$ aws payment-cryptography-data verify-card-validation-data  --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/kw8djn5qxvfh3ztm --primary-account-number=344131234567848 --verification-attributes AmexCardSecurityCodeVersion2='{CardExpiryDate=1234,ServiceCode=543}' --validation-data 921
```

```
{
    "KeyArn": arn:aws:payment-cryptography:us-east-2:111122223333:key/kw8djn5qxvfh3ztm,
    "KeyCheckValue": 8F3A21
}
```