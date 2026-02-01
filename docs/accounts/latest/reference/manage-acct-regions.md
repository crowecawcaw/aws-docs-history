# Enable or disable AWS Regions in your

account

An _AWS Region_ is a physical location in the world where AWS has
multiple Availability Zones. Availability Zones consist of one or more discrete AWS data
centers, each with redundant power, networking, and connectivity, housed in separate
facilities. This means that each AWS Region is physically isolated and independent of the
other Regions. Regions provide fault tolerance, stability, and resilience, and can also
reduce latency. Running workloads in an AWS Region closer to end users can improve
performance and lower latency. For a map of available and upcoming Regions, see [Regions and
Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az "https://aws.amazon.com/about-aws/global-infrastructure/regions_az"). To learn more about AWS Regions and resiliency
architecture for your workloads, visit [AWS
multi-Region fundamentals](../../../prescriptive-guidance/latest/aws-multi-region-fundamentals/introduction.md "../../../prescriptive-guidance/latest/aws-multi-region-fundamentals/introduction.md").

AWS Regions broadly fall into two categories of availability for accounts:

- **Default Regions** – Regions launched before
  March 20, 2019 are enabled by default. You can create and manage resources in these
  default Regions immediately after your account activation. Default Regions cannot be
  enabled or disabled.
- **Opt-in Regions** – Regions launched after
  March 20, 2019 are disabled by default and referred to as opt-in Regions. Disabled
  opt-in Regions are not shown in the Console Navigation bar, and you cannot use these
  Regions to create workloads until they are enabled. To use these opt-in Regions, you
  must first enable them in your AWS account. After enabling an opt-in Region, you
  can select that Region in the navigation bar and create and manage
  resources in that Region. To enable opt-in Region for your standalone accounts, see
  [Enable or disable a Region for
  standalone accounts](#manage-acct-regions-enable-standalone "#manage-acct-regions-enable-standalone") and to enable opt-in
  Region for your member accounts, see [Enable or disable a Region in
  your organization](#manage-acct-regions-enable-organization "#manage-acct-regions-enable-organization").
  When you sign up for an AWS account, AWS recommends an opt-in Region for you
  based on your contact address country. Customers in a country with an AWS opt-in Region
  see a recommendation on the Contact Information page to enable the opt-in Region in
  that country. Customers in a country with both an opt-in Region and a default Region, like
  India, Australia, or Canada, see a recommendation to select the opt-in Region if the opt-in
  Region is closer to them than the default Region. After an account is activated, you can
  enable other AWS opt-in Regions in your account or choose to disable the opt-in Region you
  enabled during sign-up.

When you create an AWS account, your IAM data and credentials are
automatically configured to work across all default Regions, allowing the root user and
IAM identities with appropriate permissions to access AWS services in these Regions
using their existing credentials. AWS opt-in Regions are disabled by default, and
IAM data and credentials are not initially available in these Regions, which prevents
access to AWS services in that Region. When you choose to enable an opt-in Region,
AWS propagates your IAM data and credentials to that Region. Once the propagation is
complete and the opt-in Region is enabled, the root user and IAM identities can then
access AWS services in the newly enabled opt-in Region using the same IAM
credentials they use in default Regions.

When you disable an opt-in Region, your IAM credentials are deactivated and
you lose IAM access to the resources in that opt-in Region. Disabling an opt-in Region
does not delete the resources in that Region and charges for resources (if any) in that
disabled opt-in Region continue to accrue at the standard rate.

###### Important

Disabling a Region disables IAM access to resources in the Region. This does not delete the resources in question,
which continue to incur charges. Remove any remaining resources prior to disabling a Region.

AWS groups Regions into [partitions](../../../whitepapers/latest/aws-fault-isolation-boundaries/partitions.md "../../../whitepapers/latest/aws-fault-isolation-boundaries/partitions.md"). Every Region is in exactly one partition, and each partition
has one or more Regions. Partitions have independent instances of AWS Identity and Access Management (IAM) and
provide a hard boundary between Regions in different partitions. AWS commercial
Regions are in the `aws` partition, Regions in China are in the
`aws-cn` partition, and AWS GovCloud (US) Regions are in the
`aws-us-gov` partition. Depending on the partition where you created your
AWS account, you can use AWS Regions within that partition.

- An account in `aws` partition provides you access to multiple Regions
  in the commercial partition so that you can launch AWS resources in locations that
  meet your requirements. For example, you might want to launch Amazon EC2 instances in
  Europe to be closer to your European customers or to meet legal requirements.
- An account in `aws-us-gov` partition provides you access to the
  AWS GovCloud (US-West) Region and the AWS GovCloud (US-East) Region. For more information, see
  [AWS GovCloud (US)](https://aws.amazon.com/govcloud-us/ "https://aws.amazon.com/govcloud-us/").
- An account in `aws-cn` partition provides you access to the Beijing and
  Ningxia Regions only. For more information, see [Amazon Web Services in
  China](https://www.amazonaws.cn/about-aws/china/ "https://www.amazonaws.cn/about-aws/china/").

###### Topics

- [Regional availability reference](#manage-acct-regions-regional-availability "#manage-acct-regions-regional-availability")
- [Considerations before enabling and
  disabling Regions](#manage-acct-regions-considerations "#manage-acct-regions-considerations")
- [Processing times and request
  limits](#manage-acct-regions-processing-times "#manage-acct-regions-processing-times")
- [Enable or disable a Region for
  standalone accounts](#manage-acct-regions-enable-standalone "#manage-acct-regions-enable-standalone")
- [Enable or disable a Region in
  your organization](#manage-acct-regions-enable-organization "#manage-acct-regions-enable-organization")

## Regional availability reference

The following tables list AWS Regions by availability type. Default Regions are enabled automatically and cannot be disabled, while opt-in Regions must be manually enabled before you can use them:

Opt-in Regions
The following Regions are opt-in Regions that must be enabled before you can use them:

| Name                       | Code             | Status |
| -------------------------- | ---------------- | ------ |
| Africa (Cape Town)         | `af-south-1`     | GA     |
| Asia Pacific (Hong Kong)   | `ap-east-1`      | GA     |
| Asia Pacific (Taipei)      | `ap-east-2`      | GA     |
| Asia Pacific (Hyderabad)   | `ap-south-2`     | GA     |
| Asia Pacific (Jakarta)     | `ap-southeast-3` | GA     |
| Asia Pacific (Melbourne)   | `ap-southeast-4` | GA     |
| Asia Pacific (Malaysia)    | `ap-southeast-5` | GA     |
| Asia Pacific (New Zealand) | `ap-southeast-6` | GA     |
| Asia Pacific (Thailand)    | `ap-southeast-7` | GA     |
| Canada West (Calgary)      | `ca-west-1`      | GA     |
| Europe (Zurich)            | `eu-central-2`   | GA     |
| Europe (Milan)             | `eu-south-1`     | GA     |
| Europe (Spain)             | `eu-south-2`     | GA     |
| Israel (Tel Aviv)          | `il-central-1`   | GA     |
| Middle East (UAE)          | `me-central-1`   | GA     |
| Middle East (Bahrain)      | `me-south-1`     | GA     |
| Mexico (Central)           | `mx-central-1`   | GA     |

Default Regions
The following Regions are enabled by default and cannot be disabled:

| Name                      | Code             |
| ------------------------- | ---------------- |
| Asia Pacific (Tokyo)      | `ap-northeast-1` |
| Asia Pacific (Seoul)      | `ap-northeast-2` |
| Asia Pacific (Osaka)      | `ap-northeast-3` |
| Asia Pacific (Mumbai)     | `ap-south-1`     |
| Asia Pacific (Singapore)  | `ap-southeast-1` |
| Asia Pacific (Sydney)     | `ap-southeast-2` |
| Canada (Central)          | `ca-central-1`   |
| Europe (Frankfurt)        | `eu-central-1`   |
| Europe (Stockholm)        | `eu-north-1`     |
| Europe (Ireland)          | `eu-west-1`      |
| Europe (London)           | `eu-west-2`      |
| Europe (Paris)            | `eu-west-3`      |
| South America (São Paulo) | `sa-east-1`      |
| US East (N. Virginia)     | `us-east-1`      |
| US East (Ohio)            | `us-east-2`      |
| US West (N. California)   | `us-west-1`      |
| US West (Oregon)          | `us-west-2`      |

For a list of Region names and their corresponding codes, see [Regional
endpoints](../../../general/latest/gr/rande.md#regional-endpoints "../../../general/latest/gr/rande.md#regional-endpoints") in the _AWS General Reference Guide_. For a list
of AWS services supported in each Region (without endpoints), see the [AWS
Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

###### Important

AWS recommends that you use regional AWS Security Token Service (AWS STS) endpoints instead of the
global endpoint to reduce latency. Session tokens from regional AWS STS endpoints are
valid in all AWS Regions. If you use regional AWS STS endpoints, you don't need to
make any changes. However, session tokens from the _global_
AWS STS endpoint (https://sts.amazonaws.com) are valid only in AWS Regions that
you enable, or that are enabled by default. If you intend to enable a new Region for
your account, you can either use session tokens from regional AWS STS endpoints
or activate the global AWS STS endpoint to issue session tokens that are valid in
all AWS Regions. Session tokens that are valid in all Regions are larger. If you
store session tokens, these larger tokens might affect your systems. For more
information about how AWS STS endpoints work with AWS Regions, see [Managing AWS STS in
an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md").

## Considerations before enabling and

disabling Regions

Before you enable or disable a Region, it's important to consider the
following:

- **You can use all destination Regions in a cross-Region
  inference geography regardless of Region-opt status** –
  Certain AWS generative AI services including Amazon Bedrock (see [Increase
  throughput with cross-Region inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md")) and Amazon Q Developer (see [Cross-region
  processing in Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/cross-region-processing.md "../../../amazonq/latest/qdeveloper-ug/cross-region-processing.md")) use cross-region inference. If you use
  those services, they automatically select the optimal
  AWS Region–including Regions that you have not enabled for resources
  and IAM data–within your chosen geography. This improves the customer
  experience by maximizing available compute and model availability.
- **You can use IAM permissions to control access to
  Regions** – AWS Identity and Access Management (IAM) includes four permissions that
  let you control which users can enable, disable, get, and list Regions. For more
  information, see [AWS: Allows enabling and disabling AWS Regions](../../../IAM/latest/UserGuide/reference_policies_examples_aws-enable-disable-regions.md "../../../IAM/latest/UserGuide/reference_policies_examples_aws-enable-disable-regions.md") in the
  _IAM User Guide_. You can also use the [`aws:RequestedRegion`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion") condition key to control
  access to AWS services in an AWS Region.
- **Enabling and disabling a Region is free**
  – There is no charge to enable or disable a Region. You're charged only
  for resources that you create in the new Region.
- **Amazon EventBridge integration** – You can
  subscribe to region-opt status update notifications in EventBridge. An EventBridge
  notification will be created for each status change, allowing customers to
  automate work flows.
- **Expressive Region-opt status** – Due to
  the asynchronous nature of enabling/disabling an opt-in region, there are four
  potential statuses for a region-opt request:

      + `ENABLING`
      + `DISABLING`
      + `ENABLED`
      + `DISABLED`

  You cannot cancel an opt-in or opt-out when it is in either
  `ENABLING` or `DISABLING` status. Otherwise, a
  `ConflictException` will be thrown. A completed
  (Enabled/Disabled) region-opt request is dependent on the provisioning of key
  underlying AWS services. There might be some AWS services that will not be
  immediately usable despite the status being `ENABLED`.

## Processing times and request

limits

When enabling or disabling Regions, be aware of the following timing and request limitations:

- **Enabling a Region takes a few minutes to several hours
  in some cases** – When you enable a Region, AWS performs
  actions to prepare your account in that Region, such as distributing your IAM
  resources to the Region. This process takes a few minutes for most accounts, but
  can sometimes take several hours. You cannot use the Region until this process
  is complete.
- **Disabling a Region isn't always immediately
  visible** – Services and consoles might be temporarily
  visible after disabling a region. Disabling a Region can takes a few minutes to
  several hours to take effect.
- **A single account can have 6 region-opt requests in
  progress at any given time** – One request is equal to
  either an enable or disable of one particular region for one account.
- **Organizations can have 50 region-opt requests open at a
  given time across an AWS organization** – The management
  account can at any point in time have 50 open requests pending completion for
  its organization. One request is equal to either an enable or disable of one
  particular region for one account.

## Enable or disable a Region for

standalone accounts

To update which Regions your AWS account has access to, perform the steps in the
following procedure. The AWS Management Console procedure below always works only in the standalone
context. You can use the AWS Management Console to view or update only the available Regions in the
account you used to call the operation.

AWS Management Console

###### To enable or disable a Region for a standalone AWS account

###### Minimum permissions

To perform the steps in the following procedure, an IAM user or
role must have the following permissions:

- `account:ListRegions` (needed to view the list
  of AWS Regions and whether they are currently enabled or
  disabled).
- `account:EnableRegion`
- `account:DisableRegion`

1. Sign in to
   the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as either the AWS account root user or as an IAM user or
   role that has the minimum permissions.
2. Choose your account name on the top right of the window, and then
   choose **Account**.
3. On the [**Account** page](https://console.aws.amazon.com/billing/home#/account "https://console.aws.amazon.com/billing/home#/account"), scroll down to
   the section **AWS Regions**.
4. Choose the Region that you want to enable or disable and then choose the desired action **Enable** or **Disable**. You will see a prompt to confirm.
5. If you chose the **Enable** option, review the displayed text and then choose **Enable region**.

If you chose the **Disable** option, review the displayed text, type `disable` to confirm, and then choose **Disable region**.

After the opt-in Region is enabled, you can select that Region from the Region navigation bar. For steps to select a Region, see [Choosing a Region from the navigation bar in the AWS Management Console](../../../awsconsolehelpdocs/latest/gsg/select-region-procedure.md "../../../awsconsolehelpdocs/latest/gsg/select-region-procedure.md") and for Region specific console setting in your account, see [Setting the default Region in the AWS Management Console](../../../awsconsolehelpdocs/latest/gsg/change-default-region.md "../../../awsconsolehelpdocs/latest/gsg/change-default-region.md").

AWS CLI & SDKs
You can enable, disable, read and list region opt status by using the
following AWS CLI commands or their AWS SDK equivalent operations:

- `EnableRegion`
- `DisableRegion`
- `GetRegionOptStatus`
- `ListRegions`

###### Minimum permissions

To perform the following steps, you must have the permission that maps
to that operation:

- `account:EnableRegion`
- `account:DisableRegion`
- `account:GetRegionOptStatus`
- `account:ListRegions`

If you use these individual permissions, you can grant some users the
ability to only read region opt information, and grant others the ability to
both read and write.

The following example enables a region for the specified member account in
an organization. The credentials used must be from either the organization’s
management account, or from the Account Management’s delegated admin
account.

Note that you can also disable a region using the same command and then
replacing `enable-region` with
`disable-region`.

```
aws account enable-region --region-name `af-south-1`
```

This command produces no output if it's successful.

The operation is asynchronous. The following command will allow you to see
the latest status of the request.

```
aws account get-region-opt-status --region-name `af-south-1`
  {
    "RegionName": "`af-south-1`",
    "RegionOptStatus": "ENABLING"
  }
```

## Enable or disable a Region in

your organization

To update the enabled Regions for member accounts of your AWS Organizations, perform the steps
in the following procedure.

###### Note

The AWS Organizations managed policies `AWSOrganizationsReadOnlyAccess` or
`AWSOrganizationsFullAccess` are updated to provide permission to
access the AWS Account Management APIs so you can access account data from the AWS Organizations console.
To view the updated managed policies, see [Updates to Organizations AWS managed policies](../../../organizations/latest/userguide/orgs_reference_available-policies.md#ref-iam-managed-policies-updates "../../../organizations/latest/userguide/orgs_reference_available-policies.md#ref-iam-managed-policies-updates").

###### Note

Before you can perform these operations from the management account or a
delegated admin account in an organization for use with member accounts, you
must:

- Enable all features in your organization to manage settings on your
  member accounts. This allows admin control over the member accounts.
  This is set by default when you create your organization. If your
  organization is set to consolidated billing only, and you want to enable
  all features, see [Enabling all features in your organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md").
- Enable trusted access for the AWS Account Management service. To set this up, see
  [Enable trusted access for AWS Account Management](using-orgs-trusted-access.md "using-orgs-trusted-access.md").

AWS Management Console

###### To enable or disable a Region in your organization

1. Sign in to the AWS Organizations console with your organization's
   management account credentials.
2. On the **AWS accounts** page, select the
   account that you want to update.
3. Choose the **Account settings** tab.
4. Under **Regions**, select the Region you want to
   enable or disable.
5. Choose **Actions**, and then choose either
   **Enable** or **Disable**
   option.
6. If you chose the **Enable** option, review the
   displayed text and then choose **Enable
   region**.
7. If you chose the **Disable** option, review the
   displayed text, type **disable** to confirm, and
   then choose **Disable region**.

AWS CLI & SDKs
You can enable, disable, read and list region opt status for organization
member accounts by using the following AWS CLI commands or their AWS SDK
equivalent operations:

- `EnableRegion`
- `DisableRegion`
- `GetRegionOptStatus`
- `ListRegions`

###### Minimum permissions

To perform the following steps, you must have the permission that maps
to that operation:

- `account:EnableRegion`
- `account:DisableRegion`
- `account:GetRegionOptStatus`
- `account:ListRegions`

If you use these individual permissions, you can grant some users the
ability to only read region opt information, and grant others the ability to
both read and write.

The following example enables a region for the specified member account in
an organization. The credentials used must be from either the organization’s
management account, or from the Account Management’s delegated admin
account.

Note that you can also disable a region using the same command and then
replacing `enable-region` with
`disable-region`.

```
aws account enable-region --account-id `123456789012` --region-name `af-south-1`
```

This command produces no output if it's successful.

###### Note

An organization can only have up to 20 region requests at a given
time. Otherwise, you will receive a
`TooManyRequestsException`.

The operation is asynchronous. The following command will allow you to see
the latest status of the request.

```
aws account get-region-opt-status --account-id `123456789012` --region-name `af-south-1`
  {
    "RegionName": "`af-south-1`",
    "RegionOptStatus": "ENABLING"
  }
```
