# Configuring project storage options

## Storage type selection guidelines

Choose S3 storage for teams with limited Git experience, simple projects without complex versioning needs,
quick experimentation and ad-hoc analysis, and scenarios requiring maximum regional availability.

Choose Git-based storage for projects requiring strict version control, collaborative development with code reviews,
integration with existing development workflows, and cross-project code sharing requirements.

## Amazon S3 storage configuration

S3 storage is the default option and requires minimal configuration. As an administrator, you can
enable [S3 bucket
versioning](../../../AmazonS3/latest/userguide/manage-versioning-examples.md "../../../AmazonS3/latest/userguide/manage-versioning-examples.md") to configure basic versioning capabilities for projects that require file history tracking.

## Git-based storage configuration

For projects requiring advanced version control, you can configure connections to existing Git repositories during project
creation and set default branches and branching policies for effective branch management. Additionally, you can enable multiple
projects to use the same repository when appropriate, allowing for efficient cross-project sharing of code and resources.
However, it's important to note that Git-based storage availability is limited by the CodeConnections service, which may
impose regional limitations on deployment options. For more information,
see [CodeConnections](../../../general/latest/gr/codeconnections.md "../../../general/latest/gr/codeconnections.md").

For storage organization, refer to [Managing storage resources](../userguide/managing-storage.md "../userguide/managing-storage.md").
