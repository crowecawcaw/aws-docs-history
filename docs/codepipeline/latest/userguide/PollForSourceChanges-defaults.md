# Valid settings for the

`PollForSourceChanges` parameter

The `PollForSourceChanges` parameter default is determined by the method
used to create the pipeline, as described in the following table. In many cases, the
`PollForSourceChanges` parameter defaults to true and must be disabled.

When the `PollForSourceChanges` parameter defaults to true, you should do
the following:

- Add the `PollForSourceChanges` parameter to the JSON file or AWS CloudFormation
  template.
- Create change detection resources (CloudWatch Events rule, as applicable).
- Set the `PollForSourceChanges` parameter to false.

###### Note

If you create a CloudWatch Events rule or webhook, you must set the parameter to false
to avoid triggering the pipeline more than once.

The `PollForSourceChanges` parameter is not used for Amazon ECR source
actions.

- | `PollForSourceChanges` parameter defaults                                                                                                                 | Source                                                                                                                                                                                 | Creation method                                                                                                                                     | Example "configuration" JSON structure output |
  | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
  | CodeCommit                                                                                                                                                | Pipeline is created with the console (and change detection resources are created by the console). The parameter is displayed in the pipeline structure output and defaults to `false`. | `BranchName": "main", "PollForSourceChanges": "false", "RepositoryName": "my-repo"`                                                                 |
  | Pipeline is created with the CLI or AWS CloudFormation, and the `PollForSourceChanges` parameter is not displayed in JSON output, but it sets to `true`.² | `BranchName": "main", "RepositoryName": "my-repo"`                                                                                                                                     |                                                                                                                                                     | Amazon S3                                     | Pipeline is created with the console (and change detection resources are created by the console). The parameter is displayed in the pipeline structure output and defaults to `false`.                                                                                                                                                                              | `"S3Bucket": "my-bucket", "S3ObjectKey": "object.zip", "PollForSourceChanges": "false"` |
  |                                                                                                                                                           | Pipeline is created with the CLI or AWS CloudFormation, and the `PollForSourceChanges` parameter is not displayed in JSON output, but it sets to `true`.²                              | `"S3Bucket": "my-bucket", "S3ObjectKey": "object.zip"`                                                                                              |
  | GitHub                                                                                                                                                    | Pipeline is created with the console (and change detection resources are created by the console). The parameter is displayed in the pipeline structure output and defaults to `false`. | ``"Owner": "`MyGitHubAccountName`", "Repo": "`MyGitHubRepositoryName`" "PollForSourceChanges": "false", "Branch": "`main`" "OAuthToken": "`****`"`` |
  | Pipeline is created with the CLI or AWS CloudFormation, and the `PollForSourceChanges` parameter is not displayed in JSON output, but it sets to `true`.² | ``"Owner": "`MyGitHubAccountName`", "Repo": "`MyGitHubRepositoryName`", "Branch": "`main`", "OAuthToken": "`****`"``                                                                   |                                                                                                                                                     |                                               | ² If `PollForSourceChanges` has been added at any point to the JSON structure or the AWS CloudFormation template, it is displayed as shown: `"PollForSourceChanges": "true",` ³ For information about the change detection resources that apply to each source provider, see [Change Detection Methods](change-detection-methods.md "change-detection-methods.md"). |
