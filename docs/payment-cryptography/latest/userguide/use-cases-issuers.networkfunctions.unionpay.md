

# UnionPay specific functions
<a name="use-cases-issuers.networkfunctions.unionpay"></a>

The following examples pertain to UnionPay International (UPI), also sometimes referred to as China UnionPay (CUP).

**Topics**
+ [ARQC Validation](#use-cases-issuers.networkfunctions.unionpay.arqc)
+ [CVN2 (Card Verification Number)](#use-cases-issuers.networkfunctions.unionpay.cvn2)
+ [AVN (Authentication Verification Number)](#use-cases-issuers.networkfunctions.unionpay.avn)

## ARQC Validation
<a name="use-cases-issuers.networkfunctions.unionpay.arqc"></a>

UnionPay ARQC validation uses the EMV\_OPTION\_A key derivation mode. The session key is derived from the PrimaryAccountNumber, PAN Sequence Number, and Application Transaction Counter using a UnionPay-specific scheme. For information about the transaction data format and field ordering, see the scheme documentation.

### Validate the ARQC
<a name="use-cases-issuers.networkfunctions.unionpay.arqc.validation"></a>

**Example Validate an ARQC using UnionPay key derivation**  
This example shows how to validate an ARQC generated using UnionPay key derivation.  
If AWS Payment Cryptography validates the ARQC, it returns an HTTP 200 response. If the ARQC fails validation, AWS Payment Cryptography returns an HTTP 400 response with a reason code.  

```
$ aws payment-cryptography-data verify-auth-request-cryptogram --auth-request-cryptogram A12345B1A12345B1 \
  --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk \
  --major-key-derivation-mode EMV_OPTION_A \
  --transaction-data 123456789ABCDEF80000000000000000 \
  --session-key-derivation-attributes='UnionPay={PrimaryAccountNumber=4123412341234123,PanSequenceNumber=01,ApplicationTransactionCounter=123D}'
```

```
{
    "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk",
    "KeyCheckValue": "08D7B4"
}
```
If the ARQC cannot be validated, AWS Payment Cryptography returns an error response:  

```
An error occurred (VerificationFailedException) when calling the VerifyAuthRequestCryptogram operation: Auth request cryptogram verification failed.

Reason: INVALID_AUTH_REQUEST_CRYPTOGRAM
```

## CVN2 (Card Verification Number)
<a name="use-cases-issuers.networkfunctions.unionpay.cvn2"></a>

CVN2 is the UnionPay equivalent of CVV2. It is a card verification number used for online and card-not-present transactions. Cryptographically, CVN2 uses the same algorithm as CVV2 ([CardVerificationValue2](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardVerificationValue2.html)). The inputs are the Primary Account Number (PAN) and the card expiry date (4 digits in MMYY format).

### Create the key
<a name="use-cases-issuers.networkfunctions.unionpay.cvn2.setup"></a>

To create a CVN2 key, use the `create-key` command with the `TR31_C0_CARD_VERIFICATION_KEY` usage and `TDES_2KEY` algorithm.

```
$ aws payment-cryptography create-key --exportable \
  --key-attributes KeyAlgorithm=TDES_2KEY,KeyUsage=TR31_C0_CARD_VERIFICATION_KEY,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{Generate=true,Verify=true}' \
  --tags='[{"Key":"KEY_PURPOSE","Value":"CVN2"},{"Key":"CARD_BIN","Value":"47613499"}]'
```

The response echoes back the request parameters, including an ARN for subsequent calls and a Key Check Value (KCV).

```
{
    "Key": {
        "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/7f7g4spf3xcklhzu",
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
        "KeyCheckValue": "AEA5CD",
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

Take note of the `KeyArn` value, for example *arn:aws:payment-cryptography:us-east-2:111122223333:key/7f7g4spf3xcklhzu*. You need this in the following steps.

### Generate a CVN2
<a name="use-cases-issuers.networkfunctions.unionpay.cvn2.generate"></a>

**Example Generate a CVN2 for a given PAN**  
This example generates a CVN2 for a given PAN with inputs of `PAN` and card expiry date.  
For all available parameters, see [CardVerificationValue2](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardVerificationValue2.html) in the API reference guide.  

```
$ aws payment-cryptography-data generate-card-validation-data \
  --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/7f7g4spf3xcklhzu \
  --primary-account-number=4761349999991234 \
  --generation-attributes CardVerificationValue2='{CardExpiryDate=1226}'
```

```
{
    "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/7f7g4spf3xcklhzu",
    "KeyCheckValue": "AEA5CD",
    "ValidationData": "321"
}
```

### Validate a CVN2
<a name="use-cases-issuers.networkfunctions.unionpay.cvn2.verify"></a>

**Example Validate a CVN2 for a given PAN**  
This example validates a CVN2 for a given PAN with inputs of `PAN`, card expiry date, and the CVN2 provided during the transaction.  
For all available parameters, see [CardVerificationValue2](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardVerificationValue2.html) in the API reference guide.  
CVN2 is a user-entered value. Periodic validation failures do not necessarily indicate an issue.

```
$ aws payment-cryptography-data verify-card-validation-data \
  --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/7f7g4spf3xcklhzu \
  --primary-account-number=4761349999991234 \
  --verification-attributes CardVerificationValue2='{CardExpiryDate=1226}' \
  --validation-data 321
```

```
{
    "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/7f7g4spf3xcklhzu",
    "KeyCheckValue": "AEA5CD"
}
```

## AVN (Authentication Verification Number)
<a name="use-cases-issuers.networkfunctions.unionpay.avn"></a>

AVN (Authentication Verification Number) is the UnionPay 3DS cryptogram. It uses the CVV algorithm ([CardVerificationValue1](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardVerificationValue1.html)) with repurposed input fields such as below but check the scheme documentation for finalized details.
+ *PAN* — Primary Account Number (16-19 digits, from the AReq)
+ *CardExpiryDate* — The four least significant digits of a value derived from the DS Transaction ID (dsTransID)
+ *ServiceCode* — 3 digits: Authentication Transaction Result (1 digit) \+ filling bit '0' (1 digit) \+ AV generator indicator (1 digit)

### Create the key
<a name="use-cases-issuers.networkfunctions.unionpay.avn.setup"></a>

To create an AVN key, use the `create-key` command with the `TR31_C0_CARD_VERIFICATION_KEY` usage and `TDES_2KEY` algorithm.

```
$ aws payment-cryptography create-key --exportable \
  --key-attributes KeyAlgorithm=TDES_2KEY,KeyUsage=TR31_C0_CARD_VERIFICATION_KEY,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{Generate=true,Verify=true}' \
  --tags='[{"Key":"KEY_PURPOSE","Value":"AVN"},{"Key":"CARD_BIN","Value":"47613499"}]'
```

The response echoes back the request parameters, including an ARN for subsequent calls and a Key Check Value (KCV).

```
{
    "Key": {
        "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/dnaeyrjgdjjtw6dk",
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
        "KeyCheckValue": "F3FB13",
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

Take note of the `KeyArn` value, for example *arn:aws:payment-cryptography:us-east-2:111122223333:key/dnaeyrjgdjjtw6dk*. You need this in the following steps.

### Generate an AVN
<a name="use-cases-issuers.networkfunctions.unionpay.avn.generate"></a>

**Example Generate an AVN for a given PAN**  
This example generates an AVN for a given PAN. The `CardExpiryDate` field contains the four least significant digits derived from the dsTransID. The `ServiceCode` field contains the authentication result, filling bit, and generator indicator.  
For all available parameters, see [CardVerificationValue1](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardVerificationValue1.html) in the API reference guide.  

```
$ aws payment-cryptography-data generate-card-validation-data \
  --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/dnaeyrjgdjjtw6dk \
  --primary-account-number=4761349999991234 \
  --generation-attributes CardVerificationValue1='{CardExpiryDate=9431,ServiceCode=201}'
```

```
{
    "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/dnaeyrjgdjjtw6dk",
    "KeyCheckValue": "F3FB13",
    "ValidationData": "491"
}
```

### Validate an AVN
<a name="use-cases-issuers.networkfunctions.unionpay.avn.verify"></a>

**Example Validate an AVN for a given PAN**  
This example validates an AVN for a given PAN using the same input fields that generated it, along with the AVN value to verify.  
For all available parameters, see [CardVerificationValue1](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardVerificationValue1.html) in the API reference guide.  

```
$ aws payment-cryptography-data verify-card-validation-data \
  --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/dnaeyrjgdjjtw6dk \
  --primary-account-number=4761349999991234 \
  --verification-attributes CardVerificationValue1='{CardExpiryDate=9431,ServiceCode=201}' \
  --validation-data 491
```

```
{
    "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/dnaeyrjgdjjtw6dk",
    "KeyCheckValue": "F3FB13"
}
```