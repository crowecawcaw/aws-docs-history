

# User Managed PINs
<a name="use-cases-issuers.generalfunctions.usermanagedpins"></a>

**Topics**
+ [Overview](#use-cases-issuers.generalfunctions.usermanagedpins.overview)
+ [Create the keys](#use-cases-issuers.generalfunctions.usermanagedpins.setup)
+ [Set a user-selectable PIN](#use-cases-issuers.generalfunctions.usermanagedpins.setpin)
+ [Reset a PIN (green PIN)](#use-cases-issuers.generalfunctions.usermanagedpins.resetpin)
+ [Reveal a PIN](#use-cases-issuers.generalfunctions.usermanagedpins.revealpin)

## Overview
<a name="use-cases-issuers.generalfunctions.usermanagedpins.overview"></a>

AWS Payment Cryptography supports user managed (customer managed) PIN flows, in which a PIN is exchanged securely between a cardholder device and the service through your customer backend. The device and the service use Elliptic Curve Diffie-Hellman (ECDH) key agreement to derive a shared symmetric key on each side, and that key protects an ISO format 4 [PIN block](terminology.md#terms.pinblock). Because the key is derived rather than exchanged, the clear PIN and the clear PIN block are never transmitted beyond the device. 

These flows involve three parties. The cardholder device generates its EC key pair, derives the ECDH AES-128 key, encrypts or decrypts the ISO format 4 PIN block, and holds the clear PIN; it has no AWS credentials. The customer backend (your issuer or processor server) holds the AWS credentials, calls AWS Payment Cryptography, signs the device certificate, and stores the [PVV](terminology.md#terms.pvv). AWS Payment Cryptography performs the cryptographic operations. The device communicates only with the customer backend, and the customer backend makes all calls to AWS Payment Cryptography. 

This topic covers three flows:
+ *User-selectable PIN (Set PIN)* - the cardholder chooses their own PIN on the device.
+ *Green PIN (Reset PIN)* - the service generates a random PIN that is delivered to the cardholder, for example during first issuance or a forgotten-PIN reset.
+ *Reveal PIN* - an existing PIN block is returned to an authorized device for narrow use cases.

All three flows share the same key setup and the same ECDH device-agreement mechanics, described in [Create the keys](#use-cases-issuers.generalfunctions.usermanagedpins.setup). For the details of the key agreement itself, see [Import keys using asymmetric techniques (ECDH)](keys-import.md#keys-import-ecdh). 

**Note**  
These flows handle clear PINs and PIN blocks only on the device, never in transit to AWS Payment Cryptography. Review each flow carefully with your security team before you deploy it.

The following diagram shows the user managed PIN flows.

![Sequence diagram of the ECDH key agreement and the Set PIN, Reset PIN, and Reveal PIN flows.](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/images/usermanagedpins-ecdh-flows.png)


For a complete, runnable example of these flows using the AWS SDK for Python, see the [ECDH PIN set and reveal flows sample](https://github.com/aws-samples/samples-for-payment-cryptography-service/tree/main/python_sdk_example/ecdh_flows) in the AWS samples repository on GitHub.

**Note**  
The typical flow includes a cardholder device that performs the ECDH key agreement and encrypts or decrypts the ISO format 4 PIN block. If you already protect PINs between the device and your customer backend by another means, you can use a modified version of these flows directly between the customer backend and AWS Payment Cryptography. In that variant, the customer backend performs the ECDH key agreement and the PIN block operations in place of the device.

## Create the keys
<a name="use-cases-issuers.generalfunctions.usermanagedpins.setup"></a>

All three flows use the same set of keys: an ECDH agreement key for the key agreement with the device, a Pin Generation/Verification Key (PGK) to generate the [PVV](terminology.md#terms.pvv), and a [Pin Encryption Key](terminology.md#terms.pek) (PEK) that the PIN block is translated onto for backend storage. You also import the device certificate authority's (CA) public key so that AWS Payment Cryptography trusts the device certificates presented during translation. 

Create the ECDH agreement key. This key is used to derive the shared symmetric key with the device.

```
$ aws payment-cryptography create-key \
    --exportable \
    --key-attributes KeyAlgorithm=ECC_NIST_P256,KeyClass=ASYMMETRIC_KEY_PAIR,\
        KeyUsage=TR31_K3_ASYMMETRIC_KEY_FOR_KEY_AGREEMENT,\
        KeyModesOfUse='{DeriveKey=true}'
```

The response echoes back the request parameters and includes the ARN of the ECDH key.

```
{
    "Key": {
        "KeyArn": "arn:aws:payment-cryptography:us-east-1:111122223333:key/xxxxxxxxxxxxxxxx",
        "KeyAttributes": {
            "KeyUsage": "TR31_K3_ASYMMETRIC_KEY_FOR_KEY_AGREEMENT",
            "KeyClass": "ASYMMETRIC_KEY_PAIR",
            "KeyAlgorithm": "ECC_NIST_P256",
            "KeyModesOfUse": {
                "Encrypt": false,
                "Decrypt": false,
                "Wrap": false,
                "Unwrap": false,
                "Generate": false,
                "Sign": false,
                "Verify": false,
                "DeriveKey": true,
                "NoRestrictions": false
            }
        },
        "KeyCheckValue": "1A2B3C",
        "KeyCheckValueAlgorithm": "CMAC",
        "Enabled": true,
        "Exportable": true,
        "KeyState": "CREATE_COMPLETE",
        "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
        "CreateTimestamp": "2023-06-05T06:41:46.648000-07:00",
        "UsageStartTimestamp": "2023-06-05T06:41:46.626000-07:00"
    }
}
```

Create the Pin Generation/Verification Key (PGK) used to generate the PVV.

```
$ aws payment-cryptography create-key \
    --exportable \
    --key-attributes KeyAlgorithm=TDES_2KEY,KeyUsage=TR31_V2_VISA_PIN_VERIFICATION_KEY,\
        KeyClass=SYMMETRIC_KEY,\
        KeyModesOfUse='{Generate=true,Verify=true}'
```

```
{
    "Key": {
        "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ov6icy4ryas4zcza",
        "KeyAttributes": {
            "KeyUsage": "TR31_V2_VISA_PIN_VERIFICATION_KEY",
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
        "KeyCheckValue": "51A200",
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

Create the [Pin Encryption Key](terminology.md#terms.pek) (PEK) that the device PIN block is translated onto for backend storage.

```
$ aws payment-cryptography create-key \
    --exportable \
    --key-attributes KeyAlgorithm=AES_128,KeyUsage=TR31_P0_PIN_ENCRYPTION_KEY,\
        KeyClass=SYMMETRIC_KEY,\
        KeyModesOfUse='{Encrypt=true,Decrypt=true,Wrap=true,Unwrap=true}'
```

```
{
    "Key": {
        "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt",
        "KeyAttributes": {
            "KeyUsage": "TR31_P0_PIN_ENCRYPTION_KEY",
            "KeyClass": "SYMMETRIC_KEY",
            "KeyAlgorithm": "AES_128",
            "KeyModesOfUse": {
                "Encrypt": true,
                "Decrypt": true,
                "Wrap": true,
                "Unwrap": true,
                "Generate": false,
                "Sign": false,
                "Verify": false,
                "DeriveKey": false,
                "NoRestrictions": false
            }
        },
        "KeyCheckValue": "7CC9E2",
        "KeyCheckValueAlgorithm": "CMAC",
        "Enabled": true,
        "Exportable": true,
        "KeyState": "CREATE_COMPLETE",
        "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
        "CreateTimestamp": "2023-06-05T06:41:46.648000-07:00",
        "UsageStartTimestamp": "2023-06-05T06:41:46.626000-07:00"
    }
}
```

Import the device CA's public key so that AWS Payment Cryptography can verify the device certificates presented in later translation calls. Replace `<base64-CA-cert>` with the base64-encoded CA certificate.

```
$ aws payment-cryptography import-key \
    --key-material='{"RootCertificatePublicKey":{"KeyAttributes":{"KeyAlgorithm":"ECC_NIST_P256","KeyClass":"PUBLIC_KEY","KeyModesOfUse":{"Verify":true},"KeyUsage":"TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE"},"PublicKeyCertificate":"<base64-CA-cert>"}}'
```

```
{
    "Key": {
        "KeyArn": "arn:aws:payment-cryptography:us-east-1:111122223333:key/yyyyyyyyyyyyyyyy",
        "KeyAttributes": {
            "KeyUsage": "TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE",
            "KeyClass": "PUBLIC_KEY",
            "KeyAlgorithm": "ECC_NIST_P256",
            "KeyModesOfUse": {
                "Verify": true
            }
        },
        "KeyCheckValue": "4D5E6F",
        "KeyCheckValueAlgorithm": "CMAC",
        "Enabled": true,
        "Exportable": false,
        "KeyState": "CREATE_COMPLETE",
        "KeyOrigin": "EXTERNAL",
        "CreateTimestamp": "2023-06-05T06:41:46.648000-07:00",
        "UsageStartTimestamp": "2023-06-05T06:41:46.626000-07:00"
    }
}
```

Take note of each returned `KeyArn`. The examples that follow use the following literal placeholders:
+ ECDH agreement key: `arn:aws:payment-cryptography:us-east-1:111122223333:key/xxxxxxxxxxxxxxxx`
+ Imported CA public key: `arn:aws:payment-cryptography:us-east-1:111122223333:key/yyyyyyyyyyyyyyyy`
+ PGK: `arn:aws:payment-cryptography:us-east-2:111122223333:key/ov6icy4ryas4zcza`
+ PEK: `arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt`

On the cardholder device (typically a mobile phone or similar device), the following steps run in the device's application code for each of the Set PIN, Reset PIN, and Reveal PIN flows: generate an EC key pair on curve P-256; obtain the service ECDH public certificate from the customer backend; derive the ECDH shared secret and then a 16-byte AES-128 key using the NIST SP800-56A ConcatKDF (SHA-512) with the `SharedInformation` value; and encrypt or decrypt the ISO format 4 [PIN block](terminology.md#terms.pinblock) with that derived key. The device has no AWS credentials and does not call AWS Payment Cryptography directly; it exchanges this data with the customer backend, which makes the service calls.

Because the device is typically a phone, its EC key pair and certificate are provisioned on first use and refreshed periodically thereafter. The device generates the EC key pair and a certificate signing request (CSR), and the customer backend signs that CSR using AWS Private CA or a similar CA. The customer backend uses the resulting signed device certificate in its translate-pin-data calls, and AWS Payment Cryptography verifies it against the CA public key you imported.

The customer backend obtains the service ECDH public certificate and provides it to the device. The certificate is returned as a base64-encoded PEM in the `KeyCertificate` field, which is base64-decoded to a PEM file. The device uses this certificate as the service public key when it derives the shared secret.

```
$ aws payment-cryptography get-public-key-certificate \
    --key-identifier arn:aws:payment-cryptography:us-east-1:111122223333:key/xxxxxxxxxxxxxxxx
```

**Note**  
`SharedInformation` is 32 random bytes generated on the device and passed through the customer backend to AWS Payment Cryptography as a hex string. It must match the value the device used in the KDF, or the derived keys will not agree. 

## Set a user-selectable PIN
<a name="use-cases-issuers.generalfunctions.usermanagedpins.setpin"></a>

In the Set PIN flow, the cardholder chooses their own PIN on the device (for example, `1234`). The device derives the ECDH shared key, encrypts the chosen PIN into an ISO format 4 [PIN block](terminology.md#terms.pinblock) under that key, and sends the encrypted PIN block, its certificate signing request (CSR), and the shared information to the customer backend. The customer backend signs the CSR and then performs two data-plane calls. This example uses the sample `PAN` `171234567890123`. The PIN block, certificate, and shared information values shown are fictional placeholders. 

First, translate the ECDH-protected PIN block onto the server PEK. The incoming key is the ECDH agreement key, wrapped with the Diffie-Hellman parameters and the signed device certificate; the outgoing key is the PEK.

```
$ aws payment-cryptography-data translate-pin-data \
    --encrypted-pin-block A1B2C3D4E5F60718 \
    --incoming-key-identifier arn:aws:payment-cryptography:us-east-1:111122223333:key/xxxxxxxxxxxxxxxx \
    --incoming-wrapped-key 'WrappedKeyMaterial={DiffieHellmanSymmetricKey={CertificateAuthorityPublicKeyIdentifier=arn:aws:payment-cryptography:us-east-1:111122223333:key/yyyyyyyyyyyyyyyy,KeyAlgorithm=AES_128,KeyDerivationFunction=NIST_SP800,KeyDerivationHashAlgorithm=SHA_512,PublicKeyCertificate=<base64-signed-device-cert>,SharedInformation=0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef}}' \
    --incoming-translation-attributes 'IsoFormat4={PrimaryAccountNumber=171234567890123}' \
    --outgoing-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt \
    --outgoing-translation-attributes 'IsoFormat4={PrimaryAccountNumber=171234567890123}'
```

The response contains the PIN block re-encrypted under the PEK in ISO format 4.

```
{
    "PinBlock": "F7E6D5C4B3A29180",
    "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt",
    "KeyCheckValue": "7CC9E2"
}
```

Next, generate the PVV for the PEK-encrypted PIN block. The PGK generates the PVV, and the PEK identifies the key that the supplied PIN block is encrypted under.

```
$ aws payment-cryptography-data generate-pin-data \
    --generation-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ov6icy4ryas4zcza \
    --encryption-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt \
    --pin-block-format ISO_FORMAT_4 \
    --primary-account-number 171234567890123 \
    --generation-attributes 'VisaPinVerificationValue={PinVerificationKeyIndex=1,EncryptedPinBlock=F7E6D5C4B3A29180}'
```

The response contains the PVV in `PinData.VerificationValue` and the encrypted PIN block. Store the PVV on the customer backend so that you can verify the PIN later. For verification, see [Generate a random pin and the associated PVV and then verify the value](use-cases-issuers.generalfunctions.pvv.md). 

```
{
    "GenerationKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ov6icy4ryas4zcza",
    "GenerationKeyCheckValue": "51A200",
    "EncryptionKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt",
    "EncryptionKeyCheckValue": "7CC9E2",
    "EncryptedPinBlock": "F7E6D5C4B3A29180",
    "PinData": {
        "VerificationValue": "5507"
    }
}
```

For more information, see [TranslatePinData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_TranslatePinData.html) and [GeneratePinData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GeneratePinData.html) in the API reference guide.

## Reset a PIN (green PIN)
<a name="use-cases-issuers.generalfunctions.usermanagedpins.resetpin"></a>

In the Reset PIN (green PIN) flow, AWS Payment Cryptography generates a random PIN that the customer backend returns to the device to display to the cardholder, for example during first issuance or a forgotten-PIN reset. The device performs the same ECDH setup described in [Create the keys](#use-cases-issuers.generalfunctions.usermanagedpins.setup), and the customer backend makes the data-plane calls on its behalf. This example uses the sample `PAN` `171234567890123`; the PIN block and shared information values are fictional placeholders. 

First, generate a random PIN and its PVV, encrypting the PIN block under the PEK.

```
$ aws payment-cryptography-data generate-pin-data \
    --generation-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ov6icy4ryas4zcza \
    --encryption-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt \
    --pin-block-format ISO_FORMAT_4 \
    --primary-account-number 171234567890123 \
    --generation-attributes 'VisaPin={PinVerificationKeyIndex=1}'
```

The response contains the PVV in `PinData.VerificationValue` and the PEK-encrypted PIN block (ISO format 4). Store the PVV on the customer backend for later verification.

```
{
    "GenerationKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ov6icy4ryas4zcza",
    "GenerationKeyCheckValue": "51A200",
    "EncryptionKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt",
    "EncryptionKeyCheckValue": "7CC9E2",
    "EncryptedPinBlock": "F7E6D5C4B3A29180",
    "PinData": {
        "VerificationValue": "5507"
    }
}
```

Next, translate the PEK-encrypted PIN block (ISO format 4) onto the device ECDH-derived key (ISO format 4) so that only the requesting device can read it.

```
$ aws payment-cryptography-data translate-pin-data \
    --encrypted-pin-block F7E6D5C4B3A29180 \
    --incoming-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt \
    --incoming-translation-attributes 'IsoFormat4={PrimaryAccountNumber=171234567890123}' \
    --outgoing-key-identifier arn:aws:payment-cryptography:us-east-1:111122223333:key/xxxxxxxxxxxxxxxx \
    --outgoing-wrapped-key 'WrappedKeyMaterial={DiffieHellmanSymmetricKey={CertificateAuthorityPublicKeyIdentifier=arn:aws:payment-cryptography:us-east-1:111122223333:key/yyyyyyyyyyyyyyyy,KeyAlgorithm=AES_128,KeyDerivationFunction=NIST_SP800,KeyDerivationHashAlgorithm=SHA_512,PublicKeyCertificate=<base64-signed-device-cert>,SharedInformation=0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef}}' \
    --outgoing-translation-attributes 'IsoFormat4={PrimaryAccountNumber=171234567890123}'
```

The response contains the PIN block re-encrypted under the device ECDH-derived key in ISO format 4.

```
{
    "PinBlock": "A1B2C3D4E5F60718",
    "KeyArn": "arn:aws:payment-cryptography:us-east-1:111122223333:key/xxxxxxxxxxxxxxxx",
    "KeyCheckValue": "1A2B3C"
}
```

The customer backend returns the ECDH-encrypted PIN block to the device. The device decrypts the returned PIN block with its ECDH-derived key (in the device application code) and displays the PIN to the cardholder. Because the key is derived only on that device, no other party can decrypt the PIN block.

For more information, see [GeneratePinData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GeneratePinData.html) and [TranslatePinData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_TranslatePinData.html) in the API reference guide.

## Reveal a PIN
<a name="use-cases-issuers.generalfunctions.usermanagedpins.revealpin"></a>

The Reveal PIN flow returns an existing PIN block to a cardholder device so that the device can display or otherwise reveal the PIN. The device performs the same ECDH setup described in [Create the keys](#use-cases-issuers.generalfunctions.usermanagedpins.setup), and the customer backend translates the stored PEK-encrypted PIN block back onto the ECDH-derived key and returns it to the device. This example uses the sample `PAN` `171234567890123`; the PIN block and shared information values are fictional placeholders. 

**Note**  
Consider authenticating the cardholder and letting them set a new PIN instead of revealing the existing PIN. A notable exception is in countries that use offline PIN, for example in Europe, where the PIN is also stored on the chip card. In those cases, revealing the existing PIN can be simpler than reprogramming the card.

Translate the stored PEK-encrypted PIN block (ISO format 4) onto the device ECDH-derived key (ISO format 4).

```
$ aws payment-cryptography-data translate-pin-data \
    --encrypted-pin-block F7E6D5C4B3A29180 \
    --incoming-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt \
    --incoming-translation-attributes 'IsoFormat4={PrimaryAccountNumber=171234567890123}' \
    --outgoing-key-identifier arn:aws:payment-cryptography:us-east-1:111122223333:key/xxxxxxxxxxxxxxxx \
    --outgoing-wrapped-key 'WrappedKeyMaterial={DiffieHellmanSymmetricKey={CertificateAuthorityPublicKeyIdentifier=arn:aws:payment-cryptography:us-east-1:111122223333:key/yyyyyyyyyyyyyyyy,KeyAlgorithm=AES_128,KeyDerivationFunction=NIST_SP800,KeyDerivationHashAlgorithm=SHA_512,PublicKeyCertificate=<base64-signed-device-cert>,SharedInformation=0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef}}' \
    --outgoing-translation-attributes 'IsoFormat4={PrimaryAccountNumber=171234567890123}'
```

The response contains the PIN block re-encrypted under the device ECDH-derived key in ISO format 4.

```
{
    "PinBlock": "A1B2C3D4E5F60718",
    "KeyArn": "arn:aws:payment-cryptography:us-east-1:111122223333:key/xxxxxxxxxxxxxxxx",
    "KeyCheckValue": "1A2B3C"
}
```

The customer backend returns the ECDH-encrypted PIN block to the device. The device decrypts the returned PIN block with its ECDH-derived key (in the device application code) to reveal the PIN. Because the key is derived only on that device, no other party can decrypt the PIN block.

For more information, see [TranslatePinData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_TranslatePinData.html) in the API reference guide.