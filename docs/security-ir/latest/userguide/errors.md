# Errors

**AccessDeniedException**

You do not have sufficient access to perform this action.

Please work with your AWS administrator to ensure that you have
permission to assume an IAM Role in your AWS Security Incident Response delegated
administrator or membership account. Also check the role
has a an IAM policy that permits the requested action. For more
information see [AWS Security Incident Response IAM](identity-and-access-management.md "identity-and-access-management.md").

**ConflictException**

The request causes an inconsistent state.

Please check that any case attachment file names
or default response team members that you have specified are
unique. Also check that your AWS Security Incident Response service membership has
not already been configured. Open the Security Incident Response console at https://console.aws.amazon.com/security-ir/ and navigate to
`Membership Details`.

**InternalServerException**

An unexpected error occurred during the processing of the request.
Please try again in a few minutes. If the issue persists,
[raise
a case with Support](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md").

**ResourceNotFoundException**

The request references a resource that does not exist.

One or more of the resources specified in your request does not
exist. Please check that all given resource ARNs or IDs are
correct. This applies to AWS Organizations IDs, account IDs, IAM roles,
memberships, cases, response team members, cases, case responders,
case attachments, and case comments.

**ThrottlingException**

The request was denied due to request throttling.

Too many requests have been made by your IAM principal to that API
function in a specified period. Wait a minute and try again. If the issue persists, please
consider implementing an exponential backoff and retry algorithm.

**ValidationException**

The input fails to satisfy the constraints specified by an AWS service.

One or more of the data fields in your request did not meet
validation and/or logical combination requirements. Please check
that all resource ARNs complete, and that text values meet size
and format constraints from the [AWS Security Incident Response API Reference Guide](../APIReference/Welcome.md "../APIReference/Welcome.md"). Also
check that any value updates are permitted. For example, changing
a case from AWS supported to self-managed is not possible.
