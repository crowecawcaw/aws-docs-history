

# Using Global endpoints in Amazon SES
<a name="global-endpoints"></a>

Amazon SES Global endpoints is a feature that enhances the continuity and reliability of your email sending operations. This chapter will guide you through the concept, setup, and usage of Global endpoints, helping you leverage multi-region sending (MRS) to achieve higher availability and improved disaster recovery capabilities for your email workloads.

## What are Global endpoints?
<a name="what-are-global-endpoints"></a>

Global endpoints are resources that allow you to distribute your SES outbound workloads across two AWS Regions. Once configured, SES automatically divides your sending traffic between the selected primary and secondary regions. If either region experiences an impairment, SES will automatically shift traffic away from the affected region to maintain continuity of your sending operations.

Key benefits of using Global endpoints include:
+ Improved email sending continuity
+ Automatic failover between regions
+ Simplified multi-region configuration

## How Global endpoints work
<a name="how-global-endpoints-work"></a>

When you set up a Global endpoint, you select a primary region (where the endpoint is created) and a secondary region. SES then creates a multi-region endpoint (MREP) that serves as the entry point for your email sending requests.

The Global endpoint setup process synchronizes key artifacts and sending limits from your primary region to your secondary region. This ensures that both regions have equivalent verified identities, configuration sets, and approved sending limits sufficient for all of the expected volume.

Once the Global endpoint is ready and its Endpoint ID is specified in the SendEmail API call, SES automatically routes your outbound traffic between your primary and secondary regions. If either region becomes impaired, traffic will be weighted away from that region towards the other one until the impairment is resolved.

## Setting up Global endpoints
<a name="setting-up-global-endpoints"></a>

