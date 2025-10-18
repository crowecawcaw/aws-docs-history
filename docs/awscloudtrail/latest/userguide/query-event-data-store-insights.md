# Create an event data store for Insights events with the console

AWS CloudTrail Insights help AWS users identify and respond to unusual activity associated with API call rates and API error rates by continuously analyzing CloudTrail management events. CloudTrail Insights analyze your normal patterns of API call rates and
 API error rates, also called the *baseline*, and generate Insights events
 when the call volume or error rates are outside normal patterns. Insights events on API call
 rate are generated for `write` management APIs, and Insights events on API error
 rate are generated for both `read` and `write` management
 APIs.

To log Insights events in CloudTrail Lake, you need a destination event
 data store that logs Insights events and a source event data store that enables Insights and logs management events.

###### Note

To log Insights events on the API call rate, the source event data store must log `write` management events. To log Insights events on the API error rate, the source event data store must log `read` or `write` management
 events. 

If you have CloudTrail Insights enabled on a source event data store and CloudTrail detects unusual activity, CloudTrail delivers Insights events to your destination event data store.
 Unlike other types of events captured in a CloudTrail event data store, Insights events are logged only when CloudTrail detects changes in your
 account's API usage that differ significantly from the account's typical usage
 patterns.

After you enable CloudTrail Insights for the first time on an event data store, CloudTrail may take up to 7 days to begin delivering Insights events, 
 provided that unusual activity is detected during that time.

CloudTrail Insights analyzes the management events that occur in each Region for the event data store and 
 generates an Insights events when unusual activity is detected that deviates from the baseline. 
 A CloudTrail Insights event is generated in the same Region as its supporting management event is generated.

For an organization event data store, CloudTrail Insights analyzes the management events from each member account 
 in the organization for each Region and generates an Insights event 
 when unusual activity is detected that deviates from the baseline for the account and the Region.

Additional charges apply for 
 ingesting Insights events in CloudTrail Lake. You will be charged separately if you enable Insights for both trails and CloudTrail Lake event data stores. For information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

###### Topics

