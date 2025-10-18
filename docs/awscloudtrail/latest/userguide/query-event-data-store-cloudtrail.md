# Create an event data store for CloudTrail
 events with the console

Event data stores for CloudTrail events can include CloudTrail management events, data events, and
 network activity events. You can keep the event data in an event data store for up to 3,653 days (about 10 years) if you choose the **One-year extendable retention pricing** option, 
 or up to 2,557 days (about 7 years) if you choose the **Seven-year retention pricing** option..

CloudTrail Lake event data stores incur charges. When you create an event data store, you choose the [pricing option](cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want
 to use for the event data store. The pricing option determines the cost for ingesting and storing events, and 
 the default and maximum retention period for the event data store. For information 
 about CloudTrail pricing and managing Lake costs, see
 [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") and [Managing CloudTrail Lake costs](cloudtrail-lake-manage-costs.md "cloudtrail-lake-manage-costs.md").


## To create an event
 data store for CloudTrail events


Use this procedure to create an event data store that logs CloudTrail management events, data events, or network activity events. 


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


###### Note

If you are copying trail events to this event data store, CloudTrail will
 not copy an event if its `eventTime` is older than
 the specified retention period. To determine the appropriate retention period, take the sum of the oldest event you want to copy in days and the number of days you
 want to retain the events in the event data store (**retention period** =
 `oldest-event-in-days` +
 `number-days-to-retain`). For example, if the oldest event you're copying is 45 days old
 and you want to keep the events in the event data store for a
 further 45 days, you would set the retention period to 90
 days.
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
11. Choose **Next** to configure the event data store.
12. On the **Choose events** page, choose **AWS 
 events**, and then choose **CloudTrail
 events**.
13. For **CloudTrail events**, choose at least one event type. By
 default, **Management events** is selected. You can add
 [management events](logging-management-events-with-cloudtrail.md "logging-management-events-with-cloudtrail.md"), [data events](logging-data-events-with-cloudtrail.md "logging-data-events-with-cloudtrail.md"), 
 and [network activity events](logging-network-events-with-cloudtrail.md "logging-network-events-with-cloudtrail.md") to your event data store.
14. (Optional) Choose **Copy trail events** if you want to
 copy events from an existing trail to run queries on past events. To copy
 trail events to an organization event data store, you must use the
 management account for the organization. The delegated administrator account
 cannot copy trail events to an organization event data store. For more
 information about considerations for copying trail events, see [Considerations for copying trail events](cloudtrail-copy-trail-to-lake-eds.md#cloudtrail-trail-copy-considerations-lake "cloudtrail-copy-trail-to-lake-eds.md#cloudtrail-trail-copy-considerations-lake").
15. To have your event data store collect events from all accounts in an
 AWS Organizations organization, select **Enable for all accounts in my
 organization**. You must be signed in to the management account
 or delegated administrator account for the organization to create an event
 data store that collects events for an organization.


###### Note

To copy trail events or enable Insights events, you must be signed in to the management account for your organization.
16. Expand **Additional settings** to choose whether you
 want your event data store to collect events for all AWS Regions, or
 only the current AWS Region, and choose whether the event data store
 ingests events. By default, your event data store collects events from
 all Regions in your account and starts ingesting events when it's
 created. 


	1. Select **Include only the current region in my event data
	 store** to include only events that are logged in
	 the current Region. If you do not choose this option, your event
	 data store includes events from all Regions.
	2. Deselect **Ingest events** if you do not want the event data store to start ingesting events. For example, you may want to deselect **Ingest events**, 
	 if you are copying trail events and do not want the event data store to include any future events. By default, the event data store starts ingesting events 
	 when it's created.
17. If your event data store includes management events, you can choose from
 the following options. For more information about management events, see [Logging management events](logging-management-events-with-cloudtrail.md "logging-management-events-with-cloudtrail.md").


	1. Choose between **Simple event collection** 
	 or **Advanced event collection**:
	
	
	
	
		* Choose **Simple event collection** if you want to log all events, log only read events, or log only write events. 
		 You can choose also to exclude AWS Key Management Service and Amazon RDS Data API events.
		* Choose **Advanced event collection** if you want to include or exclude management events based on the values of advanced event selector fields, including the `eventName`, 
		 `eventType`, `eventSource`, `sessionCredentialFromConsole`, and `userIdentity.arn` fields.
	2. If you selected **Simple event collection**, 
	 choose whether you want to log all events, log only read events, or log only write events. 
	 You can also choose to exclude AWS KMS and Amazon RDS Data API events.
	3. If you selected **Advanced event collection**, make the following selections:
	
	
		1. In **Log selector template**, choose a predefined template, or **Custom** to
		 build a custom configuration based on advanced event selector field values.
		
		
		You can choose from the following predefined
		 templates:
		
		
		
		
			* **Log all events** –
			 Choose this template to log all events.
			* **Log only read events** –
			 Choose this template to log only read events.
			 Read-only events are events that do not change the
			 state of a resource, such as `Get*` or `Describe*`
			 events.
			* **Log only write events** – Choose this template to log only write events. 
			 Write events add, change, or delete resources, attributes, or artifacts, 
			 such as `Put*`, `Delete*`, or `Write*` events.
			* **Log only AWS Management Console events** – 
			 Choose this template to log only events originating from the AWS Management Console.
			* **Exclude AWS service initiated events** – Choose this template to exclude 
			 AWS service events, which have an `eventType` of `AwsServiceEvent`, 
			 and events initiated with AWS service-linked roles (SLRs).
		2. (Optional) In **Selector name**, enter a name to identify your selector. The selector name is a 
		 descriptive name for an advanced event selector, such as "Log management events from AWS Management Console sessions". The selector name is listed as `Name` in the 
		 advanced event selector and is viewable if you expand the 
		 **JSON view**.
		3. If you chose **Custom**, in **Advanced event selectors** build an expression based on advanced event selector 
		 field values.
		
		
		###### Note
		
		Selectors don't support the use of wildcards like `*` . To match multiple values with a single condition, 
		 you may use `StartsWith`, `EndsWith`, `NotStartsWith`, or `NotEndsWith` to explicitly match the beginning or end of the event field.
		
		
			1. Choose from the following fields.
			
			
			
			
				* **`readOnly`** – `readOnly` can
				 be set to **equals** a value of `true` or
				 `false`. When it is set to `false`, the event data store logs
				 Write-only management events. Read-only management events are events that do not change the
				 state of a resource, such as `Get*` or `Describe*` events.
				 Write events add, change, or delete resources, attributes, or artifacts, such as
				 `Put*`, `Delete*`, or `Write*` events. To log
				 both **Read** and **Write** events, don't add a
				 `readOnly` selector.
				* **`eventName`** – `eventName`
				 can use any operator. You can use it to include or exclude any management event, such as `CreateAccessPoint` or 
				 `GetAccessPoint`.
				* **`userIdentity.arn`** – Include or exclude events for actions taken by specific IAM identities. For more information, see [CloudTrail userIdentity element](cloudtrail-event-reference-user-identity.md "cloudtrail-event-reference-user-identity.md").
				* **`sessionCredentialFromConsole`** – Include or exclude events originating from an AWS Management Console session. This field can be set to **equals** or **not equals** with a value of
				 `true`.
				* **`eventSource`** – 
				 You can use it to include or exclude specific event sources. The `eventSource` is typically a short form of the service name 
				 without spaces plus `.amazonaws.com`. For example, you could set `eventSource` **equals** to 
				 `ec2.amazonaws.com` to log only Amazon EC2 management events.
				* **`eventType`** – The [eventType](cloudtrail-event-reference-record-contents.md#ct-event-type "cloudtrail-event-reference-record-contents.md#ct-event-type") to include or exclude. For example, you can set this field to
				 **not equals** `AwsServiceEvent` to exclude [AWS service events](non-api-aws-service-events.md "non-api-aws-service-events.md").
			2. For each field, choose **+ Condition** to
			 add as many conditions as you need, up to a maximum of 500
			 specified values for all conditions.
			
			
			For information about how CloudTrail evaluates multiple conditions, see 
			 [How CloudTrail evaluates multiple conditions for a field](filtering-data-events.md#filtering-data-events-conditions "filtering-data-events.md#filtering-data-events-conditions").
			
			
			###### Note
			
			You can have a maximum of 500 values for all selectors on
			 an event data store. This includes arrays of multiple values for a
			 selector such as `eventName`. If you have single
			 values for all selectors, you can have a maximum of 500
			 conditions added to a selector.
			3. Choose **+ Field** to add additional fields
			 as required. To avoid errors, do not set conflicting or
			 duplicate values for fields.
		4. Optionally, expand **JSON view** to see your
		 advanced event selectors as a JSON block.
	4. Choose **Enable Insights events capture** to enable Insights. To enable Insights, you need to set up a [destination event data store](query-event-data-store-insights.md#query-event-data-store-insights-procedure "query-event-data-store-insights.md#query-event-data-store-insights-procedure") 
	 to collect Insights events based upon the management event activity in this event data store.
	
	
	If you choose to enable Insights, do the following.
	
	
		1. Choose the destination event store that will log Insights events. The destination event data store will collect Insights events 
		 based upon the management event activity in this event data store. For information about how to 
		 create the destination event data store, see [To create a destination event data store that logs Insights events](query-event-data-store-insights.md#query-event-data-store-insights-procedure "query-event-data-store-insights.md#query-event-data-store-insights-procedure").
		2. Choose the Insights types. You can choose
		 **API call rate**, **API error rate**,
		 or both. You must be logging **Write** management events to
		 log Insights events for **API call rate**. You must be logging 
		 **Read** or **Write** management events to 
		 log Insights events for **API error rate**.
18. To include data events in your event data store, do the following.


	1. Choose a resource type. This is the AWS service and resource
	 on which data events are logged.
	2. In **Log selector template**, choose a predefined template, or choose **Custom** to
	 define your own event collection conditions based on the values of advanced event selector fields.
	
	
	You can choose from the following predefined
	 templates:
	
	
	
	
		* **Log all events** –
		 Choose this template to log all events.
		* **Log only read events** –
		 Choose this template to log only read events.
		 Read-only events are events that do not change the
		 state of a resource, such as `Get*` or `Describe*`
		 events.
		* **Log only write events** – Choose this template to log only write events. 
		 Write events add, change, or delete resources, attributes, or artifacts, 
		 such as `Put*`, `Delete*`, or `Write*` events.
		* **Log only AWS Management Console events** – 
		 Choose this template to log only events originating from the AWS Management Console.
		* **Exclude AWS service initiated events** – Choose this template to exclude 
		 AWS service events, which have an `eventType` of `AwsServiceEvent`, 
		 and events initiated with AWS service-linked roles (SLRs).
	3. (Optional) In **Selector name**, enter a name to identify your selector. The selector name is a 
	 descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets". The selector name is listed as `Name` in the 
	 advanced event selector and is viewable if you expand the 
	 **JSON view**.
	4. If you selected **Custom**, in **Advanced event selectors** build an expression based on the values of advanced event selector fields.
	
	
	###### Note
	
	Selectors don't support the use of wildcards like `*` . To match multiple values with a single condition, 
	 you may use `StartsWith`, `EndsWith`, `NotStartsWith`, or `NotEndsWith` to explicitly match the beginning or end of the event field.
	
	
		1. Choose from the following fields.
		
		
		
		
			* **`readOnly`**
			 - `readOnly` can be set to
			 **equals** a value of
			 `true` or `false`. Read-only
			 data events are events that do not change the state of a
			 resource, such as `Get*` or
			 `Describe*` events. Write events add,
			 change, or delete resources, attributes, or artifacts,
			 such as `Put*`, `Delete*`, or
			 `Write*` events. To log both
			 `read` and `write` events,
			 don't add a `readOnly` selector.
			* **`eventName`** -
			 `eventName` can use any operator. You can
			 use it to include or exclude any data event logged to
			 CloudTrail, such as `PutBucket`,
			 `GetItem`, or
			 `GetSnapshotBlock`.
			* **`eventSource`** – The event source to include or exclude. This field can use any operator.
			* **eventType** – The event type to include or exclude. For example, you can set this field to
			 **not equals** `AwsServiceEvent` to exclude 
			 [AWS service events](non-api-aws-service-events.md "non-api-aws-service-events.md"). For a list of event types, 
			 see [eventType](cloudtrail-event-reference-record-contents.md#ct-event-type "cloudtrail-event-reference-record-contents.md#ct-event-type") in 
			 [CloudTrail record contents for management, data, and network activity events](cloudtrail-event-reference-record-contents.md "cloudtrail-event-reference-record-contents.md").
			* **sessionCredentialFromConsole** – Include or exclude events originating from an AWS Management Console session. This field can be set to **equals** or **not equals** with a value of
			 `true`.
			* **userIdentity.arn** – Include or exclude events for actions taken by specific IAM identities. For more information, see [CloudTrail userIdentity element](cloudtrail-event-reference-user-identity.md "cloudtrail-event-reference-user-identity.md").
			* **`resources.ARN`** - You can use
			 any operator with `resources.ARN`, but if you
			 use **equals** or
			 **does not equal**, the value must
			 exactly match the ARN of a valid resource of the type
			 you've specified in the template as the value of
			 `resources.type`.
			
			
			###### Note
			
			You can't use the `resources.ARN` field to filter resource types that do not have ARNs.
			
			
			For more information about the ARN formats of data event
			 resources, see [Actions, resources, and condition
			 keys for AWS services](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html "https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html") in the *Service Authorization Reference*.
		2. For each field, choose **+ Condition** to
		 add as many conditions as you need, up to a maximum of 500
		 specified values for all conditions. For example, to exclude
		 data events for two S3 buckets from data events that are logged
		 on your event data store, you can set the field to
		 **resources.ARN**, set the operator for
		 **does not start with**, and then paste in
		 an S3 bucket ARN for which you do
		 not want to log events.
		
		
		To add the second S3 bucket, choose **+
		 Condition**, and then repeat the preceding
		 instruction, pasting in the ARN for or browsing for a different
		 bucket.
		
		
		For information about how CloudTrail evaluates multiple conditions, see 
		 [How CloudTrail evaluates multiple conditions for a field](filtering-data-events.md#filtering-data-events-conditions "filtering-data-events.md#filtering-data-events-conditions").
		
		
		###### Note
		
		You can have a maximum of 500 values for all selectors on
		 an event data store. This includes arrays of multiple values for a
		 selector such as `eventName`. If you have single
		 values for all selectors, you can have a maximum of 500
		 conditions added to a selector.
		3. Choose **+ Field** to add additional fields
		 as required. To avoid errors, do not set conflicting or
		 duplicate values for fields. For example, do not specify an ARN
		 in one selector to be equal to a value, then specify that the
		 ARN not equal the same value in another selector.
	5. Optionally, expand **JSON view** to see your
	 advanced event selectors as a JSON block.
	6. To add another resource type on which to log data events, choose **Add data event type**. 
	 Repeat steps a through this step to configure advanced event selectors for the resource type.
19. To include network activity events in your event data store, do the following.


	1. From **Network activity event source**, choose the source for network activity events.
	2. In **Log selector template**, choose a template.
	 You can choose to log all network activity events, log all network activity access denied events, or choose **Custom** to
	 build a custom log selector to filter on multiple fields, such as `eventName` and `vpcEndpointId`.
	3. (Optional) Enter a name to identify the selector. The selector name is listed as **Name** in the advanced event selector and is viewable if you expand the 
	 **JSON view**.
	4. In **Advanced event
	 selectors** build expressions by choosing values for **Field**,
	 **Operator**, and **Value**. You can skip this step if you are using a predefined log template.
	
	
		1. For excluding or including network activity
		 events, you can choose from the following fields in the console.
		
		
		
		
			* **`eventName`** – You can use any operator with `eventName`. 
			 You can use it to include or exclude any event, such as `CreateKey`.
			* **`errorCode`** – You can use it to filter on an error code. Currently, the only supported `errorCode` is `VpceAccessDenied`.
			* **`vpcEndpointId`** – Identifies the VPC endpoint that the operation passed through. You can use 
			 any operator with `vpcEndpointId`.
		2. For each field, choose **+ Condition** to add as many conditions as you need, up to a maximum of 500 specified values for all conditions.
		3. Choose **+ Field** to add additional fields as required. To avoid errors, do not set conflicting or duplicate values for fields.
	5. To add another event source for which you want to log network activity events, choose **Add
	 network activity event selector**.
	6. Optionally, expand **JSON view** to see your
	 advanced event selectors as a JSON block.
20. To copy existing trail events to your event data store, do the
 following.


	1. Choose the trail that you want to copy. By default, CloudTrail only
	 copies CloudTrail events contained in the S3 bucket's
	 `CloudTrail` prefix and the prefixes inside the
	 `CloudTrail` prefix, and does not check prefixes for
	 other AWS services. If you want to copy CloudTrail events contained in
	 another prefix, choose **Enter S3 URI**, and then
	 choose **Browse S3** to browse to the prefix. If
	 the source S3 bucket for the trail uses a KMS key for data
	 encryption, ensure that the KMS key policy allows CloudTrail to decrypt
	 the data. If your source S3 bucket uses multiple KMS keys, you
	 must update each key's policy to allow CloudTrail to decrypt the data in
	 the bucket. For more information about updating the KMS key
	 policy, see [KMS key policy for decrypting data
	 in the source S3 bucket](cloudtrail-copy-trail-to-lake-eds.md#copy-trail-events-permissions-kms "cloudtrail-copy-trail-to-lake-eds.md#copy-trail-events-permissions-kms").
	2. Choose the time range for
	 copying the events. CloudTrail checks the prefix and log file name to verify the name contains a date between the chosen start and end date before attempting to copy trail events. You can choose a **Relative range** or an
	 **Absolute range**. To avoid duplicating events between the source trail and destination event data store, choose a time range that is earlier than the creation of the event data store.
	
	
	###### Note
	
	CloudTrail only copies trail events that have an `eventTime` within the event data store’s retention period. 
	 For example, if an event data store’s retention period is 90 days, then CloudTrail will not copy any trail events with an `eventTime` older than 90 days.
	
	
	
	
		* If you choose **Relative range**, you can
		 choose to copy events logged in the last 6 months, 1 year, 2 years, 7 years, or a custom range. CloudTrail copies the events logged within the chosen time period.
		* If you choose **Absolute range**, you can choose a specific start and end date. CloudTrail copies the events that occurred between the chosen 
		 start and end dates.
	3. For **Permissions**, choose from the following
	 IAM role options. If you choose an existing IAM role, verify
	 that the IAM role policy provides the necessary permissions. For
	 more information about updating the IAM role permissions, see
	 [IAM permissions
	 for copying trail events](cloudtrail-copy-trail-to-lake-eds.md#copy-trail-events-permissions-iam "cloudtrail-copy-trail-to-lake-eds.md#copy-trail-events-permissions-iam").
	
	
	
	
		* Choose **Create a new role
		 (recommended)** to create a new IAM role. For
		 **Enter IAM role name**, enter a name
		 for the role. CloudTrail automatically creates the necessary
		 permissions for this new role.
		* Choose **Use a custom IAM role ARN** to use
		 a custom IAM role that is not listed. For **Enter
		 IAM role ARN**, enter the IAM ARN.
		* Choose an existing IAM role from the drop-down list.
21. Choose **Next** to enrich your events by adding resource tag keys and IAM global condition keys.
22. In **Enrich events**, add up 
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
23. Choose **Expand event size** to expand the event payload up to 1 MB from 256 KB. This option is automatically enabled 
 when you add resource tag keys or IAM global condition keys to ensure all of your added keys are included in the event.


Expanding the event size is helpful for analyzing and troubleshooting events because it allows you to 
 see the full contents of the following fields as long as the event payload is less than 1 MB:




	* `annotation`
	* `requestID`
	* `additionalEventData`
	* `serviceEventDetails`
	* `userAgent`
	* `errorCode`
	* `responseElements`
	* `requestParameters`
	* `errorMessage`
For more information about these fields, see [CloudTrail record contents](cloudtrail-event-reference-record-contents.md "cloudtrail-event-reference-record-contents.md").
24. Choose **Next** to review your choices.
25. On the **Review and create** page, review your choices.
 Choose **Edit** to make changes to a section. When you're
 ready to create the event data store, choose **Create event data
 store**.
26. The new event data store is visible in the **Event data
 stores** table on the **Event data stores** page.


From this point forward, the event data store captures events that match
 its advanced event selectors (if you kept the **Ingest events** option selected). Events that occurred before you created the
 event data store are not in the event data store, unless you opted to copy
 existing trail events.

You can now run queries on your new event data store. The **Sample
 queries** tab provides example queries to get you started. For more
 information about creating and editing queries, see [Create or edit a query with the CloudTrail console](query-create-edit-query.md "query-create-edit-query.md").


You can also view the [managed dashboards](lake-dashboard-managed.md "lake-dashboard-managed.md"), or [create custom dashboards](lake-dashboard-custom.md "lake-dashboard-custom.md") to visualize event trends. For more information about Lake dashboards, 
 see [CloudTrail Lake dashboards](lake-dashboard.md "lake-dashboard.md").
