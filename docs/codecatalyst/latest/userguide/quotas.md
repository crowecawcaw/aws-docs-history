

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Quotas for CodeCatalyst
<a name="quotas"></a>

The following table describes quotas and limits for Amazon CodeCatalyst. You can find additional information for specific aspects of CodeCatalyst in the following topics:
+ [Quotas for source repositories in CodeCatalyst](source-quotas.md)
+ [Quotas for identity, permission, and access in CodeCatalyst](ipa-quotas.md)
+ [Quotas for workflows in CodeCatalyst](workflows-quotas.md)
+ [Quotas for Dev Environments in CodeCatalyst](devenvironment-limits.md)
+ [Quotas for projects](projects-quotas.md)
+ [Quotas for blueprints in CodeCatalyst](blueprints-quotas.md)
+ [Quotas for spaces](spaces-quotas-limits.md)
+ [Quotas for issues in CodeCatalyst](issues-quotas.md)


|  |  | 
| --- |--- |
| Maximum number of spaces in an account | 5 | 
| Maximum number of spaces a user can create in a calendar month | 5 | 
| Minimum number of AWS accounts for a space | 1 | 
| Maximum number of account connections for a space | 5,000 | 
| Maximum number of AWS accounts as the billing account for a space | 1 | 
| Maximum number of spaces in the Free tier for which a single AWS account can be specified as the billing account | 3 | 
| Maximum number of spaces in a paid tier for which a single AWS account can be specified as the billing account  | 15 | 
| Maximum number of VPC connections for a space | 100 | 
| Maximum number of projects in a space | 100 | 
| Maximum number of projects to which a user can belong | 1,000 | 
| Space descriptions | Space descriptions are optional. If specified, they must be between 0 and 200 characters in length. They can contain any combination of letters, numbers, spaces, periods, underscores, commas, dashes, and the following special characters:<br />`? & $ % + = / \ ; : \n \t \r` | 
| Space names | Space names must be unique across CodeCatalyst. You cannot reuse names of deleted spaces.Space names must be between 3 and 63 characters in length. They must also begin with an alphanumeric character. Space names can contain any combination of letters, numbers, periods, underscores, and dashes. They cannot contain any of the following characters: <br />`! ? @ # $ % ^ & * ( ) + = { } [ ] \| /\ > < ~ ` ' " ; : `  | 