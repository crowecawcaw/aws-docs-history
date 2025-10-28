End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Using git repositories with AWS Proton

AWS Proton uses git repositories for a variety of purposes. The following list categorizes
the repository types associated with AWS Proton resources. For AWS Proton features that repeatedly connect
to your repository to either push content to it or pull content from it, you have to register a
_repository link_ with AWS Proton in your AWS account. A repository link is a
set of properties that AWS Proton can use when it connects to a repository. AWS Proton currently supports
GitHub, GitHub Enterprise, and BitBucket.

Developer repositories

_Code repository_ – A repository that developers use to store
application code. Used for _code deployment_. AWS Proton doesn't interact
directly with this repository. When a developer provisions a service that includes a
pipeline, they provide the repository name and branch to read their application code from.
AWS Proton passes this information to the pipeline that it provisions.

For more information, see [Create a service](ag-create-svc.md "ag-create-svc.md").

Administrator repositories

_Template repository_ – A repository where administrators
store AWS Proton template bundles. Used for _template sync_. When an
administrator creates a template in AWS Proton, they can point to a template repository, and
AWS Proton keeps the new template in sync with it. When the administrator updates the template
bundle in the repository, AWS Proton automatically creates a new template version. Link a
template repository to AWS Proton before you can use it for syncing.

For more information, see [Template sync configurations](ag-template-sync-configs.md "ag-template-sync-configs.md").

###### Note

A template repository isn't required if you continue to upload your templates to
Amazon Simple Storage Service (Amazon S3) and call the AWS Proton template management APIs to create new templates or
template versions.

Self-managed provisioning repositories

_Infrastructure repository_ – A repository that hosts
rendered infrastructure templates. Used for _self-managed provisioning_
of _resource infrastructure_. When an administrator creates an
environment for self-managed provisioning, they provide a repository. AWS Proton submits pull
requests (PRs) to this repository to create the infrastructure for the environment and for
any service instance deployed to the environment. Link an infrastructure repository to
AWS Proton before you can use it for self-managed infrastructure provisioning.

_Pipeline repository_ – A repository used to create
pipelines. Used for _self-managed provisioning_ of
_pipelines_. Using an additional repository to provision pipelines
allows AWS Proton to store pipeline configurations independently from any individual
environment or service. You only need to provide a single pipeline repository for all your
self-managed provisioning services. Link a pipeline repository to AWS Proton before you can use
it for self-managed pipeline provisioning.

For more information, see [How AWS-managed provisioning works](ag-works-prov-methods.md#ag-works-prov-methods-direct "ag-works-prov-methods.md#ag-works-prov-methods-direct").

###### Topics

- [Create a link to your repository](ag-create-repo.md "ag-create-repo.md")
- [View linked repository data](ag-repo-view.md "ag-repo-view.md")
- [Delete a repository link](ag-repo-delete.md "ag-repo-delete.md")
