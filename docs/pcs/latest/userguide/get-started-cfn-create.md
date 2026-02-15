# Use CloudFormation to create a sample AWS PCS cluster

The following procedure uses a
CloudFormation template in the AWS Management Console to create a sample AWS PCS cluster.
For more information about CloudFormation, see [What is CloudFormation?](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
in the _AWS CloudFormation User Guide_. For more information
about AWS PCS resource types in CloudFormation, see [AWS PCS resource type
reference](../../../AWSCloudFormation/latest/UserGuide/AWS_PCS.md "../../../AWSCloudFormation/latest/UserGuide/AWS_PCS.md") in the _AWS CloudFormation User Guide_.

###### To create the sample cluster

1. Choose the AWS Region to create the cluster in (the link opens the CloudFormation console with the template):
   - [US East (N. Virginia) (us-east-1)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml&param_ClientIpCidr=0.0.0.0%2F0 "https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml¶m_ClientIpCidr=0.0.0.0%2F0")
   - [US East (Ohio) (us-east-2)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml&param_ClientIpCidr=0.0.0.0%2F0 "https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml¶m_ClientIpCidr=0.0.0.0%2F0")
   - [US West (Oregon) (us-west-2)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml&param_ClientIpCidr=0.0.0.0%2F0 "https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml¶m_ClientIpCidr=0.0.0.0%2F0")
   - [Asia Pacific (Mumbai) (ap-south-1)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml&param_ClientIpCidr=0.0.0.0%2F0 "https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml¶m_ClientIpCidr=0.0.0.0%2F0")
   - [Asia Pacific (Singapore) (ap-southeast-1)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml&param_ClientIpCidr=0.0.0.0%2F0 "https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml¶m_ClientIpCidr=0.0.0.0%2F0")
   - [Asia Pacific (Sydney) (ap-southeast-2)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml&param_ClientIpCidr=0.0.0.0%2F0 "https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml¶m_ClientIpCidr=0.0.0.0%2F0")
   - [Asia Pacific (Tokyo) (ap-northeast-1)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml&param_ClientIpCidr=0.0.0.0%2F0 "https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml¶m_ClientIpCidr=0.0.0.0%2F0")
   - [Europe (Frankfurt) (eu-central-1)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml&param_ClientIpCidr=0.0.0.0%2F0 "https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml¶m_ClientIpCidr=0.0.0.0%2F0")
   - [Europe (Ireland) (eu-west-1)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml&param_ClientIpCidr=0.0.0.0%2F0 "https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml¶m_ClientIpCidr=0.0.0.0%2F0")
   - [Europe (London) (eu-west-2)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml&param_ClientIpCidr=0.0.0.0%2F0 "https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml¶m_ClientIpCidr=0.0.0.0%2F0")
   - [Europe (Paris) (eu-west-3)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml&param_ClientIpCidr=0.0.0.0%2F0 "https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml¶m_ClientIpCidr=0.0.0.0%2F0")
   - [Europe (Stockholm) (eu-north-1)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml&param_ClientIpCidr=0.0.0.0%2F0 "https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml¶m_ClientIpCidr=0.0.0.0%2F0")
   - [AWS GovCloud (US-East) (us-gov-east-1)](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-east-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml "https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-east-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml")
   - [AWS GovCloud (US-West) (us-gov-west-1)](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml "https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/create/review?stackName=get-started-cfn&templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/pcs/getting_started/assets/cluster.yaml")

2. Under **Provide a stack name**, enter a descriptive name.
   This is the name for your CloudFormation stack. The template uses this value
   as the name for your AWS PCS cluster.
3. Under **Parameters**:
   1. Under **SlurmVersion**, choose the version of
      Slurm you want your cluster to use.
   2. Under **NodeArchitecture**, choose
      **x86** to deploy a cluster that uses
      x86_64-compatible instances,
      or choose **Graviton** to use Arm64
      instances.
   3. For **KeyName**, choose an SSH key pair
      to access the cluster login nodes. Make sure that you have
      the PEM file for the key pair that you choose.
   4. For **ClientIpCidr**, enter an IP range
      in CIDR format to control access to the login nodes.

   ###### Warning

   The default value of `0.0.0.0/0` allows
   access from all IP addresses. 5. Leave the values for **HpcRecipesS3Bucket**
   and **HpcRecipesBranch** as
   their default values.

4. Under **Capabilities and transforms**:
   1. Select the checkbox to acknowledge that CloudFormation
      will create IAM resources.
   2. Select the checkbox to acknowledge that CloudFormation
      will create IAM resources with custom names.
   3. Select the checkbox to acknowledge `CAPABILITY_AUTO_EXPAND`
      for the new stack. For more information, see
      [CreateStack](../../../AWSCloudFormation/latest/APIReference/API_CreateStack.md#API_CreateStack_RequestParameters "../../../AWSCloudFormation/latest/APIReference/API_CreateStack.md#API_CreateStack_RequestParameters")
      in the _AWS CloudFormation API Reference_.

5. Choose **Create stack**.
6. Monitor the status of your stack.
   You can connect to the cluster after the status of
   the stack is `CREATE_COMPLETE`.
