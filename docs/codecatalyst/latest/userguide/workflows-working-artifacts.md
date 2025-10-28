Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Sharing artifacts and files between

actions

An _artifact_ is the output of a workflow action, and typically consists
of a folder or archive of files. Artifacts are important because they allow you to share files
and information between actions.

For example, you might have a build action that _generates_ a
`sam-template.yml` file, but you want a deploy action to
_use_ it. In this scenario, you would use an artifact to allow the
build action to share the `sam-template.yml` file with the deploy action.
The code might look something like this:

```
Actions:
  BuildAction:
    Identifier: aws/build@v1
    Steps:
      - Run: sam package --output-template-file sam-template.yml
    **Outputs:
 Artifacts:
 - Name: MYARTIFACT
 Files:
 - sam-template.yml**
  DeployAction:
    Identifier: aws/cfn-deploy@v1
    **Inputs:
 Artifacts:
 - MYARTIFACT**
    Configuration:
      template: sam-template.yml
```

In the previous code, the build action (`BuildAction`) generates a
`sam-template.yml` file, and then adds it to an output artifact
called `MYARTIFACT`. A subsequent deploy action (`DeployAction`)
specifies `MYARTIFACT` as an input, giving it access to the
`sam-template.yml` file.

###### Topics

- [Can I share artifacts without
  specifying them as outputs and inputs?](#workflows-working-artifacts-share "#workflows-working-artifacts-share")
- [Can I share artifacts between
  workflows?](#workflows-working-artifacts-share-wf "#workflows-working-artifacts-share-wf")
- [Examples of artifacts](workflows-working-artifacts-ex.md "workflows-working-artifacts-ex.md")
- [Defining an output artifact](workflows-working-artifacts-output.md "workflows-working-artifacts-output.md")
- [Defining an input artifact](workflows-working-artifacts-refer.md "workflows-working-artifacts-refer.md")
- [Referencing files in an
  artifact](workflows-working-artifacts-refer-files.md "workflows-working-artifacts-refer-files.md")
- [Downloading artifacts](workflows-download-workflow-outputs.md "workflows-download-workflow-outputs.md")

## Can I share artifacts without

specifying them as outputs and inputs?

Yes, you can share artifacts between actions without specifying them in the
`Outputs` and `Inputs` sections of your actions' YAML code. To
do this, you must turn on compute sharing. For more information about compute sharing
and how to specify artifacts when it is turned on, see [Sharing compute across actions](compute-sharing.md "compute-sharing.md").

###### Note

Although the compute sharing feature allows you to simplify your workflow's YAML
code by eliminating the need for the `Outputs` and `Inputs`
sections, the feature has limitations that you should be aware of before you turn it
on. For information about these limitations, see [Considerations for compute sharing](compute-sharing.md#compare-compute-sharing "compute-sharing.md#compare-compute-sharing").

## Can I share artifacts between

workflows?

No, you cannot share artifacts between different workflows; however, you can share
artifacts between actions within the same workflow.
