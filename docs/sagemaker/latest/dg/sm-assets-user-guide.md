# Work with assets (user guide)

Use SageMaker Assets to seamlessly collaborate on machine learning projects with other
individuals in your organization. With SageMaker Assets, you and your collaborators create and
share models and data tables with each other. Within SageMaker Assets, these models and data
tables are known as _assets_.

SageMaker Assets is a feature within Amazon SageMaker Studio. You or your administrator create a
Studio environment within an Amazon DataZone project. For more information about setting
up Amazon DataZone, see [Set up SageMaker Assets (administrator guide)](sm-assets-set-up.md "sm-assets-set-up.md").

Assets are ML assets or data assets. ML assets are metadata that point to the
following:

- Feature Store feature groups
- SageMaker AI model groups
  The underlying model groups and feature groups are the sources of data. If you update
  a feature group or model group, the asset for the model group or feature group gets
  updated within the day.

Data assets are metadata that point to the following:

- Amazon Redshift tables
- AWS Glue tables
  For data assets, the data source is the mechanism that pulls metadata from the AWS Glue
  tables and Amazon Redshift tables into the asset. For example, a data source pulls the metadata
  from an AWS Glue table into the asset for that table.

You can make an asset visible to everyone in your organization by publishing it.
Individuals can review the metadata in the asset and request access. If you provide
access, they get access to the underlying machine learning source of data or
table.

Your administrator has likely given you access to the feature groups, model groups,
and tables. If they haven't, see the information in [Set up SageMaker Assets (administrator guide)](sm-assets-set-up.md "sm-assets-set-up.md") to help you get started.

The following sections provide reference information for feature groups and model
groups.

Amazon SageMaker Feature Store provides a centralized location to help you store and manage your
features. It's a highly performant repository that you can use for feature
engineering.

Within Feature Store, features are stored in a feature group. A feature group is a
collection of features related to a project that you're working on. For example,
if you're working on a project related to predicting housing prices, a feature
group might include features such as location or number of bedrooms.

For more information about how you can use feature groups to streamline the
process of feature engineering, see [Create, store, and share features with Feature Store](feature-store.md "feature-store.md").

You can use SageMaker AI model groups within SageMaker Model Registry to organize and
manage different versions of your models. You can compare the different versions
of the models to see which one performs best for your use case. For more
information about SageMaker Model Registry, see [Model Registration Deployment with Model Registry](model-registry.md "model-registry.md").

The following is background information on Amazon Redshift and AWS Glue.

Amazon Redshift is a large scale data warehousing service that provides fast query performance on
large datasets. For more information about Amazon Redshift, see [Amazon Redshift Serverless](../../../redshift/latest/gsg/new-user-serverless.md "../../../redshift/latest/gsg/new-user-serverless.md").

