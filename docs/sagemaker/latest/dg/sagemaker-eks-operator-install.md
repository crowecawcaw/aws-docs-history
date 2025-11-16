# Installing the training operator

See the following sections to learn about how to install the training operator.

## Prerequisites

Before you use the HyperPod training operator, you must have completed the following prerequisites:

- [Created a HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md "sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md").
- Installed the latest AMI on your HyperPod cluster. For more information, see [SageMaker HyperPod AMI releases for
  Amazon EKS](sagemaker-hyperpod-release-ami-eks.md "sagemaker-hyperpod-release-ami-eks.md").
- [Installed cert-manager](https://cert-manager.io/docs/installation/ "https://cert-manager.io/docs/installation/").
- [Set up the EKS Pod Identity Agent using the console](../../../eks/latest/userguide/pod-id-agent-setup.md "../../../eks/latest/userguide/pod-id-agent-setup.md"). If you want to use the AWS CLI,
  use the following command:

```
aws eks create-addon \
 --cluster-name `my-eks-cluster` \
 --addon-name eks-pod-identity-agent \
 --region `AWS Region`
```

- (Optional) If you run your HyperPod cluster nodes in a private VPC, you must set up PrivateLinks VPC endpoints
  for the Amazon SageMaker AI API (`com.amazonaws.`aws-region`.sagemaker.api`) and Amazon EKS Auth services (com.amazonaws.`aws-region`.eks-auth).
  You must also make sure that your cluster nodes are running
  with subnets that are in a security group that allows the traffic to route through
  the VPC endpoints to communicate with SageMaker AI and Amazon EKS. If these aren't properly set up, the add-on installation can fail. To learn more
  about setting up VPC endpoints, see [Create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws").

## Installing the training operator

You can now install the HyperPod training operator through the SageMaker AI console, the Amazon EKS console, or with the AWS CLI
The console methods offer simplified experiences that help you install the operator.
The AWS CLI offers a programmatic approach that lets you customize more of your installation.

Between the two console experiences, SageMaker AI provides a one-click installation creates the IAM execution role,
creates the pod identity association, and installs the operator. The Amazon EKS console installation is similar, but
this method doesn't automatically create the IAM execution role. During this process, you can
choose to create a new IAM execution role with information that the console pre-populates. By default,
these created roles only have access to the current cluster that you're installing the operator in. Unless you edit
the role's permissions to include other clusters, if you remove and reinstall the operator, you must create
a new role.

SageMaker AI console (recommended)

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Go to your cluster's details page.
3. On the **Dashboard** tab, locate the add-on named
   **Amazon SageMaker HyperPod training operator**, and choose **install**.
   During the installation process, SageMaker AI
   creates an IAM execution role with permissions similar to the
   [AmazonSageMakerHyperPodTrainingOperatorAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerHyperPodTrainingOperatorAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerHyperPodTrainingOperatorAccess.md") managed policy and creates a pod identity
   association between your Amazon EKS cluster and your new execution role.

Amazon EKS console

###### Note

If you install the add-on through the Amazon EKS cluster, first make sure that you've tagged
your HyperPod cluster with the key-value pair `SageMaker:true`. Otherwise,
the installation will fail.

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Go to your EKS cluster, choose **Add-ons**, then choose **Get more Add-ons**.
3. Choose Amazon SageMaker HyperPod training operator, then choose **Next**.
4. Under **Version**, the console defaults to the latest version, which we recommend
   that you use.
5. Under **Add-on access**, choose a pod identity IAM role to use with the
   training operator add-on. If you don't already have a role, choose
   **Create recommended role** to create one.
6. During this role creation process, the IAM console pre-populates all of the necessary
   information, such as the use case, the [AmazonSageMakerHyperPodTrainingOperatorAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerHyperPodTrainingOperatorAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerHyperPodTrainingOperatorAccess.md") managed policy and other
   required permissions, the role name, and the description. As you go through the steps,
   review the information, and choose **Create role**.
7. In the EKS console, review your add-on's settings, and then choose **Create**.

CLI

1. Make sure that the IAM execution role for your HyperPod cluster has a trust relationship that
   allows EKS Pod Identity to assume the role or
   or [create a new IAM role](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md")
   with the following trust policy. Alternatively, you could use the Amazon EKS console
   to install the add-on, which creates a recommended role.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowEksAuthToAssumeRoleForPodIdentity",
 "Effect": "Allow",
 "Principal": {
 "Service": "pods.eks.amazonaws.com"
 },
 "Action": [
 "sts:AssumeRole",
 "sts:TagSession",
 "eks-auth:AssumeRoleForPodIdentity"
 ]
 }
 ]
}`

```

2. Attach the [AmazonSageMakerHyperPodTrainingOperatorAccess managed policy](../../../aws-managed-policy/latest/reference/AmazonSageMakerHyperPodTrainingOperatorAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerHyperPodTrainingOperatorAccess.md") to your created role.
3. [Then create a pod identity association between your EKS cluster, your IAM role, and your new IAM role](../../../eks/latest/userguide/pod-identities.md "../../../eks/latest/userguide/pod-identities.md").

```
aws eks create-pod-identity-association \
--cluster-name `my-eks-cluster` \
--role-arn `ARN of your execution role` \
--namespace aws-hyperpod \
--service-account hp-training-operator-controller-manager \
--region `AWS Region`
```

4. After you finish the process, you can use the ListPodIdentityAssociations operation to see
   the association you created. The following is a sample response of what it might look like.

```
aws eks list-pod-identity-associations --cluster-name my-eks-cluster
{
    "associations": [{
        "clusterName": "`my-eks-cluster`",
        "namespace": "aws-hyperpod",
        "serviceAccount": "hp-training-operator-controller-manager",
        "associationArn": "arn:aws:eks:us-east-2:123456789012:podidentityassociation/my-hyperpod-cluster/a-1a2b3c4d5e6f7g8h9",
        "associationId": "`a-1a2b3c4d5e6f7g8h9`"
    }]
}
```

5. To install the training operator, use the `create-addon` operation.
   The `--addon-version` parameter is optional. If you don’t provide one, the default is the latest version.
   To get the possible versions, use the [DescribeAddonVersions](../../../eks/latest/APIReference/API_DescribeAddonVersions.md "../../../eks/latest/APIReference/API_DescribeAddonVersions.md") operation.

```
aws eks create-addon \
  --cluster-name my-eks-cluster \
  --addon-name amazon-sagemaker-hyperpod-training-operator \
  --resolve-conflicts OVERWRITE
```

The training operator comes with a number of options with default values that might fit your use case.
We recommend that you try out the training operator with default values before changing them.
The table below describes all parameters and examples of when you might want to configure each parameter.

| Parameter                                                     | Description                                        | Default                                                                                               |
| ------------------------------------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| hpTrainingControllerManager.manager.resources.requests.cpu    | How many processors to allocate for the controller | 1                                                                                                     |
| hpTrainingControllerManager.manager.resources.requests.memory | How much memory to allocate to the controller      | 2Gi                                                                                                   |
| hpTrainingControllerManager.manager.resources.limits.cpu      | The CPU limit for the controller                   | 2                                                                                                     |
| hpTrainingControllerManager.manager.resources.limits.memory   | The memory limit for the controller                | 4Gi                                                                                                   |
| hpTrainingControllerManager.nodeSelector                      | Node selector for the controller pods              | Default behavior is to select nodes with the label `sagemaker.amazonaws.com/compute-type: "HyperPod"` |

## HyperPod elastic agent

The HyperPod elastic agent is an extension of [PyTorch’s ElasticAgent](https://docs.pytorch.org/docs/stable/elastic/agent.html "https://docs.pytorch.org/docs/stable/elastic/agent.html"). It orchestrates
lifecycles of training workers on each container and communicates with the HyperPod training operator.
To use the HyperPod training operator, you must first install the HyperPod elastic agent into your training image
before you can submit and run jobs using the operator. The following is a docker file that installs elastic agent and uses
`hyperpodrun` to create the job launcher.

```
RUN pip install hyperpod-elastic-agent

ENTRYPOINT ["entrypoint.sh"]
# entrypoint.sh
...
hyperpodrun --nnodes=`node_count` --nproc-per-node=`proc_count` \
            --rdzv-backend hyperpod \ # Optional
            ... # Other torchrun args
            # pre-traing arg_group
            --pre-train-script pre.sh --pre-train-args "pre_1 pre_2 pre_3" \
            # post-train arg_group
            --post-train-script post.sh --post-train-args "post_1 post_2 post_3" \
            `training.py` --script-args
```

You can now submit jobs with `kubectl`.

### HyperPod elastic agent arguments

The HyperPod elastic agent supports all of the original arguments and adds some additional arguments.
The following is all of the arguments available in the HyperPod elastic agent. For more information about
PyTorch's Elastic Agent, see their [official documentation](https://docs.pytorch.org/docs/stable/elastic/agent.html "https://docs.pytorch.org/docs/stable/elastic/agent.html").

| Argument                  | Description                                                 | Default Value |
| ------------------------- | ----------------------------------------------------------- | ------------- |
| --shutdown-signal         | Signal to send to workers for shutdown (SIGTERM or SIGKILL) | "SIGKILL"     |
| --shutdown-timeout        | Timeout in seconds between SIGTERM and SIGKILL signals      | 30            |
| --server-host             | Agent server address                                        | "0.0.0.0"     |
| --server-port             | Agent server port                                           | 8080          |
| --server-log-level        | Agent server log level                                      | "info"        |
| --server-shutdown-timeout | Server shutdown timeout in seconds                          | 300           |
| --pre-train-script        | Path to pre-training script                                 | None          |
| --pre-train-args          | Arguments for pre-training script                           | None          |
| --post-train-script       | Path to post-training script                                | None          |
| --post-train-args         | Arguments for post-training script                          | None          |

## Task governance (optional)

The training operator is integrated with [HyperPod task governance](sagemaker-hyperpod-eks-operate-console-ui-governance.md "sagemaker-hyperpod-eks-operate-console-ui-governance.md"), a robust management system designed to streamline resource allocation and ensure efficient
utilization of compute resources across teams and projects for your Amazon EKS clusters. To set up HyperPod task governance,
see [Setup for
SageMaker HyperPod task governance](sagemaker-hyperpod-eks-operate-console-ui-governance-setup.md "sagemaker-hyperpod-eks-operate-console-ui-governance-setup.md").

###### Note

When installing the HyperPod task governance add-on, you must
use version v1.3.0-eksbuild.1 or higher.

When submitting a job, make sure you include your queue name and priority class labels of
`hyperpod-ns-`team-name`-localqueue` and ``priority-class`-name-priority`. For example, if you're using Kueue,
your labels become the following:

- kueue.x-k8s.io/queue-name: hyperpod-ns-`team-name`-localqueue
- kueue.x-k8s.io/priority-class: `priority-class`-name-priority

The following is an example of what your configuration file might look like:

```
apiVersion: sagemaker.amazonaws.com/v1
kind: HyperPodPytorchJob
metadata:
  name: hp-task-governance-sample
  namespace: hyperpod-ns-`team-name`
  labels:
    kueue.x-k8s.io/queue-name: hyperpod-ns-`team-name`-localqueue
    kueue.x-k8s.io/priority-class: `priority-class`-priority
spec:
  nprocPerNode: "1"
  runPolicy:
    cleanPodPolicy: "None"
  replicaSpecs:
    - name: pods
      replicas: 4
      spares: 2
      template:
        spec:
          containers:
            - name: ptjob
              image: XXXX
              imagePullPolicy: Always
              ports:
                - containerPort: 8080
              resources:
                requests:
                  cpu: "2"
```

Then use the following kubectl command to apply the YAML file.

```
kubectl apply -f task-governance-job.yaml
```

## Kueue (optional)

While you can run jobs directly, your organization can also integrate the training operator
with Kueue to allocate resources and schedule jobs.
Follow the steps below to install Kueue into your HyperPod cluster.

1. Follow the installation guide in the [official Kueue documentation](https://kueue.sigs.k8s.io/docs/installation/#install-a-custom-configured-released-version "https://kueue.sigs.k8s.io/docs/installation/#install-a-custom-configured-released-version"). When you reach the
   step of configuring `controller_manager_config.yaml`, add the following configuration:

```
externalFrameworks:
- "HyperPodPytorchJob.v1.sagemaker.amazonaws.com"
```

2. Follow the rest of the steps in the official installation guide. After you finish installing Kueue,
   you can create some sample queues with the `kubectl apply -f sample-queues.yaml` command.
   Use the following YAML file.

```
apiVersion: kueue.x-k8s.io/v1beta1
kind: ClusterQueue
metadata:
  name: cluster-queue
spec:
  namespaceSelector: {}
  preemption:
    withinClusterQueue: LowerPriority
  resourceGroups:
  - coveredResources:
    - cpu
    - nvidia.com/gpu
    - pods
    flavors:
    - name: default-flavor
      resources:
      - name: cpu
        nominalQuota: 16
      - name: nvidia.com/gpu
        nominalQuota: 16
      - name: pods
        nominalQuota: 16
---
apiVersion: kueue.x-k8s.io/v1beta1
kind: LocalQueue
metadata:
  name: user-queue
  namespace: default
spec:
  clusterQueue: cluster-queue
---
apiVersion: kueue.x-k8s.io/v1beta1
kind: ResourceFlavor
metadata:
  name: default-flavor
---
apiVersion: kueue.x-k8s.io/v1beta1
description: High priority
kind: WorkloadPriorityClass
metadata:
  name: high-priority-class
value: 1000
---
apiVersion: kueue.x-k8s.io/v1beta1
description: Low Priority
kind: WorkloadPriorityClass
metadata:
  name: low-priority-class
value: 500
```
