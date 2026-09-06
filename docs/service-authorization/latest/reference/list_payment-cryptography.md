

# Actions, resources, and condition keys for AWS Payment Cryptography
<a name="list_payment-cryptography"></a>

AWS Payment Cryptography (service prefix: `payment-cryptography`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/payment-cryptography/payment-cryptography.json) for this service.

**Topics**
+ [API operations defined by AWS Payment Cryptography](#list_payment-cryptography-operations)
+ [Actions defined by AWS Payment Cryptography](#list_payment-cryptography-actions-as-permissions)
+ [Resource types defined by AWS Payment Cryptography](#list_payment-cryptography-resources-for-iam-policies)
+ [Condition keys for AWS Payment Cryptography](#list_payment-cryptography-policy-keys)

## API operations defined by AWS Payment Cryptography
<a name="list_payment-cryptography-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_payment-cryptography-actions-as-permissions).




- **   AddKeyReplicationRegions  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:AddKeyReplicationRegions](#list_payment-cryptography-action-AddKeyReplicationRegions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateMpaTeam  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:AssociateMpaTeam](#list_payment-cryptography-action-AssociateMpaTeam) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAlias  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:CreateAlias](#list_payment-cryptography-action-CreateAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateKey  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:CreateKey](#list_payment-cryptography-action-CreateKey)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [payment-cryptography:TagResource](#list_payment-cryptography-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAlias  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:DeleteAlias](#list_payment-cryptography-action-DeleteAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteKey  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:DeleteKey](#list_payment-cryptography-action-DeleteKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:DeleteResourcePolicy](#list_payment-cryptography-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DisableDefaultKeyReplicationRegions  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:DisableDefaultKeyReplicationRegions](#list_payment-cryptography-action-DisableDefaultKeyReplicationRegions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateMpaTeam  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:DisassociateMpaTeam](#list_payment-cryptography-action-DisassociateMpaTeam) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableDefaultKeyReplicationRegions  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:EnableDefaultKeyReplicationRegions](#list_payment-cryptography-action-EnableDefaultKeyReplicationRegions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExportKey  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:ExportKey](#list_payment-cryptography-action-ExportKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAlias  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:GetAlias](#list_payment-cryptography-action-GetAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCertificateSigningRequest  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:GetCertificateSigningRequest](#list_payment-cryptography-action-GetCertificateSigningRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDefaultKeyReplicationRegions  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:GetDefaultKeyReplicationRegions](#list_payment-cryptography-action-GetDefaultKeyReplicationRegions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetKey  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:GetKey](#list_payment-cryptography-action-GetKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMpaTeamAssociation  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:GetMpaTeamAssociation](#list_payment-cryptography-action-GetMpaTeamAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetParametersForExport  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:GetParametersForExport](#list_payment-cryptography-action-GetParametersForExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetParametersForImport  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:GetParametersForImport](#list_payment-cryptography-action-GetParametersForImport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPublicKeyCertificate  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:GetPublicKeyCertificate](#list_payment-cryptography-action-GetPublicKeyCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:GetResourcePolicy](#list_payment-cryptography-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportKey  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:ImportKey](#list_payment-cryptography-action-ImportKey)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [payment-cryptography:TagResource](#list_payment-cryptography-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ListAliases  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:ListAliases](#list_payment-cryptography-action-ListAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListKeys  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:ListKeys](#list_payment-cryptography-action-ListKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:ListTagsForResource](#list_payment-cryptography-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutResourcePolicy  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:PutResourcePolicy](#list_payment-cryptography-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RemoveKeyReplicationRegions  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:RemoveKeyReplicationRegions](#list_payment-cryptography-action-RemoveKeyReplicationRegions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreKey  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:RestoreKey](#list_payment-cryptography-action-RestoreKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartKeyUsage  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:StartKeyUsage](#list_payment-cryptography-action-StartKeyUsage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopKeyUsage  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:StopKeyUsage](#list_payment-cryptography-action-StopKeyUsage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:TagResource](#list_payment-cryptography-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:UntagResource](#list_payment-cryptography-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAlias  **
  - **SDK client:** payment-cryptography
  - **IAM action:**  [payment-cryptography:UpdateAlias](#list_payment-cryptography-action-UpdateAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Payment Cryptography
<a name="list_payment-cryptography-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddKeyReplicationRegions](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_AddKeyReplicationRegions.html)  **
  - **Description:** Grants permission to add replication regions to an existing AWS Payment Cryptography key
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [AssociateMpaTeam](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_AssociateMpaTeam.html)  **
  - **Description:** Grants permission to associate an MPA approval team with a payment cryptography action
  - **Resource types (\*required):** [approval-team\*](#list_payment-cryptography-resource-approval-team)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateAlias.html)  **
  - **Description:** Grants permission to create a user-friendly name for a Key
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html)  **
  - **Description:** Grants permission to create a unique customer managed key in the caller's AWS account and region
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_payment-cryptography-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_payment-cryptography-aws_TagKeys)<br />[payment-cryptography:DeriveKeyUsage](#list_payment-cryptography-payment-cryptography_DeriveKeyUsage)<br />[payment-cryptography:KeyAlgorithm](#list_payment-cryptography-payment-cryptography_KeyAlgorithm)<br />[payment-cryptography:KeyClass](#list_payment-cryptography-payment-cryptography_KeyClass)<br />[payment-cryptography:KeyUsage](#list_payment-cryptography-payment-cryptography_KeyUsage)
  - **Access level:** Write

- **   [DecryptData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DecryptData.html)  **
  - **Description:** Grants permission to decrypt ciphertext data to plaintext using symmetric, asymmetric or DUKPT data encryption key
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [DeleteAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html)  **
  - **Description:** Grants permission to delete the specified alias
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_payment-cryptography-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_payment-cryptography-aws_TagKeys)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [DeleteKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html)  **
  - **Description:** Grants permission to schedule the deletion of a Key
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete the resource-based policy attached to a key
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Permissions management, Write

- **   [DisableDefaultKeyReplicationRegions](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DisableDefaultKeyReplicationRegions.html)  **
  - **Description:** Grants permission to disable default key replication regions for account-level replication
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateMpaTeam](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DisassociateMpaTeam.html)  **
  - **Description:** Grants permission to disassociate an MPA approval team from a payment cryptography action
  - **Resource types (\*required):** [approval-team\*](#list_payment-cryptography-resource-approval-team)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableDefaultKeyReplicationRegions](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_EnableDefaultKeyReplicationRegions.html)  **
  - **Description:** Grants permission to enable default key replication regions for account-level replication
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [EncryptData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EncryptData.html)  **
  - **Description:** Grants permission to encrypt plaintext data to ciphertext using symmetric, asymmetric or DUKPT data encryption key
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [ExportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportKey.html)  **
  - **Description:** Grants permission to export a key from the service
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:CertificateAuthorityPublicKeyIdentifier](#list_payment-cryptography-payment-cryptography_CertificateAuthorityPublicKeyIdentifier)<br />[payment-cryptography:ExportDukptInitialKey](#list_payment-cryptography-payment-cryptography_ExportDukptInitialKey)<br />[payment-cryptography:ExportKeyMaterial](#list_payment-cryptography-payment-cryptography_ExportKeyMaterial)<br />[payment-cryptography:PrivateKeyIdentifier](#list_payment-cryptography-payment-cryptography_PrivateKeyIdentifier)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)<br />[payment-cryptography:SigningKeyIdentifier](#list_payment-cryptography-payment-cryptography_SigningKeyIdentifier)<br />[payment-cryptography:WrappingKeyIdentifier](#list_payment-cryptography-payment-cryptography_WrappingKeyIdentifier)
  - **Access level:** Write

- **   [GenerateAs2805KekValidation](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateAs2805KekValidation.html)  **
  - **Description:** Grants permission to generate a KekValidationRequest or a KekValidationResponse for node-to-node initialization between payment processing nodes using Australian Standard 2805 (AS2805)
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [GenerateAuthRequestCryptogram](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateAuthRequestCryptogram.html)  **
  - **Description:** Grants permission to generate an Authorization Request Cryptogram (ARQC) for an EMV chip payment card authorization
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [GenerateCardValidationData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateCardValidationData.html)  **
  - **Description:** Grants permission to generate card-related data using algorithms such as Card Verification Values (CVV/CVV2), Dynamic Card Verification Values (dCVV/dCVV2) or Card Security Codes (CSC) that check the validity of a magnetic stripe card
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [GenerateMac](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateMac.html)  **
  - **Description:** Grants permission to generate a MAC (Message Authentication Code) cryptogram
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [GenerateMacEmvPinChange](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateMacEmvPinChange.html)  **
  - **Description:** Grants permission to generate a MAC (Message Authentication Code) cryptogram
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [GeneratePinData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GeneratePinData.html)  **
  - **Description:** Grants permission to generate pin-related data such as PIN, PIN Verification Value (PVV), PIN Block and PIN Offset during new card issuance or card re-issuance
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [GetAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetAlias.html)  **
  - **Description:** Grants permission to return the keyArn associated with an aliasName
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_payment-cryptography-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_payment-cryptography-aws_TagKeys)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_payment-cryptography-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_payment-cryptography-aws_TagKeys)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Read

- **   [GetCertificateSigningRequest](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetCertificateSigningRequest.html)  **
  - **Description:** Grants permission to return the Certificate Signing Request for a public key from a key of class PUBLIC\_KEY
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Read

- **   [GetDefaultKeyReplicationRegions](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetDefaultKeyReplicationRegions.html)  **
  - **Description:** Grants permission to retrieve the default key replication regions configured at the account level
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetKey.html)  **
  - **Description:** Grants permission to return the detailed information about the specified key
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Read

- **   [GetMpaTeamAssociation](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetMpaTeamAssociation.html)  **
  - **Description:** Grants permission to retrieve information about an MPA approval team association for a payment cryptography action
  - **Resource types (\*required):** [approval-team\*](#list_payment-cryptography-resource-approval-team)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetParametersForExport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForExport.html)  **
  - **Description:** Grants permission to get the export token and the signing key certificate to initiate a TR-34 key export
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetParametersForImport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html)  **
  - **Description:** Grants permission to get the import token and the wrapping key certificate to initiate a TR-34 key import
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPublicKeyCertificate](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetPublicKeyCertificate.html)  **
  - **Description:** Grants permission to return the public key from a key of class PUBLIC\_KEY
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to retrieve the resource-based policy attached to a key
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Read

