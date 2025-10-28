# Troubleshooting AWS CodeStar Notifications and AWS CodeConnections

identity and access

Use the following information to help you diagnose and fix common issues that you
might encounter when working with notifications and IAM.

###### Topics

- [I'm an administrator and
  want to allow others to access notifications](#security_iam_troubleshoot-admin-delegate "#security_iam_troubleshoot-admin-delegate")
- [I created an Amazon SNS topic and added
  it as a notification rule target, but I am not receiving emails about
  events](#security_iam_troubleshoot-sns "#security_iam_troubleshoot-sns")
- [I want to allow
  people outside of my AWS account to access my AWS CodeStar Notifications and AWS CodeConnections
  resources](#security_iam_troubleshoot-cross-account-access "#security_iam_troubleshoot-cross-account-access")

## I'm an administrator and

want to allow others to access notifications

To allow others to access AWS CodeStar Notifications and AWS CodeConnections, you must grant permission to the people or applications that need access. If you are using AWS IAM Identity Center
to manage people and applications, you assign permission sets to users or groups to define their level of access. Permission sets automatically create
and assign IAM policies to IAM roles that are associated with the person or application. For more information, see [Permission sets](../../../singlesignon/latest/userguide/permissionsetsconcept.md "../../../singlesignon/latest/userguide/permissionsetsconcept.md") in the _AWS IAM Identity Center User Guide_.

If you are not using IAM Identity Center, you must create IAM entities (users or roles) for the people or applications that need access. You must then attach
a policy to the entity that grants them the correct permissions in AWS CodeStar Notifications and AWS CodeConnections. After the permissions are granted, provide the credentials to the user
or application developer. They will use those credentials to access AWS. To learn more about creating IAM users, groups, policies, and permissions,
see [IAM Identities](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") and [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.

For AWS CodeStar Notifications specific information, see [Permissions
and examples for AWS CodeStar Notifications](security_iam_id-based-policy-examples-notifications.md "security_iam_id-based-policy-examples-notifications.md").

## I created an Amazon SNS topic and added

it as a notification rule target, but I am not receiving emails about
events

In order to receive notifications about events, you must have a valid Amazon SNS topic
subscribed as a target for the notification rule, and your email address must be
subscribed to the Amazon SNS topic. To troubleshoot problems with the Amazon SNS topic, check
the following:

- Make sure that the Amazon SNS topic is in the same AWS Region as the
  notification rule.
- Check to make sure that your email alias is subscribed to the correct
  topic, and that you have confirmed the subscription. For more information,
  see [Subscribing an endpoint to an Amazon SNS topic](../../../sns/latest/dg/sns-tutorial-create-subscribe-endpoint-to-topic.md "../../../sns/latest/dg/sns-tutorial-create-subscribe-endpoint-to-topic.md").
- Verify that the topic policy has been modified to allow AWS CodeStar Notifications to push
  notifications to that topic. The topic policy should include a statement
  similar to the following:

```
{
    "Sid": "AWSCodeStarNotifications_publish",
    "Effect": "Allow",
    "Principal": {
        "Service": [
            "codestar-notifications.amazonaws.com"
        ]
    },
    "Action": "SNS:Publish",
    "Resource": "arn:aws:sns:us-east-1:123456789012:MyNotificationTopicName",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "123456789012"
        }
    }
}
```

For more information, see [Setting up](setting-up.md "setting-up.md").

## I want to allow

people outside of my AWS account to access my AWS CodeStar Notifications and AWS CodeConnections
resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who
is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant
people access to your resources.

To learn more, consult the following:

- To learn whether AWS CodeStar Notifications and AWS CodeConnections supports these features, see [How features in the developer tools
  console work with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you
  own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the
  _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
  _IAM User Guide_.
