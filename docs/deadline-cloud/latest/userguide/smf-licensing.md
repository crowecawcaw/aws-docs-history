# Software licensing for service-managed fleets

Deadline Cloud provides usage-based licensing (UBL) for commonly used software packages. Supported
software packages are automatically licensed when they run on a service-managed fleet. You don't
need to configure or maintain a software license server. Licenses scale so you won't run out for
larger jobs.

You can install software packages that support UBL using the built-in Deadline Cloud conda channel,
or you can use your own packages. For more information about the conda channel, see [Create a queue environment](create-queue-environment.md "create-queue-environment.md").

For a list of supported software packages and information about pricing for UBL, see [AWS Deadline Cloud pricing](https://aws.amazon.com/deadline-cloud/pricing/ "https://aws.amazon.com/deadline-cloud/pricing/").

## Bring your own license with service-managed fleets

With Deadline Cloud usage-based licensing (UBL), you don't need to manage separate license
agreements with software vendors. However, if you have existing licenses or need to use
software that isn't available through UBL, you can use your own software licenses with your
Deadline Cloud service-managed fleets. Workers connect to your license server through a VPC resource
endpoint, through port forwarding to an instance in your account, or over the internet. The
license server can be in another VPC or AWS account, as long as the endpoint or forwarding
instance has network access to it.

You can also combine both methods so workers use your existing licenses first and fall
back to UBL when they run out.

For a comparison of the licensing options and setup instructions, see [Using
software licenses with Deadline Cloud](../developerguide/license.md "../developerguide/license.md") in the _Deadline Cloud Developer
Guide_.
