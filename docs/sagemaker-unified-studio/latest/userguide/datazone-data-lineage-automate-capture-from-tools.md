# Automate lineage

capture from tools

###### Topics

- [Capture
  lineage for Spark executions in Visual ETL](#datazone-data-lineage-automate-capture-from-tools-vetl "#datazone-data-lineage-automate-capture-from-tools-vetl")
- [Capture lineage for AWS Glue Spark executions in Notebooks](#datazone-data-lineage-automate-capture-from-tools-gluenotebook "#datazone-data-lineage-automate-capture-from-tools-gluenotebook")
- [Capture lineage EMR-S Spark executions from Notebooks](#datazone-data-lineage-automate-capture-from-tools-emrnotebook "#datazone-data-lineage-automate-capture-from-tools-emrnotebook")

## Capture

lineage for Spark executions in Visual ETL

When a new job is created in Visual ETL in Amazon SageMaker Unified Studio, lineage is automatically
enabled. When a Visual ETL flow is created, lineage capture for that ETL flow is
automatically enabled when you hit **Save to
Project**. For every flow to capture lineage automatically, select
**Save to Project** and then select **Run**.

**Note:** if you see that lineage is not getting
captured, select **Save** and then move back to the
Visual ETL flows section and then reopen the Visual ETL flow.

The following Spark configuration parameters are automatically added to the
job being executed. When invoking Visual ETL programmatically, use the below
configuration.

```

{
    "--conf":"spark.extraListeners=io.openlineage.spark.agent.OpenLineageSparkListener
    --conf spark.openlineage.transport.type=amazon_datazone_api
    --conf spark.openlineage.transport.domainId={DOMAIN_ID}
    --conf spark.glue.accountId={ACCOUNT_ID}
    --conf spark.openlineage.facets.custom_environment_variables=[AWS_DEFAULT_REGION;GLUE_VERSION;GLUE_COMMAND_CRITERIA;GLUE_PYTHON_VERSION;]
    --conf spark.glue.JOB_NAME={JOB_NAME}"
}

```

The parameters are auto-configured and do not need any updates from the user.
To understand the parameters in detail:

- `spark.extraListeners=io.openlineage.spark.agent.OpenLineageSparkListener`

* OpenLineageSparkListener will be created and registered with Spark's
  listener bus

- `spark.openlineage.transport.type=amazon_datazone_api` -
  This is an OpenLineage specification to tell the OpenLineage Plugin to
  use DataZone API Transport to emit lineage events to DataZone’s
  PostLineageEvent API. For more information, see [https://openlineage.io/docs/integrations/spark/configuration/spark_conf/](https://openlineage.io/docs/integrations/spark/configuration/spark_conf/ "https://openlineage.io/docs/integrations/spark/configuration/spark_conf/")
- `spark.openlineage.transport.domainId={DOMAIN_ID}` - This
  parameter establishes the domain to which the API transport will submit
  the lineage events to.
- `spark.openlineage.facets.custom_environment_variables
[AWS_DEFAULT_REGION;GLUE_VERSION;GLUE_COMMAND_CRITERIA;GLUE_PYTHON_VERSION;]`

* The following environment variables (`AWS_DEFAULT_REGION`,
  `GLUE_VERSION`, `GLUE_COMMAND_CRITERIA`, and
  `GLUE_PYTHON_VERSION`), which AWS Glue interactive
  session populates, will be added to the LineageEvent

- `spark.glue.accountId=<ACCOUNT_ID>` - Account Id of
  the Glue Data Catalog where the metadata resides. This account id is
  used to construct Glue ARN in lineage event.
- `spark.glue.JOB_NAME` - Job name of the lineage event. In
  vETL flow, the job name is configured automatically to be
  spark.glue.JOB_NAME: ${projectId}.${pathToNotebook}

**Spark compute limitations**

- OpenLineage libraries for Spark are built into AWS Glue v5.0+ for
  Spark DataFrames only. Dynamic DataFrames are not supported.
- OpenLineage libraries for Spark are built into Amazon EMR v7.5+ and
  only for EMR-S.
- Capturing lineage from Spark jobs executed on EMR on EKS and EMR on
  EC2 are not automated but can be done by manual configuration.
- LineageEvent has a size limit of 300KB.

## Capture lineage for AWS Glue Spark executions in Notebooks

Sessions in notebooks does not have a concept of a job. You can map the Spark
executions to lineage events by generating a unique job name for the notebook.
You can use the %%configure magic with the below parameters to enable lineage
capture for Spark executions in the notebook.

Note: for AWS Glue Spark executions in notebooks, lineage capture is
automated when scheduled with workflow in shared environment using remote
workflows.

```

%%configure --name {COMPUTE_NAME} -f
{
"--conf":"spark.extraListeners=io.openlineage.spark.agent.OpenLineageSparkListener --conf spark.openlineage.transport.type=amazon_datazone_api --conf spark.openlineage.transport.domainId={DOMAIN_ID} --conf spark.glue.accountId={ACCOUNT_ID} --conf spark.openlineage.facets.custom_environment_variables=[AWS_DEFAULT_REGION;GLUE_VERSION;GLUE_COMMAND_CRITERIA;GLUE_PYTHON_VERSION;] --conf spark.glue.JOB_NAME={JOB_NAME}"
}

```

Examples of {COMPUTE_NAME}: project.spark.compatibility or
project.spark.fineGrained

Here are these parameters and what they configure, in detail:

- spark.extraListeners=io.openlineage.spark.agent.OpenLineageSparkListener
  - OpenLineageSparkListener will be created and registered with
    Spark's listener bus

- spark.openlineage.transport.type=amazon_datazone_api
  - [https://openlineage.io/docs/integrations/spark/configuration/spark_conf](https://openlineage.io/docs/integrations/spark/configuration/spark_conf "https://openlineage.io/docs/integrations/spark/configuration/spark_conf")
  - This is an OpenLineage specification to tell the OpenLineage
    Plugin to use DataZone API Transport to emit lineage events to
    DataZone's PostLineageEvent API to be captured in
    SageMaker.

- spark.openlineage.transport.domainId={DOMAIN_ID}
  - This parameter establishes the domain to which the API
    transport will submit the lineage events to.

- spark.openlineage.facets.custom_environment_variables
  [AWS\_DEFAULT\_REGION;GLUE\_VERSION;GLUE\_COMMAND\_CRITERIA;GLUE\_PYTHON\_VERSION;]
  - The following environment variables (AWS_DEFAULT_REGION,
    GLUE_VERSION, GLUE_COMMAND_CRITERIA, and GLUE_PYTHON_VERSION),
    which Glue interactive session populates, will be added to the
    LineageEvent

- spark.glue.accountId=<ACCOUNT_ID>
  - Account Id of the Glue Data Catalog where the metadata
    resides. This account id is used to construct Glue ARN in
    lineage event.

- spark.glue.JOB_NAME
  - Job name of the lineage event. For example, the job name can
    be set to be spark.glue.JOB_NAME:
    ${projectId}.${pathToNotebook}.

## Capture lineage EMR-S Spark executions from Notebooks

EMR v7.5 and greater with Spark engine has the necessary OpenLineage libraries
built in. They need to be added to the spark submit properties in order to be
used especially if AWS Glue is being used as the Hive metastore. The rest of
the spark submit properties are similar to those used in AWS Glue jobs. Be
sure to replace the {Domain ID} with your specific Amazon DataZone or Amazon SageMaker Unified Studio
domain and to replace the {Account ID} with the account id where the EMR job is
run.

```

%%configure --name emr-s.{EMR_SERVERLESS_COMPUTE_NAME}
{
    "conf": {
         "spark.extraListeners": "io.openlineage.spark.agent.OpenLineageSparkListener",
         "spark.openlineage.transport.type":"amazon_datazone_api",
         "spark.openlineage.transport.domainId":"{DOMAIN_ID}",
         "spark.glue.accountId":"{ACCOUNT_ID}",
         "spark.jars":"/usr/share/aws/datazone-openlineage-spark/lib/DataZoneOpenLineageSpark-1.0.jar"
    }
}

```

- The JOB_NAME is the Spark application name that is automatically
  set
- Replace {DOMAIN_ID} and {ACCOUNT_ID}
- Amazon SageMaker Unified Studio VPC endpoint is deployed to EMR serverless VPC
  endpoint
