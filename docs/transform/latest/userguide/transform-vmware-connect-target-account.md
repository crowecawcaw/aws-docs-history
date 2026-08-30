# Connect target AWS accounts and regions

Connect AWS Transform to your target AWS environment so the agent can deploy
infrastructure, migrate networks, and rehost servers on your behalf. This involves
three steps: select your migration type, provide your MAP agreement details (if
applicable), and set up the connector. These settings apply across all migration
stages, including network migration, landing zone, and server rehost.

## Step 1: Migration type selection

AWS Transform supports both single-account and multi-account migrations. Choose
the option that matches your target environment:

- **Single-account migration** – All
  workloads migrate to one target AWS account. The connector target
  account and the target account are the same.
- **Multi-account migration** – Migrate
  workloads across multiple accounts in your organization from a single
  workspace. The connector must be connected to the organization
  management account or a Delegated Administrator (DA) account registered
  for both AWS Transform MGN and CloudFormation StackSets.

## Step 2: MAP agreement

If your migration is part of the **AWS Migration
Acceleration Program (MAP 2.0)**, provide your Migration
Program Engagement (MPE) ID. This is a 10-character code using uppercase letters
and digits (for example, ABCDE12345). When you provide your MPE ID, the MAP
tag is applied to all resources created across network migration, landing
zone, and server rehost stages. The tag format is:

- **Key:** `map-migrated`
  **Value:**
  `mig`MPE_ID``

