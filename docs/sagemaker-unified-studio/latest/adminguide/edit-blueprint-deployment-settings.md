# Edit blueprint deployment

settings

Blueprint deployment settings contain parameters used to create project profiles for
Amazon SageMaker Unified Studio projects. Complete the following procedure to edit deployment
settings for any of the supported blueprints.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and choose the domain’s name from the list.
   The name is a hyperlink.
3. Choose the **Project profiles** tab and then choose the project
   profile that contains the blueprint the deployment settings of which you want to
   modify.
4. From the **Blueprint deployment settings** list, choose the blueprint
   the deployment settings of which you want to modify. The blueprint name is a
   hyperlink.
5. On the chose blueprint's **Blueprint deployment settings summary**
   page, choose **Edit**.

You can make changes to the following:

    * The blueprint deployment settings description.
    * The AWS SSM Parameter Store path that contains parameters definition.
    * The blueprint parameters. You can use the table on this page to inspect and edit
     parameter values that will be used during project creation. To edit a parameter value,
     choose the parameter's radio button and choose **Edit**. You can
     override values that are set as blueprint or SSM values and check the
     **Editable** box if you want the values to be provided during
     project creation.
    * Notes for project owners - let project owners know why you made these changes and
     anything else they need to know about how this will impact their projects that use
     this project profile.
