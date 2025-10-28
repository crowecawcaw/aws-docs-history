# Identity and Access Management

AWS Identity and Access Management (IAM) is an AWS service that
helps an administrator control access to AWS resources. IAM
administrators control _authenticated_ (signed
in) and _authorized_ (have permissions)
principals to use AWS Security Incident Response resources. IAM is
an AWS service that you can use with no additional charge.

###### Contents

- [Authenticating with identities](authenticating-with-identities.md "authenticating-with-identities.md")
- [How AWS Security Incident Response Works with IAM](how-aws-security-incident-response-works-with-iam.md "how-aws-security-incident-response-works-with-iam.md")

**Audience**

How you use AWS Identity and Access Management (IAM) differs,
depending on the work that you do in AWS Security Incident Response.

**Security Administrators**

These users are suggested to use the [AWSSecurityIncidentResponseFullAccess](aws-managed-policies.md#AWSSecurityIncidentResponseFullAccess "aws-managed-policies.md#AWSSecurityIncidentResponseFullAccess") managed policy to ensure they have read and write
access to membership and case resources.

**Case Watchers**

These individuals do not have authoritative access to all cases but individual cases that you grant explicit permission for.

**Incident Response Team members**

Members of the team can be given both full membership and case access. It is recommended that
not all individuals have authoritative action on service membership but should have access to
any and all cases that are created and managed through the service. For more information, refer
to [AWS Security Incident Response managed policies](aws-managed-policies.md "aws-managed-policies.md").
