# Filter GitHub webhook events (CloudFormation)

To use an CloudFormation template to filter webhook events, use the AWS CodeBuild project's
`FilterGroups` property.

For more information about GitHub webhook events, see [GitHub webhook events](github-webhook.md "github-webhook.md").

The following YAML-formatted portion of an CloudFormation
template creates two filter groups. Together, they trigger a build when one or both
evaluate to true:

- The first filter group specifies pull requests are created or updated on
  branches with Git reference names that match the regular expression
  `^refs/heads/main$` by a GitHub user who does not have account ID
  `12345`.
- The second filter group specifies push requests are created on files with
  names that match the regular expression `READ_ME` in branches with
  Git reference names that match the regular expression
  `^refs/heads/.*`.
- The third filter group specifies a push request with a head commit message
  matching the regular expression `\[CodeBuild\]`.
- The fourth filter group specifies a GitHub Actions workflow job request with a
  workflow name matching the regular expression
  `\[CI-CodeBuild\]`.

```
CodeBuildProject:
  Type: AWS::CodeBuild::Project
  Properties:
    Name: MyProject
    ServiceRole: `service-role`
    Artifacts:
      Type: NO_ARTIFACTS
    Environment:
      Type: LINUX_CONTAINER
      ComputeType: BUILD_GENERAL1_SMALL
      Image: aws/codebuild/standard:5.0
    Source:
      Type: GITHUB
      Location: `source-location`
    Triggers:
      Webhook: true
      FilterGroups:
        - - Type: EVENT
            Pattern: PULL_REQUEST_CREATED,PULL_REQUEST_UPDATED
          - Type: BASE_REF
            Pattern: ^refs/heads/main$
            ExcludeMatchedPattern: false
          - Type: ACTOR_ACCOUNT_ID
            Pattern: 12345
            ExcludeMatchedPattern: true
        - - Type: EVENT
            Pattern: PUSH
          - Type: HEAD_REF
            Pattern: ^refs/heads/.*
          - Type: FILE_PATH
            Pattern: READ_ME
            ExcludeMatchedPattern: true
        - - Type: EVENT
            Pattern: PUSH
          - Type: COMMIT_MESSAGE
            Pattern: \[CodeBuild\]
          - Type: FILE_PATH
            Pattern: ^src/.+|^test/.+
        - - Type: EVENT
            Pattern: WORKFLOW_JOB_QUEUED
          - Type: WORKFLOW_NAME
            Pattern: \[CI-CodeBuild\]
```
