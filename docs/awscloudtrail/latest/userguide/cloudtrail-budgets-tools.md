# Using AWS Budgets to manage costs

AWS Budgets a feature of AWS Billing and Cost Management, allows you to set custom budgets that alert you when
 your costs or usage exceed (or are forecasted to exceed) your budgeted amount.

Creating a budget for CloudTrail by using AWS Budgets is a
 recommended best practice, and can help you track your CloudTrail spending. Cost-based budgets
 help promote awareness of how much you might be billed for your CloudTrail use. [Budget alerts](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-best-practices.html#budgets-best-practices-alerts "https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-best-practices.html#budgets-best-practices-alerts") notify you when your bill reaches a
 threshold that you define. When you receive a budget alert, you can make changes before
 the end of the billing cycle to manage your costs.

###### Note

Though you can apply tags to CloudTrail trails, AWS Billing cannot currently use tags
 applied to trails for cost allocation. Cost Explorer can show costs for CloudTrail Lake event data
 stores and for the CloudTrail service as a whole.

To get started with AWS Budgets, open [AWS Billing and Cost Management](https://console.aws.amazon.com/billing "https://console.aws.amazon.com/billing"), and then choose
 **Budgets** in the left navigation bar. We recommend configuring
 budget alerts as you create a budget to track CloudTrail spending. For more information about
 how to use AWS Budgets, see [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html "https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html") and [Best practices for AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-best-practices.html "https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-best-practices.html").


## Creating user-defined cost
 allocation tags for CloudTrail Lake event data stores


You can create [user-defined cost
 allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html") to track the query and ingestion costs for your CloudTrail
 Lake event data stores. A *user-defined cost allocation tag* is a
 key-value pair that you can associate with an event data store. After you activate
 cost allocation tags, AWS uses the tags to organize your resource costs on your
 cost allocation report.



* To create tags in the console, see step 9 of the [To create an event
 data store for CloudTrail events](query-event-data-store-cloudtrail.md#query-event-data-store-cloudtrail-procedure "query-event-data-store-cloudtrail.md#query-event-data-store-cloudtrail-procedure")
 procedure.
* To create tags using the CloudTrail API, see [CreateEventDataStore](../APIReference/API_CreateEventDataStore.md "../APIReference/API_CreateEventDataStore.md") and [AddTags](../APIReference/API_AddTags.md "../APIReference/API_AddTags.md")
 in the *AWS CloudTrail API Reference*.
* To create tags using the AWS CLI, see [create-event-data-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-event-data-store.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-event-data-store.html") and [add-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/add-tags.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/add-tags.html") in the *AWS CLI Command Reference*.

For more information about activating tags, see [Activating
 user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html").