**Topics**
+ [Prerequisites](#prerequisites)
+ [Creating a Global endpoint](#creating-global-endpoint)
+ [Global endpoint states](#global-endpoint-states)

### Prerequisites
<a name="prerequisites"></a>

Before creating a Global endpoint you'll first need to grant SES permission to create Service-Linked Roles (SLRs) in your account. These roles enable essential service functionalities and resource access needed to create, use, and monitor Global endpoints. This can be done by implementing the following policy:

------
#### [ JSON ]

****  

```
{
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
}
```

------

### Creating a Global endpoint
<a name="creating-global-endpoint"></a>

To create a new Global endpoint:

1. Open the SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the navigation pane, choose **Global Endpoints**.

1. Choose **Create global endpoint** and enter a name in the **Name** field.

1. Select a secondary region from the dropdown menu. (Your primary region defaults to the region you signed into the console with.)

1. (Optional) Add one or more **Tags** to your Global endpoint.

1. Review the configuration and choose **Create global endpoint**.

The creation process may take a few seconds. Once completed, the status of your Global endpoint will change to "Ready."

Using the AWS CLI:

```
aws sesv2 create-multi-region-endpoint --primary-region {{us-west-2}} --secondary-region {{us-east-1}} --endpoint-name {{MyGlobalEndpoint}}
```

In the preceding example:
+ Replace {{us-west-2}} with the primary region for your Global endpoint.
+ Replace {{us-east-1}} with the secondary region for your Global endpoint.
+ Replace {{MyGlobalEndpoint}} with the friendly name to give your Global endpoint.

### Global endpoint states
<a name="global-endpoint-states"></a>

Global endpoints can have the following states:
+ *Creating* – The resource is being provisioned
+ *Ready* – The resource is ready to use
+ *Failed* – The resource failed to be provisioned
+ *Deleting* – The resource is being deleted as requested

## Preparing the secondary region
<a name="region-replication"></a>

Now that you've created your global endpoint, you must now ensure that the your email sending configuration, including all its components (identities, configuration sets, email templates, and sending limits), is consistent across the primary and secondary regions before utilizing the Global endpoint for sending emails. This alignment is crucial to avoid potential issues and ensure proper email delivery and tracking.

The Region duplication feature in the console assists you by automatically duplicating resources and duplicating account-level settings from the primary to the secondary region that will quickly help you to ensure that both regions have equivalent configurations.

Based on resource dependencies, the order in which you duplicate resources matters. To avoid conflicts, follow the topic order below:

**Topics**
+ [(1) Duplicate configuration sets](#copying-configuration-sets)
+ [(2) Duplicate verified domain identities](#copying-verified-domain-identities)
+ [(3) Duplicate production limits](#aligning-production-limits)

### Duplicating configuration sets
<a name="copying-configuration-sets"></a>

You can select multiple configuration sets from your primary region to be duplicated, along with their settings, in the secondary region.

The "Duplicate configuration sets" feature allows you to:
+ Duplicate multiple configuration sets into the secondary region at once.
+ Check for differences between configuration sets in the primary region and the secondary region.

**To duplicate configuration sets:**

1. On the **Global endpoints** page, choose the Global endpoint you want to duplicate by selecting it from the **Name** column.

1. In the **Duplicate configuration sets** card, expand **Configuration sets actions** and choose **Duplicate**.

1. Select up to 10 configuration sets followed by **Confirm**.

1. If the status is not successful, choose **View report** to identify the problem.

1. (Optional) For previously duplicated configuration sets, you can check for differences between the primary and secondary regions by selecting **Check differences** while repeating the last three steps.

**Note**  
If the configuration set you duplicated contains *Event destinations*, *Reputation options*, *Archiving options*, or is referenced in an *Email template*, these settings will need to be manually configured in the secondary region. 
If you have archiving enabled for sent (outbound) email in a configuration set in the primary region, you must manually enable archiving for sent (outbound) email in the secondary region's configuration set using an archive created in the secondary region with the same name.

### Duplicating verified domain identities
<a name="copying-verified-domain-identities"></a>

To ensure the Global endpoint configuration works effectively, your sending domain identity needs to be verified in both the primary and secondary regions. SES uses [Deterministic Easy DKIM (DEED)](send-email-authentication-dkim-deed.md) to simplify this process.

Deterministic Easy DKIM (DEED) is a feature that generates consistent DKIM tokens across all AWS Regions based on a parent domain that is configured with [Easy DKIM](send-email-authentication-dkim-easy.md). This consistency allows SES to automatically verify a domain in the secondary region once it's verified in the primary region, without requiring additional DNS record updates. Therefore, you must ensure that the domain identity you want to duplicate, that is the parent, is already configured with Easy DKIM.

The "Duplicate verified domain identities" feature allows you to:
+ Duplicate multiple domain identities into the secondary region at once.
+ Verify them automatically with Deterministic Easy DKIM (DEED).
+ Check for differences between identities in the primary region and the secondary region.

**To duplicate identities from the SES console:**

1. On the **Global endpoints** page, choose the Global endpoint you want to duplicate by selecting it from the **Name** column.

1. In the **Duplicate verified domain identities** card, expand **Identities actions** and choose **Duplicate**.

1. Select up to 10 identities followed by **Confirm**.

1. If the status is not successful, choose **View report** to identify the problem.

1. (Optional) For previously duplicated identities, you can check for differences between the primary and secondary regions by selecting **Check differences** while repeating the last three steps.

**Note**  
Domain identities verified with BYODKIM, or are self-signed, will need to be created manually in the secondary region, as DEED is not applicable in this case.
Domain identities using *Mail-from attributes*, *Policies*, or *Feedback forwarding and notifications* will need to have these features manually configured in the secondary region.

### Duplicating production limits
<a name="aligning-production-limits"></a>

SES checks if sending limits are aligned between regions and allows you to request limit increases in the secondary region if needed.

The "Duplicate production limits" feature allows you to:
+ Check if production limits are aligned between primary and secondary regions.
+ Request a limit increase in the secondary region if needed.

**To duplicate production limits:**

1. On the **Global endpoints** page, choose the Global endpoint you want to duplicate by selecting it from the **Name** column.

1. In the **Duplicate production limits** card, if the status displays *Sending limits not aligned*, expand **Sending limits actions**.

1. Select **Managing sending limits** for the secondary region.

1. The **Service Quotas** page opens in the secondary region where you can request increases to "Sending quota" and "Sending rate" to match the values from the primary region.
**Tip**  
It's recommended that you request the maximum quota you're eligible for in both regions. While email traffic is distributed amongst both regions under normal operating conditions, during a failover event, the full volume of email traffic will be sent to one region and its limits should be enough to handle the full volume load.

1. (Optional) You can also request production increases for your primary region by selecting **Managing sending limits** for the primary region while repeating the previous two steps.

**Important**  
It's crucial that both regions have the equivalent verified identities and configuration sets that you intend to send email with, along with matching sending limits to ensure proper functionality of the Global endpoint. Any discrepancies could cause delivery failures, diminished failover reliability, and missing metrics.

## Using Global endpoints
<a name="using-global-endpoints"></a>

**Topics**
+ [Integrating with your application](#integrating-with-application)
+ [Monitoring and metrics](#monitoring-and-metrics)

### Integrating with your application
<a name="integrating-with-application"></a>

Using a Global endpoint in your application requires that you obtain its Endpoint ID.

**To retrieve a Global endpoint's Endpoint ID:**

1. From the SES console, go to the **Global endpoints** page and choose the Global endpoint you want to use by selecting it from the **Name** column.

1. Select the copy icon under **Endpoint ID** on the Global endpoint details page.

Using the AWS CLI:

```
aws sesv2 get-multi-region-endpoint --endpoint-name {{MyGlobalEndpoint}} --region {{us-west-2}}
```

In the preceding example:
+ Replace {{MyGlobalEndpoint}} with the friendly name you gave your Global endpoint during creation.
+ Replace {{us-west-2}} with the primary region where you created your Global endpoint.
+ The API response will include the value of your Endpoint ID such as, `"EndpointId": "abcdef12.g3h"`.

Once you've obtained the Endpoint ID of your Global endpoint, you can update your [`SendEmail`](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendEmail.html) or [`SendBulkEmail`](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendBulkEmail.html) API calls to include the Endpoint ID value for the `endpoint-id` parameter. Here's an example of how to specify the Endpoint ID in a SendEmail API call using the AWS CLI:

```
aws sesv2 send-email \ 
                --from-email-address "sender@example.com" \ 
                --destination "ToAddresses=recipient@example.com" \ 
                --content "Subject={Data=Test email,Charset=UTF-8},Body={Text={Data=This is a test email sent using Amazon SES Global endpoints.,Charset=UTF-8}}" \ 
                --endpoint-id "{{abcdef12.g3h}}"
```

Replace {{abcdef12.g3h}} with the actual Endpoint ID you obtained either through the console or API.

### Monitoring and metrics
<a name="monitoring-and-metrics"></a>

The Global endpoints feature provides a unified view of your email sending volume across both the primary and secondary regions. You can access these metrics through the Cross-region metrics tab on the Global endpoint details page in the SES console.

**To access sending metrics across both regions:**

1. From the SES console, go to the **Global endpoints** page, choose the Global endpoint you want to see metrics for by selecting it from the **Name** column.

1. Select the **Cross-region metrics** tab on the Global endpoint details page and enter a date range of up to 31 days. Metrics for both regions will be displayed for the given date range. 

Using the AWS CLI:

```
aws cloudwatch get-metric-statistics \ 
                --namespace AWS/SES \ 
                --metric-name SendCount \ 
                --dimensions Name=ses:multi-region-endpoint-id,Value={{abcdef12.g3h}} \ 
                --start-time 2024-10-01T00:00:00Z \ --end-time 2024-10-31T23:59:59Z \ 
                --period 86400 \ 
                --statistics Sum
```

Replace {{abcdef12.g3h}} with your actual Endpoint ID.

## Best practices and considerations
<a name="best-practices-and-considerations"></a>

Following these best practices and considerations helps ensure effective utilization, monitoring, and cost optimization of Global endpoints across multiple AWS Regions for improved availability and reliability of email sending capabilities.
+ Regularly synchronize any changes made to artifacts (e.g., configuration sets, verified identities) between regions to maintain sending integrity.
+ Monitor the Cross-region metrics to ensure balanced traffic distribution and identify any potential issues.
+ Be aware that there may be fractional increases in API latency when making calls to MREP-enabled distant regions.
+ To ensure balanced traffic distribution, adopt an active-active architecture that mirrors the regions of your Global endpoint. Alternatively, choose two regions that are approximately equally distant from your client application.
+ Configure your client application to detect routing changes quickly. Global endpoints publish current routing weights through DNS. Set the positive DNS cache TTL to approximately 60 seconds and the negative DNS cache TTL to approximately 10 seconds in your runtime and resolver configuration. On the JVM, these are controlled by the `networkaddress.cache.ttl` and `networkaddress.cache.negative.ttl` security properties.
+ Set HTTP connection lifetime limits in your client. Long-lived keep-alive connections continue to reach the originally resolved IP address even after DNS refreshes. Set a short [Connection TTL](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/client-configuration.html#client-configuration-http) of approximately 60 seconds on your HTTP client so that pooled connections are replaced regularly. Most AWS SDKs expose this setting.
+ Global endpoints do not support SMTP or VPC endpoint access.
+ Consider potential egress charges if routing traffic through a NAT Gateway.

## Pricing
<a name="pricing-and-sla"></a>

While exact pricing details are subject to change, Global endpoints are expected to carry a price premium over single-region sending for an equal volume of mail. Despite this increase, the overall cost is anticipated to remain competitive compared to other email service providers.

For the most up-to-date pricing information, please refer to the [Amazon SES Pricing page](https://aws.amazon.com/ses/pricing/).