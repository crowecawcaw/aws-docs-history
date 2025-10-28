Starting November 7, 2025, you will not be able to create new repository associations in Amazon CodeGuru Reviewer. If you would like to use the service, create repository associations prior to November 7, 2025. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Troubleshooting CodeGuru Reviewer identity

and access

Use the following information to help you diagnose and fix common issues that you
might encounter when working with Amazon CodeGuru Reviewer and IAM.

###### Topics

- [I am not authorized to
  perform an action in CodeGuru Reviewer](#security_iam_troubleshoot-no-permissions "#security_iam_troubleshoot-no-permissions")
- [I am not authorized to perform
  iam:PassRole](#security_iam_troubleshoot-passrole "#security_iam_troubleshoot-passrole")

## I am not authorized to

perform an action in CodeGuru Reviewer

If the AWS Management Console tells you that you're not authorized to perform an action, you
must contact your administrator for assistance.

The following example error occurs when the user `mateojackson`
tries to use the console to view details about a code review, but does not have
`codeguru-reviewer:`DescribeCodeReview``
permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform:
            codeguru-reviewer:`DescribeCodeReview` on resource: `my-example-code-review`
```

In this case, Mateo asks his administrator to update his policies to allow him to
access the `my-example-code-review` resource
using the `codeguru-reviewer:`DescribeCodeReview``
action.

## I am not authorized to perform

iam:PassRole

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to CodeGuru Reviewer.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do
this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in
CodeGuru Reviewer. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the
role to the service.

```
User: arn:aws:iam::123456789012:user/`marymajor` is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.
