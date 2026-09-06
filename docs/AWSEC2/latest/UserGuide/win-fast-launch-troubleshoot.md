

# Troubleshoot Windows EC2 Fast Launch
<a name="win-fast-launch-troubleshoot"></a>

## Troubleshooting scenarios
<a name="ts-fast-launch-scenarios"></a>

The following scenarios can help you diagnose and fix common issues that you might encounter when you try to enable EC2 Fast Launch.

### Unable to stop instance for snapshot creation
<a name="ts-fast-launch-sc-stop-instance"></a>

#### Description
<a name="ts-fast-launch-sc-stop-instance-descr"></a>

When you enable EC2 Fast Launch, the service launches a set of instances that are used to create the pre-provisioned snapshots. Each instance is given 30 minutes to complete the process. If any of the instances complete successfully, then the service sets the Fast Launch status for the AMI to `Enabled`. However, if an instance fails to complete the process in the allotted time, and none of the other instances have completed the process, the service terminates all of the instances and sets the Fast Launch status for the AMI to `enabling_failed` and the Fast Launch status reason to the following:

```
Unable to stop instance ID={{i-1234567890abcdef0}} for snapshot creation.
```

#### Cause
<a name="ts-fast-launch-sc-stop-instance-cause"></a>

Most often, this is caused by trying to enable EC2 Fast Launch for a Windows AMI that was created from a running instance, or an AMI that doesn't meet all of the [EC2 Fast Launch prerequisites](win-start-fast-launch-prereqs.md).

#### Solution
<a name="ts-fast-launch-sc-stop-instance-solution"></a>

Ensure that the AMI you use meets all [EC2 Fast Launch prerequisites](win-start-fast-launch-prereqs.md).

To configure EC2 Fast Launch for an AMI, you must create the AMI using **Sysprep** with the shutdown option. For more information, see [Create an Amazon EC2 AMI using Windows Sysprep](ami-create-win-sysprep.md).

### You've reached your VPC limit
<a name="ts-fast-launch-sc-vpc-limit"></a>

#### Description
<a name="ts-fast-launch-sc-vpc-limit-descr"></a>

If you don't use a launch template to specify an existing VPC, and don't have a default VPC defined for your account, the service automatically creates an CloudFormation stack that includes a VPC and other resources, as described in [EC2 Fast Launch prerequisites](win-start-fast-launch-prereqs.md).

#### Cause
<a name="ts-fast-launch-sc-vpc-limit-cause"></a>

You've reached the maximum number of VPCs that are allowed in your AWS account for the Region, and you have not specified an existing VPC for EC2 Fast Launch to use. This causes the process to fail.

#### Solution
<a name="ts-fast-launch-sc-vpc-limit-solution"></a>

You can address this issue with either of the following options:
+ You can request a quota increase
+ You can provide a launch template that specifies an existing VPC

To request an increase to the number of VPCs that your account can define per Region, follow these steps:

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the **Service Console Dashboard**, choose **Amazon Virtual Private Cloud (Amazon VPC)**. This opens the VPC service quotas.

1. Filter on `VPCs per Region` to go directly to the quota.

1. Select **VPCs per Region**, and choose **Request increase at account level**.

 If you have an urgent quota request, or if your quota increase request is denied, contact Support for assistance. For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

### Insufficient permissions to enable EC2 Fast Launch
<a name="ts-fast-launch-sc-insufficient-perms"></a>

#### Description
<a name="ts-fast-launch-sc-insufficient-perms-descr"></a>

When you enable EC2 Fast Launch for the first time without specifying a Launch Template, EC2 Fast Launch creates a service-owned CloudFormation stack with service default resources. However, the CloudFormation templates will fail to deploy if your IAM principal (role or user) lacks the necessary permissions.

The log message might look something like the following:

```
Can't enable EC2 Fast Launch. The IAM credentials that you are using do not have sufficient permissions. Attach EC2FastLaunchFullAccess in the IAM console.
```

#### Cause
<a name="ts-fast-launch-sc-insufficient-perms-cause"></a>

Your IAM user or role lacks the necessary permissions to enable EC2 Fast Launch.

#### Solution
<a name="ts-fast-launch-sc-insufficient-perms-solution"></a>

Verify that your IAM principal (user or role) that enables EC2 Fast Launch has the `EC2FastLaunchFullAccess` policy attached. This AWS managed policy grants full access to all EC2 Fast Launch resources. To view the permissions for this policy, see the [EC2FastLaunchFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/EC2FastLaunchFullAccess.html) policy in the *AWS Managed Policy Reference*.