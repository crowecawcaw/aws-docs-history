# Private and local repositories

If you would like to manage your operating system repository locally, either within your VPC on AWS or an on-premises data center, without using an outbound internet connection for your instance, you can use a private or local repository.

Some reasons to use a private repository are:

- They provide access to repositories for Amazon EC2 instances that do not have access to the internet for security reasons.
- You have additional add-on products from vendors that are not provided through the public cloud update infrastructure.
- You want to deploy an organized and consistent set of patches across mission-critical workloads. Using an online repository might introduce new updates which could lead to inconsistency across the landscape.
- You want to improve software download times and reduce bandwidth overhead while patching a large fleet of infrastructure.
  If you are on SUSE Linux Enterprise Server (SLES) and you want to use private repositories, make sure that the operating system repositories are pointing to the local repository instead of the respective vendor repositories before you use Patch Manager. If you are on Red Hat Enterprise Linux (RHEL) or Oracle Linux, you must use a custom baseline to point to local repositories.
