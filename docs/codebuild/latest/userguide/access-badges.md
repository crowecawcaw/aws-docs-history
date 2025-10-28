# Access AWS CodeBuild build badges

You can use AWS CodeBuild console or the AWS CLI to access build badges.

- In the CodeBuild console, in the list of build projects, in the
  **Name** column, choose the link that corresponds to the
  build project. On the **Build project:
  `project-name`** page, in **Configuration**,
  choose **Copy badge URL**. For more information, see [View a build project's details
  (console)](view-project-details.md#view-project-details-console "view-project-details.md#view-project-details-console").
- In the AWS CLI, run the `batch-get-projects` command. The build
  badge URL is included in the project environment details section of the output.
  For more information, see [View a build project's details
  (AWS CLI)](view-project-details.md#view-project-details-cli "view-project-details.md#view-project-details-cli").
  The build badge request URL is generated with a common default branch, but you can
  specify any branch in your source repository that you have used to run a build. For
  example:

```
https://codebuild.us-east-1.amazon.com/badges?uuid=...&branch=`<branch>`
```

You can also specify a tag from your source repository by substituting the
`branch` parameter with the `tag` parameter in the badge URL.
For example:

```
https://codebuild.us-east-1.amazon.com/badges?uuid=...&tag=`<tag>`
```
