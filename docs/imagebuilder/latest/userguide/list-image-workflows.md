

# List image workflows
<a name="list-image-workflows"></a>

On the **Image workflows** list page in the Image Builder console, you can get a list of the image workflow resources that you own or have access to, along with some key details about these resources. You can also use commands or actions with the Image Builder API, SDKs, or AWS CLI to list image workflows in your account.

You can use one of the following methods to list image workflow resources that you own or have access to. For the API action, see [ListWorkflows](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWorkflows.html) in the *EC2 Image Builder API Reference*. For the associated SDK request, refer to the [See Also](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWorkflows.html#API_ListWorkflows_SeeAlso) link on the same page.

You can filter on the following details to streamline the list of results. For example, if you filter on **Owner = Amazon** in the console, the list displays only AWS managed workflows.
+ Workflow
+ Version
+ Type
+ Owner

------
#### [ Console ]

**Workflow details**  
Details on the **Image workflows** list page in the Image Builder console include the following:
+ **Workflow** – The name of the most recent version of the image workflow resource. In the Image Builder console, the **Workflow** column links to the workflow detail page.
+ **Version** – The most recent version of the image workflow resource.
+ **Type** – The workflow type: `BUILD`, `TEST`, or `DISTRIBUTION`.
+ **Owner** – The owner of the workflow resource.
+ **Creation time** – The date and time when Image Builder created the most recent version of the image workflow resource.
+ **ARN** – The Amazon Resource Name (ARN) of the current version of the image workflow resource.

**List image workflows**  
To list image workflow resources in the Image Builder console, perform the following steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Image workflows** from the navigation pane.

**Filter results**  
On the **Image workflows** list page, you can search for specific image workflows to filter your results. The following filters are available for image workflows:

`Workflow`

You can enter all or part of a workflow name to streamline results. The default is to show all workflows in the list.

`Version`

You can enter all or part of a version number to streamline results. The default is to show all versions in the list.

`Type`

You can filter by the workflow type or view all types. The default is to show all workflow types in the list.
+ *BUILD*
+ *TEST*
+ *DISTRIBUTION*

`Owner`

When you select the owner filter from the search bar, Image Builder shows a list of the owners for the image workflows in your account. You can select an owner from the list to streamline results. The default is to show all owners in the list.
+ *AWS account* – The account that owns the workflow resource.
+ *Amazon* – The AWS managed build, test, and distribution workflow resources that Amazon owns and manages.

------
#### [ AWS CLI ]

When you run the **[list-workflows](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-workflows.html)** command in the AWS CLI, you can get a list of image workflows that you own or have access to.

The following command example shows how to use the **list-workflows** command without filters to list all of the Image Builder image workflow resources that you own or have access to.

**Example: list all image workflows**

```
aws imagebuilder list-workflows
```

**Output:**

```
{
    "workflowVersionList": [
        {
            "name": "{{example-test-workflow}}",
            "dateCreated": "2023-11-21T22:53:14.347Z",
            "version": "1.0.0",
            "owner": "{{111122223333}}",
            "type": "TEST",
            "arn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:workflow/test/{{example-test-workflow}}/{{1.0.0}}"
        },
        {
            "name": "{{example-build-workflow}}",
            "dateCreated": "2023-11-20T12:26:10.425Z",
            "version": "1.0.0",
            "owner": "{{111122223333}}",
            "type": "BUILD",
            "arn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:workflow/build/{{example-build-workflow}}/{{1.0.0}}"
        },
        {
            "name": "{{example-distribution-workflow}}",
            "dateCreated": "2025-11-19T10:25:10.425Z",
            "version": "1.0.0",
            "owner": "{{111122223333}}",
            "type": "DISTRIBUTION",
            "arn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:workflow/distribution/{{example-distribution-workflow}}/{{1.0.0}}"
        }
    ]
}
```

When you run the **list-workflows** command, you can apply filters to streamline the results, as the following example shows. For more information about how to filter your results, see the [list-workflows](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-workflows.html) command in the *AWS CLI Command Reference*.

**Example: filter for build workflows**

```
aws imagebuilder list-workflows --filters name="{{type}}",values="{{BUILD}}"
```

**Output:**

```
{
    "workflowVersionList": [
        {
            "name": "{{example-build-workflow}}",
            "dateCreated": "2023-11-20T12:26:10.425Z",
            "version": "1.0.0",
            "owner": "{{111122223333}}",
            "type": "BUILD",
            "arn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:workflow/build/{{example-build-workflow}}/{{1.0.0}}"
        }
    ]
}
```

**Get workflow details**  
To get the details for a specific image workflow version, run the [get-workflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-workflow.html) command in the AWS CLI. For the API action, see [GetWorkflow](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetWorkflow.html) in the *EC2 Image Builder API Reference*.

**Example: get workflow details**

```
aws imagebuilder get-workflow \
    --workflow-build-version-arn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:workflow/build/{{example-build-workflow}}/{{1.0.0}}/{{1}}
```

The response includes the workflow `type`, `state`, `data` (the YAML workflow document), `parameters`, `owner`, and `kmsKeyId`.

------