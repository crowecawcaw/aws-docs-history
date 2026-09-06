

# Enabling Slurm REST API in AWS PCS
<a name="slurm-rest-api-enable"></a>

Enable the Slurm REST API to access your cluster's HTTP interface for programmatic job management and monitoring. You can enable this feature during cluster creation or update an existing cluster that meets the requirements.

## Prerequisites
<a name="slurm-rest-api-enable-prerequisites"></a>

Before enabling the Slurm REST API, ensure you have:
+ **Cluster version**: Slurm version 25.05 or higher.
+ **Security group**: Rules allowing HTTP traffic on port 6820 from your desired sources.

## Procedure
<a name="slurm-rest-api-enable-procedure"></a>

**To enable Slurm REST API on a new cluster**

------
#### [ AWS Management Console ]

1. Open the AWS PCS console at [https://console.aws.amazon.com/pcs/](https://console.aws.amazon.com/pcs/).

1. Choose **Create cluster**.

1. Under **Cluster details**, choose Slurm version 25.05 or higher.

1. Configure the other cluster settings as needed.

1. In the **Scheduler configuration** section, set **REST API** to **Enabled**.

1. Configure your cluster security group to allow HTTP traffic on port 6820 from your desired sources.

1. Complete the cluster creation process.

------
#### [ AWS CLI ]

1. Add a Slurm REST configuration when creating your cluster.

   ```
   aws pcs create-cluster --region {{region}} \
       --cluster-name {{my-cluster}} \
       --scheduler type=SLURM, version={{25.05}} \
       --size {{SMALL}} \
       --networking subnetIds={{subnet-ExampleId1}},securityGroupIds={{sg-ExampleId1}} \
       --slurm-configuration slurmRest='{mode=STANDARD}'
   ```

1. Configure your cluster security group to allow HTTP traffic on port 6820 from your desired sources.

------

**To enable Slurm REST API on an existing cluster**

------
#### [ AWS Management Console ]

1. Open the AWS PCS console at [https://console.aws.amazon.com/pcs/](https://console.aws.amazon.com/pcs/).

1. Choose your cluster from the list.

1. Verify that your cluster uses Slurm version 25.05 or higher in the cluster details.

1. Choose **Edit cluster**.

1. In the **Scheduler configuration** section, set **REST API** to **Enabled**.

1. Choose **Update cluster** to apply the changes.

1. Configure your cluster security group to allow HTTP traffic on port 6820 from your desired sources.

------
#### [ AWS CLI ]

1. Update your cluster with a Slurm REST configuration, as in this example.

   ```
   aws pcs update-cluster --cluster-identifier {{my-cluster}} \
       --slurm-configuration 'slurmRest={mode=STANDARD}'
   ```

1. Configure your cluster security group to allow HTTP traffic on port 6820 from your desired sources.

------

## What happens after enabling
<a name="slurm-rest-api-enable-results"></a>

When you enable the REST API, AWS PCS automatically:
+ Generates a JWT signing key and stores it in AWS Secrets Manager.
+ Exposes the API endpoint at `http://{{<clusterPrivateIpAddress>}}:6820` within your VPC.
+ Updates your cluster configuration to show the REST API endpoint details.

You can now authenticate and use the REST API for job management and cluster operations.