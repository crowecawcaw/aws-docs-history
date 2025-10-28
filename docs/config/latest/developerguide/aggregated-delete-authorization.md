# Deleting Authorization for Aggregator

Accounts to Collect AWS Config Configuration and Compliance Data

_Authorization_ refers to the permissions you grant to an aggregator
account and region to collect your AWS Config configuration and compliance data. Authorization is
not required if you are aggregating source accounts that are part of AWS Organizations. You can use
the AWS Config console or the AWS CLI to delete authorizations.

###### Topics

- [Considerations](#aggregated-delete-authorization-considerations "#aggregated-delete-authorization-considerations")
- [Deleting
  Authorization](#aaggregated-delete-authorization-procedure "#aaggregated-delete-authorization-procedure")

## Considerations

**There are two types of aggregators: Individual account aggregator and
Organization aggregator**

For an individual account aggregator, authorization is required for all source
accounts and Regions that you want to include, including both external accounts and
Regions and Organization member accounts and Regions.

For an organization aggregator, authorization is not required for Organization member
account regions since authorization is integrated with the AWS Organizations service.

**Aggregators do not automatically enable AWS Config on your
behalf**

AWS Config needs to be enabled in the source account and Region for either type of
aggregator, in order for AWS Config data to be generated in the source account and
Region.

## Deleting

Authorization

Deleting Authorization (Console)

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Choose the aggregator account that you want to delete
   authorization, and then choose **Delete**.

A warning message is displayed. When you delete this
authorization, AWS Config data will no longer be shared with the
aggregator account. 3. Choose **Delete** again to confirm your
selection.

The aggregator account is now deleted.

Deleting Authorization (AWS CLI)
Enter the following command:

```
aws configservice delete-aggregation-authorization --authorized-account-id  `AccountID` --authorized-aws-region `Region`
```

If successful, the command executes with no additional output.
