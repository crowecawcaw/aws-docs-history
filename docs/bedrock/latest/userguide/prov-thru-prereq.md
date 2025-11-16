# Prerequisites for Provisioned Throughput

Before you can purchase and manage Provisioned Throughput, you need to fulfill the following prerequisites:

1.  [Request access to the model or models](model-access.md "model-access.md") that you want to purchase Provisioned Throughput for. After access has been granted, you can purchase Provisioned Throughput for the base model and any models customized from it.
2.  Ensure that your IAM role has access to the Provisioned Throughput API actions. If your role has the [AmazonBedrockFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess") AWS-managed policy attached, you can skip this step. Otherwise, do the following:
    1. Follow the steps at [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") and create the following policy, which allows a role to create a Provisioned Throughput for all foundation and custom models.

    JSON

    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Sid": "PermissionsForProvisionedThroughput",
     "Effect": "Allow",
     "Action": [
     "bedrock:GetFoundationModel",
     "bedrock:ListFoundationModels",
     "bedrock:GetCustomModel",
     "bedrock:ListCustomModels",
     "bedrock:InvokeModel",
     "bedrock:InvokeModelWithResponseStream",
     "bedrock:ListTagsForResource",
     "bedrock:UntagResource",
     "bedrock:TagResource",
     "bedrock:CreateProvisionedModelThroughput",
     "bedrock:GetProvisionedModelThroughput",
     "bedrock:ListProvisionedModelThroughputs",
     "bedrock:UpdateProvisionedModelThroughput",
     "bedrock:DeleteProvisionedModelThroughput"
     ],
     "Resource": "*"
     }
     ]
    }`

    ```

    ###### Note

    If you're using Provisioned Throughput with cross-Region inference, you may need additional permissions. See [Increase throughput with cross-Region
    inference](cross-region-inference.md "cross-region-inference.md") to learn more.

    (Optional) You can restrict the role's access in the following ways:

        * To restrict the API actions that the role can make, modify the list in the `Action` field to contain only the [API operations](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-actions-as-permissions") that you want to allow access to.
        * After creating a provisioned model, you can restrict the role's ability to perform an API request with the provisioned model by modifying the `Resource` list to contain only the [provisioned models](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-resources-for-iam-policies") that you want to allow access to. For an example, see [Allow users to invoke a provisioned model](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-perform-actions-pt "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-perform-actions-pt").
        * To restrict a role's ability to create provisioned models from specific foundation or custom models, modify the `Resource` list to contain only the [foundation and custom models](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-resources-for-iam-policies") that you want to allow access to.

    2. Follow the steps at [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") to attach the policy to a role to grant the role permissions.

3.  If you're purchasing Provisioned Throughput for a custom model that's encrypted with a customer-managed AWS KMS key, your IAM role must have permissions to decrypt the key. You can use the template at [Understand how to create a customer managed key and how to attach a key policy to it](encryption-custom-job.md#encryption-key-policy "encryption-custom-job.md#encryption-key-policy"). For minimal permissions, you can use only the `Permissions for custom model users` policy statement.
