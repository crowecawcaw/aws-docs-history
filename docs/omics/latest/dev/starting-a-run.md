# Start a run in HealthOmics

When you start a run, you specify the resources that HealthOmics allocates for the run. The following settings are
available:

1. **Output location** – Specify an Amazon S3 URI where the output files from
   the run are stored. If you run a high volume of workflows concurrently, use separate Amazon S3 output URIs for each
   workflow to avoid bucket throttling. For more information, see [Organizing objects using prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md") in the
   _Amazon S3 User Guide_ and [Scale Storage Connections Horizontally](../../../whitepapers/latest/s3-optimizing-performance-best-practices/scale-storage-connections-horizontally.md "../../../whitepapers/latest/s3-optimizing-performance-best-practices/scale-storage-connections-horizontally.md") in the _Optimizing Amazon S3
   Performance_ whitepaper.
2. **Service role** – Specify an IAM service role that grants HealthOmics
   permissions to access the resources needed for the run. Optionally, the console can create the service role for
   you. For more information, see [Service roles for AWS HealthOmics](permissions-service.md "permissions-service.md").
3. **Run storage** (optional, defaults to Dynamic) – Specify the run storage
   type and storage amount (for static storage). To ensure data isolation and security, HealthOmics provisions the storage
   at the start of each run, and deprovisions it at the end of the run. For more information, see [Run storage types in HealthOmics workflows](workflows-run-types.md "workflows-run-types.md").
4. **Run priority** (optional) – Assign a priority to the run. How priority
   impacts the run depends on whether the run is associated with a run group. For more information, see [Run priority](creating-run-groups.md#run-priority "creating-run-groups.md#run-priority").
5. **Workflow version** (optional) – Select a specific workflow version for
   the run. If you don't specify a version, HealthOmics starts the [default
   workflow version](workflows-default-version.md "workflows-default-version.md").
6. **Nextflow engine settings** (optional, Nextflow only) – Specify engine
   settings such as version and syntax parser for Nextflow workflows during runtime. For more information, see
   [Specify Nextflow engine settings](#start-run-api-engine-settings "#start-run-api-engine-settings").
7. **Input parameters** (optional) – Provide the workflow input parameters
   as a JSON file or inline values. Required parameters are defined by the workflow's parameter template. For more
   information, see [HealthOmics run inputs](workflows-run-inputs.md "workflows-run-inputs.md").
8. **Request ID** (optional, API and CLI only) – Provide a unique request
   ID for each run. The request ID is an idempotency token that HealthOmics uses to identify duplicate requests and start
   the run only once.

###### Topics

- [Starting a run using the console](#starting-a-run-console "#starting-a-run-console")
- [Starting a run using the API](#starting-a-run-api "#starting-a-run-api")
- [Specify Nextflow engine settings](#start-run-api-engine-settings "#start-run-api-engine-settings")
- [VPC networking](#start-run-vpc-networking "#start-run-vpc-networking")

## Starting a run using the console

The Start run wizard has four steps:

1. Specify run details
2. Add parameter values
3. Add run group, run cache, and tags
4. Review and start run

**To start a run**

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Runs**.
3. Choose **Start run**.

### Step 1: Specify run details

Provide the following settings:

| #   | Setting                              | Required                           | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
| --- | ------------------------------------ | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Choose workflow source**           | Required                           | Choose *_Owned workflow_<br>• (private workflows you own) or *_Shared<br>workflow_<br>• (workflows shared with you).                                                                                                                                                                                                                                                                                                 |
| 2   | **Workflow ID**                      | Required                           | Select the workflow ID for this run.                                                                                                                                                                                                                                                                                                                                                                                 |
| 3   | **Run name**                         | Required (optional on API and CLI) | A descriptive name for this run. Maximum 127 characters. A run ID is generated automatically once<br>the workflow is run.                                                                                                                                                                                                                                                                                            |
| 4   | **Configuration**                    | Optional                           | Choose a configuration to specify VPC settings (subnets, security groups) for internet<br>connectivity and to include container registry mappings and Git repository connections. Cannot be<br>changed after the run starts.                                                                                                                                                                                         |
| 5   | **Run priority**                     | Optional                           | Sets the priority of a run in a run group. A higher number means a greater priority. Integers<br>only, in the range 0–1,000.                                                                                                                                                                                                                                                                                         |
| 6   | **Run storage type**                 | Optional                           | Choose *_Dynamic storage_<br>• (default, recommended) or **Static<br>storage**. Dynamic storage scales up and down per task. Static storage provisions a fixed<br>amount. For more information, see [Run storage types in HealthOmics workflows](workflows-run-types.md "workflows-run-types.md").                                                                                                                   |
| 7   | **Run storage capacity**             | Conditional                        | For static storage only. Specify the amount in GiB.                                                                                                                                                                                                                                                                                                                                                                  |
| 8   | **Select S3 output destination**     | Required                           | The Amazon S3 location where run outputs are delivered. Format:<br>`s3://bucket/prefix/object`.                                                                                                                                                                                                                                                                                                                      |
| 9   | **Output bucket owner's account ID** | Optional                           | If your account doesn't own the output bucket, enter the bucket owner's AWS account ID.                                                                                                                                                                                                                                                                                                                              |
| 10  | **Run metadata retention mode**      | Optional                           | Choose *_Retain run metadata_<br>• (default) or **Remove oldest<br>automatically**. `RETAIN` is the default value; in this mode HealthOmics doesn't delete the<br>run metadata. If you choose `REMOVE`, HealthOmics permanently deletes the oldest<br>run metadata when the run count reaches the maximum. For more information, see [Run retention mode for HealthOmics runs](run-retention.md "run-retention.md"). |
| 11  | **Network access**                   | Optional                           | Choose *_Restricted_<br>• (default) or **Virtual Private Cloud<br>(VPC)**. For more information, see [VPC networking](#start-run-vpc-networking "#start-run-vpc-networking").                                                                                                                                                                                                                                        |
| 12  | **Service role**                     | Required                           | Choose an existing service role or create a new one. HealthOmics requires permissions for Amazon S3 and KMS.<br>For more information, see [Service roles for AWS HealthOmics](permissions-service.md "permissions-service.md").                                                                                                                                                                                      |

Choose **Next** to proceed to Step 2.

### Step 2: Add parameter values

On this page, enter the parameter values for the run, or select predefined values provided by the workflow
author.

When you select a Nextflow workflow to start the run, additional sections for **Nextflow
engine settings** and **Nextflow profiles** appear at the top of this
step. For complete details on these settings (supported values, behavior, and profile precedence), see [Specify Nextflow engine settings](#start-run-api-engine-settings "#start-run-api-engine-settings").

**Run parameter values**

Provide the run parameters. You can upload a JSON file or manually enter the values. The JSON file contains
the exact name of each input parameter and a value for the parameter.

HealthOmics supports the following JSON types for parameter values.

| JSON type | Example key and value       | Notes                                                                                                            |
| --------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| boolean   | "b":true                    | Value is not in quotes, and all lowercase.                                                                       |
| integer   | "i":7                       | Value is not in quotes.                                                                                          |
| number    | "f":42.3                    | Value is not in quotes.                                                                                          |
| string    | "s":"characters"            | Value is in quotes. Use string type for text values and URIs.<br>The URI target must be the expected input type. |
| array     | "a":[1,2,3]                 | Value is not in quotes. Array members must each have the type defined by the input parameter.                    |
| object    | "o":{"left":"a", "right":1} | In WDL, object maps to WDL Pair, Map, or Struct                                                                  |

For more information, see [HealthOmics run inputs](workflows-run-inputs.md "workflows-run-inputs.md") and
[Managing run parameters size](workflows-run-inputs.md#run-input-file-options "workflows-run-inputs.md#run-input-file-options").

Choose **Next** to proceed to Step 3.

### Step 3: Add run group, run cache, and tags

All settings on this page are optional.

| #   | Setting       | Required | Description                                                                                                                                                                                                                                                                               |
| --- | ------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Run group** | Optional | Select an existing run group or create a new one. Run groups bundle runs by category and priority<br>and set maximum vCPUs and run time. For more information, see [Using HealthOmics run groups](creating-run-groups.md "creating-run-groups.md").                                       |
| 2   | **Run cache** | Optional | Use a run cache to reuse completed task results rather than recomputing them. For more<br>information, see [Configuring a run with run cache using the console](workflow-cache-startrun.md#workflow-cache-startrun-console "workflow-cache-startrun.md#workflow-cache-startrun-console"). |
| 3   | **Tags**      | Optional | Add up to 50 key-value tags for search, filtering, and cost tracking.                                                                                                                                                                                                                     |

Choose **Next** to proceed to Step 4.

### Step 4: Review and start run

Review the run configuration from all previous steps. To modify a setting, choose **Edit**
next to the relevant step. When you're ready, choose **Start run**.

## Starting a run using the API

Use the **StartRun** API operation to create and start a run.

### Start a basic run

The following example specifies the workflow ID, service role, and output URI. This example sets the
retention mode to `REMOVE`. For more information about retention mode, see [Run retention mode for HealthOmics runs](run-retention.md "run-retention.md").

```
aws omics start-run \
     --workflow-id ``workflow id`` \
     --role-arn arn:aws:iam::123456789012:role/OmicsRole \
     --output-uri s3://amzn-s3-demo-bucket/output \
     --name "my-workflow-run" \
     --retention-mode REMOVE
```

In response, you get the following output. The `uuid` is unique to the run, and along with
`outputUri` can be used to track where output data is written.

```
{
    "arn": "arn:aws:omics:us-west-2:123456789012:run/1234567",
    "id": "123456789",
    "uuid": "96c57683-74bf-9d6d-ae7e-f09b097db14a",
    "outputUri": "s3://bucket/folder/8405154/96c57683-74bf-9d6d-ae7e-f09b097db14a",
    "status": "PENDING"
}
```

### Common API options

**Include a parameter file**

If the parameter template for a workflow declares any required parameters, you can provide a local
JSON file of the inputs when you start a workflow run. The JSON file contains the exact name of each input
parameter and a value for the parameter.

Reference the input JSON file in the AWS CLI by adding `--parameters
 file://<input_file.json>` to your `start-run` request. For more information, see supported
JSON types for parameter values in [Step 2: Add parameter values](#start-run-console-step2 "#start-run-console-step2") and [HealthOmics run inputs](workflows-run-inputs.md "workflows-run-inputs.md").

**Provide a request ID**

You can provide a unique `requestId` for each run. The request ID is an idempotency token
that HealthOmics uses to catch duplicate requests. It won't start a run if the request ID is a duplicate of a
previous run.

If you use infrastructure (such as Lambda functions or step functions) for orchestrating run starts,
best practice is to provide a unique request ID for each StartRun request. This ensures that if your
infrastructure inadvertently starts a run that it already started, HealthOmics won't start the duplicate
run.

```
aws omics start-run \
     --workflow-id ``workflow id`` \
     ... \
     --request-id "unique-request-id-12345"
```

**Choose a workflow version**

You can specify a workflow version for the run. If you don't specify a version, HealthOmics starts the run
with the default workflow version.

```
aws omics start-run \
     --workflow-id ``workflow id`` \
     ... \
     --workflow-version-name '1.2.1'
```

**Override the run storage type**

You can override the default run storage type that was set in the workflow.

```
aws omics start-run \
     --workflow-id ``workflow id`` \
     ... \
     --storage-type STATIC \
     --storage-capacity 2400
```

### Enabling ephemeral storage

To enable ephemeral storage for a run, set `--scratch-storage-mode` to `LOCAL` when
you start the run. HealthOmics mounts a dedicated local storage volume at `/tmp` for each workflow task
instance.

```
aws omics start-run \
    --workflow-id `workflow-id` \
    --role-arn `arn:aws:iam::123456789012:role/OmicsServiceRole` \
    --output-uri s3://`amzn-s3-demo-bucket`/`output-folder`/ \
    --parameters file://`/path/to/parameters.json` \
    --scratch-storage-mode LOCAL
```

To disable ephemeral storage for a specific run (for example, to isolate a failure), set
`--scratch-storage-mode` to `SHARED`.

For more information, see [Ephemeral storage for HealthOmics workflow tasks](workflows-ephemeral-storage.md "workflows-ephemeral-storage.md").

For Nextflow engine settings (engine version, profiles, syntax parser), see [Specify Nextflow engine settings](#start-run-api-engine-settings "#start-run-api-engine-settings").

## Specify Nextflow engine settings

For Nextflow workflows, you can pass an `engineSettings` map in the **StartRun** API
request to control engine behavior without modifying your workflow source code. On the console, these settings are
available in **Step 2: Add parameter values** as a separate section that appears for
Nextflow workflows.

###### Note

Engine settings apply only to Nextflow workflows. If you specify engine settings for WDL or CWL workflows in
the API or CLI, they are silently ignored and are not available in **GetRun** responses.

### Supported keys

| #   | Key             | Valid values                                                                                                                                     | Behavior                                                                                                                                           | Version support                                         |
| --- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| 1   | `engineVersion` | `"22.04.0"` (or `"22.04"`), `"23.10.0"` (or<br>`"23.10"`), `"24.10.8"` (or `"24.10"`), `"25.10.0"` (or<br>`"25.10"`), `"26.04.0"` (or `"26.04"`) | Pins the Nextflow version for the run. Overrides the version detected from<br>`nextflow.config`. Both full and short version formats are accepted. | All Nextflow versions                                   |
| 2   | `syntaxVersion` | `"v1"` (Legacy parser), `"v2"` (Strict syntax parser)                                                                                            | Selects the syntax parser.                                                                                                                         | v26.04 and later. Earlier versions support only `"v1"`. |
| 3   | `outputFormat`  | `"json"`, `"text"`, `"none"`                                                                                                                     | Sets the engine stdout/stderr summary format.                                                                                                      | v26.04 and later (ignored on earlier versions).         |
| 4   | `agentMode`     | `"true"`, `"false"`                                                                                                                              | Controls Nextflow agent mode.                                                                                                                      | v26.04 and later (ignored on earlier versions).         |
| 5   | `profile`       | Comma-separated profile names, for example `"test,docker"`                                                                                       | Activates Nextflow profiles. For more information, see [Nextflow profiles](#start-run-nextflow-profiles "#start-run-nextflow-profiles").           | All Nextflow versions                                   |

### Nextflow engine version pinning

You can select a specific Nextflow engine version to run your workflow, enabling controlled migration
across engine versions. The run-time version override ensures that even when a workflow definition specifies a
version through its config or profile, the engine version that you specify at run time takes precedence. This
enables you to test the same workflow across multiple engine versions without modifying the workflow source
code.

Supported versions: 22.04.0 (or 22.04), 23.10.0 (or 23.10), 24.10.8 (or 24.10), 25.10.0 (or 25.10), and
26.04.0 (or 26.04). Both full and short version formats are accepted.

**API and CLI**

Use the `engineVersion` key in `--engine-settings`:

```
aws omics start-run \
    --workflow-id ``workflow id`` \
    --role-arn arn:aws:iam::123456789012:role/OmicsRole \
    --output-uri s3://amzn-s3-demo-bucket/output \
    --engine-settings '{"engineVersion":"26.04"}'
```

**Console**

In [Step 2: Add parameter values](#start-run-console-step2 "#start-run-console-step2"), select the version
from the **Engine version** dropdown in the Nextflow engine settings section.

### Nextflow profiles

Nextflow profiles are named sets of execution settings defined in your workflow's
`nextflow.config`. You can activate one or more profiles at run time to apply environment-specific
settings (for example, development, test, or production) without modifying the workflow source code.

**API and CLI**

Use the `profile` key in `--engine-settings`. Specify multiple profiles as a
comma-separated list:

```
aws omics start-run \
    --workflow-id ``workflow id`` \
    --role-arn arn:aws:iam::123456789012:role/OmicsRole \
    --output-uri s3://amzn-s3-demo-bucket/output \
    --engine-settings '{"profile":"test,docker"}'
```

**Console**

In [Step 2: Add parameter values](#start-run-console-step2 "#start-run-console-step2"), the
**Nextflow profiles** section appears below the engine settings. Select one or more profiles
from the **Select profiles** dropdown. The console displays the profile application order. To
remove a profile, choose the **×** next to its name.

**Profile application order**

When you specify multiple profiles, the application order depends on the Nextflow engine version and
syntax parser:

- **Nextflow v26.04 and later with the strict syntax parser (v2)** –
  Profiles are applied in the order specified in the `profile` value (left to right), or in your
  selection order on the console. Later profiles override earlier ones for conflicting settings.
- **Nextflow versions earlier than v26.04, and v26.04 and later with the legacy
  parser (v1)** – Profiles are applied in the order defined in the
  `nextflow.config` file, regardless of the order specified in the API request or console
  selection.

**Configuration precedence**

Nextflow resolves parameters in the following order, with later layers overriding earlier ones:

1. `nextflow.config` defaults
2. Selected Nextflow profiles
3. Predefined values file
4. Run-time parameter overrides

###### Note

**Recommendation** – To ensure consistent profile application
behavior across runs, pin the Nextflow engine version using the `engineVersion` key in the API or
**Engine version** on the console.

## VPC networking

You can run workflows in your Virtual Private Cloud (VPC), which enables access to the public internet,
cross-Region traffic, and communication with resources in your VPC.

To enable VPC networking:

1. Create a configuration that specifies VPC subnets and security groups.
2. When starting a run using the console, set **Network access** to **Virtual
   Private Cloud (VPC)** and select your configuration in Step 1.
3. When starting a run using the API, use `--networking-mode VPC` and reference your
   configuration with `--configuration-name`.

For more information, see [Connecting HealthOmics workflows to a VPC](workflows-vpc-networking.md "workflows-vpc-networking.md").
