# `INVALID` compute environment

It's possible that you might have incorrectly configured a managed compute environment. If
you did, the compute environment enters an `INVALID` state and can't accept jobs for
placement. The following sections describe the possible causes and how to troubleshoot based on
the cause.

###### Important

AWS Batch creates and manages multiple AWS resources on your behalf and within your
account, including Amazon EC2 Launch Templates, Amazon EC2 Auto Scaling Groups, Amazon EC2 Spot Fleets, and Amazon ECS
Clusters. These managed resources are configured specifically to ensure optimal AWS Batch
operation. Manually modifying these Batch-managed resources, unless explicitly stated in AWS Batch
documentation, may result in unexpected behavior resulting in `INVALID` Compute Environment,
sub-optimal instance scaling behavior, delayed workload processing, or unexpected costs. These
manual modifications can not be deterministically supported by the AWS Batch service. Always use
the supported Batch APIs or the Batch console to manage your Compute Environments.

## Incorrect role name or ARN

The most common cause for a compute environment to enter an `INVALID` state is
that the AWS Batch service role or the Amazon EC2 Spot Fleet role has an incorrect name or Amazon
Resource Name (ARN). This is more common with compute environments that are created using the
AWS CLI or the AWS SDKs. When you create a compute environment in the AWS Management Console, AWS Batch helps
you choose the correct service or Spot Fleet roles. However, suppose that you manually enter
the name or the ARN and enter them incorrectly. Then, the resulting compute environment is also
`INVALID`.

However, suppose that you manually enter the name or ARN for an IAM resource in an AWS CLI
command or your SDK code. In this case, AWS Batch can't validate the string. Instead, AWS Batch
must accept the bad value and attempt to create the environment. If AWS Batch fails to create the
environment, the environment moves to an `INVALID` state, and you see the following
errors.

For an invalid service role:

`CLIENT_ERROR - Not authorized to perform sts:AssumeRole (Service:
 AWSSecurityTokenService; Status Code: 403; Error Code: AccessDenied; Request ID:
 dc0e2d28-2e99-11e7-b372-7fcc6fb65fe7)`

For an invalid Spot Fleet role:

`CLIENT_ERROR - Parameter: SpotFleetRequestConfig.IamFleetRole is invalid. (Service:
 AmazonEC2; Status Code: 400; Error Code: InvalidSpotFleetRequestConfig; Request ID:
 331205f0-5ae3-4cea-bac4-897769639f8d) Parameter: SpotFleetRequestConfig.IamFleetRole is
 invalid`

One common cause for this issue is the following scenario. You only specify the name of an
IAM role when using the AWS CLI or the AWS SDKs, instead of the full Amazon Resource Name
(ARN). Depending on how you created the role, the ARN might contain a
`aws-service-role` path prefix. For example, if you manually create the AWS Batch
service role using the procedures in [Using service-linked roles for
AWS Batch](using-service-linked-roles.md "using-service-linked-roles.md"), your service role ARN might look like the
following.

```
arn:aws:iam::`123456789012`:role/AWSBatchServiceRole
```

However, if you created the service role as part of the console first run wizard today,
your service role ARN might look like the following.

```
arn:aws:iam::`123456789012`:role/aws-service-role/AWSBatchServiceRole
```

This issue can also occur if you attach the AWS Batch service-level policy
(`AWSBatchServiceRole`) to a non-service role. For example, you may receive an
error message that resembles the following in this scenario:

```
CLIENT_ERROR - User: arn:aws:sts::`account_number`:assumed-role/batch-replacement-role/aws-batch is not
   authorized to perform: `action` on resource ...
```

To resolve this issue, do one of the following.

- Use an empty string for the service role when you create the AWS Batch compute
  environment.
- Specify the service role in the following format:
  `arn:aws:iam::`account_number`:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch`.

When you only specify the name of an IAM role when using the AWS CLI or the AWS SDKs,
AWS Batch assumes that your ARN doesn't use the `aws-service-role` path prefix.
Because of this, we recommend that you specify the full ARN for your IAM roles when you
create compute environments.

To repair a compute environment that's misconfigured this way, see [Repair an INVALID compute
environment](#repairing_invalid_compute_environment "#repairing_invalid_compute_environment").

## Repair an `INVALID` compute

environment

When you have a compute environment in an `INVALID` state, update it to repair
the invalid parameter. For an [Incorrect role name or ARN](#invalid_service_role_arn "#invalid_service_role_arn"), update the compute environment using the correct service
role.

###### To repair a misconfigured compute environment

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. From the navigation bar, select the AWS Region to use.
3. In the navigation pane, choose **Compute environments**.
4. On the **Compute environments** page, select the radio button next to
   the compute environment to edit, and then choose **Edit**.
5. On the **Update compute environment** page, for **Service
   role**, choose the IAM role to use with your compute environment. The AWS Batch
   console only displays roles that have the correct trust relationship for compute
   environments.

###### Tip

For directions on how to create a service linked role, see [Using roles for AWS Batch](using-service-linked-roles-batch-general.md "using-service-linked-roles-batch-general.md"). 6. Choose **Save** to update your compute environment.
