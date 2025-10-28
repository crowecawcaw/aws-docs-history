# Automate Connector for SCEP using EventBridge

You can use [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-cwe-now-eb.md "../../../eventbridge/latest/userguide/eb-cwe-now-eb.md") to automate your AWS services and respond automatically to
system events such as application availability issues or resource changes. Events from
AWS services are delivered to EventBridge in near-real time. You can write simple rules to
indicate which events are of interest to you and the automated actions to take when an
event matches a rule. EventBridge are published at least once. For more information, see
[Creating rules that react to events in EventBridge](../../../AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.md "../../../AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.md").

CloudWatch Events are turned into actions using EventBridge. With EventBridge, you can use events to
trigger targets. For more information, see [What Is Amazon
EventBridge?](../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md "../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md")

## Connector for SCEP event types

### Certificate Issuance Succeeded

Connector for SCEP sends a `Certificate Issuance Succeeded` event to EventBridge when we issue a certificate in response to a `PkiOperationPost` request.

The following is example data for the event.

```
{
   "version": "0",
   "id": "event_ID",
   "detail-type": "Certificate Issuance Succeeded",
   "source": "aws.pca-connector-scep",
   "account": "account",
   "time": "2024-09-12T19:14:56Z",
   "region": "region",
   "resources":[
       "arn:aws:acm-pca:us-east-1:111122223333:certificate-authority/11223344-1234-1122-2233-112233445566",
       "arn:aws:pca-connector-scep:us-east-1:111122223333:connector/11223344-1234-1122-2233-112233445566"
   ],
   "detail": {
       "result": "success",
       "requestType": "PkiOperationPost",
       "certificateArn": "arn:aws:acm-pca:region:account:certificate-authority/CA_ID/certificate/certificate_ID"
   }
}
```

### Certificate Issuance Failed

Connector for SCEP sends a `Certificate Issuance Failed` event to EventBridge when we are unable to issue a certificate in response to a `PkiOperationPost` request.

The following is example data for the event.

```
{
   "version": "0",
   "id": "event_ID",
   "detail-type": "Certificate Issuance Failed",
   "source": "aws.pca-connector-scep",
   "account": "account",
   "time": "2024-09-12T19:14:56Z",
   "region": "region",
   "resources":[
       "arn:aws:acm-pca:us-east-1:111122223333:certificate-authority/11223344-1234-1122-2233-112233445566",
       "arn:aws:pca-connector-scep:us-east-1:111122223333:connector/11223344-1234-1122-2233-112233445566"
   ],
   "detail": {
       "result": "failure",
       "requestType": "PkiOperationPost",
       "reason": "The certificate authority is not active."
   }
}
```

### Certificate Authority Certificate Retrieval Succeeded

Connector for SCEP sends a `Certificate Authority Certificate Retrieval Succeeded` event to EventBridge when we receive a `GetCACert` request and successfully retrieve the connector's private CA certificate.

The following is example data for the event.

```
{
   "version": "0",
   "id": "event_ID",
   "detail-type": "Certificate Authority Certificate Retrieval Succeeded",
   "source": "aws.pca-connector-scep",
   "account": "account",
   "time": "2024-09-12T19:14:56Z",
   "region": "region",
   "resources":[
       "arn:aws:acm-pca:us-east-1:111122223333:certificate-authority/11223344-1234-1122-2233-112233445566",
       "arn:aws:pca-connector-scep:us-east-1:111122223333:connector/11223344-1234-1122-2233-112233445566"
   ],
   "detail": {
       "result": "success",
       "requestType": "GetCACert"
   }
}
```

### Certificate Authority Certificate Retrieval Failed

Connector for SCEP sends a `Certificate Authority Certificate Retrieval Failed` event to EventBridge when we receive a `GetCACert` request and aren't able to retrieve the connector's private CA certificate. The event includes the reason for the failure.

The following is example data for the event.

