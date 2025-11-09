# Deregistering an Amazon ECS external instance

We recommend that you deregister the
instance from both Amazon ECS and AWS Systems Manager after you are done with the instance. Following deregistration, the external instance is
no longer able to accept new tasks.

If you have tasks that are running on the container instance when you deregister it, the
tasks remain running until they stop through some other means. However, these tasks are no
longer monitored or accounted for by Amazon ECS. If these tasks on your external instance are
part of an Amazon ECS service, then the service scheduler starts another copy of that task, on a
different instance, if possible.

After you deregister the instance, clean up the remaining AWS resources on
the instance. You can then register it to a new cluster.

## Procedure

AWS Management Console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. From the navigation bar, choose the Region where your external
   instance is registered.
3. In the navigation pane, choose **Clusters** and
   select the cluster that hosts the external instance.
4. On the **Cluster : `name`**
   page, choose the **Infrastructure** tab.
5. Under **Container instances**, select the external
   instance ID to deregister. You're redirected to the container instance
   detail page.
6. On the **Container Instance :
   `id`** page, choose
   **Deregister**.
7. Review the deregistration message. Select **Deregister from
   AWS Systems Manager** to also deregister the external instance as an
   Systems Manager managed instance. Choose **Deregister**.

###### Note

You can deregister the external instance as an Systems Manager managed
instance in the Systems Manager console. For instructions, see [Deregistering managed nodes in a hybrid and multicloud environment](../../../systems-manager/latest/userguide/fleet-manager-deregister-hybrid-nodes.md "../../../systems-manager/latest/userguide/fleet-manager-deregister-hybrid-nodes.md") in the
_AWS Systems Manager User Guide_. 8. After you deregister the instance, clean up AWS resources on your
on-premises server or VM.

| Operating system | Steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linux            | 1. Stop the Amazon ECS container agent and the SSM<br>Agent services on the instance.<br>``<br>`sudo systemctl stop ecs amazon-ssm-agent`<br>``<br>2. Remove the Amazon ECS and Systems Manager packages.<br>**For CentOS 7, CentOS<br>8, and RHEL 7**<br>``<br>`sudo yum remove -y amazon-ecs-init amazon-ssm-agent`<br>``<br>**For SUSE Enterprise<br>Server 15**<br>``<br>`sudo zypper remove -y amazon-ecs-init amazon-ssm-agent`<br>``<br>**For Debian and<br>Ubuntu**<br>``<br>`sudo apt remove -y amazon-ecs-init amazon-ssm-agent`<br>``<br>3. Remove the leftover directories.<br>``<br>`sudo rm -rf /var/lib/ecs /etc/ecs /var/lib/amazon/ssm /var/log/ecs /var/log/amazon/ssm`<br>`` |
| Windows          | 1. Stop the Amazon ECS container agent and the SSM<br>Agent services on the instance.<br>``<br>`Stop-Service AmazonECS`<br>``<br>``<br>`Stop-Service AmazonSSMAgent`<br>``<br>2. Remove the Amazon ECS package.<br>``<br>`.\ecs-anywhere-install.ps1 -Uninstall`<br>``                                                                                                                                                                                                                                                                                                                                                                                                                          |

AWS CLI

1. You need the instance ID and the container instance ARN to deregister
   the container instance. If you do not have theses values, run the
   following comands

Run the following commandto get the instance ID.

You use the instance ID (`instanceID`) to get the container
instance ARN (`containerInstanceARN`).

```
instanceId=$(aws ssm describe-instance-information --region "{{ `region` }}" | jq ".InstanceInformationList[] |select(.IPAddress==\"{{ IPv4 Address }}\") | .InstanceId" | tr -d'"'
```

Run the following commands.

You use the `containerInstanceArn` as a parameter in the
command to deregister the instance
(`deregister-container-instance`).

```
instances=$(aws ecs list-container-instances --cluster "{{ `cluster` }}" --region "{{ `region` }}" | jq -c '.containerInstanceArns')
containerInstanceArn=$(aws ecs describe-container-instances --cluster "{{ `cluster` }}" --region "{{ `region` }}" --container-instances $instances | jq ".containerInstances[] | select(.ec2InstanceId==\"{{ `instanceId` }}\") | .containerInstanceArn" | tr -d '"')
```

2. Run the following command to drain the instance.

```
aws ecs update-container-instances-state --cluster "{{ `cluster` }}" --region "{{ `region` }}" --container-instances "{{ `containerInstanceArn` }}" --status DRAINING
```

3. After the container instance finishes draining, run the following
   command to deregister the instance.

```
aws ecs deregister-container-instance --cluster "{{ `cluster` }}" --region "{{ `region` }}" --container-instance "{{ `containerInstanceArn` }}"
```

4. Run the following command to remove the container instance from
   SSM.

```
aws ssm deregister-managed-instance --region "{{ `region` }}" --instance-id "{{ `instanceId` }}"
```

5. After you deregister the instance, clean up AWS resources on your
   on-premises server or VM.

| Operating system | Steps                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linux            | 1. Stop the Amazon ECS container agent and the SSM<br>Agent services on the instance.<br>``<br>`sudo systemctl stop ecs amazon-ssm-agent`<br>``<br>2. Remove the Amazon ECS and Systems Manager packages.<br>``<br>`sudo (yum/apt/zypper) remove amazon-ecs-init amazon-ssm-agent`<br>``<br>3. Remove the leftover directories.<br>``<br>`sudo rm -rf /var/lib/ecs /etc/ecs /var/lib/amazon/ssm /var/log/ecs /var/log/amazon/ssm`<br>`` |
| Windows          | 1. Stop the Amazon ECS container agent and the SSM<br>Agent services on the instance.<br>``<br>`Stop-Service AmazonECS`<br>``<br>``<br>`Stop-Service AmazonSSMAgent`<br>``<br>2. Remove the Amazon ECS package.<br>``<br>`.\ecs-anywhere-install.ps1 -Uninstall`<br>``                                                                                                                                                                  |
