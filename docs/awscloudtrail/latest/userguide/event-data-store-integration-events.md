# Create an event data store for events outside of AWS with the console

You can create an event data store to include events outside of AWS, and then use
CloudTrail Lake to search, query, and analyze the data that is logged from your applications.

You can use CloudTrail Lake _integrations_ to log and store user activity
data from outside of AWS; from any source in your hybrid environments, such as in-house or
SaaS applications hosted on-premises or in the cloud, virtual machines, or containers.

When you create an event data store for an integration, you also create a channel,
and attach a resource policy to the channel.

CloudTrail Lake event data stores incur charges. When you create an event data store, you choose the [pricing option](cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want
to use for the event data store. The pricing option determines the cost for ingesting and storing events, and
the default and maximum retention period for the event data store. For information
about CloudTrail pricing and managing Lake costs, see
[AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") and [Managing CloudTrail Lake costs](cloudtrail-lake-manage-costs.md "cloudtrail-lake-manage-costs.md").

## To create an event

data store for events outside of AWS

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. From the navigation pane, under **Lake**, choose **Event data stores**.
3. Choose **Create event data store**.
4. On the **Configure event data store** page, in
   **General details**, enter a name for the event data
   store. A name is required.
5. Choose the **Pricing option** that you want to use for your event data store. The pricing option determines the cost for ingesting and storing events, and the
   default and maximum retention periods for your event data store. For more information, see
   [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") and [Managing CloudTrail Lake costs](cloudtrail-lake-manage-costs.md "cloudtrail-lake-manage-costs.md").

The following are the available options:

    * **One-year extendable retention pricing** - Generally recommended if you expect to ingest less than 25 TB of event data per month and want a flexible retention period of up to
     10 years. For the first 366 days (the default retention period), storage is
     included at no additional charge with ingestion pricing. After 366 days, extended retention is available at pay-as-you-go pricing. This is the default option.




    	+ **Default retention period:** 366 days
    	+ **Maximum retention period:** 3,653 days
    * **Seven-year retention pricing** - Recommended if you expect to ingest more than 25 TB of event data per month and need a retention period of up to 7 years. Retention is included with ingestion
     pricing at no additional charge.




    	+ **Default retention period:** 2,557 days
    	+ **Maximum retention period:** 2,557 days

6. Specify a retention period for the event data store. Retention periods can be between 7 days and 3,653 days (about 10 years) for the **One-year extendable retention pricing** option,
   or between 7 days and 2,557 days (about seven years) for the **Seven-year retention pricing** option.

CloudTrail Lake determines whether to retain an event by checking if the `eventTime`
of the event is within the specified retention period. For example, if you specify a retention period
of 90 days, CloudTrail will remove events when their `eventTime` is
older than 90 days. 7. (Optional) To enable encryption using AWS Key Management Service, choose **Use my
own AWS KMS key**. Choose **New** to have
an AWS KMS key created for you, or choose **Existing**
to use an existing KMS key. In **Enter KMS alias**,
specify an alias, in the format
`alias/``MyAliasName`. Using your
own KMS key requires that you edit your KMS key policy to
allow your event data store to be encrypted and decrypted. For more information, see [Configure AWS KMS key policies for CloudTrail](create-kms-key-policy-for-cloudtrail.md "create-kms-key-policy-for-cloudtrail.md"). CloudTrail also
supports AWS KMS multi-Region keys. For more information about multi-Region
keys, see [Using
multi-Region keys](../../../kms/latest/developerguide/multi-region-keys-overview.md "../../../kms/latest/developerguide/multi-region-keys-overview.md") in the _AWS Key Management Service Developer
Guide_.

Using your own KMS key incurs AWS KMS costs for encryption and decryption.
After you associate an event data store with a KMS key, the KMS key
cannot be removed or changed.

###### Note

To enable AWS Key Management Service encryption for an organization event data store,
you must use an existing KMS key for the management account. 8. (Optional) If you want to query against your event data using Amazon Athena, choose **Enable** in **Lake query federation**.
Federation lets you view the metadata associated with the event data store in the AWS Glue
[Data Catalog](../../../glue/latest/dg/components-overview.md#data-catalog-intro "../../../glue/latest/dg/components-overview.md#data-catalog-intro") and run SQL queries against the event data in Athena. The table metadata stored in the AWS Glue Data Catalog
lets the Athena query engine know how to find, read, and process the data that you want to query. For more information, see
[Federate an event data store](query-federation.md "query-federation.md").

To enable Lake query federation, choose **Enable** and then do the following:

    1. Choose whether you want to create a new role or use an existing IAM role. [AWS Lake Formation](../../../lake-formation/latest/dg/how-it-works.md "../../../lake-formation/latest/dg/how-it-works.md")
     uses this role to manage permissions for the federated event data store. When you create a new role using the CloudTrail console, CloudTrail automatically creates a role with the required permissions.
     If you choose an existing role, be sure the policy for the role provides the
     [required minimum permissions](query-federation.md#query-federation-permissions-role "query-federation.md#query-federation-permissions-role").
    2. If you are creating a new role, enter a name to identify the role.
    3. If you are using an existing role, choose the role you want to use. The role must exist in your account.

9. (Optional) Choose **Enable resource policy** to add a resource-based policy to your event data store.
   Resource-based policies allow you to control which principals can perform actions on your event data store.
   For example, you can add a resource based policy that allows the root users in other accounts to query this event data store and view the query results. For example policies, see
   [Resource-based policy examples for event data stores](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds").

A resource-based policy includes one or more statements. Each statement in
the policy defines the [principals](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") that are allowed or denied access
to the event data store and the actions the principals can perform
on the event data store resource.

The following actions are supported in resource-based policies for event data stores:

    * `cloudtrail:StartQuery`
    * `cloudtrail:CancelQuery`
    * `cloudtrail:ListQueries`
    * `cloudtrail:DescribeQuery`
    * `cloudtrail:GetQueryResults`
    * `cloudtrail:GenerateQuery`
    * `cloudtrail:GenerateQueryResultsSummary`
    * `cloudtrail:GetEventDataStore`

For [organization event data stores](cloudtrail-lake-organizations.md "cloudtrail-lake-organizations.md"), CloudTrail creates a [default resource-based policy](cloudtrail-lake-organizations.md#cloudtrail-lake-organizations-eds-rbp "cloudtrail-lake-organizations.md#cloudtrail-lake-organizations-eds-rbp") that
lists the actions that the delegated administrator accounts are allowed to perform on organization event data stores. The permissions in this policy are derived from the delegated
administrator permissions in AWS Organizations. This policy is updated automatically following changes to the organization event data store or to the organization
(for example, a CloudTrail delegated administrator account is registered or removed). 10. (Optional) In the **Tags** section, you can add up to 50
tag key pairs to help you identify, sort, and control access to your event
data store. For more information about how to use IAM policies to
authorize access to an event data store based on tags, see [Examples: Denying
access to create or delete event data stores based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-eds-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-eds-tags"). For
more information about how you can use tags in AWS, see [Tagging
AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md") in the
_Tagging AWS Resources
User Guide_. 11. Choose **Next** to configure the event data store. 12. On the **Choose events** page, choose **Events from integrations**. 13. From **Events from integration**, choose the source to deliver events to the event data store. 14. Provide a name to identify the integration's channel. The name can be 3-128 characters. Only letters, numbers,
periods, underscores, and dashes are allowed. 15. In **Resource policy**, configure the resource policy for
the integration's channel. Resource policies are JSON policy documents that
specify what actions a specified principal can perform on the resource and
under what conditions. The accounts defined as principals in the resource
policy can call the `PutAuditEvents` API to deliver events to
your channel. The resource owner has implicit access to the
resource if their IAM policy allows the
`cloudtrail-data:PutAuditEvents` action.

The information required for the policy is determined by the integration
type. For a direction integration, CloudTrail automatically adds the partner's AWS account IDs,
and requires you to enter the unique external ID provided by the partner. For a solution integration, you
must specify at least one AWS account ID as principal, and can
optionally enter an external ID to prevent against confused deputy.

###### Note

If you do not create a resource policy for the channel, only the channel owner can call the `PutAuditEvents` API on the channel.

    1. For a direct integration, enter the external ID provided by your
     partner. The integration partner provides a unique external ID, such
     as an account ID or a randomly generated string, to use for the
     integration to prevent against confused deputy. The partner is
     responsible for creating and providing a unique external ID.



     You can choose **How to find this?** to view the partner's documentation
     that describes how to find the external ID.




    ![Partner documentation for external ID](images/integration-external-id.png)

    ###### Note

    If the resource policy includes an external ID, all calls to the
     `PutAuditEvents` API must include the external ID. However,
     if the policy does not define an external ID, the
     partner can still call the `PutAuditEvents`
     API and specify an `externalId` parameter.
    2. For a solution integration, choose **Add AWS
     account** to specify each AWS account ID to add as a
     principal in the policy.

16. Choose **Next** to review your choices.
17. On the **Review and create** page, review your choices.
    Choose **Edit** to make changes to a section. When you're
    ready to create the event data store, choose **Create event data
    store**.
18. The new event data store is visible in the **Event data
    stores** table on the **Event data stores** page.
19. Provide the channel Amazon Resource Name (ARN) to the partner application. Instructions for providing the channel ARN
    to the partner application are found on the partner documentation website.
    For more information, choose the **Learn more**
    link for the partner on the **Available sources** tab of the **Integrations** page to open the partner's page in
    AWS Marketplace.

The event data store starts
ingesting partner events into CloudTrail through the integration's channel when you, the partner, or the partner applications calls the `PutAuditEvents` API on the channel.
