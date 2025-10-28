# Extend your AWS Managed Microsoft AD schema

AWS Managed Microsoft AD uses schemas to organize and enforce how directory data is stored. The process
of adding definitions to the schema is referred to as "extending the schema." Schema extensions
make it possible for you to modify the schema of your AWS Managed Microsoft AD directory using a valid LDAP
Data Interchange Format (LDIF) file. For more information about AD schemas and how to extend
your schema, see the topics listed below.

## When to extend your AWS Managed Microsoft AD schema

You can extend your AWS Managed Microsoft AD schema by adding new object classes and attributes. For
example, you might do this if you have an application that requires changes to your schema in
order to support single sign-on capabilities.

You can also use schema extensions to enable support for applications that rely on specific
Active Directory object classes and attributes. This can be especially useful in the case where
you need to migrate corporate applications that are dependent on AWS Managed Microsoft AD, to the AWS
cloud.

Each attribute or class that is added to an existing Active Directory schema must be defined
with a unique ID. That way when companies add extensions to the schema, they can be guaranteed
to be unique and not to conflict with each other. These IDs are referred to as AD Object
Identifiers (OIDs) and are stored in AWS Managed Microsoft AD.

To get started, see [Tutorial: Extending your AWS Managed Microsoft AD
schema](ms_ad_tutorial_extend_schema.md "ms_ad_tutorial_extend_schema.md").

### Related topics

- [Extend your AWS Managed Microsoft AD schema](ms_ad_schema_extensions.md "ms_ad_schema_extensions.md")
- [Schema elements](ms_ad_key_concepts.md#ms_ad_schema_elements "ms_ad_key_concepts.md#ms_ad_schema_elements")

###### Topics

- [Tutorial: Extending your AWS Managed Microsoft AD
  schema](ms_ad_tutorial_extend_schema.md "ms_ad_tutorial_extend_schema.md")
