

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Logging AWS Marketplace Discovery API calls with AWS CloudTrail
<a name="logging-discovery-api-calls-with-cloudtrail"></a>

The AWS Marketplace Discovery API is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures all Discovery API calls as events, including calls from the AWS SDK and the AWS CLI.

## Discovery API information in CloudTrail
<a name="discovery-cloudtrail-info"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in the Discovery API, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**.

All Discovery API actions are logged by CloudTrail. The following operations generate entries in CloudTrail log files:
+ `GetListing`
+ `GetProduct`
+ `GetOffer`
+ `GetOfferTerms`
+ `GetOfferSet`
+ `ListPurchaseOptions`
+ `ListFulfillmentOptions`
+ `SearchFacets`
+ `SearchListings`

The event source for Discovery API events is `discovery-marketplace.amazonaws.com`.

## Example Discovery API log entry
<a name="discovery-cloudtrail-example"></a>

The following example shows a CloudTrail log entry that demonstrates the `GetListing` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "{{EXAMPLE}}",
        "arn": "arn:aws:iam::{{123456789012}}:user/{{ExampleUser}}",
        "accountId": "{{123456789012}}",
        "accessKeyId": "{{EXAMPLE}}",
        "userName": "{{ExampleUser}}"
    },
    "eventTime": "2026-04-01T15:30:00Z",
    "eventSource": "discovery-marketplace.amazonaws.com",
    "eventName": "GetListing",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "{{203.0.113.50}}",
    "userAgent": "aws-sdk-python/1.34.0 Python/3.12.0",
    "requestParameters": {
        "listingId": "{{listing-saas-abc123}}"
    },
    "responseElements": null,
    "requestID": "{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}",
    "eventID": "{{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "{{123456789012}}",
    "eventCategory": "Management"
}
```