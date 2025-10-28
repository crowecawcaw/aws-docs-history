# The AWSControlTowerExecution role,

explained

The `AWSControlTowerExecution` role must be present in all enrolled
accounts. It allows AWS Control Tower to manage your individual accounts and report
information about them to your Audit and Log Archive accounts.

The `AWSControlTowerExecution` role can be added into an account in several
ways, as follows:

- For accounts in the Security OU (sometimes called _core accounts_), AWS Control Tower creates the role
  at the time of initial AWS Control Tower setup.
- For an Account Factory account created through the AWS Control Tower console, AWS Control Tower creates this
  role at the time of account creation.
- For a single account enrollment, we ask customers to manually create the
  role and then enroll the account in AWS Control Tower.
- When extending governance to an OU, AWS Control Tower uses the **StackSet-AWSControlTowerExecutionRole** to create the role in all accounts in that OU.

###### Note

When you unenroll an account, AWS Control Tower removes the `AWSControlTowerExecution` role, no matter if it was created manually or by AWS Control Tower itself.

Purpose of the `AWSControlTowerExecution` role:

- `AWSControlTowerExecution` allows you to create and enroll
  accounts, automatically, with scripts and Lambda functions.
- `AWSControlTowerExecution` helps you configure your
  organizations's logging, so that all the logs for every account are sent to
  the logging account.
- `AWSControlTowerExecution` allows you to enroll an individual account in AWS Control Tower. First, you must add the
  `AWSControlTowerExecution` role to that account. For steps on
  how to add the role, see [Manually add the required IAM role to an existing
  AWS account and enroll it](enroll-manually.md "enroll-manually.md").
  How the `AWSControlTowerExecution` role works with OUs:

The `AWSControlTowerExecution` role
ensures that your selected AWS Control Tower controls apply automatically to every
individual account, in each OU, in your organization, as well as to every new account you create
in AWS Control Tower. As a result:

- You can provide compliance and security reports more easily, based on the
  auditing and logging features embodied by AWS Control Tower [controls](guardrails.md "guardrails.md").
- Your security and compliance teams can verify that all requirements are
  met, and that no organizational drift has occurred.
  For more information about drift, see [Detect and resolve drift in AWS Control Tower](drift.md "drift.md").

To summarize, the `AWSControlTowerExecution` role and its associated
policy gives you flexible control of security and compliance across your entire
organization. Therefore, breaches of security or protocol are less likely to occur.
