# Amazon DataZone projects and environments

In Amazon DataZone, projects enable a group of users to collaborate on various business use
cases that involve publishing, discovering, subscribing to, and consuming data assets in the
Amazon DataZone catalog. Each Amazon DataZone project has a set of access controls applied to it so
that only authorized individuals, groups, and roles can access the project and the data
assets that this project subscribes to, and can use only those tools that are deﬁned by the
project permissions. Projects act as an identity principal that receives access grants to
underlying resources, enabling Amazon DataZone to operate within an organization’s infrastructure
without relying on individual user’s credentials.

In Amazon DataZone, an environment is a collection of configured resources (for example, an
Amazon S3 bucket, an AWS Glue database, or an Amazon Athena workgroup), with a given set of IAM
principals (with assigned contributor permissions) who can operate on those resources. Each
environment may also have user principals who are authorized to access the resources and get
access to data via subscription and fulfillment. Environments are designed to store
actionable links into AWS services and external IDEs and consoles. Members of the project
can access services such as the Amazon Athena console and more via deep links configured
within an environment. SSO users and IAM users from the project can be further scoped down
to use/access specific environments.

In Amazon DataZone, you create environments by using templates called environment proﬁles.
Environment profiles, in turn, are created by using built-in and custom AWS service
blueprints. With environment profiles, domain administrators can wrap blueprints with
preconfigured parameters, and then data workers can quickly create any number of new
environments by selecting existing environment profiles and specifying names for the new
environments. This enables data workers to efficiently manage their projects and
environments while ensuring that they satisfy data governance policies enforced by their
domain administrators.

For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md")

###### Topics

- [Create an environment profile](create-environment-profile.md "create-environment-profile.md")
- [Edit an environment profile](edit-environment-profile.md "edit-environment-profile.md")
- [Delete an environment profile](delete-environment-profile.md "delete-environment-profile.md")
- [Create a new environment](create-new-environment.md "create-new-environment.md")
- [Edit an environment](edit-environment.md "edit-environment.md")
- [Delete an environment](delete-environment.md "delete-environment.md")
- [Create a new project](create-new-project.md "create-new-project.md")
- [Edit project](edit-project.md "edit-project.md")
- [Move project to a different domain unit](move-project.md "move-project.md")
- [Delete project](delete-project.md "delete-project.md")
- [Leave project](leave-project.md "leave-project.md")
- [Add members to a project](add-members-to-project.md "add-members-to-project.md")
- [Remove members from a project](remove-members-from-project.md "remove-members-from-project.md")
