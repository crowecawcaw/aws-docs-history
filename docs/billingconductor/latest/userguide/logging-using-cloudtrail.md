# Logging AWS Billing Conductor API calls using AWS CloudTrail

AWS Billing Conductor is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in AWS Billing Conductor. CloudTrail captures all API calls for
AWS Billing Conductor as events. The calls captured include calls from the AWS Billing Conductor console and
code calls to the AWS Billing Conductor API operations. If you create a trail, you can enable
continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS Billing Conductor. If
you don't configure a trail, you can still view the most recent events in the CloudTrail console
in **Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to AWS Billing Conductor, the IP address from which the request
was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## AWS Billing Conductor CloudTrail events

This section shows a full list of the CloudTrail events related to Billing and Cost Management.

| Event name                                     | Definition                                                                                       |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `AssociateAccounts`                            | Logs the association of accounts to a billing group.                                             |
| `AssociatePricingRules`                        | Logs the association of pricing rules to a pricing plan.                                         |
| `AutoAssociateAccount`                         | Logs the automatic association of an account to a billing group.                                 |
| `AutoDisassociateAccount`                      | Logs the automatic disassociation of an account from a billing group in the next billing period. |
| `BatchAssociateResourcesToCustomLineItem`      | Logs the batch association of resources to a percentage custom line item.                        |
| `BatchDisassociateResourcesFromCustomLineItem` | Logs the batch disassociation of resources from a percentage custom line item.                   |
| `CreateBillingGroup`                           | Logs the creation of a billing group.                                                            |
| `CreateCustomLineItem`                         | Logs the creation of a custom line item.                                                         |
| `CreatePricingPlan`                            | Logs the creation of a pricing plan.                                                             |
| `CreatePricingRule`                            | Logs the creation of a pricing rule.                                                             |
| `DeleteBillingGroup`                           | Logs the deletion of a billing group.                                                            |
| `DeleteCustomLineItem`                         | Logs the deletion of a custom line item.                                                         |
| `DeletePricingPlan`                            | Logs the deletion of a pricing plan.                                                             |
| `DeletePricingRule`                            | Logs the deletion of a pricing rule.                                                             |
| `DisassociateAccounts`                         | Logs the disassociation of accounts from a billing group.                                        |
| `DisassociatePricingRules`                     | Logs the disassociation of pricing rules from a pricing plan.                                    |
| `ListAccountAssociations`                      | Logs the access to the account ids in the billing group.                                         |
| `ListBillingGroupCostReports`                  | Logs the access to the actual AWS charges for the billing group.                                 |
| `ListBillingGroups`                            | Logs the access to the billing groups in a billing period.                                       |
| `ListCustomLineItems`                          | Logs the access to the custom line items in a billing period.                                    |
| `ListCustomLineItemVersions`                   | Logs the access to the versions of a custom line item.                                           |
| `ListPricingPlans`                             | Logs the access to the pricing plans in a billing period.                                        |
| `ListPricingPlansAssociatedWithPricingRule`    | Logs the access to the pricing plans associated to a pricing rule.                               |
| `ListPricingRules`                             | Logs the access to the pricing rules in a billing period.                                        |
| `ListPricingRulesAssociatedToPricingPlan`      | Logs the access to the pricing rules associated to a pricing plan.                               |
| `ListResourcesAssociatedToCustomLineItem`      | Logs the access to the resources associated to a custom line item.                               |
| `ListTagsForResource`                          | Logs the access to the tags on a resource.                                                       |
| `TagResource`                                  | Logs the association of tags on a resource.                                                      |
| `UpdateBillingGroup`                           | Logs the update of a billing group.                                                              |
| `UpdateCustomLineItem`                         | Logs the update of a custom line item.                                                           |
| `UpdatePricingPlan`                            | Logs the update of a pricing plan.                                                               |
| `UpdatePricingRule`                            | Logs the update of a pricing rule.                                                               |

## AWS Billing Conductor information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs
in AWS Billing Conductor, that activity is recorded in a CloudTrail event along with other AWS service events
in **Event history**. You can view, search, and download recent events in
your AWS account. For more information, see [Viewing events with CloudTrail Event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for AWS Billing Conductor,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket.
By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail
logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket
that you specify. Additionally, you can configure other AWS services to further analyze and act
upon the event data collected in CloudTrail logs. For more information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications
  for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log
  files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log
  files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All AWS Billing Conductor actions are logged by CloudTrail and are documented in the [AWS Billing Conductor API Reference](../APIReference.md "../APIReference.md").

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding AWS Billing Conductor log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

###### Topics

- [AutoAssociateAccount](#CT-example-auto "#CT-example-auto")
- [CreateBillingGroup](#CT-example-create "#CT-example-create")

### AutoAssociateAccount

The following example shows a CloudTrail log entry that demonstrates the `AutoAssociateAccount` action.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "accountId": "111122223333",
        "invokedBy": "billingconductor.amazonaws.com"
    },
    "eventTime": "2024-02-23T00:22:08Z",
    "eventSource": "billingconductor.amazonaws.com",
    "eventName": "AutoAssociateAccount",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "billingconductor.amazonaws.com",
    "userAgent": "billingconductor.amazonaws.com",
    "requestParameters": null,
    "responseElements": null,
    "requestID": "1v14d239-fe63-4d2b-b3cd-450905b6c33",
    "eventID": "14536982-geff-4fe8-bh18-f18jde35218d0",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "requestParameters": {
            "Arn": "arn:aws:billingconductor::111122223333:billinggroup/444455556666",
            "AccountIds": [
                "333333333333"
            ]
        },
        "responseElements": {
            "Arn": "arn:aws:billingconductor::111122223333:billinggroup/444455556666"
        }
    },
    "eventCategory": "Management"
}
```

### CreateBillingGroup

The following example shows a CloudTrail log entry that demonstrates the `CreateBillingGroup` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "accountId":"111122223333",
        "accessKeyId":"ASIAIOSFODNN7EXAMPLE"
    },
    "eventTime": "2024-01-24T20:30:03Z",
    "eventSource": "billingconductor.amazonaws.com",
    "eventName": "CreateBillingGroup",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.100.10.10",
    "userAgent": "aws-internal/3 aws-sdk-java/1.11.465 Linux/4.9.124-0.1.ac.198.73.329.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.192-b12 java/1.8.0_192",
    "requestParameters": {
        "PrimaryAccountId": "444455556666",
        "ComputationPreference": {
            "PricingPlanArn": "arn:aws:billingconductor::111122223333:pricingplan/TqeITi5Bgh"
        },
        "X-Amzn-Client-Token": "32aafb5s-e5b6-47f5-9795-3a69935e9da4",
        "AccountGrouping": {
            "LinkedAccountIds": [
                "444455556666",
                "111122223333"
            ]
        },
        "Name": "***"
    },
    "responseElements": {
        "Access-Control-Expose-Headers": "x-amzn-RequestId,x-amzn-ErrorType,x-amzn-ErrorMessage,Date",
        "Arn": "arn:aws:billingconductor::111122223333:billinggroup/444455556666"
    },
    "requestID": "fb26ae47-3510-a833-98fe-3dc0f602gb49",
    "eventID": "3ab70d86-c63e-46fd8d-a33s-ce2970441a8",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```
