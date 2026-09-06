

# Reading from CircleCI entities
<a name="circleci-reading-from-entities"></a>

**Prerequisite**

A CircleCI object you would like to read from. You will need the object name.

**Supported entities for source**:


| Entity | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Context | Yes | No | No | Yes | No | 
| Organization Summary Metric | Yes | No | No | Yes | No | 
| Pipeline | No | No | No | Yes | No | 
| Pipeline Workflow | Yes | No | No | Yes | No | 
| Project Branch | Yes | No | No | Yes | No | 
| Project Flaky Test | No | No | No | Yes | No | 
| Project Summary Metric | Yes | No | No | Yes | No | 
| Schedule | No | No | No | Yes | No | 
| Workflow Job Timeseries | Yes | No | No | Yes | No | 
| Workflow Metric And Trend | Yes | No | No | Yes | No | 
| Workflow Recent Run | Yes | No | No | Yes | No | 
| Workflow Summary Metric | Yes | No | No | Yes | No | 
| Workflow Test Metric | Yes | No | No | Yes | No | 

**Example**:

```
circleci_read = glueContext.create_dynamic_frame.from_options(
    connection_type="circleci",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "context/e7ea2945-dccb-4205-b673-8391fe1b3a4c",
        "API_VERSION": "v2"
    }
```

## CircleCI entity and field details
<a name="circleci-reading-from-entities-field-details"></a>

