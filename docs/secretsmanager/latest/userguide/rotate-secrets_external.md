# Rotate Secrets Manager managed external secrets

Secrets Manager has partnered with select software vendors to offer managed external secrets. This feature helps customers manage the secret lifecycle by handling rotations automatically. With managed external secrets, customers no longer need to maintain specific rotation logic for each secret stored with different partners. This will be handled by Secrets Manager.

To view the list of partners onboarded with Secrets Manager, see Managed external secrets Partners.

## Set Up Rotation in the Console

To configure rotation for an existing managed external secret,
created by specifying the secret type and value as specified by the respective integration partners,
use the following steps:

1. Open the Secrets Manager console.
2. Select your managed external secret from the list.
3. Choose the **Configuration** tab.
4. In the **Rotation configuration** section, choose **Edit rotation**.
5. Turn on **Automatic rotation**.
6. Under **Rotation metadata**, add any partner-specific metadata required for rotation:

Follow the guidelines provided by your integration partner for other required metadata 7. In **Service permissions for secret rotation**, select or create an IAM role for rotation:

    * Choose **Create a new role** to automatically create a role with necessary permissions
    * Or select an existing role with appropriate permissions for your partner

By default, permissions are scoped to the individual partner in the region where the secret is created 8. Set your **Rotation schedule** (for example, rotate automatically every 30 days). 9. Choose **Save** to apply the rotation configuration.

The two key metadata fields configured during this process are:

| Field                          | Description                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------------- |
| ExternalSecretRotationMetadata | Partner-specific metadata required for rotation, such as API version for Salesforce           |
| ExternalSecretRotationRoleArn  | The ARN of the IAM role used for rotation, with permissions scoped to the integration partner |

For more information on these fields, see Using Secrets Manager [managed external secrets to manage Third Party secrets](managed-external-secrets.md "managed-external-secrets.md").

## Set Up Rotation Using the CLI

Run the following command to set up rotation for a Salesforce secret. This command specifies the secret ID, the IAM role ARN for rotation, the rotation schedule, and any partner-specific metadata required for the rotation process.

```
aws secretsmanager rotate-secret \
            --secret-id SampleSecret \
            --external-secret-rotation-role-arn arn:aws:iam::123412341234:role/xyz \
            --rotation-rules AutomaticallyAfterDays=1 \
            --external-secret-rotation-metadata '[{"Key":"apiVersion","Value":"v65.0"}]'
```
