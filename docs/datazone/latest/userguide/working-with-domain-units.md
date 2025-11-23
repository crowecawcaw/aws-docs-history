# Domain units and authorization policies in

Amazon DataZone

Use _domain units_ to easily organize your assets and other domain
entities under specific business units and teams. To set up secure and efficient data
sharing within and across business units of your organization, create domain units within
Amazon DataZone and enable selected users within each business unit to login and share their
assets to the catalog. Users from anywhere in the enterprise can easily search for assets
under those business units and request access to those assets.

Domain units can also be used to enable resource owners, such as AWS account owners, to
set up Amazon DataZone authorization permissions on their resources. Domain units provide a
delegated authority from account owners to domain unit owners and they can set up
authorization permissions on environment profiles (created using blueprint configurations),
on behalf of account owners. This allows you to limit who can create and use which
environment profiles depending on the business units to which they belong. Amazon DataZone
authorization permissions can also be used to enforce metadata standards and enable only
selected projects to create metadata forms and glossary. This can help maintain a consistent
and quality metadata. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

Within an Amazon DataZone domain unit, you can assign the following authorization policies to
your users and groups to grant them specific permissions:

- Domain unit creation policy
- Project creation policy
- Project membership policy
- Domain unit ownership assumption policy
- Project ownership assumption policy
  For more information, see [Assign
  authorization policies to users and groups within an Amazon DataZone domain unit](assign-authorization-policies-to-users-in-domain-unit.md "assign-authorization-policies-to-users-in-domain-unit.md").

Within an Amazon DataZone domain unit, you can assign the following authorization policies to
your projects to grant them specific permissions:

- Glossary creation policy
- Metadata forms creation policy
- Custom asset type creation policy
  For more information, see [Assign
  authorization policies to projects within an Amazon DataZone domain unit](assign-authorization-policies-to-projects-in-domain-unit.md "assign-authorization-policies-to-projects-in-domain-unit.md").

Another way to use the authorization mechanism in Amazon DataZone is to apply authorization
policies to projects and domain unit owners within Amazon DataZone blueprint configurations.

An Amazon DataZone blueprint configuration is an entity that encapsulates information needed to
create and configure resources used in publishing and subscribing user workflows. This
information includes AWS account number and region, CloudFormation templates, account level
parameters such as VPCs and subnets, and can also contain database connection information
and credentials. To control costs and improve security, data platform users require the
ability to control who can use these blueprints and create environments.

Within a specific blueprint configuration, you can assign the following authorization
policies to projects and domain unit owners:

- Create environment profiles using this blueprint - this policy can be assigned to
  Amazon DataZone projects and it authorizes them to create environment profiles using this
  blueprint.
- Grant permissions to create environment profiles using this blueprint - this
  policy can be assigned to domain unit owners and it authorizes them to grant
  permissions to projects to create environment profiles using this blueprint.
  For more information, see [Assign authorization
  policies within Amazon DataZone blueprint configurations](assign-authorization-policies-in-blueprint-config.md "assign-authorization-policies-in-blueprint-config.md").

###### Topics

- [Create domain units in Amazon DataZone](create-domain-unit.md "create-domain-unit.md")
- [Edit domain units in Amazon DataZone](edit-domain-unit.md "edit-domain-unit.md")
- [Delete domain units in Amazon DataZone](delete-domain-unit.md "delete-domain-unit.md")
- [Manage domain unit owners in Amazon DataZone](add-domain-unit-owners.md "add-domain-unit-owners.md")
- [Assign
  authorization policies to users and groups within an Amazon DataZone domain unit](assign-authorization-policies-to-users-in-domain-unit.md "assign-authorization-policies-to-users-in-domain-unit.md")
- [Assign
  authorization policies to projects within an Amazon DataZone domain unit](assign-authorization-policies-to-projects-in-domain-unit.md "assign-authorization-policies-to-projects-in-domain-unit.md")
- [Assign authorization
  policies within Amazon DataZone blueprint configurations](assign-authorization-policies-in-blueprint-config.md "assign-authorization-policies-in-blueprint-config.md")
