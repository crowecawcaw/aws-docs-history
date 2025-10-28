# Tagging Macie resources

A _tag_ is a label that you can define and assign to
AWS resources, including certain types of Amazon Macie resources. Tags can help you identify,
categorize, and manage resources in different ways, such as by purpose, owner, environment,
or other criteria. For example, you can use tags to: apply policies, allocate costs,
distinguish between versions of resources, or identify resources that support certain
compliance requirements or workflows.

You can assign tags to the following types of Macie resources: allow lists, custom data
identifiers, filter rules and suppression rules for findings, and sensitive data discovery
jobs. If you're the Macie administrator for an organization, you can also assign tags to member
accounts in your organization.

A resource can have as many as 50 tags. Each tag consists of a required _tag key_ and an optional _tag
value_. A _tag key_ is a general label that
acts as a category for a more specific tag value. A _tag
value_ acts as a descriptor for a tag key.

For example, if you create custom data identifiers and sensitive data discovery jobs to
analyze data at different points in a workflow (one set for staged data and another for
production data), you might assign a `Stack` tag key to those resources. The tag
value for this tag key might be `Staging` for custom data identifiers and jobs
that analyze staged data, and `Production` for the others.

###### Topics

- [Tagging fundamentals](tags-basics.md "tags-basics.md")
- [Adding tags to resources](tags-add.md "tags-add.md")
- [Controlling access to resources using tags](tags-iam.md "tags-iam.md")
- [Reviewing and editing tags for
  resources](tags-retrieve-update.md "tags-retrieve-update.md")
- [Removing tags from resources](tags-remove.md "tags-remove.md")
