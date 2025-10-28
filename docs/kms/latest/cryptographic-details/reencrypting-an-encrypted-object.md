# Reencrypting an encrypted object

An existing customer ciphertext encrypted under one KMS key can be reencrypted to another KMS key
through a reencrypt command. Reencrypt encrypts data on the server side with a new KMS key without
exposing the plaintext of the key on the client side. The data is first decrypted and then
encrypted.

The following is the request syntax.

```
{
	"CiphertextBlob": "blob",
	"DestinationEncryptionContext": { "string" : "string" },
	"DestinationKeyId": "string",
	"GrantTokens": ["string"],
       "SourceKeyId": "string",
	"SourceEncryptionContext": { "string" : "string"}
}
```

The request accepts the following data in JSON format.

**CiphertextBlob**

Ciphertext of the data to reencrypt.

**DestinationEncryptionContext**

(Optional) Encryption context to be used when the data is reencrypted.

**DestinationKeyId**

Key identifier of the key used to reencrypt the data.

**GrantTokens**

(Optional) A list of grant tokens that represent grants that provide permissions to
perform decryption.

**SourceKeyId**

(Optional) Key identifier of the key used to decrypt the data.

**SourceEncryptionContext**

(Optional) Encryption context used to encrypt and decrypt the data specified in the
`CiphertextBlob` parameter.

The process combines the decrypt and encrypt operations of the previous descriptions: The
customer ciphertext is decrypted under the initial HBK referenced by the customer ciphertext
to the current HBK under the intended KMS key. When the KMS keys used in this command are the same,
this command moves the customer ciphertext from an old version of an HBK to the latest version
of an HBK.

The following is the response syntax.

```
{
    "CiphertextBlob": blob,
    "DestinationEncryptionAlgorithm": "string",
    "KeyId": "string",
    "SourceEncryptionAlgorithm": "string",
    "SourceKeyId": "string"
}
```

If the calling application wants to ensure the authenticity of the underlying plaintext,
it must verify the SourceKeyId returned is the one expected.
