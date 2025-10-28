# Getting started with GuardDuty

This tutorial provides a hands-on introduction to GuardDuty. The minimum requirements for
enabling GuardDuty as a standalone account or as a GuardDuty administrator with AWS Organizations are covered
in Step 1. Steps 2 through 5 cover using additional features recommended by GuardDuty to get the
most out of your findings.

###### Topics

- [Before you begin](#setup-before "#setup-before")
- [Step 1: Enable Amazon GuardDuty](#guardduty_enable-gd "#guardduty_enable-gd")
- [Step 2: Generate sample findings and explore basic
  operations](#startup-samples "#startup-samples")
- [Step 3: Configure exporting GuardDuty findings to an Amazon S3
  bucket](#setup-export "#setup-export")
- [Step 4: Set up GuardDuty finding alerts through SNS](#setup-sns "#setup-sns")
- [Next steps](#setup_beyond "#setup_beyond")

## Before you begin

GuardDuty is a threat detection service that monitors [Foundational data sources](guardduty_data-sources.md "guardduty_data-sources.md") such as
AWS CloudTrail management events, Amazon VPC Flow Logs, and Amazon Route 53 Resolver DNS query logs. GuardDuty
also analyzes features associated with its protection types only if you enable them
separately. [Features](guardduty-features-activation-model.md "guardduty-features-activation-model.md") include Kubernetes audit logs, RDS login activity, AWS CloudTrail data events for Amazon S3, Amazon EBS volumes,
Runtime Monitoring, and Lambda network activity logs. Using these data sources and features (if
enabled), GuardDuty generates security findings for your account.

After you enable GuardDuty, it starts monitoring your account for potential threats based on
the activities in foundational data sources. By default,
[Extended Threat Detection](guardduty-extended-threat-detection.md "guardduty-extended-threat-detection.md") is enabled for all AWS accounts that have
enabled GuardDuty. This capability detects multi-stage attack sequences that span multiple foundational data sources,
AWS resources, and time, in your account. To detect potential threats to specific AWS resources, you
can choose to enable use-case focused protection plans that GuardDuty offers. For more information, see
[Features of GuardDuty](what-is-guardduty.md#features-of-guardduty "what-is-guardduty.md#features-of-guardduty").

You do not need to enable any of the foundational data sources explicitly. When you enable S3 Protection, you
don't need to enable Amazon S3 data event logging explicitly. Similarly, when you enable
EKS Protection, you don't need to enable Amazon EKS audit logs explicitly. Amazon GuardDuty pulls independent
streams of data directly from these services.

For a new GuardDuty account, some of the available
protection types that are supported in an AWS Region are enabled and included in the
30-day free trial period by default. You can opt out of any or all of them. If you've an
existing AWS account with GuardDuty enabled, you can choose to enable any or all of the protection plans
that are available in your Region. For an overview of protection plans and which protection plans will
be enabled by default, see [Pricing in GuardDuty](guardduty-pricing.md "guardduty-pricing.md").

**When enabling GuardDuty, consider the following
items**:

- GuardDuty is a Regional service, meaning any of the configuration procedures you
  follow on this page must be repeated in each Region that you want to monitor
  with GuardDuty.

We highly recommend that you enable GuardDuty in all supported AWS Regions. This
enables GuardDuty to generate findings about unauthorized or unusual activity even
in Regions that you are not actively using. This also enables GuardDuty to monitor
AWS CloudTrail events for global AWS services such as IAM. If GuardDuty is not enabled
in all supported Regions, its ability to detect activity that involves global
services is reduced. For a full list of Regions where GuardDuty is available, see
[Regions and endpoints](guardduty_regions.md "guardduty_regions.md").

- Any user with administrator privileges in an AWS account can enable GuardDuty,
  however, following the security best practice of least privilege, it is
  recommended that you create an IAM role, user, or group to manage GuardDuty
  specifically. For information about the permissions required to enable GuardDuty see
  [Permissions required to enable
  GuardDuty](security_iam_id-based-policy-examples.md#guardduty_enable-permissions "security_iam_id-based-policy-examples.md#guardduty_enable-permissions").
- When you enable GuardDuty for the first time in any AWS Region, by default, it
  also enables all the available protection types that are supported in that
  Region, including Malware Protection for EC2. GuardDuty creates a service–linked role for your
  account called `AWSServiceRoleForAmazonGuardDuty`. This role includes
  the permissions and the trust policies that allow GuardDuty to consume and analyze
  events directly from the [GuardDuty foundational data sources](guardduty_data-sources.md "guardduty_data-sources.md") to generate security findings.
  Malware Protection for EC2 creates another service–linked role for your account called
  `AWSServiceRoleForAmazonGuardDutyMalwareProtection`. This role
  includes the permissions and trust policies that allow Malware Protection for EC2 perform
  agentless scans to detect malware in your GuardDuty account. It allows GuardDuty to
  create an EBS volume snapshot in your account, and share that snapshot with the
  GuardDuty service account. For more information, see [Service-linked role permissions for GuardDuty](slr-permissions.md "slr-permissions.md"). For more
  information about service-linked roles, see [Using
  service-linked roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md").
- When you enable GuardDuty for the first time in any Region your AWS account is
  automatically enrolled in a 30-day GuardDuty free trial for that Region.

The following video explains how an administrator account can get started with GuardDuty and enable it
in multiple member accounts.

## Step 1: Enable Amazon GuardDuty

The first step to using GuardDuty is to enable it in your account. Once enabled, GuardDuty
will immediately begin to monitor for security threats in the current Region.

If you want to manage GuardDuty findings for other accounts within your organization as a
GuardDuty administrator, you must add member accounts and enable GuardDuty for them as
well.

###### Note

If you want to enable GuardDuty Malware Protection for S3 without enabling GuardDuty, then for steps, see
[GuardDuty Malware Protection for S3](gdu-malware-protection-s3.md "gdu-malware-protection-s3.md").

Standalone account environment

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/")
2. Select the **Amazon GuardDuty - All features**
   option.
3. Choose **Get started**.
4. On the **Welcome to GuardDuty** page, view the
   service terms. Choose **Enable GuardDuty**.

Multi-account environment

###### Important

As prerequisites for this process, you must be in the same
organization as all the accounts you want to manage, and have access to
the AWS Organizations management account in order to delegate an administrator for
GuardDuty within your organization. Additional permissions may be required
to delegate an administrator, for more info see [Permissions required to designate a
delegated GuardDuty administrator account](organizations_permissions.md "organizations_permissions.md").

**To designate a delegated GuardDuty administrator account**

1. Open the AWS Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/ "https://console.aws.amazon.com/organizations/"), using the
   management account.
2. Open the GuardDuty console at
   [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

Is GuardDuty already enabled in your account?

    * If GuardDuty is not already enabled, you can select
     **Get Started** and then designate a
     GuardDuty delegated administrator on the **Welcome to
     GuardDuty** page.
    * If GuardDuty is enabled, you can designate a GuardDuty delegated
     administrator on the **Settings**
     page.

3. Enter the twelve-digit AWS account ID of the account that you
   want to designate as the GuardDuty delegated administrator for the
   organization and choose **Delegate**.

###### Note

If GuardDuty is not already enabled, designating a delegated
administrator will enable GuardDuty for that account in your current
Region.

**To add member accounts**

This procedure covers adding members accounts to a GuardDuty delegated
administrator account through AWS Organizations. There is also the option to add
members by invitation. To learn more about both methods for associating
members in GuardDuty, see [Multiple accounts in Amazon GuardDuty](guardduty_accounts.md "guardduty_accounts.md").

1. Log in to the delegated administrator account
2. Open the GuardDuty console at
   [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
3. In the navigation panel, choose **Settings**, and
   then choose **Accounts**.

The accounts table displays all of the accounts in the
organization. 4. Choose the accounts that you want to add as members by selecting
the box next to the account ID. Then from the
**Action** menu select **Add
member**.

###### Tip

You can automate adding new accounts as members by turning on
the **Auto-enable** feature; however, this only
applies to accounts that join your organization after the
feature has been enabled.

## Step 2: Generate sample findings and explore basic

operations

When GuardDuty discovers a security issue, it generates a finding. A GuardDuty finding is a
dataset containing details relating to that unique security issue. The finding's details
can be used to help you investigate the issue.

GuardDuty supports generating sample findings with placeholder values, which can be used
to test GuardDuty functionality and familiarize yourself with findings before needing to
respond to a real security issue discovered by GuardDuty. Follow the guide below to generate
sample findings for each finding type available in GuardDuty, for additional ways to
generate sample findings, including generating a simulated security event within your
account, see [Sample findings](sample_findings.md "sample_findings.md").

**To create and explore sample findings**

1. In the navigation pane, choose **Settings**.
2. On the **Settings** page, under **Sample
   findings**, choose **Generate sample
   findings**.
3. In the navigation pane, choose **Summary** to view the
   insights about the findings generated in your AWS environment. For more
   information about the components of the Summary dashboard, see [Summary dashboard in Amazon GuardDuty](guardduty-summary.md "guardduty-summary.md").
4. In the navigation pane, choose **Findings**. The sample
   findings are displayed on the **Current findings** page with
   the prefix **[SAMPLE]**.
5. Select a finding from the list to display details for the finding.
   1. You can review the different information fields available in the
      finding details pane. Different types of findings can have different
      fields. For more information about the available fields across all
      finding types see [Finding details](guardduty_findings-summary.md "guardduty_findings-summary.md"). From the details pane
      you can take the following actions:
      - Select the **finding ID** at the top of the
        pane to open the complete JSON details for the finding. The
        complete JSON file can also be downloaded from this panel. The
        JSON contains some additional information not included in the
        console view and is the format that can be ingested by other
        tools and services.
      - View the **Resource affected** section. In a
        real finding, the information here will help you identify a
        resource in your account that should be investigated and will
        include links to the appropriate AWS Management Console for actionable
        resources.
      - Select the + or - looking glass icons to create an inclusive
        or exclusive filter for that detail. For more information about
        finding filters see [Filtering findings in GuardDuty](guardduty_filter-findings.md "guardduty_filter-findings.md").

6. Archive all your sample findings
   1. Select all findings by selection the check box at the top of the
      list.
   2. Deselect any findings that you wish to keep.
   3. Select the **Actions** menu and then select
      **Archive** to hide the sample findings.

   ###### Note

   To view the archived findings select **Current**
   and then **Archived** to switch the findings
   view.

## Step 3: Configure exporting GuardDuty findings to an Amazon S3

bucket

GuardDuty recommends configuring settings to export findings because it allows you to
export your findings to an S3 bucket for indefinite storage beyond the GuardDuty 90-day
retention period. This allows you to keep records of findings or track issues within
your AWS environment over time. GuardDuty encrypts the findings data in your
S3 bucket by using AWS Key Management Service (AWS KMS key). To configure the settings, you must
give GuardDuty the permission a KMS key. For more detailed steps, see [Exporting generated findings to
Amazon S3](guardduty_exportfindings.md "guardduty_exportfindings.md").

###### To export GuardDuty findings to Amazon S3 bucket

1.  ###### Attach policy to KMS key
    1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
    2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
    3. In the navigation pane, choose **Customer managed keys**.
    4. Select an existing KMS key, or perform the steps to
       [Create a symmetric
       encryption KMS key](../../../kms/latest/developerguide/create-symmetric-cmk.md "../../../kms/latest/developerguide/create-symmetric-cmk.md") in the _AWS Key Management Service Developer Guide_.

    The Region of your KMS key and Amazon S3 bucket must be the same.

    Copy the key ARN to a notepad for use in the later steps. 5. In the **Key policy** section of your KMS key, choose **Edit**. If
    **Switch to policy view** is displayed, choose it to display the **Key policy**, and
    then choose **Edit**. 6. Copy the following policy block to your KMS key policy:

    ```
    {
        "Sid": "AllowGuardDutyKey",
        "Effect": "Allow",
        "Principal": {
            "Service": "guardduty.amazonaws.com"
        },
        "Action": "kms:GenerateDataKey",
        "Resource": "`KMS key ARN`",
        "Condition": {
            "StringEquals": {
                "aws:SourceAccount": "123456789012",
                "aws:SourceArn": "arn:aws:guardduty:`Region2`:`123456789012`:detector/`SourceDetectorID`"
            }
        }
    }
    ```

    Edit the policy by replacing the following values that are formatted in
    _`red`_ in the policy
    example:

        1. Replace `KMS key ARN` with the Amazon
         Resource Name (ARN) of the KMS key. To locate the key ARN, see [Finding the key ID and
         ARN](../../../kms/latest/developerguide/find-cmk-id-arn.md "../../../kms/latest/developerguide/find-cmk-id-arn.md") in the *AWS Key Management Service Developer Guide*.
        2. Replace `123456789012` with the
         AWS account ID that owns the GuardDuty account exporting the
         findings.
        3. Replace `Region2` with the AWS Region where
         the GuardDuty findings are generated.
        4. Replace `SourceDetectorID` with the
         `detectorID` of the GuardDuty account in the specific Region
         where the findings generated.


        To find the `detectorId` for your account and current Region, see the
        **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
        or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

2.  ###### Attach policy to Amazon S3 bucket

If you do not already have an Amazon S3 bucket where you want to export these findings, see
[Creating a
bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_.

    1. Perform the steps under [To create or edit
     a bucket policy](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md") in the *Amazon S3 User Guide*, until
     the **Edit bucket policy** page appears.
    2. The **example policy** shows how grant GuardDuty
     permission to export findings to your Amazon S3 bucket. If you change the path
     after you configure export findings, then you must modify the policy to
     grant permission to the new location.


    Copy the following **example policy** and
     paste it into the **Bucket policy editor**.


    If you added the policy statement before the final statement, add a comma
     before adding this statement. Make sure that the JSON syntax of your
     KMS key policy is valid.


    **S3 bucket example policy**



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Sid": "Allow GetBucketLocation",
     "Effect": "Allow",
     "Principal": {
     "Service": "guardduty.amazonaws.com"
     },
     "Action": "s3:GetBucketLocation",
     "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
     "Condition": {
     "StringEquals": {
     "aws:SourceAccount": "`123456789012`",
     "aws:SourceArn": "arn:aws:guardduty:`us-east-2`:`123456789012`:detector/`SourceDetectorID`"

     }
     }
     },
     {
     "Sid": "Allow PutObject",
     "Effect": "Allow",
     "Principal": {
     "Service": "guardduty.amazonaws.com"
     },
     "Action": "s3:PutObject",
     "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`[optional prefix]/*",
     "Condition": {
     "StringEquals": {
     "aws:SourceAccount": "`123456789012`",
     "aws:SourceArn": "arn:aws:guardduty:`us-east-2`:`123456789012`:detector/`SourceDetectorID`"

     }
     }
     },
     {
     "Sid": "Deny unencrypted object uploads",
     "Effect": "Deny",
     "Principal": {
     "Service": "guardduty.amazonaws.com"
     },
     "Action": "s3:PutObject",
     "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`[optional prefix]/*",
     "Condition": {
     "StringNotEquals": {
     "s3:x-amz-server-side-encryption": "aws:kms"
     }
     }
     },
     {
     "Sid": "Deny incorrect encryption header",
     "Effect": "Deny",
     "Principal": {
     "Service": "guardduty.amazonaws.com"
     },
     "Action": "s3:PutObject",
     "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`[optional prefix]/*",
     "Condition": {
     "StringNotEquals": {
     "s3:x-amz-server-side-encryption-aws-kms-key-id": "arn:aws:kms:`us-east-2`:`111122223333`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
     }
     }
     },
     {
     "Sid": "Deny non-HTTPS access",
     "Effect": "Deny",
     "Principal": "*",
     "Action": "s3:*",
     "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`[optional prefix]/*",
     "Condition": {
     "Bool": {
     "aws:SecureTransport": "false"
     }
     }
     }
     ]
    }`

    ```
    3. Edit the policy by replacing the following values that are formatted in
     *`red`* in the policy
     example:




    	1. Replace `Amazon S3 bucket ARN` with the Amazon
    	 Resource Name (ARN) of the Amazon S3 bucket. You can find the
    	 **Bucket ARN** on the **Edit bucket
    	 policy** page in the [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/") console.
    	2. Replace `123456789012` with the
    	 AWS account ID that owns the GuardDuty account exporting the
    	 findings.
    	3. Replace `Region2` with the AWS Region
    	 where the GuardDuty findings are generated.
    	4. Replace `SourceDetectorID` with the
    	 `detectorID` of the GuardDuty account in the specific
    	 Region where the findings generated.


    	To find the `detectorId` for your account and current Region, see the
    	**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
    	or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.
    	5. Replace `[optional prefix]` part of the
    	 `S3 bucket ARN/[optional prefix]`
    	 placeholder value with an optional folder location to which you want
    	 to export the findings. For more information about the use of
    	 prefixes, see [Organizing
    	 objects using prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md") in the
    	 *Amazon S3 User Guide*.


    	When you provide an optional folder location that doesn't exist
    	 already, GuardDuty will create that location only if the account
    	 associated with the S3 bucket is the same as the account exporting
    	 the findings. When you export findings to an S3 bucket that belongs
    	 to another account, the folder location must exist already.
    	6. Replace `KMS key ARN` with the Amazon
    	 Resource Name (ARN) of the KMS key associated with the encryption
    	 of the findings exported to the S3 bucket. To locate the key ARN,
    	 see [Finding the key
    	 ID and ARN](../../../kms/latest/developerguide/find-cmk-id-arn.md "../../../kms/latest/developerguide/find-cmk-id-arn.md") in the
    	 *AWS Key Management Service Developer Guide*.

3. ###### Steps in GuardDuty console
   1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
   2. In the navigation pane, choose **Settings**.
   3. On the **Settings** page, under **Findings export options,**
      for **S3 bucket**, choose **Configure now** (or **Edit**,
      as needed).
   4. For **S3 bucket ARN**, enter the `bucket ARN` to which you want to send the findings. To
      view the bucket ARN, see [Viewing the properties for an S3 bucket](../../../AmazonS3/latest/userguide/view-bucket-properties.md "../../../AmazonS3/latest/userguide/view-bucket-properties.md")
      in the _Amazon S3 User Guide_.
   5. For **KMS key ARN**, enter the `key ARN`. To locate the key ARN,
      see [Find the key ID and key ARN](../../../kms/latest/developerguide/find-cmk-id-arn.md "../../../kms/latest/developerguide/find-cmk-id-arn.md") in the
      _AWS Key Management Service Developer Guide_.
   6. Choose **Save**.

[Show moreShow less](# "#")

## Step 4: Set up GuardDuty finding alerts through SNS

GuardDuty integrates with Amazon EventBridge, which can be used to send findings data to other
applications and services for processing. With EventBridge you can use GuardDuty findings to
initiate automatic responses to your findings by connecting finding events to targets
such as AWS Lambda functions, Amazon EC2 Systems Manager automation, Amazon Simple Notification Service (SNS) and more.

In this example you will create an SNS topic to be the target of an EventBridge rule, then
you'll use EventBridge to create a rule that captures findings data from GuardDuty. The resulting
rule forwards the finding details to an email address. To learn how you can send
findings to Slack or Amazon Chime, and also modify the types of findings alerts are sent for,
see [Set up an Amazon SNS
topic and endpoint](guardduty_findings_eventbridge.md#guardduty-eventbridge-set-up-sns-and-endpoint "guardduty_findings_eventbridge.md#guardduty-eventbridge-set-up-sns-and-endpoint").

**To create an SNS topic for your findings
alerts**

1. Open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Topics**.
3. Choose **Create Topic**.
4. For **Type**, select **Standard**.
5. For **Name**, enter `GuardDuty`.
6. Choose **Create Topic**. The topic details for your new topic
   will open.
7. In the **Subscriptions** section, choose **Create
   subscription**.
8. For **Protocol**, choose **Email**.
9. For **Endpoint**, enter the email address to send
   notifications to.
10. Choose **Create subscription**.

After you create your subscription, you must confirm the subscription through
email. 11. To check for a subscription message, go to your email inbox, and in the
subscription message, choose **Confirm subscription**.

###### Note

To check the email confirmation status, go to the SNS console and choose
**Subscriptions**.

**To create an EventBridge rule to capture GuardDuty findings and format
them**

1. Open the EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule.

A rule can't have the same name as another rule in the same Region and on the
same event bus. 5. For **Event bus**, choose
**default**. 6. For **Rule type**, choose **Rule with an event
pattern**. 7. Choose **Next**. 8. For **Event source**, choose **AWS
events**. 9. For **Event pattern**, choose **Event pattern
form**. 10. For **Event source**, choose **AWS
services**. 11. For **AWS service**, choose
**GuardDuty**. 12. For **Event Type**, choose **GuardDuty
Finding**. 13. Choose **Next**. 14. For **Target types**, choose **AWS
service**. 15. For **Select a target**, choose **SNS
topic**, and for **Topic**, choose the name of the
SNS topic you created earlier. 16. In the **Additional settings** section, for
**Configure target input**, choose **Input
transformer**.

Adding an input transformer formats the JSON finding data sent from GuardDuty into
a human-readable message. 17. Choose **Configure input transformer**. 18. In the **Target input transformer** section, for
**Input path**, paste the following code:

```

{
  "severity": "$.detail.severity",
  "Finding_ID": "$.detail.id",
  "Finding_Type": "$.detail.type",
  "region": "$.region",
  "Finding_description": "$.detail.description"
}

```

19. To format the email, for **Template**, paste the following
    code and make sure to replace the text in red with the values appropriate to
    your Region:

```

"You have a severity `severity` GuardDuty finding type `Finding_Type` in the `Region_Name` Region."
"Finding Description:"
"`Finding_Description`."
"For more details open the GuardDuty console at https://console.aws.amazon.com/guardduty/home?region=`region`#/findings?search=id%3D`Finding_ID`"

```

20. Choose **Confirm**.
21. Choose **Next**.
22. (Optional) Enter one or more tags for the rule. For more information, see
    [Amazon EventBridge tags](../../../eventbridge/latest/userguide/eb-tagging.md "../../../eventbridge/latest/userguide/eb-tagging.md") in
    the _Amazon EventBridge User Guide_.
23. Choose **Next**.
24. Review the details of the rule and choose **Create
    rule**.
25. (Optional) Test your new rule by generating sample findings with the process
    in Step 2. You will receive an email for each sample finding generated.

## Next steps

As you continue to use GuardDuty, you will come to understand the types of findings that
are relevant to your environment. Whenever you receive a new finding, you can find
information, including remediation recommendations about that finding, by selecting
**Learn more** from the finding description in the finding details
pane, or by searching for the finding name on [GuardDuty finding types](guardduty_finding-types-active.md "guardduty_finding-types-active.md").

The following features will help you tune GuardDuty so that it can provide the most
relevant findings for your AWS environment:

- To easily sort findings based on specific criteria, such as instance ID,
  account ID, S3 bucket name, and more, you can create and save filters within
  GuardDuty. For more information, see [Filtering findings in GuardDuty](guardduty_filter-findings.md "guardduty_filter-findings.md").
- If you are receiving findings for expected behavior in your environment, you
  can automatically archive findings based on the criteria you define with [suppression rules](findings_suppression-rule.md "findings_suppression-rule.md").
- To prevent findings from being generated from a subset of trusted IPs, or to
  have GuardDuty monitor IPs outside it's normal monitoring scope, you can set up
  [Trusted IP and threat
  lists](guardduty_upload-lists.md "guardduty_upload-lists.md").
