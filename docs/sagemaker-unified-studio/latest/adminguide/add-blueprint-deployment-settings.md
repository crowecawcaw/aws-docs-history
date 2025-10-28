# Add blueprint deployment settings

Blueprint deployment settings contain parameters used to create project profiles for
Amazon SageMaker Unified Studio projects. Complete the following procedure to add deployment
settings for any of the supported blueprints.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and choose the domain’s name from the list.
   The name is a hyperlink.
3. Choose the **Project profiles** tab and then choose the project
   profile that contains the blueprint to which you want to add a new deployment
   setting.
4. Choose the **Blueprints Deployment Settings** tab, and choose Add
   blueprint deployment settings.
5. On the **Add blueprint deployment settings** page, specify the
   following:
   - Blueprint deployment settings name.
   - The blueprint deployment settings description.
   - The blueprint to which these deployment settings will apply.
   - Deployment properties - the account and region where you want this blueprint
     deployment settings to be created. Note that the corresponding blueprint should be
     enabled in this account and region so that the blueprint deployment settings could be
     created successfully.
   - AWS SSM Parameter Store path in AWS Systems Manager Parameters Store that
     contains parameters definition.
   - Blueprint parameters - these parameter values that will be used during project
     creation. You can override values that are set as blueprint or SSM values and check
     the Editable box if you want the values to be provided during project creation.
   - Notes for project owners - let project owners know why you made these changes and
     anything else they need to know about how this will impact their projects that use
     this project profile.
