

# Using service roles for Amazon Lex V2
<a name="using-service-roles"></a>

Amazon Lex V2 uses an IAM [service role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-role) to access other AWS services on your behalf at runtime. The service role provides the permissions needed to build and run your bot. A service role is a standard customer-managed IAM role in your account. It respects the service control policies (SCPs) that you configure in AWS Organizations and gives you full control over the permissions that Amazon Lex V2 uses.

## AmazonLexServiceRole-
<a name="service-role-permissions"></a>

The AmazonLexServiceRole- role gives permissions to connect your bot to other required services. This role includes a trust policy to allow the lexv2.amazonaws.com service to assume the role and includes permissions to carry out the following actions.
+ If a bot is configured to use text-to-speech, use Amazon Polly to synthesize speech on all Amazon Lex V2 resources that the action supports.
+ If a bot is configured to use Amazon Comprehend sentiment analysis, detect the sentiment on all Amazon Lex V2 resources that the action supports.
+ If a bot is configured to store audio logs in an S3 bucket, put objects in a specified bucket.
+ If a bot is configured to store audio and text logs, create a log stream in and put logs into a specified log group.
+ If a bot is configured to use a AWS KMS key to encrypt data, generate a specific data key.
+ If a bot is configured to use Amazon Bedrock generative AI features, invoke the specified Amazon Bedrock models, inference profiles, and knowledge bases.

### Creating the role
<a name="service-role-create"></a>

Amazon Lex V2 creates a new AmazonLexServiceRole- role with a random suffix in your account when you create a bot and choose to create a new role. Amazon Lex V2 modifies the role when you add additional capabilities to a bot. For example, if you add Amazon Comprehend sentiment analysis to a bot, Amazon Lex V2 adds permission for the `comprehend:DetectSentiment` action to the service role.

You can also choose an existing IAM role that you have created and configured yourself, as long as it trusts the Amazon Lex V2 service principal (`lexv2.amazonaws.com`).

### Editing or deleting the role
<a name="service-role-edit-delete"></a>

Because a service role is a standard customer-managed IAM role, you manage it the same way as any other IAM role. Use the IAM console, the AWS CLI, or the IAM API. You can review the role's trust policy and attached permissions policies at any time in the IAM console.

**Important**  
Before you delete a service role, make sure that no bots are still using it. Deleting a role that a bot depends on causes the bot to lose the permissions it needs to run.

## Supported Regions for Amazon Lex V2 service roles
<a name="service-role-regions"></a>

Amazon Lex V2 supports using service roles in all of the Regions where the service is available. For more information, see [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).