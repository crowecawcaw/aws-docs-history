# License type conversions in License Manager

With License Manager, you can change your license type between AWS provided licensing and Bring Your
Own License model (BYOL) as your business
needs change. You can change your license type without redeploying your existing
workloads.

You can optimize your license inventory for the following scenarios using license type
conversion:

**Migrate on-premises workloads to Amazon EC2**

During your migration, you can deploy your workload to Amazon Elastic Compute Cloud (Amazon EC2) and
use AWS provided licenses. When the migration is complete, use License Manager license
type conversion to change the license type of your instances. You can change to
BYOL so that you can use the licenses that were released during the
migration.

**Continue running workloads with expiring license agreements**

You can use License Manager license type conversion to switch from BYOL
to AWS provided licenses. This switch allows you to continue running your
workloads with fully-compliant software licenses provided by AWS with a
flexible pay-as-you go licensing model. You might choose to do this if your
license agreement with the operating system's software vendor, such as Microsoft
or Canonical, is about to expire and you do not plan to renew it.

**Optimize costs**

For small or irregular workloads, AWS provided licenses (license included)
instances might be more cost effective. When you choose to use BYOL, these
options might require a longer term commitment. For this case, you can use License Manager
license type conversion to switch your instances to license included to optimize
licensing related costs. If your instances were launched from your own virtual
machine (VM) image, you can switch back to BYOL. You might choose to do this
when the workload is more steady or predictable.

**Extended maintenance**

If your Ubuntu operating system has reached the end of standard support, you
can add a paid subscription of Ubuntu Pro. Adding a subscription to Ubuntu on
Pro provides security updates for an extended period of time. For more
information, see [Ubuntu Pro](https://ubuntu.com/pro "https://ubuntu.com/pro") in the
Canonical documentation.

###### Topics

- [Eligible license types for license type conversion in
  License Manager](conversion-types.md "conversion-types.md")
- [Conversion prerequisites for License Manager license
  types](conversion-prerequisites.md "conversion-prerequisites.md")
- [Convert a license type in License Manager](conversion-procedures.md "conversion-procedures.md")
- [Tenancy conversion in License Manager](conversion-tenancy.md "conversion-tenancy.md")
- [Troubleshooting license type conversion in
  License Manager](conversion-troubleshooting.md "conversion-troubleshooting.md")
