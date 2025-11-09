Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Troubleshooting Amazon Fraud Detector identity

and access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with Amazon Fraud Detector and IAM.

###### Topics

- [I am not authorized to
  perform an action in Amazon Fraud Detector](#security_iam_troubleshoot-no-permissions "#security_iam_troubleshoot-no-permissions")
- [I am not authorized to perform
  iam:PassRole](#security_iam_troubleshoot-passrole "#security_iam_troubleshoot-passrole")
- [I want to allow people
  outside of my AWS account to access my Amazon Fraud Detector resources](#security_iam_troubleshoot-cross-account-access "#security_iam_troubleshoot-cross-account-access")
- [Amazon Fraud Detector could not assume the given role](#security_iam_troubleshoot-assume-role "#security_iam_troubleshoot-assume-role")

## I am not authorized to

perform an action in Amazon Fraud Detector

If the AWS Management Console tells you that you're not authorized to perform an action, then you
must contact your administrator for assistance. Your administrator is the person that
provided you with your sign-in credentials.

The following example error occurs when the `mateojackson` user
tries to use the console to view details about a `detector` but
does not have `frauddetector:`GetDetectors``
permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: frauddetector:`GetDetectors` on resource: `my-example-detector`
```

In this case, Mateo asks his administrator to update his policies to allow him to
access the `my-example-detector` resource using the
`frauddetector:`GetDetectors``
action.

## I am not authorized to perform

iam:PassRole

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to Amazon Fraud Detector.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do
this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in
Amazon Fraud Detector. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the
role to the service.

```
User: arn:aws:iam::123456789012:user/`marymajor` is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I want to allow people

outside of my AWS account to access my Amazon Fraud Detector resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who
is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant
people access to your resources.

To learn more, consult the following:

- To learn whether Amazon Fraud Detector supports these features, see [How Amazon Fraud Detector works with
  IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you
  own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the
  _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
  _IAM User Guide_.

## Amazon Fraud Detector could not assume the given role

If you receive an error that Amazon Fraud Detector could not assume the given role, then you must update the trust relationship for the specified role. By specifying Amazon Fraud Detector as a trusted entity, the service can assume the role.
When you use Amazon Fraud Detector to create a role, this trust relationship is automatically set. You only need to establish this trust relationship for IAM roles that are not created
by Amazon Fraud Detector.

###### To establish a trust relationship for an existing role to Amazon Fraud Detector

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")
2. In the navigation pane choose **Roles**.
3. Choose the name of the role that you want to modify, and choose the **Trust relationships** tab.
4. Choose **Edit trust relationship**.
5. Under **Policy Document**, paste the following, and then choose **Update Trust Policy**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [ {
 "Effect": "Allow",
 "Principal": {
 "Service": "frauddetector.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 } ]
 }`

```
