

# Actions, resources, and condition keys for AWS Key Management Service
<a name="list_kms"></a>

AWS Key Management Service (service prefix: `kms`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/kms/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/kms/latest/developerguide/control-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/kms/kms.json) for this service.

**Topics**
+ [API operations defined by AWS Key Management Service](#list_kms-operations)
+ [Actions defined by AWS Key Management Service](#list_kms-actions-as-permissions)
+ [Permission-only actions for AWS Key Management Service](#list_kms-permission-only-actions)
+ [Resource types defined by AWS Key Management Service](#list_kms-resources-for-iam-policies)
+ [Condition keys for AWS Key Management Service](#list_kms-policy-keys)

## API operations defined by AWS Key Management Service
<a name="list_kms-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_kms-actions-as-permissions).




- **   CancelKeyDeletion  **
  - **IAM action:**  [kms:CancelKeyDeletion](#list_kms-action-CancelKeyDeletion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ConnectCustomKeyStore  **
  - **IAM action:**  [kms:ConnectCustomKeyStore](#list_kms-action-ConnectCustomKeyStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAlias  **
  - **IAM action:**  [kms:CreateAlias](#list_kms-action-CreateAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCustomKeyStore  **
  - **IAM action:**  [kms:CreateCustomKeyStore](#list_kms-action-CreateCustomKeyStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGrant  **
  - **IAM action:**  [kms:CreateGrant](#list_kms-action-CreateGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   CreateKey  **
  - **IAM action:**  [kms:CreateKey](#list_kms-action-CreateKey)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kms:PutKeyPolicy](#list_kms-action-PutKeyPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [kms:TagResource](#list_kms-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   Decrypt  **
  - **IAM action:**  [kms:Decrypt](#list_kms-action-Decrypt) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAlias  **
  - **IAM action:**  [kms:DeleteAlias](#list_kms-action-DeleteAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomKeyStore  **
  - **IAM action:**  [kms:DeleteCustomKeyStore](#list_kms-action-DeleteCustomKeyStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteImportedKeyMaterial  **
  - **IAM action:**  [kms:DeleteImportedKeyMaterial](#list_kms-action-DeleteImportedKeyMaterial) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeriveSharedSecret  **
  - **IAM action:**  [kms:DeriveSharedSecret](#list_kms-action-DeriveSharedSecret) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeCustomKeyStores  **
  - **IAM action:**  [kms:DescribeCustomKeyStores](#list_kms-action-DescribeCustomKeyStores) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeKey  **
  - **IAM action:**  [kms:DescribeKey](#list_kms-action-DescribeKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableKey  **
  - **IAM action:**  [kms:DisableKey](#list_kms-action-DisableKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableKeyRotation  **
  - **IAM action:**  [kms:DisableKeyRotation](#list_kms-action-DisableKeyRotation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisconnectCustomKeyStore  **
  - **IAM action:**  [kms:DisconnectCustomKeyStore](#list_kms-action-DisconnectCustomKeyStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableKey  **
  - **IAM action:**  [kms:EnableKey](#list_kms-action-EnableKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableKeyRotation  **
  - **IAM action:**  [kms:EnableKeyRotation](#list_kms-action-EnableKeyRotation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   Encrypt  **
  - **IAM action:**  [kms:Encrypt](#list_kms-action-Encrypt) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GenerateDataKey  **
  - **IAM action:**  [kms:GenerateDataKey](#list_kms-action-GenerateDataKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GenerateDataKeyPair  **
  - **IAM action:**  [kms:GenerateDataKeyPair](#list_kms-action-GenerateDataKeyPair) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GenerateDataKeyPairWithoutPlaintext  **
  - **IAM action:**  [kms:GenerateDataKeyPairWithoutPlaintext](#list_kms-action-GenerateDataKeyPairWithoutPlaintext) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GenerateDataKeyWithoutPlaintext  **
  - **IAM action:**  [kms:GenerateDataKeyWithoutPlaintext](#list_kms-action-GenerateDataKeyWithoutPlaintext) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GenerateMac  **
  - **IAM action:**  [kms:GenerateMac](#list_kms-action-GenerateMac) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GenerateRandom  **
  - **IAM action:**  [kms:GenerateRandom](#list_kms-action-GenerateRandom) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetKeyLastUsage  **
  - **IAM action:**  [kms:GetKeyLastUsage](#list_kms-action-GetKeyLastUsage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetKeyPolicy  **
  - **IAM action:**  [kms:GetKeyPolicy](#list_kms-action-GetKeyPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetKeyRotationStatus  **
  - **IAM action:**  [kms:GetKeyRotationStatus](#list_kms-action-GetKeyRotationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetParametersForImport  **
  - **IAM action:**  [kms:GetParametersForImport](#list_kms-action-GetParametersForImport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPublicKey  **
  - **IAM action:**  [kms:GetPublicKey](#list_kms-action-GetPublicKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportKeyMaterial  **
  - **IAM action:**  [kms:ImportKeyMaterial](#list_kms-action-ImportKeyMaterial) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAliases  **
  - **IAM action:**  [kms:ListAliases](#list_kms-action-ListAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGrants  **
  - **IAM action:**  [kms:ListGrants](#list_kms-action-ListGrants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListKeyPolicies  **
  - **IAM action:**  [kms:ListKeyPolicies](#list_kms-action-ListKeyPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListKeyRotations  **
  - **IAM action:**  [kms:ListKeyRotations](#list_kms-action-ListKeyRotations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListKeys  **
  - **IAM action:**  [kms:ListKeys](#list_kms-action-ListKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceTags  **
  - **IAM action:**  [kms:ListResourceTags](#list_kms-action-ListResourceTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRetirableGrants  **
  - **IAM action:**  [kms:ListRetirableGrants](#list_kms-action-ListRetirableGrants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutKeyPolicy  **
  - **IAM action:**  [kms:PutKeyPolicy](#list_kms-action-PutKeyPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   ReEncrypt  **
  - **IAM action:**  [kms:ReEncryptFrom](#list_kms-action-ReEncryptFrom)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kms:ReEncryptTo](#list_kms-action-ReEncryptTo)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   ReplicateKey  **
  - **IAM action:**  [kms:ReplicateKey](#list_kms-action-ReplicateKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RetireGrant  **
  - **IAM action:**  [kms:RetireGrant](#list_kms-action-RetireGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RevokeGrant  **
  - **IAM action:**  [kms:RevokeGrant](#list_kms-action-RevokeGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RotateKeyOnDemand  **
  - **IAM action:**  [kms:RotateKeyOnDemand](#list_kms-action-RotateKeyOnDemand) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ScheduleKeyDeletion  **
  - **IAM action:**  [kms:ScheduleKeyDeletion](#list_kms-action-ScheduleKeyDeletion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   Sign  **
  - **IAM action:**  [kms:Sign](#list_kms-action-Sign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [kms:TagResource](#list_kms-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [kms:UntagResource](#list_kms-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAlias  **
  - **IAM action:**  [kms:UpdateAlias](#list_kms-action-UpdateAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCustomKeyStore  **
  - **IAM action:**  [kms:UpdateCustomKeyStore](#list_kms-action-UpdateCustomKeyStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateKeyDescription  **
  - **IAM action:**  [kms:UpdateKeyDescription](#list_kms-action-UpdateKeyDescription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePrimaryRegion  **
  - **IAM action:**  [kms:UpdatePrimaryRegion](#list_kms-action-UpdatePrimaryRegion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   Verify  **
  - **IAM action:**  [kms:Verify](#list_kms-action-Verify) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   VerifyMac  **
  - **IAM action:**  [kms:VerifyMac](#list_kms-action-VerifyMac) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Key Management Service
<a name="list_kms-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelKeyDeletion](https://docs.aws.amazon.com/kms/latest/APIReference/API_CancelKeyDeletion.html)  **
  - **Description:** Controls permission to cancel the scheduled deletion of an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [ConnectCustomKeyStore](https://docs.aws.amazon.com/kms/latest/APIReference/API_ConnectCustomKeyStore.html)  **
  - **Description:** Controls permission to connect or reconnect a custom key store to its associated AWS CloudHSM cluster or external key manager outside of AWS
  - **Resource types (\*required):** 
  - **Condition keys:** [kms:CallerAccount](#list_kms-kms_CallerAccount)
  - **Access level:** Write

- **   [CreateAlias](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateAlias.html)  **
  - **Description:** Controls permission to create an alias for an AWS KMS key. Aliases are optional friendly names that you can associate with KMS keys
  - **Resource types (\*required):** [alias\*](#list_kms-resource-alias) / **Condition keys:** [kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Resource types (\*required):** [key\*](#list_kms-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [CreateCustomKeyStore](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateCustomKeyStore.html)  **
  - **Description:** Controls permission to create a custom key store that is backed by an AWS CloudHSM cluster or an external key manager outside of AWS
  - **Resource types (\*required):** 
  - **Condition keys:** [kms:CallerAccount](#list_kms-kms_CallerAccount)
  - **Access level:** Write

- **   [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html)  **
  - **Description:** Controls permission to add a grant to an AWS KMS key. You can use grants to add permissions without changing the key policy or IAM policy
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:EncryptionContext:${EncryptionContextKey}](#list_kms-kms_EncryptionContext___EncryptionContextKey_)<br />[kms:EncryptionContextKeys](#list_kms-kms_EncryptionContextKeys)<br />[kms:GrantConstraintSourceArn](#list_kms-kms_GrantConstraintSourceArn)<br />[kms:GrantConstraintType](#list_kms-kms_GrantConstraintType)<br />[kms:GranteePrincipal](#list_kms-kms_GranteePrincipal)<br />[kms:GranteeServicePrincipal](#list_kms-kms_GranteeServicePrincipal)<br />[kms:GrantIsForAWSResource](#list_kms-kms_GrantIsForAWSResource)<br />[kms:GrantOperations](#list_kms-kms_GrantOperations)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:RetiringPrincipal](#list_kms-kms_RetiringPrincipal)<br />[kms:RetiringServicePrincipal](#list_kms-kms_RetiringServicePrincipal)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Permissions management, Write

- **   [CreateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html)  **
  - **Description:** Controls permission to create an AWS KMS key that can be used to protect data keys and other sensitive information
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kms-aws_TagKeys)<br />[kms:BypassPolicyLockoutSafetyCheck](#list_kms-kms_BypassPolicyLockoutSafetyCheck)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html)  **
  - **Description:** Controls permission to decrypt ciphertext that was encrypted under an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:EncryptionAlgorithm](#list_kms-kms_EncryptionAlgorithm)<br />[kms:EncryptionContext:${EncryptionContextKey}](#list_kms-kms_EncryptionContext___EncryptionContextKey_)<br />[kms:EncryptionContextKeys](#list_kms-kms_EncryptionContextKeys)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:RecipientAttestation:ImageSha384](#list_kms-kms_RecipientAttestation_ImageSha384)<br />[kms:RecipientAttestation:NitroTPMPCR0](#list_kms-kms_RecipientAttestation_NitroTPMPCR0)<br />[kms:RecipientAttestation:NitroTPMPCR1](#list_kms-kms_RecipientAttestation_NitroTPMPCR1)<br />[kms:RecipientAttestation:NitroTPMPCR10](#list_kms-kms_RecipientAttestation_NitroTPMPCR10)<br />[kms:RecipientAttestation:NitroTPMPCR11](#list_kms-kms_RecipientAttestation_NitroTPMPCR11)<br />[kms:RecipientAttestation:NitroTPMPCR12](#list_kms-kms_RecipientAttestation_NitroTPMPCR12)<br />[kms:RecipientAttestation:NitroTPMPCR13](#list_kms-kms_RecipientAttestation_NitroTPMPCR13)<br />[kms:RecipientAttestation:NitroTPMPCR14](#list_kms-kms_RecipientAttestation_NitroTPMPCR14)<br />[kms:RecipientAttestation:NitroTPMPCR15](#list_kms-kms_RecipientAttestation_NitroTPMPCR15)<br />[kms:RecipientAttestation:NitroTPMPCR16](#list_kms-kms_RecipientAttestation_NitroTPMPCR16)<br />[kms:RecipientAttestation:NitroTPMPCR17](#list_kms-kms_RecipientAttestation_NitroTPMPCR17)<br />[kms:RecipientAttestation:NitroTPMPCR18](#list_kms-kms_RecipientAttestation_NitroTPMPCR18)<br />[kms:RecipientAttestation:NitroTPMPCR19](#list_kms-kms_RecipientAttestation_NitroTPMPCR19)<br />[kms:RecipientAttestation:NitroTPMPCR2](#list_kms-kms_RecipientAttestation_NitroTPMPCR2)<br />[kms:RecipientAttestation:NitroTPMPCR20](#list_kms-kms_RecipientAttestation_NitroTPMPCR20)<br />[kms:RecipientAttestation:NitroTPMPCR21](#list_kms-kms_RecipientAttestation_NitroTPMPCR21)<br />[kms:RecipientAttestation:NitroTPMPCR22](#list_kms-kms_RecipientAttestation_NitroTPMPCR22)<br />[kms:RecipientAttestation:NitroTPMPCR23](#list_kms-kms_RecipientAttestation_NitroTPMPCR23)<br />[kms:RecipientAttestation:NitroTPMPCR3](#list_kms-kms_RecipientAttestation_NitroTPMPCR3)<br />[kms:RecipientAttestation:NitroTPMPCR4](#list_kms-kms_RecipientAttestation_NitroTPMPCR4)<br />[kms:RecipientAttestation:NitroTPMPCR5](#list_kms-kms_RecipientAttestation_NitroTPMPCR5)<br />[kms:RecipientAttestation:NitroTPMPCR6](#list_kms-kms_RecipientAttestation_NitroTPMPCR6)<br />[kms:RecipientAttestation:NitroTPMPCR7](#list_kms-kms_RecipientAttestation_NitroTPMPCR7)<br />[kms:RecipientAttestation:NitroTPMPCR8](#list_kms-kms_RecipientAttestation_NitroTPMPCR8)<br />[kms:RecipientAttestation:NitroTPMPCR9](#list_kms-kms_RecipientAttestation_NitroTPMPCR9)<br />[kms:RecipientAttestation:PCR0](#list_kms-kms_RecipientAttestation_PCR0)<br />[kms:RecipientAttestation:PCR1](#list_kms-kms_RecipientAttestation_PCR1)<br />[kms:RecipientAttestation:PCR10](#list_kms-kms_RecipientAttestation_PCR10)<br />[kms:RecipientAttestation:PCR11](#list_kms-kms_RecipientAttestation_PCR11)<br />[kms:RecipientAttestation:PCR12](#list_kms-kms_RecipientAttestation_PCR12)<br />[kms:RecipientAttestation:PCR13](#list_kms-kms_RecipientAttestation_PCR13)<br />[kms:RecipientAttestation:PCR14](#list_kms-kms_RecipientAttestation_PCR14)<br />[kms:RecipientAttestation:PCR15](#list_kms-kms_RecipientAttestation_PCR15)<br />[kms:RecipientAttestation:PCR16](#list_kms-kms_RecipientAttestation_PCR16)<br />[kms:RecipientAttestation:PCR17](#list_kms-kms_RecipientAttestation_PCR17)<br />[kms:RecipientAttestation:PCR18](#list_kms-kms_RecipientAttestation_PCR18)<br />[kms:RecipientAttestation:PCR19](#list_kms-kms_RecipientAttestation_PCR19)<br />[kms:RecipientAttestation:PCR2](#list_kms-kms_RecipientAttestation_PCR2)<br />[kms:RecipientAttestation:PCR20](#list_kms-kms_RecipientAttestation_PCR20)<br />[kms:RecipientAttestation:PCR21](#list_kms-kms_RecipientAttestation_PCR21)<br />[kms:RecipientAttestation:PCR22](#list_kms-kms_RecipientAttestation_PCR22)<br />[kms:RecipientAttestation:PCR23](#list_kms-kms_RecipientAttestation_PCR23)<br />[kms:RecipientAttestation:PCR24](#list_kms-kms_RecipientAttestation_PCR24)<br />[kms:RecipientAttestation:PCR25](#list_kms-kms_RecipientAttestation_PCR25)<br />[kms:RecipientAttestation:PCR26](#list_kms-kms_RecipientAttestation_PCR26)<br />[kms:RecipientAttestation:PCR27](#list_kms-kms_RecipientAttestation_PCR27)<br />[kms:RecipientAttestation:PCR28](#list_kms-kms_RecipientAttestation_PCR28)<br />[kms:RecipientAttestation:PCR29](#list_kms-kms_RecipientAttestation_PCR29)<br />[kms:RecipientAttestation:PCR3](#list_kms-kms_RecipientAttestation_PCR3)<br />[kms:RecipientAttestation:PCR30](#list_kms-kms_RecipientAttestation_PCR30)<br />[kms:RecipientAttestation:PCR31](#list_kms-kms_RecipientAttestation_PCR31)<br />[kms:RecipientAttestation:PCR4](#list_kms-kms_RecipientAttestation_PCR4)<br />[kms:RecipientAttestation:PCR5](#list_kms-kms_RecipientAttestation_PCR5)<br />[kms:RecipientAttestation:PCR6](#list_kms-kms_RecipientAttestation_PCR6)<br />[kms:RecipientAttestation:PCR7](#list_kms-kms_RecipientAttestation_PCR7)<br />[kms:RecipientAttestation:PCR8](#list_kms-kms_RecipientAttestation_PCR8)<br />[kms:RecipientAttestation:PCR9](#list_kms-kms_RecipientAttestation_PCR9)<br />[kms:RequestAlias](#list_kms-kms_RequestAlias)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [DeleteAlias](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeleteAlias.html)  **
  - **Description:** Controls permission to delete an alias. Aliases are optional friendly names that you can associate with AWS KMS keys
  - **Resource types (\*required):** [alias\*](#list_kms-resource-alias) / **Condition keys:** [kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Resource types (\*required):** [key\*](#list_kms-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [DeleteCustomKeyStore](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeleteCustomKeyStore.html)  **
  - **Description:** Controls permission to delete a custom key store
  - **Resource types (\*required):** 
  - **Condition keys:** [kms:CallerAccount](#list_kms-kms_CallerAccount)
  - **Access level:** Write

- **   [DeleteImportedKeyMaterial](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeleteImportedKeyMaterial.html)  **
  - **Description:** Controls permission to delete cryptographic material that you imported into an AWS KMS key. This action makes the key unusable
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html)  **
  - **Description:** Controls permission to use the specified AWS KMS key to derive shared secrets
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyAgreementAlgorithm](#list_kms-kms_KeyAgreementAlgorithm)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:RecipientAttestation:ImageSha384](#list_kms-kms_RecipientAttestation_ImageSha384)<br />[kms:RecipientAttestation:NitroTPMPCR0](#list_kms-kms_RecipientAttestation_NitroTPMPCR0)<br />[kms:RecipientAttestation:NitroTPMPCR1](#list_kms-kms_RecipientAttestation_NitroTPMPCR1)<br />[kms:RecipientAttestation:NitroTPMPCR10](#list_kms-kms_RecipientAttestation_NitroTPMPCR10)<br />[kms:RecipientAttestation:NitroTPMPCR11](#list_kms-kms_RecipientAttestation_NitroTPMPCR11)<br />[kms:RecipientAttestation:NitroTPMPCR12](#list_kms-kms_RecipientAttestation_NitroTPMPCR12)<br />[kms:RecipientAttestation:NitroTPMPCR13](#list_kms-kms_RecipientAttestation_NitroTPMPCR13)<br />[kms:RecipientAttestation:NitroTPMPCR14](#list_kms-kms_RecipientAttestation_NitroTPMPCR14)<br />[kms:RecipientAttestation:NitroTPMPCR15](#list_kms-kms_RecipientAttestation_NitroTPMPCR15)<br />[kms:RecipientAttestation:NitroTPMPCR16](#list_kms-kms_RecipientAttestation_NitroTPMPCR16)<br />[kms:RecipientAttestation:NitroTPMPCR17](#list_kms-kms_RecipientAttestation_NitroTPMPCR17)<br />[kms:RecipientAttestation:NitroTPMPCR18](#list_kms-kms_RecipientAttestation_NitroTPMPCR18)<br />[kms:RecipientAttestation:NitroTPMPCR19](#list_kms-kms_RecipientAttestation_NitroTPMPCR19)<br />[kms:RecipientAttestation:NitroTPMPCR2](#list_kms-kms_RecipientAttestation_NitroTPMPCR2)<br />[kms:RecipientAttestation:NitroTPMPCR20](#list_kms-kms_RecipientAttestation_NitroTPMPCR20)<br />[kms:RecipientAttestation:NitroTPMPCR21](#list_kms-kms_RecipientAttestation_NitroTPMPCR21)<br />[kms:RecipientAttestation:NitroTPMPCR22](#list_kms-kms_RecipientAttestation_NitroTPMPCR22)<br />[kms:RecipientAttestation:NitroTPMPCR23](#list_kms-kms_RecipientAttestation_NitroTPMPCR23)<br />[kms:RecipientAttestation:NitroTPMPCR3](#list_kms-kms_RecipientAttestation_NitroTPMPCR3)<br />[kms:RecipientAttestation:NitroTPMPCR4](#list_kms-kms_RecipientAttestation_NitroTPMPCR4)<br />[kms:RecipientAttestation:NitroTPMPCR5](#list_kms-kms_RecipientAttestation_NitroTPMPCR5)<br />[kms:RecipientAttestation:NitroTPMPCR6](#list_kms-kms_RecipientAttestation_NitroTPMPCR6)<br />[kms:RecipientAttestation:NitroTPMPCR7](#list_kms-kms_RecipientAttestation_NitroTPMPCR7)<br />[kms:RecipientAttestation:NitroTPMPCR8](#list_kms-kms_RecipientAttestation_NitroTPMPCR8)<br />[kms:RecipientAttestation:NitroTPMPCR9](#list_kms-kms_RecipientAttestation_NitroTPMPCR9)<br />[kms:RecipientAttestation:PCR0](#list_kms-kms_RecipientAttestation_PCR0)<br />[kms:RecipientAttestation:PCR1](#list_kms-kms_RecipientAttestation_PCR1)<br />[kms:RecipientAttestation:PCR10](#list_kms-kms_RecipientAttestation_PCR10)<br />[kms:RecipientAttestation:PCR11](#list_kms-kms_RecipientAttestation_PCR11)<br />[kms:RecipientAttestation:PCR12](#list_kms-kms_RecipientAttestation_PCR12)<br />[kms:RecipientAttestation:PCR13](#list_kms-kms_RecipientAttestation_PCR13)<br />[kms:RecipientAttestation:PCR14](#list_kms-kms_RecipientAttestation_PCR14)<br />[kms:RecipientAttestation:PCR15](#list_kms-kms_RecipientAttestation_PCR15)<br />[kms:RecipientAttestation:PCR16](#list_kms-kms_RecipientAttestation_PCR16)<br />[kms:RecipientAttestation:PCR17](#list_kms-kms_RecipientAttestation_PCR17)<br />[kms:RecipientAttestation:PCR18](#list_kms-kms_RecipientAttestation_PCR18)<br />[kms:RecipientAttestation:PCR19](#list_kms-kms_RecipientAttestation_PCR19)<br />[kms:RecipientAttestation:PCR2](#list_kms-kms_RecipientAttestation_PCR2)<br />[kms:RecipientAttestation:PCR20](#list_kms-kms_RecipientAttestation_PCR20)<br />[kms:RecipientAttestation:PCR21](#list_kms-kms_RecipientAttestation_PCR21)<br />[kms:RecipientAttestation:PCR22](#list_kms-kms_RecipientAttestation_PCR22)<br />[kms:RecipientAttestation:PCR23](#list_kms-kms_RecipientAttestation_PCR23)<br />[kms:RecipientAttestation:PCR24](#list_kms-kms_RecipientAttestation_PCR24)<br />[kms:RecipientAttestation:PCR25](#list_kms-kms_RecipientAttestation_PCR25)<br />[kms:RecipientAttestation:PCR26](#list_kms-kms_RecipientAttestation_PCR26)<br />[kms:RecipientAttestation:PCR27](#list_kms-kms_RecipientAttestation_PCR27)<br />[kms:RecipientAttestation:PCR28](#list_kms-kms_RecipientAttestation_PCR28)<br />[kms:RecipientAttestation:PCR29](#list_kms-kms_RecipientAttestation_PCR29)<br />[kms:RecipientAttestation:PCR3](#list_kms-kms_RecipientAttestation_PCR3)<br />[kms:RecipientAttestation:PCR30](#list_kms-kms_RecipientAttestation_PCR30)<br />[kms:RecipientAttestation:PCR31](#list_kms-kms_RecipientAttestation_PCR31)<br />[kms:RecipientAttestation:PCR4](#list_kms-kms_RecipientAttestation_PCR4)<br />[kms:RecipientAttestation:PCR5](#list_kms-kms_RecipientAttestation_PCR5)<br />[kms:RecipientAttestation:PCR6](#list_kms-kms_RecipientAttestation_PCR6)<br />[kms:RecipientAttestation:PCR7](#list_kms-kms_RecipientAttestation_PCR7)<br />[kms:RecipientAttestation:PCR8](#list_kms-kms_RecipientAttestation_PCR8)<br />[kms:RecipientAttestation:PCR9](#list_kms-kms_RecipientAttestation_PCR9)<br />[kms:RequestAlias](#list_kms-kms_RequestAlias)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [DescribeCustomKeyStores](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeCustomKeyStores.html)  **
  - **Description:** Controls permission to view detailed information about custom key stores in the account and region
  - **Resource types (\*required):** 
  - **Condition keys:** [kms:CallerAccount](#list_kms-kms_CallerAccount)
  - **Access level:** Read

- **   [DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html)  **
  - **Description:** Controls permission to view detailed information about an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:RequestAlias](#list_kms-kms_RequestAlias)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Read

- **   [DisableKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKey.html)  **
  - **Description:** Controls permission to disable an AWS KMS key, which prevents it from being used in cryptographic operations
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:TrailingDaysWithoutKeyUsage](#list_kms-kms_TrailingDaysWithoutKeyUsage)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [DisableKeyRotation](https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKeyRotation.html)  **
  - **Description:** Controls permission to disable automatic rotation of a customer managed AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [DisconnectCustomKeyStore](https://docs.aws.amazon.com/kms/latest/APIReference/API_DisconnectCustomKeyStore.html)  **
  - **Description:** Controls permission to disconnect the custom key store from its associated AWS CloudHSM cluster or external key manager outside of AWS
  - **Resource types (\*required):** 
  - **Condition keys:** [kms:CallerAccount](#list_kms-kms_CallerAccount)
  - **Access level:** Write

- **   [EnableKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKey.html)  **
  - **Description:** Controls permission to change the state of an AWS KMS key to enabled. This allows the KMS key to be used in cryptographic operations
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [EnableKeyRotation](https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKeyRotation.html)  **
  - **Description:** Controls permission to enable automatic rotation of the cryptographic material in an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:RotationPeriodInDays](#list_kms-kms_RotationPeriodInDays)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html)  **
  - **Description:** Controls permission to use the specified AWS KMS key to encrypt data and data keys
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:EncryptionAlgorithm](#list_kms-kms_EncryptionAlgorithm)<br />[kms:EncryptionContext:${EncryptionContextKey}](#list_kms-kms_EncryptionContext___EncryptionContextKey_)<br />[kms:EncryptionContextKeys](#list_kms-kms_EncryptionContextKeys)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:RequestAlias](#list_kms-kms_RequestAlias)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html)  **
  - **Description:** Controls permission to use the AWS KMS key to generate data keys. You can use the data keys to encrypt data outside of AWS KMS
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:EncryptionAlgorithm](#list_kms-kms_EncryptionAlgorithm)<br />[kms:EncryptionContext:${EncryptionContextKey}](#list_kms-kms_EncryptionContext___EncryptionContextKey_)<br />[kms:EncryptionContextKeys](#list_kms-kms_EncryptionContextKeys)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:RecipientAttestation:ImageSha384](#list_kms-kms_RecipientAttestation_ImageSha384)<br />[kms:RecipientAttestation:NitroTPMPCR0](#list_kms-kms_RecipientAttestation_NitroTPMPCR0)<br />[kms:RecipientAttestation:NitroTPMPCR1](#list_kms-kms_RecipientAttestation_NitroTPMPCR1)<br />[kms:RecipientAttestation:NitroTPMPCR10](#list_kms-kms_RecipientAttestation_NitroTPMPCR10)<br />[kms:RecipientAttestation:NitroTPMPCR11](#list_kms-kms_RecipientAttestation_NitroTPMPCR11)<br />[kms:RecipientAttestation:NitroTPMPCR12](#list_kms-kms_RecipientAttestation_NitroTPMPCR12)<br />[kms:RecipientAttestation:NitroTPMPCR13](#list_kms-kms_RecipientAttestation_NitroTPMPCR13)<br />[kms:RecipientAttestation:NitroTPMPCR14](#list_kms-kms_RecipientAttestation_NitroTPMPCR14)<br />[kms:RecipientAttestation:NitroTPMPCR15](#list_kms-kms_RecipientAttestation_NitroTPMPCR15)<br />[kms:RecipientAttestation:NitroTPMPCR16](#list_kms-kms_RecipientAttestation_NitroTPMPCR16)<br />[kms:RecipientAttestation:NitroTPMPCR17](#list_kms-kms_RecipientAttestation_NitroTPMPCR17)<br />[kms:RecipientAttestation:NitroTPMPCR18](#list_kms-kms_RecipientAttestation_NitroTPMPCR18)<br />[kms:RecipientAttestation:NitroTPMPCR19](#list_kms-kms_RecipientAttestation_NitroTPMPCR19)<br />[kms:RecipientAttestation:NitroTPMPCR2](#list_kms-kms_RecipientAttestation_NitroTPMPCR2)<br />[kms:RecipientAttestation:NitroTPMPCR20](#list_kms-kms_RecipientAttestation_NitroTPMPCR20)<br />[kms:RecipientAttestation:NitroTPMPCR21](#list_kms-kms_RecipientAttestation_NitroTPMPCR21)<br />[kms:RecipientAttestation:NitroTPMPCR22](#list_kms-kms_RecipientAttestation_NitroTPMPCR22)<br />[kms:RecipientAttestation:NitroTPMPCR23](#list_kms-kms_RecipientAttestation_NitroTPMPCR23)<br />[kms:RecipientAttestation:NitroTPMPCR3](#list_kms-kms_RecipientAttestation_NitroTPMPCR3)<br />[kms:RecipientAttestation:NitroTPMPCR4](#list_kms-kms_RecipientAttestation_NitroTPMPCR4)<br />[kms:RecipientAttestation:NitroTPMPCR5](#list_kms-kms_RecipientAttestation_NitroTPMPCR5)<br />[kms:RecipientAttestation:NitroTPMPCR6](#list_kms-kms_RecipientAttestation_NitroTPMPCR6)<br />[kms:RecipientAttestation:NitroTPMPCR7](#list_kms-kms_RecipientAttestation_NitroTPMPCR7)<br />[kms:RecipientAttestation:NitroTPMPCR8](#list_kms-kms_RecipientAttestation_NitroTPMPCR8)<br />[kms:RecipientAttestation:NitroTPMPCR9](#list_kms-kms_RecipientAttestation_NitroTPMPCR9)<br />[kms:RecipientAttestation:PCR0](#list_kms-kms_RecipientAttestation_PCR0)<br />[kms:RecipientAttestation:PCR1](#list_kms-kms_RecipientAttestation_PCR1)<br />[kms:RecipientAttestation:PCR10](#list_kms-kms_RecipientAttestation_PCR10)<br />[kms:RecipientAttestation:PCR11](#list_kms-kms_RecipientAttestation_PCR11)<br />[kms:RecipientAttestation:PCR12](#list_kms-kms_RecipientAttestation_PCR12)<br />[kms:RecipientAttestation:PCR13](#list_kms-kms_RecipientAttestation_PCR13)<br />[kms:RecipientAttestation:PCR14](#list_kms-kms_RecipientAttestation_PCR14)<br />[kms:RecipientAttestation:PCR15](#list_kms-kms_RecipientAttestation_PCR15)<br />[kms:RecipientAttestation:PCR16](#list_kms-kms_RecipientAttestation_PCR16)<br />[kms:RecipientAttestation:PCR17](#list_kms-kms_RecipientAttestation_PCR17)<br />[kms:RecipientAttestation:PCR18](#list_kms-kms_RecipientAttestation_PCR18)<br />[kms:RecipientAttestation:PCR19](#list_kms-kms_RecipientAttestation_PCR19)<br />[kms:RecipientAttestation:PCR2](#list_kms-kms_RecipientAttestation_PCR2)<br />[kms:RecipientAttestation:PCR20](#list_kms-kms_RecipientAttestation_PCR20)<br />[kms:RecipientAttestation:PCR21](#list_kms-kms_RecipientAttestation_PCR21)<br />[kms:RecipientAttestation:PCR22](#list_kms-kms_RecipientAttestation_PCR22)<br />[kms:RecipientAttestation:PCR23](#list_kms-kms_RecipientAttestation_PCR23)<br />[kms:RecipientAttestation:PCR24](#list_kms-kms_RecipientAttestation_PCR24)<br />[kms:RecipientAttestation:PCR25](#list_kms-kms_RecipientAttestation_PCR25)<br />[kms:RecipientAttestation:PCR26](#list_kms-kms_RecipientAttestation_PCR26)<br />[kms:RecipientAttestation:PCR27](#list_kms-kms_RecipientAttestation_PCR27)<br />[kms:RecipientAttestation:PCR28](#list_kms-kms_RecipientAttestation_PCR28)<br />[kms:RecipientAttestation:PCR29](#list_kms-kms_RecipientAttestation_PCR29)<br />[kms:RecipientAttestation:PCR3](#list_kms-kms_RecipientAttestation_PCR3)<br />[kms:RecipientAttestation:PCR30](#list_kms-kms_RecipientAttestation_PCR30)<br />[kms:RecipientAttestation:PCR31](#list_kms-kms_RecipientAttestation_PCR31)<br />[kms:RecipientAttestation:PCR4](#list_kms-kms_RecipientAttestation_PCR4)<br />[kms:RecipientAttestation:PCR5](#list_kms-kms_RecipientAttestation_PCR5)<br />[kms:RecipientAttestation:PCR6](#list_kms-kms_RecipientAttestation_PCR6)<br />[kms:RecipientAttestation:PCR7](#list_kms-kms_RecipientAttestation_PCR7)<br />[kms:RecipientAttestation:PCR8](#list_kms-kms_RecipientAttestation_PCR8)<br />[kms:RecipientAttestation:PCR9](#list_kms-kms_RecipientAttestation_PCR9)<br />[kms:RequestAlias](#list_kms-kms_RequestAlias)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [GenerateDataKeyPair](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPair.html)  **
  - **Description:** Controls permission to use the AWS KMS key to generate data key pairs
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:DataKeyPairSpec](#list_kms-kms_DataKeyPairSpec)<br />[kms:EncryptionAlgorithm](#list_kms-kms_EncryptionAlgorithm)<br />[kms:EncryptionContext:${EncryptionContextKey}](#list_kms-kms_EncryptionContext___EncryptionContextKey_)<br />[kms:EncryptionContextKeys](#list_kms-kms_EncryptionContextKeys)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:RecipientAttestation:ImageSha384](#list_kms-kms_RecipientAttestation_ImageSha384)<br />[kms:RecipientAttestation:NitroTPMPCR0](#list_kms-kms_RecipientAttestation_NitroTPMPCR0)<br />[kms:RecipientAttestation:NitroTPMPCR1](#list_kms-kms_RecipientAttestation_NitroTPMPCR1)<br />[kms:RecipientAttestation:NitroTPMPCR10](#list_kms-kms_RecipientAttestation_NitroTPMPCR10)<br />[kms:RecipientAttestation:NitroTPMPCR11](#list_kms-kms_RecipientAttestation_NitroTPMPCR11)<br />[kms:RecipientAttestation:NitroTPMPCR12](#list_kms-kms_RecipientAttestation_NitroTPMPCR12)<br />[kms:RecipientAttestation:NitroTPMPCR13](#list_kms-kms_RecipientAttestation_NitroTPMPCR13)<br />[kms:RecipientAttestation:NitroTPMPCR14](#list_kms-kms_RecipientAttestation_NitroTPMPCR14)<br />[kms:RecipientAttestation:NitroTPMPCR15](#list_kms-kms_RecipientAttestation_NitroTPMPCR15)<br />[kms:RecipientAttestation:NitroTPMPCR16](#list_kms-kms_RecipientAttestation_NitroTPMPCR16)<br />[kms:RecipientAttestation:NitroTPMPCR17](#list_kms-kms_RecipientAttestation_NitroTPMPCR17)<br />[kms:RecipientAttestation:NitroTPMPCR18](#list_kms-kms_RecipientAttestation_NitroTPMPCR18)<br />[kms:RecipientAttestation:NitroTPMPCR19](#list_kms-kms_RecipientAttestation_NitroTPMPCR19)<br />[kms:RecipientAttestation:NitroTPMPCR2](#list_kms-kms_RecipientAttestation_NitroTPMPCR2)<br />[kms:RecipientAttestation:NitroTPMPCR20](#list_kms-kms_RecipientAttestation_NitroTPMPCR20)<br />[kms:RecipientAttestation:NitroTPMPCR21](#list_kms-kms_RecipientAttestation_NitroTPMPCR21)<br />[kms:RecipientAttestation:NitroTPMPCR22](#list_kms-kms_RecipientAttestation_NitroTPMPCR22)<br />[kms:RecipientAttestation:NitroTPMPCR23](#list_kms-kms_RecipientAttestation_NitroTPMPCR23)<br />[kms:RecipientAttestation:NitroTPMPCR3](#list_kms-kms_RecipientAttestation_NitroTPMPCR3)<br />[kms:RecipientAttestation:NitroTPMPCR4](#list_kms-kms_RecipientAttestation_NitroTPMPCR4)<br />[kms:RecipientAttestation:NitroTPMPCR5](#list_kms-kms_RecipientAttestation_NitroTPMPCR5)<br />[kms:RecipientAttestation:NitroTPMPCR6](#list_kms-kms_RecipientAttestation_NitroTPMPCR6)<br />[kms:RecipientAttestation:NitroTPMPCR7](#list_kms-kms_RecipientAttestation_NitroTPMPCR7)<br />[kms:RecipientAttestation:NitroTPMPCR8](#list_kms-kms_RecipientAttestation_NitroTPMPCR8)<br />[kms:RecipientAttestation:NitroTPMPCR9](#list_kms-kms_RecipientAttestation_NitroTPMPCR9)<br />[kms:RecipientAttestation:PCR0](#list_kms-kms_RecipientAttestation_PCR0)<br />[kms:RecipientAttestation:PCR1](#list_kms-kms_RecipientAttestation_PCR1)<br />[kms:RecipientAttestation:PCR10](#list_kms-kms_RecipientAttestation_PCR10)<br />[kms:RecipientAttestation:PCR11](#list_kms-kms_RecipientAttestation_PCR11)<br />[kms:RecipientAttestation:PCR12](#list_kms-kms_RecipientAttestation_PCR12)<br />[kms:RecipientAttestation:PCR13](#list_kms-kms_RecipientAttestation_PCR13)<br />[kms:RecipientAttestation:PCR14](#list_kms-kms_RecipientAttestation_PCR14)<br />[kms:RecipientAttestation:PCR15](#list_kms-kms_RecipientAttestation_PCR15)<br />[kms:RecipientAttestation:PCR16](#list_kms-kms_RecipientAttestation_PCR16)<br />[kms:RecipientAttestation:PCR17](#list_kms-kms_RecipientAttestation_PCR17)<br />[kms:RecipientAttestation:PCR18](#list_kms-kms_RecipientAttestation_PCR18)<br />[kms:RecipientAttestation:PCR19](#list_kms-kms_RecipientAttestation_PCR19)<br />[kms:RecipientAttestation:PCR2](#list_kms-kms_RecipientAttestation_PCR2)<br />[kms:RecipientAttestation:PCR20](#list_kms-kms_RecipientAttestation_PCR20)<br />[kms:RecipientAttestation:PCR21](#list_kms-kms_RecipientAttestation_PCR21)<br />[kms:RecipientAttestation:PCR22](#list_kms-kms_RecipientAttestation_PCR22)<br />[kms:RecipientAttestation:PCR23](#list_kms-kms_RecipientAttestation_PCR23)<br />[kms:RecipientAttestation:PCR24](#list_kms-kms_RecipientAttestation_PCR24)<br />[kms:RecipientAttestation:PCR25](#list_kms-kms_RecipientAttestation_PCR25)<br />[kms:RecipientAttestation:PCR26](#list_kms-kms_RecipientAttestation_PCR26)<br />[kms:RecipientAttestation:PCR27](#list_kms-kms_RecipientAttestation_PCR27)<br />[kms:RecipientAttestation:PCR28](#list_kms-kms_RecipientAttestation_PCR28)<br />[kms:RecipientAttestation:PCR29](#list_kms-kms_RecipientAttestation_PCR29)<br />[kms:RecipientAttestation:PCR3](#list_kms-kms_RecipientAttestation_PCR3)<br />[kms:RecipientAttestation:PCR30](#list_kms-kms_RecipientAttestation_PCR30)<br />[kms:RecipientAttestation:PCR31](#list_kms-kms_RecipientAttestation_PCR31)<br />[kms:RecipientAttestation:PCR4](#list_kms-kms_RecipientAttestation_PCR4)<br />[kms:RecipientAttestation:PCR5](#list_kms-kms_RecipientAttestation_PCR5)<br />[kms:RecipientAttestation:PCR6](#list_kms-kms_RecipientAttestation_PCR6)<br />[kms:RecipientAttestation:PCR7](#list_kms-kms_RecipientAttestation_PCR7)<br />[kms:RecipientAttestation:PCR8](#list_kms-kms_RecipientAttestation_PCR8)<br />[kms:RecipientAttestation:PCR9](#list_kms-kms_RecipientAttestation_PCR9)<br />[kms:RequestAlias](#list_kms-kms_RequestAlias)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [GenerateDataKeyPairWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPairWithoutPlaintext.html)  **
  - **Description:** Controls permission to use the AWS KMS key to generate data key pairs. Unlike the GenerateDataKeyPair operation, this operation returns an encrypted private key without a plaintext copy
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:DataKeyPairSpec](#list_kms-kms_DataKeyPairSpec)<br />[kms:EncryptionAlgorithm](#list_kms-kms_EncryptionAlgorithm)<br />[kms:EncryptionContext:${EncryptionContextKey}](#list_kms-kms_EncryptionContext___EncryptionContextKey_)<br />[kms:EncryptionContextKeys](#list_kms-kms_EncryptionContextKeys)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:RequestAlias](#list_kms-kms_RequestAlias)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html)  **
  - **Description:** Controls permission to use the AWS KMS key to generate a data key. Unlike the GenerateDataKey operation, this operation returns an encrypted data key without a plaintext version of the data key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:EncryptionAlgorithm](#list_kms-kms_EncryptionAlgorithm)<br />[kms:EncryptionContext:${EncryptionContextKey}](#list_kms-kms_EncryptionContext___EncryptionContextKey_)<br />[kms:EncryptionContextKeys](#list_kms-kms_EncryptionContextKeys)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:RequestAlias](#list_kms-kms_RequestAlias)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html)  **
  - **Description:** Controls permission to use the AWS KMS key to generate message authentication codes
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MacAlgorithm](#list_kms-kms_MacAlgorithm)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:RequestAlias](#list_kms-kms_RequestAlias)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [GenerateRandom](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateRandom.html)  **
  - **Description:** Controls permission to get a cryptographically secure random byte string from AWS KMS
  - **Resource types (\*required):** 
  - **Condition keys:** [kms:RecipientAttestation:ImageSha384](#list_kms-kms_RecipientAttestation_ImageSha384)<br />[kms:RecipientAttestation:NitroTPMPCR0](#list_kms-kms_RecipientAttestation_NitroTPMPCR0)<br />[kms:RecipientAttestation:NitroTPMPCR1](#list_kms-kms_RecipientAttestation_NitroTPMPCR1)<br />[kms:RecipientAttestation:NitroTPMPCR10](#list_kms-kms_RecipientAttestation_NitroTPMPCR10)<br />[kms:RecipientAttestation:NitroTPMPCR11](#list_kms-kms_RecipientAttestation_NitroTPMPCR11)<br />[kms:RecipientAttestation:NitroTPMPCR12](#list_kms-kms_RecipientAttestation_NitroTPMPCR12)<br />[kms:RecipientAttestation:NitroTPMPCR13](#list_kms-kms_RecipientAttestation_NitroTPMPCR13)<br />[kms:RecipientAttestation:NitroTPMPCR14](#list_kms-kms_RecipientAttestation_NitroTPMPCR14)<br />[kms:RecipientAttestation:NitroTPMPCR15](#list_kms-kms_RecipientAttestation_NitroTPMPCR15)<br />[kms:RecipientAttestation:NitroTPMPCR16](#list_kms-kms_RecipientAttestation_NitroTPMPCR16)<br />[kms:RecipientAttestation:NitroTPMPCR17](#list_kms-kms_RecipientAttestation_NitroTPMPCR17)<br />[kms:RecipientAttestation:NitroTPMPCR18](#list_kms-kms_RecipientAttestation_NitroTPMPCR18)<br />[kms:RecipientAttestation:NitroTPMPCR19](#list_kms-kms_RecipientAttestation_NitroTPMPCR19)<br />[kms:RecipientAttestation:NitroTPMPCR2](#list_kms-kms_RecipientAttestation_NitroTPMPCR2)<br />[kms:RecipientAttestation:NitroTPMPCR20](#list_kms-kms_RecipientAttestation_NitroTPMPCR20)<br />[kms:RecipientAttestation:NitroTPMPCR21](#list_kms-kms_RecipientAttestation_NitroTPMPCR21)<br />[kms:RecipientAttestation:NitroTPMPCR22](#list_kms-kms_RecipientAttestation_NitroTPMPCR22)<br />[kms:RecipientAttestation:NitroTPMPCR23](#list_kms-kms_RecipientAttestation_NitroTPMPCR23)<br />[kms:RecipientAttestation:NitroTPMPCR3](#list_kms-kms_RecipientAttestation_NitroTPMPCR3)<br />[kms:RecipientAttestation:NitroTPMPCR4](#list_kms-kms_RecipientAttestation_NitroTPMPCR4)<br />[kms:RecipientAttestation:NitroTPMPCR5](#list_kms-kms_RecipientAttestation_NitroTPMPCR5)<br />[kms:RecipientAttestation:NitroTPMPCR6](#list_kms-kms_RecipientAttestation_NitroTPMPCR6)<br />[kms:RecipientAttestation:NitroTPMPCR7](#list_kms-kms_RecipientAttestation_NitroTPMPCR7)<br />[kms:RecipientAttestation:NitroTPMPCR8](#list_kms-kms_RecipientAttestation_NitroTPMPCR8)<br />[kms:RecipientAttestation:NitroTPMPCR9](#list_kms-kms_RecipientAttestation_NitroTPMPCR9)<br />[kms:RecipientAttestation:PCR0](#list_kms-kms_RecipientAttestation_PCR0)<br />[kms:RecipientAttestation:PCR1](#list_kms-kms_RecipientAttestation_PCR1)<br />[kms:RecipientAttestation:PCR10](#list_kms-kms_RecipientAttestation_PCR10)<br />[kms:RecipientAttestation:PCR11](#list_kms-kms_RecipientAttestation_PCR11)<br />[kms:RecipientAttestation:PCR12](#list_kms-kms_RecipientAttestation_PCR12)<br />[kms:RecipientAttestation:PCR13](#list_kms-kms_RecipientAttestation_PCR13)<br />[kms:RecipientAttestation:PCR14](#list_kms-kms_RecipientAttestation_PCR14)<br />[kms:RecipientAttestation:PCR15](#list_kms-kms_RecipientAttestation_PCR15)<br />[kms:RecipientAttestation:PCR16](#list_kms-kms_RecipientAttestation_PCR16)<br />[kms:RecipientAttestation:PCR17](#list_kms-kms_RecipientAttestation_PCR17)<br />[kms:RecipientAttestation:PCR18](#list_kms-kms_RecipientAttestation_PCR18)<br />[kms:RecipientAttestation:PCR19](#list_kms-kms_RecipientAttestation_PCR19)<br />[kms:RecipientAttestation:PCR2](#list_kms-kms_RecipientAttestation_PCR2)<br />[kms:RecipientAttestation:PCR20](#list_kms-kms_RecipientAttestation_PCR20)<br />[kms:RecipientAttestation:PCR21](#list_kms-kms_RecipientAttestation_PCR21)<br />[kms:RecipientAttestation:PCR22](#list_kms-kms_RecipientAttestation_PCR22)<br />[kms:RecipientAttestation:PCR23](#list_kms-kms_RecipientAttestation_PCR23)<br />[kms:RecipientAttestation:PCR24](#list_kms-kms_RecipientAttestation_PCR24)<br />[kms:RecipientAttestation:PCR25](#list_kms-kms_RecipientAttestation_PCR25)<br />[kms:RecipientAttestation:PCR26](#list_kms-kms_RecipientAttestation_PCR26)<br />[kms:RecipientAttestation:PCR27](#list_kms-kms_RecipientAttestation_PCR27)<br />[kms:RecipientAttestation:PCR28](#list_kms-kms_RecipientAttestation_PCR28)<br />[kms:RecipientAttestation:PCR29](#list_kms-kms_RecipientAttestation_PCR29)<br />[kms:RecipientAttestation:PCR3](#list_kms-kms_RecipientAttestation_PCR3)<br />[kms:RecipientAttestation:PCR30](#list_kms-kms_RecipientAttestation_PCR30)<br />[kms:RecipientAttestation:PCR31](#list_kms-kms_RecipientAttestation_PCR31)<br />[kms:RecipientAttestation:PCR4](#list_kms-kms_RecipientAttestation_PCR4)<br />[kms:RecipientAttestation:PCR5](#list_kms-kms_RecipientAttestation_PCR5)<br />[kms:RecipientAttestation:PCR6](#list_kms-kms_RecipientAttestation_PCR6)<br />[kms:RecipientAttestation:PCR7](#list_kms-kms_RecipientAttestation_PCR7)<br />[kms:RecipientAttestation:PCR8](#list_kms-kms_RecipientAttestation_PCR8)<br />[kms:RecipientAttestation:PCR9](#list_kms-kms_RecipientAttestation_PCR9)
  - **Access level:** Write

- **   [GetKeyLastUsage](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyLastUsage.html)  **
  - **Description:** Controls permission to view the last usage of an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Read

- **   [GetKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyPolicy.html)  **
  - **Description:** Controls permission to view the key policy for the specified AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Read

- **   [GetKeyRotationStatus](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyRotationStatus.html)  **
  - **Description:** Controls permission to view the key rotation status for an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Read

- **   [GetParametersForImport](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetParametersForImport.html)  **
  - **Description:** Controls permission to get data that is required to import cryptographic material into a customer managed key, including a public key and import token
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)<br />[kms:WrappingAlgorithm](#list_kms-kms_WrappingAlgorithm)<br />[kms:WrappingKeySpec](#list_kms-kms_WrappingKeySpec)
  - **Access level:** Read

- **   [GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html)  **
  - **Description:** Controls permission to download the public key of an asymmetric AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:RequestAlias](#list_kms-kms_RequestAlias)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Read

- **   [ImportKeyMaterial](https://docs.aws.amazon.com/kms/latest/APIReference/API_ImportKeyMaterial.html)  **
  - **Description:** Controls permission to import cryptographic material into an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:ExpirationModel](#list_kms-kms_ExpirationModel)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ValidTo](#list_kms-kms_ValidTo)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [ListAliases](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListAliases.html)  **
  - **Description:** Controls permission to view the aliases that are defined in the account. Aliases are optional friendly names that you can associate with AWS KMS keys
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGrants](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListGrants.html)  **
  - **Description:** Controls permission to view all grants for an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:GrantIsForAWSResource](#list_kms-kms_GrantIsForAWSResource)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** List

- **   [ListKeyPolicies](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeyPolicies.html)  **
  - **Description:** Controls permission to view the names of key policies for an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** List

- **   [ListKeyRotations](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeyRotations.html)  **
  - **Description:** Controls permission to view the list of key materials for an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** List

- **   [ListKeys](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html)  **
  - **Description:** Controls permission to view the key ID and Amazon Resource Name (ARN) of all AWS KMS keys in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceTags](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListResourceTags.html)  **
  - **Description:** Controls permission to view all tags that are attached to an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** List

- **   [ListRetirableGrants](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListRetirableGrants.html)  **
  - **Description:** Controls permission to view grants in which the specified principal is the retiring principal. Other principals might be able to retire the grant and this principal might be able to retire other grants
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html)  **
  - **Description:** Controls permission to replace the key policy for the specified AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:BypassPolicyLockoutSafetyCheck](#list_kms-kms_BypassPolicyLockoutSafetyCheck)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Permissions management, Write

- **   [ReEncryptFrom](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html)  **
  - **Description:** Controls permission to decrypt data as part of the process that decrypts and reencrypts the data within AWS KMS
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:EncryptionAlgorithm](#list_kms-kms_EncryptionAlgorithm)<br />[kms:EncryptionContext:${EncryptionContextKey}](#list_kms-kms_EncryptionContext___EncryptionContextKey_)<br />[kms:EncryptionContextKeys](#list_kms-kms_EncryptionContextKeys)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ReEncryptOnSameKey](#list_kms-kms_ReEncryptOnSameKey)<br />[kms:RequestAlias](#list_kms-kms_RequestAlias)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [ReEncryptTo](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html)  **
  - **Description:** Controls permission to encrypt data as part of the process that decrypts and reencrypts the data within AWS KMS
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:EncryptionAlgorithm](#list_kms-kms_EncryptionAlgorithm)<br />[kms:EncryptionContext:${EncryptionContextKey}](#list_kms-kms_EncryptionContext___EncryptionContextKey_)<br />[kms:EncryptionContextKeys](#list_kms-kms_EncryptionContextKeys)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ReEncryptOnSameKey](#list_kms-kms_ReEncryptOnSameKey)<br />[kms:RequestAlias](#list_kms-kms_RequestAlias)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [ReplicateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReplicateKey.html)  **
  - **Description:** Controls permission to replicate a multi-Region primary key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ReplicaRegion](#list_kms-kms_ReplicaRegion)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html)  **
  - **Description:** Controls permission to retire a grant. The RetireGrant operation is typically called by the grant user after they complete the tasks that the grant allowed them to perform
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:EncryptionContext:${EncryptionContextKey}](#list_kms-kms_EncryptionContext___EncryptionContextKey_)<br />[kms:EncryptionContextKeys](#list_kms-kms_EncryptionContextKeys)<br />[kms:GrantConstraintType](#list_kms-kms_GrantConstraintType)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Permissions management, Write

- **   [RevokeGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html)  **
  - **Description:** Controls permission to revoke a grant, which denies permission for all operations that depend on the grant
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:GrantIsForAWSResource](#list_kms-kms_GrantIsForAWSResource)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Permissions management, Write

- **   [RotateKeyOnDemand](https://docs.aws.amazon.com/kms/latest/APIReference/API_RotateKeyOnDemand.html)  **
  - **Description:** Controls permission to invoke on-demand rotation of the cryptographic material in an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [ScheduleKeyDeletion](https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html)  **
  - **Description:** Controls permission to schedule deletion of an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ScheduleKeyDeletionPendingWindowInDays](#list_kms-kms_ScheduleKeyDeletionPendingWindowInDays)<br />[kms:TrailingDaysWithoutKeyUsage](#list_kms-kms_TrailingDaysWithoutKeyUsage)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [Sign](https://docs.aws.amazon.com/kms/latest/APIReference/API_Sign.html)  **
  - **Description:** Controls permission to produce a digital signature for a message
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MessageType](#list_kms-kms_MessageType)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:RequestAlias](#list_kms-kms_RequestAlias)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:SigningAlgorithm](#list_kms-kms_SigningAlgorithm)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/kms/latest/APIReference/API_TagResource.html)  **
  - **Description:** Controls permission to create or update tags that are attached to an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kms-aws_TagKeys)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/kms/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Controls permission to delete tags that are attached to an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kms-aws_TagKeys)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Tagging, Write

- **   [UpdateAlias](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdateAlias.html)  **
  - **Description:** Controls permission to associate an alias with a different AWS KMS key. An alias is an optional friendly name that you can associate with a KMS key
  - **Resource types (\*required):** [alias\*](#list_kms-resource-alias) / **Condition keys:** [kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Resource types (\*required):** [key\*](#list_kms-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [UpdateCustomKeyStore](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdateCustomKeyStore.html)  **
  - **Description:** Controls permission to change the properties of a custom key store
  - **Resource types (\*required):** 
  - **Condition keys:** [kms:CallerAccount](#list_kms-kms_CallerAccount)
  - **Access level:** Write

- **   [UpdateKeyDescription](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdateKeyDescription.html)  **
  - **Description:** Controls permission to delete or change the description of an AWS KMS key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [UpdatePrimaryRegion](https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdatePrimaryRegion.html)  **
  - **Description:** Controls permission to update the primary Region of a multi-Region primary key
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:PrimaryRegion](#list_kms-kms_PrimaryRegion)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [Verify](https://docs.aws.amazon.com/kms/latest/APIReference/API_Verify.html)  **
  - **Description:** Controls permission to use the specified AWS KMS key to verify digital signatures
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MessageType](#list_kms-kms_MessageType)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:RequestAlias](#list_kms-kms_RequestAlias)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:SigningAlgorithm](#list_kms-kms_SigningAlgorithm)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write

- **   [VerifyMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_VerifyMac.html)  **
  - **Description:** Controls permission to use the AWS KMS key to verify message authentication codes
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:CallerAccount](#list_kms-kms_CallerAccount)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MacAlgorithm](#list_kms-kms_MacAlgorithm)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:RequestAlias](#list_kms-kms_RequestAlias)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)<br />[kms:ViaService](#list_kms-kms_ViaService)
  - **Access level:** Write



## Permission-only actions for AWS Key Management Service
<a name="list_kms-permission-only-actions"></a>

The following actions are defined by AWS Key Management Service but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [SynchronizeMultiRegionKey](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-auth.html#multi-region-auth-slr)  **
  - **Description:** Controls access to internal APIs that synchronize multi-Region keys
  - **Resource types (\*required):** [key\*](#list_kms-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases)
  - **Access level:** Write



## Resource types defined by AWS Key Management Service
<a name="list_kms-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [alias](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#alias-concept)  | arn:${Partition}:kms:${Region}:${Account}:alias/${Alias} |   | 
|  [key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys)  | arn:${Partition}:kms:${Region}:${Account}:key/${KeyId} | [aws:ResourceTag/${TagKey}](#list_kms-aws_ResourceTag___TagKey_)<br />[kms:KeyOrigin](#list_kms-kms_KeyOrigin)<br />[kms:KeySpec](#list_kms-kms_KeySpec)<br />[kms:KeyUsage](#list_kms-kms_KeyUsage)<br />[kms:MultiRegion](#list_kms-kms_MultiRegion)<br />[kms:MultiRegionKeyType](#list_kms-kms_MultiRegionKeyType)<br />[kms:ResourceAliases](#list_kms-kms_ResourceAliases) | 

## Condition keys for AWS Key Management Service
<a name="list_kms-policy-keys"></a>

AWS Key Management Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access to the specified AWS KMS operations based on both the key and value of the tag in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/kms/latest/developerguide/tag-authorization.html)  | Filters access to the specified AWS KMS operations based on tags assigned to the AWS KMS key | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access to the specified AWS KMS operations based on tag keys in the request | ArrayOfString | 
|   [kms:BypassPolicyLockoutSafetyCheck](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-bypass-policy-lockout-safety-check)  | Filters access to the CreateKey and PutKeyPolicy operations based on the value of the BypassPolicyLockoutSafetyCheck parameter in the request | Bool | 
|   [kms:CallerAccount](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-caller-account)  | Filters access to specified AWS KMS operations based on the AWS account ID of the caller. You can use this condition key to allow or deny access to all IAM users and roles in an AWS account in a single policy statement | String | 
|   [kms:CustomerMasterKeySpec](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-key-spec-replaced)  | The kms:CustomerMasterKeySpec condition key is deprecated. Instead, use the kms:KeySpec condition key | String | 
|   [kms:CustomerMasterKeyUsage](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-key-usage-replaced)  | The kms:CustomerMasterKeyUsage condition key is deprecated. Instead, use the kms:KeyUsage condition key | String | 
|   [kms:DataKeyPairSpec](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-data-key-pair-spec)  | Filters access to GenerateDataKeyPair and GenerateDataKeyPairWithoutPlaintext operations based on the value of the KeyPairSpec parameter in the request | String | 
|   [kms:EncryptionAlgorithm](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-encryption-algorithm)  | Filters access to encryption operations based on the value of the encryption algorithm in the request | String | 
|   [kms:EncryptionContext:${EncryptionContextKey}](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-encryption-context)  | Filters access to a symmetric AWS KMS key based on the encryption context in a cryptographic operation. This condition evaluates the key and value in each key-value encryption context pair | String | 
|   [kms:EncryptionContextKeys](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-encryption-context-keys)  | Filters access to a symmetric AWS KMS key based on the encryption context in a cryptographic operation. This condition key evaluates only the key in each key-value encryption context pair | ArrayOfString | 
|   [kms:ExpirationModel](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-expiration-model)  | Filters access to the ImportKeyMaterial operation based on the value of the ExpirationModel parameter in the request | String | 
|   [kms:GrantConstraintSourceArn](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-grant-constraint-source-arn)  | Filters access to the CreateGrant operation based on the value of SourceArn constraint in the request | ARN | 
|   [kms:GrantConstraintType](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-grant-constraint-type)  | Filters access to the CreateGrant operation based on the grant constraint in the request | String | 
|   [kms:GrantIsForAWSResource](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-grant-is-for-aws-resource)  | Filters access to the CreateGrant operation when the request comes from a specified AWS service | Bool | 
|   [kms:GrantOperations](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-grant-operations)  | Filters access to the CreateGrant operation based on the operations in the grant | ArrayOfString | 
|   [kms:GranteePrincipal](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-grantee-principal)  | Filters access to the CreateGrant operation based on the grantee principal in the grant | String | 
|   [kms:GranteeServicePrincipal](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-grantee-service-principal)  | Filters access to the CreateGrant operation based on the value of GranteeServicePrincipal in the request | String | 
|   [kms:KeyAgreementAlgorithm](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-key-agreement-algorithm)  | Filters access to the DeriveSharedSecret operation based on the value of the KeyAgreementAlgorithm parameter in the request | String | 
|   [kms:KeyOrigin](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-key-origin)  | Filters access to an API operation based on the Origin property of the AWS KMS key created by or used in the operation. Use it to qualify authorization of the CreateKey operation or any operation that is authorized for a KMS key | String | 
|   [kms:KeySpec](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-key-spec)  | Filters access to an API operation based on the KeySpec property of the AWS KMS key that is created by or used in the operation. Use it to qualify authorization of the CreateKey operation or any operation that is authorized for a KMS key resource | String | 
|   [kms:KeyUsage](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-key-usage)  | Filters access to an API operation based on the KeyUsage property of the AWS KMS key created by or used in the operation. Use it to qualify authorization of the CreateKey operation or any operation that is authorized for a KMS key resource | String | 
|   [kms:MacAlgorithm](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-mac-algorithm)  | Filters access to the GenerateMac and VerifyMac operations based on the MacAlgorithm parameter in the request | String | 
|   [kms:MessageType](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-message-type)  | Filters access to the Sign and Verify operations based on the value of the MessageType parameter in the request | String | 
|   [kms:MultiRegion](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-multi-region)  | Filters access to an API operation based on the MultiRegion property of the AWS KMS key created by or used in the operation. Use it to qualify authorization of the CreateKey operation or any operation that is authorized for a KMS key resource | Bool | 
|   [kms:MultiRegionKeyType](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-multi-region-key-type)  | Filters access to an API operation based on the MultiRegionKeyType property of the AWS KMS key created by or used in the operation. Use it to qualify authorization of the CreateKey operation or any operation that is authorized for a KMS key resource | String | 
|   [kms:PrimaryRegion](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-primary-region)  | Filters access to the UpdatePrimaryRegion operation based on the value of the PrimaryRegion parameter in the request | String | 
|   [kms:ReEncryptOnSameKey](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-reencrypt-on-same-key)  | Filters access to the ReEncrypt operation when it uses the same AWS KMS key that was used for the Encrypt operation | Bool | 
|   [kms:RecipientAttestation:ImageSha384](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-image-sha)  | Filters access to the API operations based on the image hash in the attestation document in the request | String | 
|   [kms:RecipientAttestation:NitroTPMPCR0](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 0 in the attestation document in the request. PCR0 is a contiguous measure of core system firmware executable code | String | 
|   [kms:RecipientAttestation:NitroTPMPCR1](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 1 in the attestation document in the request. PCR1 is a contiguous measure of core system firmware data/host platform configuration, typically including serial and model numbers | String | 
|   [kms:RecipientAttestation:NitroTPMPCR10](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 10 in the attestation document in the request. PCR10 is a contiguous measure of protection of the IMA measurement log | String | 
|   [kms:RecipientAttestation:NitroTPMPCR11](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 11 in the attestation document in the request. PCR11 is a contiguous measure of all components of unified kernel images (UKIs) | String | 
|   [kms:RecipientAttestation:NitroTPMPCR12](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 12 in the attestation document in the request. PCR12 is a contiguous measure of kernel command line, system credentials and system configuration images | String | 
|   [kms:RecipientAttestation:NitroTPMPCR13](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 13 in the attestation document in the request. PCR13 is a contiguous measure of all system extension images for the initrd | String | 
|   [kms:RecipientAttestation:NitroTPMPCR14](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 14 in the attestation document in the request. PCR14 is a contiguous measure of "MOK" certificates and hashes | String | 
|   [kms:RecipientAttestation:NitroTPMPCR15](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 15 in the attestation document in the request. PCR15 is a contiguous measure of root file system volume encryption key | String | 
|   [kms:RecipientAttestation:NitroTPMPCR16](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 16 in the attestation document in the request. PCR16 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:NitroTPMPCR17](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 17 in the attestation document in the request. PCR17 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:NitroTPMPCR18](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 18 in the attestation document in the request. PCR18 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:NitroTPMPCR19](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 19 in the attestation document in the request. PCR19 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:NitroTPMPCR2](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 2 in the attestation document in the request. PCR2 is a contiguous measure of extended or pluggable executable code, including option ROMs on pluggable hardware | String | 
|   [kms:RecipientAttestation:NitroTPMPCR20](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 20 in the attestation document in the request. PCR20 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:NitroTPMPCR21](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 21 in the attestation document in the request. PCR21 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:NitroTPMPCR22](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 22 in the attestation document in the request. PCR22 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:NitroTPMPCR23](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 23 in the attestation document in the request. PCR23 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:NitroTPMPCR3](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 3 in the attestation document in the request. PCR3 is a contiguous measure of extended or pluggable firmware data, including information about pluggable hardware | String | 
|   [kms:RecipientAttestation:NitroTPMPCR4](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 4 in the attestation document in the request. PCR4 is a contiguous measure of boot loader and additional drivers, including binaries and extensions loaded by the boot loader | String | 
|   [kms:RecipientAttestation:NitroTPMPCR5](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 5 in the attestation document in the request. PCR5 is a contiguous measure of GPT/Partition table | String | 
|   [kms:RecipientAttestation:NitroTPMPCR6](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 6 in the attestation document in the request. PCR6 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:NitroTPMPCR7](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 7 in the attestation document in the request. PCR7 is a contiguous measure of SecureBoot state | String | 
|   [kms:RecipientAttestation:NitroTPMPCR8](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 8 in the attestation document in the request. PCR8 is a contiguous measure of commands and kernel command line | String | 
|   [kms:RecipientAttestation:NitroTPMPCR9](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html#conditions-kms-recipient-nitro-tpm-pcrs)  | Filters access by the platform configuration register (PCR) 9 in the attestation document in the request. PCR9 is a contiguous measure of all files read (including kernel image) | String | 
|   [kms:RecipientAttestation:PCR0](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 0 in the attestation document in the request. PCR0 is a contiguous measure of the contents of the enclave image file, without the section data | String | 
|   [kms:RecipientAttestation:PCR1](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 1 in the attestation document in the request. PCR1 is a contiguous measurement of the Linux kernel and bootstrap data | String | 
|   [kms:RecipientAttestation:PCR10](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 10 in the attestation document in the request. PCR10 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR11](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 11 in the attestation document in the request. PCR11 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR12](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 12 in the attestation document in the request. PCR12 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR13](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 13 in the attestation document in the request. PCR13 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR14](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 14 in the attestation document in the request. PCR14 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR15](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 15 in the attestation document in the request. PCR15 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR16](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 16 in the attestation document in the request. PCR16 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR17](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 17 in the attestation document in the request. PCR17 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR18](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 18 in the attestation document in the request. PCR18 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR19](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 19 in the attestation document in the request. PCR19 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR2](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 2 in the attestation document in the request. PCR2 is a contiguous, in-order measurement of the user applications, without the boot ramfs | String | 
|   [kms:RecipientAttestation:PCR20](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 20 in the attestation document in the request. PCR20 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR21](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 21 in the attestation document in the request. PCR21 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR22](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 22 in the attestation document in the request. PCR22 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR23](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 23 in the attestation document in the request. PCR23 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR24](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 24 in the attestation document in the request. PCR24 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR25](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 25 in the attestation document in the request. PCR25 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR26](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 26 in the attestation document in the request. PCR26 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR27](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 27 in the attestation document in the request. PCR27 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR28](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 28 in the attestation document in the request. PCR28 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR29](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 29 in the attestation document in the request. PCR29 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR3](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 3 in the attestation document in the request. PCR3 is a contiguous measurement of the IAM role assigned to the parent instance | String | 
|   [kms:RecipientAttestation:PCR30](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 30 in the attestation document in the request. PCR30 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR31](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 31 in the attestation document in the request. PCR31 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR4](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 4 in the attestation document in the request. PCR4 is a contiguous measurement of the ID of the parent instance | String | 
|   [kms:RecipientAttestation:PCR5](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 5 in the attestation document in the request. PCR5 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR6](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 6 in the attestation document in the request. PCR6 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR7](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 7 in the attestation document in the request. PCR7 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:RecipientAttestation:PCR8](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 8 in the attestation document in the request. PCR8 is a measure of the signing certificate specified for the enclave image file | String | 
|   [kms:RecipientAttestation:PCR9](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclaves.html#conditions-kms-recipient-pcrs)  | Filters access by the platform configuration register (PCR) 9 in the attestation document in the request. PCR9 is a custom PCR that can be defined by the user for specific use cases | String | 
|   [kms:ReplicaRegion](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-replica-region)  | Filters access to the ReplicateKey operation based on the value of the ReplicaRegion parameter in the request | String | 
|   [kms:RequestAlias](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-request-alias)  | Filters access to cryptographic operations, DescribeKey, and GetPublicKey based on the alias in the request | String | 
|   [kms:ResourceAliases](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-resource-aliases)  | Filters access to specified AWS KMS operations based on aliases associated with the AWS KMS key | ArrayOfString | 
|   [kms:RetiringPrincipal](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-retiring-principal)  | Filters access to the CreateGrant operation based on the retiring principal in the grant | String | 
|   [kms:RetiringServicePrincipal](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-retiring-service-principal)  | Filters access to the CreateGrant operation based on the value of RetiringServicePrincipal in the request | String | 
|   [kms:RotationPeriodInDays](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-rotation-period-in-days)  | Filters access to the EnableKeyRotation operation based on the value of the RotationPeriodInDays parameter in the request | Numeric | 
|   [kms:ScheduleKeyDeletionPendingWindowInDays](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-schedule-key-deletion-pending-window-in-days)  | Filters access to the ScheduleKeyDeletion operation based on the value of the PendingWindowInDays parameter in the request | Numeric | 
|   [kms:SigningAlgorithm](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-signing-algorithm)  | Filters access to the Sign and Verify operations based on the signing algorithm in the request | String | 
|   [kms:TrailingDaysWithoutKeyUsage](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-trailing-days-without-key-usage)  | Filters access to the ScheduleKeyDeletion and DisableKey operations based on the number of days since the AWS KMS key was last used | Numeric | 
|   [kms:ValidTo](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-valid-to)  | Filters access to the ImportKeyMaterial operation based on the value of the ValidTo parameter in the request. You can use this condition key to allow users to import key material only when it expires by the specified date | Date | 
|   [kms:ViaService](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-via-service)  | Filters access when a request made on the principal's behalf comes from a specified AWS service | String | 
|   [kms:WrappingAlgorithm](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-wrapping-algorithm)  | Filters access to the GetParametersForImport operation based on the value of the WrappingAlgorithm parameter in the request | String | 
|   [kms:WrappingKeySpec](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-wrapping-key-spec)  | Filters access to the GetParametersForImport operation based on the value of the WrappingKeySpec parameter in the request | String | 