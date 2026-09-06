

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Rehost applications on Amazon EC2 template
<a name="rehost-on-ec2"></a>

You can rehost your custom Windows and Linux applications on Amazon EC2 using the *Rehost applications on Amazon EC2* template.

## Prerequisites
<a name="prerequisites-rehost-on-ec2"></a>

You must meet the following requirements to create a migration workflow using this template.
+ Verify that your applications are on a supported operating system. For more information, see [Supported operating systems](https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html).
+ AWS Application Migration Service must be initialized by the IAM admin of the AWS account. For more information, see [Application Migration Service initialization and permissions](https://docs.aws.amazon.com/mgn/latest/ug/mandatory-setup.html).
+ Complete the replication settings for AWS Application Migration Service. For more information, see [Replication settings](https://docs.aws.amazon.com/mgn/latest/ug/replication-settings-template.html).
+ Users must have the permissions granted by the [AWSApplicationMigrationAgentPolicy](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationAgentPolicy.html) policy.
+ Provide credentials in the AWS Secrets Manager to install the AWS Replication Agent on your remote server.

  1. Sign in to [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

  1. On the AWS Secrets Manager page, select **Store a new secret**.

  1. For Secret type, select **Other type of secret** and enter the following keys.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/rehost-on-ec2.html)

  1. Select **Next** and enter a name for the key pair beginning with `migrationhub-orchestrator-{{secretname123}}`.
**Important**  
The Secret ID must begin with the prefix `migrationhub-orchestrator-` and must only be followed by an alphanumeric value.

  1. Select **Next** and then, select **Store**.
+  Create an IAM role with the Amazon EC2 use case to run test scripts on migrated instances. Attach the [AWSMigrationHubOrchestratorInstanceRolePolicy](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AWSMigrationHubOrchestratorInstanceRolePolicy) and AmazonSSMManagedInstanceCore policies to this role. Once the role is created, update the trust policy to include SSM (` ssm.amazonaws.com`). For more information on updating a trust policy, see [Modifying a role trust policy (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy). 
+ The IAM user running the AWS Application Migration Service must have permissions to perform the `startTest` and `startCutoverInstance` tasks. Create an IAM user and attach the **AWSApplicationMigrationFullAccess**, **AWSApplicationMigrationEC2Access**, and **AmazonEC2FullAccess** policies along with the following inline policy.

  ```
         {
              "Effect": "Allow",
              "Action": [
                  "mgn:StartCutover",
                  "mgn:StartTest"
              ],
              "Resource": "*"
          },
          {
              "Effect": "Allow",
              "Action": "iam:PassRole",
              "Resource": "*",
              "Condition": {
                  "StringEquals": {
                      "iam:PassedToService": "ec2.amazonaws.com"
                  }
              }
          }
  ```

## Create a migration workflow
<a name="create-workflow-rehost-on-ec2"></a>

1. Go to [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/), and select **Create migration workflow**.

1. On Choose a workflow template page, select **Rehost on Amazon EC2 using AWS Application Migration Service** template.

1. Configure and submit your workflow to begin migration.
   + [Details](#details-rehost-on-ec2)
   + [Application](#applications-rehost-on-ec2)
   + [Target environment configuration](#target-env-config-rehost-on-ec2)

**Note**  
You can customize the migration workflow once it has been created. For more information, see [Migration workflows for Migration Hub Orchestrator](migration-workflows.md).

## Details
<a name="details-rehost-on-ec2"></a>

Enter a name for your workflow. Optionally, you can enter a description and add tags. If you intend to run multiple migrations, we recommend adding tags to enhance searchability. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).

## Application
<a name="applications-rehost-on-ec2"></a>

Select the application you want to migrate. If you do not see the application in the list, you must define it in [AWS Application Discovery Service](https://console.aws.amazon.com/discovery/home).

### Define applications
<a name="define-applications"></a>

Define applications by adding a data source and grouping the servers as applications.

**Topics**
+ [Add data source](#add-data-source)
+ [Group servers](#group-servers)

#### Add data source
<a name="add-data-source"></a>

Get metadata about the source servers and applications that you want to migrate to AWS. You can use one of the following methods to collect the data.
+ **Migration Hub import** – Import information about your on-premises servers and applications into Migration Hub. For more information, see [Migration Hub Import](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html) in the *Application Discovery Service User Guide*. 
+ **AWS Agentless Discovery Connector** – The Discovery Connector is a VMware appliance that collects information about VMware virtual machines (VMs). For more information, see [AWS Agentless Discovery Connector](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-connector.html) in the *Application Discovery Service User Guide*.
+ **AWS Application Discovery Agent** – The Discovery Agent is AWS software that you install on your on-premises servers and VMs to capture system information, as well as information about the network connections between systems. For more information, see [AWS Application Discovery Agent](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-agent.html) in the *Application Discovery Service User Guide*.

#### Group servers
<a name="group-servers"></a>

To use Migration Hub Orchestrator, you must group servers as applications.

1. In AWS Migration Hub console, select **Discover**, **Servers**.

1. In the servers list, select each server that you want to group into a new or existing application.

1. To create your application, or add to an existing one, choose **Group as application**.

1. In the **Group as application** dialog box, choose **Group as a new application** or **Add to an existing application**.

1. Select **Group**.

To view and edit your applications in the AWS Migration Hub console, go to **Discover** > **Servers**.

## Target environment configuration
<a name="target-env-config-rehost-on-ec2"></a>

If you want to run test scripts on migrated instances, check the box for *I want to run test scripts on the migrated instances*.

**Note**  
We recommend having separate workflows for Linux and Windows servers if you want to run validation tests on migrated instances.
+ Test script location: Specify the Amazon S3 bucket that contains your test script. For more information, see [Getting started with Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html).
+ IAM role: Choose the IAM role you created in [Prerequisites](#prerequisites-rehost-on-ec2).
+ Script run command: Enter the **run** command for your script.

Credentials to install AWS Replication Agent: Select the credentials you created in [Prerequisites](#prerequisites-rehost-on-ec2).