# Using Global endpoints in Amazon SES

Amazon SES Global endpoints is a feature that enhances the continuity and reliability of your email
sending operations. This chapter will guide you through the concept, setup, and usage of
Global endpoints, helping you leverage multi-region sending (MRS) to achieve higher availability and
improved disaster recovery capabilities for your email workloads.

## What are Global endpoints?

Global endpoints are resources that allow you to distribute your SES outbound workloads across
two AWS Regions. Once configured, SES automatically splits your sending traffic
between the selected primary and secondary regions. If either region experiences an
impairment, SES will automatically shift traffic away from the affected region to
maintain continuity of your sending operations.

Key benefits of using Global endpoints include:

- Improved email sending continuity
- Automatic failover between regions
- Simplified multi-region configuration

## How Global endpoints work

When you set up a Global endpoint, you select a primary region (where the endpoint is created)
and a secondary region. SES then creates a multi-region endpoint (MREP) that
serves as the entry point for your email sending requests.

The Global endpoint setup process synchronizes key artifacts and sending limits from your primary
region to your secondary region. This ensures that both regions have equivalent verified
identities, configuration sets, and approved sending limits sufficient for all of the
expected volume.

Once the Global endpoint is ready and its Endpoint ID is specified in the SendEmail API call,
SES automatically routes your outbound traffic evenly between your primary and
secondary regions. If either region becomes impaired, traffic will be weighted away from
that region towards the other one until the impairment is resolved.

## Setting up Global endpoints

###### Topics

- [Prerequisites](#prerequisites "#prerequisites")
- [Creating a Global endpoint](#creating-global-endpoint "#creating-global-endpoint")
- [Global endpoint states](#global-endpoint-states "#global-endpoint-states")

### Prerequisites

Before creating a Global endpoint you'll first need to grant SES permission to create
Service-Linked Roles (SLRs) in your account. These roles enable essential service
functionalities and resource access needed to create, use, and monitor Global endpoints. This
can be done by implementing the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "ses.amazonaws.com"
 }
 }
 }
 ]
}`

```

### Creating a Global endpoint

To create a new Global endpoint:

1. Open the SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the navigation pane, choose **Global
   Endpoints**.
3. Choose **Create global endpoint** and enter a name in the
   **Name** field.
4. Select a secondary region from the dropdown menu. (Your primary region
   defaults to the region you signed into the console with.)
5. (Optional) Add one or more **Tags** to your Global endpoint.
6. Review the configuration and choose **Create global
   endpoint**.

The creation process may take a few seconds. Once completed, the status of your
Global endpoint will change to "Ready."

Using the AWS CLI:

```
aws sesv2 create-multi-region-endpoint --primary-region `us-west-2` --secondary-region `us-east-1` --endpoint-name `MyGlobalEndpoint`
```

In the preceding example:

- Replace `us-west-2` with the primary region for
  your Global endpoint.
- Replace `us-east-1` with the secondary region for
  your Global endpoint.
- Replace `MyGlobalEndpoint` with the friendly name
  to give your Global endpoint.

### Global endpoint states

Global endpoints can have the following states:

- _Creating_ – The resource is being
  provisioned
- _Ready_ – The resource is ready to use
- _Failed_ – The resource failed to be
  provisioned
- _Deleting_ – The resource is being deleted as
  requested

## Preparing the secondary region

Now that you've created your global endpoint, you must now ensure that the your email
sending configuration, including all its components (identities, configuration sets,
email templates, and sending limits), is consistent across the primary and secondary
regions before utilizing the Global endpoint for sending emails. This alignment is crucial to avoid
potential issues and ensure proper email delivery and tracking.

The Region duplication feature in the console assists you by automatically duplicating
resources and duplicating account-level settings from the primary to the secondary
region that will quickly help you to ensure that both regions have equivalent
configurations.

Based on resource dependencies, the order in which you duplicate resources matters. To
avoid conflicts, follow the topic order below:

###### Topics

