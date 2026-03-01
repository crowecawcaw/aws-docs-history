# Retrieving Amazon ECS-optimized Bottlerocket AMI metadata

You can retrieve the Amazon Machine Image (AMI) ID for Amazon ECS-optimized AMIs by
querying the AWS Systems Manager Parameter Store API. Using this parameter, you don't need to
manually look up Amazon ECS-optimized AMI IDs. For more information about the Systems Manager Parameter
Store API, see [GetParameter](../../../systems-manager/latest/APIReference/API_GetParameter.md "../../../systems-manager/latest/APIReference/API_GetParameter.md"). The
user that you use must have the `ssm:GetParameter` IAM permission to
retrieve the Amazon ECS-optimized AMI metadata.

## `aws-ecs-2` Bottlerocket AMI variant

You can retrieve the latest stable `aws-ecs-2` Bottlerocket AMI
variant by AWS Region and architecture with the AWS CLI or the AWS Management Console.

- AWS CLI – You can retrieve the image
  ID of the latest recommended Amazon ECS-optimized Bottlerocket AMI
  with the following AWS CLI command by using the subparameter
  `image_id`. Replace the
  `region` with the Region code
  that you want the AMI ID for.

For information about the supported
AWS Regions, see [Finding an AMI](https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami "https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami") on GitHub. To retrieve a version other than the
latest, replace `latest` with the version number.

    + For the 64-bit (`x86_64`) architecture:



    ```
    aws ssm get-parameter --region `us-east-2` --name "/aws/service/bottlerocket/aws-ecs-2/x86_64/latest/image_id" --query Parameter.Value --output text
    ```
    + For the 64-bit Arm (`arm64`) architecture:



    ```
    aws ssm get-parameter --region `us-east-2` --name "/aws/service/bottlerocket/aws-ecs-2/arm64/latest/image_id" --query Parameter.Value --output text
    ```

- AWS Management Console – You can query for the
  recommended Amazon ECS-optimized AMI ID using a URL in the AWS Management Console. The URL
  opens the Amazon EC2 Systems Manager console with the value of the ID for the parameter. In
  the following URL, replace `region`
  with the Region code that you want the AMI ID for.

For information about the
supported AWS Regions, see [Finding an AMI](https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami "https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami") on GitHub.

    + For the 64-bit (`x86_64`) architecture:



    ```
    https://console.aws.amazon.com/systems-manager/parameters/aws/service/bottlerocket/aws-ecs-2/x86_64/latest/image_id/description?region=`region`#
    ```
    + For the 64-bit Arm (`arm64`) architecture:



    ```
    https://console.aws.amazon.com/systems-manager/parameters/aws/service/bottlerocket/aws-ecs-2/arm64/latest/image_id/description?region=`region`#
    ```

## `aws-ecs-2-nvidia` Bottlerocket AMI variant

You can retrieve the latest stable `aws-ecs-2-nvdia` Bottlerocket AMI
variant by Region and architecture with the AWS CLI or the AWS Management Console.

- AWS CLI – You can retrieve the image
  ID of the latest recommended Amazon ECS-optimized Bottlerocket AMI
  with the following AWS CLI command by using the subparameter
  `image_id`. Replace the
  `region` with the Region code
  that you want the AMI ID for.

For information about the supported
AWS Regions, see [Finding an AMI](https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami "https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami") on GitHub. To retrieve a version other than the
latest, replace `latest` with the version number.

    + For the 64-bit (`x86_64`) architecture:



    ```
    aws ssm get-parameter --region `us-east-1` --name "/aws/service/bottlerocket/aws-ecs-2-nvidia/x86_64/latest/image_id" --query Parameter.Value --output text
    ```
    + For the 64 bit Arm (`arm64`) architecture:



    ```
    aws ssm get-parameter --region `us-east-1` --name "/aws/service/bottlerocket/aws-ecs-2-nvidia/arm64/latest/image_id" --query Parameter.Value --output text
    ```

- AWS Management Console – You can query for the
  recommended Amazon ECS optimized AMI ID using a URL in the AWS Management Console. The URL
  opens the Amazon EC2 Systems Manager console with the value of the ID for the parameter. In
  the following URL, replace `region`
  with the Region code that you want the AMI ID for.

For
information about the supported AWS Regions, see [Finding an AMI](https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami "https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami") on GitHub.

    + For the 64 bit (`x86_64`) architecture:



    ```
    https://`region`console.aws.amazon.com/systems-manager/parameters/aws/service/bottlerocket/aws-ecs-2-nvidia/x86_64/latest/image_id/description?region=`region`#
    ```
    + For the 64 bit Arm (`arm64`)
     architecture:



    ```
    https://`region`console.aws.amazon.com/systems-manager/parameters/aws/service/bottlerocket/aws-ecs-2-nvidia/arm64/latest/image_id/description?region=`region`#
    ```

