

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Referencing files in an artifact
<a name="workflows-working-artifacts-refer-files"></a>

If you have a file that resides within an artifact, and you need to refer to this file in one of your Amazon CodeCatalyst workflow actions, complete the following procedure.

**Note**  
See also [Referencing source repository files](workflows-sources-reference-files.md).

------
#### [ Visual ]

*Not available. Choose YAML to view the YAML instructions.*

------
#### [ YAML ]

**To reference files in an artifact (YAML editor)**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **YAML**.

1. In the action where you want to reference a file, add code similar to the following:

   ```
   Actions:
     My-action:
       Inputs:
         Sources:
           - WorkflowSource
         Artifacts:
           - {{artifact-name}}  
       Configuration:
         template: {{artifact-path}}/path/to/file.yml
   ```

   In the previous code, replace:
   + {{artifact-name}} with the name of the artifact.
   + {{artifact-path}} with a value from the following table.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-artifacts-refer-files.html)

   For examples, see [Examples of artifacts](workflows-working-artifacts-ex.md).
**Note**  
You can omit the {{artifact-path}} and just specify the file path relative to the artifact root directory if:  
The action where you're including the reference only includes one item under `Inputs` (for example, it includes one input artifact and no source).
The file that you want to reference resides in the primary input. The *primary input* is either the `WorkflowSource`, or the first input artifact listed, if there is no `WorkflowSource`.

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------