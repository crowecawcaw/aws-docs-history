

# Logging procurement system API calls with AWS CloudTrail
<a name="buyer-cloudtrail-logging"></a>

AWS Marketplace is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Marketplace. CloudTrail captures API calls for AWS Marketplace as events. The calls captured include calls from the AWS Marketplace console and code calls to the AWS Marketplace API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. For more information, see the [CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## Invoicing CloudTrail events
<a name="buyer-cloudtrail-invoicing-events"></a>

The following table shows the CloudTrail events for the invoicing actions used with procurement system integrations. These CloudTrail events use `invoicing.amazonaws.com` as the event source.


**Invoicing CloudTrail events**  

| Event name | Definition | 
| --- | --- | 
| CreateProcurementPortalPreference | Logs the creation of a procurement portal preference. | 
| GetProcurementPortalPreference | Logs the retrieval of a procurement portal preference. | 
| ListProcurementPortalPreferences | Logs the retrieval and listing of procurement portal preferences. | 

## AWS Marketplace information in AWS CloudTrail
<a name="buyer-cloudtrail-info"></a>

CloudTrail is enabled on your AWS account when you create the account. When supported event activity occurs in AWS Marketplace, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *CloudTrail User Guide*.

For an ongoing record of events in your AWS account, including events for AWS Marketplace, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail log files from multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html)
+ [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management user credentials.
+ Whether the request was made with temporary security credentials for a role or a federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html) in the *CloudTrail User Guide*.

## CloudTrail log entry examples
<a name="buyer-cloudtrail-log-entry-examples"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `CreateProcurementPortalPreference` action.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAEXAMPLEID:ExampleUser",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/ExampleUser",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAEXAMPLEID",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2026-03-16T15:44:15Z",
                "mfaAuthenticated": "false"
            }
        },
        "inScopeOf": {}
    },
    "eventTime": "2026-03-16T15:45:27Z",
    "eventSource": "invoicing.amazonaws.com",
    "eventName": "CreateProcurementPortalPreference",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.1",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:148.0) Gecko/20100101 Firefox/148.0",
    "requestParameters": {
        "ProcurementPortalName": "COUPA",
        "BuyerDomain": "NetworkID",
        "BuyerIdentifier": "da1307f028f21a95876634f3afaf23a8",
        "SupplierDomain": "NetworkID",
        "SupplierIdentifier": "da1307f028f21a95876634f3afaf23a8",
        "EinvoiceDeliveryEnabled": true,
        "PurchaseOrderRetrievalEnabled": false,
        "Contacts": "HIDDEN_DUE_TO_SECURITY_REASONS",
        "Selector": {
            "InvoiceUnitArns": [],
            "SellerOfRecords": []
        },
        "ProcurementPortalSharedSecret": "HIDDEN_DUE_TO_SECURITY_REASONS",
        "ProcurementPortalInstanceEndpoint": "https://example.com",
        "EinvoiceDeliveryPreference": {
            "EinvoiceDeliveryDocumentTypes": [
                "AWS_MARKETPLACE_INVOICE"
            ],
            "Protocol": "CXML",
            "PurchaseOrderDataSources": [
                {
                    "EinvoiceDeliveryDocumentType": "AWS_MARKETPLACE_INVOICE",
                    "PurchaseOrderDataSourceType": "ASSOCIATED_PURCHASE_ORDER_REQUIRED"
                }
            ],
            "ConnectionTestingMethod": "PROD_ENV_DOLLAR_TEST",
            "EinvoiceDeliveryActivationDate": 1773619200,
            "EinvoiceDeliveryAttachmentTypes": []
        },
        "ClientToken": "c333a7e9-17d6-4f58-a4a1-EXAMPLE"
    },
    "responseElements": {
        "ProcurementPortalPreferenceArn": "arn:aws:invoicing::111122223333:procurement-portal-preference/090d2e03-EXAMPLE"
    },
    "requestID": "935ec8a3-b9dd-4309-b975-EXAMPLE",
    "eventID": "b15c33a2-36a3-4b0a-b2e4-EXAMPLE",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "tlsDetails": {
        "clientProvidedHostHeader": "invoicing.us-east-1.api.aws"
    },
    "sessionCredentialFromConsole": "true"
}
```