# Create an event data store for
 configuration items with the console

You can create an event data store to include [AWS Config configuration items](https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html#config-items "https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html#config-items"), and use
 the event data store to investigate non-compliant changes to your production
 environments. With an event data store, you can relate non-compliant rules to the users
 and resources associated with the changes. A configuration item represents a
 point-in-time view of the attributes of a supported AWS resource that exists in your
 account. AWS Config creates a configuration item whenever it detects a change to a resource
 type that it is recording. AWS Config also creates configuration items when a configuration
 snapshot is captured.

You can use both AWS Config and CloudTrail Lake to run queries against your configuration items.
 You can use AWS Config to query the current configuration state of AWS resources based on
 configuration properties for a single AWS account and AWS Region, or across multiple
 accounts and Regions. In contrast, you can use CloudTrail Lake to query across diverse data
 sources such as CloudTrail events, configuration items, and rule evaluations. CloudTrail Lake
 queries cover all AWS Config configuration items including resource configuration and
 compliance history.

Creating an event data store for configuration items doesn't impact existing AWS Config
 advanced queries, or any configured AWS Config aggregators. You can continue to run advanced
 queries using AWS Config, and AWS Config continues to deliver history files to your S3
 buckets.

CloudTrail Lake event data stores incur charges. When you create an event data store, you choose the [pricing option](cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want
 to use for the event data store. The pricing option determines the cost for ingesting and storing events, and 
 the default and maximum retention period for the event data store. For information 
 about CloudTrail pricing and managing Lake costs, see
 [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") and [Managing CloudTrail Lake costs](cloudtrail-lake-manage-costs.md "cloudtrail-lake-manage-costs.md").


## Limitations


The following limitations apply to event data stores for configuration
 items.



* No support for custom configuration items
* No support for event filtering using advanced event selectors

## Prerequisites


Before you create your event data store, set up AWS Config recording for all your
 accounts and Regions. You can use [Quick
 Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-config.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-config.html"), a capability of AWS Systems Manager, to quickly create a configuration
 recorder powered by AWS Config. 


###### Note

You are charged service usage fees when AWS Config starts recording configurations.
 For more information about pricing, see [AWS Config
 Pricing](https://aws.amazon.com/config/pricing/ "https://aws.amazon.com/config/pricing/"). For information about managing the configuration recorder,
 see [Managing the
 Configuration Recorder](https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder.html "https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder.html") in the *AWS Config Developer
 Guide*.


Additionally, the following actions are recommended, but are not required to
 create an event data store.



* Set up an Amazon S3 bucket to receive a configuration snapshot on request and
 configuration history. For more information about snapshots, see [Managing
 the Delivery Channel](https://docs.aws.amazon.com/config/latest/developerguide/manage-delivery-channel.html "https://docs.aws.amazon.com/config/latest/developerguide/manage-delivery-channel.html") and [Delivering
 Configuration Snapshot to an Amazon S3 Bucket](https://docs.aws.amazon.com/config/latest/developerguide/deliver-snapshot-cli.html "https://docs.aws.amazon.com/config/latest/developerguide/deliver-snapshot-cli.html") in the
 *AWS Config Developer Guide*.
* Specify the rules that you want AWS Config to use to evaluate compliance
 information for the recorded resource types. Several of the CloudTrail Lake sample
 queries for AWS Config require AWS Config Rules to evaluate the compliance state of your
 AWS resources. For more information about AWS Config Rules, see [Evaluating
 Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html "https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html") in the *AWS Config Developer
 Guide*.

## To create an event data store for
 configuration items


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
 older than 90 days.
7. (Optional) To enable encryption using AWS Key Management Service, choose **Use my
 own AWS KMS key**. Choose **New** to have
 an AWS KMS key created for you, or choose **Existing**
 to use an existing KMS key. In **Enter KMS alias**,
 specify an alias, in the format
 `alias/``MyAliasName`. Using your
 own KMS key requires that you edit your KMS key policy to 
 allow your event data store to be encrypted and decrypted. For more information, see [Configure AWS KMS key policies for CloudTrail](create-kms-key-policy-for-cloudtrail.md "create-kms-key-policy-for-cloudtrail.md"). CloudTrail also
 supports AWS KMS multi-Region keys. For more information about multi-Region
 keys, see [Using
 multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html "https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html") in the *AWS Key Management Service Developer
 Guide*.


Using your own KMS key incurs AWS KMS costs for encryption and decryption.
 After you associate an event data store with a KMS key, the KMS key
 cannot be removed or changed.


###### Note

To enable AWS Key Management Service encryption for an organization event data store,
 you must use an existing KMS key for the management account.
8. (Optional) If you want to query against your event data using Amazon Athena, choose **Enable** in **Lake query federation**.
 Federation lets you view the metadata associated with the event data store in the AWS Glue 
 [Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro "https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro") and run SQL queries against the event data in Athena. The table metadata stored in the AWS Glue Data Catalog 
 lets the Athena query engine know how to find, read, and process the data that you want to query. For more information, see 
 [Federate an event data store](query-federation.md "query-federation.md").


To enable Lake query federation, choose **Enable** and then do the following:


	1. Choose whether you want to create a new role or use an existing IAM role. [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/how-it-works.html "https://docs.aws.amazon.com/lake-formation/latest/dg/how-it-works.html") 
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
 the policy defines the [principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html") that are allowed or denied access
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
 (for example, a CloudTrail delegated administrator account is registered or removed).
10. (Optional) In the **Tags** section, you can add up to 50
 tag key pairs to help you identify, sort, and control access to your event
 data store. For more information about how to use IAM policies to
 authorize access to an event data store based on tags, see [Examples: Denying
 access to create or delete event data stores based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-eds-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-eds-tags"). For
 more information about how you can use tags in AWS, see [Tagging
 AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html "https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html") in the
 *Tagging AWS Resources
 User Guide*.
11. Choose **Next**.
12. On the **Choose events** page, choose **AWS events**, and then choose
 **Configuration items**.
13. CloudTrail stores the event data store resource in the Region in which you
 create it, but by default, the configuration items collected in the data
 store are from all Regions in your account that have recording enabled.
 Optionally, you can select **Include only the current region in my
 event data store** to include only configuration items that are
 captured in the current Region. If you do not choose this option, your event
 data store includes configuration items from all Regions that have recording
 enabled.
14. To have your event data store collect configuration items from all
 accounts in an AWS Organizations organization, select **Enable for all
 accounts in my organization**. You must be signed in to the
 management account or delegated administrator account for the organization
 to create an event data store that collects configuration items for an
 organization.
15. Choose **Next** to review your choices.
16. On the **Review and create** page, review your choices.
 Choose **Edit** to make changes to a section. When you're
 ready to create the event data store, choose **Create event data
 store**.
17. The new event data store is visible in the **Event data
 stores** table on the **Event data stores** page.


From this point forward, the event data store captures configuration
 items. Configuration items that occurred before you created the event data
 store are not in the event data store.

## Configuration item
 schema


The following table describes the required and optional schema elements that match
 those in configuration item records. The contents of `eventData` are
 provided by your configuration items; other fields are provided by CloudTrail after
 ingestion.


CloudTrail event record contents are described in more detail in [CloudTrail record contents for management, data, and network activity events](cloudtrail-event-reference-record-contents.md "cloudtrail-event-reference-record-contents.md").



* [Fields that are provided by CloudTrail after
 ingestion](#fields-cloudtrail-event "#fields-cloudtrail-event")
* [Fields that are provided by your
 events](#fields-config "#fields-config")




Fields that are provided by CloudTrail after ingestion| Field name | Input type | Requirement | Description |
| --- | --- | --- | --- |
| eventVersion | string | Required | The version of the AWS event format. |
| eventCategory | string | Required | The event category. For configuration items, the valid value is `ConfigurationItem`. |
| eventType | string | Required | The event type. For configuration items, the valid value is `AwsConfigurationItem`. |
| eventID | string | Required | A unique ID for an event. |
| eventTime | string | Required | The event timestamp, in `yyyy-MM-DDTHH:mm:ss` format, in Universal Coordinated Time (UTC). |
| awsRegion | string | Required | The AWS Region to which to assign an event. |
| recipientAccountId | string | Required | Represents the AWS account ID that received this event. |
| addendum | addendum | Optional | Shows information about why an event was delayed. If information was missing from an existing event, the addendum block includes the missing information and a reason for why it was missing. | Fields in `eventData` are provided by your configuration items| Field name | Input type | Requirement | Description |
| --- | --- | --- | --- |
| eventData | - | Required | Fields in eventData are provided by your configuration items. |
| <br>• configurationItemVersion | string | Optional | The version of the configuration item from its source. |
| <br>• configurationItemCaptureTime | string | Optional | The time when the configuration recording was initiated. |
| <br>• configurationItemStatus | string | Optional | The configuration item status. Valid values are `OK`, `ResourceDiscovered`, `ResourceNotRecorded`, `ResourceDeleted`, and `ResourceDeletedNotRecorded`. |
| <br>• accountId | string | Optional | The 12-digit AWS account ID associated with the resource. |
| <br>• resourceType | string | Optional | The type of AWS resource. For more information about valid resource types, see [ConfigurationItem](https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationItem.html "https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationItem.html") in the *AWS Config API Reference*. |
| <br>• resourceId | string | Optional | The ID of the resource (for example., sg-`xxxxxx`). |
| <br>• resourceName | string | Optional | The custom name of the resource, if available. |
| <br>• arn | string | Optional | Amazon Resource Name (ARN) associated with the resource. |
| <br>• awsRegion | string | Optional | The AWS Region where the resource resides. |
| <br>• availabilityZone | string | Optional | The Availability Zone associated with the resource. |
| <br>• resourceCreationTime | string | Optional | The time stamp when the resource was created. |
| <br>• configuration | JSON | Optional | The description of the resource configuration. |
| <br>• supplementaryConfiguration | JSON | Optional | Configuration attributes that AWS Config returns for certain resource types to supplement the information returned for the configuration parameter. |
| <br>• relatedEvents | string | Optional | A list of CloudTrail event IDs. |
| <br>• relationships | - | Optional | A list of related AWS resources. |
| <br>• + name | string | Optional | The type of relationship with the related resource. |
| <br>• + resourceType | string | Optional | The resource type of the related resource. |
| <br>• + resourceId | string | Optional | The ID of the related resource (for example, sg-`xxxxxx`). |
| <br>• + resourceName | string | Optional | The custom name of the related resource, if available. |
| <br>• tags | JSON | Optional | A mapping of key value tags associated with the resource. | The following example shows the hierarchy of schema elements that match those in configuration item records. ``` { "eventVersion": String, "eventCategory: String, "eventType": String, "eventID": String, "eventTime": String, "awsRegion": String, "recipientAccountId": String, "addendum": Addendum, "eventData": { "configurationItemVersion": String, "configurationItemCaptureTime": String, "configurationItemStatus": String, "configurationStateId": String, "accountId": String, "resourceType": String, "resourceId": String, "resourceName": String, "arn": String, "awsRegion": String, "availabilityZone": String, "resourceCreationTime": String, "configuration": { JSON, }, "supplementaryConfiguration": { JSON, }, "relatedEvents": [ String ], "relationships": [ struct{ "name" : String, "resourceType": String, "resourceId": String, "resourceName": String } ], "tags": { JSON } } } } ```
