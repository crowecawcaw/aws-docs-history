# Default S3 storage

Every project in Amazon SageMaker Unified Studio includes S3 shared storage by default. No additional
configuration is required to use this storage option.

## Access model

All project members have read, write, update, and delete access to the S3 shared
storage area. This storage operates on a last-write-wins principle. When multiple team
members modify the same file, the most recent save overwrites previous versions.

## Enabling S3 bucket versioning

Administrators can turn on S3 bucket versioning from the Amazon S3 console under
Account settings. Enabling versioning allows you to preserve, retrieve, and restore
previous versions of files stored in the shared storage area.

## Next steps

To make repositories available to project members, configure a Git connection.
For more information, see [Git connections](git-connections.md "git-connections.md").
