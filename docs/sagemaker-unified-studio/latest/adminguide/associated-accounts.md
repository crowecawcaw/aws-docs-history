# Associated accounts in Amazon SageMaker Unified Studio

In Amazon SageMaker Unified Studio, associated accounts are other AWS accounts that can be associated with an
Amazon SageMaker unified domains so that resources can be created and accessed in these accounts
for various purposes.

Complete the following procedures to manage account associations and configure domains in
associated accounts in Amazon SageMaker Unified Studio.

###### Topics

- [Request association with other AWS
  accounts](#invite-account-to-associate "#invite-account-to-associate")
- [Accept an account association request from an
  Amazon SageMaker Unified Studio domain and enable an environment blueprint](#accept-invitation-to-associate "#accept-invitation-to-associate")
- [Reject an account association request from an
  Amazon SageMaker Unified Studio domain](#reject-invitation-to-associate "#reject-invitation-to-associate")
- [Remove an associated account in Amazon SageMaker Unified Studio](#remove-associated-account "#remove-associated-account")
- [Configure Amazon Bedrock in SageMaker Unified Studio
  in an associated account](#configure-generative-ai "#configure-generative-ai")

## Request association with other AWS

accounts

###### Note

By sending an association request to another AWS account, you are sharing your domain
with the other AWS account with AWS Resource Access Manager (RAM). Be sure to check the
accuracy of the account IDs that you enter.

Complete the following procedure to request association with other AWS accounts.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and choose an Amazon SageMaker unified domain
   name from the list. The name is a hyperlink.
3. Choose the **Account associations** tab and then choose
   **Request association**.
4. On the **Request association** page, enter the IDs of the accounts
   with which you want to associate this domain. When you are satisfied with the list of
   account IDs, choose **Request association**.

Notice that the account IDs to which you sent an association request now appear in the
list of accounts in the **Associated accounts** tab with the
**Requested** status.

## Accept an account association request from an

Amazon SageMaker Unified Studio domain and enable an environment blueprint

Complete the following procedure to accept association with an Amazon SageMaker unified
domain.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View requests** and select the inviting domain from the list
   of requests. The domain name is a hyperlink. You can also use the radio button next to the
   domain name and then choose **Review request**.
3. On the **Accept and configure AWS association page**, choose
   **Accept new permissions** to accept the association request.
4. Once the action completes and your account is associated with the inviting Amazon
   SageMaker unified domain, this domain's name appears in the **Associated
   domains** list on the **Associated domains** page. The name is
   a hyperlink. If you choose it, you then navigate to the Amazon SageMaker console for this
   domain as the associated account. You can perform the following configurations for this
   domain in your associated account:
   - Configure Data analytics and AI/ML model development capability under the
     **Next steps for your domain**. For more information, see [All capabilities project profile](all-capabilities.md "all-capabilities.md").
   - Configure Generative AI application development capability under the
     **Next steps for your domain**. For more information, see [Configure Amazon Bedrock in SageMaker Unified Studio
     in an associated account](#configure-generative-ai "#configure-generative-ai").
   - Configure SQL analytics capability under the **Next steps for your
     domain**. For more information, see [SQL analytics project profile](sql-analytics.md "sql-analytics.md").
   - View the permissions that govern the association between this account and the
     domain in the **Permissions** tab.
   - Use the **Blueprints** tab to configure blueprints that contain
     the tools, resources and parameters that are used in this account. For more
     information, see [Blueprints in Amazon SageMaker Unified Studio](blueprints.md "blueprints.md").
   - Use the **Amazon Bedrock models** tab to configure access to your
     Amazon Bedrock serverless models for this account and set the default models for the
     generative AI playground model selector in this account. For more information, see
     [Amazon Bedrock in SageMaker Unified Studio](amazon-bedrock.md "amazon-bedrock.md").

## Reject an account association request from an

Amazon SageMaker Unified Studio domain

Complete the following to reject an association request from an Amazon SageMaker unified
domain.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View requests** and select the inviting domain from the list
   of requests. The domain name is a hyperlink. You can also use the radio button next to the
   domain name and then choose **Review request**.
3. On the **Accept and configure AWS association** page, choose
   **Reject new permissions** to reject the association request.

## Remove an associated account in Amazon SageMaker Unified Studio

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and choose an Amazon SageMaker unified domain
   name from the list. The name is a hyperlink.
3. Choose the **Account associations** tab, choose the account that you
   want to disassociate, and then choose **Disassociate**. In the
   **Disassociate account** pop up window, confirm disassociation by
   typing **disassociate** in the field.

## Configure Amazon Bedrock in SageMaker Unified Studio

in an associated account

In Amazon SageMaker Unified Studio, Generative AI enables project users to explore, build, and collaborate on
generative AI applications using Amazon Bedrock foundation models and tools.

###### Important

As a user from an associated account, you can complete the procedure below to configure
the available generative AI blueprints in your associated account. However, in order to
fully use the generative AI capability in your Amazon SageMaker Unified Studio projects, you must also have the
Generative AI application development project profile created for your associated account by
the domain administrator from the AWS account that owns this domain.

In the current release of Amazon SageMaker Unified Studio, project profiles for the
domain can only be created by domain administrators from the AWS account that owns the
domain.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View associated domains** and then choose the associated
   domain where you want to configure Amazon Bedrock in SageMaker Unified Studio.
3. In the **Next steps for your associated domain** section, choose
   **Configure** next to **Generative AI**.
4. In the **Set up generative AI** page, in the **Generative AI
   blueprints** section, under **Provisioning role**, specify a
   new or existing service role that is to be used by Amazon SageMaker Unified Studio to provision and manage
   resources defined in the selected blueprints in your associated account. Enabling
   generative AI blueprints automatically configures default resources for the essential
   generative AI capabilities that projects need. The following blueprints powered by Amazon
   Bedrock are included: Chat Agents, Knowledge Bases, Guardrails, Functions, Flows, Prompts,
   and Evaluations.
5. Locate the **Default tooling blueprint deployment settings** section
   that contains the Tooling bluepring deployment settings used to create projects from this
   project profile and review them and modify the following as needed. Note that if you have
   already enabled the Tooling blueprint, you cannot use this procedure to modify any of the
   Tooling blueprint settings.
   - Under **Manage access role**, specify a service role that gives
     Amazon SageMaker Unified Studio the authorization to create and configure project resources using AWS
     CloudFormation in the project account and region. If this service role already exists
     in this AWS account, it is selected by default.
   - For the Tooling blueprint deployment account and region, note that by configuring
     Amazon Bedrock in SageMaker Unified Studio for your associated domain, you can only
     enable the Tooling blueprint in the same AWS account and region as your associated
     domain.
   - In the **Amazon S3 bucket for blueprints** section, specify an
     Amazon S3 bucket for blueprints in your AWS account.
   - In the **Networking** section, in the **Virtual private
     cloud (VPC) setting**, choose a VPC in which to provision your Amazon
     SageManker unified domain. VPCs tagged with Amazon SageMaker Unified Studio should be correctly
     configured.

   In the **Subnets** section, select at least 3 subnets in
   different **Availability Zones** that contain required VPC Endpoints.
   Private subnets are recommended, not all functionality is available when selecting
   public subnets.
   - In the **Data encryption** section, your data is encrypted by
     default with a key that AWS owns and manages for you. Encryption cannot be changed
     after the domain is created. Choose either **Use AWS owned key** (a
     key that AWS owns and manages for you) or the **Choose a different AWS KMS
     key (advanced)** (a key that you have permissions to use, or create a new
     one) and then specify an existing or create a new AWS KMS key.

6. In the **Permissions for Amazon Bedrock model access** section,
   specify the permissions for users to interact with the enabled Amazon Bedrock models. The
   system can automatically create roles to control user access and interactions with these
   models or you can specify existing roles.

For the **Model provisioning** role, you can create a new or use an
existing role. The system uses the role you specify as the provisioning role to create an
inference profile that has access to an Amazon Bedrock model in a project. The role you
specify here is used as the provisioning role for all the Amazon Bedrock models enabled
for this domain.

For the **Model consumption** role, you can create a new or use an
existing role. The system uses a consumption role to grant users access to Amazon Bedrock
models in the playground in the Amazon SageMaker Unified Studio. 7. Choose **Submit**.

Once the action is successfully completed and you've finished configuring Amazon
Bedrock in SageMaker Unified Studio for this associated account, you are redirected to the
associated domain's details page where you can find the enabled generative AI blueprints
under the **Blueprints** tab and the enabled models listed in the
**Amazon Bedrock models** tab. Note, that you can manage model access
directly from **Amazon Bedrock models** tab. For more information, see
[Amazon Bedrock in SageMaker Unified Studio](amazon-bedrock.md "amazon-bedrock.md"). Also, if you want to
publish models from your associated account, the IAM identity of the associated account
must be added to the **GenerativeAIModelGovernanceProject** project. For
more information, see [Publishing models from associated
accounts](amazon-bedrock.md#publishing-models-associated-account "amazon-bedrock.md#publishing-models-associated-account").
