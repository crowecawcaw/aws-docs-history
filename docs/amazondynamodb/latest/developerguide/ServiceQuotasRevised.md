# Quotas and constraints for Amazon DynamoDB

This topic describes current quotas, formerly referred to as limits, within Amazon DynamoDB.
This topic also describes how you can perform the quota management tasks, for example,
viewing your current quotas and requesting a quota increase.

###### Topics

- [Performing quota management tasks in DynamoDB](#ServiceQuotasManagementTasks "#ServiceQuotasManagementTasks")
- [Requesting a quota increase in DynamoDB](RequestingQuotaIncrease.md "RequestingQuotaIncrease.md")
- [Quotas in Amazon DynamoDB](ServiceQuotas.md "ServiceQuotas.md")
- [Constraints in Amazon DynamoDB](Constraints.md "Constraints.md")

## Performing quota management tasks in DynamoDB

Amazon DynamoDB has several service components, such as tables, streams, indexes, and more.
When you create your AWS account, there are default _quotas_
(formerly referred to as limits) set on these components. Unless otherwise noted, each
quota is Region-specific. You can request increases for some of the quotas. After a
quota for a resource has been reached, additional requests to create that resource fail
with an exception.

### Accessing DynamoDB quotas

You can work with DynamoDB Service Quotas in the following ways:

- AWS Management Console

The [Service Quotas console](http://console.aws.amazon.com/servicequotas/home/services/dynamodb/quotas "http://console.aws.amazon.com/servicequotas/home/services/dynamodb/quotas") is a browser-based interface that you can use to
view and manage your Service Quotas. You can access Service Quotas from any AWS Management Console page by
choosing it on the top navigation bar, or by searching for Service Quotas in the
AWS Management Console.

- AWS Command Line Interface tools

When using AWS Command Line Interface tools, you can issue commands
at your system's command line to perform Service Quotas tasks. The command
line tools are useful if you want to build scripts that perform AWS tasks.

- AWS SDKs

You can use the AWS SDKs for various programming languages and platforms
(for example, Java, Python, Ruby, .NET, iOS and Android, and others) to
perform Service Quotas tasks.

If an adjustable quota isn't available in the Service Quotas console, use the
AWS Support Center Console to create a [Service Quotas increase case](https://support.console.aws.amazon.com/support/home#/case/create%3FissueType=service-limit-increase "https://support.console.aws.amazon.com/support/home#/case/create%3FissueType=service-limit-increase").

### Viewing current quotas in the console

###### To view your current DynamoDB quotas using the Service Quotas console

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home/services/dynamodb/quotas/](https://console.aws.amazon.com/servicequotas/home/services/dynamodb/quotas/ "https://console.aws.amazon.com/servicequotas/home/services/dynamodb/quotas/")
2. From the navigation bar, at the top of the screen, select a Region.
3. The console displays details about the DynamoDB **Quota
   name**, **Applied account-level quota value**, **AWS
   default quota value**, **Utilization**, and the
   **Adjustability** of the quota at the account-level or
   resource-level.

If the applied quota value or utilization is not available, the console
displays **Not available**. You can request your applied
quota value through the Support Center Console. 4. Choose a specific **Quota name** to view the **Details**
page, which displays that quota's **Description**,
**Quota code**, **Quota ARN**,
**Utilization**, **Applied account-level quota
value**, **Adjustability**, and **AWS default quota value**.

If applicable, the **Details** page also displays any **Monitoring** options, **Alarms**,**request history**, and any of the quota's
**Tags**.

### Viewing current quotas using the AWS CLI

###### To view the default values for DynamoDB quotas:

- Call the `ListDefaultServiceQuotas` operation with the DynamoDB service code (dynamodb)
  to retrieve default values for Amazon DynamoDB Service quotas.

```
$ aws service-quotas list-aws-default-service-quotas \
        --service-code dynamodb

 {
    "Quotas": [
        {
            "ServiceCode": "dynamodb",
            "ServiceName": "Amazon DynamoDB",
            "QuotaArn": "arn:aws:servicequotas:us-east-1::dynamodb/L-F7858A77",
            "QuotaCode": "L-F7858A77",
            "QuotaName": "Global Secondary Indexes per table",
            "Value": 20.0,
            "Unit": "None",
            "Adjustable": true,
            "GlobalQuota": false
        },
        {
            "ServiceCode": "dynamodb",
            "ServiceName": "Amazon DynamoDB",
            "QuotaArn": "arn:aws:servicequotas:us-east-1::dynamodb/L-AB614373",
            "QuotaCode": "L-AB614373",
            "QuotaName": "Table-level write throughput limit",
            "Value": 40000.0,
            "Unit": "None",
            "Adjustable": true,
            "GlobalQuota": false
        }......
    ]
}
```

###### To view the applied quota values:

- Call the [`ListServiceQuotas`](../../../servicequotas/2019-06-24/apireference/API_ListServiceQuotas.md "../../../servicequotas/2019-06-24/apireference/API_ListServiceQuotas.md") operation with the DynamoDB service code
  (dynamodb) to retrieve all applied quota values either at the account-level,
  resource-level, or all levels by passing `ACCOUNT`,
  `RESOURCE`, or `ALL` respectively as the value for
  the parameter `QuotaAppliedAtLevel`. The following CLI example
  retrieves quota values applied at the account-level.

```
$ aws service-quotas list-service-quotas \
        --service-code dynamodb \
        --quota-applied-at-level ACCOUNT


{
    "Quotas": [
        {
            "ServiceCode": "dynamodb",
            "ServiceName": "Amazon DynamoDB",
            "QuotaArn": "arn:aws:servicequotas:us-east-1:303935678045:dynamodb/L-F7858A77",
            "QuotaCode": "L-F7858A77",
            "QuotaName": "Global Secondary Indexes per table",
            "Value": 20.0,
{
    "Quotas": [
        {
            "ServiceCode": "dynamodb",
            "ServiceName": "Amazon DynamoDB",
            "QuotaArn": "arn:aws:servicequotas:us-east-1:303935678045:dynamodb/L
-F7858A77",
            "QuotaCode": "L-F7858A77",
            "QuotaName": "Global Secondary Indexes per table",
            "Value": 20.0,
            "Unit": "None",
            "Adjustable": true,
            "GlobalQuota": false,
            "QuotaAppliedAtLevel": "ACCOUNT"
        }.....

        }
    ]
}
```
