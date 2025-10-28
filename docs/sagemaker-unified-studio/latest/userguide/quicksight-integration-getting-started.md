# Getting started using Amazon Quick Suite integration

1. ###### Create a Amazon SageMaker Unified Studio project with Quick Suite blueprint

You must sign in to Amazon SageMaker Unified Studio by selecting **Sign in with SSO** and
create a new project. For more information, see [Create a new project](create-new-project.md "create-new-project.md").

###### Note

When creating the project, you must choose a project profile which has
**Quick Suite** blueprint added to it.

    1. ###### Automatic resource provisioning


    When your project is created, the following resources are provisioned:




    	* One restricted Quick Suite folder per project. All new assets—like analyses,
    	 datasets, and dashboards—created using the project's data are scoped to this
    	 folder and cannot be moved outside of it. Only Amazon SageMaker Unified Studio, not end users, can grant
    	 access to this folder, enforcing centralized, policy-based control.
    	* Real-time folder permission sync. Amazon SageMaker Unified Studio keeps the Amazon Quick Suite folder's
    	 access permissions aligned with project membership. Whenever a user or group is
    	 added to or removed from the Amazon SageMaker project, those changes are reflected
    	 in the corresponding Amazon Quick Suite folder.
    	* Preconfigured Quick Suite data sources for Athena and Amazon Redshift:




    		+ If the project profile includes the *LakehouseDatabase*
    		 blueprint, an Athena data source is created.
    		+ If the project profile includes the
    		 *RedshiftServerless* blueprint, a Redshift data source is
    		 provisioned.###### Note

You can also enable Amazon QuickSight integration for existing projects in
Amazon SageMaker Unified Studio. In the current release of Amazon SageMaker Unified Studio, this is only supported for projects that
were created with a project profile where the QuickSight blueprint is added with the **On
demand** deployment setting mode. For more information, see [Amazon Quicksight in SageMaker Unified Studio](../adminguide/amazon-quicksight.md "../adminguide/amazon-quicksight.md"). If this condition is met, you can then add the Amaon QuickSight environment to the existing project by invoking the CreateEnvironment API. For more information, see [CreateEnvironment](../../../datazone/latest/APIReference/API_CreateEnvironment.md "../../../datazone/latest/APIReference/API_CreateEnvironment.md"). 2. ###### Get access to data

Before visualizing data in Quick Suite, your project must have access to the required data
assets. You can get access in the following ways:

    1. ###### Subscribe to data in Amazon SageMaker Catalog


    If the data assets are available in the catalog, you can request access to
     available data assets directly within Amazon SageMaker Unified Studio. Once approved, Amazon SageMaker Unified Studio configures
     necessary permissions. For detailed steps, see [Data discovery,
     subscription, and consumption](discover-data.md "discover-data.md").
    2. ###### Grant access through project's IAM Role


    Administrators grant access by assigning AWS Lake Formation permissions to the project's
     IAM role. This enables fine-grained control at database, table, and column level.
     For more information, see [Granting data
     permissions using the named resource method](../../../lake-formation/latest/dg/granting-cat-perms-named-resource.md "../../../lake-formation/latest/dg/granting-cat-perms-named-resource.md").
    3. ###### Create new connections


    You can create connections directly to Amazon Redshift and other third party sources like
     Oracle and Snowflake from Amazon SageMaker Unified Studio. You configure connection details and credentials
     securely and manage them within the project. For detailed steps, see [Amazon Redshift
     compute connections](compute-redshift.md "compute-redshift.md") and [Data
     connections in lakehouse architecture](lakehouse-data-connection.md "lakehouse-data-connection.md").

3. ###### Open in Quick Suite

Once your project has access to the necessary datasets, you can start building
visualizations in Amazon Quick Suite. Amazon SageMaker Unified Studio provides two integrated paths for creating Quick Suite
datasets and analyses:

    1. ###### Create a dataset manually in Quick Suite




    	1. From Project Overview, choose **Actions** and then choose
    	 **Open Quick Suite**
    	2. Choose from available data source(s) (Athena or Redshift)
    	3. Create new dataset by connecting to data source tables or views or writing
    	 custom SQL query
    This approach gives you flexibility to define datasets as needed and combine data
     from different sources within your project. For detailed steps on creating a dataset
     from an existing data source, refer to [Creating a Dataset
     Using an Existing Data Source](../../../quicksight/latest/user/create-a-data-set-existing.md "../../../quicksight/latest/user/create-a-data-set-existing.md").
    2. ###### Create dataset from Data Explorer




    	1. Navigate to **Data** tab in your project
    	2. Select table or view to visualize
    	3. Choose **Visualize in Quick Suite** under **Actions**
    When you choose this option, Amazon SageMaker Unified Studio creates a Quick Suite dataset using the selected
     table or view. The dataset is named after the table or view and is placed into the
     project's restricted folder in Quick Suite. The dataset is immediately opened in a new
     browser tab, allowing you to begin building an analysis.


    From more information on building an analysis using the newly created dataset, see
     [Working with an Analysis
     in Quick Suite](../../../quicksight/latest/user/working-with-an-analysis.md "../../../quicksight/latest/user/working-with-an-analysis.md"). For more information on joining your dataset with other datasets
     available within the project folder, see [Joining datasets in
     Quick Suite](../../../quicksight/latest/user/joining-data.md "../../../quicksight/latest/user/joining-data.md").

4. ###### Publish Quick Suite dashboards

Once a dashboard is created, it is added to the project as an asset.

###### Note

Only dashboards that are created within the **Assets** sub-folder
in Amazon QuickSight folder are added to the project.

To view the newly created dashboard assets:

    1. Navigate to your project
    2. Select **Assets** under **Project Catalog**
    3. Find **Quick Suite dashboard** listed as new asset

Dashboard assets include:

    * AWS Account
    * AWS Region
    * Creation date
    * Dashboard name
    * Last updated
    * Owner
    * Quick Suite account
    * URL

For more information on editing asset metadata, see [Updating asset
metadata](update-metadata.md "update-metadata.md").

###### Note

Dashboard subscription is not supported at this time. The
**Subscribe** button is inactive for dashboard assets.
