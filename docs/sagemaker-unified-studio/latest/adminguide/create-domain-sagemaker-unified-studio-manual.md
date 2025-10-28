# Create a Amazon SageMaker Unified Studio domain -

manual setup

Complete the following procedure to create a Amazon SageMaker Unified Studio domain with the quick setup option.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **Create a Unified Studio domain** and then choose
   **Manual setup**.

With this option, you're choosing to create an Amazon SageMaker unified domain and
your'e claiming full control over customizing your domain settings, including the
following:

    * Customize data analytics, machine learning, SQL, Generative AI, and more
    * Data and AI governance
    * Configure Amazon Bedrock generative AI playgrounds and application
     development
    * Amazon Q - Free tier
    * Authentication via AWS IAM, AWS IAM Identity Center, or SAML

3. In **Name**, specify the domain name.
4. In **Description**, specify the domain description.
5. Under **Permissions**, specify the domain execution role. For more
   information, see [AmazonSageMakerDomainExecution
   role](AmazonSageMakerDomainExecution.md "AmazonSageMakerDomainExecution.md").
6. Under **Permissions**, specify the domain service role. For more
   information, see [AmazonSageMakerDomainService role](AmazonSageMakerDomainService.md "AmazonSageMakerDomainService.md").
7. Under **Data encryption**, specify the data encryption settings. Your
   data is encrypted by default with a key that AWS owns and manages for you. To choose a
   different key, customize your encryption settings.
8. Under **Tags**, specify the tags for your domian.
9. Choose **Create domain**.
   Once your domain is created, you can proceed to customizing your domain settings,
   including [SSO](user-management.md "user-management.md"), [project
   profiles](project-profiles.md "project-profiles.md"), [blueprints](blueprints.md "blueprints.md"), [account associations](associated-accounts.md "associated-accounts.md"), [Amazon Bedrock models](amazon-bedrock.md "amazon-bedrock.md"), [connections](git-connections.md "git-connections.md"), and [AmazonQ](amazonq.md "amazonq.md").
