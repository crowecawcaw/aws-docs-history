# Authorizing Aggregator Accounts to Collect

AWS Config Configuration and Compliance Data

_Authorization_ refers to the permissions you grant to an aggregator
account and region to collect your AWS Config configuration and compliance data. Authorization is
not required if you are aggregating source accounts that are part of AWS Organizations. You can use
the AWS Config console or the AWS CLI to authorize aggregator accounts.

###### Topics

- [Considerations](#aggregated-add-authorization-considerations "#aggregated-add-authorization-considerations")
- [Adding Authorization](#aggregated-add-authorization-procedure "#aggregated-add-authorization-procedure")

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

## Adding Authorization

Adding Authorization (Console)
You can add authorization to grant permission to aggregator accounts
and Regions to collect AWS Config configuration and compliance data.

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Navigate to the **Authorizations** page and
   choose **Add authorization**.
3. For **Aggregator account**, type the 12-digit
   account ID of an aggregator account.
4. For **Aggregator region**, choose the
   AWS Regions where the aggregator account is allowed to collect
   AWS Config configuration and compliance data.
5. Choose **Add authorization** to confirm your
   selection.

AWS Config displays an aggregator account, Region, and authorization
status.

###### Note

You can also add authorizations to aggregator accounts and
Regions programatically using CloudFormation sample templates. For more
information, see [AWS::Config::AggregationAuthorization](../../../AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.md") in the
_CloudFormation User Guide_.

Authorizing a Pending Request (Console)
If you have a pending authorization request from an existing
aggregator account you will see the request status on the
**Authorizations** page. You can authorize a
pending request from this page.

1. Choose the aggregator account that you want to authorize, and then
   choose **Authorize**.

A confirmation message is displayed to confirm that you want to
grant the aggregator account permission to collect AWS Config data from
this account. 2. Choose **Authorize** again to confirm that you
want to grant permission to the aggregator account.

The authorization status changes from **Requesting for
authorization** to
**Authorized**.

**Authorization approval period**

Authorization approval is required to add source accounts to an individual
account aggregator. A pending authorization approval request will be
available for 7 days after an individual account aggregator adds a source
account.

Adding Authorization (AWS CLI)

1. Open a command prompt or a terminal window.
2. Enter the following command:

```
aws configservice put-aggregation-authorization --authorized-account-id  `AccountID` --authorized-aws-region `Region`
```

3. You should see output similar to the following:

```

{
    "AggregationAuthorization": {
        "AuthorizedAccountId": "`AccountID`",
        "AggregationAuthorizationArn": "arn:aws:config:`Region`:`AccountID`:aggregation-authorization/`AccountID`/`Region`",
        "CreationTime": 1518116709.993,
        "AuthorizedAwsRegion": "`Region`"
    }
}

```
