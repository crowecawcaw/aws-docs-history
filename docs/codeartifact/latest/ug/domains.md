# Working with domains in CodeArtifact

CodeArtifact _domains_ make it easier to manage multiple repositories across an
organization. You can use a domain to apply permissions across many
repositories owned by different AWS accounts. An asset is stored only once
in a domain, even if it's available from multiple repositories.

Although you can have multiple domains, we recommend a single production domain that contains all
published artifacts so that your development teams can find and share packages. You can use a second
preproduction domain to test changes to the production domain configuration.

These topics describe how to use the CodeArtifact console, the AWS CLI, and AWS CloudFormation to create or configure CodeArtifact domains.

###### Topics

- [Domain overview](domain-overview.md "domain-overview.md")
- [Create a domain](domain-create.md "domain-create.md")
- [Delete a domain](delete-domain.md "delete-domain.md")
- [Domain policies](domain-policies.md "domain-policies.md")
- [Tag a domain](tag-domains.md "tag-domains.md")
