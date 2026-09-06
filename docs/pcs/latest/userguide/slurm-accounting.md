

# Slurm accounting in AWS PCS
<a name="slurm-accounting"></a>

**Note**  
Accounting is supported for Slurm 24.11 or later.

You can enable accounting on your new AWS PCS clusters to monitor cluster usage, enforce resource limits, and manage fine-grained access control to specific queues or compute node groups. AWS PCS creates and manages the accounting database for your cluster, eliminating the need for you to create and manage your own separate accounting database. AWS PCS uses the accounting feature in Slurm. For more information about the accounting feature in Slurm, see the [Slurm documentation at SchedMD.](https://slurm.schedmd.com/accounting.html)

To use accounting, enable it when you create a new cluster and optionally set accounting parameters. After your cluster status is `Active` and has compute node groups, you can connect to the Linux shell of a login node to perform accounting functions, such as viewing job data with the Slurm `sacct` command.

------
#### [ AWS PCS console ]

On the **Create cluster** page, under **Scheduler settings**, enable **Accounting**.

------
#### [ AWS PCS API ]

Provide the `accounting` configuration in your call to the `CreateCluster` API action. In the `accounting` object, set the `mode` to `STANDARD`. For more information, see [CreateCluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_CreateCluster.html) and [Accounting](https://docs.aws.amazon.com/pcs/latest/APIReference/API_Accounting.html) in the *AWS PCS API Reference*.

The following example uses the AWS CLI to call the `CreateCluster` API action. The parameter value substring `accounting='{mode=STANDARD}'` enables accounting. 

```
aws pcs create-cluster --cluster-name {{cluster-name}} \
                       --scheduler type=SLURM,version=25.11 \
                       --size SMALL \
                       --networking subnetIds={{cluster-subnet-id}},securityGroupIds={{cluster-security-group-id}} \
                       --slurm-configuration scaleDownIdleTimeInSeconds=180,accounting='{mode=STANDARD}',slurmCustomSettings='[{parameterName=SelectTypeParameters,parameterValue=CR_CPU_Memory}]'
```

------

**Important**  
 You get additional billing charges if you enable accounting. For more information, see the [AWS PCS pricing page](https://aws.amazon.com/pcs/pricing/). 

## Modifying accounting settings
<a name="slurm-accounting-modify"></a>

You can enable or disable accounting on existing clusters without rebuilding your infrastructure. For more information, see [Updating a cluster in AWS PCS](working-with_clusters_update.md).

When you disable accounting, billing for the accounting feature stops as soon as the cluster enters the `UPDATING` state. When you enable accounting, billing begins when the cluster successfully returns to the `ACTIVE` state.

## Key concepts for Slurm accounting in AWS PCS
<a name="slurm-accounting-concepts"></a>

The following concepts are specific to AWS PCS and control how AWS PCS implements Slurm accounting.

### Accounting database
<a name="slurm-accounting-concepts_accounting-db"></a>

AWS PCS stores your accounting data in a database created in an AWS account that AWS owns. You don't have access to the `slurmdbd.conf.`

### Default purge time
<a name="slurm-accounting-concepts_default-purge-time"></a>

This AWS PCS setting specifies the retention period (in days) for all accounting record types (jobs, events, reservations, steps, suspensions, transactions, usage data). For example, if the value is 30, AWS PCS retains accounting records for 30 days. You provide this value when you create the cluster. If you don't provide a value, AWS PCS retains accounting records in the database indefinitely.

------
#### [ AWS PCS console ]

You specify default purge time as part of the steps to create a cluster. On the **Create cluster** page, enable accounting. Under **Scheduler settings**, provide an integer value for **Default purge time (days)**.

------
#### [ AWS PCS API ]

Specify the `defaultPurgeTimeInDays` as part of the `accounting` information you provide in your call to the `CreateCluster` API action. For more information, see [CreateCluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_CreateCluster.html) and [Accounting](https://docs.aws.amazon.com/pcs/latest/APIReference/API_Accounting.html) in the *AWS PCS API Reference*.

**Note**  
When you use the AWS PCS API to create a cluster, the default value for `defaultPurgeTimeInDays` is `-1` and `0` isn't a valid value.

------

### Accounting policy enforcement
<a name="slurm-accounting-concepts_accounting-policy-enforcement"></a>

This setting determines how strictly Slurm enforces job submission rules, resource limits, and accounting policies for your cluster. This setting corresponds to the `AccountingStorageEnforce` parameter in your cluster's `slurm.conf` file. You can select any combination of enforcement options. If you don’t select any options, there are no accounting constraints applied to jobs on the cluster. AWS PCS supports the following options:
+ **associations** — job-to-account mapping
+ **limits** — resource constraints
+ **QoS** — quality of service requirements
+ **safe mode** — guaranteed completion within limits
+ **nosteps** — disable step accounting
+ **nojobs** — disable job accounting

For more information about these options, see the [Slurm documentation at SchedMD](https://slurm.schedmd.com/slurm.conf.html#OPT_AccountingStorageEnforce).

------
#### [ AWS PCS console ]

You set the options as part of the steps to create a cluster. On the **Create cluster** page, enable accounting. Select the options you want from the **Accounting policy enforcement** dropdown list under **Scheduler settings**.

------
#### [ AWS PCS API ]

In Slurm, these options are set in a cluster's `slurm.conf` file. You don't have direct access to the `slurm.conf` for your AWS PCS cluster. Instead, you provide `SlurmCustomSettings` to the `CreateCluster` API action when you create a cluster. For more information, see [CreateCluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_CreateCluster.html) in the *AWS PCS API Reference*.

------

## Get the accounting configuration for an existing AWS PCS cluster
<a name="slurm-accounting-get"></a>

The Slurm accounting configuration is included in the Slurm configuration for your cluster.

------
#### [ AWS PCS console ]

1. Choose **Clusters** from the navigation pane.

1. Choose the cluster name from the list.

1. On the **Configuration** tab, find the accounting configuration under **Slurm configuration**

------
#### [ AWS PCS API ]

Use the `GetCluster` API action to get the cluster configuration. You can find the accounting configuration in the `slurmConfiguration`. The setting for `mode` and the value of `defaultPurgeTimeInDays` are under `accounting`. The selected accounting policy enforcement options are under `slurmCustomSettings`. For more information, see [GetCluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_GetCluster.html) in the *AWS PCS API Reference*.

------