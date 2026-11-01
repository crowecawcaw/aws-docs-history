

# Package and supply a HealthOmics workflow definition
<a name="workflow-defn-packaging"></a>

When you create a workflow or a workflow version, you supply the definition from exactly one source: a ZIP archive that you send with the request, a ZIP archive in Amazon S3, or a Git-based repository. A request that includes more than one definition source fails. The parameters in this topic apply to both the `CreateWorkflow` and `CreateWorkflowVersion` operations. For the full procedures, see [Create a private workflow](create-private-workflow.md) and [Create a workflow version](workflows-version-create.md).

**Note**  
HealthOmics lints some workflow definitions when you create a workflow. For which engines are linted, whether findings block the workflow, and how to read them, see [Workflow linters in HealthOmics](workflows-linter.md).

## Choose a workflow definition source
<a name="workflow-defn-source-selection"></a>


| Use this source | API parameter | Maximum size | AWS CLI flag | 
| --- | --- | --- | --- | 
| A ZIP archive on your local machine. | definitionZip | 4.4 MB | --definition-zip fileb://my-definition.zip | 
| A ZIP archive in an Amazon S3 bucket. The bucket must be in the same AWS Region as the workflow. | definitionUri | 100 MB | --definition-uri s3://amzn-s3-demo-bucket1/my-definition.zip | 
| A supported Git-based repository, through an AWS CodeConnections connection. | definitionRepository | 1 GiB repository, 100 MiB per file | --definition-repository with a JSON value | 

