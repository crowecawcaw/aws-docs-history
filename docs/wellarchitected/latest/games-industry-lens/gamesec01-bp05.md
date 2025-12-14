# GAMESEC01-BP05 Use a central identity provider

A central identity provider acts as a single source for storing and
managing user credentials, identities, permissions, and
authentication.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Use a central identity provider to streamline your user
authentication process, enforce consistent security polices, and
simplify your user management across your AWS accounts and
applications. Having a centralized approach removes the need to
manage user identities and credentials separately, which reduces
the risk of inconsistencies, redundancies, and other security
vulnerabilities. Consolidating user identities and authentication
into one place also allows for better visibility, control, and
auditability for your entire AWS environment. 

**Customer example**

AnyCompany Games faced significant challenges with managing
developer access across their rapidly expanding AWS
infrastructure. Their development team grew from 50 to 200 people
across three major titles. Initially, each project team managed
their own AWS access credentials, resulting in inconsistent
security practices, delayed onboarding for new developers, and
occasional security incidents.

The studio implemented AWS IAM Identity Center as their central
identity provider, consolidating user management into a single
system. They connected it with their existing corporate directory,
enabling developers to use their same company credentials for AWS
access. Now developers use their single, existing company login to
gain the AWS access they require to complete their work

### Implementation steps

- Consider using AWS IAM Identity Center as your central
  identity provider. This provides consistent access
  management across your AWS accounts, provides your employees
  with single sign-on authentication, and simplifies user
  access auditing to your AWS applications. IAM Identity Center also connects with existing corporate identities from
  supported identity providers.
