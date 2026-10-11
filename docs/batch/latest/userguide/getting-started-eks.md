

# Getting started with AWS Batch on Amazon EKS
<a name="getting-started-eks"></a>

AWS Batch on Amazon EKS is a managed service for scheduling and scaling batch workloads into existing Amazon EKS clusters. AWS Batch doesn't create, administer, or perform lifecycle operations of your Amazon EKS clusters on your behalf. AWS Batch orchestration scales up and down nodes managed by AWS Batch and run pods on those nodes.

**Note**  
This tutorial uses Amazon EKS access entries for cluster authentication. Access entries are the recommended method and are required for Amazon EKS clusters whose `authenticationMode` is `API`. They're also available for Amazon EKS clusters whose `authenticationMode` is `API_AND_CONFIG_MAP`.  
If your cluster's `authenticationMode` is `CONFIG_MAP`, we recommend that you update your cluster to `API_AND_CONFIG_MAP` so that you can follow this tutorial. To use the legacy `aws-auth` ConfigMap approach, see [Getting started with AWS Batch on Amazon EKS using ConfigMap authentication](getting-started-eks-configmap.md).  
For more information about authentication methods, see [Amazon EKS access entry authentication](eks-access-entries.md).

AWS Batch doesn't touch nodes, auto scaling node groups or pods lifecycles that aren't associated with AWS Batch compute environments within your Amazon EKS cluster. For AWS Batch to operate effectively, its [service-linked role](using-service-linked-roles.md) needs access to your existing Amazon EKS cluster. AWS Batch creates an Amazon EKS access entry for the service-linked role, and you associate an access policy that grants AWS Batch permissions in your namespace.

AWS Batch requires a Kubernetes namespace where it can scope pods as AWS Batch jobs into. We recommend a dedicated namespace to isolate the AWS Batch pods from your other cluster workloads.

After a namespace has been established, you can associate that Amazon EKS cluster to an AWS Batch compute environment using the [CreateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html) API operation. A job queue can be associated with this new Amazon EKS compute environment. AWS Batch jobs are submitted to the job queue based on an Amazon EKS job definition using the [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) API operation. AWS Batch then launches AWS Batch managed nodes and place jobs from job queue as Kubernetes pods into the EKS cluster associated with an AWS Batch compute environment.

The following sections cover how to get set up for AWS Batch on Amazon EKS.

