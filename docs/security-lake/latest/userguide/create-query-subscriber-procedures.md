

# Creating a subscriber with query access in Security Lake
<a name="create-query-subscriber-procedures"></a>

Choose your preferred method to create a subscriber with query access in the current AWS Region. A subscriber can query data only from the AWS Region that it is created in. To create a subscriber, you'll need to have the AWS account ID and external ID of the subscriber. The external ID is a unique identifier that the subscriber provides to you. For more information about external IDs, see [How to use an external ID when granting access to your AWS resources to a third party](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html) in the *IAM User Guide*.

**Note**  
Security Lake does not support Lake Formation cross-account data sharing version 1. You must update Lake Formation cross-account data sharing to version 2 or version 3. For the steps to update **Cross account version settings** through the AWS Lake Formation console or the AWS CLI, see [To enable the new version](https://docs.aws.amazon.com/lake-formation/latest/dg/optimize-ram.html#version-update-steps) in the *AWS Lake Formation Developer Guide*.

------
#### [ Console ]

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/).

   Sign in to the delegated administrator account.

1. By using the AWS Region selector in the upper-right corner of the page, select the Region where you want to create the subscriber.

1. In the navigation pane, choose **Subscribers**.

1. On the **Subscribers** page, choose **Create subscriber**.

1. For **Subscriber details**, enter a **Subscriber name** and an optional **Description**.

   The **Region** is auto-populated as your currently selected AWS Region and can't be modified.

1. For **Log and event sources**, choose which sources you want Security Lake to include when returning query results.

1. For **Data access method**, choose **Lake Formation** to create query access for the subscriber.

1. For **Subscriber credentials**, provide the subscriber's AWS account ID and [external ID](https://docs.aws.amazon.com/security-lake/latest/userguide/prereqs-creating-subscriber.html#subscriber-external-id).

1. (Optional) For **Tags**, enter as many as 50 tags to assign to the subscriber.

   A *tag* is a label that you can define and assign to certain types of AWS resources. Each tag consists of a required tag key and an optional tag value. Tags can help you identify, categorize, and manage resources in different ways. To learn more, see [Tagging Security Lake resources](tagging-resources.md).

1. Choose **Create**.

------
#### [ API ]

To create a subscriber with query access programmatically, use the [CreateSubscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateSubscriber.html) operation of the Security Lake API. If you're using the AWS Command Line Interface (AWS CLI), run the [create-subscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-subscriber.html) command. 

In your request, use these parameters to specify the following settings for the subscriber:
+ For `accessTypes`, specify `LAKEFORMATION`.
+ For `sources`, specify each source that you want Security Lake to include when returning query results.
+ For `subscriberIdentity`, specify the AWS identity and external ID that the subscriber uses to query source data.

The following example creates a subscriber with query access in the current AWS Region for the specified subscriber identity. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\\) line-continuation character to improve readability.

```
$ aws securitylake create-subscriber \ 
--subscriber-identity {"accountID": {{129345678912}},"externalId": {{123456789012}}} \
--sources [{"awsLogSource": {"sourceName": {{VPC_FLOW,}} "sourceVersion": {{2.0}}}}] \
--subscriber-name {{subscriber name}} \
--access-types {{LAKEFORMATION}}
```

------

## Setting up cross-account table sharing (subscriber step)
<a name="grant-query-access-subscriber"></a>

Security Lake uses Lake Formation cross-account table sharing to support subscriber query access. When you create a subscriber with query access in the Security Lake console, API, or AWS CLI, Security Lake shares information about the relevant Lake Formation tables with the subscriber by creating a [resource share](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-terms-and-concepts.html#term-resource-share) in AWS Resource Access Manager (AWS RAM).

When you make certain types of edits to a subscriber with query access, Security Lake creates a new resource share. For more information, see [Editing a subscriber with query access in Security Lake](editing-query-access-subscriber.md).

The subscriber should follow these steps to consume data from your Lake Formation tables:

1. **Accept the resource share** – The subscriber must accept the resource share that has the `resourceShareArn` and `resourceShareName` that's generated when you create or edit the subscriber. Choose one of the following access methods:
   + For console and AWS CLI, see [Accepting a resource share invitation from AWS RAM](https://docs.aws.amazon.com/lake-formation/latest/dg/accepting-ram-invite.html).
   + For API, invoke the [GetResourceShareInvitations](https://docs.aws.amazon.com/ram/latest/APIReference/API_GetResourceShareInvitations.html) API. Filter by `resourceShareArn` and `resourceShareName` to find the correct resource share. Accept the invitation with the [AcceptResourceShareInvitation](https://docs.aws.amazon.com/ram/latest/APIReference/API_AcceptResourceShareInvitation.html) API.

   The resource share invitation expires in 12 hours, so you must validate and accept the invitation within 12 hours. If the invitation expires, you continue to see it in a `PENDING` state, but accepting it won't give you access to the shared resources. When more than 12 hours have passed, delete the Lake Formation subscriber and recreate the subscriber to get a new resource share invitation.

1. **Create a resource link to the shared database** – The subscriber must create a resource link to the shared Lake Formation database in either AWS Lake Formation (if using the console) or AWS Glue (if using API/AWS CLI). This resource link points the subscriber's account to the shared database. Choose one of the following access methods:
   + For console and AWS CLI, see [see Creating a resource link to a shared Data Catalog database.](https://docs.aws.amazon.com/lake-formation/latest/dg/create-resource-link-database.html) in the *AWS Lake Formation Developer Guide*.
   + We recommend that subscribers also create a unique database with the [CreateDatabase](https://docs.aws.amazon.com/glue/latest/webapi/API_CreateDatabase.html) API to store resource link tables.

1. **Query the shared tables** – Services like Amazon Athena can refer to the tables directly, and new data that Security Lake collects is automatically available to query. Queries run in the subscriber's AWS account, and costs incurred from queries are billed to the subscriber. You can control read access to resources in your own Security Lake account.

For more information about granting cross-account permissions, see [Cross-account data sharing in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-permissions.html) in the *AWS Lake Formation Developer Guide*.