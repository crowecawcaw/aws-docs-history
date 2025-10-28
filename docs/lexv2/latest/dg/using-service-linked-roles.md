# Using service-linked roles for

Amazon Lex V2

Amazon Lex V2 uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of
IAM role that is linked directly to Amazon Lex V2. Service-linked roles
are predefined by Amazon Lex V2 and include all the permissions that the
service requires to call other AWS services on your behalf.

A service-linked role makes setting up Amazon Lex V2 easier because you
don’t have to manually add the necessary permissions. Amazon Lex V2 defines
the permissions of its service-linked roles, and unless defined otherwise,
only Amazon Lex V2 can assume its roles. The defined permissions include the
trust policy and the permissions policy, and that permissions policy cannot
be attached to any other IAM entity.

For information about other services that support service-linked roles,
see [AWS Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that
have **Yes** in the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation
for that service.

You must configure permissions to allow an IAM entity (such as a
user, group, or role) to create, edit, or delete a service-linked role.
For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

You can delete a service-linked role only after first deleting
related resources. This protects your Amazon Lex V2 resources because you
can't inadvertently remove permissions to access the resources.

###### Topics

- [Creating a service-linked role for
  Amazon Lex V2](#create-slr "#create-slr")
- [Editing a service-linked role for
  Amazon Lex V2](#edit-slr "#edit-slr")
- [Deleting a service-linked role for
  Amazon Lex V2](#delete-slr "#delete-slr")
- [Service-linked role permissions for
  Amazon Lex V2](#slr-permissions "#slr-permissions")
- [Supported regions for Amazon Lex V2
  service-linked roles](#slr-regions "#slr-regions")

## Creating a service-linked role for

Amazon Lex V2

You don't need to manually create a service-linked role, because Amazon Lex V2 creates the service-linked role for you when you carry out the relevant action (see [Service-linked role permissions for
Amazon Lex V2](#slr-permissions "#slr-permissions") for more information) in the AWS Management Console, AWS CLI, or AWS API.

If you delete this service-linked role, and then need to create one
again, you can use the same process to create a new role in your account.

## Editing a service-linked role for

Amazon Lex V2

Amazon Lex V2 doesn't allow you to edit service-linked roles. After you create a service-linked role,
you can't change the name of the role because various entities might
reference the role. However, you can edit the description of a role using IAM. For more information, see [Editing a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for

Amazon Lex V2

If you no longer need to use a feature or service that requires a
service-linked role, we recommend that you delete that role. That way you
don’t have an unused entity that is not actively monitored or maintained.
However, you must clean up the resources for your service-linked role
before you can manually delete it.

###### Note

If the Amazon Lex V2 service is using the role when you try to
delete the resources, then the deletion might fail. If that happens,
wait for a few minutes and try the operation again.

To see the steps for deleting resources for specific service-linked roles in Amazon Lex V2, refer to the section specific to the role in [Service-linked role permissions for
Amazon Lex V2](#slr-permissions "#slr-permissions").

**To manually delete a service-linked role using
IAM**

After deleting resources related to a service-linked role, use the IAM console, the AWS CLI, or the AWS API to delete the role. For more information,
see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Service-linked role permissions for

Amazon Lex V2

Amazon Lex V2 uses service-linked roles with the following prefixes.

###### Topics

- [AWSServiceRoleForLexV2Bots\_](#slr-bots "#slr-bots")
- [AWSServiceRoleForLexV2Channels\_](#slr-channels "#slr-channels")
- [AWSServiceRoleForLexV2Replication](#slr-replication "#slr-replication")

### AWSServiceRoleForLexV2Bots\_

The AWSServiceRoleForLexV2Bots\_ role gives permissions to connect your bot to other required services. This role includes a trust policy to allow the lexv2.amazonaws.com service to assume the role and includes permissions to carry out the following actions.

- Use Amazon Polly to synthesize speech on all Amazon Lex V2 resources that the action
  supports.
- If a bot is configured to use Amazon Comprehend sentiment analysis, detect the sentiment on all
  Amazon Lex V2 resources that the action supports.
- If a bot is configured to store audio logs in an S3 bucket, put objects in a
  specified bucket.
- If a bot is configured to store audio and text logs, create a log stream in and put
  logs into a specified log group.
- If a bot is configured to use a AWS KMS key to encrypt data, generate a specific data
  key.
- If a bot is configured to use the `KendraSearchIntent` intent, query
  access to a specified Amazon Kendra index.

**To create the role**

Amazon Lex V2 creates a new AWSServiceRoleForLexV2Bots\_ role with a random suffix in your account each time that you [create a bot](create-bot.md "create-bot.md").
Amazon Lex V2 modifies the role when you
add additional capabilities to a bot. For example, if you [add Amazon Comprehend
sentiment analysis to a bot](sentiment.md "sentiment.md"), Amazon Lex V2 adds permission for the
`lex:DetectSentiment` action to the service role.

###### To delete the role

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. From the left navigation pane, select **Bots** and choose the bot whose service-linked role you want to delete.
3. Select any version of the bot.
4. The **IAM permissions runtime role** is in the **Version details**.
5. Return to the **Bots** page and choose the radio button next to the bot to delete.
6. Select **Action** and then choose
   **Delete**.
7. Follow the steps at [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") to delete the IAM role.

### AWSServiceRoleForLexV2Channels\_

The AWSServiceRoleForLexV2Channels\_ role gives permission to list bots in an account and to call conversation APIs for a bot. This role includes a trust policy to allow the channels.lexv2.amazonaws.com service to assume the role. If a bot is configured to use a channel to communicate with a
messaging service, the AWSServiceRoleForLexV2Channels\_ role permissions policy allows
Amazon Lex V2 to complete the following actions.

- List permissions on all bots in an account.
- Recognize text, get session and put session permissions on
  a specified bot alias.

**To create the role**

When you create a channel integration to deploy a bot on a messaging
platform, Amazon Lex V2 creates a new service-linked role in your account for
each channel with a random suffix.

###### To delete the role

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. From the left navigation pane, select **Bots**.
3. Choose a bot.
4. From the left navigation pane, choose **Channel integrations** under **Deployments**.
5. Select a channel whose service-linked role you want to delete.
6. The **IAM permissions runtime role** is in the **General configuration**
7. Choose **Delete**, then
   choose **Delete** again to delete the channel.
8. Follow the steps at [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") to delete the IAM role.

### AWSServiceRoleForLexV2Replication

The AWSServiceRoleForLexV2Replication role gives permission to replicate bots in a second region. This role includes a trust policy to allow the replication.lexv2.amazonaws.com service to assume the role and also includes the [AmazonLexReplicationPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLexReplicationPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLexReplicationPolicy") AWS managed policy, which allows permissions for the following actions.

- Pass bot IAM roles to the replica bot to reduplicate the appropriate permissions for the replica bot.
- Create and manage bots and bot resources (versions, aliases, intents, slots, custom vocabularies, and so on) in other Regions.

**To create the role**

When you enable Global Resiliency for a bot, Amazon Lex V2 creates the AWSServiceRoleForLexV2Replication service-linked role in your account. Ensure that you have the correct [permissions](gr-permissions.md "gr-permissions.md") to grant the Amazon Lex V2 service permissions to create the service-linked role.

###### To delete Amazon Lex V2 resources used by AWSServiceRoleForLexV2Replication so that you can delete the role

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. Choose a bot for which Global Resiliency is enabled.
3. Select **Global Resiliency** under **Deployment**.
4. Select **Disable Global Resiliency**.
5. Repeat the process for all bots that have Global Resiliency enabled.
6. Follow the steps at [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") to delete the IAM role.

## Supported regions for Amazon Lex V2

service-linked roles

Amazon Lex V2 supports using service-linked roles in all of the
regions where the service is available. For more information, see
[AWS Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
