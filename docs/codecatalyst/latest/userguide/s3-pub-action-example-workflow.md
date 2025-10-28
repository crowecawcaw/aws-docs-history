Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Example: Publish files to Amazon S3

The following example workflow includes the **Amazon S3 publish** action,
along with a build action. The workflow builds a static documentation website and then
publishes it to Amazon S3, where it is hosted. The workflow consists of the following building
blocks that run sequentially:

- A **trigger** – This trigger starts the workflow run
  automatically when you push a change to your source repository. For more information about
  triggers, see [Starting a workflow run automatically using
  triggers](workflows-add-trigger.md "workflows-add-trigger.md").
- A **build** action (`BuildDocs`) – On trigger, the
  action builds a static documentation website (`mkdocs build`) and adds the
  associated HTML files and supporting metadata to an artifact called
  `MyDocsSite`. For more information about the build action, see [Building with workflows](build-workflow-actions.md "build-workflow-actions.md").
- An **Amazon S3 publish** action (`PublishToS3`) – On
  completion of the build action, this action copies the site in the `MyDocsSite`
  artifact to Amazon S3 for hosting.

###### Note

The following workflow example is for illustrative purposes, and will not work without
additional configuration.

###### Note

In the YAML code that follows, you can omit the `Connections:` section if you
want. If you omit this section, you must ensure that the role specified in the
**Default IAM role** field in your environment includes the permissions
and trust policies required by the **Amazon S3 publish** action. For more
information about setting up an environment with a default IAM role, see [Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md"). For more information about the
permissions and trust policies required by the **Amazon S3 publish** action, see
the description of the [Role](s3-pub-action-ref.md#s3.pub.environment.connections.role "s3-pub-action-ref.md#s3.pub.environment.connections.role") property in the ['Amazon S3 publish' action YAML](s3-pub-action-ref.md "s3-pub-action-ref.md").

```
Name: codecatalyst-s3-publish-workflow
SchemaVersion: 1.0

Triggers:
  - Type: PUSH
    Branches:
      - main
Actions:
  BuildDocs:
    Identifier: aws/build@v1
    Inputs:
      Sources:
        - WorkflowSource
    Configuration:
      Steps:
        - Run: echo BuildDocs started on `date`
        - Run: pip install --upgrade pip
        - Run: pip install mkdocs
        - Run: mkdocs build
        - Run: echo BuildDocs completed on `date`
    Outputs:
      Artifacts:
      - Name: MyDocsSite
        Files:
          - "site/**/*"

  PublishToS3:
    Identifier: aws/s3-publish@v1
    Environment:
      Name: codecatalyst-s3-publish-environment
      Connections:
        - Name: codecatalyst-account-connection
          Role: codecatalyst-s3-publish-build-role
    Inputs:
      Sources:
        - WorkflowSource
      Artifacts:
        - MyDocsSite
    Configuration:
      DestinationBucketName: amzn-s3-demo-bucket
      SourcePath: /artifacts/PublishToS3/MyDocSite/site
      TargetPath: my/docs/site
```
