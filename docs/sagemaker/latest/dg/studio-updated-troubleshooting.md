# Troubleshooting

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the updated Studio
experience. For information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md "studio.md").

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

This section shows how to troubleshoot common problems in Amazon SageMaker Studio.

## Recovery mode

Recovery mode allows you to access your Studio application when a configuration
issue prevents your normal start up. It provides a simplified environment with essential
functionality to help you diagnose and fix the issue.

When an application fails to launch, you may see an error message about accessing
recovery mode to address one of the following configuration issues.

- Corrupted [`.condarc`](https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html "https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html") file.

For information on troubleshooting your `.condarc` file, see the
[troubleshooting](https://docs.conda.io/projects/conda/en/latest/user-guide/troubleshooting.html "https://docs.conda.io/projects/conda/en/latest/user-guide/troubleshooting.html") page in the _Conda user
guide_.

- Insufficient storage volume available.

You can increase the Amazon EBS space storage available for the application or
enter recovery mode to remove unnecessary data.

For information on increasing the Amazon EBS volume size, see [request a
quota size](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas Developer
Guide_.

In recovery mode:

- Your home directory will differ from your normal start up. This directory is
  temporary and ensures that any corrupted configurations in your standard home
  directory does not impact your recovery mode operations. You can navigate to
  your standard home directory by using the command `cd
/home/sagemaker-user`.
  - Standard mode: `/home/sagemaker-user`
  - Recovery mode: `/tmp/sagemaker-recovery-mode-home`

- The conda environment uses a minimal base conda environment with essential
  packages only. The simplified conda setup helps isolate environment-related
  issues and provides basic functionality for troubleshooting.

You can use the Studio UI or the AWS CLI to access the application in recovery
mode.

The following provides instructions on accessing your application in recovery
mode.

1. If you have not already done so, launch the Studio UI by
   following the instructions in [Launch from the Amazon SageMaker AI console](studio-updated-launch.md#studio-updated-launch-console "studio-updated-launch.md#studio-updated-launch-console").
2. In the left navigation menu, under **Applications**,
   choose the application.
3. Choose the space you are having configuration issues with.

The following steps become available to you when you have one one or
more of the configuration issues mentioned previously. In this case, you
will see a warning banner and **Recovery mode**
message.

###### Note

The warning banner should have a recommended solution for the
issue. Take note of it before proceeding. 4. Choose **Run space (Recovery mode)**. 5. To access your application in recovery mode, choose **Open
`application` (Recovery
mode)**.
To access your application in recovery mode, you must append
`--recovery-mode` to your [create-app](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-app.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-app.html") AWS CLI command. The following provides an example on how
to access your application in recovery mode.

For the following example, you will need your:

- `domain-id`

To obtain your domain details, see [View domains](domain-view.md "domain-view.md").

- `space-name`

To obtain the space names associated with your domain, see [Use the AWS CLI to view the
SageMaker AI spaces in your domain](sm-console-domain-resources-view.md#sm-console-domain-resources-view-spaces-cli "sm-console-domain-resources-view.md#sm-console-domain-resources-view-spaces-cli").

- `app-name`

The name of your application. To view your applications, see [Use the AWS CLI to view the
SageMaker AI applications in your domain](sm-console-domain-resources-view.md#sm-console-domain-resources-view-apps-cli "sm-console-domain-resources-view.md#sm-console-domain-resources-view-apps-cli").

Access Code Editor application in recovery mode

```
aws sagemaker create-app \
    --app-name `app-name` \
    --app-type CodeEditor \
    --domain-id `domain-id` \
    --space-name `space-name` \
    --recovery-mode
```

Access JupyterLab application in recovery mode

```
aws sagemaker create-app \
    --app-name `app-name` \
    --app-type JupyterLab \
    --domain-id `domain-id` \
    --space-name `space-name` \
    --recovery-mode
```

## Cannot delete

the Code Editor or JupyterLab application

This issue occurs when a user creates an application from Amazon SageMaker Studio, that is
only available in Studio, then reverts their default experience to Studio Classic. As a
result, the user cannot delete an application for Code Editor, based on Code-OSS, Visual Studio Code - Open Source or JupyterLab, because
they can't access the Studio UI.

To resolve this issue, notify your administrator so that they can delete the
application manually using the AWS Command Line Interface (AWS CLI).

## EC2InsufficientCapacityError

This issue occurs when you try to run a space and AWS does not currently have enough
available on-demand capacity to fulfill your request.

To resolve this issue, complete the following.

- Wait a few minutes, then resubmit your request. Capacity can shift
  frequently.
- Run the space with an alternate instance size or type.

###### Note

Capacity is available in different Availability Zones. To maximize capacity
availability for users, we recommend setting up subnets in all Availability Zones.
Studio retries all available Availability Zones for the domain.

Instance type availability differs between regions. For a list of supported
instances types per Region, see [Amazon SageMaker AI pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/"))

The following table lists instance families and their recommended alternatives.

| Instance family | CPU Type                                      | vCPUs    | Memory (GiB) | GPU type                | GPUs   | GPU Memory (GiB)                 | Recommended alternative |
| --------------- | --------------------------------------------- | -------- | ------------ | ----------------------- | ------ | -------------------------------- | ----------------------- |
| G4dn            | 2nd Generation Intel Xeon Scalable Processors | 4 to 96  | 16 to 384    | NVIDIA T4 Tensor Core   | 1 to 8 | 16 per GPU                       | G6                      |
| G5              | 2nd generation AMD EPYC processors            | 4 to 192 | 16 to 768    | NVIDIA A10G Tensor core | 1 to 8 | 24 per GPU                       | G6e                     |
| G6              | 3rd generation AMD EPYC processors            | 4 to 192 | 16 to 768    | NVIDIA L4 Tensor Core   | 1 to 8 | 24 per GPU                       | G4dn                    |
| G6e             | 3rd generation AMD EPYC processors            | 4 to 192 | 32 to 1536   | NVIDIA L40S Tensor Core | 1 to 8 | 48 per GPU                       | G5, P4                  |
| P3              | Intel Xeon Scalable Processors                | 8 to 96  | 61 to 768    | NVIDIA Tesla V100       | 1 to 8 | 16 per GPU (32 per GPU for P3dn) | G6e, P4                 |
| P4              | 2nd Generation Intel Xeon Scalable processors | 96       | 1152         | NVIDIA A100 Tensor Core | 8      | 320 (640 for P4de)               | G6e                     |
| P5              | 3rd Gen AMD EPYC processors                   | 192      | 2000         | NVIDIA H100 Tensor Core | 8      | 640                              | P4de                    |

## Insufficient limit

(quota increase required)

This issue occurs when you get the following error message while attempting to run a
space.

```
Error when creating application for space: ... : The account-level service limit is X Apps, with current utilization Y Apps and a request delta of 1 Apps. Please use Service Quotas to request an increase for this quota.
```

There is a default limit on the number of instances, for each instance type, that you
can run in each AWS Region. This error means that you have reached that limit.

To resolve this issue, request an instance limit increase for the AWS Region that
you are launching the space in. For more information, see [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md").

## Failure to load custom

image

This issue occurs when a SageMaker AI image is deleted before detaching the image from your
domain. This can be seen when you view the **Environment** tab for
your domain.

To resolve this issue, you will need to create a temporary new image with the same
name as the deleted one, detach the image, then delete the temporary image. Use the
following instructions for a walk through.

1. If you have not already done so, launch the [SageMaker AI console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker").
2. In the left navigation menu, under **Admin configurations**,
   choose **Domains**.
3. Choose your domain.
4. Choose the **Environment** tab. You will see the error
   message on this page.
5. Copy your image name from the image ARN.
6. In the left navigation menu, under **Admin configurations**,
   choose **Images**.
7. Choose **Create image**.
8. Follow the steps in the procedure, but ensure that your image name is the same
   as the image name from above.

If you do not have an image in a Amazon ECR directory, see the instructions in
[Create a custom image and push to
Amazon ECR](studio-updated-byoi-how-to-prepare-image.md "studio-updated-byoi-how-to-prepare-image.md"). 9. Once you have created your SageMaker AI image, navigate back to your domain
**Environment** tab. You will see the image attached to
your domain. 10. Select the image and choose **Detach**. 11. Follow the instructions to detach and delete the temporary SageMaker AI image.
