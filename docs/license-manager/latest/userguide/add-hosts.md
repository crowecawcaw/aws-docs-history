# Add Dedicated Hosts to a host resource group in License Manager

You can add your existing hosts to a host resource group from the AWS Management Console, AWS CLI, or
AWS API. To add your hosts, you must be the AWS account owner where you created the
Dedicated Host and host resource groups. If your host resource group lists allowed
self-managed licenses and instances types, the host you add must match these requirements.

###### Note

If you stop instances and want to restart them, you must perform the following two
tasks:

- [Modify](../../../AWSEC2/latest/APIReference/API_ModifyInstancePlacement.md "../../../AWSEC2/latest/APIReference/API_ModifyInstancePlacement.md") the
  instance to point to the host resource group.
- [Associate](../APIReference/API_UpdateLicenseSpecificationsForResource.md "../APIReference/API_UpdateLicenseSpecificationsForResource.md") self-managed licenses to match the host resource group.
  There is no limit to the number of Dedicated Hosts that you can add to a host resource group. For more
  information about Resource Groups, see [AWS Resource Groups User Guide](../../../ARG/latest/userguide/welcome.md "../../../ARG/latest/userguide/welcome.md").

Use the following steps to add one or more Dedicated Hosts to a resource group:

1. Log into the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. Choose **Host resource groups**.
3. From the list of host resource group names, click on the name of the host resource group where you want to add the Dedicated Host.
4. Choose **Dedicated Hosts**.
5. Choose **Add**.
6. Choose one or more Dedicated Hosts to add to the host resource group.
7. Choose **Add**.

Adding the host may take 1 - 2 minutes, and then it appears in the list of
**Dedicated Hosts.**
