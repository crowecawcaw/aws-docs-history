

# Importing key material
<a name="importing-key-material"></a>

AWS KMS provides a mechanism for importing the cryptographic material used for an HBK. As described in [Calling CreateKey](create-key.md), when the CreateKey command is used with `Origin` set to `EXTERNAL`, a logical KMS key is created that contains no underlying HBK. The cryptographic material must be imported using the [`ImportKeyMaterial`](https://docs.aws.amazon.com/kms/latest/APIReference/API_ImportKeyMaterial.html) API call. You can use this feature to control the key creation and durability of the cryptographic material. If you use this feature, we recommend that you take significant caution in the handling and durability of these keys in your environment. For complete details and recommendations for importing key material, see [Importing key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) in the *AWS Key Management Service Developer Guide*.

## Calling ImportKeyMaterial
<a name="importkeymaterial"></a>

The `ImportKeyMaterial` request imports the necessary cryptographic material for the HBK. The cryptographic material must be a 256-bit symmetric key. It must be encrypted using the algorithm specified in `WrappingAlgorithm` under the returned public key from a recent [`GetParametersForImport`](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetParametersForImport.html) request.

[An `ImportKeyMaterial` request](https://docs.aws.amazon.com/kms/latest/APIReference/API_ImportKeyMaterial.html#API_ImportKeyMaterial_RequestSyntax) takes the following arguments.

```
{
  "EncryptedKeyMaterial": blob,
  "ExpirationModel": "string",
  "ImportToken": blob,
  "KeyId": "string",
  "ValidTo": number
}
```

**EncryptedKeyMaterial**  
The imported key material encrypted with the public key returned in a `GetParametersForImport` request using the wrapping algorithm specified in that request. 

**ExpirationModel**  
Specifies whether the key material expires. When this value is `KEY_MATERIAL_EXPIRES`, the `ValidTo` parameter must contain an expiration date. When this value is `KEY_MATERIAL_DOES_NOT_EXPIRE`, do not include the `ValidTo` parameter. The valid values are `"KEY_MATERIAL_EXPIRES"` and `"KEY_MATERIAL_DOES_NOT_EXPIRE"`.

**ImportToken**  
The import token returned by the same `GetParametersForImport` request that provided the public key.

**KeyId**  
The KMS key that will be associated with the imported key material. The `Origin` of the KMS key must be `EXTERNAL`.  
You can delete and reimport the *same* imported key material into the specified KMS key, but you cannot import or associate the KMS key any other key material.

**ValidTo**  
(Optional) The time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the KMS key becomes unusable. This parameter is required when the value of the `ExpirationModel` is `KEY_MATERIAL_EXPIRES`. Otherwise it is invalid.

When the request succeeds, the KMS key is available for use within AWS KMS until the specified expiration date, if one is provided. After the imported key material expires, the EKT is deleted from the AWS KMS storage layer. 