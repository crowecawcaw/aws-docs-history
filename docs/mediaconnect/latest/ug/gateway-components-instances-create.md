# Registering a MediaConnect Gateway

instance

You can register an instance by running a custom Linux command on the device that
will be hosting the instance. You generate the command by following the instance
registration process in the AWS Management Console. Registering an instance using the AWS CLI is
not currently supported.

###### Contents

- [Prerequisites](gateway-components-instances-create.md#gateway-components-instances-create-prerequisites "gateway-components-instances-create.md#gateway-components-instances-create-prerequisites")
- [Procedure](gateway-components-instances-create.md#gateway-components-instances-create-procedure "gateway-components-instances-create.md#gateway-components-instances-create-procedure")
- [Next steps](gateway-components-instances-create.md#gateway-components-instances-create-next-steps "gateway-components-instances-create.md#gateway-components-instances-create-next-steps")
- [Additional resources](gateway-components-instances-create.md#gateway-components-instances-create-additional-resources "gateway-components-instances-create.md#gateway-components-instances-create-additional-resources")

## Prerequisites

The following procedure assumes that you have previously created a
gateway.

## Procedure

###### To register a MediaConnect Gateway instance

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. From the navigation pane, select **Gateways**.
3. In the **Gateways** section, select the gateway you
   want to register the instance to.
4. On the gateway **Details** page, select the
   **Instances** tab.
5. On the **Instances** tab, choose **Register
   instance**.
6. On the **Register Gateway instances** page, complete
   the following steps:
   1. For **Activation key duration**, enter the
      number of days that the activation key will remain active. After
      that number of days, the key will no longer work when
      registering a gateway instance.
   2. For **Number of instances**, enter the number
      of instances that you want to register to your gateway with this
      activation key.
   3. For **Instance role**, choose the IAM role
      to associate with your external instances.
   4. Select **Generate registration
      command**.

7. Copy the **Linux command** that is displayed.
8. Run the command on each instance you want to register to this
   gateway.

###### Important

The bash portion of the script must be run as root. If the command
isn't run as root, an error is returned. 9. After a few minutes, the instance will register to the gateway. All
instances registered to this gateway will appear in the
**Instances** tab.

## Next steps

After you’ve registered an instance to a MediaConnect Gateway, you can create a bridge
on that instance. For instructions, see [Creating a MediaConnect Gateway bridge](gateway-components-bridges-create.md "gateway-components-bridges-create.md").

## Additional resources

- [Deregistering a MediaConnect Gateway
  instance](gateway-components-instances-delete.md "gateway-components-instances-delete.md")
