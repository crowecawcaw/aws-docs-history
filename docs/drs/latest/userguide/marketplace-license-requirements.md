# Supporting marketplace licenses

Installing the AWS replication agent on an EC2 instance on AWS that has
one or more active subscriptions to a marketplace license requires taking the
following points into consideration:

- Some marketplace products do not function with certain instance types or on certain regions.
  DRS does not verify if the marketplace license applies to the instance type and region defined.
  To see if the marketplace product applies to the current settings, visit the marketplace product page.
  It is also very recommended to do periodic drills as some of these incompatibilities are only identified upon launch.
- If an agent is to be installed on an EC2 instance existing on one account
  (source account) which is a different AWS account than the AWS account where DRS is
  operated (the target account), it is mandatory to provide permissions that allow
  getting the marketplace license information from the source account. [Create a Failback and in-AWS right-sizing
  role for trusted account](adding-trusted-account.md#trusted-accounts-failback-role "adding-trusted-account.md#trusted-accounts-failback-role") using the target account AWS account ID. This role
  must be created in the source account, or the agent installation fails. If this role
  is removed or modified, launch operations might fail if new marketplace licenses are
  added.
- If an agent was installed on an EC2 instance existing on one account (source account), and DRS is operated
  on a different account (target account), and a new volume, that has a marketplace license associated with it,
  is connected to the instance with the **Automatically replicate new disks** setting active, the volume might fail
  to be added if permissions to allow getting the marketplace license information were removed or do not exist.
  [Create a Failback and in-AWS right-sizing role for trusted account](adding-trusted-account.md#trusted-accounts-failback-role "adding-trusted-account.md#trusted-accounts-failback-role")
  using the target account AWS account ID, and re-install the agent if a volume fails to be added due to this reason.
- In case of EC2 instances from one account that replicate to a staging account (see [multi-account](multi-account.md "multi-account.md"))
  and launch in one or more target accounts, only the staging account must have
  a [Failback and in-AWS right-sizing role created](adding-trusted-account.md#trusted-accounts-failback-role "adding-trusted-account.md#trusted-accounts-failback-role") for.
