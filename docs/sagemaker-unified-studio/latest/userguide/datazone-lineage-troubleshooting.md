# Troubleshooting data

lineage

This comprehensive troubleshooting guide helps you resolve common data lineage
visibility issues in Amazon SageMaker Unified Studio. The guide covers programmatically published events,
data source configurations, and tool-specific lineage capture problems.

###### Topics

- [Not seeing lineage
  graph for events published programmatically](#lineage-troubleshooting-programmatic-events "#lineage-troubleshooting-programmatic-events")
- [Not seeing lineage for
  assets even though importLineage is shown as true in AWS Glue
  datasource](#lineage-troubleshooting-glue-datasource "#lineage-troubleshooting-glue-datasource")
- [Not seeing lineage
  for assets even though importLineage is shown as true in Amazon Redshift
  datasource](#lineage-troubleshooting-redshift-datasource "#lineage-troubleshooting-redshift-datasource")
- [Troubleshooting lineage for
  lineage events published from AWS Glue ETL jobs/vETL/Notebooks](#lineage-troubleshooting-glue-etl-jobs "#lineage-troubleshooting-glue-etl-jobs")
- [Troubleshooting lineage for
  lineage events published from EMR-S/EC2/EKS](#lineage-troubleshooting-emr "#lineage-troubleshooting-emr")

## Not seeing lineage

graph for events published programmatically

**Primary requirement:** Lineage graphs are only
visible in Amazon SageMaker Unified Studio if at least one node of the graph is an asset. You must
create assets for any dataset nodes and properly link them using the
sourceIdentifier attribute.

**Troubleshooting steps:**

1. Create assets for any of the dataset nodes involved in your lineage
   events. Refer to the following sections for proper linking:
   - [The importance of
     the sourceIdentifier attribute to lineage nodes](datazone-data-lineage-sourceIdentifier-attribute.md "datazone-data-lineage-sourceIdentifier-attribute.md")
   - [Linking dataset lineage nodes
     with assets imported into Amazon SageMaker Unified Studio](datazone-data-lineage-linking-nodes.md "datazone-data-lineage-linking-nodes.md")

2. Once the asset is created, verify that you can see the lineage on the
   asset details page.
3. If you are still not seeing lineage, verify that the asset's
   sourceIdentifier (present in AssetCommonDetailsForm) has the same value
   as the sourceIdentifier of any input/output dataset node in the lineage
   event.

Use the following command to get asset details:

```

aws datazone get-asset --domain-identifier {DOMAIN_ID} --identifier {ASSET_ID}

```

The response appears as follows:

```

{
    .....
    "formsOutput": [
        .....
        {
            "content": "{\"sourceIdentifier\":\"arn:aws:glue:eu-west-1:123456789012:table/testlfdb/testlftb-1\"}",
            "formName": "AssetCommonDetailsForm",
            "typeName": "amazon.datazone.AssetCommonDetailsFormType",
            "typeRevision": "6"
        },
        .....
    ],
    "id": "{ASSET_ID}",
    ....
}

```

4. If both sourceIdentifiers are matching but you still cannot see
   lineage, retrieve the eventId from the PostLineageEvent response or use
   ListLineageEvents to find the eventId, then invoke
   GetLineageEvent:

```

aws datazone list-lineage-events --domain-identifier {DOMAIN_ID}
// You can apply additional filters like timerange etc.
// Refer https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListLineageEvents.html

aws datazone get-lineage-event --domain-identifier {DOMAIN_ID} --identifier {EVENT_ID} --output json event.json

```

The response appears as follows and the open-lineage event is written
to the event.json file:

```

{
    "domainId": "{DOMAIN_ID}",
    "id": "{EVENT_ID}",
    "createdBy": ....,
    "processingStatus": "SUCCESS"/"FAILED etc",
    "eventTime": "2024-05-04T10:15:30+00:00",
    "createdAt": "2025-05-04T22:18:27+00:00"
}

```

5. If the GetLineageEvent response's processingStatus is FAILED, contact
   AWS support by providing the GetLineageEvent response for the
   appropriate event and the response from GetAsset.
6. If the GetLineageEvent response's processingStatus is SUCCESS,
   double-check that the sourceIdentifier of the dataset node from the
   lineage event matches the value in the GetAsset response above. The
   following steps help verify this.
7. Invoke GetLineageNode for the job run where the identifier is composed
   of namespace, name of job and run_id in the lineage event:

```

aws datazone get-lineage-node --domain-identifier {DOMAIN_ID} --identifier <job's namespace>.<job's name>/<run_id>

```

The response appears as follows:

```

{
    .....
    "downstreamNodes": [
        {
            "eventTimestamp": "2024-07-24T18:08:55+08:00",
            "id": "afymge5k4v0euf"
        }
    ],
    "formsOutput": [
        <some forms corresponding to run and job>
    ],
    "id": "<system generated node-id for run>",
    "sourceIdentifier": "<job's namespace>.<job's name>/<run_id>",
    "typeName": "amazon.datazone.JobRunLineageNodeType",
    ....
    "upstreamNodes": [
        {
            "eventTimestamp": "2024-07-24T18:08:55+08:00",
            "id": "6wf2z27c8hghev"
        },
        {
            "eventTimestamp": "2024-07-24T18:08:55+08:00",
            "id": "4tjbcsnre6banb"
        }
    ]
}

```

8. Invoke GetLineageNode again by passing in the downstream/upstream node
   identifier (which you think should be linked to the asset node):

```

aws datazone get-lineage-node --domain-identifier {DOMAIN_ID} --identifier afymge5k4v0euf

```

This returns the lineage node details corresponding to the dataset:
`afymge5k4v0euf`. Verify if the sourceIdentifier matches
that of the asset. If not matching, fix the namespace and name of the
dataset in the lineage event and publish the lineage event again. You
will see the lineage graph on the asset.

```

{
    .....
    "downstreamNodes": [],
    "eventTimestamp": "2024-07-24T18:08:55+08:00",
    "formsOutput": [
        .....
    ],
    "id": "afymge5k4v0euf",
    "sourceIdentifier": "<sample_sourceIdentifier_value>",
    "typeName": "amazon.datazone.DatasetLineageNodeType",
    "typeRevision": "1",
    ....
    "upstreamNodes": [
        ...
    ]
}

```

## Not seeing lineage for

assets even though importLineage is shown as true in AWS Glue
datasource

Open the datasource run(s) associated with the AWS Glue datasource and you
can see the assets imported as part of the run and the lineage import status
along with error message in case of failure.

**Limitations:**

- Lineage for crawler run importing more than 250 tables isn't
  supported.

## Not seeing lineage

for assets even though importLineage is shown as true in Amazon Redshift
datasource

Lineage on Amazon Redshift tables is captured by retrieving user queries
performed on the Amazon Redshift database, from the system tables.

**Lineage is not supported in the following cases:**

- External Tables
- Unload / Copy
- Merge / Update
- Queries that produce Lineage Events larger than 16MB
- Datashares
- ColumnLineage limitations:
  - Column Lineage is not supported for queries not containing specific columns such as (select \* from tableA)
  - Column Lineage is not supported for queries involving temp tables

- Any limitations pertaining to [OpenLineageSqlParser](https://github.com/OpenLineage/OpenLineage/blob/main/integration/sql/README.md "https://github.com/OpenLineage/OpenLineage/blob/main/integration/sql/README.md") results in failure to process some
  queries

**Troubleshooting steps:**

1. On the Amazon Redshift connection details, you will see the
   lineageJobId along with the job run schedule. Alternatively, you can
   fetch it using the [get-connection](../../../cli/latest/reference/datazone/get-connection.md "../../../cli/latest/reference/datazone/get-connection.md") API.
2. Invoke [list-job-runs](../../../cli/latest/reference/datazone/list-job-runs.md "../../../cli/latest/reference/datazone/list-job-runs.md") to get the runs corresponding to the
   job:

```

aws datazone list-job-runs --domain-identifier {DOMAIN_ID} --job-identifier {JOB_ID}

```

The response appears as follows:

```

{
   "items": [
      {
         .....
         "error": {
            "message": "string"
         },
         "jobId": {JOB_ID},
         "jobType": LINEAGE,
         "runId": ...,
         "runMode": SCHEDULED,
         "status": SCHEDULED | IN_PROGRESS | SUCCESS | PARTIALLY_SUCCEEDED | FAILED | ABORTED | TIMED_OUT | CANCELED
         .....
      }
   ],
   "nextToken": ...
}

```

3. If no job-runs are returned, check your job run schedule on the Amazon
   Redshift connection details. Reach out to AWS support providing the
   lineageJobId, connectionId, projectId and domainId if job runs are not
   executed per given schedule.
4. If job-runs are returned, pick the relevant jobRunId and invoke
   GetJobRun to get job run details:

```

aws datazone get-job-run --domain-identifier {DOMAIN_ID} --identifier {JOB_RUN_ID}

```

The response appears as follows:

```

{
  ....
  "details": {
    "lineageRunDetails": {
      "sqlQueryRunDetails": {
        "totalQueriesProcessed": ..,
        "numQueriesFailed": ...,
        "errorMessages":....,
        "queryEndTime": ...,
        "queryStartTime": ...
      }
    }
  },
  .....
}

```

5. The job run fails if none of the queries are successfully processed;
   partially succeeds if some queries are successfully processed; succeeds
   if all queries are successfully processed and response also contains
   start and end times of processed queries.

## Troubleshooting lineage for

lineage events published from AWS Glue ETL jobs/vETL/Notebooks

**Limitations:**

- OpenLineage libraries for Spark are built into AWS Glue v5.0+
  for Spark DataFrames only. Does not support Glue
  DynamicFrames.
- Lineage capture for Spark jobs with fine-grained permission mode
  are not supported.
- Lineage event has a size limit of 300KB.
  **Common Issues:**

- If the AWS Glue ETL is in VPC, make sure the Amazon DataZone
  VPC endpoint is deployed in that VPC.
- In case your domain is using a CMK, make sure that the AWS
  Glue execution role has the appropriate KMS permissions. CMK can
  be found via [https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetDomain.html](../../../datazone/latest/APIReference/API_GetDomain.md "../../../datazone/latest/APIReference/API_GetDomain.md")
- Failed to publish Lineage Event because payload is greater
  than 300 kb:
  - Add the following to Spark conf:

  `"spark.openlineage.columnLineage.datasetLineageEnabled": "True"`
  - **Important
    Note:**
    - Column lineage typically constitutes a
      significant portion of the payload and enabling
      this will efficiently generate the column lineage
      info.
    - Disabling it can help reduce payload size and
      avoid validation exceptions.

- Cross account lineage event submission:
  - Follow [https://docs.aws.amazon.com/datazone/latest/userguide/working-with-associated-accounts.html](../../../datazone/latest/userguide/working-with-associated-accounts.md "../../../datazone/latest/userguide/working-with-associated-accounts.md")
    to set up account association
  - Ensure that RAM policy is using the latest
    policy

- When the same DataFrame is written to multiple destinations or
  formats in sequence, Lineage SparkListener may only capture the
  lineage for the first write operation:

      + For optimization purposes, Spark's internals may reuse
       execution plans definition for consecutive write
       operations on the same DataFrame. This can lead to only
       capturing first lineage event.

  **Troubleshooting steps:**

1. Lineage graph can only be visualized if at least one node of the graph
   is an asset. Therefore, create assets for any of the datasets (such as
   tables) involved in the job and then attempt to visualize lineage on the
   asset.
2. First, invoke [ListLineageEvents](../../../datazone/latest/APIReference/API_ListLineageEvents.md "../../../datazone/latest/APIReference/API_ListLineageEvents.md") to see if the lineage events were
   submitted (refer to the linked doc to pass filters).
3. If no events are submitted, check AWS CloudWatch logs to see
   if any exceptions are thrown from the Amazon DataZone Lineage
   lib:
   - Log groups: /aws-glue/jobs/error,
     /aws-glue/sessions/error
   - Make sure logging is enabled: [https://docs.aws.amazon.com/glue/latest/dg/monitor-continuous-logging-enable.html](../../../glue/latest/dg/monitor-continuous-logging-enable.md "../../../glue/latest/dg/monitor-continuous-logging-enable.md")
   - Following is the AWS CloudWatch log insights query to check for exceptions:

   ```

   fields @timestamp, @message
   | filter @message like /(?i)exception/ and like /(?i)datazone/
   | sort @timestamp desc

   ```

   - Following is the AWS CloudWatch log insights query to inspect generated events:

   Pass `--conf spark.log.level=DEBUG` while submitting the spark job.

   ```

   fields @timestamp, @message
   | filter @message like /Emitting lineage completed successfully/
   | sort @timestamp desc

   ```

4. Enable Spark UI to see if Spark Logical Plans and Spark Confs
   are generated properly: [https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-jobs.html#monitor-spark-ui-jobs-cli](../../../glue/latest/dg/monitor-spark-ui-jobs.md#monitor-spark-ui-jobs-cli "../../../glue/latest/dg/monitor-spark-ui-jobs.md#monitor-spark-ui-jobs-cli")

Under Environment, all the spark configurations passed could
be found. Verify the following are there:

```

spark.extraListeners  io.openlineage.spark.agent.OpenLineageSparkListener
spark.openlineage.transport.domainId  <domain-id>
spark.openlineage.transport.type  amazon_datazone_api

```

5. After verifying lineage events are successfully processed in AWS
   CloudWatch logs, follow the steps in [Not seeing lineage
   graph for events published programmatically](#lineage-troubleshooting-programmatic-events "#lineage-troubleshooting-programmatic-events") to
   troubleshoot.
6. If you are still unable to see lineage and it doesn't fall under the
   limitations category, reach out to AWS support by providing:
   - Spark config parameters
   - Lineage event from GetLineageEvent response for successfully
     processed events to which lineage isn't visible
   - GetAsset response

## Troubleshooting lineage for

lineage events published from EMR-S/EC2/EKS

**Notes:**

- Lineage is supported from following versions of EMR:
  - EMR-S: 7.5+
  - EMR-EC2: 7.11+
  - EMR-EKS: 7.12+

- Lineage capture for Spark jobs with fine-grained permission mode
  are not supported.
- If you are trying EMR outside of Amazon SageMaker Unified Studio, Amazon DataZone VPC
  endpoint needs to be deployed for EMR VPC.
- Lineage event has a size limit of 300KB.
  **Common Issues:**

- In case your domain is using a CMK, make sure that the job's
  execution role has the appropriate KMS permissions. CMK can be
  found via [https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetDomain.html](../../../datazone/latest/APIReference/API_GetDomain.md "../../../datazone/latest/APIReference/API_GetDomain.md")
- Failed to publish Lineage Event because payload is greater
  than 300 kb:
  - Add the following to Spark conf which efficiently generates the event payload:

  `"spark.openlineage.columnLineage.datasetLineageEnabled": "true"`

- Cross account lineage event submission:
  - Follow [https://docs.aws.amazon.com/datazone/latest/userguide/working-with-associated-accounts.html](../../../datazone/latest/userguide/working-with-associated-accounts.md "../../../datazone/latest/userguide/working-with-associated-accounts.md")
    to set up account association
  - Ensure that RAM policy is using the latest
    policy

- When the same DataFrame is written to multiple destinations or
  formats in sequence, Lineage SparkListener may only capture the
  lineage for the first write operation:

      + For optimization purposes, Spark's internals may reuse
       execution plans definition for consecutive write
       operations on the same DataFrame. This can lead to only
       capturing first lineage event.

  **Troubleshooting steps:**

1. Lineage graph can only be visualized if at least one node of the graph
   is an asset. Therefore, create assets for any of the datasets (such as
   tables) involved in the job and then attempt to visualize lineage on the
   asset.
2. First, invoke [ListLineageEvents](../../../datazone/latest/APIReference/API_ListLineageEvents.md "../../../datazone/latest/APIReference/API_ListLineageEvents.md") to see if the lineage events were
   submitted (refer to the linked doc to pass filters).
3. If no events are submitted, check AWS CloudWatch logs to see
   if any exceptions are thrown from the Amazon DataZone Lineage
   lib:
   - **EC2:**
     - You can enable provide the CloudWatch log group or log
       destination for S3 path at the time of creating EC2
       cluster. Refer [https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-debugging.html](../../../emr/latest/ManagementGuide/emr-plan-debugging.md "../../../emr/latest/ManagementGuide/emr-plan-debugging.md")
     - You will see logs in stderr file within
       cluster-id/containers/application\*/ folder.

   - **EKS:**
     - You need to provide the CloudWatch log group or log
       destination for S3 path while submitting spark job. Refer
       [https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/getting-started.html](../../../emr/latest/EMR-on-EKS-DevelopmentGuide/getting-started.md "../../../emr/latest/EMR-on-EKS-DevelopmentGuide/getting-started.md")
     - You will see logs in stderr file of spark_driver within
       virtual-cluster-id/jobs/job-id/containers/\* folder.

   - **EMR-S:**
     - You can enable logs by following [https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/logging.html](../../../emr/latest/EMR-Serverless-UserGuide/logging.md "../../../emr/latest/EMR-Serverless-UserGuide/logging.md")
     - You will see logs in stderr files of spark_driver

   - Following is the AWS CloudWatch log insights query to check for exceptions:

   ```

   fields @timestamp, @message
   | filter @message like /(?i)exception/ and like /(?i)datazone/
   | sort @timestamp desc

   ```

   - Following is the AWS CloudWatch log insights query to inspect generated events:

   Pass `--conf spark.log.level=DEBUG` while submitting the spark job.

   ```

   fields @timestamp, @message
   | filter @message like /Emitting lineage completed successfully/
   | sort @timestamp desc

   ```

4. After verifying lineage events are successfully processed in AWS
   CloudWatch logs, follow the steps in [Not seeing lineage
   graph for events published programmatically](#lineage-troubleshooting-programmatic-events "#lineage-troubleshooting-programmatic-events") to
   troubleshoot.
5. If you are still unable to see lineage and it doesn't fall under the
   limitations category, reach out to AWS Support by providing:
   - Spark config parameters
   - Lineage event from GetLineageEvent response for successfully
     processed events to which lineage isn't visible
   - GetAsset response
