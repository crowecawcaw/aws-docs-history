

# Understanding key attributes for AWS Payment Cryptography key
<a name="keys-validattributes"></a>

A tenet of proper key management is that keys are appropriately scoped and can only be used for permitted operations. As such, certain keys can only be created with certain key modes of use. Whenever possible, this aligns with the available modes of use as defined by [TR-31](terminology.md#terms.tr31). 

 Although AWS Payment Cryptography will prevent you from creating invalid keys, valid combinations are provided here for your convenience. 

## Symmetric Keys
<a name="w2aac12c39b7"></a>
+ TR31\_B0\_BASE\_DERIVATION\_KEY
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY ,AES\_128 ,AES\_192 ,AES\_256
  + **Allowed combination of key modes of use**: { DeriveKey = true },{ NoRestrictions = true }
+ TR31\_C0\_CARD\_VERIFICATION\_KEY
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY ,AES\_128\* ,AES\_192\* ,AES\_256\*
  + **Allowed combination of key modes of use**: { Generate = true } ,{ Verify = true } ,{ Generate = true, Verify= true } ,{ NoRestrictions = true }
+ TR31\_D0\_SYMMETRIC\_DATA\_ENCRYPTION\_KEY
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY ,AES\_128 ,AES\_192 ,AES\_256
  + **Allowed combination of key modes of use**: { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true } , { Encrypt = true, Wrap = true } ,{ Decrypt = true, Unwrap = true } ,{ NoRestrictions = true }
+ TR31\_E0\_EMV\_MKEY\_APP\_CRYPTOGRAMS
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY\*, AES\_128\* ,AES\_192\* ,AES\_256\*
  + **Allowed combination of key modes of use**: { DeriveKey = true }, { NoRestrictions = true }
+ TR31\_E1\_EMV\_MKEY\_CONFIDENTIALITY
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY, AES\_128\*,AES\_192\*,AES\_256\*
  + **Allowed combination of key modes of use**: { DeriveKey = true }, { NoRestrictions = true }
+ TR31\_E2\_EMV\_MKEY\_INTEGRITY
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY ,AES\_128\* ,AES\_192\* ,AES\_256\*
  + **Allowed combination of key modes of use**: { DeriveKey = true }, { NoRestrictions = true }
+ TR31\_E4\_EMV\_MKEY\_DYNAMIC\_NUMBERS
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY ,AES\_128\* ,AES\_192\* ,AES\_256\*
  + **Allowed combination of key modes of use**: { DeriveKey = true }, { NoRestrictions = true }
+ TR31\_E5\_EMV\_MKEY\_CARD\_PERSONALIZATION
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY ,AES\_128\* ,AES\_192\* ,AES\_256\*
  + **Allowed combination of key modes of use**: { DeriveKey = true }, { NoRestrictions = true }
+ TR31\_E6\_EMV\_MKEY\_OTHER
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY ,AES\_128\* ,AES\_192\* ,AES\_256\*
  + **Allowed combination of key modes of use**: { DeriveKey = true }, { NoRestrictions = true }
+ TR31\_K0\_KEY\_ENCRYPTION\_KEY
  + Recommended to use TR31\_K1\_KEY\_BLOCK\_PROTECTION\_KEY. **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY ,AES\_128 ,AES\_192 ,AES\_256
  + **Allowed combination of key modes of use**: { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true } , { Encrypt = true, Wrap = true } ,{ Decrypt = true, Unwrap = true } ,{ NoRestrictions = true }
+ TR31\_K1\_KEY\_BLOCK\_PROTECTION\_KEY
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY ,AES\_128 ,AES\_192 ,AES\_256
  + **Allowed combination of key modes of use**: { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true } , { Encrypt = true, Wrap = true } ,{ Decrypt = true, Unwrap = true } ,{ NoRestrictions = true }
+ TR31\_M1\_ISO\_9797\_1\_MAC\_KEY
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY
  + **Allowed combination of key modes of use**: { Generate = true } ,{ Verify = true } ,{ Generate = true, Verify= true } ,{ NoRestrictions = true }
+ TR31\_M3\_ISO\_9797\_3\_MAC\_KEY
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY
  + **Allowed combination of key modes of use**: { Generate = true } ,{ Verify = true } ,{ Generate = true, Verify= true } ,{ NoRestrictions = true }
+ TR31\_M6\_ISO\_9797\_5\_CMAC\_KEY
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY ,AES\_128 ,AES\_192 ,AES\_256
  + **Allowed combination of key modes of use**: { Generate = true } ,{ Verify = true } ,{ Generate = true, Verify= true } ,{ NoRestrictions = true }
+ TR31\_M7\_HMAC\_KEY
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY ,AES\_128 ,AES\_192 ,AES\_256
  + **Allowed combination of key modes of use**: { Generate = true } ,{ Verify = true } ,{ Generate = true, Verify= true } ,{ NoRestrictions = true }
+ TR31\_P0\_PIN\_ENCRYPTION\_KEY
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY ,AES\_128 ,AES\_192 ,AES\_256
  + **Allowed combination of key modes of use**: { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true } ,{ Encrypt = true, Wrap = true } ,{ Decrypt = true, Unwrap = true } ,{ NoRestrictions = true }
+ TR31\_V1\_IBM3624\_PIN\_VERIFICATION\_KEY
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY ,AES\_128 ,AES\_192 ,AES\_256
  + **Allowed combination of key modes of use**: { Generate = true } ,{ Verify = true } ,{ Generate = true, Verify= true } ,{ NoRestrictions = true }
+ TR31\_V2\_VISA\_PIN\_VERIFICATION\_KEY
  + **Allowed Key Algorithms**: TDES\_2KEY ,TDES\_3KEY ,AES\_128 ,AES\_192 ,AES\_256
  + **Allowed combination of key modes of use**: { Generate = true } ,{ Verify = true } ,{ Generate = true, Verify= true } ,{ NoRestrictions = true }

## Asymmetric Keys
<a name="w2aac12c39b9"></a>
+ TR31\_D1\_ASYMMETRIC\_KEY\_FOR\_DATA\_ENCRYPTION
  + **Allowed Key Algorithms**: RSA\_2048 ,RSA\_3072 ,RSA\_4096
  + **Allowed combination of key modes of use**: { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true } ,{ Encrypt = true, Wrap = true } ,{ Decrypt = true, Unwrap = true }
  + **NOTE:**: { Encrypt = true, Wrap = true } is the only valid option when importing a public key that is intended for encrypting data or wrapping a key
+ TR31\_S0\_ASYMMETRIC\_KEY\_FOR\_DIGITAL\_SIGNATURE
  + **Allowed Key Algorithms**: RSA\_2048 ,RSA\_3072 ,RSA\_4096
  + **Allowed combination of key modes of use**: { Sign = true } ,{ Verify = true }
  + **NOTE:**: { Verify = true } is the only valid option when importing a key meant for signing, such as root certificate, intermediate certificate or signing certificates for TR-34. 
+ TR31\_K3\_ASYMMETRIC\_KEY\_FOR\_KEY\_AGREEMENT
  + Used for key agreement algorithms such as ECDH
  + **Allowed Key Algorithms**: ECC\_NIST\_P256,ECC\_NIST\_P384,ECC\_NIST\_P521
  + **Allowed combination of key modes of use**: { DeriveKey = true }.
  + **NOTE:**DeriveKeyUsage is used to specify what kind of key will be derived from this base key. This is fixed at key creation/import.
+ TR31\_K2\_TR34\_ASYMMETRIC\_KEY
  + Asymmetric key used for X9.24 compatible key exchange mechanisms like TR-34
  + **Allowed Key Algorithms**: RSA\_2048,RSA\_3072,RSA\_4096
  + **Allowed combination of key modes of use**: { DeriveKey = true }.
  + **Allowed combination of key modes of use**: { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true } ,{ Encrypt = true, Wrap = true } ,{ Decrypt = true, Unwrap = true }
  + **NOTE:**: { Encrypt = true, Wrap = true } is the only valid option when importing a public key that is intended for encrypting data or wrapping a key

\* This algorithm/key type combination is not currently supported by any cryptographic operations