# Link monitoring accounts with source

accounts

The topics in this section explain how to set up links between monitoring accounts and
source accounts.

We recommend that you create a new AWS account to serve as the monitoring account
for your organization.

###### Contents

- [Necessary
  permissions](CloudWatch-Unified-Cross-Account-Setup.md#CloudWatch-Unified-Cross-Account-Setup-permissions "CloudWatch-Unified-Cross-Account-Setup.md#CloudWatch-Unified-Cross-Account-Setup-permissions")
  - [Permissions needed to create links](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-permissions-setup "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-permissions-setup")
  - [Permissions needed to monitor across accounts](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-permissions-monitor "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-permissions-monitor")

- [Setup overview](CloudWatch-Unified-Cross-Account-Setup.md#CloudWatch-Unified-Cross-Account-Setup-overview "CloudWatch-Unified-Cross-Account-Setup.md#CloudWatch-Unified-Cross-Account-Setup-overview")
- [Step 1: Set
  up a monitoring account](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-Setup-ConfigureMonitoringAccount "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-Setup-ConfigureMonitoringAccount")
- [Step 2: (Optional)
  Download an AWS CloudFormation template or URL](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-Setup-TemplateOrURL "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-Setup-TemplateOrURL")
- [Step 3: Link
  the source accounts](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-Setup-ConfigureSourceAccount "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-Setup-ConfigureSourceAccount")
  - [Use an AWS CloudFormation
    template to set up all accounts in an organization or an organizational unit
    as source accounts](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-SetupSource-OrgTemplate "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-SetupSource-OrgTemplate")
  - [Use an AWS CloudFormation
    template to set up individual source accounts](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-SetupSource-SingleTemplate "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-SetupSource-SingleTemplate")
  - [Use a URL to set
    up individual source accounts](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-SetupSource-SingleURL "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-SetupSource-SingleURL")

## Necessary

permissions

### Permissions needed to create links

To create links between a monitoring account and a source account, you must be
signed in with certain permissions.

- **To set up a monitoring account** –
  You must have either full administrator access in the monitoring account, or
  you must sign in to that account with the following permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSinkModification",
 "Effect": "Allow",
 "Action": [
 "oam:CreateSink",
 "oam:DeleteSink",
 "oam:PutSinkPolicy",
 "oam:TagResource"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowReadOnly",
 "Effect": "Allow",
 "Action": ["oam:Get*", "oam:List*"],
 "Resource": "*"
 }
 ]
}`

```

- **Source account, scoped to a specific monitoring
  account** – To create, update, and manage links for
  just one specified monitoring account, you must sign in to account with at least the
  following permissions. In this example, the monitoring account is
  `999999999999`.

