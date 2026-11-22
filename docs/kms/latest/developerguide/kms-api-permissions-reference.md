

# AWS KMS permissions

This table is designed to help you understand AWS KMS permissions so you can control access to your AWS KMS resources. Definitions of the column headings appear below the table.

You can also learn about AWS KMS permissions in the [Actions, resources, and condition keys for AWS Key Management Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awskeymanagementservice.html) topic of the *Service Authorization Reference*. However, that topic doesn't list all of the condition keys that you can use to refine each permission.

For more information on which AWS KMS operations are valid for symmetric encryption KMS keys, asymmetric KMS keys, and HMAC KMS keys, see the [Key type reference](symm-asymm-compare.md). 

**Note**  
You might have to scroll horizontally or vertically to see all of the data in the table.

<a name="kms-api-permissions-reference-table"></a>

- ** [CancelKeyDeletion](https://docs.aws.amazon.com/kms/latest/APIReference/API_CancelKeyDeletion.html) `kms:CancelKeyDeletion` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- **[ConnectCustomKeyStore](https://docs.aws.amazon.com/kms/latest/APIReference/API_ConnectCustomKeyStore.html) `kms:ConnectCustomKeyStore`**
  - **Policy type:** IAM policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** `*`
  - **AWS KMS condition keys:** [kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)
  - **AWS RAM customer managed permission:** No

- ** [CreateAlias](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateAlias.html) `kms:CreateAlias` To use this operation, the caller needs `kms:CreateAlias` permission on two resources: +  The alias (in an IAM policy) <br />+  The KMS key (in a key policy)  For details, see [Controlling access to aliases](alias-access.md). **
  - **Policy type:** IAM policy (for the alias) / **Cross-account use:** No / **Resources (for IAM policies):** Alias / **AWS KMS condition keys:** None (when controlling access to the alias)
  - **Policy type:** Key policy (for the KMS key) / **Cross-account use:** No / **Resources (for IAM policies):** KMS key / **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- **[CreateCustomKeyStore](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateCustomKeyStore.html)`kms:CreateCustomKeyStore`**
  - **Policy type:** IAM policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** `*`
  - **AWS KMS condition keys:** [kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)
  - **AWS RAM customer managed permission:** No

- ** [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) `kms:CreateGrant` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Encryption context conditions:*<br />[kms:EncryptionContext:*context-key*](conditions-kms.md#conditions-kms-encryption-context-keys)<br />[kms:EncryptionContextKeys](conditions-kms.md#conditions-kms-encryption-context-keys)<br />*Grant conditions:*<br />[kms:GrantConstraintSourceArn](conditions-kms.md#conditions-kms-grant-constraint-source-arn)<br />[kms:GrantConstraintType](conditions-kms.md#conditions-kms-grant-constraint-type)<br />[kms:GranteePrincipal](conditions-kms.md#conditions-kms-grantee-principal)<br />[kms:GranteeServicePrincipal](conditions-kms.md#conditions-kms-grantee-service-principal)<br />[kms:GrantIsForAWSResource](conditions-kms.md#conditions-kms-grant-is-for-aws-resource)<br />[kms:GrantOperations](conditions-kms.md#conditions-kms-grant-operations)<br />[kms:RetiringPrincipal](conditions-kms.md#conditions-kms-retiring-principal)<br />[kms:RetiringServicePrincipal](conditions-kms.md#conditions-kms-retiring-service-principal)<br />*Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes, with a condition that requires `kms:GrantIsForAWSResource` or `aws:PrincipalIsAWSService` to be `true`

- ** [CreateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html) `kms:CreateKey` **
  - **Policy type:** IAM policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** `*`
  - **AWS KMS condition keys:** [kms:BypassPolicyLockoutSafetyCheck](conditions-kms.md#conditions-kms-bypass-policy-lockout-safety-check)<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />[aws:RequestTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag) (AWS global condition key)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys) (AWS global condition key)
  - **AWS RAM customer managed permission:** No

- ** [Decapsulate](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decapsulate.html) `kms:Decapsulate` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** Conditions for cryptographic operations:[kms:EncapsulationAlgorithm](conditions-kms.md#conditions-kms-encapsulation-algorithm)<br />[kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias)<br />*Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) `kms:Decrypt` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for cryptographic operations*<br />[kms:EncryptionAlgorithm](conditions-kms.md#conditions-kms-encryption-algorithm)<br />[kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias)<br />*Encryption context conditions:*<br />[kms:EncryptionContext:*context-key*](conditions-kms.md#conditions-kms-encryption-context-keys)<br />[kms:EncryptionContextKeys](conditions-kms.md#conditions-kms-encryption-context-keys)<br />*Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [DeleteAlias](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeleteAlias.html) `kms:DeleteAlias` To use this operation, the caller needs `kms:DeleteAlias` permission on two resources: +  The alias (in an IAM policy) <br />+  The KMS key (in a key policy)  For details, see [Controlling access to aliases](alias-access.md). **
  - **Policy type:** IAM policy (for the alias) / **Cross-account use:** No / **Resources (for IAM policies):** Alias / **AWS KMS condition keys:** None (when controlling access to the alias)
  - **Policy type:** Key policy (for the KMS key) / **Cross-account use:** No / **Resources (for IAM policies):** KMS key / **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- **[DeleteCustomKeyStore](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeleteCustomKeyStore.html)`kms:DeleteCustomKeyStore`**
  - **Policy type:** IAM policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** `*`
  - **AWS KMS condition keys:** [kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)
  - **AWS RAM customer managed permission:** No

- ** [DeleteImportedKeyMaterial](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeleteImportedKeyMaterial.html) `kms:DeleteImportedKeyMaterial` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- **[DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html)`kms:DeriveSharedSecret`**
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)Conditions for cryptographic operations:<br />[kms:KeyAgreementAlgorithm](conditions-kms.md#conditions-kms-key-agreement-algorithm)
  - **AWS RAM customer managed permission:** Yes

- **[DescribeCustomKeyStores](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeCustomKeyStores.html)`kms:DescribeCustomKeyStores`**
  - **Policy type:** IAM policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** `*`
  - **AWS KMS condition keys:** [kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)
  - **AWS RAM customer managed permission:** No

- ** [DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html) `kms:DescribeKey` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />*Other conditions:*<br />[kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias)
  - **AWS RAM customer managed permission:** Yes

- ** [DisableKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKey.html) `kms:DisableKey` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />*Key last usage condition:*<br />[kms:TrailingDaysWithoutKeyUsage](conditions-kms.md#conditions-kms-trailing-days-without-key-usage)
  - **AWS RAM customer managed permission:** Yes

- ** [DisableKeyRotation](https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKeyRotation.html) `kms:DisableKeyRotation` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- **[DisconnectCustomKeyStore](https://docs.aws.amazon.com/kms/latest/APIReference/API_DisconnectCustomKeyStore.html)`kms:DisconnectCustomKeyStore`**
  - **Policy type:** IAM policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** `*`
  - **AWS KMS condition keys:** [kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)
  - **AWS RAM customer managed permission:** No

- ** [EnableKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKey.html) `kms:EnableKey` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [EnableKeyRotation](https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKeyRotation.html) `kms:EnableKeyRotation` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />*Automatic key rotation conditions:*<br />[kms:RotationPeriodInDays](conditions-kms.md#conditions-kms-rotation-period-in-days)
  - **AWS RAM customer managed permission:** Yes

- ** [Encapsulate](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encapsulate.html) `kms:Encapsulate` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** Conditions for cryptographic operations:[kms:EncapsulationAlgorithm](conditions-kms.md#conditions-kms-encapsulation-algorithm)<br />[kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias)<br />*Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) `kms:Encrypt` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for cryptographic operations*<br />[kms:EncryptionAlgorithm](conditions-kms.md#conditions-kms-encryption-algorithm)<br />[kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias)<br />*Encryption context conditions:*<br />[kms:EncryptionContext:*context-key*](conditions-kms.md#conditions-kms-encryption-context-keys)<br />[kms:EncryptionContextKeys](conditions-kms.md#conditions-kms-encryption-context-keys)<br />*Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) `kms:GenerateDataKey` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for cryptographic operations*<br />[kms:EncryptionAlgorithm](conditions-kms.md#conditions-kms-encryption-algorithm)<br />[kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias)<br />*Encryption context conditions:*<br />[kms:EncryptionContext:*context-key*](conditions-kms.md#conditions-kms-encryption-context-keys)<br />[kms:EncryptionContextKeys](conditions-kms.md#conditions-kms-encryption-context-keys)<br />*Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [GenerateDataKeyPair](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPair.html) `kms:GenerateDataKeyPair` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key<br />Generates an asymmetric data key pair that is protected by a symmetric encryption KMS key.
  - **AWS KMS condition keys:** *Conditions for data key pairs:*<br />[kms:DataKeyPairSpec](conditions-kms.md#conditions-kms-data-key-spec)<br />*Conditions for cryptographic operations*<br />[kms:EncryptionAlgorithm](conditions-kms.md#conditions-kms-encryption-algorithm)<br />[kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias)<br />*Encryption context conditions:*<br />[kms:EncryptionContext:*context-key*](conditions-kms.md#conditions-kms-encryption-context-keys)<br />[kms:EncryptionContextKeys](conditions-kms.md#conditions-kms-encryption-context-keys)<br />*Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [GenerateDataKeyPairWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPairWithoutPlaintext.html) `kms:GenerateDataKeyPairWithoutPlaintext` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key<br />Generates an asymmetric data key pair that is protected by a symmetric encryption KMS key.
  - **AWS KMS condition keys:** *Conditions for data key pairs:*<br />[kms:DataKeyPairSpec](conditions-kms.md#conditions-kms-data-key-spec)<br />*Conditions for cryptographic operations*<br />[kms:EncryptionAlgorithm](conditions-kms.md#conditions-kms-encryption-algorithm)<br />[kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias)<br />*Encryption context conditions:*<br />[kms:EncryptionContext:*context-key*](conditions-kms.md#conditions-kms-encryption-context-keys)<br />[kms:EncryptionContextKeys](conditions-kms.md#conditions-kms-encryption-context-keys)<br />*Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html) `kms:GenerateDataKeyWithoutPlaintext` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for cryptographic operations*<br />[kms:EncryptionAlgorithm](conditions-kms.md#conditions-kms-encryption-algorithm)<br />[kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias)<br />*Encryption context conditions:*<br />[kms:EncryptionContext:*context-key*](conditions-kms.md#conditions-kms-encryption-context-keys)<br />[kms:EncryptionContextKeys](conditions-kms.md#conditions-kms-encryption-context-keys)<br />*Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- **[GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html)`kms:GenerateMac`**
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)Conditions for cryptographic operations:<br />[kms:MacAlgorithm](conditions-kms.md#conditions-kms-mac-algorithm) <br />[kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias)
  - **AWS RAM customer managed permission:** Yes

- ** [GenerateRandom](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateRandom.html) `kms:GenerateRandom` **
  - **Policy type:** IAM policy
  - **Cross-account use:** N/A
  - **Resources (for IAM policies):** `*`
  - **AWS KMS condition keys:** None
  - **AWS RAM customer managed permission:** No

- ** [GetKeyLastUsage](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyLastUsage.html) `kms:GetKeyLastUsage` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [GetKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyPolicy.html) `kms:GetKeyPolicy` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />*Other conditions:*<br />[kms:PolicyName](conditions-kms.md#conditions-kms-policy-name)
  - **AWS RAM customer managed permission:** Yes

- ** [GetKeyRotationStatus](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyRotationStatus.html) `kms:GetKeyRotationStatus` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [GetParametersForImport](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetParametersForImport.html) `kms:GetParametersForImport` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** [kms:WrappingAlgorithm](conditions-kms.md#conditions-kms-wrapping-algorithm)<br />[kms:WrappingKeySpec](conditions-kms.md#conditions-kms-wrapping-key-spec)<br />*Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html) `kms:GetPublicKey` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />*Other conditions:*<br />[kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias)
  - **AWS RAM customer managed permission:** Yes

- ** [ImportKeyMaterial](https://docs.aws.amazon.com/kms/latest/APIReference/API_ImportKeyMaterial.html) `kms:ImportKeyMaterial` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />*Other conditions:*[kms:ExpirationModel](conditions-kms.md#conditions-kms-expiration-model)<br />[kms:ValidTo](conditions-kms.md#conditions-kms-valid-to)
  - **AWS RAM customer managed permission:** Yes

- ** [ListAliases](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListAliases.html) `kms:ListAliases` **
  - **Policy type:** IAM policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** `*`
  - **AWS KMS condition keys:** None
  - **AWS RAM customer managed permission:** No

- ** [ListGrants](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListGrants.html) `kms:ListGrants` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />*Other conditions:*<br />[kms:GrantIsForAWSResource](conditions-kms.md#conditions-kms-grant-is-for-aws-resource)
  - **AWS RAM customer managed permission:** Yes

- ** [ListKeyPolicies](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeyPolicies.html) `kms:ListKeyPolicies` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [ListKeyRotations](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeyRotations.html) `kms:ListKeyRotations` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [ListKeys](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html) `kms:ListKeys` You can use the same permission to list the KMS keys that other AWS accounts shared with you through AWS Resource Access Manager (AWS RAM) (the `ResourceOwners` parameter). For more information about identifying KMS keys that are shared with you, see [Identifying a shared KMS key](key-sharing-ram.md#key-sharing-ram-identify). **
  - **Policy type:** IAM policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** `*`
  - **AWS KMS condition keys:** None
  - **AWS RAM customer managed permission:** No

- ** [ListResourceTags](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListResourceTags.html) `kms:ListResourceTags` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [ListRetirableGrants](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListRetirableGrants.html) `kms:ListRetirableGrants` **
  - **Policy type:** IAM policy
  - **Cross-account use:** The specified principal must be in the local account, but the operation returns grants in all accounts.
  - **Resources (for IAM policies):** `*`
  - **AWS KMS condition keys:** None
  - **AWS RAM customer managed permission:** No

- ** [PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html) `kms:PutKeyPolicy` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />*Other conditions:*<br />[kms:BypassPolicyLockoutSafetyCheck](conditions-kms.md#conditions-kms-bypass-policy-lockout-safety-check)<br />[kms:PolicyName](conditions-kms.md#conditions-kms-policy-name)
  - **AWS RAM customer managed permission:** No

- ** [ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html) `kms:ReEncryptFrom` `kms:ReEncryptTo` To use this operation, the caller needs permission on two KMS keys: +  `kms:ReEncryptFrom` on the KMS key used to decrypt <br />+  `kms:ReEncryptTo` on the KMS key used to encrypt  **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for cryptographic operations*<br />[kms:EncryptionAlgorithm](conditions-kms.md#conditions-kms-encryption-algorithm)<br />[kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias)<br />*Encryption context conditions:*<br />[kms:EncryptionContext:*context-key*](conditions-kms.md#conditions-kms-encryption-context-keys)<br />[kms:EncryptionContextKeys](conditions-kms.md#conditions-kms-encryption-context-keys)<br />*Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />*Other conditions:* <br />[kms:ReEncryptOnSameKey](conditions-kms.md#conditions-kms-reencrypt-on-same-key)
  - **AWS RAM customer managed permission:** Yes

- ** [ReplicateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReplicateKey.html) `kms:ReplicateKey` To use this operation, the caller needs the following permissions: +  `kms:ReplicateKey` on the multi-Region primary key <br />+  `kms:CreateKey` in an IAM policy in the replica Region  **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />*Other conditions:* <br />[kms:ReplicaRegion](conditions-kms.md#conditions-kms-replica-region)
  - **AWS RAM customer managed permission:** Yes

- ** [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) `kms:RetireGrant` Permission to retire a grant is determined primarily by the grant. A policy alone cannot allow access to this operation. For more information, see [Retiring and revoking grants](grant-delete.md). **
  - **Policy type:** IAM policy <br />(This permission is not effective in a key policy.)
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Encryption context conditions:*<br />[kms:EncryptionContext:*context-key*](conditions-kms.md#conditions-kms-encryption-context-keys)<br />[kms:EncryptionContextKeys](conditions-kms.md#conditions-kms-encryption-context-keys)<br />*Grant conditions:*<br />[kms:GrantConstraintType](conditions-kms.md#conditions-kms-grant-constraint-type)<br />*Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes (has no effect on its own)

- ** [RevokeGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html) `kms:RevokeGrant` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />*Other conditions:*<br />[kms:GrantIsForAWSResource](conditions-kms.md#conditions-kms-grant-is-for-aws-resource)
  - **AWS RAM customer managed permission:** Yes

- ** [RotateKeyOnDemand](https://docs.aws.amazon.com/kms/latest/APIReference/API_RotateKeyOnDemand.html) `kms:RotateKeyOnDemand` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [ScheduleKeyDeletion](https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html) `kms:ScheduleKeyDeletion` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />*Key last usage condition:*<br />[kms:TrailingDaysWithoutKeyUsage](conditions-kms.md#conditions-kms-trailing-days-without-key-usage)
  - **AWS RAM customer managed permission:** Yes

- ** [Sign](https://docs.aws.amazon.com/kms/latest/APIReference/API_Sign.html) `kms:Sign` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for signing and verification:*<br />[kms:MessageType](conditions-kms.md#conditions-kms-message-type)[kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias)<br />[kms:SigningAlgorithm](conditions-kms.md#conditions-kms-signing-algorithm) <br />*Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [TagResource](https://docs.aws.amazon.com/kms/latest/APIReference/API_TagResource.html) `kms:TagResource` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />*Conditions for tagging:*<br />[aws:RequestTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag) (AWS global condition key)<br />[aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys) (AWS global condition key)
  - **AWS RAM customer managed permission:** Yes

- ** [UntagResource](https://docs.aws.amazon.com/kms/latest/APIReference/API_UntagResource.html) `kms:UntagResource` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />*Conditions for tagging:*<br />[aws:RequestTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag) (AWS global condition key)<br />[aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys) (AWS global condition key)
  - **AWS RAM customer managed permission:** Yes

- ** [UpdateAlias](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdateAlias.html) `kms:UpdateAlias` To use this operation, the caller needs `kms:UpdateAlias` permission on three resources: +  The alias <br />+  The currently associated KMS key  <br />+  The newly associated KMS key   For details, see [Controlling access to aliases](alias-access.md). **
  - **Policy type:** IAM policy (for the alias) / **Cross-account use:** No / **Resources (for IAM policies):** Alias / **AWS KMS condition keys:** None (when controlling access to the alias)
  - **Policy type:** Key policy (for the KMS keys) / **Cross-account use:** No / **Resources (for IAM policies):** KMS key / **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- **[UpdateCustomKeyStore](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdateCustomKeyStore.html)`kms:UpdateCustomKeyStore`**
  - **Policy type:** IAM policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** `*`
  - **AWS KMS condition keys:** [kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)
  - **AWS RAM customer managed permission:** No

- ** [UpdateKeyDescription](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdateKeyDescription.html) `kms:UpdateKeyDescription` **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- ** [UpdatePrimaryRegion](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdatePrimaryRegion.html) `kms:UpdatePrimaryRegion` To use this operation, the caller needs `kms:UpdatePrimaryRegion` permission on both the [multi-Region primary key](multi-region-keys-overview.md#mrk-primary-key) that will become a replica key and the [multi-Region replica key](multi-region-keys-overview.md#mrk-replica-key) that will become the primary key. **
  - **Policy type:** Key policy
  - **Cross-account use:** No
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)<br />*Other conditions*<br />[kms:PrimaryRegion](conditions-kms.md#conditions-kms-primary-region)
  - **AWS RAM customer managed permission:** Yes

- ** [Verify](https://docs.aws.amazon.com/kms/latest/APIReference/API_Verify.html) `kms:Verify` **
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for signing and verification:*<br />[kms:MessageType](conditions-kms.md#conditions-kms-message-type)[kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias)<br />[kms:SigningAlgorithm](conditions-kms.md#conditions-kms-signing-algorithm) <br />*Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)
  - **AWS RAM customer managed permission:** Yes

- **[VerifyMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_VerifyMac.html)`kms:VerifyMac`**
  - **Policy type:** Key policy
  - **Cross-account use:** Yes
  - **Resources (for IAM policies):** KMS key
  - **AWS KMS condition keys:** *Conditions for KMS key operations:*<br />[kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account)<br />[kms:KeySpec](conditions-kms.md#conditions-kms-key-spec)<br />[kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage)<br />[kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin)<br />[kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion)<br />[kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type)<br />[kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases)<br />[aws:ResourceTag/*tag-key*](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) (AWS global condition key)<br />[kms:ViaService](conditions-kms.md#conditions-kms-via-service)Conditions for cryptographic operations:<br />[kms:MacAlgorithm](conditions-kms.md#conditions-kms-mac-algorithm) <br />[kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias)
  - **AWS RAM customer managed permission:** Yes



## Column descriptions
<a name="permissions-column-descriptions"></a>

The columns in this table provide the following information:
+ **Actions and permissions **lists each AWS KMS API operation and the permission that allows the operation. You specify the operation in `Action` element of a policy statement.
+ **Policy type** indicates whether the permission can be used in a key policy or IAM policy. 

  *Key policy* means that you can specify the permission in the key policy. When the key policy contains the [policy statement that enables IAM policies](key-policy-default.md#key-policy-default-allow-root-enable-iam), you can specify the permission in an IAM policy. 

  *IAM policy* means that you can specify the permission only in an IAM policy.
+ **Cross-account use** shows the operations that authorized users can perform on resources in a different AWS account. 

  A value of *Yes* means that principals can perform the operation on resources in a different AWS account.

  A value of *No* means that principals can perform the operation only on resources in their own AWS account.

  If you give a principal in a different account a permission that can't be used on a cross-account resource, the permission is not effective. For example, if you give a principal in a different account [kms:TagResource](https://docs.aws.amazon.com/kms/latest/APIReference/API_TagResource.html) permission to a KMS key in your account, their attempts to tag the KMS key in your account will fail.
+ **Resources** lists the AWS KMS resources to which the permissions apply. AWS KMS supports two resource types: a KMS key and an alias. In a key policy, the value of the `Resource` element is always `*`, which indicates the KMS key to which the key policy is attached. 

  Use the following values to represent an AWS KMS resource in an IAM policy.  
**KMS key**  
When the resource is a KMS key, use its [key ARN](concepts.md#key-id-key-ARN). For help, see [Find the key ID and key ARN](find-cmk-id-arn.md).  
`arn:{{AWS_partition_name}}:kms:{{AWS_Region}}:{{AWS_account_ID}}:key/{{key_ID}}`  
For example:  
arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab  
**Alias**  
When the resource is an alias, use its [alias ARN](concepts.md#key-id-alias-ARN). For help, see [Find the alias name and alias ARN for a KMS key](alias-view.md).  
`arn:{{AWS_partition_name}}:kms:{{AWS_region}}:{{AWS_account_ID}}:alias/{{alias_name}}`  
For example:  
arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias  
**`*` (asterisk)**  
When the permission doesn't apply to a particular resource (KMS key or alias), use an asterisk (`*`).  
In an IAM policy for an AWS KMS permission, an asterisk in the `Resource` element indicates all AWS KMS resources (KMS keys and aliases). You can also use an asterisk in the `Resource` element when the AWS KMS permission doesn't apply to any particular KMS keys or aliases. For example, when allowing or denying `kms:CreateKey` or `kms:ListKeys` permission, you must set the `Resource` element to `*`.
+ **AWS KMS condition keys** lists the AWS KMS condition keys that you can use to control access to the operation. You specify conditions in a policy's `Condition` element. For more information, see [AWS KMS condition keys](conditions-kms.md). This column also includes [AWS global condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) that are supported by AWS KMS, but not by all AWS services.
+ **AWS RAM customer managed permission** shows whether a customer managed permission for a KMS key that you share through AWS Resource Access Manager (AWS RAM) can include the permission. A customer managed permission can't include `kms:PutKeyPolicy`, because a principal that can replace the key policy could give itself other permissions or lock the key's administrators out of the KMS key. For more information about customer managed permissions, see [Considerations for using managed permissions with KMS keys](key-sharing-ram.md#key-sharing-ram-cmp).