**Contents**
+ [Overview](#getting-started-eks-context)
+ [Prerequisites](#getting-started-eks-prerequisites)
+ [Step 1: Create your Amazon EKS cluster for AWS Batch](#getting-started-eks-step-0)
+ [Step 2: Prepare your Amazon EKS cluster for AWS Batch](#getting-started-eks-step-1)
+ [Step 3: Create an Amazon EKS compute environment](#getting-started-eks-step-2)
+ [Step 3a: Associate the namespace policy](#getting-started-eks-step-2a)
+ [Step 4: Create a job queue and attach the compute environment](#getting-started-eks-step-3)
+ [Step 5: Create a job definition](#getting-started-eks-step-4)
+ [Step 6: Submit a job](#getting-started-eks-step-5)
+ [Step 7: View the Job's output](#getting-started-eks-step-7)
+ [Step 8: (Optional) Submit a job with overrides](#getting-started-eks-step-6)
+ [Step 9: Clean up your tutorial resources](#getting-started-eks-step-8)
+ [Additional resources](#getting-started-eks-additional-resources)

## Overview
<a name="getting-started-eks-context"></a>

This tutorial demonstrates how to setup AWS Batch with Amazon EKS using the AWS CLI, `kubectl` and `eksctl`. 

**Intended Audience**  
This tutorial is designed for system administrators and developers responsible for setting up, testing, and deploying AWS Batch.

**Features Used**  
This tutorial shows you how to use the AWS CLI, to:  
+ Create and configure an Amazon EKS compute environment
+ Create a job queue.
+ Create a job definition
+ Create and submit a job to run
+ Submit a job with overrides

**Time Required**  
It should take about 30–40 minutes to complete this tutorial.

**Regional Restrictions**  
There are no country or regional restrictions associated with using this solution.

**Resource Usage Costs**  
There's no charge for creating an AWS account. However, by implementing this solution, you might incur some or all of the costs that are listed in the following table.  


<table>
<thead>
  <tr><th>Description</th><th>Cost (US dollars)</th></tr>
</thead>
<tbody>
  <tr><td>You are charged by the cluster hour</td><td>Varies depending on Instance, see <a href="https://aws.amazon.com/eks/pricing/">Amazon EKS pricing</a> </td></tr>
</tbody>
</table>


## Prerequisites
<a name="getting-started-eks-prerequisites"></a>

Before starting this tutorial, you must install and configure the following tools and resources that you need to create and manage both AWS Batch and Amazon EKS resources.
+ **AWS CLI** – A command line tool for working with AWS services, including Amazon EKS. This guide requires that you use version 2.37.7 or later of the AWS CLI version 2. Earlier versions don't support the `accessEntry` parameter. For more information, see [Installing, updating, and uninstalling the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) in the *AWS Command Line Interface User Guide*. After installing the AWS CLI, we recommend that you also configure it. For more information, see [Quick configuration with `aws configure`](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config) in the *AWS Command Line Interface User Guide*.
+ **`kubectl`** – A command line tool for working with Kubernetes clusters. Use a `kubectl` version that's within one minor version difference of your cluster's Kubernetes version. For more information, see [Installing or updating `kubectl`](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) in the *Amazon EKS User Guide*.
+ **`eksctl`** – A command line tool for working with Amazon EKS clusters that automates many individual tasks. This guide requires that you use version `0.167.0` or later. For more information, see [Installing or updating `eksctl`](https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html) in the **Amazon EKS User Guide**.
+ **Required IAM permissions** – The IAM security principal that you're using must have permissions to work with Amazon EKS IAM roles and service linked roles, CloudFormation, and a VPC and related resources. For more information, see [Actions, resources, and condition keys for Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelastickubernetesservice.html) and [Using service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) in the *IAM User Guide*. You must complete all steps in this guide as the same user.
+ **Permissions** – Users calling the [CreateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html) API operation to create a compute environment that uses Amazon EKS resources require permissions to the `eks:DescribeCluster` API operation. When using access entries, AWS Batch manages the access entry using your credentials, so you also need permissions to manage Amazon EKS access entries: `eks:DescribeAccessEntry`, `eks:CreateAccessEntry`, `eks:AssociateAccessPolicy`, and `eks:DeleteAccessEntry`. For more information, see [Required permissions](eks-access-entries.md#eks-access-entries-permissions).
+ **AWS account number** – You need to know your AWS account ID. Follow the directions in [Viewing your AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console-account-id.html).
+ **(Optional) CloudWatch** – To examine the details of [(Optional) Submit a job with overrides](#getting-started-eks-step-6), logging must be configured. For more information, see [Use CloudWatch Logs to monitor AWS Batch on Amazon EKS jobs](batch-eks-cloudwatch-logs.md).

## Step 1: Create your Amazon EKS cluster for AWS Batch
<a name="getting-started-eks-step-0"></a>

**Important**  
To get started as simply and quickly as possible, this tutorial includes steps with default settings. Before creating for production use, we recommend that you familiarize yourself with all settings and deploy with the settings that meet your requirements.

Once you have installed the prerequisites you need to create your cluster using `eksctl`. Creating the cluster can take between 10-15 minutes. 

```
$  eksctl create cluster --name {{my-cluster-name}} --region {{region-code}}
```

In the preceding command replace:
+ Replace {{my-cluster-name}} with the name you want to use for your cluster. 
+ Replace {{region-code}} with the AWS Region to create the cluster in, for example `us-west-2`.

The cluster name and region are needed for later in this tutorial.

## Step 2: Prepare your Amazon EKS cluster for AWS Batch
<a name="getting-started-eks-step-1"></a>

This method uses Amazon EKS access entries to grant AWS Batch cluster access. It eliminates the need for manual RBAC configuration and `aws-auth` ConfigMap edits.

1. 

**Create a dedicated namespace for AWS Batch jobs**

   Use `kubectl` to create a new namespace.

   ```
   $ namespace={{my-aws-batch-namespace}}
   ```

   ```
   $ cat - <<EOF | kubectl create -f -
   {
     "apiVersion": "v1",
     "kind": "Namespace",
     "metadata": {
       "name": "${namespace}",
       "labels": {
         "name": "${namespace}"
       }
     }
   }
   EOF
   ```

   Output:

   ```
   namespace/my-aws-batch-namespace created
   ```

1. 

**Configure cluster access for the node instance role**

   Instances launched by AWS Batch join the cluster using the instance profile that you specify in `computeResources.instanceRole` when you create the compute environment in the next step. That role needs its own access to the cluster, which is separate from the AWS Batch-managed access entry.

   The node instance role is created when you create the cluster. To find the node instance role, list all entities that use the `AmazonEKSWorkerNodePolicy` policy:

   ```
   $  aws iam list-entities-for-policy --policy-arn arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy
   ```

   The command lists every role that uses this policy. Choose the role whose name contains your cluster name, for example `eksctl-{{my-cluster-name}}-nodegroup-example`.

   This step is only needed if the node instance role doesn't already have an access entry on the cluster. For example, Amazon EKS typically creates an access entry for the node role of a managed node group, such as the one that `eksctl` created in Step 1. To check whether the role already has an access entry, run the following command:

   ```
   $ aws eks describe-access-entry \
       --cluster-name {{my-cluster-name}} \
       --principal-arn arn:aws:iam::{{your-account-number}}:role/{{eksctl-my-cluster-name-nodegroup-example}}
   ```

   Replace {{eksctl-my-cluster-name-nodegroup-example}} with the name of the node instance role that the previous command returned.

   If the command returns the access entry, skip the rest of this step. If it returns a `ResourceNotFoundException` error, create an access entry for the node instance role:

   ```
   $ aws eks create-access-entry \
       --cluster-name {{my-cluster-name}} \
       --principal-arn arn:aws:iam::{{your-account-number}}:role/{{eksctl-my-cluster-name-nodegroup-example}} \
       --type EC2_LINUX
   ```
**Note**  
On clusters whose `authenticationMode` is `API_AND_CONFIG_MAP`, if the node instance role is already mapped in the `aws-auth` ConfigMap, you can also skip this step. Nodes join successfully using the ConfigMap entry. On clusters whose `authenticationMode` is `API`, the ConfigMap isn't used, so the node instance role must have an access entry.
**Important**  
Without proper cluster access for the node instance role, EC2 instances cannot join the cluster. Jobs will remain in the `RUNNABLE` state because no capacity registers with the cluster.

## Step 3: Create an Amazon EKS compute environment
<a name="getting-started-eks-step-2"></a>

AWS Batch compute environments define compute resource parameters to meet your batch workload needs. In a managed compute environment, AWS Batch helps you to manage the capacity and instance types of the compute resources (Kubernetes nodes) within your Amazon EKS cluster. This is based on the compute resource specification that you define when you create the compute environment. You can use EC2 On-Demand Instances or EC2 Spot Instances.

Create a compute environment that targets your Amazon EKS cluster. Because the compute environment sets `accessEntry.desiredState` to `ENABLED`, AWS Batch creates an access entry for the **AWSServiceRoleForBatch** service-linked role on your cluster. You grant that access entry permissions in your namespace in the next step.
+ For `subnets` run `eksctl get cluster {{my-cluster-name}}` to get the subnets used by the cluster. 
+ For `securityGroupIds` parameter you can use the same security group as the Amazon EKS cluster. This command retrieves the security group ID for the cluster.

  ```
  $ aws eks describe-cluster \
      --name {{my-cluster-name}} \
      --query cluster.resourcesVpcConfig.clusterSecurityGroupId
  ```
+ The `instanceRole` is the instance profile for the node instance role that you found in Step 2. To find the `instanceRole` arn run the following command:

  ```
  $  aws iam list-instance-profiles-for-role --role-name eksctl-{{my-cluster-name}}-nodegroup-example        
  ```

  Output:

  ```
  INSTANCEPROFILES        arn:aws:iam::{{<your-account-number>}}:instance-profile/eks-04cb2200-94b9-c297-8dbe-87f12example
  ```

  For more information, see [Creating the Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html#create-worker-node-role) and [Grant IAM users access to Kubernetes with Amazon EKS access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) in the *Amazon EKS User Guide*. If you're using pod networking, see [Configuring the Amazon VPC CNI plugin for Kubernetes to use IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/cni-iam-role.html) in the **Amazon EKS User Guide**.

```
$ cat <<EOF > ./batch-eks-compute-environment.json
{
  "computeEnvironmentName": "{{My-Eks-CE1}}",
  "type": "MANAGED",
  "state": "ENABLED",
  "eksConfiguration": {
    "eksClusterArn": "arn:aws:eks:{{region-code}}:{{your-account-number}}:cluster/{{my-cluster-name}}",
    "kubernetesNamespace": "{{my-aws-batch-namespace}}",
    "accessEntry": {
      "desiredState": "ENABLED"
    }
  },
  "computeResources": {
    "type": "EC2",
    "allocationStrategy": "BEST_FIT_PROGRESSIVE",
    "minvCpus": 0,
    "maxvCpus": 128,
    "instanceTypes": [
        "m5"
    ],
    "subnets": [
        "{{<eks-cluster-subnets-with-access-to-internet-for-image-pull>}}"
    ],
    "securityGroupIds": [
        "{{<eks-cluster-sg>}}"
    ],
    "instanceRole": "{{<eks-instance-profile>}}"
  }
}
EOF
```

```
$ aws batch create-compute-environment --cli-input-json file://./batch-eks-compute-environment.json
```

**Notes**
+ Maintenance of an Amazon EKS compute environment is a shared responsibility. For more information, see [Shared responsibility of the Kubernetes nodes](eks-ce-shared-responsibility.md).

## Step 3a: Associate the namespace policy
<a name="getting-started-eks-step-2a"></a>

After creating the compute environment with `accessEntry.desiredState=ENABLED`, AWS Batch creates a cluster-level access entry. You must then associate the namespace-scoped `AWSBatchNamespacePolicy` to grant AWS Batch permission to create and manage pods in your namespace.

**Important**  
Without the namespace-scoped policy association, jobs will remain stuck in `RUNNABLE` status. The cluster-level policy alone does not grant pod management permissions.

1. 

**Wait for the access entry to become active**

   Check the access entry status:

   ```
   $ aws batch describe-compute-environments \
       --compute-environments {{My-Eks-CE1}} \
       --query 'computeEnvironments[0].eksConfiguration.accessEntry.status' \
       --output text
   ```

   Output when ready:

   ```
   ACTIVE
   ```

   An `ACTIVE` status means that AWS Batch created the access entry on your cluster and you can associate the namespace policy with it. If the status is `INACTIVE`, wait a moment and try again. Do not proceed until the status is `ACTIVE`.

1. 

**Associate the namespace policy**

   Once the access entry is `ACTIVE`, associate the namespace-scoped policy:

   ```
   $ aws eks associate-access-policy \
       --cluster-name {{my-cluster-name}} \
       --principal-arn arn:aws:iam::{{your-account-number}}:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch \
       --policy-arn arn:aws:eks::aws:cluster-access-policy/AWSBatchNamespacePolicy \
       --access-scope type=namespace,namespaces={{my-aws-batch-namespace}}
   ```

   Output:

   ```
   {
       "clusterName": "my-cluster-name",
       "principalArn": "arn:aws:iam::123456789012:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch",
       "associatedAccessPolicy": {
           "policyArn": "arn:aws:eks::aws:cluster-access-policy/AWSBatchNamespacePolicy",
           "accessScope": {
               "type": "namespace",
               "namespaces": [
                   "my-aws-batch-namespace"
               ]
           },
           "associatedAt": "2024-01-15T10:30:00.000000-08:00",
           "modifiedAt": "2024-01-15T10:30:00.000000-08:00"
       }
   }
   ```

## Step 4: Create a job queue and attach the compute environment
<a name="getting-started-eks-step-3"></a>

**Important**  
It's important to confirm that the compute environment is healthy before proceeding. The [DescribeComputeEnvironments](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeComputeEnvironments.html) API operation can be used to do this.  

```
$ aws batch describe-compute-environments --compute-environments {{My-Eks-CE1}}
```
Confirm that the `status` parameter is not `INVALID`. If it is, look at the `statusReason` parameter for the cause. For more information, see [Troubleshooting AWS Batch](troubleshooting.md).

Jobs submitted to this new job queue are run as pods on AWS Batch managed nodes that joined the Amazon EKS cluster that's associated with your compute environment.

```
$ cat <<EOF > ./batch-eks-job-queue.json
 {
    "jobQueueName": "{{My-Eks-JQ1}}",
    "priority": 10,
    "computeEnvironmentOrder": [
      {
        "order": 1,
        "computeEnvironment": "{{My-Eks-CE1}}"
      }
    ]
  }
EOF
```

```
$ aws batch create-job-queue --cli-input-json file://./batch-eks-job-queue.json
```

## Step 5: Create a job definition
<a name="getting-started-eks-step-4"></a>

The following Job definition instructs the pod to sleep for 60 seconds.

```
$ cat <<EOF > ./batch-eks-job-definition.json
{
  "jobDefinitionName": "{{MyJobOnEks_Sleep}}",
  "type": "container",
  "eksProperties": {
    "podProperties": {
      "hostNetwork": true,
      "containers": [
        {
          "image": "public.ecr.aws/amazonlinux/amazonlinux:2",
          "command": [
            "sleep",
            "60"
          ],
          "resources": {
            "limits": {
              "cpu": "1",
              "memory": "1024Mi"
            }
          }
        }
      ],
      "metadata": {
        "labels": {
          "environment": "{{test}}"
        }
      }
    }
  }
}
EOF
```

```
$ aws batch register-job-definition --cli-input-json file://./batch-eks-job-definition.json
```

**Notes**
+ There are considerations for the `cpu` and `memory` parameters. For more information, see [Memory and vCPU considerations for AWS Batch on Amazon EKS](memory-cpu-batch-eks.md).

## Step 6: Submit a job
<a name="getting-started-eks-step-5"></a>

Run the following AWS CLI command to submit a new Job.

```
$ aws batch submit-job --job-queue {{My-Eks-JQ1}} \
    --job-definition {{MyJobOnEks_Sleep}} --job-name {{My-Eks-Job1}}
```

To check the status of a Job:

```
$ aws batch describe-jobs --job {{<jobId-from-submit-response>}}
```

**Notes**
+ For more information about running jobs on Amazon EKS resources, see [Amazon EKS jobs](eks-jobs.md).

## Step 7: View the Job's output
<a name="getting-started-eks-step-7"></a>

To view the Job's output, do the following:

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. In the navigation pane choose **Jobs**. 

1. In the **Job queue** drop down choose the Job queue you created for the tutorial.

1. The **Jobs** table lists all of your Jobs and what their current status is. Once the Job's **Status** is **Succeeded** choose the **Name** of the Job, {{My-Eks-Job1}}, to view the Job's details. 

1. In the **Details** pane the **Started at** and **Stopped at** times should be one minute apart. 

## Step 8: (Optional) Submit a job with overrides
<a name="getting-started-eks-step-6"></a>

This job overrides the command passed to the container. AWS Batch aggressively cleans up the pods after the jobs complete to reduce the load to Kubernetes. To examine the details of a job, logging must be configured. For more information, see [Use CloudWatch Logs to monitor AWS Batch on Amazon EKS jobs](batch-eks-cloudwatch-logs.md).

```
$ cat <<EOF > ./submit-job-override.json
{
  "jobName": "{{EksWithOverrides}}",
  "jobQueue": "{{My-Eks-JQ1}}",
  "jobDefinition": "{{MyJobOnEks_Sleep}}",
  "eksPropertiesOverride": {
    "podProperties": {
      "containers": [
        {
          "command": [
            "/bin/sh"
          ],
          "args": [
            "-c",
            "echo hello world"
          ]
        }
      ]
    }
  }
}
EOF
```

```
$ aws batch submit-job --cli-input-json file://./submit-job-override.json
```

**Notes**
+ For improved visibility into the details of the operations, enable Amazon EKS control plane logging. For more information, see [Amazon EKS control plane logging](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) in the *Amazon EKS User Guide*.
+ Daemonsets and kubelets overhead affects available vCPU and memory resources, specifically scaling and job placement. For more information, see [Memory and vCPU considerations for AWS Batch on Amazon EKS](memory-cpu-batch-eks.md).

To view the Job's output, do the following:

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. In the navigation pane choose **Jobs**. 

1. In the **Job queue** drop down choose the Job queue you created for the tutorial.

1. The **Jobs** table lists all of your Jobs and what their current status is. Once the Job's **Status** is **Succeeded** choose the **Name** of the Job to view the Job's details. 

1. In the **Details** pane choose **Log stream name**. The CloudWatch console for the Job will open and there should be one event with the **Message** of `hello world` or your custom message.

## Step 9: Clean up your tutorial resources
<a name="getting-started-eks-step-8"></a>

You are charged for the Amazon EC2 instance while it is enabled. You can delete the instance to stop incurring charges.

To delete the resources you created, do the following:

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. In the navigation pane choose **Job queue**. 

1. In the **Job queue** table choose the Job queue you created for the tutorial.

1. Choose **Disable**. Once the Job queue **State** is Disabled you can choose **Delete**.

1. Once the Job queue is deleted, set `accessEntry.desiredState` to `DISABLED` on the compute environment so that AWS Batch removes the access entry that it created on your cluster:

   ```
   $ aws batch update-compute-environment \
       --compute-environment {{My-Eks-CE1}} \
       --eks-configuration 'accessEntry={desiredState=DISABLED}'
   ```
**Important**  
You must set `desiredState` to `DISABLED` before you delete the compute environment. Deleting a compute environment doesn't remove the access entry even if it's the last AWS Batch compute environment on the cluster. If other AWS Batch compute environments target the same cluster, AWS Batch removes the access entry only after every one of them has `desiredState` set to `DISABLED`. For more information, see [What AWS Batch creates on your cluster](eks-access-entries.md#eks-access-entries-what-batch-creates).
**Expected status after disabling the access entry**  
After AWS Batch removes the access entry, the compute environment's **Status** changes to `INVALID` with a status reason of `Unable to validate Kubernetes Namespace`. This is expected because AWS Batch no longer has access to your cluster. You can still disable and delete the compute environment.

1. In the navigation pane choose **Compute environments**.

1. Choose the compute environment you created for this tutorial and then choose **Disable**. It may take 1–2 minutes for the compute environment to complete being disabled.

1. Once the compute environment’s **State** is Disabled, choose **Delete**. It may take 1–2 minutes for the compute environment to be deleted.

## Additional resources
<a name="getting-started-eks-additional-resources"></a>

After you complete the tutorial, you might want to explore the following topics::
+ Learn more about the [Best practices](best-practices.md).
+ Explore the AWS Batch core components. For more information, see [Components of AWS Batch](batch_components.md).
+ Learn more about the different [Compute Environments](compute_environments.md) available in AWS Batch.
+ Learn more about [Job queues](job_queues.md) and their different scheduling options.
+ Learn more about [Job definitions](job_definitions.md) and the different configuration options.
+ Learn more about the different types of [Jobs](jobs.md).