For more information about the entities and field details see:
+ [Contexts](https://circleci.com/docs/api/v2/#operation/listContexts)
+ [Project Summary Metrics](https://circleci.com/docs/api/v2/#operation/getProjectWorkflowsPageData)
+ [Workflow Job Timeseries](https://circleci.com/docs/api/v2/#operation/getJobTimeseries)
+ [Organization Summary Metrics](https://circleci.com/docs/api/v2/#operation/getOrgSummaryData)
+ [Project Branches](https://circleci.com/docs/api/v2/#operation/getAllInsightsBranches)
+ [Project Flaky Tests](https://circleci.com/docs/api/v2/#operation/getFlakyTests)
+ [Workflow Recent Runs](https://circleci.com/docs/api/v2/#operation/getProjectWorkflowRuns)
+ [Workflow Summary Metrics](https://circleci.com/docs/api/v2/#operation/getProjectWorkflowMetrics)
+ [Workflow Metrics and Trends](https://circleci.com/docs/api/v2/#operation/getWorkflowSummary)
+ [Workflow Test Metrics](https://circleci.com/docs/api/v2/#operation/getProjectWorkflowTestMetrics)
+ [Pipelines](https://circleci.com/docs/api/v2/#operation/listPipelinesForProject)
+ [Pipeline Workflows](https://circleci.com/docs/api/v2/#operation/listWorkflowsByPipelineId)
+ [Schedules](https://circleci.com/docs/api/v2/#operation/listSchedulesForProject)

Entities with static metadata:



- **Context**
  - **Field:** Created At / **Data type:** String / **Supported operators:** 
  - **Field:** ID / **Data type:** String / **Supported operators:** 
  - **Field:** Name / **Data type:** String / **Supported operators:** 
  - **Field:** Owner Type / **Data type:** String / **Supported operators:** EQUAL\_TO

- **Organization Summary Metric**
  - **Field:** All Projects / **Data type:** List / **Supported operators:** 
  - **Field:** Org Data / **Data type:** Struct / **Supported operators:** 
  - **Field:** Org Project Data / **Data type:** List / **Supported operators:** 
  - **Field:** Project Names / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** Reporting Window / **Data type:** String / **Supported operators:** EQUAL\_TO

- **Pipeline**
  - **Field:** Branch / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** Created At / **Data type:** String / **Supported operators:** 
  - **Field:** Errors / **Data type:** List / **Supported operators:** 
  - **Field:** ID / **Data type:** String / **Supported operators:** 
  - **Field:** Number / **Data type:** Integer / **Supported operators:** 
  - **Field:** Project Slug / **Data type:** String / **Supported operators:** 
  - **Field:** State / **Data type:** String / **Supported operators:** 
  - **Field:** Trigger / **Data type:** Struct / **Supported operators:** 
  - **Field:** Trigger Parameters / **Data type:** Struct / **Supported operators:** 
  - **Field:** Updated At / **Data type:** String / **Supported operators:** 
  - **Field:** VCS / **Data type:** Struct / **Supported operators:** 

- **Pipeline Workflow**
  - **Field:** Canceled By / **Data type:** String / **Supported operators:** 
  - **Field:** Created At / **Data type:** String / **Supported operators:** 
  - **Field:** Errorer By / **Data type:** String / **Supported operators:** 
  - **Field:** ID / **Data type:** String / **Supported operators:** 
  - **Field:** Name / **Data type:** String / **Supported operators:** 
  - **Field:** Pipeline ID / **Data type:** String / **Supported operators:** 
  - **Field:** Pipeline Number / **Data type:** Integer / **Supported operators:** 
  - **Field:** Project Slug / **Data type:** String / **Supported operators:** 
  - **Field:** Started By / **Data type:** String / **Supported operators:** 
  - **Field:** Status / **Data type:** String / **Supported operators:** 
  - **Field:** Stopped At / **Data type:** String / **Supported operators:** 
  - **Field:** Tag / **Data type:** String / **Supported operators:** 

- **Project Branch**
  - **Field:** Branches / **Data type:** List / **Supported operators:** 
  - **Field:** Org ID / **Data type:** String / **Supported operators:** 
  - **Field:** Project ID / **Data type:** String / **Supported operators:** 
  - **Field:** Workflow Name / **Data type:** String / **Supported operators:** EQUAL\_TO

- **Project Flaky Test**
  - **Field:** Classname / **Data type:** String / **Supported operators:** 
  - **Field:** File / **Data type:** String / **Supported operators:** 
  - **Field:** Job Name / **Data type:** String / **Supported operators:** 
  - **Field:** Job Number / **Data type:** Integer / **Supported operators:** 
  - **Field:** Pipeline Number / **Data type:** Integer / **Supported operators:** 
  - **Field:** Source / **Data type:** String / **Supported operators:** 
  - **Field:** Test Name / **Data type:** String / **Supported operators:** 
  - **Field:** Time Wasted / **Data type:** Integer / **Supported operators:** 
  - **Field:** Times Flaked / **Data type:** Integer / **Supported operators:** 
  - **Field:** Workflow Created At / **Data type:** String / **Supported operators:** 
  - **Field:** Workflow ID / **Data type:** String / **Supported operators:** 
  - **Field:** Workflow Name / **Data type:** String / **Supported operators:** 

- **Project Summary Metric**
  - **Field:** All Branches / **Data type:** List / **Supported operators:** 
  - **Field:** All Workflows / **Data type:** List / **Supported operators:** 
  - **Field:** Branches / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** Organization ID / **Data type:** String / **Supported operators:** 
  - **Field:** Project Data / **Data type:** Struct / **Supported operators:** 
  - **Field:** Project ID / **Data type:** String / **Supported operators:** 
  - **Field:** Project Workflow Branch Data / **Data type:** List / **Supported operators:** 
  - **Field:** Project Workflow Data / **Data type:** List / **Supported operators:** 
  - **Field:** Reporting Window / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** Workflow Names / **Data type:** String / **Supported operators:** EQUAL\_TO

- **Schedule**
  - **Field:** Actor / **Data type:** Struct / **Supported operators:** 
  - **Field:** Created At / **Data type:** String / **Supported operators:** 
  - **Field:** Description / **Data type:** String / **Supported operators:** 
  - **Field:** ID / **Data type:** String / **Supported operators:** 
  - **Field:** Name / **Data type:** String / **Supported operators:** 
  - **Field:** Parameters / **Data type:** Struct / **Supported operators:** 
  - **Field:** Project Slug / **Data type:** String / **Supported operators:** 
  - **Field:** Timetable / **Data type:** Struct / **Supported operators:** 
  - **Field:** Updated At / **Data type:** String / **Supported operators:** 

- **Workflow Job Timeseries**
  - **Field:** Branch / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** Granularity / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** Max Ended At / **Data type:** String / **Supported operators:** 
  - **Field:** Metrics / **Data type:** Struct / **Supported operators:** 
  - **Field:** Min Started At / **Data type:** String / **Supported operators:** 
  - **Field:** Name / **Data type:** String / **Supported operators:** 
  - **Field:** Start End Date / **Data type:** DateTime / **Supported operators:** EQUAL\_TO, BETWEEN
  - **Field:** Timestamp / **Data type:** String / **Supported operators:** 

- **Workflow Metric and Trend**
  - **Field:** All Branches / **Data type:** Boolean / **Supported operators:** EQUAL\_TO
  - **Field:** Branches / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** Metrics / **Data type:** Struct / **Supported operators:** 
  - **Field:** Trends / **Data type:** Struct / **Supported operators:** 
  - **Field:** Workflow Names / **Data type:** List / **Supported operators:** 

- **Workflow Recent Run**
  - **Field:** All Brances / **Data type:** Boolean / **Supported operators:** EQUAL\_TO
  - **Field:** Branch / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** Created At / **Data type:** String / **Supported operators:** 
  - **Field:** Credits Used / **Data type:** Integer / **Supported operators:** 
  - **Field:** Duration / **Data type:** Integer / **Supported operators:** 
  - **Field:** ID / **Data type:** String / **Supported operators:** 
  - **Field:** Is Approval / **Data type:** Boolean / **Supported operators:** 
  - **Field:** Start End Date / **Data type:** DateTime / **Supported operators:** EQUAL\_TO, BETWEEN
  - **Field:** Status / **Data type:** String / **Supported operators:** 
  - **Field:** Stopped At / **Data type:** String / **Supported operators:** 

- **Workflow Summary Metric**
  - **Field:** All Branches / **Data type:** Boolean / **Supported operators:** EQUAL\_TO
  - **Field:** Branch / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** Metrics / **Data type:** Struct / **Supported operators:** 
  - **Field:** Name / **Data type:** String / **Supported operators:** 
  - **Field:** Project ID / **Data type:** String / **Supported operators:** 
  - **Field:** Reporting Window / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** Window End / **Data type:** String / **Supported operators:** 
  - **Field:** Window Start / **Data type:** String / **Supported operators:** 

- **Workflow Test Metric**
  - **Field:** Average Test Count / **Data type:** Integer / **Supported operators:** 
  - **Field:** Branch / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** Most Failed Tests / **Data type:** List / **Supported operators:** 
  - **Field:** Most Failed Tests Extra / **Data type:** Integer / **Supported operators:** 
  - **Field:** Slowest Tests / **Data type:** List / **Supported operators:** 
  - **Field:** Slowest Tests Extra / **Data type:** Integer / **Supported operators:** 
  - **Field:** Test Runs / **Data type:** List / **Supported operators:** 
  - **Field:** Total Test Runs / **Data type:** Integer / **Supported operators:** 



**Note**  
Struct and List data types are converted to String data type in the response of the connector.

**Partitioning queries**

CircleCI doesn’t support field-based or record-based partitioning.