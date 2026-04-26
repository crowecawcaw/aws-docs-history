# Connect target AWS accounts

Configure your target AWS account connector for network migration, landing zone
build, and server migration.
This involves three steps: selecting your migration type, providing your MAP
agreement details (if applicable), and setting up the connector. These settings
apply across all migration stages — network migration, landing zone, and server
rehost.

## Step 1: Migration type selection

Choose whether you are performing a single-account or multi-account
migration:

- **Single-account migration** – All
  workloads migrate to one target AWS account. The connector target
  account and the target account are the same.
- **Multi-account migration** – Workloads
  migrate to different target accounts. The connector must be connected to
  the organization management account or a Delegated Administrator (DA)
  account registered for both Application Migration Service and CloudFormation StackSets.

## Step 2: MAP agreement

If your migration is part of the **AWS Migration
Acceleration Program (MAP 2.0)**, provide your MPE ID — a
10-character code using uppercase letters and digits (for example,
ABCDE12345). AWS Transform applies the MAP tag to all resources created across
network migration, landing zone, and server rehost stages. The tag format
is:

- **Key:** `map-migrated`
  **Value:**
  `mig`MPE_ID``

MAP tags are required to receive MAP credit. For more information, see [AWS
Migration Acceleration Program](https://aws.amazon.com/migration-acceleration-program/ "https://aws.amazon.com/migration-acceleration-program/").

## Step 3: Connector configuration

The target account connector connects your migration job to the AWS
environment where your workloads will reside after migration. It's important to
ensure that the target AWS account is properly set up with the necessary
permissions, quotas, and configurations to support your migrated infrastructure.

When you approve the connector request, you grant AWS Transform permissions to:

- Manage Amazon S3 bucket operations (read/write) for VMware migration,
  along with access to AWS Migration Hub and AWS Application
  Migration Service (Application Migration Service). This includes permissions for the following
  items, all restricted to resources within the target account and tagged
  with `CreatedBy:AWSTransform` or
  `CreatedFor:AWSTransform`:
  - Managing migration waves
  - Network configurations (Amazon EC2, VPC, Transit Gateway,
    Direct Connect, Load Balancers, Network Firewall)
  - CloudFormation stack deployments
  - Automated agent installations via Systems
    Manager

- Migrate your on-premises workloads to the target AWS account and
  Region by using the information stored in the discovery Region.
- Provision and manage landing zone infrastructure in the target
  AWS account and Region. This includes permissions for the following
  items, restricted to resources tagged with
  `CreatedBy:AWSTransform` where applicable:
  - Amazon S3 bucket operations (create, read, write, delete)
    for buckets starting with
    `transform-vmware-landing-zone-`
  - CloudFormation stack deployments and change set management for
    landing zone stacks
  - AWS Control Tower operations (managing landing zones,
    enabling baselines and controls)
  - AWS Organizations management (creating and managing
    organizational units, creating accounts, and moving
    accounts)
  - Service control policy (SCP) management via AWS
    Control Tower
  - AWS Service Catalog provisioning artifact
    management

###### Note

AWS Transform may update connector types when introducing features requiring
permission changes. The current version for the target account connector
type is 2.0. New connectors are always created with the latest version.

Before setting up the connector, understand the account roles involved in
your migration:

| Account                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS Transform account    | Any member account in your AWS Organization where you set<br>up AWS Transform. This is where your AWS Transform workspace runs. It<br>does not need to be the management account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Connector target account | The account your AWS Transform connector is configured to.<br>This depends on your migration type:<br>• **Single-account<br>migration\*<br>• – Connect to the account<br>you are migrating workloads to. The connector<br>target account and the target account are the<br>same.<br>• **Multi-account<br>migration\*<br>• – Connect to the<br>organization management account or a Delegated<br>Administrator (DA) account. The DA account must<br>be registered as delegated administrator for both<br>Application Migration Service and CloudFormation StackSets in your AWS<br>Organization. AWS Transform checks whether the<br>connected account is the management account or a<br>DA account and adjusts its behavior<br>accordingly. |
| Target account           | The AWS account where your workloads are migrated to. In<br>a single-account migration, this is the same as the connector<br>target account. In a multi-account migration, these are the<br>individual member accounts receiving the migrated<br>workloads.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Using a delegated administrator account

For multi-account migrations, AWS recommends using a Delegated
Administrator (DA) account rather than the organization management account
directly. The DA account must be registered as delegated administrator for
both Application Migration Service and CloudFormation StackSets in your AWS Organization.

The key difference between the two options is:

- **Management account** – Can enable
  trusted access for Application Migration Service and CloudFormation StackSets across the
  organization. AWS Transform calls CloudFormation StackSets APIs with
  `CallAs: SELF`.
- **Delegated Administrator account**
  – Cannot enable trusted access directly (that must be done from the
  management account), but can manage Application Migration Service source servers, launch
  instances, and deploy CloudFormation StackSets across member accounts.
  AWS Transform calls CloudFormation StackSets APIs with
  `CallAs: DELEGATED_ADMIN`.

For more information, see [Delegated administrator
for Application Migration Service](../../../mgn/latest/ug/mgn-delegated-admin.md "../../../mgn/latest/ug/mgn-delegated-admin.md") in the _Application Migration Service User Guide_.

### IAM roles created during setup

During migration setup, AWS Transform deploys a CloudFormation StackSet
(`MGNMultiAccountRoles`) to create the required IAM roles across
your target accounts. The following roles are created:

- `AWSApplicationMigrationConnectorManagementRole` –
  Used during agent installation to access source server credentials
  from AWS Secrets Manager.
- `AWSApplicationMigrationConnectorSharingRole_<ACCOUNT-ID>`
  – Contains permissions for agent installation across
  accounts.
- Application Migration Service service roles – Created automatically during Application Migration Service
  initialization in each target account. These include roles for
  replication and launch operations, and cross-account roles for
  multi-account migrations.

###### Note

IAM roles are created idempotently — if they already exist in the
account, the setup process skips creating them again.

### How to set up the connector

###### Important

AWS Transform creates an Amazon S3 bucket on your behalf in the target
AWS account. This bucket won't have `SecureTransport` enabled
by default. If you want the bucket policy to include secure transport, you
must update the policy yourself. For more information, see [Security
best practices for Amazon S3](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md").

###### To use an existing target account connector

1. In the **Job Plan** pane, expand **Choose
   target account**, and then choose **Create or
   select connectors**.
2. In the **Collaboration** tab, select an existing
   connector and then choose **Use connector**. If a
   connector is grayed out, its version isn't compatible with the job type
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

If you plan to modify the AWS Application Migration Service template to enable post-launch actions,
add the following permission to the target connector role. You can find the role
name in the **Collaboration** tab after the connector is
created. For information about adding permissions to a role, see [Update
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

When you create the connector, specify a target AWS Region. You can use
any of the following AWS Regions:

- US East (N. Virginia)
- US East (Ohio)
- US West (Oregon)
- Asia Pacific (Mumbai)
- Asia Pacific (Tokyo)
- Asia Pacific (Seoul)
- Asia Pacific (Osaka)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- Europe (Stockholm)
- South America (São Paulo)

###### Important

If you specify a target AWS Region that is different from the
AWS Transform AWS Region, that means AWS Transform will be transferring your
data across AWS Regions.

###### Note

If you plan to run a job that includes server migration only (without
network migration execution), additional commercial AWS Regions are
available as target Regions: US West (N. California), Europe (Milan),
Asia Pacific (Jakarta), Europe (Zurich), Europe (Spain), Asia Pacific
(Hyderabad), Asia Pacific (Melbourne), Middle East (Tel Aviv), Asia
Pacific (Bangkok), Asia Pacific (Kuala Lumpur), Middle East (Bahrain),
Africa (Cape Town), Asia Pacific (Hong Kong), and Middle East (UAE). To
use one of these additional Regions before Q3 2026, contact your AWS
account team to have your account allow-listed. Starting in Q3 2026,
these Regions will be generally available without the need for an
allow-list request.
