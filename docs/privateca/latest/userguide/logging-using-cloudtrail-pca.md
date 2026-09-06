

# Logging AWS Private Certificate Authority API calls using AWS CloudTrail
<a name="logging-using-cloudtrail-pca"></a>

AWS Private Certificate Authority is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Private CA. CloudTrail captures API calls and signing operations for AWS Private CA as events. The calls captured include calls from the AWS Private CA console and code calls to the AWS Private CA API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS Private CA. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to AWS Private CA, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

## AWS Private CA information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in AWS Private CA, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for AWS Private CA, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All AWS Private CA actions are logged by CloudTrail and are documented in the [AWS Private CA API reference](https://docs.aws.amazon.com/privateca/latest/APIReference/Welcome.html). For example, calls to the `ImportCACertificate`, `IssueCertificate` and `CreateAuditReport` actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

**Note**  
You can configure your CloudTrail trail to deliver events to Amazon CloudWatch Logs in addition to Amazon S3. When configured, CloudWatch Logs receives the same AWS Private CA events that are delivered to your S3 bucket. AWS Private CA does not publish events directly to CloudWatch Logs. For more information, see [Sending events to CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.html) in the *AWS CloudTrail User Guide*.

For information about how CloudTrail delivers events — including delivery timing, durability, and integration with other AWS services — see [Getting and viewing your CloudTrail log files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html) and the [AWS CloudTrail Service Level Agreement](https://aws.amazon.com/cloudtrail/sla/).

## AWS Private CA management events
<a name="pca-management-events"></a>

AWS Private CA integrates with CloudTrail to record API actions made by a user, a role, or an AWS service in AWS Private CA. You can use CloudTrail to monitor AWS Private CA API requests in real time and store logs in Amazon Simple Storage Service, Amazon CloudWatch Logs, and Amazon CloudWatch Events. AWS Private CA supports logging the following actions and operations as events in CloudTrail log files:
+ [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html)
+ [CreateCertificateAuthorityAuditReport](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html)
+ [CreatePermission](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreatePermission.html)
+ [DeleteCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthority.html)
+ [DeletePermission](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePermission.html)
+ [DeletePolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePolicy.html)
+ [DescribeCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthority.html)
+ [DescribeCertificateAuthorityReport](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthorityReport.html)
+ [GetCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificate.html)
+ [GetCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCertificate.html)
+ [GetCertificateAuthorityCsr](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCsr.html)
+ [GetPolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_API_GetPolicy.html)
+ [ImportCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html)
+ [IssueCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html)
+ [ListCertificateAuthorities](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html)
+ [ListPermissions](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListPermissions.html)
+ [ListTags](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListTags.html)
+ [PutPolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_PutPolicy.html)
+ [RestoreCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_RestoreCertificateAuthority.html)
+ [RevokeCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html)
+ [TagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_TagCertificateAuthority.html)
+ [UntagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UntagCertificateAuthority.html)
+ [UpdateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html)
+ `GenerateOCSPResponse` - Triggered when AWS Private CA generates a OCSP response.
+ `SignCertificate` - Generated when your client calls [IssueCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html).
+ `SignOCSPResponse` - Generated when AWS Private CA signs an OCSP response.
+ `GenerateCRL` - Generated when AWS Private CA generates a certificate revocation list (CRL).
+ `SignCACSR` - Generated when AWS Private CA signs a certificate authority (CA) certificate signing request (CSR).
+ `SignCRL` - Generated when AWS Private CA signs a CRL.

**Note**  
CloudTrail provides a real-time event stream of API calls and signing operations. For a complete point-in-time inventory of all certificates that your private CA has issued or revoked, including validity dates and revocation status, see [Use audit reports with your private CA](PcaAuditReport.md).

## Identifying the original requester
<a name="pca-identifying-original-requester"></a>

When an intermediate service calls `IssueCertificate` on behalf of end-users or workloads, the CloudTrail event records the intermediate service's IAM identity in the `userIdentity` field — not the original requester.

To trace certificate issuance back to the original requester, the intermediate service can propagate identity information using standard IAM mechanisms:
+ **Session tags** — The intermediate service passes identifying information (such as the original requester's ID) as session tags when assuming its IAM role via AWS STS. These tags appear in the CloudTrail event's `userIdentity` block under `sessionContext`. For more information, see [Passing session tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html).
+ **Source identity** — The intermediate service sets a source identity when assuming its role. Source identity is immutable across role chains and appears in CloudTrail as `sourceIdentity`. For more information, see [Monitoring and controlling actions taken with assumed roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html).
+ **IAM Roles Anywhere** — If the calling workload authenticates with an X.509 certificate via IAM Roles Anywhere, the certificate's Subject, Issuer, and Subject Alternative Name (SAN) fields are automatically mapped to session principal tags. For example, a SPIFFE ID in the SAN appears as `aws:PrincipalTag/x509SAN/URI`. For more information, see [The IAM Roles Anywhere trust model](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/trust-model.html).

These identity attributes are recorded in CloudTrail events for all AWS service calls, including AWS Private CA API operations.

## Example AWS Private CA events
<a name="understanding-service-name-entries-pca"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following are examples of AWS Private CA CloudTrail events.

**Example 1: Management event, `IssueCertificate`**  
The following example shows a CloudTrail log entry that demonstrates the `IssueCertificate` action.

```
{
   "version":"0",
   "id":"{{event_ID}}",
   "detail-type":"ACM Private CA Certificate Issuance",
   "source":"aws.acm-pca",
   "account":"{{account}}",
   "time":"2019-11-04T19:57:46Z",
   "region":"{{region}}",
   "resources":[
      "arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}",
      "arn:aws:acm-pca:{{region}}:{{account}}:certificate-authority/{{CA_ID}}/certificate/{{certificate_ID}}"
   ],
   "detail":{
      "result":"success"
   }
}
```

**Example 2: Management event, `ImportCertificateAuthorityCertificate`**  
The following example shows a CloudTrail log entry that demonstrates the `ImportCertificateAuthorityCertificate` action.

```
{
   "eventVersion":"1.05",
   "userIdentity":{
      "type":"IAMUser",
      "principalId":"{{account}}",
      "arn":"arn:aws:iam::{{account}}:{{user/name}}",
      "accountId":"{{account}}",
      "accessKeyId":"{{key_ID}}"
   },
   "eventTime":"2018-01-26T21:53:28Z",
   "eventSource":"acm-pca.amazonaws.com",
   "eventName":"ImportCertificateAuthorityCertificate",
   "awsRegion":"{{region}}",
   "sourceIPAddress":"{{IP_address}}",
   "userAgent":"{{agent}}",
   "requestParameters":{
      "certificateAuthorityArn":"arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}",
      "certificate":{
         "hb":[
            45,
            45,
            ...10
         ],
         "offset":0,
         "isReadOnly":false,
         "bigEndian":true,
         "nativeByteOrder":false,
         "mark":-1,
         "position":1257,
         "limit":1257,
         "capacity":1257,
         "address":0
      },
      "certificateChain":{
         "hb":[
            45,
            45,
            ...10
         ],
         "offset":0,
         "isReadOnly":false,
         "bigEndian":true,
         "nativeByteOrder":false,
         "mark":-1,
         "position":1139,
         "limit":1139,
         "capacity":1139,
         "address":0
      }
   },
   "responseElements":null,
   "requestID":"{{request_ID}}",
   "eventID":"{{event_ID}}",
   "eventType":"AwsApiCall",
   "recipientAccountId":"{{account}}"
}
```