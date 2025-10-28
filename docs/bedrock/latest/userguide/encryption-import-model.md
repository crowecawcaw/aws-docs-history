# Encryption of imported custom models

Amazon Bedrock supports creating custom models through two methods that both use the same encryption approach. Your custom models are managed and stored by AWS:

- **Custom model import jobs** — For importing customized open-source foundation models (such as Mistral AI or Llama models).
- **Create custom model** — For importing Amazon Nova models that you customized in SageMaker AI.
  For encryption of your custom models, Amazon Bedrock provides the following options:

- **AWS owned keys** – By default, Amazon Bedrock encrypts imported custom models with AWS owned keys. You can't view, manage, or use AWS owned keys, or audit their use.
  However, you don't have to take any action or change any programs to protect the keys that encrypt your data. For more information, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk")
  in the _AWS Key Management Service Developer Guide_.
- **Customer managed keys (CMK)** – You can choose to add a second layer of encryption over the existing AWS owned encryption keys by choosing a customer managed key(CMK). You create,
  own, and manage your customer managed keys.

Because you have full control of this layer of encryption, in it you can perform the following tasks:

    + Establish and maintain key policies
    + Establish and maintain IAM policies and grants
    + Enable and disable key policies
    + Rotate key cryptographic material
    + Add tags
    + Create key aliases
    + Schedule keys for deletion

For more information, see [customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer Guide_.

###### Note

For all the custom models that you import, Amazon Bedrock automatically enables encryption at rest using AWS owned keys to protect customer data at no charge.
If you use a customer managed key, AWS KMS charges apply. For more information about pricing, see [AWS Key Management Service Pricing.](../../../index.md "../../../index.md").

## How Amazon Bedrock uses grants in AWS KMS

If you specify a customer managed key to encrypt the imported model. Amazon Bedrock creates a **primary** AWS KMS [grant](../../../index.md "../../../index.md")
associated with the imported model on your behalf by sending a [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") request to AWS KMS.
This grant allows Amazon Bedrock to access and use your customer managed key. Grants in AWS KMS are used to give Amazon Bedrock access to a KMS key in a customer’s account.

Amazon Bedrock requires the primary grant to use your customer managed key for the following internal operations:

- Send [DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") requests to AWS KMS to verify that the symmetric customer managed KMS key ID
  you entered when creating the job is valid.
- Send [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") and [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") requests to AWS KMS
  to generate data keys encrypted by your customer managed key and decrypt the encrypted data keys so that they can be used to encrypt the model artifacts.
- Send [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") requests to AWS KMS to create scoped down secondary grants with a subset of the above operations (`DescribeKey`, `GenerateDataKey`, `Decrypt`),
  for the asynchronous execution of model import and for on-demand inference.
- Amazon Bedrock specifies a retiring principal during the creation of grants, so the service can send a [RetireGrant](../../../kms/latest/APIReference/API_RetireGrant.md "../../../kms/latest/APIReference/API_RetireGrant.md") request.

You have full access to your customer managed AWS KMS key. You can revoke access to the grant by following the steps at [Retiring and revoking grants](../../../kms/latest/developerguide/grant-manage.md#grant-delete "../../../kms/latest/developerguide/grant-manage.md#grant-delete")
in the _AWS Key Management Service Developer Guide_ or remove the service’s access to your customer managed key at any time by modifying the key policy. If you do so, Amazon Bedrock won’t be able to access the
imported model encrypted by your key.

### Life cycle of primary and secondary grants for custom imported models

- **Primary grants** have a long lifespan and remain active as long as the associated custom models are still in use. When a custom imported model is deleted,
  the corresponding primary grant is automatically retired.
- **Secondary grants** are short-lived. They are automatically retired as soon as the operation that Amazon Bedrock performs on behalf of the customers is completed. For example,
  once a custom model import job is finished, the secondary grant that allowed Amazon Bedrock to encrypt the custom imported model will be retired immediately.
