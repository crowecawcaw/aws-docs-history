Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding an action to a workflow

Use the following instructions to add an action to a workflow and then configure
it.

###### To add and configure an action

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. At the top-left, choose **+ Actions**, The
   **Actions** catalog appears.
7. In the drop-down list, do one of the following:
   - Choose **Amazon CodeCatalyst** to view [CodeCatalyst](workflows-actions.md#workflows-actions-types-cc "workflows-actions.md#workflows-actions-types-cc"), [CodeCatalyst Labs](workflows-actions.md#workflows-actions-types-cc-labs "workflows-actions.md#workflows-actions-types-cc-labs") , or
     [third-party](workflows-actions.md#workflows-actions-types-3p "workflows-actions.md#workflows-actions-types-3p")
     actions.
     - CodeCatalyst actions have a **by AWS**
       label.
     - CodeCatalyst Labs actions have a **by CodeCatalyst Labs**
       label.
     - Third-party actions have a **by
       `vendor`** label,
       where `vendor` is the name of the
       third-party vendor.

   - Choose **GitHub** to view a [curated list of
     GitHub Actions](integrations-github-action-add-curated.md "integrations-github-action-add-curated.md").

8. In the action catalog, search for an action, and then do one of the
   following:
   - Choose the plus sign (**+**) to add the action to
     your workflow.
   - Choose the action's name to view its readme.

9. Configure the action. Choose **Visual** to use the visual
   editor, or **YAML** to use the YAML editor. For detailed
   instructions, see the following links.

For instructions on adding [CodeCatalyst
actions](workflows-actions.md#workflows-actions-types-cc "workflows-actions.md#workflows-actions-types-cc"), see:

    * [Adding the build action](build-add-action.md "build-add-action.md")
    * [Adding the test action](test-add-action.md "test-add-action.md")
    * [Adding the 'Deploy to Amazon ECS' action](deploy-action-ecs-adding.md "deploy-action-ecs-adding.md")
    * [Adding the 'Deploy to Kubernetes cluster' action](deploy-action-eks-adding.md "deploy-action-eks-adding.md")
    * [Adding the 'Deploy AWS CloudFormation stack' action](deploy-action-cfn-adding.md "deploy-action-cfn-adding.md")
    * [Adding the 'AWS CDK deploy' action](cdk-dep-action-add.md "cdk-dep-action-add.md")
    * [Adding the 'AWS CDK bootstrap' action](cdk-boot-action-add.md "cdk-boot-action-add.md")
    * [Adding the 'Amazon S3 publish' action](s3-pub-action-add.md "s3-pub-action-add.md")
    * [Adding the 'AWS Lambda invoke' action](lam-invoke-action-add.md "lam-invoke-action-add.md")
    * [Adding the 'Render Amazon ECS task definition'
     action](render-ecs-action-add.md "render-ecs-action-add.md")

For instructions on adding [CodeCatalyst Labs actions](workflows-actions.md#workflows-actions-types-cc-labs "workflows-actions.md#workflows-actions-types-cc-labs"), see:

    * The action's readme. You can find the readme by choosing the action's
     name in the action catalog.

For instructions on adding [GitHub Actions](workflows-actions.md#workflows-actions-types-github "workflows-actions.md#workflows-actions-types-github"), see:

    * [Integrating with GitHub Actions](integrations-github-actions.md "integrations-github-actions.md")

For instructions on adding [third-party actions](workflows-actions.md#workflows-actions-types-3p "workflows-actions.md#workflows-actions-types-3p"), see:

    * The action's readme. You can find the readme by choosing the action's
     name in the action catalog.

10. (Optional) Choose **Validate** to make sure the YAML code is
    valid.
11. Choose **Commit** to commit your changes.
