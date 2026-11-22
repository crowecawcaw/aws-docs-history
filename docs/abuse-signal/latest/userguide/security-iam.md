

# Identity and access management for AWS Abuse Signal API

Every request to AWS Abuse Signal API must be both *authenticated* (signed) and *authorized* (permitted by IAM). AWS Identity and Access Management (IAM) is an AWS service that helps you securely control access to AWS resources. You use IAM to control who can submit and track abuse reports.

**Topics**
+ [Authentication](#security-iam-authentication)
+ [Authorization with IAM](#security-iam-authorization)
+ [AWS Abuse Signal API identity-based policy examples](security-iam-id-based-policy-examples.md)

## Authentication
<a name="security-iam-authentication"></a>

Sign every request with AWS Signature Version 4 (SigV4) or Signature Version 4A (SigV4a) using the signing name `abuse`. The service rejects unsigned or improperly signed requests. For multi-Region access, sign with SigV4a. For more information, see [Choosing SigV4 or SigV4a](regions-endpoints.md#regions-endpoints-signing).

The following principal types are supported:
+ AWS account root user
+ IAM users
+ IAM roles
+ Federated users

As a best practice, prefer IAM roles and short-lived credentials over long-lived access keys, and avoid using the account root user. Most AWS SDKs and the AWS CLI sign requests for you. If you don’t use AWS tools, you must sign requests yourself. For more information, see [Signature Version 4 signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

## Authorization with IAM
<a name="security-iam-authorization"></a>

The service enforces authorization at the API edge using the AWS cross-account SigV4 mechanism. Callers must have IAM permissions for the relevant `abuse:` actions:


| IAM action | Grants | 
| --- | --- | 
|  `abuse:CreateAbuseReport`  | Permission to submit a new abuse report | 
|  `abuse:GetAbuseReportStatus`  | Permission to retrieve the status of an abuse report | 
|  `abuse:ListAbuseReportStatuses`  | Permission to list abuse report statuses | 

If you send a request that is unauthenticated or lacks permission, you receive `AccessDeniedException` (HTTP 403). Follow least privilege: grant `abuse:CreateAbuseReport` to reporting identities, and grant the read actions only where status tracking is needed. The service always scopes results from `ListAbuseReportStatuses` to your own AWS account.

**Note**  
AWS Abuse Signal API authorizes each caller directly as the signing IAM principal and does not assume a role in your account or access your resources on your behalf. It does not use resource-based policies, access control lists (ACLs), service-linked roles, or service roles.