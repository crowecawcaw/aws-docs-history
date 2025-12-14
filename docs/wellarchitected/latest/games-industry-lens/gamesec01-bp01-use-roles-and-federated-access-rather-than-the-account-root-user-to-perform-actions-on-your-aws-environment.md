# GAMESEC01-BP01 Use roles and federated access, rather than the

account root user, to perform actions on your AWS environment

When you first create an AWS account, you begin with an identity
known as the root user, which is accessed using the email address
and password associated with the account. The root user has
complete access to AWS services and resources within that account.
In most cases, you should avoid using the root user for day-to-day
tasks. When root-level access is required, confirm that it's
absolutely necessary and verify that additional logging and
guardrails are in place to track its use.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

In an AWS Organizations configuration, each account still has its
own root user, but day-to-day access should instead be managed
through IAM roles and IAM Identity Center users. Create role-based
access tailored to your game's lifecycle stages and teams. For
example, the live operations team might need permissions to manage
in-game events, while developers need access to push updates. When
working with third-party services or partners, use federated
access to enable secure collaboration without exposing sensitive
infrastructure. This approach verifies that each user or partner
has only the access they need while maintaining the security of
your game's infrastructure and player data.

**Customer example**

AnyCompany Games implemented role-based access control when
developing their new game. By using specific IAM roles for their
diverse development teams, they avoid using shared credentials.
This setup allows a dev team to assume a role for core game
systems, while the content team's role is only able to access
asset management services.

### Implementation steps

- Do not use the root user after setting up an account unless
  absolutely necessary. Create the account, secure the root
  user, and immediately create the required administration IAM
  roles and assign that role to federated user.
- Only use the root user when you need to perform
  [a
  limited number of tasks that are only available to the root
  user](../../../IAM/latest/UserGuide/root-user-tasks.md "../../../IAM/latest/UserGuide/root-user-tasks.md"). Examples of these tasks include changing your
  root user email address and changing your AWS support plan.
