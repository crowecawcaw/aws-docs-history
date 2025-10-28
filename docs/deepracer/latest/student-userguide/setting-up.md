# What are AWS Player accounts?

AWS Player accounts are a managed identity solution for AWS DeepRacer multi-user and AWS DeepRacer Student created by AWS.
Your AWS Player account holds _all_ of the resources created in each of these AWS services.

## Creating an AWS Player account for supported services

When you create an account for either [AWS DeepRacer multi-user](https://console.aws.amazon.com/deepracer/home?region=us-east-1#multiRacerGetStarted "https://console.aws.amazon.com/deepracer/home?region=us-east-1#multiRacerGetStarted")
or [AWS DeepRacer Student](https://student.deepracer.com/ "https://student.deepracer.com/") you automatically create an
AWS Player account. When you use different features in these services, new resources are added automatically into
your AWS Player account. To get started with AWS DeepRacer multi-user and AWS DeepRacer Student, use the
following links.

###### Creating an AWS DeepRacer Student account

To use AWS DeepRacer Student, get started by creating an account. To learn how to create an account see,
[Step 1: Sign up for AWS DeepRacer Student](getting-started.md#getting-started-step1 "getting-started.md#getting-started-step1") in the
_AWS DeepRacer Student User Guide_.

###### Use AWS DeepRacer multi-user to sponsor multiple participants under one account.

AWS DeepRacer multi-user mode supports two different user profiles, admin and participant. Both have different setup requirements. To get started, see [Multi-user Mode](../developerguide/multi-user-mode.md "../developerguide/multi-user-mode.md") in the _AWS DeepRacer Developer Guide_.

## Deleting an AWS Player account

If you delete an AWS Player account, you immediately lose access to all supported services. This includes any achievements (badges, points, avatars, etc) that you earned.

Deleting your AWS Player account account does not delete your AWS account. If you would also like to delete your AWS account, use the steps outlined in [Closing your AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/close-aws-account/ "https://aws.amazon.com/premiumsupport/knowledge-center/close-aws-account/").

If you have used your AWS Player account account to create an event in AWS DeepRacer multi-user you cannot delete your
AWS Player account account. This is to ensure that participants in events you have created are not left with a
broken experience. To learn more about how an admin creates events in AWS DeepRacer multi-user mode, use the following topic.

###### Setting up events using AWS DeepRacer multi-user mode (admin)

To learn how to create events using multi-user mode, see [Set up multi-user mode (admin)](../developerguide/deepracer-multi-user-admin-set-up.md "../developerguide/deepracer-multi-user-admin-set-up.md") in the _AWS DeepRacer Developer Guide_.

AWS Player accounts do not have access to any AWS resources other than those created in the service's account. Any AWS Identity and Access Management policies and associated resources in the service account are limited to only the required resources.
