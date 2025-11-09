# Parameter Reference

The cluster setup uses parameters, including SID and System Number that are unique to your setup. It is useful to predetermine the values with the following examples and guidance.

###### Topics

- [Global AWS Parameters](#_global_parameters "#_global_parameters")
- [Amazon EC2 Instance Parameters](#_amazon_ec2_instance_parameters "#_amazon_ec2_instance_parameters")
- [SAP and Pacemaker Resource Parameters](#_sap_and_pacemaker_resource_parameters "#_sap_and_pacemaker_resource_parameters")
- [Red Hat Cluster Parameters](#_red_hat_cluster_parameters "#_red_hat_cluster_parameters")

## Global AWS Parameters

| Name           | Parameter      | Example        |
| -------------- | -------------- | -------------- |
| AWS account ID | `<account_id>` | `123456789100` |
| AWS Region     | `<region>`     | `us-east-1`    |

- AWS account – For more details, see [Your AWS account ID and its alias](../../../IAM/latest/UserGuide/console-account-alias.md "../../../IAM/latest/UserGuide/console-account-alias.md").
- AWS Region – For more details, see [Describe your Regions](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-availability-zones "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-availability-zones").

## Amazon EC2 Instance Parameters

| Name                   | Parameter                | Primary example            | Secondary example          |
| ---------------------- | ------------------------ | -------------------------- | -------------------------- |
| Amazon EC2 instance ID | `<instance_id_x>`        | `i-xxxxinstidforhost1`     | `i-xxxxinstidforhost2`     |
| Hostname               | `<hostname_x>`           | `hanahost01`               | `hanahost02`               |
| Host IP                | `<host_ip_x>`            | `10.1.20.1`                | `10.2.20.1`                |
| Host additional IP     | `<host_additional_ip_x>` | `10.1.20.2`                | `10.2.20.2`                |
| Configured subnet      | `<subnet_id>`            | `subnet-xxxxxxxxxxsubnet1` | `subnet-xxxxxxxxxxsubnet2` |

- Hostnames must comply with SAP requirements outlined in [SAP Note 611361 - Hostnames of SAP ABAP Platform servers](https://me.sap.com/notes/611361 "https://me.sap.com/notes/611361") (requires SAP portal access).
- Run the following command on your instances to retrieve the hostname:

```
$ hostname
```

- Amazon EC2 instance ID – run the following command (IMDSv2 compatible) on your instances to retrieve instance metadata:

```
$ /usr/bin/curl --noproxy '*' -w "\n" -s -H "X-aws-ec2-metadata-token: $(curl --noproxy '*' -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")" http://169.254.169.254/latest/meta-data/instance-id
```

For more details, see [Retrieve instance metadata](../../../AWSEC2/latest/UserGuide/instancedata-data-retrieval.md "../../../AWSEC2/latest/UserGuide/instancedata-data-retrieval.md") and [Instance identity documents](../../../AWSEC2/latest/UserGuide/instance-identity-documents.md "../../../AWSEC2/latest/UserGuide/instance-identity-documents.md").

**For Scale-out Deployments**

| Role     | Primary Coordinator        | Primary Worker             | Primary Worker             | Secondary Coordinator      | Secondary Worker           | Secondary Worker           | Majority Maker             |
| -------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| Hostname | `hanahost01`               | `hanahostworker01a`        | `hanahostworker01b`        | `hanahost02`               | `hanahostworker02a`        | `hanahostworker02b`        | `hanamm`                   |
| Subnet   | `subnet-xxxxxxxxxxsubnet1` | `subnet-xxxxxxxxxxsubnet1` | `subnet-xxxxxxxxxxsubnet1` | `subnet-xxxxxxxxxxsubnet2` | `subnet-xxxxxxxxxxsubnet2` | `subnet-xxxxxxxxxxsubnet2` | `subnet-xxxxxxxxxxsubnet3` |

- Example for a 6 node cluster with a majority maker
- The majority maker can use minimal resources as it only provides cluster quorum functionality

## SAP and Pacemaker Resource Parameters

| Name                                        | Parameter                 | Example                |
| ------------------------------------------- | ------------------------- | ---------------------- |
| SAP HANA SID                                | `<SID>` or `<sid>`        | `HDB`                  |
| SAP HANA System Number                      | `<hana_sys_nr>`           | `00`                   |
| SAP HANA Virtual Hostname                   | `<hana_virt_hostname>`    | `hanahdb`              |
| SAP HANA Overlay IP                         | `<hana_overlayip>`        | `172.16.52.1`          |
| SAP HANA Read Enabled Overlay IP (optional) | `<readenabled_overlayip>` | `172.16.52.2`          |
| VPC Route Tables                            | `<routetable_id>`         | `rtb-xxxxxroutetable1` |

- SAP details – SAP parameters, including SID and instance number must follow the guidance and limitations of SAP and Software Provisioning Manager. Refer to [SAP Note 1979280 - Reserved SAP System Identifiers (SAPSID) with Software Provisioning Manager](https://me.sap.com/notes/1979280 "https://me.sap.com/notes/1979280") for more details.
- Post-installation, use the following command to find the details of the instances running on a host:

```
$ sudo /usr/sap/hostctrl/exe/saphostctrl -function ListInstances
```

- Overlay IP – This value is defined by you. For more information, see [Overlay IP](sap-hana-pacemaker-rhel-concepts.md#overlay-ip-rhel "sap-hana-pacemaker-rhel-concepts.md#overlay-ip-rhel").

## Red Hat Cluster Parameters

| Name                    | Parameter               | Example     |
| ----------------------- | ----------------------- | ----------- |
| Cluster user            | `<cluster_user>`        | `hacluster` |
| Cluster password        | `<cluster_password>`    |             |
| Cluster name            | `<cluster_name>`        | `myCluster` |
| AWS CLI cluster profile | `<cli_cluster_profile>` | `cluster`   |

- Cluster user – Installing cluster packages will create the user hacluster, set a password to this account to ensure that the cluster can perform the tasks which do not require root access.
