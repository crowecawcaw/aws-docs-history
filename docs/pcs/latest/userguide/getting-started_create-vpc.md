# Create a VPC and subnets for AWS PCS

You can create a VPC and subnets with a CloudFormation template. Use the following
URL to download the CloudFormation template, then upload the template in the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home#/stacks/create "https://console.aws.amazon.com/cloudformation/home#/stacks/create") to create a new CloudFormation
stack. For more information, see [Using the AWS CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-using-console.md "../../../AWSCloudFormation/latest/UserGuide/cfn-using-console.md")
in the _AWS CloudFormation User Guide_.

```
https://aws-hpc-recipes.s3.amazonaws.com/main/recipes/net/hpc_large_scale/assets/main.yaml
```

With the template open in the AWS CloudFormation console, enter the following options. You can
use the default values provided in the template.

- Under **Provide a stack name**:
  - Under **Stack name**, enter:

  ```
  hpc-networking
  ```

- Under **Parameters**:
  - Under **VPC**:
    - Under **CidrBlock**, enter:

    ```
    10.3.0.0/16
    ```

  - Under **Subnets A**:
    - Under **CidrPublicSubnetA**, enter:

    ```
    10.3.0.0/20
    ```

    - Under **CidrPrivateSubnetA**, enter:

    ```
    10.3.128.0/20
    ```

  - Under **Subnets B**:
    - Under **CidrPublicSubnetB**, enter:

    ```
    10.3.16.0/20
    ```

    - Under **CidrPrivateSubnetB**, enter:

    ```
    10.3.144.0/20
    ```

  - Under **Subnets C**:
    - For **ProvisionSubnetsC**, select **True**
    - Under **CidrPublicSubnetC**, enter:

    ```
    10.3.32.0/20
    ```

    - Under **CidrPrivateSubnetC**, enter:

    ```
    10.3.160.0/20
    ```

- Under **Capabilities**:

      + Check the box for **I acknowledge that AWS CloudFormation might create IAM
       resources**.

  Monitor the status of the CloudFormation stack. When it reaches
  `CREATE_COMPLETE`, find the ID for the default security group in the new VPC. You
  use the ID later in the tutorial.

## Find the default security group for the

cluster VPC

To find the ID for the default security group in the new VPC, follow this procedure:

- Navigate to the [Amazon VPC console](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc").
- Under the **VPC Dashboard**, select **Filter by VPC**.
  - Choose the VPC where the name starts with `hpc-networking`.
  - Under **Security**, choose **Security groups**.

- Find the **Security group ID** for the group named `default`.
  It has the description `default VPC security group`. You use the ID later to
  configure EC2 launch templates.