You must apply MAP tags to receive MAP credit. For more information
about MAP, see [AWS
Migration Acceleration Program](https://aws.amazon.com/migration-acceleration-program/ "https://aws.amazon.com/migration-acceleration-program/").

## Step 3: Connector configuration

You use the target account connector to connect your migration job to
the AWS environment where your workloads reside after migration.
Before you begin, verify that your target AWS account has the necessary
permissions, quotas, and configurations to support your migrated
infrastructure.

When you approve the connector request, you grant AWS Transform permissions to:

- Manage Amazon S3 bucket operations (read/write) for VMware migration,
  along with access to AWS Migration Hub and AWS Application
  Migration Service (MGN). This includes permissions for the following
  items, all restricted to resources within the target account that are
  tagged with `CreatedBy:AWSTransform` or
  `CreatedFor:AWSTransform`:

  - Manage migration waves.
  - Manage network configurations (Amazon EC2, VPC, Transit Gateway,
    Direct Connect, Load Balancers, Network Firewall).
  - Manage CloudFormation stack deployments.
  - Perform automated agent installations through Systems
    Manager.

- Migrate your on-premises workloads to the target AWS account and
  Region by using the information stored in the discovery Region.
- Provision and manage landing zone infrastructure in the target
  AWS account and Region. This includes permissions for the following
  items, restricted to resources that are tagged with
  `CreatedBy:AWSTransform` where applicable:

  - Perform Amazon S3 bucket operations (create, read, write, delete)
    for buckets that start with
    `transform-vmware-landing-zone-`.
  - Manage CloudFormation stack deployments and change sets for
    landing zone stacks.
  - Perform AWS Control Tower operations. You can
    manage landing zones, enable baselines, and enable
    controls.
  - Manage AWS Organizations. You can create and manage
    organizational units, create accounts, and move
    accounts.
  - Manage service control policies (SCPs) through AWS
    Control Tower.
  - Manage AWS Service Catalog provisioning
    artifacts.

###### Note

Connector types might be updated when new features require permission
changes. The current version for the target account connector type is 2.0.
When you create a new connector, it uses the latest version.

Before you set up the connector, understand the account roles involved in
your migration:

| Account                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS Transform account    | Any member account in your AWS Organization where you set<br>up AWS Transform. This is where your AWS Transform workspace runs. It<br>does not need to be the management account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Connector target account | The account your AWS Transform connector is configured to.<br>This depends on your migration type:<br>• *_Single-account<br>migration_<br>• – Connect to the account<br>you are migrating workloads to. The connector<br>target account and the target account are the<br>same.<br>• *_Multi-account<br>migration_<br>• – Connect to the<br>organization management account or a Delegated<br>Administrator (DA) account. The DA account must<br>be registered as delegated administrator for both<br>MGN and CloudFormation StackSets in your AWS<br>Organization. AWS Transform checks whether the<br>connected account is the management account or a<br>DA account and adjusts its behavior<br>accordingly. |
| Target account           | The AWS account where your workloads are migrated to. In<br>a single-account migration, this is the same as the connector<br>target account. In a multi-account migration, these are the<br>individual member accounts receiving the migrated<br>workloads.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### Using a delegated administrator account

For multi-account migrations, AWS recommends that you use a Delegated
Administrator (DA) account rather than the organization management account
directly. A DA account follows the principle of least privilege by
limiting the scope of permissions required for migration operations.
The DA account must be registered as delegated administrator for
both MGN and CloudFormation StackSets in your AWS Organization.

The key difference between the two options is:

- **Management account** – Can enable
  trusted access for MGN and CloudFormation StackSets across the
  organization. AWS Transform calls CloudFormation StackSets APIs with
  `CallAs: SELF`.
- **Delegated Administrator account**
  – Cannot enable trusted access directly (that must be done from the
  management account), but can manage MGN source servers, launch
  instances, and deploy CloudFormation StackSets across member accounts.
  AWS Transform calls CloudFormation StackSets APIs with
  `CallAs: DELEGATED_ADMIN`.

For more information, see [Delegated administrator
for MGN](../../../mgn/latest/ug/mgn-delegated-admin.md "../../../mgn/latest/ug/mgn-delegated-admin.md") in the _MGN User Guide_.

### IAM roles created during connector setup

During connector setup, AWS Transform creates the following IAM role in your
target account:

- `AWSTransform-Connector-role-`
  – Created when you set up the target account connector, in the
  management account or the delegated administrator account of your
  AWS Organization. This role allows AWS Transform to connect to your
  target account and act on your behalf to run migration
  operations.

### Target account connector setup

###### Important

During connector setup, an Amazon S3 bucket is created in your target
AWS account. This bucket won't enforce HTTPS-only access
(`SecureTransport`) by default. If you want the bucket policy
to include secure transport, you must update the policy yourself. For more
information, see [Security
best practices for Amazon S3](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md").

###### To use an existing target account connector

1. In the **Job Plan** pane, expand **Choose
   target account**, and then choose **Create or
   select connectors**.
2. In the **Collaboration** tab, select an existing
   connector and then choose **Use connector**. If a
   connector is unavailable, its version isn't compatible with the job type
   you selected.

###### Important

If you specify a connector with a target AWS Region that is
different from the AWS Transform Region, AWS Transform will transfer your data
across AWS Regions. 3. Choose **Continue**.

###### To create a new connector

1. In the **Job Plan** pane, expand **Connect
   target account**, and then choose **Create or
   select connectors**.
2. Specify the AWS account and AWS Region for your target, and then
   choose **Next**.

###### Important

If the target AWS Region differs from the discovery
AWS Region, AWS Transform will transfer your data across
AWS Regions. 3. Choose whether to use Amazon S3 managed keys for encryption. If you
specify your own KMS key, you can use the default key policy or a
less permissive one. For information about creating a KMS key, see
[Create a KMS
key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.

AWS Transform uses the `kms:DescribeKey` permission to verify
the key exists, and `kms:GenerateDataKey` and
`kms:Decrypt` to encrypt and decrypt job data in the
Amazon S3 bucket. For more information, see [Reducing the cost
of SSE-KMS with Amazon S3 Bucket Keys](../../../AmazonS3/latest/userguide/bucket-key.md "../../../AmazonS3/latest/userguide/bucket-key.md"). 4. Choose **Continue**. 5. Copy the verification link, share it with an administrator of the
target AWS account, and ask them to approve the connection
request. 6. After the administrator approves the request, select the newly created
connector from the list and choose **Use
connector**. 7. Choose **Send to AWS Transform**.

If you plan to modify the AWS Transform MGN template to enable post-launch actions,
add the following permission to the target connector role. This JSON policy
statement grants the `iam:PassRole` permission for the post-launch
actions role. You can find the role name in the
**Collaboration** tab after the connector is created. For
information about adding permissions to a role, see [Update
permissions for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md") in the
_IAM User Guide_.

```
{
      "Sid": "MGNPostLaunchActions",
      "Effect": "Allow",
      "Action": [
        "iam:PassRole"
      ],
      "Resource": "arn:aws:iam::`target-account-ID`:role/service-role/AWSApplicationMigrationLaunchInstanceWithSsmRole"
}
```

### Supported target regions

A migration target region is the AWS Region where migrated resources
are deployed, including landing zones, network infrastructure, and server
rehosting. When you create the connector, specify a target AWS Region.
You can use any of the following AWS Regions:

- US East (N. Virginia)
- US East (Ohio)
- US West (N. California)
- US West (Oregon)
- Africa (Cape Town)
- Asia Pacific (Hong Kong)
- Asia Pacific (Taipei)
- Asia Pacific (Mumbai)
- Asia Pacific (Hyderabad)
- Asia Pacific (Tokyo)
- Asia Pacific (Seoul)
- Asia Pacific (Osaka)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Jakarta)
- Asia Pacific (Melbourne)
- Asia Pacific (Malaysia)
- Asia Pacific (New Zealand)
- Asia Pacific (Thailand)
- Canada (Central)
- Canada West (Calgary)
- Europe (Frankfurt)
- Europe (Zurich)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- Europe (Stockholm)
- Europe (Milan)
- Europe (Spain)
- Israel (Tel Aviv)
- Mexico (Central)
- South America (São Paulo)

###### Important

If you specify a target AWS Region that differs from the
AWS Transform AWS Region, some of your data is transferred across
AWS Regions.

Note that your server replication data goes directly from your
source environment to your target account and region.
