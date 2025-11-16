AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Supported AWS CLI commands for data transfer to or from Snowball Edge

Following, you can find information about how to specify the Amazon S3 adapter or Amazon S3 compatible storage on Snowball Edge as the endpoint
for applicable AWS Command Line Interface (AWS CLI) commands. You can also find the list of AWS CLI commands
for Amazon S3 that are supported for transferring data to the AWS Snowball Edge device with the adapter or Amazon S3 compatible storage on Snowball Edge.

###### Note

For information about installing and setting up the AWS CLI, including specifying
what Regions you want to make AWS CLI calls against, see [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

Currently, Snowball Edge devices support only version 1.16.14 and earlier of the
AWS CLI when using the Amazon S3 adapter. See [Finding Snowball Edge client version](using-adapter.md#aws-cli-version "using-adapter.md#aws-cli-version"). If you are using Amazon S3 compatible storage on Snowball Edge, you can use the lastest version of the AWS CLI. To download and use the latest version, see [AWS Command Line Interface User Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md").

###### Note

Be sure to install version 2.6.5+ or 3.4+ of Python before you install version
1.16.14 of the AWS CLI.

## Supported AWS CLI commands for data transfer with

Amazon S3 and Snowball Edge

Following is a description of the subset of AWS CLI commands and options for Amazon S3
that the AWS Snowball Edge device supports. If a command or option isn't listed, it's not
supported. You can declare some unsupported options, like `--sse` or
`--storage-class`, along with a command. However, these are ignored
and have no impact on how data is imported.

- [cp](../../../cli/latest/reference/s3/cp.md "../../../cli/latest/reference/s3/cp.md") – Copies a file or
  object to or from the AWS Snowball Edge device. The following are options for this
  command:
  - `--dryrun` (Boolean) – The operations that would
    be performed using the specified command are displayed without being
    run.
  - `--quiet` (Boolean) – Operations performed by
    the specified command are not displayed.
  - `--include` (string) – Don't exclude files or
    objects in the command that match the specified pattern. For
    details, see [Use of Exclude and Include Filters](../../../cli/latest/reference/s3/index.md#use-of-exclude-and-include-filters "../../../cli/latest/reference/s3/index.md#use-of-exclude-and-include-filters") in the
    _AWS CLI Command Reference_.
  - `--exclude` (string) – Exclude all files or
    objects from the command that matches the specified pattern.
  - `--follow-symlinks | --no-follow-symlinks` (Boolean)
    – Symbolic links (symlinks) are followed only when uploading
    to Amazon S3 from the local file system. Amazon S3 doesn't support symbolic
    links, so the contents of the link target are uploaded under the
    name of the link. When neither option is specified, the default is
    to follow symlinks.
  - `--only-show-errors` (Boolean) – Only errors and
    warnings are displayed. All other output is suppressed.
  - `--recursive` (Boolean) – The command is
    performed on all files or objects under the specified directory or
    prefix.
  - `--page-size` (integer) – The number of results
    to return in each response to a list operation. The default value is
    1000 (the maximum allowed). Using a lower value might help if an
    operation times out.
  - `--metadata` (map) – A map of metadata to store
    with the objects in Amazon S3. This map is applied to every object that
    is part of this request. In a sync, this functionality means that
    files that haven't changed don't receive the new metadata. When
    copying between two Amazon S3 locations, the
    `metadata-directive` argument defaults to
    `REPLACE` unless otherwise specified.

- [ls](../../../cli/latest/reference/s3/ls.md "../../../cli/latest/reference/s3/ls.md") – Lists objects on
  the AWS Snowball Edge device. The following are options for this command:
  - `--human-readable` (Boolean) – File sizes are
    displayed in human-readable format.
  - `--summarize` (Boolean) – Summary information is
    displayed. This information is the number of objects and their total
    size.
  - `--recursive` (Boolean) – The command is
    performed on all files or objects under the specified directory or
    prefix.
  - `--page-size` (integer) – The number of results
    to return in each response to a list operation. The default value is
    1000 (the maximum allowed). Using a lower value might help if an
    operation times out.

- [rm](../../../cli/latest/reference/s3/rm.md "../../../cli/latest/reference/s3/rm.md") – Deletes an object
  on the AWS Snowball Edge device. The following are options for this command:
  - `--dryrun` (Boolean) – The operations that would
    be performed using the specified command are displayed without being
    run.
  - `--include` (string) – Don't exclude files or
    objects in the command that match the specified pattern. For
    details, see [Use of Exclude and Include Filters](../../../cli/latest/reference/s3/index.md#use-of-exclude-and-include-filters "../../../cli/latest/reference/s3/index.md#use-of-exclude-and-include-filters") in the
    _AWS CLI Command Reference_.
  - `--exclude` (string) – Exclude all files or
    objects from the command that matches the specified pattern.
  - `--recursive` (Boolean) – The command is
    performed on all files or objects under the specified directory or
    prefix.
  - `--page-size` (integer) – The number of results
    to return in each response to a list operation. The default value is
    1000 (the maximum allowed). Using a lower value might help if an
    operation times out.
  - `--only-show-errors` (Boolean) – Only errors and
    warnings are displayed. All other output is suppressed.
  - `--quiet` (Boolean) – Operations performed by
    the specified command are not displayed.

- [sync](../../../cli/latest/reference/s3/sync.md "../../../cli/latest/reference/s3/sync.md") – Syncs
  directories and prefixes. This command copies new and updated files from the
  source directory to the destination. This command only creates directories
  in the destination if they contain one or more files.

###### Important

Syncing from one directory to another directory on the same Snowball
Edge isn't supported.

Syncing from one AWS Snowball Edge device to another AWS Snowball Edge device
isn't supported.

You can only use this option to sync the contents between your
on-premises data storage and a Snowball Edge.

    + `--dryrun` (Boolean) – The operations that would
     be performed using the specified command are displayed without being
     run.
    + `--quiet` (Boolean) – Operations performed by
     the specified command are not displayed.
    + `--include` (string) – Don't exclude files or
     objects in the command that match the specified pattern. For
     details, see [Use of Exclude and Include Filters](../../../cli/latest/reference/s3/index.md#use-of-exclude-and-include-filters "../../../cli/latest/reference/s3/index.md#use-of-exclude-and-include-filters") in the
     *AWS CLI Command Reference*.
    + `--exclude` (string) – Exclude all files or
     objects from the command that matches the specified pattern.
    + `--follow-symlinks` or
     `--no-follow-symlinks` (Boolean) – Symbolic
     links (symlinks) are followed only when uploading to Amazon S3 from the
     local file system. Amazon S3 doesn't support symbolic links, so the
     contents of the link target are uploaded under the name of the link.
     When neither option is specified, the default is to follow
     symlinks.
    + `--only-show-errors` (Boolean) – Only errors and
     warnings are displayed. All other output is suppressed.
    + `--no-progress` (Boolean) – File transfer
     progress is not displayed. This option is only applied when the
     `--quiet` and `--only-show-errors` options
     are not provided.
    + `--page-size` (integer) – The number of results
     to return in each response to a list operation. The default value is
     1000 (the maximum allowed). Using a lower value might help if an
     operation times out.
    + `--metadata` (map) – A map of metadata to store
     with the objects in Amazon S3. This map is applied to every object that
     is part of this request. In a sync, this functionality means that
     files that haven't changed don't receive the new metadata. When
     copying between two Amazon S3 locations, the
     `metadata-directive` argument defaults to
     `REPLACE` unless otherwise specified.


    ###### Important

    Syncing from one directory to another directory on the same
     Snowball Edge isn't supported.

    Syncing from one AWS Snowball Edge device to another AWS Snowball Edge
     device isn't supported.

    You can only use this option to sync the contents between your
     on-premises data storage and a Snowball Edge.
    + `--size-only` (Boolean) – With this option, the
     size of each key is the only criterion used to decide whether to
     sync from source to destination.
    + `--exact-timestamps` (Boolean) – When syncing
     from Amazon S3 to local storage, same-sized items are ignored only when
     the timestamps match exactly. The default behavior is to ignore
     same-sized items unless the local version is newer than the Amazon S3
     version.
    + `--delete` (Boolean) – Files that exist in the
     destination but not in the source are deleted during sync.

You can work with files or folders with spaces in their names, such as `my
 photo.jpg` or `My Documents`. However, make sure that you
handle the spaces properly in the AWS CLI commands. For more information, see [Specifying parameter values for the AWS
CLI](../../../cli/latest/userguide/cli-using-param.md "../../../cli/latest/userguide/cli-using-param.md") in the _AWS Command Line Interface User Guide_.