* [To create a destination event data store that logs Insights events](#query-event-data-store-insights-procedure "#query-event-data-store-insights-procedure")
* [To create a source event data store that enables Insights events](#query-event-data-store-cloudtrail-insights "#query-event-data-store-cloudtrail-insights")

## To create a destination event data store that logs Insights events


When you create an Insights event data store, you have the option to choose an existing
 source event data store that logs management events and then specify the Insights types you
 want to receive. Or, you can alternatively enable Insights on a new or existing event data store after
 you create your Insights event data store and then choose this event data store as the destination event data store.


This procedure shows you how to create a destination event data store that logs Insights events.


1. Sign in to the AWS Management Console and open the CloudTrail console at
 [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. From the navigation pane, open the **Lake** submenu, then choose **Event data stores**.
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
6. Specify a retention period for the event data store in days. Retention periods can be between 7 days and 3,653 days (about 10 years) for the **One-year extendable retention pricing** option, 
or between 7 days and 2,557 days (about seven years) for the **Seven-year retention pricing** option. The event data store retains
 event data for the specified number of days.
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
 Insights events**.
13. In **CloudTrail Insights events**, do the following.


	1. Choose **Allow delegated administrator access** if you want to give your organization's delegated administrator access to this event data store. This option is only available if you are signed in with the 
	 management account for an AWS Organizations organization.
	2. (Optional) Choose an existing
	 source event data store that logs management events and specify the Insights types you
	 want to receive.
	
	
	To add a source event data store, do the following.
	
	
		1. Choose **Add source event data store**.
		2. Choose the source event data store.
		3. Choose the **Insights type** that you want to receive.
		
		
		
		
			* `ApiCallRateInsight` – The `ApiCallRateInsight` Insights type analyzes 
			 write-only management API calls that are aggregated per minute against a baseline API call volume. To receives Insights on `ApiCallRateInsight`, the source event data store must log **Write** management events.
			* `ApiErrorRateInsight` – The `ApiErrorRateInsight` Insights 
			 type analyzes management API calls that result in error codes. The error is shown if the API call is unsuccessful. To receive Insights on `ApiErrorRateInsight`, the source event data store must log **Write** or **Read** management events.
		4. Repeat the previous two steps (ii and iii) to add any additional
		 Insights types you want to receive.
14. Choose **Next** to review your choices.
15. On the **Review and create** page, review your choices.
 Choose **Edit** to make changes to a section. When you're
 ready to create the event data store, choose **Create event data
 store**.
16. The new event data store is visible in the **Event data
 stores** table on the **Event data stores** page.
17. If you did not choose a source event data store in step 10, follow the steps in 
 [To create a source event data store that enables Insights events](#query-event-data-store-cloudtrail-insights "#query-event-data-store-cloudtrail-insights") 
 to create a source event data store.

## To create a source event data store that enables Insights events


This procedure shows you how to create a source event data store that enables Insights events and logs management events.


1. Sign in to the AWS Management Console and open the CloudTrail console at
 [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. From the navigation pane, open the **Lake** submenu, then choose **Event data stores**.
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
11. Choose **Next** to configure the event data store.
12. On the **Choose events** page, choose **AWS 
 events**, and then choose **CloudTrail
 events**.
13. In **CloudTrail events**, leave **Management events** selected.
14. To have your event data store collect events from all accounts in an
 AWS Organizations organization, select **Enable for all accounts in my
 organization**. You must be signed in to the management account
 for the organization to create an event
 data store that enables Insights.
15. Expand **Additional settings** to choose whether you
 want your event data store to collect events for all AWS Regions, or
 only the current AWS Region, and choose whether the event data store
 ingests events. By default, your event data store collects events from
 all Regions in your account and starts ingesting events when it's
 created. 


	1. Choose **Include only the current region in my event data
	 store** if you want to include only events that are logged in
	 the current Region. If you do not choose this option, your event
	 data store includes events from all Regions.
	2. Leave **Ingest events** selected.
16. Choose between **Simple event collection** 
 or **Advanced event collection**:




	* Choose **Simple event collection** if you want to log all events, log only read events, or log only write events. 
	 You can choose also to exclude AWS Key Management Service and Amazon RDS Data API events.
	* Choose **Advanced event collection** if you want to include or exclude management events based on the values of advanced event selector fields, including the `eventName`, 
	 `eventType`, `eventSource`, `sessionCredentialFromConsole`, and `userIdentity.arn` fields.
17. If you selected **Simple event collection**, 
 choose whether you want to log all events, log only read events, or log only write events. 
 You can also choose to exclude AWS KMS and Amazon RDS Data API events.
18. If you selected **Advanced event collection**,
 make the following selections:


	1. In **Log selector template**, choose a predefined template, or choose **Custom** to
	 write your own event collection conditions based on the values of advanced event selector fields.
	
	
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
19. Choose **Enable Insights events capture**.
20. Choose the destination event store that will log Insights events. The destination event data store will collect Insights events 
 based upon the management event activity in this event data store. For information about how to 
 create the destination event data store, see [To create a destination event data store that logs Insights events](#query-event-data-store-insights-procedure "#query-event-data-store-insights-procedure").
21. Choose the Insights types. You can choose
 **API call rate**, **API error rate**,
 or both. You must be logging **Write** management events to
 log Insights events for **API call rate**. You must be logging 
 **Read** or **Write** management events to 
 log Insights events for **API error rate**.
22. Choose **Next** to enrich your events by adding resource tag keys and IAM global condition keys.
23. In **Enrich events**, add up 
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
24. Choose **Expand event size** to expand the event payload up to 1 MB from 256 KB. This option is automatically enabled 
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
25. Choose **Next** to review your choices.
26. On the **Review and create** page, review your choices.
 Choose **Edit** to make changes to a section. When you're
 ready to create the event data store, choose **Create event data
 store**.
27. The new event data store is visible in the **Event data
 stores** table on the **Event data stores** page.


From this point forward, the event data store captures events that match
 its advanced event selectors. After you enable CloudTrail Insights for the first time on your source event data store, 
 CloudTrail may take up to 7 days to begin delivering Insights events, 
 provided that unusual activity is detected during that time.


You can view the CloudTrail Lake dashboard to visualize the Insights events in your destination event data store. For more information about Lake dashboards, 
 see [CloudTrail Lake dashboards](lake-dashboard.md "lake-dashboard.md").

Additional charges apply for 
 ingesting Insights events in CloudTrail Lake. You will be charged separately if you enable Insights for both trails and event data stores. For information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").
