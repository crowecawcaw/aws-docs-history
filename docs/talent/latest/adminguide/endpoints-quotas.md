

# Service quotas and endpoints for Amazon Connect Talent
<a name="endpoints-quotas"></a>

The following sections describe the service quotas and the service endpoints for Amazon Connect Talent.

**Topics**
+ [Service quotas](#talent-quotas)
+ [Service endpoints](#talent-endpoints)

## Service quotas
<a name="talent-quotas"></a>

Amazon Connect Talent creates Amazon Connect resources and related AWS resources in your AWS account. These resources count against the same service quotas as your Amazon Connect resources, so Amazon Connect Talent and Amazon Connect share these quotas. Most quotas apply per account per Region. Some apply per Amazon Connect instance or per domain.

Review these quotas in the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home) before you create Amazon Connect Talent instances or invite candidates at volume, and request increases for the adjustable ones in advance. For how to request an increase, see [Request a quota increase](#talent-quotas-request).

The service names in the tables below (for example, **Amazon Connect**, **Amazon Connect Cases**) are the names you select in the Service Quotas console. In the **Adjustable** column:
+ **Yes (account level)** — the new value applies to every instance in the account and Region.
+ **Yes (resource level)** — the new value applies to one instance, which you choose when you make the request.
+ **No** — you can't increase the quota.

### Quotas that limit how many instances you can create
<a name="talent-quotas-instance-count"></a>

Each Amazon Connect Talent instance creates the account-level resources below. With default quotas, you can create **2** instances per Region. If you raise the Amazon Connect instance count quota, the next limit is **5 per Region**, because the Amazon Q in Connect assistant quota and the Amazon Connect Cases domain quota both default to 5.

The assistant quota is shared across Amazon Connect Talent and Amazon Connect, so active assistants created by either count toward it. If your account already has assistants, you can create fewer Amazon Connect Talent instances. If you reach either quota, instance creation fails with a generic error that doesn't name the quota, so count your existing assistants and Cases domains before you create an instance.


| Service | Resource | Service Quotas name | Default | Used per instance | Adjustable | Quota code | 
| --- | --- | --- | --- | --- | --- | --- | 
| Amazon Connect | Amazon Connect instances | Amazon Connect instance count | 2 | 1 | Yes (account level) | L-AA17A6B9 | 
| Amazon Q in Connect | Amazon Q in Connect assistants | Connect AI agent - assistant count | 5 | 1 | No (contact your account team) | L-5558F50C | 
| Amazon Connect Cases | Amazon Connect Cases domains | Domains | 5 | 1 | Yes (account level) | L-C2B81BC3 | 
| Amazon Connect Customer Profiles | Customer Profiles domains | Amazon Connect Customer Profiles domain count | 100 | 1 | Yes (account level) | L-6603B252 | 
| Amazon Lex | Amazon Lex V2 bots | Bots per account (V2) | 100 | 3 | Yes (account level) | L-36FA8BD2 | 
| AWS Identity and Access Management (IAM) | IAM roles (global) | Roles per account | 1,000 | 1 (API) or 3 (console) | Yes (account level) | L-FE177D64 | 
| Amazon Simple Storage Service (Amazon S3) | Amazon S3 general purpose buckets (global) | General purpose buckets | 10,000 | Up to 2 | Yes (account level) | L-DC2B2D3D | 
| — | Instance creations and deletions | Not in Service Quotas | 100 per rolling 30 days | 1 per create, 1 per delete | No | — | 

### Quotas per instance
<a name="talent-quotas-per-instance"></a>

Amazon Connect Talent uses part of each quota below when it creates an instance. The rest is available for your own configuration.


| Service | Resource | Service Quotas name | Default | Used at creation | Adjustable | Quota code | 
| --- | --- | --- | --- | --- | --- | --- | 
| Amazon Connect | Users | Users per instance | 500 | 1 | Yes (resource level) | L-9A46857E | 
| Amazon Connect | Security profiles | Security profiles per instance | 100 | 7 | Yes (resource level) | L-F325A715 | 
| Amazon Connect | Flows | Contact flows per instance | 100 | 4 | Yes (resource level) | L-22922690 | 
| Amazon Connect | Workspaces | Workspaces per instance | 20 | 2 | Yes (resource level) | L-6402A996 | 
| Amazon Connect | Queues | Queues per instance | 100 | 2 | Yes (resource level) | L-19A87C94 | 
| Amazon Connect | Routing profiles | Routing profiles per instance | 500 | 1 | Yes (resource level) | L-D3E7BE26 | 
| Amazon Connect | Hours of operation | Hours of operation per instance | 100 | 1 | Yes (resource level) | L-20CD02F7 | 
| Amazon Connect | Email addresses | Email addresses per instance | 100 | 1 | Yes (resource level) | L-F4C86B27 | 
| Amazon Connect | Amazon Lex bots | Amazon Lex bots per instance | 70 | 3 | Yes (resource level) | L-B93A6612 | 
| Amazon Connect | Amazon Lex V2 bot aliases | Amazon Lex V2 bot aliases per instance | 100 | 3 | Yes (resource level) | L-CCEA7427 | 
| Amazon Connect | AI agent assistant associations | Connect AI agent assistant integration associations per instance | 1 | 1 | No | L-FFE16A0F | 
| Amazon Connect | Cases domain associations | Cases domain integration associations per instance | 1 | 1 | No | L-0AA82C05 | 
| Amazon Connect Customer Profiles | Customer Profiles object types | Object types per domain | 100 | 1 | Yes (account level) | L-14092FF4 | 
| Amazon Connect Customer Profiles | Customer Profiles integrations | Maximum number of integrations | 50 | 1 | Yes (account level) | L-4A5ECB8E | 
| Amazon Connect Cases | Cases fields | Fields per domain | 500 | 4 | Yes (account level) | L-C5B69356 | 
| Amazon Connect Cases | Cases templates | Templates per domain | 100 | 1 | Yes (account level) | L-0482161A | 
| Amazon Connect Cases | Cases layouts | Layouts per domain | 100 | 1 | Yes (account level) | L-D0ED993F | 

Your instance's AI agent assistant association and Cases domain association are both used by Amazon Connect Talent. Neither is adjustable, so you can't attach a different assistant or Cases domain to an Amazon Connect Talent instance.

### Quotas that limit interview volume
<a name="talent-quotas-interview-volume"></a>

**Important**  
The AI-led interview requires these quotas to meet the values in the table below at minimum. If an applied value in the Service Quotas console is lower, the AI-led interview will not work. Before you send evaluations, check your applied values and request an increase for any that do not meet the minimum requirements. See [Request a quota increase](#talent-quotas-request).

For each quota, check your applied account-level quota value in the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). It must match or exceed the value shown in the table below. If it is lower, request a quota increase to the value shown.

Rate quotas apply per account per Region. All instances in the same account and Region share one allowance.


| Service | Quota | Default | What uses it | Adjustable | Quota code | 
| --- | --- | --- | --- | --- | --- | 
| Amazon Connect | Concurrent active calls per instance | 10 | 1 per voice interview, held for the full interview | Yes (resource level) | L-12AB7C57 | 
| Amazon Connect | Rate of StartWebRTCContact API requests | 2 per second | 1 each time a candidate starts or restarts a voice interview | Yes (account level) | L-5CFC10A5 | 
| Amazon Connect | Concurrent active chats per instance | 500 | 1 per assessment session | Yes (resource level) | L-D4BA6F6E | 
| Amazon Connect | Rate of StartChatContact API requests | 5 per second | 1 or more each time a candidate starts an assessment | Yes (account level) | L-AA48CD49 | 
| Amazon Connect | Rate of DescribeWorkspace API requests | 2 per second | 1 per invitation sent, and 1 each time a candidate opens an invitation link | Yes (account level) | L-9962AF53 | 
| Amazon Connect | Rate of ListWorkspaceMedia API requests | 2 per second | 1 each time a candidate opens an invitation link | Yes (account level) | L-E09C4A84 | 
| Amazon Connect | Rate of DescribeInstance API requests | 1 per second | 1 each time a recruiter loads Amazon Connect Talent | Yes (account level) | L-D14CF86E | 
| Amazon Simple Email Service (Amazon SES) | Sending quota | 200 per 24 hours in the sandbox | 1 per candidate invitation | Yes — first move out of the sandbox | L-804C8AE8 | 
| Amazon Simple Email Service (Amazon SES) | Sending rate | 1 per second in the sandbox | 1 per candidate invitation | Yes — first move out of the sandbox | L-CDEF9B6B | 

#### Monitor usage
<a name="talent-quotas-monitor"></a>
+ **Concurrent calls and chats:** In Amazon CloudWatch, the `AWS/Connect` namespace publishes `ConcurrentCalls`, `ConcurrentCallsPercentage`, and `CallsBreachingConcurrencyQuota`, plus `ConcurrentActiveChats` and `ConcurrentActiveChatsPercentage`, per instance. `ConcurrentCallsPercentage` displays as a decimal — 0.8 means 80%.
+ **API rate quotas and Amazon SES quotas:** The Service Quotas console shows usage. You can create a CloudWatch alarm from each quota's page.
+ **Resource-count quotas** (assistants, domains, bots, security profiles): Service Quotas doesn't track usage for these. Check the count in each service's console.

### Request a quota increase
<a name="talent-quotas-request"></a>

Amazon Connect Talent uses the standard Amazon Connect quota process. Amazon Connect quotas are listed under **Amazon Connect** in the Service Quotas console. Cases, Customer Profiles, Amazon Lex, and Amazon SES quotas are listed under their own services — the **Service** column in each table tells you which.

Key points:
+ Create your instance before you request an increase to a per-instance quota. A resource-level request applies to the one instance you select.
+ An account-level increase applies to all instances in that account and Region. You can't raise a resource-level quota at the account level.
+ Quotas apply per AWS Region. Request each increase in every Region where you run Amazon Connect Talent.
+ Smaller increases can be approved within hours; larger ones can take up to 3 weeks, so plan ahead of launch.
+ The defaults on this page are for new accounts. Check your account's **Applied quota value** before you plan — an older account can have different values.

**To request an increase**

1. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home) in the Region of your instance.

1. In the navigation pane, choose **AWS services**.

1. Choose the service shown in the **Service** column (for example, **Amazon Connect**).

1. Find the quota by its **Service Quotas name**, then:
   + **Account-level quota:** select the quota and choose **Request increase at account-level**.
   + **Resource-level quota:** choose the quota name, select your instance under **Resource-level quotas**, and choose **Request increase at resource-level**.

1. For **Increase quota value**, enter the new value, then choose **Request**.

To track a request, open the **Request history** tab on the service's page, or choose **Dashboard** in the navigation pane. After the request is resolved, the quota's **Applied quota value** shows the new value.

For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide* and [Amazon Connect service quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html).

## Service endpoints
<a name="talent-endpoints"></a>

A service endpoint is the URL of the entry point for an AWS service. Amazon Connect Talent is available in specific AWS Regions, and you connect to the endpoint for the Region where your instance is hosted. For more information about the Regions where Amazon Connect Talent is available, see [Supported Regions and endpoints](what-is-talent.md#talent-regions-endpoints).