# Removing a MediaConnect Gateway

To remove a gateway, you must first remove all of its components, such as its
networks, instances, and bridges. The following is the process for removing a
gateway and its components.

###### Contents

- [Prerequisites](gateway-cleanup-console.md#gateway-create-prerequisites "gateway-cleanup-console.md#gateway-create-prerequisites")
- [Procedure](gateway-cleanup-console.md#gateway-create-procedure "gateway-cleanup-console.md#gateway-create-procedure")

## Prerequisites

The following procedure assumes that you have previously created at least one
MediaConnect Gateway.

## Procedure

You can remove a gateway using the console or the AWS CLI.

Console

###### To remove a gateway using the console

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. From the navigation pane, select
   **Gateways**. In the
   **Gateways** section, select the gateway
   you want to delete.
3. On the MediaConnect Gateway details page, select the
   **Bridges** tab. Complete the following
   steps to delete the bridges:
   1. Select the bridge you want to delete.
   2. If the bridge has been started, select
      **Stop**.
   3. When the bridge is stopped, select
      **Delete**.
   4. Confirm the deletion of the bridge by selecting
      **Delete bridge**.
   5. Repeat these steps for any additional bridges you need
      to delete.

4. Return to the gateway's **Details** page,
   select the **Instances** tab. Complete the
   following steps to delete the instances:
   1. Select the instance you want to delete.
   2. Select **Deregister**.
   3. Confirm the deregistration of the instance by
      selecting **Deregister
      instance**.
   4. Repeat these steps for any additional instances you
      need to deregister.

   ###### Note

   **OPTIONAL**: If you
   want to reuse the instance for Amazon ECS Anywhere or as
   another gateway instance, you will need to complete
   the following steps. If not, continue with Step 5. 5. Make sure that the **Instance state**
   is **Deregistered** for the instance
   you want to reuse. 6. From a computer with the access to do so, connect to
   the instance using SSH. 7. Run the following commands, in order:

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

5. After successfully deleting all bridges and deregistering all
   instances associated with the gateway, you may delete the
   gateway. Deleting the gateway will delete all networks created
   under that gateway.
   1. From the navigation pane, select
      **Gateways**.
   2. In the **Gateways** section, select
      the gateway that you want to delete to view that
      gateway's **Details** page.
   3. Choose the **Delete** button.
   4. Confirm the deletion of the gateway by choosing
      **Delete gateway**.

AWS CLI

###### To remove a gateway using the AWS CLI

1. Delete the bridges by running the following command.

```
aws --profile `<Profile>` --region `<Region>` mediaconnect delete-bridge --bridge-arn `<BridgeArn>`
```

2. Deregister the instances by running the following
   command.

```
aws --profile `<Profile>` --region `<Region>` mediaconnect deregister-gateway-instance --gateway-instance-arn `<GatewayArn>`
```

###### Note

**OPTIONAL**: If you want to
reuse the instance for Amazon ECS Anywhere or as another
AWS Elemental MediaConnect Gateway instance, you will need to complete the following
steps. If not, continue with Step 3.

    1. Make sure that the `InstanceState` is
     `DEREGISTERED` for the instance you want
     to reuse. You can verify using the
     `describe-gateway-instance` command shown
     in the following example.



    ```
    aws --profile `<Profile>` --region `<Region>` mediaconnect describe-gateway-instance
          --gateway-instance-arn `<GatewayInstanceArn>`
    ```
    2. From a computer with the access to do so, connect to
     the instance using SSH.
    3. Run the following commands, in order.



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

3. Delete the gateway. This will delete all networks associated
   with the gateway.

```
aws --profile `<Profile>` --region `<Region>` mediaconnect delete-gateway --gateway-arn `<GatewayArn>`
```