If the link isn't going to share all seven resource types (metrics, logs, traces, Application Insights applications, Application Signals services and service level objectives (SLOs), and
Internet Monitor monitors), you can omit `cloudwatch:Link`, `logs:Link`,
`xray:Link`, `applicationinsights:Link`, `application-signals:Link`, or `internetmonitor:Link` as needed.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "oam:CreateLink",
 "oam:UpdateLink",
 "oam:DeleteLink",
 "oam:GetLink",
 "oam:TagResource"
 ],
 "Effect": "Allow",
 "Resource": "arn:*:oam:*:*:link/*"
 },
 {
 "Action": [
 "oam:CreateLink",
 "oam:UpdateLink"
 ],
 "Effect": "Allow",
 "Resource": "arn:*:oam:*:*:sink/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": [
 "999999999999"
 ]
 }
 }
 },
 {
 "Action": "oam:ListLinks",
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": "cloudwatch:Link",
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": "logs:Link",
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": "xray:Link",
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": "applicationinsights:Link",
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": "internetmonitor:Link",
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": "application-signals:Link",
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

- **Source account, with permissions to link to
  any monitoring account** – To
  create a link to any existing monitoring account sink and share
  metrics, log groups, traces, Application Insights applications, and Internet Monitor
  monitors,
  you must sign in to the source
  account with full administrator permissions or sign in there with the
  following permissions

If the link isn't going to share all seven resource types (metrics, logs, traces, Application Insights applications, Application Signals services and service level objectives (SLOs), and
Internet Monitor monitors), you can omit `cloudwatch:Link`, `logs:Link`,
`xray:Link`, `applicationinsights:Link`, `application-signals:Link`, or `internetmonitor:Link` as needed.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "oam:CreateLink",
 "oam:UpdateLink"
 ],
 "Resource": [
 "arn:aws:oam:*:*:link/*",
 "arn:aws:oam:*:*:sink/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "oam:List*",
 "oam:Get*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "oam:DeleteLink",
 "oam:GetLink",
 "oam:TagResource"
 ],
 "Resource": "arn:aws:oam:*:*:link/*"
 },
 {
 "Action": "cloudwatch:Link",
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": "xray:Link",
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": "logs:Link",
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": "applicationinsights:Link",
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": "internetmonitor:Link",
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": "application-signals:Link",
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

### Permissions needed to monitor across accounts

After a link has been created, to view source account information from a monitoring account, you must be signed in
to an account with one of the following:

- Full
  administrator access in the monitoring account
- The following cross-account permissions, in addition to permissions to view the specific types of
  resources that you will be monitoring

```
{
   "Sid": "AllowReadOnly",
   "Effect": "Allow",
   "Action": [
     "oam:Get*",
     "oam:List*"
   ],
   "Resource": "*"
 }
```

## Setup overview

The following high-level steps show you how to set up CloudWatch cross-account
observability.

###### Note

We recommend creating a new AWS account to use as your organization's
monitoring account.

1. Set up a dedicated monitoring account.
2. (Optional) Download an AWS CloudFormation template or copy a URL to link source
   accounts.
3. Link source accounts to the monitoring account.

After completing these steps, you can use the monitoring account to view the
observability data of the source accounts.

## Step 1: Set

up a monitoring account

Follow the steps in this section to set up an AWS account as a monitoring
account for CloudWatch cross-account observability.

###### Prerequisites

- **If you're setting up accounts in an AWS Organizations organization as the
  source accounts** – Get the organization path or
  organization ID.
- **If you're not using Organizations for the source accounts** – Get
  the account IDs of the source accounts.

To set up an account as a monitoring account, you must have certain permissions.
For more information, see [Necessary
permissions](#CloudWatch-Unified-Cross-Account-Setup-permissions "#CloudWatch-Unified-Cross-Account-Setup-permissions").

###### To set up a monitoring account

1. Sign in to the account that you want to use as a monitoring
   account.
2. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
3. In the left navigation pane, choose **Settings**.
4. By **Monitoring account configuration**, choose
   **Configure**.
5. For **Select data**, choose whether this monitoring
   account will be able to view **Logs**,
   **Metrics**,
   **Traces**, **Application Insights - Applications**,
   **Internet Monitor - Monitors**, and **Application Signals - Services, Service Level Objectives (SLOs)** data from
   the source accounts it is linked to.
6. For **List source accounts**, enter the source accounts
   that this monitoring account will view. To identify the source accounts,
   enter individual account IDs, organization paths, or organization IDs. If
   you enter an organization path or organization ID, this monitoring account
   is allowed to view observability data from all linked accounts in that
   organization.

Separate the entries in this list with commas.

###### Important

When you enter an organization path, follow the exact format. The ou-id must end with a `/` (a slash character).
For example: `o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-def0-awsbbbb/` 7. For **Define a label to use to identify your source account**,
you can define alabel that is used to create a AWS CloudFormation template. The label is then applied to source accounts when that template is used to link the source accounts to this monitoring account.

You can specify whether to use account names or email addresses in this label, and also use variables such as `$AccountName`, `$AcccountEmail`,
and `$AcccountEmailNoDomain`.

###### Note

In the AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions, the only supported option is to use custom labels, and the `$AccountName`, `$AcccountEmail`,
and `$AcccountEmailNoDomain` variables
all resolve as `account-id` instead of the specified variable. 8. Choose **Configure**.

###### Important

The link between the monitoring and source accounts is not complete until you
configure the source accounts. For more information, see the following
sections.

## Step 2: (Optional)

Download an AWS CloudFormation template or URL

To link source accounts to a monitoring account, we recommend using an AWS CloudFormation
template or a URL.

- **If you are linking an entire organization**
  – CloudWatch provides an AWS CloudFormation template.
- **If you are linking individual accounts**
  – Use either an AWS CloudFormation template or a URL that CloudWatch provides.

To use an AWS CloudFormation template, you must download it during these steps. After you link
the monitoring account with at least one source account, the AWS CloudFormation template is no
longer available to download.

###### To download an AWS CloudFormation template or copy a URL for linking source accounts to the

monitoring account

1. Sign in to the account that you want to use as a monitoring
   account.
2. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
3. In the left navigation pane, choose **Settings**.
4. By **Monitoring account configuration**, choose
   **Resources to link accounts**.
5. Do one of the following:
   - Choose **AWS organization** to get a template to use
     to link accounts in an organization to this monitoring
     account.
   - Choose **Any account** to get a template or URL for setting up individual
     accounts as source accounts.

6. Do one of the following:
   - If you chose **AWS organization**, choose
     **Download CloudFormation template**.
   - If you chose **Any account**, choose either
     **Download CloudFormation template** or
     **Copy URL**.

7. (Optional) Repeat steps 5-6 to download both the AWS CloudFormation template and
   the URL.

## Step 3: Link

the source accounts

Use the steps in these sections to link source accounts to a monitoring
account.

To link monitoring accounts with source accounts, you must have certain
permissions. For more information, see [Necessary
permissions](#CloudWatch-Unified-Cross-Account-Setup-permissions "#CloudWatch-Unified-Cross-Account-Setup-permissions").

### Use an AWS CloudFormation

template to set up all accounts in an organization or an organizational unit
as source accounts

These steps assume that you already downloaded the necessary AWS CloudFormation template by
performing the steps in [Step 2: (Optional)
Download an AWS CloudFormation template or URL](#Unified-Cross-Account-Setup-TemplateOrURL "#Unified-Cross-Account-Setup-TemplateOrURL").

###### To use an AWS CloudFormation template to link accounts in an organization or

organizational unit to the monitoring account

1. Sign in to the organization's management account.
2. Open the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
3. In the left navigation bar, choose
   **StackSets**.
4. Check that you are signed in to the Region that you want, then choose
   **Create StackSet**.
5. Choose **Next**.
6. Choose **Template is ready** and choose
   **Upload a template file**.
7. Choose **Choose file**, choose the template that you
   downloaded from the monitoring account, and choose
   **Open**.
8. Choose **Next**.
9. For **Specify StackSet details**, enter a name for
   the StackSet and choose **Next**.
10. For **Add stacks to stack set**, choose
    **Deploy new stacks**.
11. For **Deployment targets**, choose whether to deploy
    to the entire organization or to specified organizational units.
12. For **Specify regions**, choose which Regions to
    deploy CloudWatch cross-account observability to.
13. Choose **Next**.
14. On the **Review** page, confirm your selected options
    and choose **Submit**.
15. In the **Stack instances** tab, refresh the screen
    until you see that your stack instances have the status
    **CREATE_COMPLETE**.

### Use an AWS CloudFormation

template to set up individual source accounts

These steps assume that you already downloaded the necessary AWS CloudFormation template by
performing the steps in [Step 2: (Optional)
Download an AWS CloudFormation template or URL](#Unified-Cross-Account-Setup-TemplateOrURL "#Unified-Cross-Account-Setup-TemplateOrURL").

###### To use an AWS CloudFormation template to set up individual source accounts for CloudWatch

cross-account observability

1. Sign in to the source account.
2. Open the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
3. In the left navigation bar, choose **Stacks**.
4. Check that you are signed in to the Region that you want, then choose
   **Create stack**, **With new resources (standard)**.
5. Choose **Next**.
6. Choose **Upload a template file**.
7. Choose **Choose file**, choose the template that you
   downloaded from the monitoring account, and choose
   **Open**.
8. Choose **Next**.
9. For **Specify stack details**, enter a name for the
   stack and choose **Next**.
10. On the **Configure stack options** page, choose
    **Next**.
11. On the **Review** page, choose
    **Submit**.
12. On the status page for your stack, refresh the screen until you see
    that your stack has the status
    **CREATE_COMPLETE**.
13. To use this same template to link more source accounts to this
    monitoring account, sign out of this account and sign in to the next
    source account. Then repeat steps 2-12.

### Use a URL to set

up individual source accounts

These steps assume that you already copied the necessary URL by performing
the steps in [Step 2: (Optional)
Download an AWS CloudFormation template or URL](#Unified-Cross-Account-Setup-TemplateOrURL "#Unified-Cross-Account-Setup-TemplateOrURL").

###### To use a URL to link individual source accounts to the monitoring

account

1. Sign in to the account that you want to use as a source
   account.
2. Enter the URL that you copied from the monitoring account.

You see the CloudWatch settings page, with some information filled
in. 3. For **Select data**, choose whether this source account will share **Logs**,
**Metrics**,
**Traces**, **Application Insights - Applications**, and
**Internet Monitor - Monitors** data to this monitoring account.

For both **Logs** and
**Metrics**, you can choose whether to share all resources or a subset
with the monitoring account.

    1. (Optional) To share a subset of this account's log groups with the monitoring account, select **Logs**
     and choose **Filter Logs**. Then use the **Filter Logs** box to construct a query to find the log groups
     that you want to share. The query will use the term `LogGroupName` and one or
     more of the following operands.




    	* `=` and `!=`
    	* `AND`
    	* `OR`
    	* `^` indicates LIKE and `!^` indicates NOT LIKE. These can be used only as prefix searches. Include a `%` at the end
    	 of the string that you want to search for and include.
    	* `IN` and `NOT IN`, using parentheses (`( )`)
    The complete query must be no more than 2000 characters and is limited to five conditional operands.
     Conditional operands are `AND` and `OR`. There isn't a limit on the number of other operands.


    ###### Tip

    Choose **View sample queries** to see the correct syntax for common query formats.
    2. (Optional) To share a subset of this account's metric namespaces with the monitoring account, select **Metrics** and
     choose **Filter Metrics**. Then use the **Filter Metrics** box to construct a query to find the metric namespaces
     that you want to share. Use the term `Namespace` and one or
     more of the following operands.




    	* `=` and `!=`
    	* `AND`
    	* `OR`
    	* `LIKE` and `NOT LIKE`. These can be used only as prefix searches. Include a `%` at the end
    	 of the string that you want to search for and include.
    	* `IN` and `NOT IN`, using parentheses (`( )`)
    The complete query must be no more than 2000 characters and is limited to five conditional operands.
     Conditional operands are `AND` and `OR`. There isn't a limit on the number of other operands.###### Tip

Choose **View sample queries** to see the correct syntax for common query formats. 4. Do not change the ARN in **Enter monitoring account
configuration ARN**. 5. The **Define a label to identify your source
account** section is pre-filled with the label choice from
the monitoring account, if there is one. Optionally, choose **Edit** to
change it.

###### Note

In the AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions, the only supported option is to use custom labels, and the `$AccountName`, `$AcccountEmail`,
and `$AcccountEmailNoDomain` variables
all resolve as `account-id` instead of the specified variable. 6. Choose **Link**. 7. Enter `Confirm` in the box and choose
**Confirm**. 8. To use this same URL to link more source accounts to this monitoring
account, sign out of this account and sign in to the next source
account. Then repeat steps 2-7.
