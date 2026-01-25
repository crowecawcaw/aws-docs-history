# EC2 Instance Configuration

Amazon EC2 instance settings can be applied using Infrastructure as Code or manually using AWS Command Line Interface or AWS Console. We recommend Infrastructure as Code automation to reduce manual steps, and ensure consistency.

###### Topics

- [Assign or Review Pacemaker IAM Role](#_assign_or_review_pacemaker_iam_role "#_assign_or_review_pacemaker_iam_role")
- [Assign or Review Security Groups](#_assign_or_review_security_groups "#_assign_or_review_security_groups")
- [Assign Secondary IP Addresses](#_assign_secondary_ip_addresses "#_assign_secondary_ip_addresses")
- [Disable Source/Destination Check](#source_dest "#source_dest")
- [Review Stop Protection](#stop_protection "#stop_protection")
- [Review Automatic Recovery](#auto_recovery "#auto_recovery")

###### Important

The following configurations must be performed on all cluster nodes. Ensure consistency across nodes to prevent cluster issues.

## Assign or Review Pacemaker IAM Role

The two cluster resource IAM policies must be assigned to an IAM role associated with your Amazon EC2 instance. If an IAM role is not associated to your instance, create a new IAM role for cluster operations.

1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Select one of your cluster nodes.
3. In the navigation pane, choose **Actions** → **Security** → **Modify IAM role**.
4. Choose the IAM role that contains the policies created in [Create IAM Roles and Policies for Pacemaker](sap-hana-pacemaker-rhel-infra-setup.md#iam_roles_rhel "sap-hana-pacemaker-rhel-infra-setup.md#iam_roles_rhel").
5. Choose **Update IAM role**.
6. Repeat these steps for all nodes in the cluster.

## Assign or Review Security Groups

The security group rules created in the AWS
[Modify Security Groups for Cluster Communication](sap-hana-pacemaker-rhel-infra-setup.md#sg-rhel "sap-hana-pacemaker-rhel-infra-setup.md#sg-rhel") section must be assigned to your Amazon EC2 instances. If a security group is not associated with your instance, or if the required rules are not present in the assigned security group, add the security group or update the rules.

1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Select one of your cluster nodes.
3. In the **Security** tab, review the security groups, ports, and source of traffic.
4. If required, choose **Actions** → **Security** → **Change security groups**.
5. Under **Associated security groups**, search for and select the required groups.
6. Choose **Save**.
7. Repeat these steps for all nodes in the cluster.

You can verify the security group rules on your instances using the AWS CLI:

```
$ aws ec2 describe-instance-attribute --instance-id <instance_id> --attribute groupSet
```

## Assign Secondary IP Addresses

Secondary IP addresses are used to create a redundant communication channel (secondary ring) in corosync for clusters. The cluster nodes can use the secondary ring to communicate in case of underlying network disruptions.

These IPs are only used in cluster configurations. The secondary IPs provide the same fault tolerance as a secondary Elastic Network Interface (ENI). For more information, see [Secondary IP addresses for your EC2 Instance](../../../AWSEC2/latest/UserGuide/instance-secondary-ip-addresses.md "../../../AWSEC2/latest/UserGuide/instance-secondary-ip-addresses.md").

You can verify the secondary IP configuration on your instances using the AWS CLI:

```
$ aws ec2 describe-instances --instance-id <instance_id> \
    --query 'Reservations[*].Instances[*].NetworkInterfaces[*].PrivateIpAddresses[*].PrivateIpAddress' \
    --output text
```

Verify that:

- Each instance returns two IP addresses from the same subnet
- The primary network interface (eth0) has both IPs assigned
- The secondary IPs will be used later for ring0_addr and ring1_addr in corosync.conf

## Disable Source/Destination Check

Amazon EC2 instances perform source/destination checks by default, requiring that an instance is either the source or the destination of any traffic it sends or receives. In the pacemaker cluster, source/destination check must be disabled on both instances receiving traffic from the Overlay IP.

The following AWS Console or AWS CLI commands can be used to modify the attribute.

AWS Console

1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Select one of your cluster nodes.
3. In the navigation pane, choose **Actions** → **Networking** → **Change source/destination check**.
4. For Source/Destination Checking, choose **Stop** to allow traffic when the source or destination is not the instance itself.
5. Repeat these steps for all nodes in the cluster.

AWS CLI
To modify using the AWS CLI (requires appropriate configuration permissions):

```
$ aws ec2 modify-instance-attribute --instance-id <instance_id> --no-source-dest-check
```

Repeat for all nodes in the cluster.

To confirm the value of an attribute for a particular instance, use the following command. The value `false` means source/destination checking is disabled

```
$ aws ec2 describe-instance-attribute --instance-id <instance_id> --attribute sourceDestCheck
```

The output

```
{
    "InstanceId": "i-xxxxinstidforhost1",
    "SourceDestCheck": {
        "Value": false
    }
}
```

## Review Stop Protection

To ensure that STONITH actions can be executed, you must ensure that stop protection is disabled for Amazon EC2 instances that are part of a pacemaker cluster. If the default settings have been modified, use the following commands for both instances to disable stop protection via AWS CLI.

The following AWS Console or CLI commands can be used to modify the attribute.

AWS Console

1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Select one of your cluster nodes.
3. Choose **Actions** → **Instance settings** → **Change stop protection**.
4. Ensure **Stop protection** is not enabled.
5. Repeat these steps for all nodes in the cluster.

AWS CLI
To modify using the AWS CLI (requires appropriate configuration permissions):

```
$ aws ec2 modify-instance-attribute --instance-id <instance_id> --no-disable-api-stop
```

Repeat this command for all nodes in the cluster.

To confirm the value of an attribute for a particular instance, use the following command. The value `false` means it is possible to stop the instance using an AWS CLI.

```
$ aws ec2 describe-instance-attribute --instance-id <instance_id> --attribute disableApiStop
```

The output

```
{
    "InstanceId": "i-xxxxinstidforhost1",
    "DisableApiStop": {
        "Value": false
    }
}
```

## Review Automatic Recovery

After a failure, cluster-controlled operations must be resumed in a coordinated way. This helps ensure that the cause of failure is known and addressed, and the status of the cluster is as expected. For example, verifying that there are no pending fencing actions.

The following AWS Console or CLI commands can be used to modify the attribute.

AWS Console

1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Select one of your cluster nodes.
3. Choose **Actions** → **Instance settings** → **Change auto-recovery behavior**.
4. Select **Off** to disable auto-recovery for system status check failures.
5. Repeat these steps for all nodes in the cluster.

AWS CLI
To modify auto-recovery settings (requires appropriate configuration permissions):

```
$ aws ec2 modify-instance-maintenance-options --instance-id <instance_id> --auto-recovery disabled
```

Repeat this command for all nodes in the cluster.

To confirm the value of an attribute for a particular instance, use the following command. The value `disabled` means autorecovery will not be attempted.

```
$ aws ec2 describe-instances --instance-ids <instance_id> --query 'Reservations[*].Instances[*].MaintenanceOptions.AutoRecovery'
```

The output:

```
[
    [
        "disabled"
    ]
]
```
