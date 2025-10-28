# Amazon Quicksight in SageMaker Unified Studio

Enabling Amazon QuickSight integration in Amazon SageMaker Unified Studio allows data consumers to directly
visualize and analyze data from the SageMaker Catalog using QuickSight. With QuickSight in
Amazon SageMaker Unified Studio, users can access their data and employ the built-in business intelligence
visualization capabilities reaching a seamless data analysis workflow.

With this integration, users can go from exploring data in Amazon SageMaker Unified Studio to visualizing it in
QuickSight with a single click. Behind the scenes, Amazon SageMaker Unified Studio creates a QuickSight dataset and
organizes it in a secured folder accessible only to members within the project. Any dashboards
you build in QuickSight stay within this folder and are automatically added as assets to your
Amazon SageMaker Unified Studio project, where you can publish them to the SageMaker Catalog. From there, you can
share them with users or groups in your corporate directory for broader access—all within
Amazon SageMaker Unified Studio. This keeps your dashboards organized, discoverable, shareable, and governed, making
cross-team collaboration and asset reuse much easier.

###### Important

To enable the QuickSight blueprint in an AWS account, you must meet the following
required conditions:

- Your Amazon SageMaker unified domain and QuickSight account both must be integrated
  with AWS IAM Identity Center using the same Identity Center instance.
- Your QuickSight account must exist in the same AWS Account where you are looking to
  enable the QuickSight blueprint.

###### Enable the QuickSight blueprint

1.  Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
    navigation bar to choose the appropriate AWS Region.
2.  Choose **View domains** or **View associated domains**
    depending on whether you want to enable the Quicksight blueprint in the domain owner AWS
    account or the associated AWS account and then choose that domain by choosing its name
    from the list. The name is a hyperlink.
3.  On the domain's details page, navigate to the **Blueprints** tab.
4.  In the **Blueprints** tab, locate the **QuickSight**
    blueprint. You can either choose the radio button next to the QuickSight blueprint and then
    choose the **Enable** button. Or you can choose the
    **QuickSight** blueprint (the name is a hyperlink) and then on the
    blueprint details page, choose **Enable in this account**.
5.  On the **Enable QuickSight** page, specify the following and then
    choose **Enable blueprint**:

        * **Provisioning role** - Amazon SageMaker Unified Studio uses this role to provision and
         manage resources defined in the selected blueprints in your account. You can either
         choose the existing or create a new role. For more information, see [AmazonSageMakerProvisioning](AmazonSageMakerProvisioning.md "AmazonSageMakerProvisioning.md") role.
        * **QuickSight VPC manager role** - Amazon SageMaker Unified Studio provisions QuickSight
         to create and manage VPCs in your account using this role. You can either choose the
         existing or create a new role. For more information, see [AmazonSageMakerQuickSightVPCTRole](AmazonSageMakerQuickSightVPCRole.md "AmazonSageMakerQuickSightVPCRole.md").
        * **Authorized domain units** - these are domain units where projects
         can access resources defined by this blueprint. You can use the text field to search for
         the domain units and then the **Add** button to add them to the list of
         authorized domain units.

    Complete the following steps to add the Quicksight blueprint to an existing project profile.
    You can only do this in the domain owner AWS account.

###### Add the QuickSight blueprint to an existing project profile

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and then choose the domain that you're working
   with by choosing its name from the list. The name is a hyperlink.
3. On the domain's details page, navigate to the **Project profiles** tab
   and then choose the project profile to which you want to add the Quicksight blueprint. It
   can be either the All capabilities project profile, or the Generative AI application
   development project profile, or the SQL analytics project profile, or an existing custom
   project profile.
4. On the chosen project profile's details page, choose **Add blueprint deployment
   settings**.
5. On the Add blueprint deployment settings page, specify the following and then choose Add
   blueprint deployment settings.
   - Blueprint deployment settings name
   - Blueprint deployment settings description - optional
   - Under **Blueprint**, use the drop-down menu to choose
     **Quicksight**.
   - Deployment properties - the account and region where you want this blueprint
     deployment settings to be created. Note that the corresponding blueprint should be
     enabled in this account and region so that the blueprint deployment settings could be
     created successfully. This is also where you can specify the **Mode**,
     choosing between **On create** (deploy the blueprint deployment
     settings as soon as the project is created) or **On demand** (deploy
     blueprint deployment settings when users need it) and the deployment order.
   - AWS SSM Parameter Store path in AWS Systems Manager Parameters Store that
     contains parameters definition.
   - Blueprint parameters - these parameter values that will be used during project
     creation. You can override values that are set as blueprint or SSM values and check the
     Editable box if you want the values to be provided during project creation.

###### Note

It is recommend when you add the Quicksight blueprint to a project profile together with
at least one of the following blueprints - LakehouseDatabase, LakehouseCatalog,
RedshiftServerless. For more information, see [Blueprints in Amazon SageMaker Unified Studio](blueprints.md "blueprints.md").

If you include the above blueprint(s), it is also recommended that in the blueprint
deployment configuration, you keep the order of the Quicksight blueprint after the
LakehouseDatabase, LakehouseCatalog, RedshiftServerless blueprints.

You can also add the Quicksight blueprint to a new custom project profile. For more
information on creating custom project profiles, see [Custom project profile](custom.md "custom.md").

For information on the user flow for Quicksight in Amazon SageMaker Unified Studio, see [Amazon QuickSight in Amazon SageMaker Unified Studio](../userguide/quicksight-integration.md "../userguide/quicksight-integration.md").
