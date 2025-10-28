# Build a custom AMI

The following page explains how to build a custom Amazon Machine Image (AMI) using Amazon SageMaker HyperPod
base AMIs. You begin by selecting a base AMI, and then you create your own customized AMI using any of the common methods
for creating new images, such as the AWS CLI.

## Select a SageMaker HyperPod base

AMI

You can select a SageMaker HyperPod base AMI through one of the following
methods.

### AWS console

selection

You can select public SageMaker HyperPod AMIs through the AWS console or by
using the `DescribeImages` API call. SageMaker HyperPod AMIs are public
and visible in every AWS account. You can find them in the Amazon EC2 AMI
catalog by applying a filter to search for public AMIs owned by Amazon.

To find SageMaker HyperPod AMIs in the console:

1. Sign in to the Amazon EC2 console.
2. In the left navigation pane, choose **AMIs**.
3. For the **Image type** dropdown,
   select **Public images**.
4. In the search bar filters, set the **Owner alias** filter to
   `amazon`.
5. Search for AMIs prefixed as **HyperPod
   EKS** and select the AMI (preferably latest) that works
   for your use case. For instance, you can choose an AMI between
   Kubernetes 1.31 versus Kubernetes 1.30.

### Fetch latest public AMI ID

through the AWS CLI

If you want to always use the latest release public AMI, it is more
efficient to use the public SageMaker HyperPod SSM parameter that contains the
value of the latest AMI ID released by SageMaker HyperPod.

The following example shows how to retrieve the latest AMI ID using the
AWS CLI:

```
aws ssm get-parameter \
  --name "/aws/service/sagemaker-hyperpod/ami/x86_64/eks-1.31-amazon-linux-2/latest/ami-id" \
  --region `us-east-1` \
  --query "Parameter.Value" \
  --output text
```

###### Note

Replace the parameter name with the corresponding Kubernetes version
as required. For example, if you want to use Kubernetes 1.30, use the
following parameter:
`/aws/service/hyperpod/ami/x86_64/eks-1.30-amazon-linux-2/latest/ami-id`.

## Build your custom AMI

After you have selected a SageMaker HyperPod public AMI, use that as the base AMI to
build your own custom AMI with one of the following methods. Note that this is not
an exhaustive list for building AMIs. You can use any method of your choice for
building AMIs. SageMaker HyperPod does not have any specific recommendation.

- **AWS Management Console**: You can launch
  an Amazon EC2 instance using the SageMaker HyperPod AMI, make desired customizations,
  and then create an AMI from that instance.
- **AWS CLI**: You can also use the `aws ec2
create-image` command to create an AMI from an existing Amazon EC2
  instance after performing the customization.
- **HashiCorp Packer**: Packer is an
  open-source tool from HashiCorp that enables you to create identical machine
  images for multiple platforms from a single source configuration. It
  supports creating AMIs for AWS, as well as images for other cloud
  providers and virtualization platforms.
- **Image Builder**: EC2 Image Builder is a fully managed
  AWS service that makes
  it easier to automate the creation, maintenance, validation, sharing, and
  deployment of Linux or Windows Server images. For more information,
  see the [EC2 Image Builder User Guide](../../../imagebuilder/latest/userguide/what-is-image-builder.md "../../../imagebuilder/latest/userguide/what-is-image-builder.md").

### Build a custom AMI with customer

managed AWS KMS encryption

The following sections describe how to build a custom AMI with a customer managed AWS KMS key
to encrypt your HyperPod cluster volumes. For more information about customer managed keys in HyperPod
and granting the required IAM and KMS key policy permissions, see
[Customer managed AWS KMS key encryption for SageMaker HyperPod](smcluster-cmk.md "smcluster-cmk.md"). If you plan
to use a custom AMI that is encrypted with a customer managed key, ensure that you also encrypt
your HyperPod cluster's Amazon EBS root volume with the same key.

#### AWS CLI example: Create a new

AMI using EC2 Image Builder and a HyperPod base image

The following example shows how to create an AMI using Image Builder with
AWS KMS encryption:

```
aws imagebuilder create-image-recipe \
    name "`hyperpod-custom-recipe`" \
    version "1.0.0" \
    parent-image "`<hyperpod-base-image-id>`" \
    block-device-mappings DeviceName="/dev/xvda",Ebs={VolumeSize=100,VolumeType=gp3,Encrypted=true,KmsKeyId=arn:aws:kms:`us-east-1`:`111122223333`:key/`key-id`,DeleteOnTermination=true}
```

#### Amazon EC2 console: Create

a new AMI from an Amazon EC2

To create an AMI from an Amazon EC2 instance using the Amazon EC2 console:

1. Right-click on your customized Amazon EC2 instance and choose
   **Create Image**.
2. In the **Encryption** section, select
   **Encrypt snapshots**.
3. Select your KMS key from the dropdown. For example:
   `arn:aws:kms:`us-east-2`:`111122223333`:key/`<your-kms-key-id>``
or use the key alias: `alias/`<your-hyperpod-key>``.

#### AWS CLI example: Create

a new AMI from an Amazon EC2 instance

Use the `aws ec2 create-image` command with AWS KMS
encryption:

```
aws ec2 create-image \
    instance-id "`<instance-id>`" \
    name "`MyCustomHyperPodAMI`" \
    description "`Custom HyperPod AMI`" \
    block-device-mappings '[
        {
            "DeviceName": "/dev/xvda",
            "Ebs": {
                "Encrypted": true,
                "KmsKeyId": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-id`",
                "VolumeType": "gp2"
            }
        }
    ]'
```
