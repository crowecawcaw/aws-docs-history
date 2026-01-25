# Grant access for approved subscriptions to

unmanaged assets in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio enables users to publish any type of asset in the Amazon SageMaker Catalog. For some of
these assets, Amazon SageMaker Unified Studio can can automatically manage access grants. These assets are called
**managed assets** and include Lake Formation-managed AWS Glue Data
Catalog tables and Amazon Redshift tables and views. All other assets to which Amazon SageMaker Unified Studio can't
automatically grant subscriptions are called **unmanaged**.

Amazon SageMaker Unified Studio provides a path for you to manage access grants for your unmanaged assets. When
a subscription to an asset in the Amazon SageMaker Catalog is approved by the data owner, Amazon SageMaker Unified Studio
publishes an event in Amazon EventBridge in your account along with all the necessary
information in the payload that enables you to create the access grants between the source and
the target. When you receive this event, you can trigger a custom handler which can use the
information in the event to create necessary grants or permissions. After you have granted the
access, you can report back and update the status of the subscription in Amazon SageMaker Unified Studio so that it
can notify the user(s) who subscribed to the asset that they can start consuming the asset.

## Set up Cross-Region Subscriptions

Cross-region subscriptions allow data consumers to subscribe to and access data assets published in a different AWS Region than their consuming project or environment.

With cross-region subscriptions, you can:

- Subscribe to data published in a different Region than your consuming environment
- Extend existing approved subscriptions to another Region

For AWS Glue assets, cross-region access is achieved through resource links. The original table remains in the source Region, and a resource link is created in the target Region for consumer access.

For Amazon Redshift assets, cross-region data sharing uses Redshift's native datashare functionality. For cross-account scenarios, AWS Resource Access Manager (AWS RAM) authorization is required.

### Supported assets and Regions

Cross-region subscriptions support AWS Glue tables, AWS Glue views, Amazon Redshift tables, and Amazon Redshift views across all standard (non-opt-in) AWS Regions. Cross-region subscriptions to opt-in Regions are not supported.

### Prerequisites

Before you enable cross-region subscriptions, you must have the following:

- An existing Amazon DataZone or SageMaker Unified Studio domain
- Permissions to manage blueprints, environments, and projects in your domain
- For Glue assets: The appropriate data lake blueprint enabled in both source and target Regions
- For Redshift assets: The appropriate data warehouse blueprint enabled in both source and target Regions

### Enabling cross-region subscriptions (DataZone domains - V1)

Complete the following steps to enable cross-region subscriptions in DataZone domains.

#### Step 1: Enable the blueprint in the target Region

1. Open the Amazon DataZone console at [https://console.aws.amazon.com/datazone/](https://console.aws.amazon.com/datazone/ "https://console.aws.amazon.com/datazone/").
2. Choose your domain.
3. In the navigation pane, choose **Blueprints**.
4. Choose the appropriate blueprint:
   - For Glue assets, choose **DataLake**
   - For Redshift assets, choose **DataWarehouse**

5. If the blueprint is disabled, choose **Enable**.

#### Step 2: Create an environment profile

1. Sign in to the Amazon DataZone data portal.
2. Navigate to the subscriber project.
3. Choose **Create environment profile**.
4. For **Region**, select the Region that you enabled in Step 1.
5. Configure other settings as needed, and then choose **Create**.

#### Step 3: Create an environment

1. In the subscriber project, choose **Environments**.
2. Choose **Create environment**.
3. For **Environment profile**, select the environment profile that you created in Step 2.
4. Configure other settings as needed, and then choose **Create**.

#### Step 4: Subscribe to assets

1. Navigate to the data catalog and find the asset that you want to subscribe to.
2. Choose **Subscribe**.
3. Select the subscriber project with the cross-region environment.
4. Complete the subscription request.

The subscription automatically fulfills to the new Region. You can query the data from the new Region environment.

### Enabling cross-region subscriptions (SageMaker Unified Studio domains - V2)

Complete the following steps to enable cross-region subscriptions in SageMaker Unified Studio domains.

#### Step 1: Enable the blueprints in the target Region

1. Open the SMUS portal.
2. Choose your domain.
3. In the navigation pane, choose **Blueprints**.
4. Enable the **Tooling** blueprint in the target Region. This is required for both Glue and Redshift assets.
5. Enable the appropriate asset blueprint in the target Region:
   - For Glue assets, choose **LakeHouseDatabase**
   - For Redshift assets, choose **RedshiftServerless**
   - **Tooling** (required)

6. Add the target Regions to each blueprint.

#### Step 2: Create a project profile

1. In the navigation pane, choose **Project profiles**.
2. Choose **Create project profile**.
3. For **Region**, select the Region that you enabled in Step 1.
4. Configure other settings as needed, and then choose **Create**.

#### Step 3: Create a project

1. On SMUS, Choose **Create project**.
2. For **Project profile**, select the project profile that you created in Step 2.
3. Configure other settings as needed, and then choose **Create**.

The project is provisioned in the target Region. Subscriptions to this project automatically fulfill to the target Region.

### Considerations

When working with cross-region subscriptions, keep the following in mind:

- **Region restrictions** – Cross-region subscriptions are not supported in opt-in Regions.
- **Blueprint requirements** – Blueprints must be enabled in both the source and target Regions before you can create cross-region subscriptions.
- **Environment requirements (V1)** – Environments must exist in the target Region before subscriptions can be fulfilled to that Region.
- **Project requirements (V2)** – In SageMaker Unified Studio domains, you cannot add new environments to existing projects through the console. To subscribe to assets in a new Region, you must create a new project with a project profile configured for that Region.
- **Tooling blueprint (V2)** – The Tooling blueprint must be enabled in the target Region before enabling LakeHouseDatabase or RedshiftServerless blueprints.
- **Cross-account Redshift sharing** – For cross-account Redshift data sharing, AWS RAM authorization is required on both the producer and consumer sides.
