# Copy trail events to a new event data store with the console

This walkthrough shows you how to copy trail events to a new CloudTrail Lake event data store for historical analysis. For more information about copying trail events, see [Copy trail events to an event data store](cloudtrail-copy-trail-to-lake-eds.md "cloudtrail-copy-trail-to-lake-eds.md").

###### To copy trail events to a new event data store

1. Sign in to the AWS Management Console and open the CloudTrail console at
 [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. From the navigation pane, under **Lake**, choose **Event data stores**.
3. Choose **Create event data store**.
4. On the **Configure event data store** page, in
 **General details**, give your event data store a name, such as
 `my-management-events-eds`. As a best practice, use a name that
 quickly identifies the purpose of the event data store. For information about CloudTrail naming requirements, see [Naming requirements for CloudTrail resources, S3 buckets, and KMS keys](cloudtrail-trail-naming-requirements.md "cloudtrail-trail-naming-requirements.md").
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

CloudTrail will not copy an event if its `eventTime` is older than
 the specified retention period.
 

To determine the appropriate retention period, take the sum of the oldest event you want to copy in days and the number of days you
 want to retain the events in the event data store (**retention period** =
 `oldest-event-in-days` +
 `number-days-to-retain`). For example, if the oldest event you're copying is 45 days old
 and you want to keep the events in the event data store for a
 further 45 days, you would set the retention period to 90
 days.
7. (Optional) In **Encryption**. choose whether you want to encrypt the event data store using your own KMS key.
 By default, all events in an event data store are encrypted by CloudTrail using a KMS key that AWS owns and manages for you.


To enable encryption using your own KMS key, choose **Use my
 own AWS KMS key**. Choose **New** to have
 an AWS KMS key created for you, or choose **Existing**
 to use an existing KMS key. In **Enter KMS alias**,
 specify an alias, in the format
 `alias/``MyAliasName`. Using your
 own KMS key requires that you edit your KMS key policy to allow CloudTrail
 logs to be encrypted and decrypted. For more information, see [Configure AWS KMS key policies for CloudTrail](create-kms-key-policy-for-cloudtrail.md "create-kms-key-policy-for-cloudtrail.md"). CloudTrail also
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
10. (Optional) In **Tags**, add one or more custom tags (key-value pairs) to your event data store. Tags can help you identify your CloudTrail event data stores. For example, you could attach a tag with the name 
 `stage` and the value `prod`. You can use tags to limit access 
 to your event data store. You can also use tags to track the query and ingestion costs for your event data store.


For information about how to use tags to track costs, see [Creating user-defined cost
 allocation tags for CloudTrail Lake event data stores](cloudtrail-budgets-tools.md#cloudtrail-lake-manage-costs-tags "cloudtrail-budgets-tools.md#cloudtrail-lake-manage-costs-tags"). For information about how to use IAM policies to
 authorize access to an event data store based on tags, see [Examples: Denying
 access to create or delete event data stores based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-eds-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-eds-tags"). For
 information about how you can use tags in AWS, see [Tagging
 your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html "https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html") in the
 *Tagging AWS Resources User Guide*.
11. Choose **Next** to configure the event data store.
12. On the **Choose events** page, leave the default selections for **Event type**.



![Choose event type for the event data store](images/lake-event-type.png)
13. For **CloudTrail events**, we'll leave **Management events** selected and choose **Copy trail events**. In this example, we're not concerned about the event types because we are only using the event data store to analyze past events and are not ingesting future events.
 


If you're creating an event 
 data store to replace an existing trail, choose the same event selectors as your trail to ensure the event data store has the same event coverage.



![Choose CloudTrail events types for your event data store](images/cloudtrail-events-copy-trail.png)
14. Choose **Enable for all accounts in my organization** if this is an organization event data store. This option won't be available to change unless you have accounts configured in AWS Organizations.


###### Note

If you are creating an organization event data store, you must be signed in with the management account for the organization because only the management account can copy trail events to an organization event data store.
15. For **Additional settings**, we'll deselect **Ingest events**, because in this example we don't want the event data store to ingest any future events as we're only interested in 
 querying the copied events. By default, an event data store 
 collects events for all AWS Regions and starts ingesting events when it's created.
16. For **Management
 events**, we'll leave the default settings.
17. In the **Copy trail events** area, complete the following steps.


	1. Choose the trail that you want to copy. In this example, we'll choose a trail named `management-events`.
	
	
	By default, CloudTrail only
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
	2. Choose a time range for copying the events. CloudTrail checks the prefix and log file name to
	 verify the name contains a date between the chosen start and end
	 date before attempting to copy trail events. You can choose a
	 **Relative range** or an **Absolute
	 range**. To avoid duplicating events between the source
	 trail and destination event data store, choose a time range that is
	 earlier than the creation of the event data store.
	
	
	
	
		* If you choose **Relative range**, you can
		 choose to copy events logged in the last 6 months, 1 year, 2 years, 7 years, or a custom range. CloudTrail copies the
		 events logged within the chosen time period.
		* If you choose **Absolute range**, you can
		 choose a specific start and end date. CloudTrail copies the events
		 that occurred between the chosen start and end dates.
	In this example, we'll choose **Absolute range** and we'll select the
	 entire month of May.
	
	
	
	![Choose absolute range for event data store](images/absolute-range-example.png)
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
	In this example, we'll choose **Create a new role
	 (recommended)** and will provide the name `copy-trail-events`.
![Choose options for copying CloudTrail events](images/copy-trail-events.png)
18. Choose **Next** to review your choices.
19. On the **Review and create** page, review your choices.
 Choose **Edit** to make changes to a section. When you're
 ready to create the event data store, choose **Create event data
 store**.
20. The new event data store is visible in the **Event data
 stores** table on the **Event data stores** page.



![View event data stores](images/event-data-stores-table.png)
21. Choose the event data store name to view its details page. The details page shows the details for your event data store and the status of the copy. 
 The event copy status is shown in the **Event copy status** area.


When a trail event copy completes, its **Copy status** is set to either
 **Completed** if there were no errors, or **Failed** if
 errors occurred.



![View the event copy status on the details page](images/event-copy-status.png)
22. To view more details about the copy, choose the copy name in the **Event log S3 location** column, or choose the **View details** option from the **Actions** menu. 
 For more information about viewing the details of a trail event copy, see [View event copy details with the CloudTrail console](copy-trail-details.md "copy-trail-details.md").



![View event copy details](images/copy-details.png)
23. The **Copy failures** area shows any errors that occurred when copying trail events. If the **Copy status** is **Failed**, fix any errors shown in **Copy failures**, and then choose **Retry copy**. 
 When you retry a copy, CloudTrail resumes the copy at the location where the failure occurred.
