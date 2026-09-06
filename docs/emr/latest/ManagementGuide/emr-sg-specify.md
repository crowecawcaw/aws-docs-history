

# Specifying Amazon EMR-managed and additional security groups
<a name="emr-sg-specify"></a>

You can specify security groups using the AWS Management Console, the AWS CLI, or the Amazon EMR API. If you don't specify security groups, Amazon EMR creates default security groups. Specifying additional security groups is optional. You can assign additional security groups for primary instances, core and task instances, and service access (private subnets only).

------
#### [ Console ]

**To specify security groups with the console**

1. Sign in to the AWS Management Console, and open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr).

1. Under **EMR on EC2** in the left navigation pane, choose **Clusters**, and then choose **Create cluster**.

1. Under **Networking**, select the arrow next to **EC2 security groups (firewall)** to expand this section. Under **Primary node** and **Core and task nodes**, the default Amazon EMR managed security groups are selected by default. If you use a private subnet, you also have the option to select a security group for **Service access**.

1. To change your Amazon EMR managed security group, use the **Choose security groups** dropdown menu to select a different option from the **Amazon EMR-managed security group** list of options. You have one Amazon EMR managed security group for both **Primary node** and **Core and task nodes**.

1. To add custom security groups, use the same **Choose security groups** dropdown menu to select up to four custom security groups from the **Custom security group** list of options. You can have up to four custom security groups for both **Primary node** and **Core and task nodes**.

1. Choose any other options that apply to your cluster. 

1. To launch your cluster, choose **Create cluster**.

------

## Specifying security groups with the AWS CLI
<a name="emr-sg-specify-cli"></a>

To specify security groups using the AWS CLI you use the `create-cluster` command with the following parameters of the `--ec2-attributes` option:


| Parameter | Description | 
| --- | --- | 
| `EmrManagedPrimarySecurityGroup` | Use this parameter to specify a custom managed security group for the primary instance. If this parameter is specified, `EmrManagedCoreSecurityGroup` must also be specified. For clusters in private subnets, `ServiceAccessSecurityGroup` must also be specified. | 
| `EmrManagedCoreSecurityGroup` | Use this parameter to specify a custom managed security group for core and task instances. If this parameter is specified, `EmrManagedPrimarySecurityGroup` must also be specified. For clusters in private subnets, `ServiceAccessSecurityGroup` must also be specified. | 
| `ServiceAccessSecurityGroup` | Use this parameter to specify a custom managed security group for service access, which applies only to clusters in private subnets. The security group you specify as `ServiceAccessSecurityGroup` should not be used for any other purpose and should also be reserved for Amazon EMR. If this parameter is specified, `EmrManagedPrimarySecurityGroup` must also be specified. | 
| `AdditionalPrimarySecurityGroups` | Use this parameter to specify up to four additional security groups for the primary instance. | 
| `AdditionalCoreSecurityGroups` | Use this parameter to specify up to four additional security groups for core and task instances. | 

**Example — specify custom Amazon EMR-managed security groups and additional security groups**  
The following example specifies custom Amazon EMR managed security groups for a cluster in a private subnet, multiple additional security groups for the primary instance, and a single additional security group for core and task instances.  
Linux line continuation characters (\\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
 1. aws emr create-cluster --name "{{ClusterCustomManagedAndAdditionalSGs}}" \
 2. --release-label emr-{{emr-7.13.0}} --applications Name={{Hue}} Name={{Hive}} \
 3. Name={{Pig}} --use-default-roles --ec2-attributes \
 4. SubnetIds={{subnet-xxxxxxxxxxxx}},KeyName={{myKey}},\
 5. ServiceAccessSecurityGroup={{sg-xxxxxxxxxxxx}},\
 6. EmrManagedPrimarySecurityGroup={{sg-xxxxxxxxxxxx}},\
 7. EmrManagedCoreSecurityGroup={{sg-xxxxxxxxxxx}},\
 8. AdditionalPrimarySecurityGroups=['{{sg-xxxxxxxxxxx}}',\
 9. '{{sg-xxxxxxxxxxx}}','{{sg-xxxxxxxxxx}}'],\
10. AdditionalCoreSecurityGroups={{sg-xxxxxxxxxxx}} \
11. --instance-type {{m5.xlarge}}
```

For more information, see [create-cluster](https://docs.aws.amazon.com/cli/latest/reference/emr/create-cluster.html) in the *AWS CLI Command Reference*.