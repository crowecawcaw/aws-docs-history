# Logging AWS Private Certificate Authority API calls using AWS CloudTrail

AWS Private Certificate Authority is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in AWS Private CA. CloudTrail captures API calls and signing operations for
AWS Private CA as events. The calls captured include calls from the AWS Private CA console and
code calls to the AWS Private CA API operations. If you create a trail, you can enable
continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS Private CA. If
you don't configure a trail, you can still view the most recent events in the CloudTrail console
in **Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to AWS Private CA, the IP address from which the request
was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## AWS Private CA information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs
in AWS Private CA, that activity is recorded in a CloudTrail event along with other AWS service events
in **Event history**. You can view, search, and download recent events in
your AWS account. For more information, see [Viewing events with CloudTrail Event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for AWS Private CA,
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

All AWS Private CA actions are logged by CloudTrail and are documented in the [AWS Private CA API reference](../APIReference/Welcome.md "../APIReference/Welcome.md"). For example,
calls to the `ImportCACertificate`, `IssueCertificate` and `CreateAuditReport` actions generate
entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## AWS Private CA management events

AWS Private CA integrates with CloudTrail to record API actions made by a user, a role, or an AWS service in AWS Private CA. You can use CloudTrail to monitor AWS Private CA API requests in real time and store logs in Amazon Simple Storage Service, Amazon CloudWatch Logs, and Amazon CloudWatch Events. AWS Private CA supports logging the following actions and operations as events in CloudTrail log files:

- [CreateCertificateAuthority](../APIReference/API_CreateCertificateAuthority.md "../APIReference/API_CreateCertificateAuthority.md")
- [CreateCertificateAuthorityAuditReport](../APIReference/API_CreateCertificateAuthorityAuditReport.md "../APIReference/API_CreateCertificateAuthorityAuditReport.md")
- [CreatePermission](../APIReference/API_CreatePermission.md "../APIReference/API_CreatePermission.md")
- [DeleteCertificateAuthority](../APIReference/API_DeleteCertificateAuthority.md "../APIReference/API_DeleteCertificateAuthority.md")
- [DeletePermission](../APIReference/API_DeletePermission.md "../APIReference/API_DeletePermission.md")
- [DeletePolicy](../APIReference/API_DeletePolicy.md "../APIReference/API_DeletePolicy.md")
- [DescribeCertificateAuthority](../APIReference/API_DescribeCertificateAuthority.md "../APIReference/API_DescribeCertificateAuthority.md")
- [DescribeCertificateAuthorityReport](../APIReference/API_DescribeCertificateAuthorityReport.md "../APIReference/API_DescribeCertificateAuthorityReport.md")
- [GetCertificate](../APIReference/API_GetCertificate.md "../APIReference/API_GetCertificate.md")
- [GetCertificateAuthorityCertificate](../APIReference/API_GetCertificateAuthorityCertificate.md "../APIReference/API_GetCertificateAuthorityCertificate.md")
- [GetCertificateAuthorityCsr](../APIReference/API_GetCertificateAuthorityCsr.md "../APIReference/API_GetCertificateAuthorityCsr.md")
- [GetPolicy](../APIReference/API_API_GetPolicy.md "../APIReference/API_API_GetPolicy.md")
- [ImportCertificateAuthorityCertificate](../APIReference/API_ImportCertificateAuthorityCertificate.md "../APIReference/API_ImportCertificateAuthorityCertificate.md")
- [IssueCertificate](../APIReference/API_IssueCertificate.md "../APIReference/API_IssueCertificate.md")
- [ListCertificateAuthorities](../APIReference/API_ListCertificateAuthorities.md "../APIReference/API_ListCertificateAuthorities.md")
- [ListPermissions](../APIReference/API_ListPermissions.md "../APIReference/API_ListPermissions.md")
- [ListTags](../APIReference/API_ListTags.md "../APIReference/API_ListTags.md")
- [PutPolicy](../APIReference/API_PutPolicy.md "../APIReference/API_PutPolicy.md")
- [RestoreCertificateAuthority](../APIReference/API_RestoreCertificateAuthority.md "../APIReference/API_RestoreCertificateAuthority.md")
- [RevokeCertificate](../APIReference/API_RevokeCertificate.md "../APIReference/API_RevokeCertificate.md")
- [TagCertificateAuthority](../APIReference/API_TagCertificateAuthority.md "../APIReference/API_TagCertificateAuthority.md")
- [UntagCertificateAuthority](../APIReference/API_UntagCertificateAuthority.md "../APIReference/API_UntagCertificateAuthority.md")
- [UpdateCertificateAuthority](../APIReference/API_UpdateCertificateAuthority.md "../APIReference/API_UpdateCertificateAuthority.md")
- `GenerateOCSPResponse` - Triggered when AWS Private CA generates a OCSP response.
- `SignCertificate` - Generated when your client calls [IssueCertificate](../APIReference/API_IssueCertificate.md "../APIReference/API_IssueCertificate.md").
- `SignOCSPResponse` - Generated when AWS Private CA signs an OCSP response.
- `GenerateCRL` - Generated when AWS Private CA generates a certificate revocation list (CRL).
- `SignCACSR` - Generated when AWS Private CA signs a certificate authority (CA) certificate signing request (CSR).
- `SignCRL` - Generated when AWS Private CA signs a CRL.

## Example AWS Private CA events

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following are examples of AWS Private CA CloudTrail events.

###### Example 1: Management event, `IssueCertificate`

The following example shows a CloudTrail log entry that demonstrates the `IssueCertificate` action.

```
{
   "version":"0",
   "id":"`event_ID`",
   "detail-type":"ACM Private CA Certificate Issuance",
   "source":"aws.acm-pca",
   "account":"`account`",
   "time":"2019-11-04T19:57:46Z",
   "region":"`region`",
   "resources":[
      "arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`",
      "arn:aws:acm-pca:`region`:`account`:certificate-authority/`CA_ID`/certificate/`certificate_ID`"
   ],
   "detail":{
      "result":"success"
   }
}
```

###### Example 2: Management event, `ImportCertificateAuthorityCertificate`

The following example shows a CloudTrail log entry that demonstrates the `ImportCertificateAuthorityCertificate` action.

```
{
   "eventVersion":"1.05",
   "userIdentity":{
      "type":"IAMUser",
      "principalId":"`account`",
      "arn":"arn:aws:iam::`account`:`user/name`",
      "accountId":"`account`",
      "accessKeyId":"`key_ID`"
   },
   "eventTime":"2018-01-26T21:53:28Z",
   "eventSource":"acm-pca.amazonaws.com",
   "eventName":"ImportCertificateAuthorityCertificate",
   "awsRegion":"`region`",
   "sourceIPAddress":"`IP_address`",
   "userAgent":"`agent`",
   "requestParameters":{
      "certificateAuthorityArn":"arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566`",
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
   "requestID":"`request_ID`",
   "eventID":"`event_ID`",
   "eventType":"AwsApiCall",
   "recipientAccountId":"`account`"
}
```
