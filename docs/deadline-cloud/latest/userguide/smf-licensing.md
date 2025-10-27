# Software licensing for service-managed fleets

Deadline Cloud provides usage-based licensing (UBL) for commonly used software packages. Supported
software packages are automatically licensed when they run on a service-managed fleet. You don't
need to configure or maintain a software license server. Licenses scale so you won't run out for
larger jobs.

You can install software packages that support UBL using the built-in Deadline Cloud conda channel,
or you can use your own packages. For more information about the conda channel, see [Create a queue environment](create-queue-environment.md "create-queue-environment.md").

For a list of supported software packages and information about pricing for UBL, see [AWS Deadline Cloud pricing](https://aws.amazon.com/deadline-cloud/pricing/ "https://aws.amazon.com/deadline-cloud/pricing/").

## Bring your own license with service-managed fleets

With Deadline Cloud usage-based licensing (UBL) you don't need to manage separate licence
agreements with software vendors. However, if you have existing licenses or need to use
software that isn't available through UBL, you can use your own software licenses with your
Deadline Cloud service-managed fleets. You connect your SMF to the software license server via the
internet to check out a license for each worker in the fleet.

For an example of connecting to a license server using a proxy, see [Connect
service-managed fleets to a custom license server](../developerguide/smf-byol.md "../developerguide/smf-byol.md") in the _Deadline Cloud Developer
Guide_.
