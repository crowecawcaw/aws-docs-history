

# Troubleshooting
<a name="sagemaker-eks-operator-troubleshooting"></a>

See the following sections to learn how to troubleshoot error when using the training operator.

## I can't install the training operator
<a name="sagemaker-eks-operator-troubleshooting-installation-error"></a>

If you can't install the training operator, make sure that you're using the [ supported versions of components](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-operator.html#sagemaker-eks-operator-supported-versions). For example, if you get an error that your HyperPod AMI release is incompatible with the training operator, [ update to the latest version](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSoftware.html).

## Incompatible HyperPod task governance version
<a name="sagemaker-eks-operator-troubleshooting-task-governance-version"></a>

During installation, you might get an error message that the version of HyperPod task governance is incompatible. The training operator works only with version v1.3.0-eksbuild.1 or higher. Update your HyperPod task governance add-on and try again. 

## Missing permissions
<a name="sagemaker-eks-operator-troubleshooting-task-missing-permissions"></a>

 While you're setting up the training operator or running jobs, you might receive errors that you're not authorized to run certain operations, such as `DescribeClusterNode`. To resolve these errors, make sure you correctly set up IAM permissions while you're [setting up the Amazon EKS Pod Identity Agent](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-operator-install.html#sagemaker-eks-operator-install-pod-identity).