- [(1) Duplicate configuration
  sets](#copying-configuration-sets "#copying-configuration-sets")
- [(2) Duplicate
  verified domain identities](#copying-verified-domain-identities "#copying-verified-domain-identities")
- [(3) Duplicate production
  limits](#aligning-production-limits "#aligning-production-limits")

### Duplicating configuration sets

You can select multiple configuration sets from your primary region to be
duplicated, along with their settings, in the secondary region.

The "Duplicate configuration sets" feature allows you to:

- Duplicate multiple configuration sets into the secondary region at
  once.
- Check for differences between configuration sets in the primary region and
  the secondary region.

###### To duplicate configuration sets:

1. On the **Global endpoints** page, choose the Global endpoint you want to
   duplicate by selecting it from the **Name** column.
2. In the **Duplicate configuration sets** card, expand
   **Configuration sets actions** and choose
   **Duplicate**.
3. Select up to 10 configuration sets followed by
   **Confirm**.
4. If the status is not successful, choose **View report**
   to identify the problem.
5. (Optional) For previously duplicated configuration sets, you can check for
   differences between the primary and secondary regions by selecting
   **Check differences** while repeating the last three
   steps.

###### Note

- If the configuration set you duplicated contains _Event
  destinations_, _Reputation options_,
  _Archiving options_, or is referenced in an
  _Email template_, these settings will need to be
  manually configured in the secondary region.
- If you have archiving enabled for sent (outbound) email in a
  configuration set in the primary region, you must manually enable
  archiving for sent (outbound) email in the secondary region's
  configuration set using an archive created in the secondary region with
  the same name.

### Duplicating verified domain

identities

To ensure the Global endpoint configuration works effectively, your sending domain identity
needs to be verified in both the primary and secondary regions. SES uses
[Deterministic Easy DKIM
(DEED)](send-email-authentication-dkim-deed.md "send-email-authentication-dkim-deed.md")
to simplify this process.

Deterministic Easy DKIM (DEED) is a feature that generates consistent DKIM tokens
across all AWS Regions based on a parent domain that is configured with [Easy DKIM](send-email-authentication-dkim-easy.md "send-email-authentication-dkim-easy.md"). This consistency
allows SES to automatically verify a domain in the secondary region once it's
verified in the primary region, without requiring additional DNS record updates.
Therefore, you must ensure that the domain identity you want to duplicate, that is
the parent, is already configured with Easy DKIM.

The "Duplicate verified domain identities" feature allows you to:

- Duplicate multiple domain identities into the secondary region at
  once.
- Verify them automatically with Deterministic Easy DKIM (DEED).
- Check for differences between identities in the primary region and the
  secondary region.

###### To duplicate identities from the SES console:

1. On the **Global endpoints** page, choose the Global endpoint you want to
   duplicate by selecting it from the **Name** column.
2. In the **Duplicate verified domain identities** card,
   expand **Identities actions** and choose
   **Duplicate**.
3. Select up to 10 identities followed by
   **Confirm**.
4. If the status is not successful, choose **View report**
   to identify the problem.
5. (Optional) For previously duplicated identities, you can check for
   differences between the primary and secondary regions by selecting
   **Check differences** while repeating the last three
   steps.

###### Note

- Domain identities verified with BYODKIM, or are self-signed, will need
  to be created manually in the secondary region, as DEED is not
  applicable in this case.
- Domain identities using _Mail-from attributes_,
  _Policies_, or _Feedback forwarding and
  notifications_ will need to have these features manually
  configured in the secondary region.

### Duplicating production limits

SES checks if sending limits are aligned between regions and allows you to
request limit increases in the secondary region if needed.

The "Duplicate production limits" feature allows you to:

- Check if production limits are aligned between primary and secondary
  regions.
- Request a limit increase in the secondary region if needed.

###### To duplicate production limits:

1. On the **Global endpoints** page, choose the Global endpoint you want to
   duplicate by selecting it from the **Name** column.
2. In the **Duplicate production limits** card, if the
   status displays _Sending limits not aligned_, expand
   **Sending limits actions**.
3. Select **Managing sending limits** for the secondary
   region.
4. The **Service Quotas** page opens in the secondary region
   where you can request increases to "Sending quota" and "Sending rate" to
   match the values from the primary region.

###### Tip

It's recommended that you request the maximum quota you're eligible
for in both regions. While email traffic is distributed amongst both
regions under normal operating conditions, during a failover event, the
full volume of email traffic will be sent to one region and its limits
should be enough to handle the full volume load. 5. (Optional) You can also request production increases for your primary
region by selecting **Managing sending limits** for the
primary region while repeating the previous two steps.

###### Important

It's crucial that both regions have the equivalent verified identities and
configuration sets that you intend to send email with, along with matching
sending limits to ensure proper functionality of the Global endpoint. Any
discrepancies could cause delivery failures, diminished failover reliability, and
missing metrics.

## Using Global endpoints

###### Topics

- [Integrating with your
  application](#integrating-with-application "#integrating-with-application")
- [Monitoring and metrics](#monitoring-and-metrics "#monitoring-and-metrics")

### Integrating with your

application

Using a Global endpoint in your application requires that you obtain its Endpoint ID.

###### To retrieve a Global endpoint's Endpoint ID:

1. From the SES console, go to the **Global endpoints** page and
   choose the Global endpoint you want to use by selecting it from the
   **Name** column.
2. Select the copy icon under **Endpoint ID** on the Global endpoint
   details page.

Using the AWS CLI:

```
aws sesv2 get-multi-region-endpoint --endpoint-name `MyGlobalEndpoint` --region `us-west-2`
```

In the preceding example:

- Replace `MyGlobalEndpoint` with the friendly name
  you gave your Global endpoint during creation.
- Replace `us-west-2` with the primary region where
  you created your Global endpoint.
- The API response will include the value of your Endpoint ID such as,
  `"EndpointId": "abcdef12.g3h"`.

Once you've obtained the Endpoint ID of your Global endpoint, you can update your [`SendEmail`](../APIReference-V2/API_SendEmail.md "../APIReference-V2/API_SendEmail.md") or [`SendBulkEmail`](../APIReference-V2/API_SendBulkEmail.md "../APIReference-V2/API_SendBulkEmail.md")
API calls to include the Endpoint ID value for the `endpoint-id`
parameter. Here's an example of how to specify the Endpoint ID in a SendEmail API
call using the AWS CLI:

```
aws sesv2 send-email \
                --from-email-address "sender@example.com" \
                --destination "ToAddresses=recipient@example.com" \
                --content "Subject={Data=Test email,Charset=UTF-8},Body={Text={Data=This is a test email sent using Amazon SES Global endpoints.,Charset=UTF-8}}" \
                --endpoint-id "`abcdef12.g3h`"
```

Replace `abcdef12.g3h` with the actual Endpoint ID you
obtained either through the console or API.

### Monitoring and metrics

The Global endpoints feature provides a unified view of your email sending
volume across both the primary and secondary regions. You can access these metrics
through the Cross-region metrics tab on the Global endpoint details page in the SES
console.

###### To access sending metrics across both regions:

1. From the SES console, go to the **Global endpoints** page,
   choose the Global endpoint you want to see metrics for by selecting it from the
   **Name** column.
2. Select the **Cross-region metrics** tab on the Global endpoint
   details page and enter a date range of up to 31 days. Metrics for both
   regions will be displayed for the given date range.

Using the AWS CLI:

```
aws cloudwatch get-metric-statistics \
                --namespace AWS/SES \
                --metric-name SendCount \
                --dimensions Name=ses:multi-region-endpoint-id,Value=`abcdef12.g3h` \
                --start-time 2024-10-01T00:00:00Z \ --end-time 2024-10-31T23:59:59Z \
                --period 86400 \
                --statistics Sum
```

Replace `abcdef12.g3h` with your actual Endpoint
ID.

## Best practices and

considerations

Following these best practices and considerations helps ensure effective utilization,
monitoring, and cost optimization of Global endpoints across multiple AWS Regions for improved
availability and reliability of email sending capabilities.

- Regularly synchronize any changes made to artifacts (e.g., configuration sets,
  verified identities) between regions to maintain sending integrity.
- Monitor the Cross-region metrics to ensure balanced traffic distribution and
  identify any potential issues.
- Be aware that while Global endpoints provide improved availability, they do not change
  the physical state of regional availability for SES Outbound.
- Note that at launch, Global endpoints do not support SMTP or VPC endpoint access.
- Consider potential egress charges if using an AWS address translation
  gateway.
- Be aware that there may be fractional increases in API latency when making
  calls to MREP-enabled distant regions.

## Pricing

While exact pricing details are subject to change, Global endpoints are expected to carry a price
premium over single-region sending for an equal volume of mail. Despite this increase,
the overall cost is anticipated to remain competitive compared to other email service
providers.

For the most up-to-date pricing information, please refer to the [Amazon SES Pricing page](https://aws.amazon.com/ses/pricing/ "https://aws.amazon.com/ses/pricing/").
