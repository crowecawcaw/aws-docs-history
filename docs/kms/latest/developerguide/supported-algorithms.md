

# Supported cryptographic algorithms
<a name="supported-algorithms"></a>

AWS KMS supports the following cryptographic algorithms for KMS keys. The algorithms you can use depend on the [key spec](create-keys.md#key-spec) and [key usage](create-keys.md#key-usage) of the KMS key. For detailed descriptions of each key spec and the algorithms it supports, see [Key spec reference](symm-asymm-choose-key-spec.md).

For guidance on which algorithms to use and when, see [Cryptography algorithms and AWS services](https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/aws-cryptography-services.html#algorithms).

## Symmetric key algorithms
<a name="supported-algorithms-symmetric"></a>

AWS KMS supports the following algorithms for symmetric KMS keys.


**Supported algorithms for symmetric KMS keys**  

| Algorithm | Key usage | Key spec | 
| --- | --- | --- | 
| AES-256-GCM | Encrypt and decrypt | SYMMETRIC\_DEFAULT | 
| SM4-128 (China Regions only) | Encrypt and decrypt | SYMMETRIC\_DEFAULT | 
| HMAC\_SHA\_224 | Generate and verify MAC | HMAC\_224 | 
| HMAC\_SHA\_256 | Generate and verify MAC | HMAC\_256 | 
| HMAC\_SHA\_384 | Generate and verify MAC | HMAC\_384 | 
| HMAC\_SHA\_512 | Generate and verify MAC | HMAC\_512 | 

## Asymmetric key algorithms
<a name="supported-algorithms-asymmetric"></a>

Each asymmetric KMS key has a single [key usage](create-keys.md#key-usage) that determines which of these algorithms you can use.


**Supported algorithms for asymmetric KMS keys**  

| Algorithm | Key usage | Key spec | 
| --- | --- | --- | 
| RSAES\_OAEP\_SHA\_1, RSAES\_OAEP\_SHA\_256 | Encrypt and decrypt | RSA\_2048, RSA\_3072, RSA\_4096 | 
| RSASSA\_PSS\_SHA\_256, RSASSA\_PSS\_SHA\_384, RSASSA\_PSS\_SHA\_512, RSASSA\_PKCS1\_V1\_5\_SHA\_256, RSASSA\_PKCS1\_V1\_5\_SHA\_384, RSASSA\_PKCS1\_V1\_5\_SHA\_512 | Sign and verify | RSA\_2048, RSA\_3072, RSA\_4096 | 
| ECDSA\_SHA\_256 | Sign and verify | ECC\_NIST\_P256 (secp256r1) | 
| ECDSA\_SHA\_384 | Sign and verify | ECC\_NIST\_P384 (secp384r1) | 
| ECDSA\_SHA\_512 | Sign and verify | ECC\_NIST\_P521 (secp521r1) | 
| ECDSA\_SHA\_256 | Sign and verify | ECC\_SECG\_P256K1 (secp256k1) | 
| ED25519\_SHA\_512, ED25519\_PH\_SHA\_512 | Sign and verify | ECC\_NIST\_EDWARDS25519 (ed25519) | 
| ML\_DSA\_SHAKE\_256 | Sign and verify | ML\_DSA\_44, ML\_DSA\_65, ML\_DSA\_87 | 
| ECDH | Key agreement | ECC\_NIST\_P256, ECC\_NIST\_P384, ECC\_NIST\_P521 | 
| SM2PKE (encryption), SM2DSA (signing), ECDH (key agreement) | Encrypt and decrypt, sign and verify, or key agreement | SM2 (China Regions only) | 