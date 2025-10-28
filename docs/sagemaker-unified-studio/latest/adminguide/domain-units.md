# Domain units and authorization policies in Amazon SageMaker Unified Studio

Use _domain units_ to organize your assets and other domain entities
under specific business units and teams. To set up secure and efficient data sharing within
and across business units of your organization, create domain units within Amazon SageMaker Unified Studio and
grant access to selected users within each business unit so they can log in and share their
assets to the catalog. Users from anywhere in the enterprise can search for assets under
those business units and request access to those assets.

Resource owners such as AWS account owners can use domain units to set up Amazon SageMaker Unified Studio
authorization permissions on their resources. Domain units provide a delegated authority
from account owners to domain unit owners, and they can set up authorization permissions on
project profiles (created using blueprint configurations) on behalf of account owners.
This way, you can limit who can create and use project profiles depending on the
business units to which they belong. Amazon SageMaker Unified Studio authorization permissions can also be used to
enforce metadata standards and enable only selected projects to create metadata forms and
glossary. This can help maintain consistent and quality metadata. For more information, see
[Amazon SageMaker Unified Studio terminology and concepts](concepts.md "concepts.md").

Within an Amazon SageMaker Unified Studio domain unit, you can assign the following authorization policies to
your users and groups to grant them specific permissions:

- Domain unit creation policy
- Project creation policy
- Project membership policy
- Domain unit ownership assumption policy
- Project ownership assumption policy
  Within an Amazon SageMaker Unified Studio domain unit, you can assign the following authorization policies to
  your projects to grant them specific permissions:

- Glossary creation policy
- Metadata forms creation policy
- Custom asset type creation policy

###### Topics

- [Create
  domain units in Amazon SageMaker Unified Studio](create-domain-unit.md "create-domain-unit.md")
- [Edit
  domain units in Amazon SageMaker Unified Studio](edit-domain-unit.md "edit-domain-unit.md")
- [Delete
  domain units in Amazon SageMaker Unified Studio](delete-domain-unit.md "delete-domain-unit.md")
- [Manage
  domain unit owners in Amazon SageMaker Unified Studio](add-domain-unit-owners.md "add-domain-unit-owners.md")
- [Assign
  authorization policies to users and groups within an Amazon SageMaker Unified Studio domain unit](assign-authorization-policies-to-users-in-domain-unit.md "assign-authorization-policies-to-users-in-domain-unit.md")
- [Assign
  authorization policies to projects within an Amazon SageMaker Unified Studio domain unit](assign-authorization-policies-to-projects-in-domain-unit.md "assign-authorization-policies-to-projects-in-domain-unit.md")
- [Assign authorization
  policies to asset types](assign-authorization-policies-to-asset-types.md "assign-authorization-policies-to-asset-types.md")
