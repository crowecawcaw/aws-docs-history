

# Logging AWS Payment Cryptography API calls using AWS CloudTrail
<a name="monitoring-cloudtrail"></a>

AWS Payment Cryptography is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Payment Cryptography. CloudTrail captures all API calls for AWS Payment Cryptography as events. The calls captured include calls from the console and code calls to the API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS Payment Cryptography. If you don't configure a trail, you can still view the most recent management (Control Plane) events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to AWS Payment Cryptography, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

**Topics**
+ [AWS Payment Cryptography information in CloudTrail](#service-name-info-in-cloudtrail)
+ [Control plane events in CloudTrail](#management-events-in-cloud-trail)
+ [Data events in CloudTrail](#data-events-in-cloud-trail)
+ [Understanding AWS Payment Cryptography Control Plane log file entries](#understanding-controlplane-entries)
+ [Understanding AWS Payment Cryptography Data plane log file entries](#understanding-dataplane-entries)

## AWS Payment Cryptography information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in AWS Payment Cryptography, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for AWS Payment Cryptography, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail log files from multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html)
+ [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Control plane events in CloudTrail
<a name="management-events-in-cloud-trail"></a>

CloudTrail logs AWS Payment Cryptography operations, such as [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html), [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html), [DeleteKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html), [ListKeys](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListKeys.html), [TagResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html), and all other control plane operations.

## Data events in CloudTrail
<a name="data-events-in-cloud-trail"></a>

 [ Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events.html) provide information about the resource operations performed on or in a resource, such as encrypting a payload or translating a pin. Data events are high-volume activities that CloudTrail does not log by default. You can enable data events API action logging for AWS Payment Cryptography data plane events by using CloudTrail APIs or console. For more information, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide*. 

 With CloudTrail, you must use advanced event selectors to decide which AWS Payment Cryptography API activities are logged and recorded. To log AWS Payment Cryptography data plane events, you must include the resource type `AWS Payment Cryptography key` and `AWS Payment Cryptography alias`. Once this is set, you can refine your logging preferences further by selecting specific data events for recording, such as using the `eventName` filter to track `EncryptData` events. For more information, see [`AdvancedEventSelector`](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html) in the *AWS CloudTrail API Reference*. 

**Note**  
To subscribe to AWS Payment Cryptography data events, you must utilize advanced event selectors. We recommend subscribing to key and alias events to ensure that you receive all events. 

**AWS Payment Cryptography data events:**
+ `[DecryptData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DecryptData.html)`
+ `[EncryptData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EncryptData.html)`
+ `[GenerateCardValidationData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateCardValidationData.html)`
+ `[GenerateMac](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateMac.html)`
+ `[GeneratePinData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GeneratePinData.html)`
+ `[ReEncryptData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_ReEncryptData.html)`
+ `[TranslatePinData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_TranslatePinData.html)`
+ `[VerifyAuthRequestCryptogram](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyAuthRequestCryptogram.html)`
+ `[VerifyCardValidationData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyCardValidationData.html)`
+ `[VerifyMac](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyMac.html)`
+ `[VerifyPinData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyPinData.html)`

 Additional charges apply for data events. For more information, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/). 

## Understanding AWS Payment Cryptography Control Plane log file entries
<a name="understanding-controlplane-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following example shows a CloudTrail log entry that demonstrates the AWS Payment Cryptography `CreateKey` action.

```
      {
    CloudTrailEvent: {
      tlsDetails= {
        TlsDetails: {
          cipherSuite=TLS_AES_128_GCM_SHA256, 
          tlsVersion=TLSv1.3, 
          clientProvidedHostHeader=controlplane.paymentcryptography.us-west-2.amazonaws.com
        }
      }, 
    requestParameters=CreateKeyInput (
      keyAttributes=KeyAttributes(
        KeyUsage=TR31_B0_BASE_DERIVATION_KEY, 
        keyClass=SYMMETRIC_KEY, 
        keyAlgorithm=AES_128, 
        keyModesOfUse=KeyModesOfUse(
          encrypt=false,
          decrypt=false,
          wrap=false
          unwrap=false,
          generate=false,
          sign=false, 
          verify=false,
          deriveKey=true,
          noRestrictions=false)
        ), 
      keyCheckValueAlgorithm=null, 
      exportable=true, 
      enabled=true, 
      tags=null), 
    eventName=CreateKey, 
    userAgent=Coral/Apache-HttpClient5, 
    responseElements=CreateKeyOutput(
      key=Key(
        keyArn=arn:aws:payment-cryptography:us-east-2:111122223333:key/5rplquuwozodpwsp, 
          keyAttributes=KeyAttributes(
            KeyUsage=TR31_B0_BASE_DERIVATION_KEY, 
            keyClass=SYMMETRIC_KEY, 
            keyAlgorithm=AES_128, 
            keyModesOfUse=KeyModesOfUse(
              encrypt=false, 
              decrypt=false, 
              wrap=false, 
              unwrap=false, 
              generate=false,
              sign=false,
              verify=false,
              deriveKey=true,
              noRestrictions=false)
            ), 
          keyCheckValue=FE23D3, 
          keyCheckValueAlgorithm=ANSI_X9_24, 
          enabled=true, 
          exportable=true, 
          keyState=CREATE_COMPLETE, 
          keyOrigin=AWS_PAYMENT_CRYPTOGRAPHY, 
          createTimestamp=Sun May 21 18:58:32 UTC 2023, 
          usageStartTimestamp=Sun May 21 18:58:32 UTC 2023, 
          usageStopTimestamp=null, 
          deletePendingTimestamp=null, 
          deleteTimestamp=null)
        ), 
      sourceIPAddress=192.158.1.38, 
        userIdentity={
          UserIdentity: {
            arn=arn:aws:sts::111122223333:assumed-role/TestAssumeRole-us-west-2/ControlPlane-IntegTest-68211a2a-3e9d-42b7-86ac-c682520e0410, 
            invokedBy=null, 
            accessKeyId=TESTXECZ5U2ZULLHHMJG, 
            type=AssumedRole, 
            sessionContext={
              SessionContext: {
                sessionIssuer={
                  SessionIssuer: {arn=arn:aws:iam::111122223333:role/TestAssumeRole-us-west-2, 
                  type=Role, 
                  accountId=111122223333, 
                  userName=TestAssumeRole-us-west-2, 
                  principalId=TESTXECZ5U9M4LGF2N6Y5}
                }, 
                attributes={
                  SessionContextAttributes: {
                    creationDate=Sun May 21 18:58:31 UTC 2023,
                    mfaAuthenticated=false
                  }
                },
                webIdFederationData=null
              }
            },
          username=null, 
          principalId=TESTXECZ5U9M4LGF2N6Y5:ControlPlane-User, 
          accountId=111122223333,
          identityProvider=null
        }
      }, 
      eventTime=Sun May 21 18:58:32 UTC 2023, 
      managementEvent=true, 
      recipientAccountId=111122223333, 
      awsRegion=us-west-2, 
      requestID=151cdd67-4321-1234-9999-dce10d45c92e, 
      eventVersion=1.08, eventType=AwsApiCall, 
      readOnly=false, 
      eventID=c69e3101-eac2-1b4d-b942-019919ad2faf, 
      eventSource=payment-cryptography.amazonaws.com, 
      eventCategory=Management, 
      additionalEventData={
    }
  }
}
```

The following example shows a CloudTrail log entry that demonstrates the AWS Payment Cryptography enabling Multi-Region key replication.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "accountId": "111122223333",
        "invokedBy": "payment-cryptography.amazonaws.com"
    },
    "eventTime": "2025-08-15T17:50:41Z",
    "eventSource": "payment-cryptography.amazonaws.com",
    "eventName": "SynchronizeMultiRegionKey",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "payment-cryptography.amazonaws.com",
    "userAgent": "payment-cryptography.amazonaws.com",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "55c0fcbc-5b2e-4bd2-a976-99305be6e6fc",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "keyArn": "arn:aws:payment-cryptography:us-east-1:111122223333:key/key-id",
        "replicationRegion": "us-east-2"
    },
    "eventCategory": "Management"
}
```

## Understanding AWS Payment Cryptography Data plane log file entries
<a name="understanding-dataplane-entries"></a>

Data plane events can optionally be configured and function similarly to control plane logs but are typically much higher volumes. Given the sensitive nature of some inputs and outputs to AWS Payment Cryptography data plane operations, you may find certain fields with the message "\*\*\* Sensitive Data Redacted \*\*\*". This is not configurable and is intended to prevent sensitive data from appearing in logs or trails. 

The following example shows a CloudTrail log entry that demonstrates the AWS Payment Cryptography `EncryptData` action.

```
      {
        "Records": [
            {
                "eventVersion": "1.09",
                "userIdentity": {
                    "type": "AssumedRole",
                    "principalId": "TESTXECZ5U2ZULLHHMJG:DataPlane-User",
                    "arn": "arn:aws:sts::111122223333:assumed-role/Admin/DataPlane-User",
                    "accountId": "111122223333",
                    "accessKeyId": "TESTXECZ5U2ZULLHHMJG",
                    "userName": "",
                    "sessionContext": {
                        "sessionIssuer": {
                            "type": "Role",
                            "principalId": "TESTXECZ5U9M4LGF2N6Y5",
                            "arn": "arn:aws:iam::111122223333:role/Admin",
                            "accountId": "111122223333",
                            "userName": "Admin"
                        },
                        "attributes": {
                            "creationDate": "2024-07-09T14:23:05Z",
                            "mfaAuthenticated": "false"
                        }
                    }
                },
                "eventTime": "2024-07-09T14:24:02Z",
                "eventSource": "payment-cryptography.amazonaws.com",
                "eventName": "GenerateCardValidationData",
                "awsRegion": "us-east-2",
                "sourceIPAddress": "192.158.1.38",
                "userAgent": "aws-cli/2.17.6 md/awscrt#0.20.11 ua/2.0 os/macos#23.4.0 md/arch#x86_64 lang/python#3.11.8 md/pyimpl#CPython cfg/retry-mode#standard md/installer#exe md/prompt#off md/command#payment-cryptography-data.generate-card-validation-data",
                "requestParameters": {
                    "key_identifier": "arn:aws:payment-cryptography:us-east-2:111122223333:key/5rplquuwozodpwsp",
                    "primary_account_number": "*** Sensitive Data Redacted ***",
                    "generation_attributes": {
                        "CardVerificationValue2": {
                            "card_expiry_date": "*** Sensitive Data Redacted ***"
                        }
                    }
                },
                "responseElements": null,
                "requestID": "f2a99da8-91e2-47a9-b9d2-1706e733991e",
                "eventID": "e4eb3785-ac6a-4589-97a1-babdd3d4dd95",
                "readOnly": true,
                "resources": [
                    {
                        "accountId": "111122223333",
                        "type": "AWS::PaymentCryptography::Key",
                        "ARN": "arn:aws:payment-cryptography:us-east-2:111122223333:key/5rplquuwozodpwsp"
                    }
                ],
                "eventType": "AwsApiCall",
                "managementEvent": false,
                "recipientAccountId": "111122223333",
                "eventCategory": "Data",
                "tlsDetails": {
                    "tlsVersion": "TLSv1.3",
                    "cipherSuite": "TLS_AES_128_GCM_SHA256",
                    "clientProvidedHostHeader": "dataplane.payment-cryptography.us-east-2.amazonaws.com"
                }
            }
        ]
    }
```