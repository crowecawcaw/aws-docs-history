# Update Amazon GameLift Servers Realtime script files

You can update the metadata for a script resource using either the Amazon GameLift Servers console or
the [`update-script`](../../../cli/latest/reference/gamelift/update-script.md "../../../cli/latest/reference/gamelift/update-script.md") AWS CLI command.

You can also update the script content for a script resource. Amazon GameLift Servers deploys script
content to all fleet instances that use the updated script resource. When the updated
script is deployed, instances use it when starting new game sessions. Game sessions that
are already running at the time of the update don't use the updated script.

**To update script files**

- For script files stored locally, to upload the updated script .zip file, use
  either the Amazon GameLift Servers console or the **update-script** command.
- For script files stored in an Amazon S3 bucket, upload the updated script files to
  the S3 bucket. Amazon GameLift Servers periodically checks for updated script files and retrieves
  them directly from the S3 bucket.
