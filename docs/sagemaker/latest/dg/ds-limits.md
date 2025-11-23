# Limits

Spaces run as pods on HyperPod EKS nodes with attached EBS volumes. The number of
Spaces that can be deployed per node is constrained by AWS infrastructure limits.

**EBS Volume Limits per Node**

Reference: [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html](../../../AWSEC2/latest/UserGuide/volume_limits.md "../../../AWSEC2/latest/UserGuide/volume_limits.md")

EC2 nodes have a maximum number of EBS volumes that can be attached. Since each Space
typically uses one EBS volume, this limits how many Spaces with dedicated EBS storage
can run on a single node.

**Maximum Pods per HyperPod Node**

Reference: [https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-prerequisites.html](sagemaker-hyperpod-eks-prerequisites.md "sagemaker-hyperpod-eks-prerequisites.md")

Each HyperPod instance type supports a maximum number of pods based on available IP
addresses from the VPC CNI plugin. Since each Space runs as a pod, this directly caps
the number of Spaces per node.

**Impact**

The effective limit for Spaces per node is whichever constraint is reached first.