AWS Glue is an extract, transform, load (ETL) service that you can use to simplify
the process of data preparation. For more information about AWS Glue, see [What is
AWS Glue?](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md")

You can use the SQL editor to connect AWS Glue and Amazon Redshift databases and run queries. You
can share any tables that you create in the editor within SageMaker Assets. For more information,
see [Data preparation with SQL in Studio](sagemaker-sql-extension.md "sagemaker-sql-extension.md").

###### Topics

- [Terminology and Concepts](#sm-assets-terminology "#sm-assets-terminology")
- [Step 1: Access SageMaker Assets](#sm-assets-access "#sm-assets-access")
- [Step 2: Share assets and manage access to
  them](#sm-assets-share "#sm-assets-share")
- [Step 3: Manage access requests](#sm-assets-manage-requests "#sm-assets-manage-requests")
- [Step 4: Find assets and request access to
  them](#sm-assets-request-access "#sm-assets-request-access")
- [Step 5: Use a shared asset in your machine
  learning workflows](#sm-assets-consume "#sm-assets-consume")

## Terminology and Concepts

Before you get started with using SageMaker Assets, it's helpful to familiarize yourself
with the following terminology and concepts:

- Asset – The metadata that points to the models or data tables that
  you're sharing. You either request access to an asset that someone else owns
  or share your asset with others. You and your teammates access the asset and
  the underlying data table or model associated with it.
- Subscribed assets – To request access to an asset, you submit a
  subscription request. If your request is approved, the asset appears under
  your subscribed assets.
- Owned assets – The assets that you've shared with your teammates.
- Asset catalog – The assets that you've shared across your
  organization.

## Step 1: Access SageMaker Assets

Access SageMaker Assets to view your assets and share them with others. Use the following
information to help you get started with using it.

You access SageMaker Assets from a _project_ within an Amazon DataZone domain.
A project is a collaboration between you and your team members. Within the project,
you and the other members of your project have access to the assets that you and
your other team members create within the inventory catalog. You can publish the
assets to the published catalog to make them visible to other individuals in your
organization.

Those individuals can request access to your asset. If you provide them with
access, they can get access to the updated source of data. For example, if an
individual subscribes to an AWS Glue table that you update, they can access the updated
AWS Glue table in real time.

Use the following procedure to access SageMaker Assets.

###### To access SageMaker Assets

1. Open the [Amazon DataZone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone")
   console.
2. Choose **View domains**.
3. Next to the domain containing your project, choose **Open data
   portal**.
4. Under **Analytics Tools**, choose **SageMaker AI
   Studio**.
5. Choose **Open Amazon SageMaker AI**.
6. Choose **Assets**.

The assets that have been shared with you are under **Subscribed
assets**. The assets that you and your project members create are under
**Owned assets**. The assets that you and the other members of
your organization have published are in the **Assets
catalog**.

## Step 2: Share assets and manage access to

them

After you create machine learning models, feature groups, or data tables, you can
make them visible to the individuals collaborating with you on your project or your
organization more broadly. You can respond to requests for access to the asset. If
you approve an individual's request, they can modify the asset's underlying source
of data.

When you're sharing an asset, you have two options:

- Publish to asset catalog – Make the asset visible to everyone in
  your organization
- Publish to inventory – Make the asset visible to everyone working on
  your project

If you've published your asset to the asset catalog, individuals in your
organization can find it in the assets catalog. They can view your asset's metadata
and decide if they want to request access to them. If you approve their request,
they get access to the underlying source of data.

If you publish to inventory, you and the other members of your project can access
the asset without any additional action.

Assets published to the inventory only appear under **Owned
assets**. Assets published to the catalog appear under **Owned
assets** and **Assets catalog**.

When you publish a data table, you must create a data source that pulls the
metadata from the underlying AWS Glue table or Amazon Redshift table into the asset. Use the
following procedures to publish a AWS Glue or Amazon Redshift table.

Publish an AWS Glue table
To publish an asset for an AWS Glue table, you create a data source for
it and publish it. A data source is the mechanism that pulls the
metadata from the AWS Glue table into the asset.

Use the following procedure to publish an AWS Glue table.

###### To publish a AWS Glue table

1. Navigate to the **SageMaker Assets** landing
   page.
2. Select **Owned assets**.
3. Choose **View data sources**.
4. Choose **Create data source**.
5. For **Name**, specify a name for the data
   source.
6. For **Description**, provide a
   description.
7. For **Type**, select
   **AWS Glue**.
8. For **Data selection**, select the database
   containing the AWS Glue table.
9. For **Table selection criteria**, specify the
   name of the table.

###### Note

Even though you can specify more than one table, we
strongly suggest providing only one table name. 10. Choose **Next**. 11. _ For **Publish asset to the catalog**,
select **Yes** to publish to the asset
catalog.
_ For **Publish asset to the catalog**,
select **No** to publish to the asset
catalog. 12. Choose **Next**. 13. Under **Asset details**, choose **Run
on a schedule** or **Run on
demand** to determine how the metadata from the
AWS Glue table is pulled into the asset. 14. (Optional) If you choose **Run on a
schedule**, specify the schedule that pulls the
metadata into the asset. 15. Choose **Next**. 16. Choose **Create**. 17. (Optional) If you haven't created a schedule, choose
**Run** to bring the metadata from the
AWS Glue table into the asset.

Publish an Amazon Redshift table
To publish an asset for an Amazon Redshift table, you create a data source for it
and publish it. A data source is the mechanism that pulls the metadata
from the Amazon Redshift table into the asset.

Use the following procedure to publish an Amazon Redshift table.

###### To publish an Amazon Redshift table

1. Navigate to the **SageMaker Assets** landing
   page.
2. Select **Owned assets**.
3. Choose **View data sources**.
4. Choose **Create data source**.
5. For **Name**, specify a name for the data
   source.
6. For **Description**, provide a
   description.
7. For **Type**, select
   **Amazon Redshift**.
8. - Select **Redshift cluster**.
     1. For **Redshift cluster**,
        specify the name of the Amazon Redshift cluster containing
        the database for the table.
     2. For **Secret**, specify the
        name of the AWS Secrets Manager secret containing the
        credentials for the cluster.

   - Select **Redshift
     serverless**.
     1. For **Redshift workgroup**,
        specify the name of the Amazon Redshift workgroup containing
        the database for the table.
     2. For **Secret**, specify the
        name of the AWS Secrets Manager secret containing the
        credentials for the workgroup.

9. For **Publish source selection**, select the
   database containing the Amazon Redshift table.
10. For **Table selection criteria**, specify the
    name of the table.

###### Note

Even though you can specify more than one table, we
strongly suggest providing only one table name. 11. Choose **Next**. 12. _ For **Publish asset to the catalog**,
select **Yes** to publish to the asset
catalog.
_ For **Publish asset to the catalog**,
select **No** to publish to the asset
catalog. 13. Choose **Next**. 14. Under **Asset details**, choose **Run
on a schedule** or **Run on
demand** to determine how the metadata from the
Amazon Redshift table is pulled into the asset. 15. (Optional) If you choose **Run on a
schedule**, specify the schedule that pulls the
metadata into the asset. 16. Choose **Next**. 17. Choose **Create**. 18. (Optional) If you haven't created a schedule, choose
**Run** to bring the metadata from the Amazon Redshift
table into the asset.

Use the following procedures to publish an asset for a feature group or model
package group.

Publish a feature group
Use the following procedure to navigate to a feature group that you've
created and publish it to your owned assets or asset catalog.

###### To publish the feature group to your owned assets or asset

catalog

1. Within Studio, select **Data** on the
   left hand navigation.
2. Select the feature group that you're publishing.
3. Choose the
   ![Three dots next to the feature group.](/images/sagemaker/latest/dg/images/sm-assets-publish-icon.png)
   icon.
4. - Select **Publish to asset catalog**
     to publish to the asset catalog.
   - Select **Publish to inventory** to
     publish to the owned assets of your group.

Publish a model group
Use the following procedure to navigate to a model group that you've
created and publish it to your owned assets or asset catalog.

###### To publish the model group to your owned assets or asset

catalog

1. Within Studio, select **Models** on the
   left hand navigation.
2. Select the model group that you're publishing.
3. Choose the
   ![Three dots next to the model group.](/images/sagemaker/latest/dg/images/sm-assets-publish-icon.png)
   icon.
4. - Select **Publish to asset catalog**
     to publish to the asset catalog.
   - Select **Publish to inventory** to
     publish to the owned assets of your group.

Use the following procedure to publish an asset from your owned assets to the
asset catalog.

###### To publish an asset from the SageMaker Assets page

1. Within Studio, navigate to **Assets**.
2. Select **Owned assets**.
3. Specify the name of your asset in the search bar.
4. Choose the asset.
5. Choose **Publish**.

You can use the following SageMaker Python SDK code to publish a feature group or
model package group. The code assumes that you've already created the feature group
or model package group.

```

from sagemaker.asset import AssetManager

publisher = AssetPublisher()
publisher.publish_to_catalog(`name-of-your-feature-group-or-model-package`)

```

## Step 3: Manage access requests

After you've published an asset, users outside of your project might want to
access it. You can provide, reject, or revoke access requests. You can also delete
assets to only make the underlying source of data only available to yourself.

Use the following procedure to respond to subscription requests.

###### To approve subscription requests

1. Navigate to the **SageMaker Assets** page.
2. Choose **Manage asset assets**.
3. Select **Incoming subscription requests**.
4. - (Optional) Choose **Approve** and provide
     reason.
   - (Optional) Choose **Reject**.

You can revoke access to an asset that you've previously approved. If you choose
to revoke access, users lose access to both the asset and the underlying asset.
source. Use the following procedure to revoke access.

###### To revoke access

1. Navigate to the **SageMaker Assets** page.
2. Choose **Manage asset assets**.
3. Select **Incoming subscription requests**.
4. Select the **Approved** tab.
5. Choose **Revoke** next to the asset.

You can also unpublish assets, making them only show up as owned assets. The
assets won't be visible in the resouce catalog, but the individuals whose
subscription requests you've approved can still access them.

###### To unpublish an asset

1. Navigate to the **SageMaker Assets** page.
2. Under **Owned assets**, select the asset that you're
   unpublishing.
3. Choose **Unpublish**.

You can also delete assets from the same page where you unpublish them. Deleting
an asset doesn't delete the source of data. Asset deletion only makes the asset
invisible to the other members of your project or organization.

## Step 4: Find assets and request access to

them

You can request access to assets that other users have published to the resource
catalog. If they approve the subscription request, you get access to the underlying
source of data.

At the top of the SageMaker Assets page, you can specify a search query to find assets that
other users in your organization have published. You can also select an asset type
to view all the published assets of that type. For example, you can select
**Glue Table** to view all of the published AWS Glue
tables.

You can also view the asset type directly under the name of the asset. The
following are the available names for the asset types:

- Redshift table
- Glue table
- Models
- Feature group

###### Note

Feature groups in the following stores have the type of **Glue
table**:

- Offline
- Offline and online

###### To make a subscription request

1. Navigate to the **SageMaker Assets** page.
2. - In the search bar, specify the name of the asset and choose
     **Search**.
   - For **Types**, select the asset type and find an
     asset that you're accessing within the resource catalog.
3. Choose the asset.
4. Choose **Subscribe**.
5. Provide a reason for the request.
6. Choose **Submit**.

Your subscription request appears under **Outgoing subscription
requests** under **Manage asset requests**. If the
publisher of the asset approves your request, it appears under **Subscribed
assets**. You can now use the Amazon Redshift, AWS Glue table, or ML source of data
in your machine learning workflows.

## Step 5: Use a shared asset in your machine

learning workflows

If your subscription request to an asset is approved, you can use it in your
machine learning workflows.

The feature groups to which you've been given access appear in your list of
feature groups in Studio.

The model groups to which you've been given access appear in your list of model
groups in Studio. You can open your model group in model registry from SageMaker Assets.
Use the following procedure to open the model group within model registry.
**Subscribed assets**.

###### To open a model group from SageMaker Assets

1. Select the model group.
2. Choose **Open in Model Registry**.

You can access AWS Glue or Amazon Redshift tables in Data Wrangler within SageMaker Canvas. SageMaker Canvas is an application
that lets you perform exploratory data analysis (EDA) and train models without code.
For more information about SageMaker Canvas, see [Amazon SageMaker Canvas](canvas.md "canvas.md").

You can also bring the data from your AWS Glue or Amazon Redshift tables into your Jupyter
notebooks by using the SQL extension. You can convert your data into pandas
dataframes for your machine learning workflows. For more information, see [Data preparation with SQL in Studio](sagemaker-sql-extension.md "sagemaker-sql-extension.md").
