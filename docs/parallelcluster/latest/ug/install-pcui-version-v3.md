

# Identify the AWS ParallelCluster and PCUI version
<a name="install-pcui-version-v3"></a>

**To identify the AWS ParallelCluster and PCUI version:**

1. In the CloudFormation console, select a PCUI stack.

1. Select the **Parameters** tab.

1. The AWS ParallelCluster version is the value of the parameter **Version**.

1. The PCUI version is at the end of the **PublicEcrImageUri** value. For example, if the value is `public.ecr.aws/pcui/parallelcluster-ui-awslambda:2023.02`, then the version is `2023.02`.

**Note**  
To update the PCUI to the latest AWS ParallelCluster version, launch a new stack by choosing a [quick-create link](install-pcui-v3.md#install-pcui-steps-v3).