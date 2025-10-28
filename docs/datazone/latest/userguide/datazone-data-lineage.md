# Data lineage in Amazon DataZone

Data lineage in Amazon DataZone is an OpenLineage-compatible feature that can help you to
capture and visualize lineage events, from OpenLineage-enabled systems or through APIs,
to trace data origins, track transformations, and view cross-organizational data
consumption. It provides you with an overarching view into your data assets to see the
origin of assets and their chain of connections. The lineage data includes information
on the activities inside the Amazon DataZone's business data catalog, including information
about the catalogued assets, the subscribers of those assets, and the activities that
happen outside the business data catalog captured programmatically using the
APIs.

###### Topics

- [Types of lineage nodes in
  Amazon DataZone](#datazone-data-lineage-node-types "#datazone-data-lineage-node-types")
- [Key attributes in lineage
  nodes](#datazone-data-lineage-key-attributes "#datazone-data-lineage-key-attributes")
- [Visualizing data lineage](#datazone-data-lineage-history "#datazone-data-lineage-history")
- [Data lineage authorization in
  Amazon DataZone](#datazone-data-lineage-authorization "#datazone-data-lineage-authorization")
- [Data lineage sample
  experience in Amazon DataZone](#datazone-data-lineage-sample-experience "#datazone-data-lineage-sample-experience")
- [Enable data lineage in the management
  console](#enable-data-lineage "#enable-data-lineage")
- [Using Amazon DataZone data lineage
  programmatically](#datazone-data-lineage-apis "#datazone-data-lineage-apis")
- [Automate lineage for the AWS Glue
  catalog](#datazone-data-lineage-automate "#datazone-data-lineage-automate")
- [Automate lineage from
  Amazon Redshift](#datazone-data-lineage-automate-redshift "#datazone-data-lineage-automate-redshift")
  Lineage can be setup to be automatically captured from AWS Glue and Amazon Redshift
  databases when added to Amazon DataZone. Additionally, Spark ETL job runs in AWS Glue (v5.0
  and higher) console or notebooks can be configured to send lineage events to Amazon DataZone
  domains.

In Amazon DataZone, domain administrators can configure lineage while setting up data lake
and data warehouse build-in blueprints which ensures that all data source runs created
from those resources are enabled for automatic lineage capture.

Using Amazon DataZone's OpenLineage-compatible APIs, domain administrators and data
producers can capture and store lineage events beyond what is available in Amazon DataZone,
including transformations in Amazon S3, AWS Glue, and other services. This provides a
comprehensive view for the data consumers and helps them gain confidence of the asset's
origin, while data producers can assess the impact of changes to an asset by
understanding its usage. Additionally, Amazon DataZone versions lineage with each event,
enabling users to visualize lineage at any point in time or compare transformations
across an asset's or job's history. This historical lineage provides a deeper
understanding of how data has evolved, essential for troubleshooting, auditing, and
ensuring the integrity of data assets.

With data lineage, you can accomplish the following in Amazon DataZone:

- Understand the provenance of data: knowing where the data originated fosters
  trust in data by providing you with a clear understanding of its origins,
  dependencies, and transformations. This transparency helps in making confident
  data-driven decisions.
- Understand the impact of changes to data pipelines: when changes are made to
  data pipelines, lineage can be used to identify all of the downstream consumers
  that are to be affected. This helps to ensure that changes are made without
  disrupting critical data flows.
- Identify the root cause of data quality issues: if a data quality issue is
  detected in a downstream report, lineage, especially column-level lineage, can
  be used to trace the data back (at a column level) to identify the issue back to
  its source. This can help data engineers to identify and fix the problem.
- Improve data governance and compliance: column-level lineage can be used to
  demonstrate compliance with data governance and privacy regulations. For
  example, column-level lineage can be used to show where sensitive data (such as
  PII) is stored and how it is processed in downstream activities.

## Types of lineage nodes in

Amazon DataZone

in Amazon DataZone, data lineage information is presented in nodes that represent
tables and views. Depending on the context of the project, for example, a project
selected at the top left in the data portal, the producers are able to view both,
inventory and published assets, whereas consumers can only view the published
assets. When you first open the lineage tab in the asset details page, the
catalogued dataset node is the starting point for navigating upstream or downstream
through the lineage nodes of your lineage graph.

The following are the types of data lineage nodes that are supported in
Amazon DataZone:

- **Dataset node** - this node type includes
  data lineage information about a specific data asset.
  - Dataset nodes that include information about AWS Glue or Amazon
    Redshift assets published in the Amazon DataZone catalog are
    auto-generated and include a corresponding AWS Glue or Amazon
    Redshift icon within the node.
  - Dataset nodes that include information about assets that are not
    published in the Amazon DataZone catalog, are created manually by domain
    administrators (producers) and are represented by a default custom
    asset icon within the node.

- **Job (run) node** - this node type displays
  the details of the job, including the latest run of a particular job and run
  details. This node also captures multiple runs of the job and can be viewed
  in the **History** tab of the node details. You can view
  node details by choosing the node icon.

## Key attributes in lineage

nodes

The `sourceIdentifier` attribute in a lineage node represents the
events happening on a dataset. The `sourceIdentifier` of the lineage node
is the identifier of the dataset (table/view etc). It’s used for uniqueness
enforcement on the lineage nodes. For example, there can’t be two lineage nodes with
same `sourceIdentifier`. The following are examples of
`sourceIdentifier` values for different types of nodes:

- For dataset node with respective dataset type:
  - Asset: amazon.datazone.asset/<assetId>
  - Listing (published asset):
    amazon.datazone.listing/<listingId>
  - AWS Glue table:
    arn:aws:glue:<region>:<account-id>:table/<database>/<table-name>
  - Amazon Redshift table/view:
    arn:aws:<redshift/redshift-serverless>:<region>:<account-id>:<table-type(table/view
    etc)>/<clusterIdentifier/workgroupName>/<database>/<schema>/<table-name>
  - For any other type of dataset nodes imported using open-lineage
    run events, <namespace>/<name> of the input/output
    dataset is used as `sourceIdentifier` of the node.

- For jobs:
  - For job nodes imported using open-lineage run events,
    <jobs_namespace>.<job_name> is used as
    sourceIdentifier.

- For job runs:
  - For job run nodes imported using open-lineage run events,
    <jobs_namespace>.<job_name>/<run_id> is used as
    sourceIdentifier.

For assets created using `createAsset` API, the
`sourceIdentifier` must be updated using
`createAssetRevision` API to enable mapping the asset to upstream
resources.

## Visualizing data lineage

Amazon DataZone’s asset details page provides a graphical representation of data
lineage, making it easier to visualize data relationships upstream or downstream.
The asset details page provides the following capabilities to navigate the
graph:

- Column-level lineage: expand column-level lineage when available in
  dataset nodes. This automatically shows relationships with upstream or
  downstream dataset nodes if source column information is available.
- Column search: when the default display for number of columns is 10. If
  there are more than 10 columns, pagination is activiated to navigate to the
  rest of the columns. To quickly view a particular column, you can search on
  the dataset node that list just the searched column.
- View dataset nodes only: if you want to toggle to view only dataset
  lineage nodes and filter out the job nodes, you can choose the Open view
  control icon on the top left of the graph viewer and toggle the
  **Display dataset nodes only** option. This will remove
  all the job nodes from the graph and lets you navigate just the dataset
  nodes. Note that when the view only dataset nodes is turned on, the graph
  cannot be expanded upstream or downstream.
- Details pane: Each lineage node has details captured and displayed when
  selected.
  - Dataset node has a detail pane to display all the details captured
    for that node for a given timestamp. Every dataset node has 3 tabs,
    namely: Lineage info, Schema, and History tab. The history tab lists
    the different versions of lineage event captured for that node. All
    details captured from API are displayed using metadata forms or a
    JSON viewer.
  - Job node has a detail pane to display job details with tabs,
    namely: Job info, and History. The details pane also captures query
    or expressions captured as part of the job run. The history tab
    lists the different versions of job run event captured for that job.
    All details captured from API are displayed using metadata forms or
    a JSON viewer.

- Version tabs: all lineage nodes in Amazon DataZone data lineage have
  versioning. For every dataset node or job node, the versions are captured as
  history and that enables you to navigate between the different versions to
  identify what has changed overtime. Each version opens a new tab in the
  lineage page to help compare or contrast.

## Data lineage authorization in

Amazon DataZone

**Write permissions** - to publish lineage data into
Amazon DataZone, you must have an IAM role with a permissions policy that includes an
`ALLOW` action on the `PostLineageEvent` API. This IAM
authorization happens at API Gateway layer.

**Read permissions** - there are two operations:
`GetLineageNode` and `ListLineageNodeHistory` that are
included in the `AmazonDataZoneDomainExecutionRolePolicy` managed policy
and therefore every user in the Amazon DataZone domain can invoke these to traverse the
data lineage graph.

## Data lineage sample

experience in Amazon DataZone

You can use the data lineage sample experience to browse and understand data
lineage in Amazon DataZone, including traversing upstream or downstream in your data
lineage graph, exploring versions and column-level lineage.

Complete the followng procedure to try the sample data lineage experience in
Amazon DataZone:

1. Navigate to the Amazon DataZone data portal URL and sign in using single
   sign-on (SSO) or your AWS credentials. If you’re an Amazon DataZone
   administrator, you can navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose any available data asset to open the asset's details page.
3. On the asset's details page, choose the **Lineage** tab,
   then mouse over the information icon, and then choose **Try sample
   lineage**.
4. In the data lineage pop up window, choose **Start guided data
   lineage tour**.

At this point, a fullscreen tab that provides all the space of lineage
information is displayed. The sample data lineage graph is initially
displayed with a base node with 1-depth at either ends, upstream and
downstream. You can expand the graph upstream or downstream. The columns
information is also available for you to choose and see how lineage flows
through the nodes.

## Enable data lineage in the management

console

You can enable data lineage as part of configuring your Default Data Lake and
Default Data Warehouse blueprints.

Complete the following procedure to enable data lineage for your Default Data Lake
blueprint.

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with your
   account credentials.
2. Choose **View domains** and choose the domain where you
   want to enable data lineage for your DefaultDataLake blueprint.
3. On the domain details page, navigate to the
   **Blueprints** tab.
4. On the DefaultDataLake blueprint's details page, choose the
   **Regions** tab.
5. You can enable data lineage as part of adding a region for your
   DefaultDataLake blueprint. So if a region is already added but the data
   lineage functionality in it is not enabled (**No** is
   displayed in the **Import data lineage** column, you must
   first remove this region. To enable data lineage, choose **Add
   region**, then choose the region you want to add, and make sure
   to check the **Enable importing data lineage** checkbox in
   the **Add Region** pop up window.

To enabled data lineage for your DefaultDataWarehouse blueprint, complete the
following procedure.

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with your
   account credentials.
2. Choose **View domains** and choose the domain where you
   want to enable data lineage for your DefaultDataWarehouse blueprint.
3. On the domain details page, navigate to the
   **Blueprints** tab.
4. On the DefaultDataWarehouse blueprint's details page, choose the
   **Parameter sets** tab.
5. You can enable data lineage as part of adding a parameter set for your
   DefaultDataWarehouse blueprint. To do so, choose **Create parameter
   set**.
6. On the **Create parameter set** page, specify the
   following and then choose **Create parameter set**.
   - Name for the parameter set.
   - Description for the parameter set.
   - AWS Region where you want to create environments.
   - Specify whether Amazon DataZone is to use these parameters to establish
     a connection to your Amazon Redshift cluster or serverless
     workgroup.
   - Specify an AWS secret.
   - Specfy either a cluster or serverless workgroup that you want to
     use when creating environments.
   - Specify the name of the database (within the cluster or workgroup
     you specified) that you want to use when creating
     environments.
   - Under **Import data lineage**, check the
     **Enable importing data lineage**.

## Using Amazon DataZone data lineage

programmatically

To use the data lineage functionality in Amazon DataZone, you can invoke the following
APIs:

- [GetLineageNode](../APIReference/API_GetLineageNode.md "../APIReference/API_GetLineageNode.md")
- [ListLineageNodeHistory](../APIReference/API_ListLineageNodeHistory.md "../APIReference/API_ListLineageNodeHistory.md")
- [PostLineageEvent](../APIReference/API_PostLineageEvent.md "../APIReference/API_PostLineageEvent.md")

## Automate lineage for the AWS Glue

catalog

As and when AWS Glue databases and tables are added to the Amazon DataZone catalog,
the lineage extraction is automated for those tables using data source runs. There
are few ways lineage is automated for this source:

- Blueprint configuration - administrators setting up blueprints can
  configure blueprints to capture lineage automatically. This enables the
  administrators to define which data sources are important for lineage
  capture rather than relying on data producers cataloguing data. For more
  information, see [Enable data lineage in the management
  console](#enable-data-lineage "#enable-data-lineage").
- Data source configuration - data producers, as they configure data source
  runs for AWS Glue databases, are presented with a view along with Data
  Quality to inform about automated data lineage for that data source.
  - The lineage setting can be viewed in the **Data Source
    Definition** tab. This value is not editable by data
    producers.
  - The lineage collection in Data Source run fetches information from
    table metadata to build lineage. AWS Glue crawler supports
    different types of sources and the sources for which lineage is
    captured as part of the Data Source run include Amazon S3, DynamoDB,
    Catalog, Delta Lake, Iceberg tables, and Hudi tables stored in
    Amazon S3. JDBC and DocumentDB or MongoDB are current not supported
    as sources.
  - Limitation - it the number of tables is more than 100, the lineage
    run fails after 100 tables. Make sure the AWS Glue crawler is not
    configured to bring in more that 100 tables in a run.

- AWS Glue (v5.0) configuration - while running AWS Glue jobs in AWS
  Glue Studio, data lineage can be configured for the jobs to send lineage
  events directly to Amazon DataZone domain.
  1.  Navigate to the AWS Glue console at
      https://console.aws.amazon.com/gluestudio and sign in with your
      account credentials.
  2.  Choose **ETL jobs** and either create a new job
      or click on any of the existing jobs.
  3.  Go to **Job details** (including ETL Flows job)
      tab and scroll down to Generate lineage events section.
  4.  Select the checkbox to enable sending lineage events and that
      expands to display an input field to enter the Amazon DataZone
      Domain ID.

- AWS Glue (V5.0) Notebook configuration - in a notebook, you can automate
  the collection of Spark executions by adding a %%configure magic. This
  configuration will send events to Amazon DataZone domain.

```

%%configure --name project.spark -f
{
    "--conf":"spark.extraListeners=io.openlineage.spark.agent.OpenLineageSparkListener --conf spark.openlineage.transport.type=amazon_datazone_api --conf spark.openlineage.transport.domainId={DOMAIN_ID}  --conf spark.glue.accountId={ACCOUNT_ID} --conf spark.openlineage.facets.custom_environment_variables=[AWS_DEFAULT_REGION;GLUE_VERSION;GLUE_COMMAND_CRITERIA;GLUE_PYTHON_VERSION; --conf spark.glue.JOB_NAME={JOB_NAME}"
}

```

The following are the parameter details:

    + `spark.extraListeners=io.openlineage.spark.agent.OpenLineageSparkListener`
     - OpenLineageSparkListener will be created and registered with
     Spark's listener bus
    + `spark.openlineage.transport.type=amazon_datazone_api`
     - This is an OpenLineage specification to tell the OpenLineage
     Plugin to use DataZone API Transport to emit lineage events to
     DataZone’s PostLineageEvent API. For more information, see [https://openlineage.io/docs/integrations/spark/configuration/spark\_conf](https://openlineage.io/docs/integrations/spark/configuration/spark_conf "https://openlineage.io/docs/integrations/spark/configuration/spark_conf")
    + `spark.openlineage.transport.domainId={DOMAIN_ID}` -
     This parameter establishes the domain to which the API transport
     will submit the lineage events to.
    + `spark.openlineage.facets.custom_environment_variables
     [AWS_DEFAULT_REGION;GLUE_VERSION;GLUE_COMMAND_CRITERIA;GLUE_PYTHON_VERSION;]`
     - The following environment variables (AWS\_DEFAULT\_REGION ,
     GLUE\_VERSION , GLUE\_COMMAND\_CRITERIA, and GLUE\_PYTHON\_VERSION),
     which Glue interactive session populates, will be added to the
     LineageEvent
    + `spark.glue.accountId=<ACCOUNT_ID>` - Account Id
     of the Glue Data Catalog where the metadata resides. This account id
     is used to construct Glue ARN in lineage event.
    + `spark.glue.JOB_NAME` - Job name of the lineage event.
     The job name in notebook can be set as `spark.glue.JOB_NAME:
     ${projectId}.${pathToNotebook}`.

- Set up parameters to configure communication to Amazon DataZone from AWS
  Glue

Param key: --conf

Param value:

```

spark.extraListeners=io.openlineage.spark.agent.OpenLineageSparkListener
--conf spark.openlineage.transport.type=amazon_datazone_api
--conf spark.openlineage.transport.domainId=<DOMAIN_ID>
--conf spark.openlineage.facets.custom_environment_variables=[AWS_DEFAULT_REGION;GLUE_VERSION;GLUE_COMMAND_CRITERIA;GLUE_PYTHON_VERSION;]
--conf spark.glue.accountId=<ACCOUNT_ID> (replace <DOMAIN_ID> and <ACCOUNT_ID> with the right values)

```

For Notebooks add these additinal parameters:

```

--conf spark.glue.JobName=<SessionId> --conf spark.glue.JobRunId=<SessionId or NONE?>
replace <SessionId> and <SessionId> with the right values

```

## Automate lineage from

Amazon Redshift

Capturing lineage from Amazon Redshift service with data warehouse blueprint
configuration setup by administrators, lineage is automatically captured by Amazon
DataZone. The lineage runs captures queries executed for a given database and
generates lineage events to be stored in Amazon DataZone to be visualized by data
producers or consumers when they go to a particular asset.

Lineage can be automated using the following configurations:

- Blueprint configuration: administrators setting up blueprints can
  configure blueprints to capture lineage automatically. This enables the
  administrators to define which data sources are important for lineage
  capture rather than relying on data producers cataloguing data. To setup, go
  to [Enable data lineage in the management
  console](#enable-data-lineage "#enable-data-lineage").
- Data source configuration: data producers, as they configure data source
  runs for Amazon Redshift databases, are presented with automated data
  lineage setting for that data source.

The lineage setting can be viewed in the **Data Source
Definition** tab. This value is not editable by data producers.
