# Creating keys

You can create AWS Payment Cryptography keys using the **CreateKey** API operation.
When you create a key, you specify attributes such as the key algorithm, key usage,
permitted operations, and whether it's exportable. You can't change these properties
after you create the AWS Payment Cryptography key.

###### Note

If Multi-Region key replication is enabled for your AWS account and you create an Payment Cryptography key,
this key will automatically become a [Primary Region key
(PRK)](terminology.md#term.prk "terminology.md#term.prk"). PRK is replicated even if you don't specify the
`--replication-regions` parameter in the **CreateKey**
command. For more information, see [How Multi-Region key replication works](keys-multi-region-replication.md#how-mrr-works "keys-multi-region-replication.md#how-mrr-works").

###### Examples

- [Creating a 3KEY TDES base derivation
  key](#3des-deriv-mrr-example "#3des-deriv-mrr-example")
- [Creating a 2KEY TDES key for CVV/CVV2](#cvvkey-example "#cvvkey-example")
- [Creating an HMAC key](#hmac-example "#hmac-example")
- [Creating an AES-256 key](#aes-example "#aes-example")
- [Creating a PIN Encryption Key (PEK)](#pekkey-example "#pekkey-example")
- [Creating an asymmetric (RSA) key](#asymmetrickey-example "#asymmetrickey-example")
- [Creating a PIN Verification Value (PVV) Key](#pvv-example "#pvv-example")
- [Creating an asymmetric ECC key](#ECDH-example "#ECDH-example")

## Creating a 3KEY TDES base derivation

key

This command creates creates a 3KEY TDES derivation key that will be
[replicated](keys-multi-region-replication.md#how-mrr-works "keys-multi-region-replication.md#how-mrr-works") to US East (Ohio) and US West (Oregon) regions.
The response includes the reques parameters, an Amazon Resource Name (ARN) for
subsequent calls, and a Key Check Value (KCV).

```
`$` `aws payment-cryptography create-key --exportable --key-attributes \
 "KeyUsage=TR31_B0_BASE_DERIVATION_KEY, \
 KeyClass=SYMMETRIC_KEY,KeyAlgorithm=TDES_3KEY, \
 KeyModesOfUse={NoRestrictions=true}" \
 --replication-regions us-east-2 --region us-west-2`
```

Example output:

```
{
    "Key": {
        "CreateTimestamp": "2022-10-26T16:04:11.642000-07:00",
        "Enabled": true,
        "Exportable": true,
        "KeyArn": "FE23D3",
        "KeyAttributes": {
            "KeyAlgorithm": "TDES_3KEY",
            "KeyClass": "SYMMETRIC_KEY",
            "KeyModesOfUse": {
                "Decrypt": false,
                "DeriveKey": true,
                "Encrypt": false,
                "Generate": false,
                "NoRestrictions": false,
                "Sign": false,
                "Unwrap": false,
                "Verify": true,
                "Wrap": false
            },
            "KeyUsage": "TR31_B0_BASE_DERIVATION_KEY"
        },
        "KeyCheckValue": "FE23D3",
        "KeyCheckValueAlgorithm": "ANSI_X9_24",
        "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
        "KeyState": "CREATE_COMPLETE",
        "UsageStartTimestamp": "2022-10-26T16:04:11.559000-07:00"
}
```

## Creating a 2KEY TDES key for CVV/CVV2

This command creates a 2KEY TDES key for generating and verifying CVV/CVV2
values. The response includes the request parameters, an Amazon Resource Name
(ARN) for subsequent calls, and a Key Check Value (KCV).

```
`$` `aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=TDES_2KEY, \
 KeyUsage=TR31_C0_CARD_VERIFICATION_KEY,KeyClass=SYMMETRIC_KEY, \
 KeyModesOfUse='{Generate=true,Verify=true}'`
```

Example output:

```
{
    "Key": {
        "CreateTimestamp": "2022-10-26T16:04:11.642000-07:00",
        "Enabled": true,
        "Exportable": true,
        "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/7f7g4spf3xcklhzu",
        "KeyAttributes": {
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
            "KeyUsage": "TR31_C0_CARD_VERIFICATION_KEY"
        },
        "KeyCheckValue": "AEA5CD",
        "KeyCheckValueAlgorithm": "ANSI_X9_24",
        "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
        "KeyState": "CREATE_COMPLETE",
        "UsageStartTimestamp": "2022-10-26T16:04:11.559000-07:00"
    }
}
```

## Creating an HMAC key

HMAC keys are used for generating or verifying hash message authentication codes (HMAC). With HMAC keys,
the hash type is assigned at the time of key creation (such as HMAC_SHA224 and HMAC_SHA512) and cannot be modified.

```
`$` `aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=HMAC_SHA512,KeyUsage=TR31_M7_HMAC_KEY,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{Generate = true,Verify = true}'`
```

Example output:

```
{
 "Key": {
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/qnobl5lghrzunce6",
 "KeyAttributes": {
 "KeyUsage": "TR31_M7_HMAC_KEY",
 "KeyClass": "SYMMETRIC_KEY",
 "KeyAlgorithm": "HMAC_SHA512",
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
 "KeyCheckValue": "2976E7",
 "KeyCheckValueAlgorithm": "HMAC",
 "Enabled": true,
 "Exportable": true,
 "KeyState": "CREATE_COMPLETE",
 "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
 "CreateTimestamp": "2025-07-30T10:06:12.142000-07:00",
 "UsageStartTimestamp": "2025-07-30T10:06:12.128000-07:00"
 }
}
```

## Creating an AES-256 key

This command creates an AES-256 symmetric key for data encryption and decryption.
AES keys provide strong encryption for sensitive data and are commonly used in payment processing
for encrypting cardholder data and other sensitive information, however TDES is more commonly used for issuer use cases like EMV.

```
`$` `aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=AES_256,KeyUsage=TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{Encrypt=true,Decrypt=true,Wrap=true,Unwrap=true}'`
```

Example output:

```
{
    "Key": {
        "CreateTimestamp": "2025-02-02T10:15:30.142000-08:00",
        "Enabled": true,
        "Exportable": true,
        "KeyArn": "arn:aws:payment-cryptography:us-east-1:111122223333:key/kwapwa6qaifllw2h",
        "KeyAttributes": {
            "KeyAlgorithm": "AES_256",
            "KeyClass": "SYMMETRIC_KEY",
            "KeyModesOfUse": {
                "Decrypt": true,
                "DeriveKey": false,
                "Encrypt": true,
                "Generate": false,
                "NoRestrictions": false,
                "Sign": false,
                "Unwrap": true,
                "Verify": false,
                "Wrap": true
            },
            "KeyUsage": "TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY"
        },
        "KeyCheckValue": "2976F5",
        "KeyCheckValueAlgorithm": "CMAC",
        "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
        "KeyState": "CREATE_COMPLETE",
        "UsageStartTimestamp": "2025-02-02T10:15:30.128000-08:00"
    }
}
```

## Creating a PIN Encryption Key (PEK)

This command creates a 3KEY TDES key for encrypting PIN values although pin keys can also be AES depending
on your need for interoperability. You can use
this key to securely store PINs or decrypt PINs during verification, such as in
a transaction. The response includes the request parameters, an ARN for
subsequent calls, and a KCV.

```
`$` `aws payment-cryptography create-key --exportable --key-attributes \
 KeyAlgorithm=TDES_3KEY,KeyUsage=TR31_P0_PIN_ENCRYPTION_KEY, \
 KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{Encrypt=true,Decrypt=true,Wrap=true,Unwrap=true}'`
```

Example output:

```
{
    "Key": {
        "CreateTimestamp": "2022-10-27T08:27:51.795000-07:00",
        "Enabled": true,
        "Exportable": true,
        "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt",
        "KeyAttributes": {
            "KeyAlgorithm": "TDES_3KEY",
            "KeyClass": "SYMMETRIC_KEY",
            "KeyModesOfUse": {
                "Decrypt": true,
                "DeriveKey": false,
                "Encrypt": true,
                "Generate": false,
                "NoRestrictions": false,
                "Sign": false,
                "Unwrap": true,
                "Verify": false,
                "Wrap": true
            },
            "KeyUsage": "TR31_P0_PIN_ENCRYPTION_KEY"
        },
        "KeyCheckValue": "7CC9E2",
        "KeyCheckValueAlgorithm": "ANSI_X9_24",
        "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
        "KeyState": "CREATE_COMPLETE",
        "UsageStartTimestamp": "2022-10-27T08:27:51.753000-07:00"
    }
}
```

## Creating an asymmetric (RSA) key

This command generates a new asymmetric RSA 2048-bit key pair. It creates a
new private key and its matching public key. You can retrieve the public key
using the [getPublicCertificate](keys.md "keys.md") API.

```
`$` `aws payment-cryptography create-key --exportable \
 --key-attributes KeyAlgorithm=RSA_2048,KeyUsage=TR31_D1_ASYMMETRIC_KEY_FOR_DATA_ENCRYPTION, \
 KeyClass=ASYMMETRIC_KEY_PAIR,KeyModesOfUse='{Encrypt=true, Decrypt=True,Wrap=True,Unwrap=True}'`
```

Example output:

```
{
    "Key": {
        "CreateTimestamp": "2022-11-15T11:15:42.358000-08:00",
        "Enabled": true,
        "Exportable": true,
        "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/nsq2i3mbg6sn775f",
        "KeyAttributes": {
            "KeyAlgorithm": "RSA_2048",
            "KeyClass": "ASYMMETRIC_KEY_PAIR",
            "KeyModesOfUse": {
                "Decrypt": true,
                "DeriveKey": false,
                "Encrypt": true,
                "Generate": false,
                "NoRestrictions": false,
                "Sign": false,
                "Unwrap": true,
                "Verify": false,
                "Wrap": true
            },
            "KeyUsage": "TR31_D1_ASYMMETRIC_KEY_FOR_DATA_ENCRYPTION"
        },
        "KeyCheckValue": "40AD487F",
        "KeyCheckValueAlgorithm": "SHA-1",
        "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
        "KeyState": "CREATE_COMPLETE",
        "UsageStartTimestamp": "2022-11-15T11:15:42.182000-08:00"
    }
}
```

## Creating a PIN Verification Value (PVV) Key

This command creates a 3KEY TDES key for generating PVV values. You can use
this key to generate a PVV that can be compared against a subsequently
calculated PVV. The response includes the request parameters, an ARN for
subsequent calls, and a KCV.

```
`$` `aws payment-cryptography create-key --exportable \
 --key-attributes KeyAlgorithm=TDES_3KEY,KeyUsage=TR31_V2_VISA_PIN_VERIFICATION_KEY, \
 KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{Generate=true,Verify=true}'`
```

Example output:

```
{
    "Key": {
        "CreateTimestamp": "2022-10-27T10:22:59.668000-07:00",
        "Enabled": true,
        "Exportable": true,
        "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2",
        "KeyAttributes": {
            "KeyAlgorithm": "TDES_3KEY",
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
            "KeyUsage": "TR31_V2_VISA_PIN_VERIFICATION_KEY"
        },
        "KeyCheckValue": "7F2363",
        "KeyCheckValueAlgorithm": "ANSI_X9_24",
        "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
        "KeyState": "CREATE_COMPLETE",
        "UsageStartTimestamp": "2022-10-27T10:22:59.614000-07:00"
    }
}
```

## Creating an asymmetric ECC key

This command generates an ECC key pair for establishing an ECDH (Elliptic
Curve Diffie-Hellman) key agreement between two parties. With ECDH, each party
generates its own ECC key pair with key purpose K3 and mode of use X, and they
exchange public keys. Both parties then use their private key and the received
public key to establish a shared derived key.

To maintain the single-use principle of cryptographic keys in payments, we
recommend not reusing ECC key pairs for multiple purposes, such as ECDH key
derivation and signing.

```
`$` `aws payment-cryptography create-key --exportable \
 --key-attributes KeyAlgorithm=ECC_NIST_P256,KeyUsage=TR31_K3_ASYMMETRIC_KEY_FOR_KEY_AGREEMENT, \
 KeyClass=ASYMMETRIC_KEY_PAIR,KeyModesOfUse='{DeriveKey=true}'`
```

Example output:

```
{
    "Key": {
        "CreateTimestamp": "2024-10-17T01:31:55.908000+00:00",
        "Enabled": true,
        "Exportable": true,
        "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/wc3rjsssguhxtilv",
        "KeyAttributes": {
            "KeyAlgorithm": "ECC_NIST_P256",
            "KeyClass": "ASYMMETRIC_KEY_PAIR",
            "KeyModesOfUse": {
                "Decrypt": false,
                "DeriveKey": true,
                "Encrypt": false,
                "Generate": false,
                "NoRestrictions": false,
                "Sign": false,
                "Unwrap": false,
                "Verify": false,
                "Wrap": false
            },
            "KeyUsage": "TR31_K3_ASYMMETRIC_KEY_FOR_KEY_AGREEMENT"
        },
        "KeyCheckValue": "7E34F19F",
        "KeyCheckValueAlgorithm": "SHA-1",
        "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
        "KeyState": "CREATE_COMPLETE",
        "UsageStartTimestamp": "2024-10-17T01:31:55.866000+00:00"
    }
}
```
