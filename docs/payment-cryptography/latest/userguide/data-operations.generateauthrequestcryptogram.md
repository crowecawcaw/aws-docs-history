

# Generate auth request (ARQC) cryptogram
<a name="data-operations.generateauthrequestcryptogram"></a>

 The generate auth request cryptogram API is used for generating [ARQC](terminology.md#terms.arqc). This API enables you to generate ARQC using AWS Payment Cryptography for development and testing purposes. 

**Important**  
This operation is intended for development and testing scenarios only. It is not recommended to use this operation as a substitute for card-based cryptogram generation in production payment flows.

For all available options, see [GenerateAuthRequestCryptogram](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateAuthRequestCryptogram.html) in the API Reference. 

ARQC cryptograms typically require the following inputs (although this may vary by implementation): 
+ [PAN](terminology.md#terms.pan) - Specified in the PrimaryAccountNumber field
+ [PAN Sequence Number (PSN)](terminology.md#terms.psn) - Specified in the PanSequenceNumber field
+ Key Derivation Method such as Common Session Key (CSK) - Specified in the SessionKeyDerivationAttributes
+ Master Key Derivation Mode (such as EMV Option A) - Specified in the MajorKeyDerivationMode
+ Transaction data - A string of transaction, terminal, and card data such as Amount and Date. Specified in the TransactionData field.
+ [Issuer Master Key](terminology.md#terms.imk) - The master key used to derive the cryptogram (AC) key. This key protects individual transactions and is specified in the KeyIdentifier field.

For more information about building and padding transaction data, see [Verify auth request (ARQC) cryptogram](data-operations.verifyauthrequestcryptogram.md).

**Topics**
+ [Examples](#w2aac15c25c10c17)

## Examples
<a name="w2aac15c25c10c17"></a>

### Visa CVN10
<a name="w2aac15c25c10c17b3"></a>

**Example**  
The following example generates an ARQC using Visa CVN10.  
If AWS Payment Cryptography generates the ARQC successfully, an http/200 is returned with the generated cryptogram.  

```
$ aws payment-cryptography-data generate-auth-request-cryptogram \
--key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk \
--major-key-derivation-mode EMV_OPTION_A \
--transaction-data 00000000170000000000000008400080008000084016051700000000093800000B03011203000000 \
--session-key-derivation-attributes='{"Visa":{"PanSequenceNumber":"01", \
"PrimaryAccountNumber":"9137631040001422"}}'
```

```
{
  "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk",
  "KeyCheckValue": "08D7B4",
  "AuthRequestCryptogram": "D791093C8A921769"
}
```

### Visa CVN18 and Visa CVN22
<a name="w2aac15c25c10c17b5"></a>

**Example**  
The following example generates an ARQC using Visa CVN18 or CVN22. The cryptographic operations are the same between CVN18 and CVN22 but the data contained within transaction data varies. Compared to CVN10, a completely different cryptogram is generated even with the same inputs.  
If AWS Payment Cryptography generates the ARQC successfully, an http/200 is returned with the generated cryptogram.  

```
$ aws payment-cryptography-data generate-auth-request-cryptogram \
--key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk \
--major-key-derivation-mode EMV_OPTION_A \
--transaction-data 00000000170000000000000008400080008000084016051700000000093800000B1F22010300000000000 \
00000000000000000000000000000000000000000008000000000000000 \
--session-key-derivation-attributes='{"EmvCommon":{"ApplicationTransactionCounter":"000B", \
"PanSequenceNumber":"01","PrimaryAccountNumber":"9137631040001422"}}'
```

```
{
  "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/pw3s6nl62t5ushfk",
  "KeyCheckValue": "08D7B4",
  "AuthRequestCryptogram": "61EDCC708B4C97B4"
}
```