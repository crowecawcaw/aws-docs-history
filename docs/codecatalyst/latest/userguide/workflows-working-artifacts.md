

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Sharing artifacts and files between actions
<a name="workflows-working-artifacts"></a>

An *artifact* is the output of a workflow action, and typically consists of a folder or archive of files. Artifacts are important because they allow you to share files and information between actions.

For example, you might have a build action that *generates* a `sam-template.yml` file, but you want a deploy action to *use* it. In this scenario, you would use an artifact to allow the build action to share the `sam-template.yml` file with the deploy action. The code might look something like this:

```
Actions:
  BuildAction:
    Identifier: aws/build@v1
    Steps:
      - Run: sam package --output-template-file sam-template.yml
    Outputs:
      Artifacts:
        - Name: MYARTIFACT
          Files:
            - sam-template.yml
  DeployAction:
    Identifier: aws/cfn-deploy@v1  
    Inputs:
      Artifacts:
        - MYARTIFACT
    Configuration:
      template: sam-template.yml
```

In the previous code, the build action (`BuildAction`) generates a `sam-template.yml` file, and then adds it to an output artifact called `MYARTIFACT`. A subsequent deploy action (`DeployAction`) specifies `MYARTIFACT` as an input, giving it access to the `sam-template.yml` file.

**Topics**
+ [Can I share artifacts without specifying them as outputs and inputs?](#workflows-working-artifacts-share)
+ [Can I share artifacts between workflows?](#workflows-working-artifacts-share-wf)
+ [Examples of artifacts](workflows-working-artifacts-ex.md)
+ [Defining an output artifact](workflows-working-artifacts-output.md)
+ [Defining an input artifact](workflows-working-artifacts-refer.md)
+ [Referencing files in an artifact](workflows-working-artifacts-refer-files.md)
+ [Downloading artifacts](workflows-download-workflow-outputs.md)

## Can I share artifacts without specifying them as outputs and inputs?
<a name="workflows-working-artifacts-share"></a>

Yes, you can share artifacts between actions without specifying them in the `Outputs` and `Inputs` sections of your actions' YAML code. To do this, you must turn on compute sharing. For more information about compute sharing and how to specify artifacts when it is turned on, see [Sharing compute across actions](compute-sharing.md). 

**Note**  
Although the compute sharing feature allows you to simplify your workflow's YAML code by eliminating the need for the `Outputs` and `Inputs` sections, the feature has limitations that you should be aware of before you turn it on. For information about these limitations, see [Considerations for compute sharing](compute-sharing.md#compare-compute-sharing).

## Can I share artifacts between workflows?
<a name="workflows-working-artifacts-share-wf"></a>

No, you cannot share artifacts between different workflows; however, you can share artifacts between actions within the same workflow.