- **   [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html)  **
  - **Description:** Grants permission to imports keys and public key certificates
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_payment-cryptography-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_payment-cryptography-aws_TagKeys)<br />[payment-cryptography:CertificateAuthorityPublicKeyIdentifier](#list_payment-cryptography-payment-cryptography_CertificateAuthorityPublicKeyIdentifier)<br />[payment-cryptography:ImportKeyMaterial](#list_payment-cryptography-payment-cryptography_ImportKeyMaterial)<br />[payment-cryptography:PrivateKeyIdentifier](#list_payment-cryptography-payment-cryptography_PrivateKeyIdentifier)<br />[payment-cryptography:WrappingKeyIdentifier](#list_payment-cryptography-payment-cryptography_WrappingKeyIdentifier)
  - **Access level:** Write

- **   [ListAliases](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html)  **
  - **Description:** Grants permission to return a list of aliases created for all keys in the caller's AWS account and Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListKeys](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListKeys.html)  **
  - **Description:** Grants permission to return a list of keys created in the caller's AWS account and Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to return a list of tags created in the caller's AWS account and Region
  - **Resource types (\*required):** [key](#list_payment-cryptography-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Read

- **   [PutResourcePolicy](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to attach or replace a resource-based policy on a key
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Permissions management, Write

- **   [ReEncryptData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_ReEncryptData.html)  **
  - **Description:** Grants permission to re-encrypt ciphertext using DUKPT, Symmetric and Asymmetric Data Encryption Keys
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [RemoveKeyReplicationRegions](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_RemoveKeyReplicationRegions.html)  **
  - **Description:** Grants permission to remove replication regions from an existing AWS Payment Cryptography key
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [RestoreKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_RestoreKey.html)  **
  - **Description:** Grants permission to cancel a scheduled key deletion if at any point during the waiting period a Key needs to be revived
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [StartKeyUsage](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StartKeyUsage.html)  **
  - **Description:** Grants permission to enable a disabled Key
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [StopKeyUsage](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StopKeyUsage.html)  **
  - **Description:** Grants permission to disable an enabled Key
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or overwrites one or more tags for the specified resource
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_payment-cryptography-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_payment-cryptography-aws_TagKeys)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Tagging, Write

- **   [TranslateKeyMaterial](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_TranslateKeyMaterial.html)  **
  - **Description:** Grants permission to translate wrapping key type for a wrapped key
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [TranslatePinData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_TranslatePinData.html)  **
  - **Description:** Grants permission to translate encrypted PIN block from and to ISO 9564 formats 0,1,3,4
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the specified tag or tags from the specified resource
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_payment-cryptography-aws_TagKeys)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Tagging, Write

- **   [UpdateAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html)  **
  - **Description:** Grants permission to change the key to which an alias is assigned, or unassign it from its current key
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_payment-cryptography-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_payment-cryptography-aws_TagKeys)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_payment-cryptography-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_payment-cryptography-aws_TagKeys)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [VerifyAuthRequestCryptogram](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyAuthRequestCryptogram.html)  **
  - **Description:** Grants permission to verify Authorization Request Cryptogram (ARQC) for a EMV chip payment card authorization
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [VerifyCardValidationData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyCardValidationData.html)  **
  - **Description:** Grants permission to verify card-related validation data using algorithms such as Card Verification Values (CVV/CVV2), Dynamic Card Verification Values (dCVV/dCVV2) and Card Security Codes (CSC)
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [VerifyMac](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyMac.html)  **
  - **Description:** Grants permission to verify MAC (Message Authentication Code) of input data against a provided MAC
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write