Additional considerations:
+ These size quotas can't be increased. For more information, see [HealthOmics workflow fixed size quotas](fixed-quotas.md#fixed-quotas-workflows).
+ If your account doesn't own the Amazon S3 bucket that holds the definition, provide the bucket owner's AWS account ID in `workflowBucketOwnerId` (`--workflow-bucket-owner-id`).
+ With `definitionRepository`, HealthOmics reads the definition files from the repository, and `main`, `parameterTemplatePath`, and `readmePath` are paths within the repository rather than within an archive. For more information about the `definitionRepository` fields, see [Use the workflow definition from a Git-based repository](create-private-workflow.md#create-defn-uri-git). For more information about the connection setup and the supported providers, see [HealthOmics workflow integration with Git-based repositories](workflows-git-integration.md).

## ZIP archive layout and the main definition file
<a name="workflow-defn-zip-layout"></a>

Include every file that the main definition imports, such as subworkflows, `nextflow.config`, and any `bin` scripts.

A definition file is a file whose extension matches a supported engine, such as `.wdl`, `.nf`, or `.cwl`. If you omit `main`, HealthOmics chooses it from the definition files that sit nearest the root of the archive. It ignores hidden files and folders, and it ignores definition files deeper in the archive. Automatic selection also requires a single engine, either because the archive holds one engine's definition files or because you set `engine`. Of the files at that nearest level:
+ If there is exactly one definition file, HealthOmics uses it, whatever it is named.
+ If there are several, HealthOmics uses the one named `main.wdl`, `main.nf`, or `main.cwl`.

In two cases HealthOmics can't resolve the archive. The request itself succeeds and the workflow or workflow version starts in `CREATING`, but then moves to `FAILED`, and its status message gives the reason:
+ `Zip file contains multiple workflow definition types` – the archive holds definition files for more than one engine and you didn't set `engine`. This applies whether or not you set `main`. Set `engine`, or remove the other engine's files. HealthOmics reports this reason first when both cases apply.
+ `Zip file contains multiple top-level workflow definition files` – you omitted `main`, several definition files sit at the nearest level, and not exactly one of them is named `main.wdl`, `main.nf`, or `main.cwl`. Set `main` to the path of the one you want.

To choose the main definition file yourself, set `main` (`--main`) to its path, relative to the root of the archive. The path can be up to 128 characters.

For example, for an archive whose main definition file is `workflow-definition/main-file.wdl`:

```
--main workflow-definition/main-file.wdl
```

Set `engine` (`--engine`) to name the engine yourself, either to resolve an archive that holds more than one engine's definition files or to use the WDL lenient engine.

Consider a workflow folder on your local machine with the following layout:

```
my-workflow/
    main.wdl
    tasks/align.wdl
    tasks/call-variants.wdl
```

Create the archive from inside that folder, so that `main.wdl` and the `tasks` folder sit at the root of the archive. The following command also adds hidden files and folders, such as a `.git` folder in a cloned repository. These count toward the definition size, so exclude the ones you don't need, for example, with `-x '.*' -x '*/.*'`:

```
cd my-workflow
zip -r ../my-definition.zip .
cd ..
```

`main.wdl` is now the only definition file at the root of the archive, so you can omit `main`:

```
main.wdl
tasks/align.wdl
tasks/call-variants.wdl
```

## Send the archive inline or through Amazon S3
<a name="workflow-defn-zip-handoff"></a>

`definitionZip` is a binary parameter. When you use the AWS CLI, pass the archive with the `fileb://` prefix and the AWS CLI reads the file and encodes it for you. The AWS SDKs do the encoding for you. If you call the API directly over HTTP, send the archive as a base64-encoded string.

The parameter template in the following examples is optional. If you omit it, HealthOmics derives the run parameters from your workflow definition. For more information, see [Parameter template files for HealthOmics workflows](parameter-templates.md).

The following AWS CLI example creates a workflow by sending the ZIP archive with the request. Replace each value in italics:

```
aws omics create-workflow \
  --name {{my-workflow-name}} \
  --definition-zip fileb://{{my-definition.zip}} \
  --parameter-template file://{{my-parameter-template.json}}
```

For an archive larger than the `definitionZip` limit in [Choose a workflow definition source](#workflow-defn-source-selection), upload it to an Amazon S3 bucket in the same Region as the workflow and use `definitionUri` instead. Replace each value in italics, and replace the bucket with your own:

```
aws s3 cp {{my-definition.zip}} s3://amzn-s3-demo-bucket1/my-definition.zip

aws omics create-workflow \
  --name {{my-workflow-name}} \
  --definition-uri s3://amzn-s3-demo-bucket1/my-definition.zip \
  --parameter-template file://{{my-parameter-template.json}}
```

## Set the default run storage
<a name="workflow-defn-storage-pairing"></a>

We recommend dynamic run storage for most workflows. Choose static run storage in either of these cases:
+ The workflow uses more than 9.6 TiB of data, and its tasks benefit from high sustained I/O.
+ More than 100 scattered tasks read from the shared run storage at once.

For more information about each run storage type, including its throughput characteristics and how to size static run storage, see [Run storage types in HealthOmics workflows](workflows-run-types.md) and [Run optimization for a private HealthOmics workflow](workflows-run-optimize.md).

The `storageType` (`--storage-type`) and `storageCapacity` (`--storage-capacity`) parameters set the defaults for runs that use the workflow. You can override both at run time, as described in [Start a run in HealthOmics](starting-a-run.md). Pair them as follows:
+ `storageType` of `DYNAMIC` – HealthOmics scales the run storage up and down based on file system utilization. Don't set `storageCapacity`. If you do, the request fails: `CreateWorkflow` reports `You cannot set the storage capacity for workflows that use DYNAMIC run storage type`, and `CreateWorkflowVersion` reports `You cannot set the storage capacity for workflow version that use DYNAMIC run storage type`.
+ `storageType` of `STATIC` – HealthOmics allocates a fixed amount of run storage, so also set `storageCapacity`, in GiB. If neither the workflow nor the run specifies a capacity, the run uses 1,200 GiB. The maximum is a per-account limit. HealthOmics provisions static run storage only as 1,200 GiB or as a multiple of 2,400 GiB, and rounds any other value up to the next supported size. For example, HealthOmics provisions 1,200 GiB for a capacity below 1,200 GiB.

The following example sets the default run storage to 1,200 GiB of static storage:

```
aws omics create-workflow \
  --name {{my-workflow-name}} \
  --definition-zip fileb://{{my-definition.zip}} \
  --storage-type STATIC \
  --storage-capacity 1200
```