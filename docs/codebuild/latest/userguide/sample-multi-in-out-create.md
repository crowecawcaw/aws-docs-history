# Create a build project with multiple inputs and outputs

Use the following procedure to create a build project with multiple inputs and outputs.

###### To create a build project with multiple inputs and outputs

1. Upload your sources to one or more S3 buckets, CodeCommit, GitHub, GitHub Enterprise Server, or Bitbucket repositories.
2. Choose which source is the primary source. This is the source in which CodeBuild looks for and runs
   your buildspec file.
3. Create a build project. For more information, see [Create a build project in AWS CodeBuild](create-project.md "create-project.md").
4. Create your build project,
   run the build, and get information about the build.
5. If you use the AWS CLI to create the build project, the JSON-formatted input to the
   `create-project` command might look similar to the following:

```
{
  "name": "sample-project",
  "source": {
    "type": "S3",
    "location": "`<bucket/sample.zip>`"
  },
  "secondarySources": [
    {
      "type": "CODECOMMIT",
      "location": "https://git-codecommit.us-west-2.amazonaws.com/v1/repos/repo",
      "sourceIdentifier": "source1"
    },
    {
      "type": "GITHUB",
      "location": "https://github.com/awslabs/aws-codebuild-jenkins-plugin",
      "sourceIdentifier": "source2"
    }
  ],
  "secondaryArtifacts": [ss
    {
      "type": "S3",
      "location": "`<output-bucket>`",
      "artifactIdentifier": "artifact1"
    },
    {
      "type": "S3",
      "location": "`<other-output-bucket>`",
      "artifactIdentifier": "artifact2"
    }
  ],
  "environment": {
    "type": "LINUX_CONTAINER",
    "image": "aws/codebuild/standard:5.0",
    "computeType": "BUILD_GENERAL1_SMALL"
  },
  "serviceRole": "arn:aws:iam::account-ID:role/role-name",
  "encryptionKey": "arn:aws:kms:region-ID:account-ID:key/key-ID"
}
```

Your primary source is defined under the `source` attribute. All other sources are called
secondary sources and appear under `secondarySources`. All secondary sources are installed in
their own directory. This directory is stored in the built-in environment variable
`CODEBUILD_SRC_DIR_`sourceIdentifer``. For more information, see
[Environment variables in build
environments](build-env-ref-env-vars.md "build-env-ref-env-vars.md").

The `secondaryArtifacts` attribute contains a list of artifact definitions.
These artifacts use the `secondary-artifacts` block of the buildspec file that is
nested inside the `artifacts` block.

Secondary artifacts in the buildspec file have the same structure as artifacts and are separated by their
artifact identifier.

###### Note

In the [CodeBuild API](../APIReference.md "../APIReference.md"), the
`artifactIdentifier` on a secondary artifact is a required attribute in
`CreateProject` and `UpdateProject`. It must be used to reference a
secondary artifact.

Using the preceding JSON-formatted input, the buildspec file for the project might look
like:

```
version: 0.2

phases:
  install:
    runtime-versions:
      java: openjdk11
  build:
    commands:
      - cd $CODEBUILD_SRC_DIR_source1
      - touch file1
      - cd $CODEBUILD_SRC_DIR_source2
      - touch file2

artifacts:
  files:
    - '**.*'
  secondary-artifacts:
    artifact1:
      base-directory: $CODEBUILD_SRC_DIR_source1
      files:
        - file1
    artifact2:
      base-directory: $CODEBUILD_SRC_DIR_source2
      files:
        - file2
```

You can override the version of the primary source using the API with the
`sourceVersion` attribute in `StartBuild`. To override one or more
secondary source versions, use the `secondarySourceVersionOverride` attribute.

The JSON-formatted input to the the `start-build` command in the AWS CLI might look like:

```
{
   "projectName": "sample-project",
   "secondarySourcesVersionOverride": [
      {
        "sourceIdentifier": "source1",
        "sourceVersion": "codecommit-branch"
      },
      {
        "sourceIdentifier": "source2",
        "sourceVersion": "github-branch"
      },
   ]
}
```
