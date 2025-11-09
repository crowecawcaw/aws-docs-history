# Amazon DocumentDB quick start using AWS CloudFormation

This section contains steps and other information to help you get
started quickly with Amazon DocumentDB (with MongoDB compatibility) using [AWS CloudFormation](../../../en_us/AWSCloudFormation/latest/UserGuide/Welcome.md "../../../en_us/AWSCloudFormation/latest/UserGuide/Welcome.md").
For general information about Amazon DocumentDB, see [What is Amazon DocumentDB (with MongoDB compatibility)](what-is.md "what-is.md").

These instructions use an AWS CloudFormation template to create a cluster and
instances in your default Amazon VPC. For instructions on creating these
resources yourself, see [Get started with Amazon DocumentDB](get-started-guide.md "get-started-guide.md").

###### Important

The AWS CloudFormation stack that is created by this template creates multiple
resources, including resources in Amazon DocumentDB (for example, a cluster and
instances) and Amazon Elastic Compute Cloud (for example, a subnet group).

Some of these resources are not free-tier resources. For pricing
information, see [Amazon DocumentDB
Pricing](https://aws.amazon.com/documentdb/pricing/ "https://aws.amazon.com/documentdb/pricing/") and [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/").
You can delete the stack when you are finished with it to stop any
charges.

This AWS CloudFormation stack is intended for tutorial purposes only. If you use
this template for a production environment, we recommend that you use
stricter IAM policies and security. For information about securing
resources, see [Amazon VPC Security](../../../vpc/latest/userguide/VPC_Security.md "../../../vpc/latest/userguide/VPC_Security.md") and [Amazon EC2 Network and Security](../../../AWSEC2/latest/UserGuide/EC2_Network_and_Security.md "../../../AWSEC2/latest/UserGuide/EC2_Network_and_Security.md").

###### Topics

- [Prerequisites](#quick_start_cfn-prerequisites "#quick_start_cfn-prerequisites")
- [Launching an Amazon DocumentDB
  AWS CloudFormation stack](#quick_start_cfn-launch_stack "#quick_start_cfn-launch_stack")
- [Accessing the Amazon DocumentDB cluster](#quick_start_cfn-accessing_stack "#quick_start_cfn-accessing_stack")
- [Termination
  protection and deletion protection](#quick_start_cfn-termination_deletion_protection "#quick_start_cfn-termination_deletion_protection")

## Prerequisites

Before you create an Amazon DocumentDB cluster, you must have the following:

- A default Amazon VPC
- The required IAM permissions

### Required IAM

Permissions

The following permissions allow you to create resources for the
AWS CloudFormation stack:

**AWS Managed Policies**

- `AWSCloudFormationReadOnlyAccess`
- `AmazonDocDBFullAccess`

###### Additional IAM Permissions

The following policy outlines the additional permissions that
are required to create and delete this AWS CloudFormation stack.

In the following examples, replace each `user input placeholder` with your resource's information.

### Amazon EC2 Key Pair

You must have a key pair (and the PEM file) available in the
Region where you will create the AWS CloudFormation stack. If you need to create
a key pair, see [Creating a Key Pair Using Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md#having-ec2-create-your-key-pair "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md#having-ec2-create-your-key-pair")
in the _Amazon EC2 User Guide_.

## Launching an Amazon DocumentDB

AWS CloudFormation stack

This section describes how to launch and configure an Amazon DocumentDB AWS CloudFormation
stack.

1. Sign in to the AWS Management Console at [https://console.aws.amazon.com/](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. The following table lists the Amazon DocumentDB stack templates for each
   AWS Region. Choose **Launch Stack** for the AWS Region you want to launch your stack in.

| Region                   | View Template                                                                                                                                                                                                                          | View in Designer                                                                                                                                                                                                                                                                                                                                                                                                                              | Launch                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (Ohio)           | [View Template](https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=us-east-2&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/designer/home?region=us-east-2&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")                   | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")           |
| US East (N. Virginia)    | [View Template](https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") | [View in Designer](https://us-east-2.console.aws.amazon.com/cloudformation/designer/home?templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml&region=us-east-2 "https://us-east-2.console.aws.amazon.com/cloudformation/designer/home?templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml®ion=us-east-2") | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")           |
| US West (Oregon)         | [View Template](https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=us-west-2&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/designer/home?region=us-west-2&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")                   | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")           |
| Asia Pacific (Mumbai)    | [View Template](https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=ap-south-1&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/designer/home?region=ap-south-1&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")                 | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")         |
| Asia Pacific (Seoul)     | [View Template](https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=ap-northeast-2&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/designer/home?region=ap-northeast-2&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")         | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") |
| Asia Pacific (Singapore) | [View Template](https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=ap-southeast-1&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/designer/home?region=ap-southeast-1&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")         | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") |
| Asia Pacific (Sydney)    | [View Template](https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=ap-southeast-2&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/designer/home?region=ap-southeast-2&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")         | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") |
| Asia Pacific (Tokyo)     | [View Template](https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=ap-northeast-1&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/designer/home?region=ap-northeast-1&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")         | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") |
| Canada (Central)         | [View Template](https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=ca-central-1&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/designer/home?region=ca-central-1&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")             | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")     |
| Europe (Frankfurt)       | [View Template](https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=eu-central-1&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/designer/home?region=eu-central-1&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")             | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")     |
| Europe (Ireland)         | [View Template](https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=eu-west-1&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/designer/home?region=eu-west-1&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")                   | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")           |
| Europe (London)          | [View Template](https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=eu-west-2&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/designer/home?region=eu-west-2&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")                   | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")           |
| Europe (Paris)           | [View Template](https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=eu-west-3&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/designer/home?region=eu-west-3&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")                   | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml "https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/new?stackName=DocumentDBQuickStart&templateURL=https://s3.amazonaws.com/amazon-documentdb-samples/v1/cloudformation-templates/documentdb_full_stack.yaml")           |

3. **Create stack** — Describes the
   Amazon DocumentDB template that you selected. Every stack is based on a
   template — a JSON or YAML file — that contains
   configuration about the AWS resources you want to include in the
   stack. Because you chose to launch a stack from the provided
   templates above, your template has already been configured to
   create an Amazon DocumentDB stack for the AWS Region you chose.

When you launch an AWS CloudFormation stack, [deletion protection](#quick_start_cfn-termination_deletion_protection "#quick_start_cfn-termination_deletion_protection")
for your Amazon DocumentDB cluster is disabled by default. If you want
to enable deletion protection for your cluster, complete the
following steps. Otherwise, choose **Next** to
continue to the next step.

**To enable deletion protection for your
Amazon DocumentDB cluster:**

    1. Choose **View in Designer** from the
     bottom right corner of the **Create stack**
     page.
    2. Modify the template using the integrated JSON and YAML
     editor in the resulting AWS CloudFormation Designer page of the console.
     Scroll to the `Resources` section and modify it
     to include `DeletionProtection`, as follows. For
     more information about using AWS CloudFormation Designer,
     see [What Is AWS CloudFormation Designer?](../../../en_us/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../en_us/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md").



    JSON:



    ```
    "Resources": {
        "DBCluster": {
            "Type": "AWS::DocDB::DBCluster",
            "DeletionPolicy": "Delete",
            "Properties": {
                "DBClusterIdentifier": {
                    "Ref": "DBClusterName"
                },
                "MasterUsername": {
                    "Ref": "MasterUser"
                },
                "MasterUserPassword": {
                    "Ref": "MasterPassword"
                },
                "DeletionProtection": "true"
            }
        },
    ```

    YAML:



    ```
    Resources:
      DBCluster:
        Type: 'AWS::DocDB::DBCluster'
        DeletionPolicy: Delete
        Properties:
          DBClusterIdentifier: !Ref DBClusterName
          MasterUsername: !Ref MasterUser
          MasterUserPassword: !Ref MasterPassword
          DeletionProtection: 'true'
    ```
    3. Choose **Create Stack** (

    ![Cloud icon with arrow pointing to it, representing cloud upload or storage.](images/cfn-create-stack-icon.png)
    )
     from the top left corner of the page to save your changes
     and create a stack with these changes enabled.
    4. After you save your changes, you will be redirected
     to the **Create stack** page.
    5. Choose **Next** to continue.

4.  **Specify stack details** — Enter the
    stack name and parameters for your template. Parameters are
    defined in your template and allow you to input custom values
    when you create or update a stack.
    - Under **Stack name**, enter a name for
      your stack or accept the provided name. The stack name can
      include letters (A—Z and a—z), numbers
      (0—9), and dashes (—).
    - Under **Parameters**, enter the
      following details:

          + **DBClusterName** — Enter
           a name for your Amazon DocumentDB cluster or accept the
           provided name.


          Cluster naming constraints:




          	- Length is [1—63] letters, numbers, or
          	 hyphens.
          	- First character must be a letter.
          	- Cannot end with a hyphen or contain two
          	 consecutive hyphens.
          	- Must be unique for all clusters across Amazon RDS,
          	 Neptune, and Amazon DocumentDB per AWS account, per
          	 Region.
          + **DBInstanceClass** — From
           the drop-down list, select the instance class for
           your Amazon DocumentDB cluster.
          + **DBInstanceName** — Enter
           a name for your Amazon DocumentDB instance or accept the
           provided name.


          Instance naming constraints:




          	- Length is [1—63] letters,
          	 numbers, or hyphens.
          	- First character must be a letter.
          	- Cannot end with a hyphen or contain two
          	 consecutive hyphens.
          	- Must be unique for all instances
          	 across Amazon RDS, Neptune, and Amazon DocumentDB
          	 per AWS account, per Region.
          + **MasterPassword** — The
           database admin account password.
          + **MasterUser** — The
           database admin account username. The MasterUser must
           begin with a letter and can contain only alphanumeric
           characters.Choose **Next** to save your changes and

      continue.

5.  **Configure stack options** —
    Configure your stack's tags, permissions, and additional options.
    - **Tags** — Specify tags
      (key-value) pairs to apply to your resources in your stack.
      You can add up to 50 unique tags for each stack.
    - **Permissions** — Optional.
      Choose an IAM role to explicitly define how AWS CloudFormation can
      create, modify, or delete resources in the stack. If you
      don't choose a role, AWS CloudFormation uses permissions based on your
      user credentials. Before you specify a service role, ensure
      that you have permission to pass it
      (`iam:PassRole`). The `iam:PassRole`
      permission specifies which roles you can use.

    ###### Note

    When you specify a service role, AWS CloudFormation always uses
    that role for all operations that are performed on that
    stack. Other users that have permissions to perform
    operations on this stack will be able to use this role,
    even if they don't have permission to pass it. If the
    role includes permissions that the user shouldn't have,
    you can unintentionally escalate a user's permissions.
    Ensure that the role grants [least privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege").
    - **Advanced options** — You can
      set the following advanced options:
      - **Stack policy** — Optional.
        Defines the resources that you want to protect from
        unintentional updates during a stack update. By
        default, all resources can be updated during a stack
        update.

      You can enter the stack policy directly as JSON,
      or upload a JSON file containing the stack policy.
      For more information, see [Prevent Updates to Stack Resources](../../../AWSCloudFormation/latest/UserGuide/protect-stack-resources.md "../../../AWSCloudFormation/latest/UserGuide/protect-stack-resources.md").
      - **Rollback configuration** —
        Optional. Specify CloudWatch Logs alarms for AWS CloudFormation to monitor
        when creating and updating the stack. If the operation
        breaches an alarm threshold, AWS CloudFormation rolls it back.
      - **Notification options** —
        Optional. Specify topics for Simple Notification
        System (SNS).
      - **Stack creation options** —
        Optional. You can specify the following options:
        - **Rollback on failure**
          — Whether or not the stack should be
          rolled back if the stack creation fails.
        - **Timeout** —The
          number of minutes before a stack creation times
          out.
        - **Termination protection**
          — Prevents the stack from being
          accidentally deleted.

        ###### Note

        AWS CloudFormation termination protection is different
        from the Amazon DocumentDB concept of deletion
        protection. For more information, see [Termination
        protection and deletion protection](#quick_start_cfn-termination_deletion_protection "#quick_start_cfn-termination_deletion_protection").Choose **Next** to continue.

6.  **Review <stack-name>** — Review
    your stack template, details, and configuration options. You can
    also open a **quick-create link** at the bottom
    of the page to create stacks with the same basic configurations
    as this one.
    - Choose **Create** to create the stack.
    - Alternatively, you can choose **Create change
      set**. A change set is a preview of how this stack
      will be configured before creating the stack. This allows
      you to examine various configurations before executing the
      change set.

## Accessing the Amazon DocumentDB cluster

Once the AWS CloudFormation stack has been completed, you can use an Amazon EC2 instance
to connect to your Amazon DocumentDB cluster. For information about connecting to
an Amazon EC2 instance using SSH, see [Connect to Your Linux Instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md")
in the _Amazon EC2 User Guide_.

After you are connected, see the following sections, which contain
information about using Amazon DocumentDB.

- [Step 3: Insert and query data](get-started-guide.md#get-start-insert-query "get-started-guide.md#get-start-insert-query")
- [Managing Amazon DocumentDB resources](managing-documentdb.md "managing-documentdb.md")
- [Monitoring Amazon DocumentDB](monitoring_docdb.md "monitoring_docdb.md")

## Termination

protection and deletion protection

It is an Amazon DocumentDB best practice to enable deletion protection and
termination protection. CloudFormation termination protection is a
distinctly different feature from the Amazon DocumentDB deletion protection
feature.

- **Termination protection** —
  You can prevent a stack from being accidentally deleted by
  enabling termination protection for your CloudFormation stack. If
  a user attempts to delete a stack with termination protection
  enabled on it, the deletion fails and the stack remains unchanged.
  Termination protection is disabled by default when you create a
  stack using CloudFormation. You can enable termination protection
  on a stack when you create it. For more information, see [Setting AWS CloudFormation Stack Options](../../../AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.md").
- **Deletion protection** —
  Amazon DocumentDB also provides the ability to enable deletion protection
  for a cluster. If a user attempts to delete an Amazon DocumentDB cluster
  with deletion protection enabled on it, the deletion fails and
  the cluster remains unchanged. Deletion protection, when enabled,
  safeguards against accidental deletes from the Amazon DocumentDB AWS Management Console,
  AWS CLI, and CloudFormation. For more information on enabling and
  disabling deletion protection for an Amazon DocumentDB cluster, see [Deletion protection](db-cluster-delete.md#db-cluster-deletion-protection "db-cluster-delete.md#db-cluster-deletion-protection").
