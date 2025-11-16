# Create a private workflow

Create a workflow using the HealthOmics console, AWS CLI commands, or one of the AWS SDKs.

###### Note

Don’t include any personally identifiable information (PII) in workflow names. These names are visible in
CloudWatch logs.

When you create a workflow, HealthOmics assigns a universally unique identifier (UUID) to the workflow. The workflow UUID is a Globally Unique
Identifier (guid) that's unique across workflows and workflow versions. For data provenance purposes, we recommend
that you use the workflow UUID to uniquely identify workflows.

If your workflow tasks use any external tools (executables, libraries, or scripts), you build these tools into a
container image. You have the following options for hosting the container image:

- Host the container image in the ECR private registry. Prerequisites for this option:
  - Create an ECR private repository, or choose an existing repository.
  - Configure the ECR resource policy as described in [Amazon ECR permissions](permissions-ecr.md "permissions-ecr.md").
  - Upload your container image to the private repository.

- Synchronize the container image with the contents of a supported third-party registry.
  Prerequisites for this option:

      + In the ECR private registry, configure a pull through cache rule for each upstream registry. For more
       information, see [Image mappings](workflows-ecr.md#ecr-pull-through-mapping-format "workflows-ecr.md#ecr-pull-through-mapping-format") .
      + Configure the ECR resource policy as described in [Amazon ECR permissions](permissions-ecr.md "permissions-ecr.md").
      + Create repository creation templates. The template defines settings for when Amazon ECR creates the private
       repository for an upstream registry.
      + Create prefix mappings to remap container image references in the workflow definition to ECR cache
       namespaces.

  When you create a workflow, you provide a workflow definition that contains information about the workflow,
  runs, and tasks. HealthOmics can retrieve the workflow definition as a .zip archive stored locally or in an Amazon S3
  bucket, or from a supported Git-based repository.

###### Topics

- [Creating a workflow using the console](#console-create-workflows "#console-create-workflows")
- [Creating a workflow using the CLI](#api-create-workflows "#api-create-workflows")
- [Creating a workflow using an SDK](#sdk-create-workflows "#sdk-create-workflows")

## Creating a workflow using the console

###### Steps to create a workflow

1.  Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2.  If required, open the left navigation pane (≡). Choose **Private workflows**.
3.  On the **Private workflows** page, choose **Create
    workflow**.
4.  On the **Define workflow** page, provide the
    following information:
    1. **Workflow name**: A distinctive name for this workflow. We recommend setting workflow
       names to organize your runs in the AWS HealthOmics console and CloudWatch logs.
    2. **Description** (optional): A description of this workflow.

5.  In the **Workflow definition** panel, provide the following information:
    1.  **Workflow language** (optional): Select the specification language of the
        workflow. Otherwise, HealthOmics determines the language from the workflow definition.
    2.  For **Workflow definition source**, choose to import the definition folder from a
        Git-based repository, an Amazon S3 location, or from a local drive.
        1. For **Import from a repository service**:

        ###### Note

        HealthOmics supports public and private repositories for GitHub, GitLab,
        Bitbucket, GitHub self-managed, GitLab self-managed.

            1. Choose a **Connection** to connect your AWS resources to the external repository.
             To create a connection, see [Connect with external code repositories](setting-up-new.md#setting-up-omics-repository "setting-up-new.md#setting-up-omics-repository").


            ###### Note

            Customers in the TLV region need to create a connection in the IAD
             (us-east-1) region to create a workflow.
            2. In **Full repository ID**, enter your repository ID as user-name/repo-name.
             Verify you have access to the files in this repository.
            3. In **Source reference** (optional), enter a repository source reference (branch,
             tag, or commit ID). HealthOmics uses the default branch if no source reference is specified.
            4. In **Exclude file patterns**, enter the file patterns to exclude specific folders,
             files, or extensions. This helps manage data size when importing repository files. There is a max of 50
             patterns, and the patters must follow the
             [glob pattern syntax](https://fossil-scm.org/home/doc/tip/www/globs.md "https://fossil-scm.org/home/doc/tip/www/globs.md"). For example:




            	1. `tests/`
            	2. `*.jpeg`
            	3. `large_data.zip`

        2. For **Select definition folder from S3**:
           1. Enter the Amazon S3 location that contains the zipped workflow definition folder. The Amazon S3 bucket
              must be in the same region as the workflow.
           2. If your account doesn't own the Amazon S3 bucket, enter the bucket owner's AWS account ID in the **S3
              bucket owner's account ID**. This information is required so that HealthOmics can verify the bucket ownership.

        3. For **Select definition folder from a local source**:
           1. Enter the local drive location of the zipped workflow definition folder.

    3.  **Main workflow definition file path** (optional): Enter the file path from the
        zipped workflow definition folder or repository to the `main` file. This parameter is not
        required if there is only one file in the workflow definition folder, or if the main file is named "main".

6.  In the **README file** (optional) panel,
    select the **Source of the README file** and provide the following information:
    - For **Import from a repository service**, in **README file path**,
      enter the path to the README file within the repository.
    - For **Select file from S3**, in **README file in S3**, enter
      the Amazon S3 URI for the README file.
    - For **Select file from a local source**: in **README -
      optional**, chose **Choose file** to select the markdown (.md) file to
      upload.

7.  In the **Default run storage configuration** panel, provide the default run storage type
    and capacity for runs that use this workflow:
    1. **Run storage type**: Choose whether to use static or dynamic storage as
       the default for the temporary run storage. The default is static storage.
    2. **Run storage capacity** (optional): For static run storage type, you can enter the
       default amount of run storage required for this workflow. The default value for this parameter is 1200 GiB.
       You can override these default values when you start a run.

8.  **Tags** (optional): You can associate up to 50 tags with this workflow.
9.  Choose **Next**.
10. On the **Add workflow parameters** (optional) page, select the **Parameter source**:
    1. For **Parse from workflow definition file**, HealthOmics will automatically parse the
       workflow parameters from the workflow definition file.
    2. For **Provide parameter template from Git repository**, use the path to the
       parameter template file from your repository.
    3. For **Select JSON file from local source**, upload a JSON
       file from a local source that specifies the parameters.
    4. For **Manually enter workflow parameters**, manually enter parameter names and descriptions.

11. In the **Parameter preview** panel, you can review or change the parameters for
    this workflow version. If you restore the JSON file, you lose any local changes that you made.
12. Choose **Next**.
13. On the **Container URI remapping** page, in the **Mapping rules**
    panel, you can define URI mapping rules for your workflow.

For **Source of mapping file**, select one of the following options:

    * **None** – No mapping rules required.
    * **Select JSON file from S3** – Specify the S3 location for the mapping file.
    * **Select JSON file from a local source** – Specify the mapping file location
     on your local device.
    * **Manually enter mappings** – enter the registry mappings and image mappings in
     the **Mappings** panel.

14. The console displays the **Mappings** panel. If you chose a mapping source file,
    the console displays the values from the file.
    1.  In **Registry mappings**, you can edit the mappings or add mappings (maximum of
        20 registry mappings).

    Each registry mapping contains the following fields:

        * **Upstream registry URL** – The URI of the upstream registry.
        * **ECR repository prefix** –
         The repository prefix to use in the Amazon ECR private repository.
        * (Optional) **Upstream repository prefix** –
         The prefix of the repository in the upstream registry.
        * (Optional) **ECR account ID** –
         Account ID of the account that owns the upstream container image.

    2.  In **Image mappings**, you can edit the image mappings or add mappings (maximum of
        100 image mappings).

    Each image mapping contains the following fields:

        * **Source image** –
         Specifies the URI of the source image in the upstream registry.
        * **Destination image** –
         Specifies the URI of the corresponding image in the private Amazon ECR registry.

15. Choose **Next**.
16. Review the workflow configuration, then choose **Create workflow**.

## Creating a workflow using the CLI

If your workflow files and the parameter template file are on your local machine, you can create a workflow using the following CLI command.

```
aws omics create-workflow  \
  --name "my_workflow"   \
  --definition-zip fileb://my-definition.zip \
  --parameter-template file://my-parameter-template.json
```

The `create-workflow` operation returns the following response:

```
{
  "arn": "arn:aws:omics:us-west-2:....",
  "id": "1234567",
  "status": "CREATING",
  "tags": {
      "resourceArn": "arn:aws:omics:us-west-2:...."
  },
  "uuid": "64c9a39e-8302-cc45-0262-2ea7116d854f"
}
```

### Optional parameters to use when creating a workflow

You can specify any of the optional parameters when you create a workflow. For syntax details, see [CreateWorkflow](../api/API_CreateWorkflow.md "../api/API_CreateWorkflow.md") in the
AWS HealthOmics API Reference.

###### Topics

- [Specify the workflow definition Amazon S3 location](#create-defn-uri-parameter "#create-defn-uri-parameter")
- [Use the workflow definition from a Git-based repository](#create-defn-uri-git "#create-defn-uri-git")
- [Specify a Readme file](#specify-readme-file "#specify-readme-file")
- [Specify the main definition file](#create-main-parameter "#create-main-parameter")
- [Specify the run storage type](#create-run-storage-parameter "#create-run-storage-parameter")
- [Specify the GPU configuration](#create-accelerator-parameter "#create-accelerator-parameter")
- [Configure pull through cache mapping parameters](#create-prefix-mapping-parameters "#create-prefix-mapping-parameters")

#### Specify the workflow definition Amazon S3 location

If your workflow definition file is located in an Amazon S3 folder, specify the location using the
`definition-uri` parameter, as shown in the following example. If your account does not own the Amazon S3
bucket, provide the owner's AWS account ID.

```
aws omics create-workflow  \
  --name Test  \
  --definition-uri s3://omics-bucket/workflow-definition/  \
  --owner-id  123456789012
    ...
```

#### Use the workflow definition from a Git-based repository

To use the workflow definition from a supported Git-based repository, use the `definition-repository`
parameter in your request. Don’t provide any other `definition` parameter, as a request fails if it
includes more than one input source.

The `definition-respository` parameter contains the following fields:

- **connectionArn** – ARN of the Code Connection that connects your AWS resources to
  the external repository.
- **fullRepositoryId** – Enter the repository ID as `owner-name/repo-name`.
  Verify you have access to the files in this repository.
- **sourceReference** (Optional) – Enter a repository reference type (BRANCH, TAG, or COMMIT) and a value.

HealthOmics uses the latest commit on the default branch if you don't specify a source reference.

- **excludeFilePatterns** (Optional) – Enter the file patterns to exclude specific folders, files, or extensions. This helps manage data
  size when importing repository files. Provide a maximum of 50 patterns. the patterns must follow the
  [glob pattern syntax](https://fossil-scm.org/home/doc/tip/www/globs.md "https://fossil-scm.org/home/doc/tip/www/globs.md"). For
  example:
  - `tests/`
  - `*.jpeg`
  - `large_data.zip`

When you specify the workflow definition from a Git-based repository, use `parameter-template-path` to
specify the parameter template file. If you don’t provide this parameter, HealthOmics creates the workflow
without a parameter template.

The following example shows the parameters related to content from a Git-based private repository:

```
aws omics create-workflow \
    --name custom-variant \
    --description "Custom variant calling pipeline" \
    --engine "WDL" \
    --definition-repository '{
            "connectionArn": "arn:aws:codeconnections:us-east-1:123456789012:connection/abcd1234-5678-90ab-cdef-1234567890ab",
            "fullRepositoryId": "myorg/my-genomics-workflows",
            "sourceReference": {
                "type": "BRANCH",
                "value": "main"
            },
            "excludeFilePatterns": ["tests/**", "*.log"]
      }' \
    --main "workflows/variant-calling/main.wdl" \
    --parameter-template-path "parameters/variant-calling-params.json" \
    --readme-path "docs/variant-calling-README.md" \
    --storage-type "DYNAMIC" \
```

For more examples, see the blog post [How To Create an AWS HealthOmics Workflows from Content in Git](https://repost.aws/articles/ARCEN7AjhaRSmteczRoc_QsA/how-to-create-an-aws-healthomics-workflows-from-content-in-git "https://repost.aws/articles/ARCEN7AjhaRSmteczRoc_QsA/how-to-create-an-aws-healthomics-workflows-from-content-in-git").

#### Specify a Readme file

You can specify the README file location using one of the following parameters:

- **readme-markdown** – String input or a file on your local machine.
- **readme-uri** – The URI of a file stored on S3.
- **readme-path** – The path to the README file in the repository.

Use readme-path only in conjunction with **definition-respository**. If
you don’t specify any README parameter, HealthOmics imports the root level README.md file in the
repository (if it exists).

The following examples show how specify the README file location using readme-path and readme-uri.

```
# Using README from repository
aws omics create-workflow \
    --name "documented-workflow" \
    --definition-repository '...' \
    --readme-path "docs/workflow-guide.md"

# Using README from S3
aws omics create-workflow \
    --name "s3-readme-workflow" \
    --definition-repository '...' \
    --readme-uri "s3://my-bucket/workflow-docs/readme.md"
```

For more information, see [HealthOmics Workflow README files](workflows-readme.md "workflows-readme.md").

#### Specify the **main** definition file

If you are including multiple workflow definition files, use the `main` parameter to specify
the main definition file for your workflow.

```
aws omics create-workflow  \
  --name Test  \
  --main multi_workflow/workflow2.wdl  \
    ...
```

#### Specify the run storage type

You can specify the default run storage type (DYNAMIC or STATIC) and run storage capacity (required for
static storage). For more information about run storage types, see [Run storage types in HealthOmics workflows](workflows-run-types.md "workflows-run-types.md").

```
aws omics create-workflow  \
  --name my_workflow   \
  --definition-zip fileb://my-definition.zip \
  --parameter-template file://my-parameter-template.json   \
  --storage-type 'STATIC'  \
  --storage-capacity 1200  \
```

#### Specify the GPU configuration

Use the accelerators parameter to create a workflow that runs on an accelerated-compute instance. The
following example shows how to use the `accelerators` parameter. You specify the GPU configuration
in the workflow definition. See [Accelerated-computing instances](memory-and-compute-tasks.md#workflow-task-accelerated-computing-instances "memory-and-compute-tasks.md#workflow-task-accelerated-computing-instances").

```
aws omics create-workflow --name ``workflow name`` \
   --definition-uri s3://amzn-s3-demo-bucket1/GPUWorkflow.zip \
   --accelerators GPU
```

#### Configure pull through cache mapping parameters

If you're using the Amazon ECR pull through cache mapping feature, you can override the default mappings. For
more information about the container setup parameters, see [Container images for private workflows](workflows-ecr.md "workflows-ecr.md").

In the following example, file `mappings.json` contains this content:

```
{
    "registryMappings": [
        {
            "upstreamRegistryUrl": "registry-1.docker.io",
            "ecrRepositoryPrefix": "docker-hub"
        },
        {
            "upstreamRegistryUrl": "quay.io",
            "ecrRepositoryPrefix": "quay",
            "accountId": "123412341234"
        },
        {

            "upstreamRegistryUrl": "public.ecr.aws",
            "ecrRepositoryPrefix": "ecr-public"
        }
    ],
    "imageMappings": [{
            "sourceImage": "docker.io/library/ubuntu:latest",
            "destinationImage": "healthomics-docker-2/custom/ubuntu:latest",
            "accountId": "123412341234"
        },
        {
            "sourceImage": "nvcr.io/nvidia/k8s/dcgm-exporter",
            "destinationImage": "healthomics-nvidia/k8s/dcgm-exporter"
        }
    ]
}
```

Specify the mapping parameters in the create-workflow command:

```
aws omics create-workflow  \
     ...
--container-registry-map-file file://mappings.json
    ...
```

You can also specify the S3 location of the mapping parameters file:

```
aws omics create-workflow  \
     ...
--container-registry-map-uri s3://amzn-s3-demo-bucket1/test.zip
    ...
```

## Creating a workflow using an SDK

You can create a workflow using one of the SDKs. The following example shows how to create a workflow using
the Python SDK

```
import boto3

omics = boto3.client('omics')

with open('definition.zip', 'rb') as f:
   definition = f.read()

response = omics.create_workflow(
   name='my_workflow',
   definitionZip=definition,
   parameterTemplate={ ... }
)
```
