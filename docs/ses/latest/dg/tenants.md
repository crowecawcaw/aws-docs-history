

# Tenants
<a name="tenants"></a>

This chapter explains how to use Amazon SES tenant management to isolate, monitor, and manage email sending across multiple tenants within your SES account. This feature helps Independent Software Vendors (ISVs), enterprises, and organizations sending emails on behalf of multiple downstream entities maintain separate reputation profiles and prevent issues with one tenant from affecting others.

## What is tenant management?
<a name="what-is-tenant-management"></a>

Tenant management is a feature that allows you to create isolated containers called "tenants" within your SES account. Each tenant can have its own email identities, configuration sets, templates, and reputation metrics, ensuring that email activities are completely separated between different customers or business units.

Tenant management addresses the challenge where one customer's poor email practices could previously pause an entire SES account, affecting all other customers. With tenant isolation, you can manage multiple email streams independently while maintaining centralized oversight and control.

A tenant serves as a logical container that groups related SES resources together. When you send emails on behalf of a specific tenant, SES tracks reputation metrics, and enforces policies at the tenant level. This isolation ensures that a high bounce rate or complaint rate from one tenant doesn't impact the deliverability of emails sent by other tenants.

Tenant management is particularly valuable for:
+ **Independent Software Vendors (ISVs)** sending emails on behalf of multiple customers.
+ **Enterprises** managing email communications across different business units.
+ **Service providers** who need to isolate email reputation by client or application.
+ **Organizations** requiring compliance with different regulatory requirements per tenant.

## How tenant management works
<a name="how-tenant-management-works"></a>

Tenant reputation management works by creating a logical container for your email sending resources. You assign specific resources to each tenant, including verified identities (domains and email addresses), configuration sets, and templates. When sending email on behalf of a tenant, you specify the tenant in your API call or SMTP header, and SES verifies that the resources being used are properly associated with that tenant.

### Resource association
<a name="resource-association"></a>

Resources in your SES account can be associated with tenants in two ways:
+ **Dedicated assignment** – Resources used exclusively by specific tenants.
+ **Shared assignment** – Resources available to multiple tenants.

When you associate a resource with a tenant, that tenant gains permission to use that resource for email sending. With each send request, SES validates that the specified tenant has permission to use the identity, configuration set, and template in the request. If the resources aren't properly associated, the send request fails.

### Reputation monitoring and enforcement
<a name="reputation-monitoring-enforcement"></a>

SES continuously monitors key reputation metrics for each tenant, including bounce rates, complaint rates (including those from the mailbox provider Feedback Loop (FBL) system), and third-party feedback signals. When these metrics exceed defined thresholds, SES creates "reputation findings" categorized as:
+ **Low severity warnings** – Minor issues that could affect deliverability if not addressed.
+ **High severity warnings** – Serious issues likely affecting deliverability that may trigger enforcement.

Based on these findings, SES can automatically pause problematic tenants through reputation policies that you configure. Three enforcement levels are available:
+ **Standard** (recommended) – Automatically pauses tenant sending when high-severity reputation findings are detected. This provides balanced protection while minimizing disruption.
+ **Strict** – Automatically pauses tenant sending when any reputation finding is detected, including low-severity issues. Provides maximum protection but may result in more frequent pausing.
+ **None** – Disables automated pausing for the tenant. All reputation findings are still recorded and visible, but no automated enforcement actions are taken.

When a tenant's metrics trigger a reputation finding that meets the threshold for enforcement under your selected policy, the system automatically updates the tenant's sending status to "Paused" without affecting the sending capability of other tenants. While a tenant is paused, any attempt to send email using that tenant will fail until you review the issue and manually re-enable sending. Additionally, you can manually pause a tenant's sending capabilities when needed, and unpause it when ready to resume sending.

## Setting up tenants
<a name="setting-up-tenants"></a>

