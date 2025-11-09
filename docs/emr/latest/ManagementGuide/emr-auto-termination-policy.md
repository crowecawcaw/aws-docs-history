# Using an auto-termination policy for Amazon EMR cluster cleanup

An auto-termination policy lets you orchestrate cluster cleanup without the need to
monitor and manually terminate unused clusters. When you add an auto-termination policy
to a cluster, you specify the amount of idle time after which the cluster should
automatically shut down.

Depending on release version, Amazon EMR uses different criteria to mark a cluster as idle.
The following table outlines how Amazon EMR determines cluster idleness.

| When you use ...                                            | A cluster is considered idle when ...                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon EMR versions 5.34.0 and later, and 6.4.0 and later   | • There are no active YARN applications<br>• HDFS utilization is below 10%<br>• There are no active EMR notebook or EMR Studio<br>connections<br>• There are no on-cluster application user interfaces in<br>use<br>• There are no pending steps                                                                                                                                                                                  |
| Amazon EMR versions 5.30.0<br>• 5.33.0 and 6.1.0<br>• 6.3.0 | • There are no active YARN applications<br>• The cluster has no active Spark jobs<br>NoteAmazon EMR marks a cluster as idle and may automatically terminate<br>the cluster even if you have an active Python3 kernel. This is<br>because executing a Python3 kernel does not submit a Spark job<br>on the cluster. To use auto-termination with a Python3 kernel,<br>we recommend that you use Amazon EMR version 6.4.0 or later. |

###### Note

Amazon EMR versions 6.4.0 and later support an on-cluster file for detecting activity
on the primary node: `/emr/metricscollector/isbusy`. When you use
a cluster to run shell scripts or non-YARN applications, you can periodically touch
or update `isbusy` to tell Amazon EMR that the cluster is not idle.

You can attach an auto-termination policy when you create a cluster, or add a policy
to an existing cluster. To change or disable auto-termination, you can update or remove
the policy.

## Considerations

Consider the following features and limitations before using an auto-termination
policy:

- In the following AWS Regions, Amazon EMR auto-termination is available with
  Amazon EMR 6.14.0 and higher:
  - Europe (Spain) (eu-south-2)

- In the following AWS Regions, Amazon EMR auto-termination is available with
  Amazon EMR 5.30.0 and 6.1.0 and higher:
  - US East (N. Virginia) (us-east-1)
  - US East (Ohio) (us-east-2)
  - US West (Oregon) (us-west-2)
  - US West (N. California) (us-west-1)
  - Africa (Cape Town) (af-south-1)
  - Asia Pacific (Hong Kong) (ap-east-1)
  - Asia Pacific (Mumbai) (ap-south-1)
  - Asia Pacific (Hyderabad) (ap-south-2)
  - Asia Pacific (Seoul) (ap-northeast-2)
  - Asia Pacific (Osaka) (ap-northeast-3)
  - Asia Pacific (Singapore) (ap-southeast-1)
  - Asia Pacific (Sydney) (ap-southeast-2)
  - Asia Pacific (Jakarta) (ap-southeast-3)
  - Asia Pacific (Tokyo) (ap-northeast-1)
  - Canada (Central) (ca-central-1)
  - South America (São Paulo) (sa-east-1)
  - Europe (Frankfurt) (eu-central-1)
  - Europe (Zurich) (eu-central-2)
  - Europe (Ireland) (eu-west-1)
  - Europe (London) (eu-west-2)
  - Europe (Milan) (eu-south-1)
  - Europe (Paris) (eu-west-3)
  - Europe (Stockholm) (eu-north-1)
  - Israel (Tel Aviv) (il-central-1)
  - Middle East (UAE) (me-central-1)
  - China (Beijing) (cn-north-1)
  - China (Ningxia) (cn-northwest-1)
  - AWS GovCloud (US-East) (us-gov-east-1)
  - AWS GovCloud (US-West) (us-gov-west-1)

- Idle timeout defaults to 60 minutes (one hour) when you don't specify an
  amount. You can specify a minimum idle timeout of one minute, and a maximum
  idle timeout of 7 days.
- With Amazon EMR versions 6.4.0 and later, auto-termination is enabled by
  default when you create a new cluster with the Amazon EMR console.