```
{
   "version": "0",
   "id": "event_ID",
   "detail-type": "Certificate Authority Certificate Retrieval Failed",
   "source": "aws.pca-connector-scep",
   "account": "account",
   "time": "2024-09-12T19:14:56Z",
   "region": "region",
   "resources":[
       "arn:aws:acm-pca:us-east-1:111122223333:certificate-authority/11223344-1234-1122-2233-112233445566",
       "arn:aws:pca-connector-scep:us-east-1:111122223333:connector/11223344-1234-1122-2233-112233445566"
   ],
   "detail": {
       "result": "failure",
       "requestType": "GetCACert",
       "reason": "The certificate authority certificate validity must be at least one year from today."
   }
}
```

### Certificate Authority Certificate Retrieval Succeeded

Connector for SCEP sends a `Certificate Authority Certificate Retrieval Succeeded` event to EventBridge when we receive a `GetCACert` request and successfully retrieve the connector's private CA certificate.

The following is example data for the event.

```
{
   "version": "0",
   "id": "event_ID",
   "detail-type": "Certificate Authority Certificate Retrieval Succeeded",
   "source": "aws.pca-connector-scep",
   "account": "account",
   "time": "2024-09-12T19:14:56Z",
   "region": "region",
   "resources":[
       "arn:aws:acm-pca:us-east-1:111122223333:certificate-authority/11223344-1234-1122-2233-112233445566",
       "arn:aws:pca-connector-scep:us-east-1:111122223333:connector/11223344-1234-1122-2233-112233445566"
   ],
   "detail": {
       "result": "success",
       "requestType": "GetCACert"
   }
}
```

### Certificate Authority Capabilities Retrieval Succeeded

Connector for SCEP sends a `Certificate Authority Capabilities Retrieval Succeeded` event to EventBridge when we receive a SCEP `GetCACaps` request and successfully retrieve the CA's capabilities.

The following is example data for the event.

### Certificate Authority Capabilities Retrieval Failed

Connector for SCEP sends a `Certificate Authority Capabilities Retrieval Failed` event to EventBridge when we receive a SCEP `GetCACaps` request and can't retrieve the CA's capabilities. We include the reason for failure in the event.

The following is example data for the event.

```
{
 "resources":
     [
     "arn:aws:acm-pca:us-east-1:111122223333:certificate-authority/11223344-1234-1122-2233-112233445566",
     "arn:aws:pca-connector-scep:us-east-1:111122223333:connector11223344-1234-1122-2233-112233445566"
     ],
 "detailType":"Certificate Authority Capabilities Retrieval Failed",
 "detail": {
     "result":"failure",
     "requestType":"GetCACaps",
     "reason":"The request was denied due to request throttling."
 },
 "source":"aws.pca-connector-scep","accountId":"111122223333"
 }
```

### Unsupported Operation Invoked

###### Unsupported Operation Invoked

Connector for SCEP sends an `Unsupported Operation Invoked` event to EventBridge if the operation sent to the connector endpoint is unsupported or unknown.

```
{
   "version": "0",
   "id": "event_ID",
   "detail-type": "Unsupported Operation Invoked",
   "source": "aws.pca-connector-scep",
   "account": "account",
   "time": "2024-09-12T19:14:56Z",
   "region": "region",
   "resources":[
       "arn:aws:acm-pca:us-east-1:111122223333:certificate-authority/11223344-1234-1122-2233-112233445566",
       "arn:aws:pca-connector-scep:us-east-1:111122223333:connector/11223344-1234-1122-2233-112233445566"
   ],
   "detail": {}
}
```

## Create an EventBridge rule

In EventBridge, you can create rules that responds to events recorded by CloudTrail. To create a rule that includes all events logged by Connector for SCEP, set the source to `aws.pca-connector-scep`. For more information about rules, see [Create a rule in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md#eb-gs-create-rule "../../../eventbridge/latest/userguide/eb-get-started.md#eb-gs-create-rule").
