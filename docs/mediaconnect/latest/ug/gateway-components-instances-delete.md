# Deregistering a MediaConnect Gateway

instance

You can deregister an instance you no longer want to use within MediaConnect Gateway. By
deregistering the instance, it will no longer support bridges and will not be a part
of your gateway.

###### Contents

- [Prerequisites](gateway-components-instances-delete.md#gateway-components-instances-delete-prerequisites "gateway-components-instances-delete.md#gateway-components-instances-delete-prerequisites")
- [Procedure](gateway-components-instances-delete.md#gateway-components-instances-delete-procedure "gateway-components-instances-delete.md#gateway-components-instances-delete-procedure")
- [Next steps](gateway-components-instances-delete.md#gateway-components-instances-delete-next-steps "gateway-components-instances-delete.md#gateway-components-instances-delete-next-steps")
  - [Reusing a gateway instance](gateway-components-instances-delete.md#gateway-components-instances-reuse "gateway-components-instances-delete.md#gateway-components-instances-reuse")

- [Additional resources](gateway-components-instances-delete.md#gateway-components-instances-delete-additional-resources "gateway-components-instances-delete.md#gateway-components-instances-delete-additional-resources")

## Prerequisites

The following procedure assumes that you have previously registered at
least one instance to your gateway.

## Procedure

###### To deregister a gateway instance

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. From the navigation pane, select **Gateways**. In the
   **Gateways** section, select the gateway that
   contains the instance you want to deregister.
3. On the gateway **Details** page, select the
   **Instances** tab. Select the **Instance
   ID** of the instance you want to deregister.
4. Select **Deregister**.
5. Confirm the deregistration of the instance by selecting
   **Deregister instance**.
6. Repeat the previous steps for any additional instances you need to
   deregister.

## Next steps

### Reusing a gateway instance

If you want to reuse the instance for Amazon ECS Anywhere or as another
gateway instance, you will need to complete the following steps.

###### To reuse a gateway instance (optional)

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. From the navigation pane, select **Gateways**. In the
   **Gateways** section, select the gateway that contains
   the instance you want to reuse.
3. On the gateway **Details** page, select the
   **Instances** tab. Locate the **Instance
   ID** of the instance you want to reuse.
4. Make sure that the **Instance state** is
   **Deregistered** for the instance you want
   to reuse.
5. From a computer with the access to do so, connect to the instance
   using SSH.
6. Run the following commands, in order.

```
sudo docker stop $(sudo docker ps -f "name=MediaConnectGatewayAgent" -q); \
sudo docker stop ecs-agent; \
sudo systemctl stop ecs amazon-ssm-agent; \
sudo yum remove -y amazon-ecs-init amazon-ssm-agent;  `# or apt or snap as needed` \
sudo rm /var/lib/ecs /etc/ecs /var/lib/amazon/ssm /var/log/ecs /var/log/amazon/ssm -rf; \
sudo docker rm -f ecs-agent ssm-agent; \
sudo docker container rm -f $(sudo docker ps -a -f "name=MediaConnectGatewayAgent" -q); \
sudo docker volume rm -f ecsdata docker run; \
sudo pkill -f -KILL network_bootstra[p]; \
sudo pkill -KILL mcproxy;
```

## Additional resources

For more information about deleting a MediaConnect Gateway and its networks, see [Removing a MediaConnect Gateway](gateway-cleanup-console.md "gateway-cleanup-console.md").