- **   [VerifyPinData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyPinData.html)  **
  - **Description:** Grants permission to verify pin-related data such as PIN and PIN Offset using algorithms including VISA PVV and IBM3624
  - **Resource types (\*required):** [alias\*](#list_payment-cryptography-resource-alias) / **Condition keys:** [payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Resource types (\*required):** [key\*](#list_payment-cryptography-resource-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:RequestAlias](#list_payment-cryptography-payment-cryptography_RequestAlias)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases)
  - **Access level:** Write



## Resource types defined by AWS Payment Cryptography
<a name="list_payment-cryptography-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [alias](${APIReferenceDocPage}API_Alias.html)  | arn:${Partition}:payment-cryptography:${Region}:${Account}:alias/${Alias} | [payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases) | 
|  [approval-team](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html)  | arn:${Partition}:mpa:${Region}:${Account}:approval-team/${ApprovalTeamId} | [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_) | 
|  [key](${APIReferenceDocPage}API_Key.html)  | arn:${Partition}:payment-cryptography:${Region}:${Account}:key/${KeyId} | [aws:ResourceTag/${TagKey}](#list_payment-cryptography-aws_ResourceTag___TagKey_)<br />[payment-cryptography:ResourceAliases](#list_payment-cryptography-payment-cryptography_ResourceAliases) | 

## Condition keys for AWS Payment Cryptography
<a name="list_payment-cryptography-policy-keys"></a>

AWS Payment Cryptography defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by both the key and value of the tag in the request for the specified operation | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags assigned to a key for the specified operation | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in the request for the specified operation | ArrayOfString | 
|   [payment-cryptography:CertificateAuthorityPublicKeyIdentifier](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html)  | Filters access by the CertificateAuthorityPublicKeyIdentifier specified in the request or the ImportKey, and ExportKey operations | String | 
|   [payment-cryptography:DeriveKeyUsage](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html)  | Filters access by the DeriveKeyUsage specified in the request for the CreateKey operation | String | 
|   [payment-cryptography:ExportDukptInitialKey](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html)  | Filters access by whether the request is to export a DUKPT initial key for the ExportKey operation | Bool | 
|   [payment-cryptography:ExportKeyMaterial](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html)  | Filters access by the type of key material being exported [Tr34KeyBlock, Tr31KeyBlock, DiffieHellmanTr31KeyBlock, As2805KeyCryptogram, KeyCryptogram] for the ExportKey operation | String | 
|   [payment-cryptography:ImportKeyMaterial](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html)  | Filters access by the type of key material being imported [RootCertificatePublicKey, TrustedCertificatePublicKey, Tr34KeyBlock, Tr31KeyBlock, DiffieHellmanTr31KeyBlock, As2805KeyCryptogram, KeyCryptogram] for the ImportKey operation | String | 
|   [payment-cryptography:KeyAlgorithm](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html)  | Filters access by KeyAlgorithm specified in the request for the CreateKey operation | String | 
|   [payment-cryptography:KeyClass](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html)  | Filters access by KeyClass specified in the request for the CreateKey operation | String | 
|   [payment-cryptography:KeyUsage](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html)  | Filters access by KeyUsage specified in the request or associated with a key for the CreateKey operation | String | 
|   [payment-cryptography:PrivateKeyIdentifier](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html)  | Filters access by the PrivateKeyIdentifier specified in the request for the ImportKey and ExportKey operations | String | 
|   [payment-cryptography:RequestAlias](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html)  | Filters access by aliases in the request for the specified operation | String | 
|   [payment-cryptography:ResourceAliases](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html)  | Filters access by aliases associated with a key for the specified operation | ArrayOfString | 
|   [payment-cryptography:SigningKeyIdentifier](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html)  | Filters access by the SigningKeyIdentifier specified in the request for the ExportKey operation | String | 
|   [payment-cryptography:WrappingKeyIdentifier](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security-iam.html)  | Filters access by the WrappingKeyIdentifier specified in the request for the ImportKey, and ExportKey operations | String | 