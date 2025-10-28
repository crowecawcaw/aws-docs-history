# Create a build project without a source

You can configure a CodeBuild project by choosing the `NO_SOURCE` source type when you configure your source.
When your source type is `NO_SOURCE`, you cannot specify a buildspec file because your project does not
have a source. Instead, you must specify a YAML-formatted buildspec string in the `buildspec` attribute of the
JSON-formatted input to the `create-project` CLI command. It might look like this:

```
{
  "name": "project-name",
  "source": {
    "type": "NO_SOURCE",
    "buildspec": "version: 0.2\n\nphases:\n  build:\n    commands:\n      - command"
   },
  "environment": {
    "type": "LINUX_CONTAINER",
    "image": "aws/codebuild/standard:5.0",
    "computeType": "BUILD_GENERAL1_SMALL",
  },
  "serviceRole": "arn:aws:iam::account-ID:role/role-name",
  "encryptionKey": "arn:aws:kms:region-ID:account-ID:key/key-ID"
}
```

For more information, see [Create a build project (AWS CLI)](create-project.md#create-project-cli "create-project.md#create-project-cli").
