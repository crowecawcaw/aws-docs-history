Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Sharing compute across actions

By default, actions in a workflow run on separate instances in a
[ﬂeet](workflows-working-compute.md#compute.fleets "workflows-working-compute.md#compute.fleets"). This behavior provides actions with isolation and
predictability on the state of inputs. The default behavior requires explicit configuration to
share context such as files and variables between actions.

Compute sharing is a capability that allows you to run all the actions in a workﬂow on the same
instance. Using compute sharing can provide faster workﬂow runtimes because less time is spent
provisioning instances. You can also share files (artifacts) between actions without additional workflow
conﬁguration.

When a workflow is run using compute sharing, an instance
in the default or specified fleet is reserved for the duration of all actions in that workflow. When the
workflow run completes, the instance reservation is released.

###### Topics

- [Running multiple actions on shared compute](#how-to-compute-share "#how-to-compute-share")
- [Considerations for compute sharing](#compare-compute-sharing "#compare-compute-sharing")
- [Turning on compute sharing](#compute-sharing-steps "#compute-sharing-steps")
- [Examples](#compute-sharing-examples "#compute-sharing-examples")

## Running multiple actions on shared compute

You can use the `Compute` attribute in the
definition YAML at the workflow level to specify both the fleet and compute sharing
properties of actions. You can also configure compute properties using the visual editor in
CodeCatalyst. To specify a fleet, set the name of an existing fleet, set the compute type to
**EC2**, and turn on compute sharing.

###### Note

Compute sharing is only supported if the compute type is set to **EC2**, and
it's not supported for the Windows Server 2022 operating system. For more information about compute fleets, compute types, and properties, see [Configuring compute and runtime images](workflows-working-compute.md "workflows-working-compute.md").

###### Note

If you're on the Free tier and you specify the `Linux.x86-64.XLarge` or
`Linux.x86-64.2XLarge` fleet manually in the workflow definition YAML, the
action will still run on the default fleet (`Linux.x86-64.Large`). For more
information about compute availability and pricing, see the [table for the tiers options](https://codecatalyst.aws/explore/pricing "https://codecatalyst.aws/explore/pricing").

When compute sharing is turned on, the folder containing the workflow source is automatically copied across actions. You
don't need to configure output artifacts and reference them as input artifacts throughout a workflow definition (YAML file). As a workflow author,
you need to wire up environment variables using inputs and outputs, just as you would without using compute sharing.
If you want to share folders between actions outside the workflow source, consider file caching. For more information, see
[Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md") and
[Caching files between workflow runs](workflows-caching.md "workflows-caching.md").

The source repository where your workflow definition file resides is identified by the label
`WorkflowSource`. While using compute sharing, the workflow source is downloaded in the first action that
references it and automatically made available for subsequent actions in the workflow run to use.
Any changes made to the folder containing the workflow source by an action, such as adding, modifying, or removing
files, are also visible in the subsequent actions in the workflow. You can reference files that reside in the workflow source folder in any of
your workflow actions, just as you can without using compute sharing. For more information,
see [Referencing source repository
files](workflows-sources-reference-files.md "workflows-sources-reference-files.md").

###### Note

Compute sharing workflows need to specify a strict sequence of actions, so parallel actions can't be set.
While output
artifacts can be configured at any action in the sequence, input artifacts aren't supported.

## Considerations for compute sharing

You can run workflows with compute sharing in order to accelerate workflow runs and share context between
actions in a workflow that use the same instance. Consider the following to determine whether using compute sharing is
appropriate for your scenario:

|                                        | Compute sharing                                                   | Without compute sharing                                                |
| -------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Compute type                           | Amazon EC2                                                        | Amazon EC2, AWS Lambda                                                 |
| Instance provisioning                  | Actions run on same instance                                      | Actions run on separate instances                                      |
| Operating system                       | Amazon Linux 2                                                    | Amazon Linux 2, Windows Server 2022 (build action only)                |
| Referencing files                      | `$CATALYST_SOURCE_DIR_WorkflowSource`, `/sources/WorkflowSource/` | `$CATALYST_SOURCE_DIR_WorkflowSource`, `/sources/WorkflowSource/`      |
| Workflow structure                     | Actions can only run sequentially                                 | Actions can run parallel                                               |
| Accessing data across workflow actions | Access cached workflow source (`WorkflowSource`)                  | Access outputs of shared artifacts (requires additional configuration) |

## Turning on compute sharing

Use the following instruction to turn on compute sharing for a workflow.

Visual

###### To turn on compute sharing using the visual editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow.
5. Choose **Edit**.
6. Choose **Visual**.
7. Choose **Workflow properties**.
8. From the **Compute type** dropdown menu, choose
   **EC2**.
9. (Optional) From the **Compute fleet - optional** dropdown
   menu, choose a fleet you want to use to run workflow actions. You can choose an
   on-demand fleet or create and choose a provisioned fleet. For more information, see
   [Creating a provisioned fleet](projects-create-compute-resource.md "projects-create-compute-resource.md") and
   [Assigning a fleet or compute to an
   action](workflows-assign-compute-resource.md "workflows-assign-compute-resource.md")
10. Switch the toggle to turn on compute sharing and have actions in the
    workflow run on the same fleet.
11. (Optional) Choose the run mode for the workflow. For more information,
    see [Configuring the queuing behavior of runs](workflows-configure-runs.md "workflows-configure-runs.md").
12. Choose **Commit**, enter a commit message, and
    choose **Commit** again.

YAML

###### To turn on compute sharing using the YAML editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow.
5. Choose **Edit**.
6. Choose **YAML**.
7. Turn on compute sharing setting the `SharedInstance` field
   to `TRUE` and `Type` to `EC2`. Set
   `Fleet` to a compute fleet you want to use to run workflow actions.
   You can choose an on-demand fleet or create and choose a provisioned fleet.
   For more information, see
   [Creating a provisioned fleet](projects-create-compute-resource.md "projects-create-compute-resource.md") and
   [Assigning a fleet or compute to an
   action](workflows-assign-compute-resource.md "workflows-assign-compute-resource.md")

In a workflow YAML, add code similar to the following:

```

  Name: MyWorkflow
  SchemaVersion: "1.0"
  Compute: # Define compute configuration.
    Type: EC2
    Fleet: `MyFleet` # Optionally, choose an on-demand or provisioned fleet.
    SharedInstance: true # Turn on compute sharing. Default is False.
  Actions:
    BuildFirst:
      Identifier: aws/build@v1
      Inputs:
        Sources:
          - WorkflowSource
      Configuration:
        Steps:
          - Run: ...
          ...

```

8. (Optional) Choose **Validate** to validate the
   workflow's YAML code before committing.
9. Choose **Commit**, enter a commit message, and
   choose **Commit** again.

## Examples

###### Topics

- [Example: Amazon S3 Publish](#compute-share-s3 "#compute-share-s3")

### Example: Amazon S3 Publish

The following workflow examples show how to perform the Amazon Amazon S3 Publish action in
two ways: first using input artifacts and then using compute sharing. With compute sharing,
the input artifacts aren't needed since you can access the cached
`WorkflowSource`. Additionally, the output artifact in the Build action is no
longer needed. The S3 Publish action is configured to use the explicit `DependsOn` property
to maintain sequential actions; the Build action must run successfully in order for the S3
Publish action to run.

- Without compute sharing, you need to use input artifacts and share the outputs with subsequent actions:

```

Name: S3PublishUsingInputArtifact
SchemaVersion: "1.0"
Actions:
  Build:
    Identifier: aws/build@v1
    Outputs:
      Artifacts:
        - Name: ArtifactToPublish
          Files: [output.zip]
    Inputs:
      Sources:
        - WorkflowSource
    Configuration:
      Steps:
        - Run: ./build.sh # Build script that generates output.zip
  PublishToS3:
    Identifier: aws/s3-publish@v1
    Inputs:
      Artifacts:
      - ArtifactToPublish
    Environment:
      Connections:
        - Role: codecatalyst-deployment-role
          Name: dev-deployment-role
      Name: dev-connection
    Configuration:
      SourcePath: output.zip
      DestinationBucketName: amzn-s3-demo-bucket

```

- When using compute sharing by setting `SharedInstance` to `TRUE`,
  you can run multiple actions on the same instance and share artifacts by specifying a single
  workflow source. Input artifacts aren't required and can't be specified:

```

Name: S3PublishUsingComputeSharing
SchemaVersion: "1.0"
Compute:
  Type: EC2
  Fleet: dev-fleet
  SharedInstance: TRUE
Actions:
  Build:
    Identifier: aws/build@v1
    Inputs:
      Sources:
        - WorkflowSource
    Configuration:
      Steps:
        - Run: ./build.sh # Build script that generates output.zip
  PublishToS3:
    Identifier: aws/s3-publish@v1
    DependsOn:
      - Build
    Environment:
      Connections:
        - Role: codecatalyst-deployment-role
          Name: dev-deployment-role
      Name: dev-connection
    Configuration:
      SourcePath: output.zip
      DestinationBucketName: amzn-s3-demo-bucket

```