**Topics**
+ [Creating tenants](#creating-tenants)
+ [Assigning resources to a tenant](#assigning-resources-to-tenant)
+ [Configuring reputation policies](#configuring-reputation-policies)

### Creating tenants
<a name="creating-tenants"></a>

**Using the console:**

1. Sign in to the AWS Management Console and open the SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the navigation pane, choose **Tenants**.

1. Choose **Create tenant**.

1. For **Tenant name**, enter a unique name for your tenant.

1. Choose **Create tenant**.

**Using the AWS CLI:**

```
aws sesv2 create-tenant \
    --tenant-name "MyTenant" \
    --region us-east-1
```

### Assigning resources to a tenant
<a name="assigning-resources-to-tenant"></a>

After creating a tenant, you must assign at least one verified identity and one configuration set before the tenant can send email.

**Using the console:**

1. In the SES console, navigate to the **Tenants** page.

1. Select the tenant you want to configure.

1. In the **Tenant setup** section, you can use the **Identities** and **Configuration sets** cards to assign these resources. Optionally, you can scroll down to the tabbed section and use the **Identities** and **Configuration sets** tabs to do the same.
**Note**  
Any attempt to delete an identity or configuration set that is associated with a tenant will fail. You must first remove these associations from the tenant before you can delete the associated resources.

1. (Optional) You can assign one or more tags to your tenant by selecting the **Tags** tab.

**Using the AWS CLI:**

```
# Assign an identity to a tenant
aws sesv2 create-tenant-resource-association \
    --tenant-name "MyTenant" \
    --resource-arn "arn:aws:ses:us-east-1:123456789012:identity/example.com" \
    --region us-east-1

# Assign a configuration set to a tenant
aws sesv2 create-tenant-resource-association \
    --tenant-name "MyTenant" \
    --resource-arn "arn:aws:ses:us-east-1:123456789012:configuration-set/MyConfigSet" \
    --region us-east-1
```

### Configuring reputation policies
<a name="configuring-reputation-policies"></a>

Reputation policies determine when a tenant's email sending is automatically paused based on reputation metrics. When you create a tenant, SES automatically assigns the *Standard* reputation policy. Use the following steps if you want to change to another policy.

**Using the console:**

1. In the SES console, navigate to the **Tenants** page.

1. Select the tenant you want to configure.

1. In the **Tenant setup** section, you can use the **Reputation policy** card to assign a policy. Optionally, you can scroll down to the tabbed section and use the **Reputation policy** tab to do the same.

1. Select one of the following policies:
   + **Standard (recommended)** – Pause sending when high-severity findings are detected.
   + **Strict** – Pause sending when any findings (including low-severity) are detected.
   + **None** – Do not automatically pause sending regardless of findings. *There are risks associated with this level as explained in [Trust & Safety](#integration-with-aws-trust-safety).*

**Using the AWS CLI:**

```
update-reputation-entity-policy \
    --reputation-entity-type "RESOURCE" \
    --reputation-entity-reference "arn:aws:ses:us-east-1:123456789012:tenant/tenantId" \
    --reputation-entity-policy "arn:aws:ses:us-east-1:aws:reputation-policy/standard"
```

## Sending email with tenants
<a name="sending-email-with-tenants"></a>

When sending email through a tenant, you must specify the tenant in your API calls or SMTP headers and ensure that all resources used are associated with that tenant.

**Topics**
+ [Using the SendEmail API with tenants](#using-sendemail-api-with-tenants)
+ [Using SMTP with tenants](#using-smtp-with-tenants)

### Using the SendEmail API with tenants
<a name="using-sendemail-api-with-tenants"></a>

**AWS CLI Example:**

```
aws sesv2 send-email \
  --tenant-name "MyTenant" \
  --from-email-address "sender@example.com" \
  --destination "ToAddresses=recipient@example.com" \
  --content "Simple={Subject={Data='Test Subject',Charset=utf-8},Body={Text={Data='Test email body',Charset=utf-8}}}" \
  --configuration-set-name "MyConfigSet"
```

**AWS SDK for Python Example:**

```
import boto3

client = boto3.client('sesv2')
response = client.send_email(
    FromEmailAddress='sender@example.com',
    Destination={
        'ToAddresses': ['recipient@example.com']
    },
    Content={
        'Simple': {
            'Subject': {
                'Data': 'Test email'
            },
            'Body': {
                'Text': {
                    'Data': 'This is a test email sent using a tenant.'
                }
            }
        }
    },
    ConfigurationSetName='MyConfigurationSet',
     TenantName='MyTenant'
)
```

### Using SMTP with tenants
<a name="using-smtp-with-tenants"></a>

When using SMTP to send email through a tenant, include the tenant information in an email header:

```
X-SES-TENANT: MyTenant
```

This header tells SES which tenant should be used for the email sending operation, allowing SES to apply the appropriate resource validation and reputation tracking.

## Managing tenant status
<a name="managing-tenant-status"></a>

**Topics**
+ [Viewing tenant status and metrics](#viewing-tenant-status-and-metrics)
+ [Pausing and unpausing tenants](#pausing-and-unpausing-tenants)

### Viewing tenant status and metrics
<a name="viewing-tenant-status-and-metrics"></a>

**Using the console:**

1. In the SES console, navigate to the **Tenants** page.

1. Select a tenant to view its details.

1. The **Tenant status** box displays:

   **Sending Status:**.
   + **Enabled** – The tenant can send emails.
   + **Paused** – You or SES automated policies have paused sending for this tenant.
   + **Enforced** – SES has paused sending due to serious reputation issues.
   + **Reinstated** – Sending was reactivated after being paused.

   **Reputation Status:**
   + **No findings detected** – No issues affecting deliverability.
   + **Low severity warning** – Minor issues that could affect deliverability if not addressed.
   + **High severity warning** – Serious issues likely affecting deliverability.

1. Scroll down to **Sending statistics** under the **Resources** tab to view delivery, bounce, and complaint metrics for the date range selected.

**Using the AWS CLI:**

```
# Get tenant details
aws sesv2 get-tenant --tenant-name "MyTenant"
```

### Pausing and unpausing tenants
<a name="pausing-and-unpausing-tenants"></a>

You can manually pause a tenant's sending capabilities when needed, and unpause it when ready to resume sending.

**Using the console:**

1. In the SES console, navigate to the **Tenants** page.

1. Select the checkbox next to the tenant you want to pause or unpause.

1. Choose **Pause sending** or **Resume sending**.

1. Confirm the action.

**Using the AWS CLI:**

To pause a tenant:

```
# Pause a tenant
aws sesv2 update-reputation-entity-customer-managed-status \
  --reputation-entity-type RESOURCE 
  --reputation-entity-reference "arn:aws:ses:us-east-1:593442965613:tenant/tenantId"
  --sending-status DISABLED
```

To unpause a tenant:

```
# Unpause a tenant
aws sesv2 update-reputation-entity-customer-managed-status \
  --reputation-entity-type RESOURCE 
  --reputation-entity-reference "arn:aws:ses:us-east-1:593442965613:tenant/tenantId"
  --sending-status ENABLED
```

## Working with reputation findings
<a name="working-with-reputation-findings"></a>

**Topics**
+ [Viewing reputation findings](#viewing-reputation-findings)
+ [Understanding reputation findings](#understanding-reputation-findings)
+ [Resolving reputation issues](#resolving-reputation-issues)

### Viewing reputation findings
<a name="viewing-reputation-findings"></a>

**Using the console:**

1. In the SES console, navigate to the **Tenants** page.

1. Select the tenant you want to examine.

1. Navigate to the **Reputation findings** table.

1. Review any active findings, including their type, severity, detection date, and guidance to resolve the issue.

**Using the AWS CLI:**

```
aws sesv2 list-recommendations \
   --filter='{ "RESOURCE_ARN":"arn:aws:ses:us-east-1:012345678901:tenant/tenantId"}'
```

The response includes details about all active findings:

```
{
    "Recommendations": [
        {
            "ResourceArn": "arn:aws:ses:us-east-1:012345678901:tenant/{tenant-name}/{tenant-id}",
            "Type": "BOUNCE",
            "Description": "The bounce rate exceeded 15.0% based on a representative volume of 664 emails from July 11, 2025 at 14:41 (UTC) to July 11, 2025 at 16:26 (UTC).",
            "Status": "OPEN",
            "CreatedTimestamp": "2025-07-11T16:16:14.029000+00:00",
            "LastUpdatedTimestamp": "2025-07-11T16:37:14.145000+00:00",
            "Impact": "HIGH"
        }
    ]
}
```

### Understanding reputation findings
<a name="understanding-reputation-findings"></a>

Reputation findings provide insights into potential issues with your tenants' email sending practices. Each finding includes:
+ **Impact** – Severity level (high or low).
+ **Finding type** – Bounce rates, complaint rates, third-party feedback from mailbox providers, and IP blocklist listings.
+ **Age** – Time since first detected date.
+ **Description** – Context about the problem (such as the specific rate that triggered the finding).
+ **Last checked** – Date of most recent status update.
+ **Resolve issue** – Links to the relevant section in the SES Developer Guide with guidance to help resolve the issue.

Common findings include:
+ **High bounce rates** – When bounce rates exceed configured thresholds.
+ **Complaint activity** – When spam reports are received from mailbox providers that exceed thresholds.
+ **Third-party feedback** – Negative signals from mailbox providers.
+ **Blocklist appearances** – When sending IPs appear on a reputation blocklist.

### Resolving reputation issues
<a name="resolving-reputation-issues"></a>

When you receive a reputation finding, it's important to investigate the root cause and take corrective action promptly:

1. **Address the root cause** – Advise your tenant to improve list hygiene, update email content, or fix technical issues.

1. **Review sending practices** – Ensure your tenant complies with email best practices.

1. **Monitor metrics** – Watch for improvement in bounce and complaint rates.

1. **Communicate with affected parties** – Inform relevant stakeholders about the issue and resolution steps.

## Monitoring and analytics
<a name="monitoring-and-analytics"></a>

**Topics**
+ [Setting up CloudWatch metrics](#cloud-watch-metrics)
+ [Setting up EventBridge notifications](#setting-up-eventbridge-notifications)

### Setting up CloudWatch metrics
<a name="cloud-watch-metrics"></a>

SES publishes tenant-specific metrics to Amazon CloudWatch. The following metrics are available for each tenant:
+ **Sends** – Total number of emails sent by the tenant.
+ **Bounces** – Number of bounced emails for the tenant.
+ **Complaints** – Number of bounced emails for the tenant.

**Accessing tenant metrics in CloudWatch:**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. Select the **AWS/SES** namespace.

1. Choose **By TenantId** and **TenantName** to view tenant-specific metrics.

### Setting up EventBridge notifications
<a name="setting-up-eventbridge-notifications"></a>

By default, SES sends events to the EventBridge default event bus when tenant reputation findings are detected or when tenant status changes occur.

You can create rules on the default event bus to identify specific events for EventBridge to send to one or more specified targets.

The following detail-types are available:

**For tenant sending status changes:**
+ `Sending Status Enabled` – The tenant is enabled and can send email.
+ `Sending Status Disabled` – The tenant has been paused and cannot send email.

**For reputation findings:**
+ `Advisor Recommendation Status Open`
+ `Advisor Recommendation Status Closed`

**Setting up EventBridge rules**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. Choose **Create rule**.

1. Enter a name and description for your rule.

1. For **Define pattern**, choose **Event pattern**.

1. Choose **Pre-defined pattern by service**.

1. Choose **SES** as the service name.

1. For **Event type**, choose **Sending Status Enabled** or **Sending Status Disabled**.

1. Configure the event pattern to match specific events you're interested in.

1. Choose your target (such as an AWS Lambda function, Amazon SNS topic, or Amazon SQS queue).

1. Configure any additional settings as needed.

1. Choose **Create**.

**Example EventBridge rule pattern for reputation findings:**

```
{
  "detail-type": "Advisor Recommendation Status Open",
  "source": "aws.ses",
  "account": "012345678901",
  "time": "2023-11-15T17:00:59Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:ses:us-east-1:012345678901:tenant/{tenant-name}/{tenant-id}"
  ],
  "detail": { 
       "version": "1.0.0",
       "data": "The bounce rate exceeded 15.0% based on a representative volume of 197 emails from July 11, 2025 at 14:43 (UTC) to July 11, 2025 at 16:13 (UTC).",
       "metadata":{"impact":"HIGH","type":"BOUNCE"}
  
    }
}
```

**Example EventBridge rule pattern for sending status changes:**

```
{
        "detail-type": "Sending Status Disabled",
        "source": "aws.ses",
        "account": "012345678901",
        "time": "2025-07-24T12:44:28Z",
        "region": "us-east-1",
        "resources": [
            "arn:aws:ses:us-east-1:012345678901:tenant/{tenant-name}/{tenant-id}"
        ],
        "detail": {
            "version": "1.0.0",
            "data": {
                "origin": "CUSTOMER_MANAGED",
                "record": {
                    "status": "DISABLED",
                    "cause": "Status manually updated.",
                    "lastUpdatedTimestamp": [2025, 7, 24, 12, 44, 28, 995000000]
                }
            }
        }
    }
```

Field descriptions:
+ **source** – Identifies the service that generated the event. For SES events, this value is `aws.ses`.
+ **detail-type** – The type of status change event (see Event Types above).
+ **resources** – Array containing the ARN of the affected tenant.
+ **detail.data.origin** – Source of the status change (e.g., "CUSTOMER\_MANAGED" or "AWS\_MANAGED").
+ **detail.data.record.status ** – The new status of the tenant (ENABLED, DISABLED, or REINSTATED).
+ **detail.data.record.cause** – Description of why the status changed.
+ **detail.data.record.lastUpdatedTimestamp ** – Timestamp when the status was updated.

You can use these events to monitor tenant status changes and automate responses in your applications. For example, you might want to trigger alerts when tenants are disabled or track tenant health metrics over time.

## Integration with AWS Trust & Safety
<a name="integration-with-aws-trust-safety"></a>

When AWS Trust & Safety detects issues that would normally result in account-level enforcement, the tenant system enables more targeted responses. Instead of pausing your entire account, Trust & Safety can pause only the problematic tenants while allowing compliant tenants to continue sending.

This tenant-level enforcement reduces the impact of reputation issues and helps maintain business continuity for your other email streams.

You'll receive notifications when SES has disabled sending due to high-severity issues affecting tenant reputation and has placed your account under review. A case will be opened for you in the AWS Support Center so that you can work with Trust & Safety to resolve issues and restore sending for the affected tenant.

**Note**  
As the account owner, it's your responsibility to monitor the reputation metrics of all your tenants. While the tenant feature isolates reputation tracking at the tenant level, their combined sending activity still affects your overall account reputation—tenants that develop poor sending practices could put your entire account at risk. Therefore, it's essential to ensure all tenants maintain good email sending practices to protect your account's standing.

## Best practices
<a name="isv-best-practices"></a>

Follow these best practices to effectively manage tenant reputation in Amazon SES:
+ **Start with the Standard policy** – For most tenants, the Standard reputation policy provides a good balance between protection and operational stability.
+ **Monitor before enforcing** – When onboarding new tenants, consider temporarily using the "None" policy while monitoring their sending patterns (such as with EventBridge) before enabling automated enforcement.
+ **Set up EventBridge notifications** – Create alerts for reputation findings to take proactive action before automated pausing occurs.
+ **Review tenant metrics regularly** – Monitor tenant-level sending statistics even in the absence of reputation findings to identify emerging patterns. 
+ **Educate your tenants** – Provide guidelines on [Email best practices](best-practices.md) to help tenants maintain good sending reputation.
+ **Apply appropriate policies** – Apply the Strict policy to high-risk tenants or those with a history of reputation issues.
+ **React quickly to findings** – When a finding is detected, investigate the root cause immediately and take appropriate corrective action.
+ **Resource planning** – Design your tenant structure to match your business needs. Tenants can represent multiple customers (ISVs), business units, client/application types, and regulatory requirements.

## Tenant-level suppression lists
<a name="tenant-suppression-list-overview"></a>

By default, all tenants in your account share the account-level suppression list. This means that when a recipient bounces or complains about one tenant's email, that address is suppressed for every tenant in the account. Tenant-level suppression lists solve this by giving each tenant its own isolated suppression list.

When you enable tenant-level suppression for a tenant, SES maintains a separate suppression list for that tenant. Bounces and complaints only affect the tenant that sent the email. Other tenants can continue sending to the same recipients. You configure tenant-level suppression by setting the `SuppressionScope` to `TENANT` and choosing which `SuppressedReasons` (bounces, complaints, or both) to track.

For complete information about configuring and managing tenant-level suppression lists, see [Using tenant-level suppression lists in Amazon SES](sending-email-suppression-list-tenant-level.md).

## Limitations
<a name="limitations"></a>

When using tenant management, be aware of these limitations:
+ **Regional scope** – Tenants are region-specific and are not automatically replicated across AWS Regions. If you send email from multiple regions, you'll need to configure and monitor tenant reputation separately in each region.
+ **Quota limits** – By default, accounts can create up to 10,000 tenants. You can request increases through the AWS Service Quota Console, with automatic approval available up to 300,000 tenants for qualifying accounts.
+ **Configuration set requirement** – When sending on behalf of a tenant, you must specify a configuration set that is associated with that tenant, or use an identity that has a default configuration set associated with the tenant.
+ **Metric calculation periods** – Reputation metrics are calculated based on recent sending activity, typically over a rolling 24-hour to 7-day period depending on the metric type.
+ **Minimum sending volume** – Some reputation findings require a minimum representative volume of emails before they can be triggered.
+ **Re-enabling grace period** – After re-enabling a paused tenant, they enter into a 'reinstated' state where active reputation findings are temporarily ignored to allow the tenant to recover. The tenant will remain in this state until all active findings are resolved.
+ **Cross-account limitations** – Tenants cannot span multiple AWS accounts. Each account manages its own set of tenants independently.
+ **No tenant nesting** – Tenants cannot contain other tenants - they are flat structures.

## Pricing
<a name="pricing"></a>

There's an additional charge per tenant per month based on the number of emails. For detailed pricing information, see the [SES pricing page](https://aws.amazon.com/ses/pricing/).

When using CloudWatch with tenant metrics, the standard CloudWatch metrics for each tenant are provided at no additional cost as part of the basic monitoring. Additional CloudWatch features like custom dashboards, alarms, or detailed monitoring may incur standard CloudWatch charges.