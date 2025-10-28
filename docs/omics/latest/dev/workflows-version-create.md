AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Create a workflow version

When you create a new version of a workflow, you need to specify the configuration values for the new version.
It doesn't inherit any configuration values from the workflow.

When you create the version, provide a version name that is unique for this workflow. You cannot change the name
after HealthOmics creates the version.

The version name must start with a letter or number and it can include upper-case and lower-case letters,
numbers, hyphens, periods and underscores. The maximum length is 64 characters. For example, you can use a simple
naming scheme, such as version1, version2, version3. You can also match your workflow versions with your own
internal versioning conventions, such as 2.7.0, 2.7.1, 2.7.2.

Optionally, use the version description field to add notes about this version. For example: **Fix for
syntax error in workflow definition**.

###### Note

Don’t include any personally identifiable information (PII) in the version name. Version names appear in the workflow
version ARN.

HealthOmics assigns a unique ARN to the workflow version. The ARN is unique based on the combination of workflow ID and
version name.

###### Warning

After you delete a workflow version, HealthOmics lets you reuse the version name for a different workflow version. Best
practice is to not reuse version names. If you do reuse a name, the workflow and each version have a unique UUID that you
can use for provenance.

###### Topics

- [Create a workflow version using the console](#workflow-versions-console-create "#workflow-versions-console-create")
- [Create a workflow version using the CLI](#workflow-versions-api-create "#workflow-versions-api-create")
- [Create a workflow version using an SDK](#workflow-versions-sdk "#workflow-versions-sdk")
- [Verify the status of a workflow version](#using-get-workflow "#using-get-workflow")

## Create a workflow version using the console

###### Steps to create a workflow version

1.  Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2.  If required, open the left navigation pane (≡). Choose **Private workflows**.
3.  On the **Private workflows** page, choose the workflow
    for the new version.
4.  On the **Workflow details** page, choose **Create
    new version**.
5.  On the **Create version** page, provide the
    following information:
    1. **Version name**: Enter a name for the workflow version that is unique across the
       workflow.
    2. **Version description** (optional): You can use the description field to add notes
       about this version.

6.  In the **Workflow definition** panel, provide the
    following information:
    1.  **Workflow language** (optional): Select the specification language for the
        workflow version. Otherwise, HealthOmics determines the language from the workflow definition.
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

7.  In the **README file** (optional) panel,
    select the **Source of the README file** and provide the following information:
    - For **Import from a repository service**, in **README file path**,
      enter the path to the README file within the repository.
    - For **Select file from S3**, in **README file in S3**, enter
      the Amazon S3 URI for the README file.
    - For **Select file from a local source**: in **README -
      optional**, chose **Choose file** to select the markdown (.md) file to
      upload.

8.  In the **Default run storage configuration** panel, provide the default run storage type
    and capacity for runs that use this workflow:
    1. **Run storage type**: Choose whether to use static or dynamic storage as
       the default for the temporary run storage. The default is static storage.
    2. **Run storage capacity** (optional): For static run storage type, you can enter the
       default amount of run storage required for this workflow. The default value for this parameter is 1200 GiB.
       You can override these default values when you start a run.

9.  **Tags** (optional): You can associate up to 50 tags with this workflow version.
10. Choose **Next**.
11. On the **Add workflow parameters** (optional) page, select the **Parameter source**:
    1. For **Parse from workflow definition file**, HealthOmics will automatically parse the
       workflow parameters from the workflow definition file.
    2. For **Provide parameter template from Git repository**, use the path to the
       parameter template file from your repository.
    3. For **Select JSON file from local source**, upload a JSON
       file from a local source that specifies the parameters.
    4. For **Manually enter workflow parameters**, manually enter parameter names and descriptions.

12. In the **Parameter preview** panel, you can review or change the parameters for
    this workflow version. If you restore the JSON file, you lose any local changes that you made.
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
16. Review the version configuration, then choose **Create version**.

When the version is created, the console returns to the workflow detail page and displays the
new version in the **Workflows and versions** table.

## Create a workflow version using the CLI

You can create a workflow version using the `CreateWorkflowVersion` API operation.
For optional parameters, HealthOmics uses the following defaults:

| Parameter                             | Default                                                                                                                                                                                             |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Engine                                | Determined from the workflow definition                                                                                                                                                             |
| Storage type                          | STATIC                                                                                                                                                                                              |
| Storage capacity (for static storage) | 1200 GiB                                                                                                                                                                                            |
| Main                                  | Determined based on the contents of the workflow definition folder. For details, see [HealthOmics workflow definition requirements](workflow-defn-requirements.md "workflow-defn-requirements.md"). |
| Accelerators                          | none                                                                                                                                                                                                |
| Tags                                  | none                                                                                                                                                                                                | The following CLI example creates a workflow version with static storage as the default run storage: `aws omics create-workflow-version \ --workflow-id 1234567  \ --version-name "my_version" \ --engine WDL \ --definition-zip fileb://workflow-crambam.zip \ --description "my version description" \ --main file://workflow-params.json \ --parameter-template file://workflow-params.json \ --storage-type='STATIC'   \ --storage-capacity 1200   \ --tags example123=string  \ --accelerators GPU` If your workflow definition file located in an Amazon S3 folder, enter the location using the `definition-uri` parameter instead of `definition-zip`. For more information, see [CreateWorkflowVersion](../api/API_CreateWorkflowVersion.md "../api/API_CreateWorkflowVersion.md") in the AWS HealthOmics API Reference. You receive the following response to the `create-workflow-version` request. `{ "workflowId": "1234567", "versionName": "my_version", "arn": "arn:aws:omics:us-west-2:123456789012:workflow/1234567/version/3", "status": "ACTIVE", "tags": { "environment": "production", "owner": "team-alpha" }, "uuid": "0ac9a563-355c-fc7a-1b47-a115167af8a2" }` ## Create a workflow version using an SDK You can create a workflow using one of the SDKs. The following example shows how to create a workflow version using the Python SDK `import boto3 omics = boto3.client('omics') with open('definition.zip', 'rb') as f: definition = f.read() response = omics.create_workflow_version( workflowId='1234567', versionName='my_version', requestId='my_request_1' definitionZip=definition, parameterTemplate={ ... } )` ## Verify the status of a workflow version After you create your workflow version, you can verify the status and view other details of the workflow using **get-workflow-version**, as shown. `aws omics get-workflow-version --workflow-id 9876543 --version-name "my_version"` The response gives you your workflow details, including the status, as shown. `{ "workflowId": "1234567", "versionName": "3.0.0", "arn": "arn:aws:omics:us-west-2:123456789012:workflow/1234567/version/3.0.0", "status": "ACTIVE", "description": ... "uuid": "0ac9a563-355c-fc7a-1b47-a115167af8a2" }` Before you can start a run with this workflow version, the status must transition to `ACTIVE`. |
