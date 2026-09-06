

# Deregistering a MediaConnect Gateway instance
<a name="gateway-components-instances-delete"></a>



You can deregister an instance you no longer want to use within MediaConnect Gateway. By deregistering the instance, it will no longer support bridges and will not be a part of your gateway. 

**Contents**
+ [Prerequisites](#gateway-components-instances-delete-prerequisites)
+ [Procedure](#gateway-components-instances-delete-procedure)
+ [Next steps](#gateway-components-instances-delete-next-steps)
  + [Reusing a gateway instance](#gateway-components-instances-reuse)
+ [Additional resources](#gateway-components-instances-delete-additional-resources)

## Prerequisites
<a name="gateway-components-instances-delete-prerequisites"></a>

The following procedure assumes that you have previously registered at least one instance to your gateway.

## Procedure
<a name="gateway-components-instances-delete-procedure"></a>

**To deregister a gateway instance**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. From the navigation pane, select **Gateways**. In the **Gateways** section, select the gateway that contains the instance you want to deregister. 

1. On the gateway **Details** page, select the **Instances** tab. Select the **Instance ID** of the instance you want to deregister.

1. Select **Deregister**.

1. Confirm the deregistration of the instance by selecting **Deregister instance**.

1. Repeat the previous steps for any additional instances you need to deregister.

## Next steps
<a name="gateway-components-instances-delete-next-steps"></a>

### Reusing a gateway instance
<a name="gateway-components-instances-reuse"></a>

If you want to reuse the instance for Amazon ECS Anywhere or as another gateway instance, you will need to complete the following steps.

**To reuse a gateway instance (optional)**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. From the navigation pane, select **Gateways**. In the **Gateways** section, select the gateway that contains the instance you want to reuse. 

1. On the gateway **Details** page, select the **Instances** tab. Locate the **Instance ID** of the instance you want to reuse.

1. Make sure that the **Instance state** is **Deregistered** for the instance you want to reuse.

1. From a computer with the access to do so, connect to the instance using SSH.

1. Run the following commands, in order.

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
<a name="gateway-components-instances-delete-additional-resources"></a>

For more information about deleting a MediaConnect Gateway and its networks, see [Removing a MediaConnect Gateway](gateway-cleanup-console.md).