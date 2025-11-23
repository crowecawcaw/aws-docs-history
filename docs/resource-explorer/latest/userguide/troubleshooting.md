# Troubleshooting Resource Explorer

If you encounter issues when working with Resource Explorer, consult the topics in this section. Also
see [Troubleshooting AWS Resource Explorer permissions](security_iam_troubleshoot.md "security_iam_troubleshoot.md") in
the **Security** section of this guide.

###### Topics

- [General issues](#troubleshooting_general "#troubleshooting_general")
  (_this page_)
- [Troubleshooting Resource Explorer setup and configuration
  issues](troubleshooting_setup.md "troubleshooting_setup.md")
- [Troubleshooting Resource Explorer search issues](troubleshooting_search.md "troubleshooting_search.md")

## General issues

###### Topics

- [I received a link to Resource Explorer
  but when I open it, the console shows only an error.](#troubleshooting_general_url-no-region "#troubleshooting_general_url-no-region")
- [Why does Unified Search
  in the console cause "access denied" errors in my CloudTrail logs?](#troubleshooting_general_us-access-denied "#troubleshooting_general_us-access-denied")

### I received a link to Resource Explorer

but when I open it, the console shows only an error.

Some third-party tools produce link URLs to pages in Resource Explorer. In some cases, those
URLs don't include the parameter that directs the console to a specific
AWS Region. If you open such a link, the Resource Explorer console isn't told which Region to
use, and defaults to using the last Region the user signed in to. If the user
doesn't have permissions to access Resource Explorer in that Region, then the console attempts
to use US East (N. Virginia) (`us-east-1`) Region, or US West (Oregon)
(`us-west-2`) if the console can't reach
`us-east-1`.

If the user doesn't have permission to access the index in any of those Regions,
then the Resource Explorer console returns an error.

You can prevent this issue by ensuring that all users have the following
permissions:

- `ListIndexes` – no specific resource; use
  `*`.
- `GetIndex` for the ARN of the each index created in the
  account. To avoid having to redo permission policies if you delete and
  recreate an index, we recommend that you use `*`.

The minimum policy to achieve this might look like this example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "resource-explorer-2:GetIndex",
 "resource-explorer-2:ListIndexes"
 ],
 "Resource": "*"
 }
 ]
}`

```

Alternatively, you might consider attaching the [AWS managed permission `AWSResourceExplorerReadOnlyAccess`](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSResourceExplorerReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSResourceExplorerReadOnlyAccess")
to all users who need to use Resource Explorer. That grants these required permissions, plus
the permissions needed see the available views in the Region and search using those
views.

### Why does Unified Search

in the console cause "access denied" errors in my CloudTrail logs?

[Unified Search in the AWS Management Console](using-unified-search.md "using-unified-search.md") lets
principals search from any page in the AWS Management Console. The results can include resources
from the principal's account if Resource Explorer is turned on and configured to support
Unified Search. Whenever you start typing in the Unified Search bar, Unified Search
attempts to call `resource-explorer-2:ListIndexes` operation to check
whether it can include resources from the user's account in the results.

Unified Search uses the currently signed-in user's permissions to perform this
check. If that user doesn't have permission to call
`resource-explorer-2:ListIndexes` granted in an attached AWS Identity and Access Management
(IAM) permission policy, then the check fails. That failure is added as an
`Access denied` entry in your CloudTrail logs.

This CloudTrail log entry has the following characteristics:

- **Event source:**
  `resource-explorer-2.amazonaws.com`
- **Event name:**
  `ListIndexes`
- **Error code:**
  `403` (Access denied)

The following AWS managed policies include permission to call
`resource-explorer-2:ListIndexes`. If you assign any of these to the
principal, or any other policy that includes this permission, then this error does
not occur:

- [AWSResourceExplorerReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSResourceExplorerReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSResourceExplorerReadOnlyAccess")
- [AWSResourceExplorerFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSResourceExplorerFullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSResourceExplorerFullAccess")
- [ReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ReadOnlyAccess")
- [ViewOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/job-function/ViewOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/job-function/ViewOnlyAccess")