## `aws-ecs-1` Bottlerocket AMI variant

You can retrieve the latest stable `aws-ecs-1` Bottlerocket AMI
variant by AWS Region and architecture with the AWS CLI or the AWS Management Console.

- AWS CLI – You can retrieve the image
  ID of the latest recommended Amazon ECS-optimized Bottlerocket AMI
  with the following AWS CLI command by using the subparameter
  `image_id`. Replace the
  `region` with the Region code
  that you want the AMI ID for.

For information about the supported
AWS Regions, see [Finding an AMI](https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami "https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami") on GitHub. To retrieve a version other than the
latest, replace `latest` with the version number.

    + For the 64-bit (`x86_64`) architecture:



    ```
    aws ssm get-parameter --region `us-east-1` --name "/aws/service/bottlerocket/aws-ecs-1/x86_64/latest/image_id" --query Parameter.Value --output text
    ```
    + For the 64-bit Arm (`arm64`) architecture:



    ```
    aws ssm get-parameter --region `us-east-1` --name "/aws/service/bottlerocket/aws-ecs-1/arm64/latest/image_id" --query Parameter.Value --output text
    ```

- AWS Management Console – You can query for the
  recommended Amazon ECS-optimized AMI ID using a URL in the AWS Management Console. The URL
  opens the Amazon EC2 Systems Manager console with the value of the ID for the parameter. In
  the following URL, replace `region`
  with the Region code that you want the AMI ID for.

For information about the
supported AWS Regions, see [Finding an AMI](https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami "https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami") on GitHub.

    + For the 64-bit (`x86_64`) architecture:



    ```
    https://`region`.console.aws.amazon.com/systems-manager/parameters/aws/service/bottlerocket/aws-ecs-1/x86_64/latest/image_id/description
    ```
    + For the 64-bit Arm (`arm64`) architecture:



    ```
    https://`region`.console.aws.amazon.com/systems-manager/parameters/aws/service/bottlerocket/aws-ecs-1/arm64/latest/image_id/description
    ```

## `aws-ecs-1-nvidia` Bottlerocket AMI variant

You can retrieve the latest stable `aws-ecs-1-nvdia` Bottlerocket AMI
variant by Region and architecture with the AWS CLI or the AWS Management Console.

- AWS CLI – You can retrieve the image
  ID of the latest recommended Amazon ECS-optimized Bottlerocket AMI
  with the following AWS CLI command by using the subparameter
  `image_id`. Replace the
  `region` with the Region code
  that you want the AMI ID for.

For information about the
supported AWS Regions, see [Finding an AMI](https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami "https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami") on GitHub.

    + For the 64-bit (`x86_64`) architecture:



    ```
    aws ssm get-parameter --region `us-east-1` --name "/aws/service/bottlerocket/aws-ecs-1-nvidia/x86_64/latest/image_id" --query Parameter.Value --output text
    ```
    + For the 64 bit Arm (`arm64`) architecture:



    ```
    aws ssm get-parameter --region `us-east-1` --name "/aws/service/bottlerocket/aws-ecs-1-nvidia/arm64/latest/image_id" --query Parameter.Value --output text
    ```

- AWS Management Console – You can query for the
  recommended Amazon ECS optimized AMI ID using a URL in the AWS Management Console. The URL
  opens the Amazon EC2 Systems Manager console with the value of the ID for the parameter. In
  the following URL, replace `region`
  with the Region code that you want the AMI ID for.

For information about the
supported AWS Regions, see [Finding an AMI](https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami "https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md#finding-an-ami") on GitHub.

    + For the 64 bit (`x86_64`) architecture:



    ```
    https://console.aws.amazon.com/systems-manager/parameters/aws/service/bottlerocket/aws-ecs-1-nvidia/x86_64/latest/image_id/description?region=`region`#
    ```
    + For the 64 bit Arm (`arm64`) architecture:



    ```
    https://console.aws.amazon.com/systems-manager/parameters/aws/service/bottlerocket/aws-ecs-1-nvidia/arm64/latest/image_id/description?region=`region`#
    ```

## Next steps

For a detailed tutorial on how to get started with the Bottlerocket
operating system on Amazon ECS, see [Using a Bottlerocket AMI with Amazon ECS](https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md "https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-ECS.md") on GitHub and [Getting started withBottlerocket and Amazon ECS](https://aws.amazon.com/blogs/containers/getting-started-with-bottlerocket-and-amazon-ecs/ "https://aws.amazon.com/blogs/containers/getting-started-with-bottlerocket-and-amazon-ecs/") on the AWS
blog site.

For information about how to launch a Bottlerocket instance, see [Launching a Bottlerocket instance for Amazon ECS](bottlerocket-launch.md "bottlerocket-launch.md")
