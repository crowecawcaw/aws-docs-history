# Update an event data store with the console

This section describes how to update an event data store's settings using the
 AWS Management Console. For information about how to update an event data store using the AWS CLI,
 see [Update an event data store with the AWS CLI](lake-cli-update-eds.md "lake-cli-update-eds.md").

###### To update an event data store

1. Sign in to the AWS Management Console and open the CloudTrail console at
 [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, under **Lake**, choose **Event data stores**.
3. Choose the event data store that you want to update. This action opens the
 event data store's details page.
4. In **General details**, choose **Edit**
 to change the following settings:




	* **Event data store name**
	 -
	 Change the name that identifies your event data store.
	* **[Pricing
	 option](cloudtrail-lake-concepts.md#eds-pricing-tier "cloudtrail-lake-concepts.md#eds-pricing-tier")**- For event data stores using
	 the **Seven-year retention pricing** option, you
	 can choose to use **One-year extendable retention pricing**
	 instead. We recommend one-year extendable retention pricing for
	 event data stores that ingest less than 25 TB of event data on a
	 monthly basis. We also recommend one-year extendable retention
	 pricing if you're seeking a flexible retention period of up to
	 10 years. For more information, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") and [Managing CloudTrail Lake costs](cloudtrail-lake-manage-costs.md "cloudtrail-lake-manage-costs.md").
	
	
	###### Note
	
	You can't change the pricing option for event data stores
	 that use **One-year extendable retention pricing**. If
	 you want to use
	 **Seven-year retention pricing**, [stop ingestion](query-eds-stop-ingestion.md "query-eds-stop-ingestion.md")
	 on your current event data store. Then create a new event
	 data store with the
	 **Seven-year retention pricing**
	 option.
	* **Retention period** - Change the retention period for the event data store. The retention period determines 
	 how long event data is kept in the event data store. Retention periods can be between 7 days and 3,653 days (about 10 years) for the **One-year extendable retention pricing** option, 
	or between 7 days and 2,557 days (about seven years) for the **Seven-year retention pricing** option.
	
	
	###### Note
	
	If you decrease the retention period of an event data store, CloudTrail will remove any events with 
	 an `eventTime` older than the new retention period. For example, if the previous retention period was 365 days and you decrease it to 100 days, 
	 CloudTrail will remove events with an `eventTime` older than 100 days.
	* **Encryption** - To encrypt your event data
	 store using your own KMS key, choose **Use my own
	 AWS KMS key**. By default, all events in an
	 event data store are encrypted by CloudTrail. Using your own KMS key
	 incurs AWS KMS costs for encryption and decryption.
	
	
	###### Note
	
	After you associate an event data store with a KMS key,
	 the KMS key can't be removed or changed.
	* To include only events that are logged in the current
	 AWS Region, choose **Include on the current region in
	 my event data store**. If you don't choose this
	 option, your event data store includes events from all
	 Regions.
	* To have your event data store collect events from all accounts in
	 an AWS Organizations organization, choose **Enable for all accounts
	 in my organization**. This option is only available if
	 you're signed in with the management account for your organization, and the **Event
	 type** for the event data store is **CloudTrail
	 events** or **Configuration items**.
Choose **Save changes** when you're finished.
5. In **Lake query federation**, choose
 **Edit** to enable or disable Lake query federation.
 [Enabling Lake query
 federation](query-enable-federation.md "query-enable-federation.md") lets you view the metadata for your event data store
 in the AWS Glue [Data
 Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro "https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro") and run SQL queries on the event data using Amazon Athena.
 [Disabling Lake query
 federation](query-disable-federation.md "query-disable-federation.md") disables the integration with AWS Glue, AWS Lake Formation, and Amazon Athena. 
 After disabling Lake query federation, you can no longer query your data in Athena. 
 No CloudTrail Lake data is deleted when you disable federation and you can continue to run queries in CloudTrail Lake.


To enable federation, do the following:


	1. Choose **Enable**.
	2. Choose whether to create a new IAM role, or use an existing role. When you create a new role, 
	 CloudTrail automatically creates a role with the required permissions. If you're using an existing role, be sure the role's policy provides the 
	 [required minimum permissions](query-federation.md#query-federation-permissions-role "query-federation.md#query-federation-permissions-role").
	3. If you're creating a new IAM role, enter a name for the role.
	4. If you're choosing an existing IAM role, choose the role you want to use. The role must exist in your account.Choose **Save changes** when you are finished.
6. In **Resource policy**, choose **Edit** to add or revise the resource-based policy for the event data store.


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
7. Edit any additional settings specific to your event data store's **Event type**.


**Settings for CloudTrail events**




	* To change which events your event data store
	 logs, choose **Edit** in
	 **CloudTrail events**.
	* In **Management events**,
	 choose **Edit** to change the
	 settings for management events. For more
	 information, see [Updating the management event settings for an existing event data store](logging-management-events-with-cloudtrail.md#logging-management-events-with-the-cloudtrail-console-eds "logging-management-events-with-cloudtrail.md#logging-management-events-with-the-cloudtrail-console-eds").
	* In **Data events**, choose
	 **Edit** to change the settings
	 for data events. You can choose which resource types 
	 you want to log and choose the log selector
	 template you want to use. For more information,
	 see [Updating an existing event data store to log
	 data events using the console](logging-data-events-with-cloudtrail.md#logging-data-events-with-the-cloudtrail-console-eds "logging-data-events-with-cloudtrail.md#logging-data-events-with-the-cloudtrail-console-eds").
	* In **Network activity
	 events**, choose
	 **Edit** to change the settings
	 for network activity events. You can choose which
	 network activity event type you want to log and
	 choose the log selector template you want to use.
	 For more information, see [Update an existing event data
	 store to log network activity events](logging-network-events-with-cloudtrail.md#log-network-events-lake-console "logging-network-events-with-cloudtrail.md#log-network-events-lake-console").
	* In **Enrich events, expand event size**, 
	 choose **Edit** to add or remove resource tags and IAM global condition keys, and expand the event size.
	
	
	In **Enrich events**, add up 
	 to 50 resource tag keys and 50 IAM global condition keys to provide additional 
	 metadata about your events. This helps you categorize and group related events.
	
	
	If you add resource tag keys, CloudTrail will include the selected tag keys associated with the resources that were involved in the API call. API events related to deleted resources will not have resource tags.
	
	
	If you add IAM global condition keys, 
	 CloudTrail will include information about the selected condition keys that were evaluated during the authorization process, 
	 including additional details about the principal, session, network, and the request itself.
	
	
	Information about the resource tag keys and IAM global condition keys is shown in the `eventContext` 
	 field of the event. For more information, see [Enrich CloudTrail events by adding resource tag
	 keys and IAM global condition keys](cloudtrail-context-events.md "cloudtrail-context-events.md").
	
	
	###### Note
	
	If an event contains a resource that doesn’t belong to the event Region, 
	 CloudTrail will not populate tags for this resource because tag retrieval is limited to the event Region.
	
	
	Choose **Expand event size** to expand the event payload up to 1 MB from 256 KB. This option is automatically enabled 
	 when you add resource tag keys or IAM global condition keys to ensure all of your added keys are included in the event.
	
	
	Expanding the event size is helpful for analyzing and troubleshooting events because it allows you to 
	 see the full contents of the following fields as long as the event payload is less than 1 MB:
	
	
	
	
		+ `annotation`
		+ `requestID`
		+ `additionalEventData`
		+ `serviceEventDetails`
		+ `userAgent`
		+ `errorCode`
		+ `responseElements`
		+ `requestParameters`
		+ `errorMessage`
	For more information about these fields, see [CloudTrail record contents](cloudtrail-event-reference-record-contents.md "cloudtrail-event-reference-record-contents.md").
	
	
	Choose **Save changes** when you're finished.
**Settings for Events from integration**


In **Integrations**, choose your
 integration. Then choose **Edit** to
 change the following settings:




	* In **Integration details**, change the name that identifies your integration's channel.
	* In **Event delivery location**, choose the destination for your events.
	* In **Resource policy**, configure the resource policy for the integration's channel.
Choose **Save changes** when you're
 finished.


For more information about these settings, see [Create an integration with a CloudTrail partner with the console](query-event-data-store-integration-partner.md "query-event-data-store-integration-partner.md").
8. To add, change, or remove tags, choose **Edit** in
 **Tags**. You can add up to 50 tag key pairs to help
 you identify, sort, and control access to your event data store. Choose
 **Save changes** when you're finished.