- Amazon EMR publishes high-resolution Amazon CloudWatch metrics when you
  enable auto-termination for a cluster. You can use these metrics to track
  cluster activity and idleness. For more information, see [Cluster capacity metrics](UsingEMR_ViewingMetrics.md#emr-metrics-managed-scaling "UsingEMR_ViewingMetrics.md#emr-metrics-managed-scaling").
- Auto-termination is not supported when you use non-YARN based applications
  such as Presto, Trino, or HBase.
- To use auto-termination, the metrics-collector process must be able to
  connect to the public API endpoint for auto-termination in API Gateway. If you use
  a private DNS name with Amazon Virtual Private Cloud, auto-termination won't function
  properly. To ensure that auto-termination works, we recommend that you take
  one of the following actions:
  - Remove the API Gateway interface VPC endpoint from your Amazon VPC.
  - Follow the instructions in [Why do I get an HTTP 403 Forbidden error when connecting to my
    API Gateway APIs from a VPC?](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-vpc-connections/ "https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-vpc-connections/") to disable the private DNS name
    setting.
  - Launch your cluster in a private subnet instead. For more
    information, see the topic on [Private subnets](emr-clusters-in-a-vpc.md#emr-vpc-private-subnet "emr-clusters-in-a-vpc.md#emr-vpc-private-subnet").

- (EMR 5.30.0 and later) If you remove the default **Allow
  All** outbound rule to 0.0.0.0/ for the primary security group,
  you must add a rule that allows outbound TCP connectivity to your security
  group for service access on port 9443. Your security group for service
  access must also allow inbound TCP traffic on port 9443 from the primary
  security group. For more information about configuring security groups, see
  [Amazon EMR-managed security group for the primary instance (private
  subnets)](emr-man-sec-groups.md#emr-sg-elasticmapreduce-master-private "emr-man-sec-groups.md#emr-sg-elasticmapreduce-master-private").

## Permissions to use

auto-termination

Before you can apply and manage auto-termination policies for Amazon EMR, you need to attach the permissions that are listed in the following example IAM permissions policy to the IAM resources that manage your EMR cluster.

```
{
  "Version": "2012-10-17",
  "Statement": {
      "Sid": "AllowAutoTerminationPolicyActions",
      "Effect": "Allow",
      "Action": [
        "elasticmapreduce:PutAutoTerminationPolicy",
        "elasticmapreduce:GetAutoTerminationPolicy",
        "elasticmapreduce:RemoveAutoTerminationPolicy"
      ],
      "Resource": "`<your-resources>`"
    }
}
```

## Attach, update, or remove an

auto-termination policy

This section includes instructions to help you attach, update, or remove an
auto-termination policy from an Amazon EMR cluster. Before you work with auto-termination
policies, make sure you have the necessary IAM permissions. See [Permissions to use
auto-termination](#emr-auto-termination-permissions "#emr-auto-termination-permissions").

Console

###### To attach an auto-termination policy when you create a cluster

with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation
   pane, choose **Clusters**, and then choose
   **Create cluster**.
3. Under **Cluster termination**, select
   **Terminate cluster after idle time**.
4. Specify the number of idle hours and minutes that can elapse
   before the cluster auto-terminates. The default idle time is 1
   hour.
5. Choose any other options that apply to your cluster.
6. To launch your cluster, choose **Create
   cluster**.

###### To attach, update, or remove an auto-termination policy on a

running cluster with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation
   pane, choose **Clusters**, and select the
   cluster that you want to update.
3. On the **Properties** tab of the cluster
   details page, find **Cluster termination** and
   select **Edit**.
4. Select or clear **Enable auto-termination**
   to turn the feature on or off. If you turn on auto-termination,
   specify the number of idle hours and minutes that can elapse
   before the cluster auto-terminates. Then select **Save
   changes** to confirm.

AWS CLI
**Before you start**

Before you work with auto-termination policies, we recommend that you
update to the latest version of the AWS CLI. For instructions, see [Installing,
updating, and uninstalling the AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md").

###### To attach or update an auto-termination policy using the

AWS CLI

- You can use the `aws emr
put-auto-termination-policy` command to attach or
  update an auto-termination policy on a cluster.

The following example specifies 3600 seconds for
`IdleTimeout`. If you don't specify
`IdleTimeout`, the value defaults
to one hour.

```
aws emr put-auto-termination-policy \
--cluster-id `<your-cluster-id>` \
--auto-termination-policy IdleTimeout=3600
```

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

You can also specify a value for
`--auto-termination-policy` when you use the
`aws emr create-cluster` command. For more
information on using Amazon EMR commands in the AWS CLI, see the [AWS CLI Command
Reference](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

###### To remove an auto-termination policy with the AWS CLI

- Use the `aws emr remove-auto-termination-policy`
  command to remove an auto-termination policy from a cluster. For
  more information on using Amazon EMR commands in the AWS CLI, see the
  [AWS CLI Command
  Reference](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

```
aws emr remove-auto-termination-policy --cluster-id `<your-cluster-id>`
```
