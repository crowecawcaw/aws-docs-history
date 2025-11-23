# Learn how to configure FSx for Windows File Server file systems for

Amazon ECS

Learn how to launch an Amazon ECS-Optimized Windows instance that hosts an FSx for Windows File Server
file system and containers that can access the file system. To do this, you first create an
Directory Service AWS Managed Microsoft Active Directory. Then, you create an FSx for Windows File Server
File Server file system and cluster with an Amazon EC2 instance and a task
definition. You configure the task definition for your containers to use the FSx for Windows File Server
file system. Finally, you test the file system.

It takes 20 to 45 minutes each time you launch or delete either the Active Directory or
the FSx for Windows File Server file system. Be prepared to reserve at least 90 minutes to complete the
tutorial or complete the tutorial over a few sessions.

## Prerequisites for the tutorial

- An administrative user. See [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md").
- (Optional) A `PEM` key pair for connecting to your
  EC2 Windows instance through RDP access. For information about how
  to create key pairs, see [Amazon EC2 key pairs and
  Amazon EC2 instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") in the _Amazon EC2 User Guide_.
- A VPC with at least one public and one private subnet, and one security group.
  You can use your default VPC. You don't need a NAT gateway or device. Directory Service
  doesn't support Network Address Translation (NAT) with Active Directory. For
  this to work, the Active Directory, FSx for Windows File Server file system, ECS Cluster, and
  EC2 instance must be located within your VPC. For more information
  regarding VPCs and Active Directories, see [Create a VPC](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md") and [Prerequisites for creating an AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_getting_started.md#ms_ad_getting_started_prereqs "../../../directoryservice/latest/admin-guide/ms_ad_getting_started.md#ms_ad_getting_started_prereqs").
- The IAM ecsInstanceRole and ecsTaskExecutionRole permissions are associated
  with your account. These service-linked roles allow services to make API calls
  and access containers, secrets, directories, and file servers on your
  behalf.

## Step 1: Create IAM access roles

###### Create a cluster with the AWS Management Console.

1.  See [Amazon ECS container instance IAM role](instance_IAM_role.md "instance_IAM_role.md") to
    check whether you have an ecsInstanceRole and to see how you can create one if
    you don't have one.
2.  We recommend that role policies are customized for minimum permissions in an
    actual production environment. For the purpose of working through this tutorial,
    verify that the following AWS managed policy is attached to your
    ecsInstanceRole. Attach the policy if it is not already attached.

        * AmazonEC2ContainerServiceforEC2Role
        * AmazonSSMManagedInstanceCore
        * AmazonSSMDirectoryServiceAccess

    To attach AWS managed policies.

        1. Open the [IAM
         console](https://console.aws.amazon.com//iam/ "https://console.aws.amazon.com//iam/").
        2. In the navigation pane, choose **Roles.**
        3. Choose an **AWS managed role**.
        4. Choose **Permissions, Attach policies**.
        5. To narrow the available policies to attach, use
         **Filter**.
        6. Select the appropriate policy and choose **Attach
         policy**.

3.  See [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md") to check whether you have an
    ecsTaskExecutionRole and to see how you can create one if you don't have
    one.

We recommend that role policies are customized for minimum permissions in an
actual production environment. For the purpose of working through this tutorial,
verify that the following AWS managed policies are attached to your
ecsTaskExecutionRole. Attach the policies if they are not already attached. Use
the procedure given in the preceding section to attach the AWS managed
policies.

    * SecretsManagerReadWrite
    * AmazonFSxReadOnlyAccess
    * AmazonSSMReadOnlyAccess
    * AmazonECSTaskExecutionRolePolicy

## Step 2: Create Windows Active Directory (AD)

1. Follow the steps described in [Creating your AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_getting_started.md#ms_ad_getting_started_create_directory "../../../directoryservice/latest/admin-guide/ms_ad_getting_started.md#ms_ad_getting_started_create_directory") in the AWS
   _Directory Service Administration Guide_. Use the VPC you
   have designated for this tutorial. On Step 3 of _Creating your AWS Managed Microsoft AD_, save the user name and admin password for use in
   a following step. Also, note the fully qualified directory DNS name for future steps.
   You can complete the following step while the Active Directory is being
   created.
2. Create an AWS Secrets Manager secret to use in the following steps. For more
   information, see [Get started
   with Secrets Manager](../../../secretsmanager/latest/userguide/intro.md#get-started "../../../secretsmanager/latest/userguide/intro.md#get-started") in the AWS _Secrets Manager
   User Guide_.
   1. Open the [Secrets Manager
      console](https://console.aws.amazon.com//secretsmanager/ "https://console.aws.amazon.com//secretsmanager/").
   2. Click **Store a new secret**.
   3. Select **Other type of secrets**.
   4. For **Secret key/value**, in the first row, create a
      key `username` with value
      `admin`. Click on **+ Add
      row**.
   5. In the new row, create a key `password`. For
      value, type in the password you entered in Step 3 of _Create
      Your AWS Managed AD Directory_.
   6. Click on the **Next** button.
   7. Provide a secret name and description. Click
      **Next**.
   8. Click **Next**. Click
      **Store**.
   9. From the list of **Secrets** page, click on the
      secret you have just created.
   10. Save the ARN of the new secret for use in the following steps.
   11. You can proceed to the next step while your Active Directory is being
       created.

## Step 3: Verify and update your security group

In this step, you verify and update the rules for the security group that you're
using. For this, you can use the default security group that was created for your
VPC.

###### Verify and update security group.

You need to create or edit your security group to send data from and to the ports,
which are described in [Amazon VPC Security Groups](../../../fsx/latest/WindowsGuide/limit-access-security-groups.md#fsx-vpc-security-groups "../../../fsx/latest/WindowsGuide/limit-access-security-groups.md#fsx-vpc-security-groups") in the _FSx for Windows File Server User
Guide_. You can do this by creating the security group inbound rule
shown in the first row of the following table of inbound rules. This rule allows
inbound traffic from network interfaces (and their associated instances) that are
assigned to the security group. All of the cloud resources you create are within the
same VPC and attached to the same security group. Therefore, this rule allows
traffic to be sent to and from the FSx for Windows File Server file system, Active Directory, and
ECS instance as required. The other inbound rules allow traffic to serve the website
and RDP access for connecting to your ECS instance.

The following table shows which security group inbound rules are required for this
tutorial.

| Type        | Protocol | Port range | Source                 |
| ----------- | -------- | ---------- | ---------------------- |
| All traffic | All      | All        | `sg-securitygroup`     |
| HTTPS       | TCP      | 443        | 0.0.0.0/0              |
| RDP         | TCP      | 3389       | your laptop IP address |

The following table shows which security group outbound rules are required for
this tutorial.

| Type        | Protocol | Port range | Destination |
| ----------- | -------- | ---------- | ----------- |
| All traffic | All      | All        | 0.0.0.0/0   |

1. Open the [EC2 console](https://console.aws.amazon.com//ec2/ "https://console.aws.amazon.com//ec2/")
   and select **Security Groups** from the left-hand menu.
2. From the list of security groups now displayed, select check the check-box to
   the left of the security group that you are using for this tutorial.

Your security group details are displayed. 3. Edit the inbound and outbound rules by selecting the **Inbound
rules** or **Outbound rules** tabs and choosing
the **Edit inbound rules** or **Edit outbound
rules** buttons. Edit the rules to match those displayed in the
preceding tables. After you create your EC2 instance later on in
this tutorial, edit the inbound rule RDP source with the public IP address of
your EC2 instance as described in [Connect
to your Windows instance using RDP](../../../AWSEC2/latest/UserGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/UserGuide/connecting_to_windows_instance.md") from the _Amazon EC2
User Guide_.

## Step 4: Create an FSx for Windows File Server file system

After your security group is verified and updated and your Active Directory is created
and is in the active status, create the FSx for Windows File Server file system in the same VPC as your
Active Directory. Use the following steps to create an FSx for Windows File Server file system for your
Windows tasks.

###### Create your first file system.

1. Open the [Amazon FSx console](https://console.aws.amazon.com//fsx/ "https://console.aws.amazon.com//fsx/").
2. On the dashboard, choose **Create file system** to start the
   file system creation wizard.
3. On the **Select file system type** page, choose
   **FSx for Windows File Server**, and then choose
   **Next**. The **Create file system** page
   appears.
4. In the **File system details** section, provide a name for
   your file system. Naming your file systems makes it easier to find and manage
   your them. You can use up to 256 Unicode characters. Allowed characters are
   letters, numbers, spaces, and the special characters plus sign (+). minus sign
   (-), equal sign (=), period (.), underscore (\_), colon (:), and forward slash
   (/).
5. For **Deployment type** choose **Single-AZ**
   to deploy a file system that is deployed in a single Availability Zone.
   _Single-AZ 2_ is the latest generation of single
   Availability Zone file systems, and it supports SSD and HDD storage.
6. For **Storage type**, choose
   **HDD**.
7. For **Storage capacity**, enter the minimum storage capacity.
8. Keep **Throughput capacity** at its default
   setting.
9. In the **Network & security** section, choose the same
   Amazon VPC that you chose for your Directory Service directory.
10. For **VPC Security Groups**, choose the security group that
    you verified in _Step 3: Verify and update your security
    group_.
11. For **Windows authentication**, choose **AWS
    Managed Microsoft Active Directory**, and then choose your Directory Service
    directory from the
    list.
12. For **Encryption**, keep the default **Encryption
    key** setting of **aws/fsx (default)**.
13. Keep the default settings for **Maintenance
    preferences**.
14. Click on the **Next** button.
15. Review the file system configuration shown on the **Create file
    system** page. For your reference, note which file system settings
    you can modify after file system is created. Choose **Create file
    system**.
16. Note the file system ID. You will need to use it in a later step.

You can go on to the next steps to create a cluster and EC2
instance while the FSx for Windows File Server file system is being created.

## Step 5: Create an Amazon ECS cluster

###### Create a cluster using the Amazon ECS console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. From the navigation bar, select the Region to use.
3. In the navigation pane, choose **Clusters**.
4. On the **Clusters** page, choose **Create
   cluster**.
5. Under **Cluster configuration**, for **Cluster
   name**, enter **windows-fsx-cluster**.
6. Expand **Infrastructure**, clear AWS Fargate (serverless)
   and then select **Amazon EC2 instances**.
   1. To create a Amazon EC2 Auto Scaling group, from **Auto Scaling group
      (ASG)**, select **Create new group**, and
      then provide the following details about the group:
      - For **Operating system/Architecture**, choose
        **Windows Server 2019 Core**.
      - For **EC2 instance type**, choose t2.medium
        or t2.micro.

7. Choose **Create**.

## Step 6: Create an Amazon ECS optimized Amazon EC2

instance

Create an Amazon ECS Windows container instance.

###### To create an Amazon ECS instance

1. Use the `aws ssm get-parameters` command to retrieve the AMI name
   for the Region that hosts your VPC. For more information, see
   [Retrieving Amazon ECS-Optimized AMI metadata](retrieve-ecs-optimized_windows_AMI.md "retrieve-ecs-optimized_windows_AMI.md").
2. Use the Amazon EC2 console to launch the instance.
   1. Open the Amazon EC2 console at
      [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
   2. From the navigation bar, select the Region to
      use.
   3. From the **EC2 Dashboard**, choose **Launch
      instance**.
   4. For **Name**, enter a unique name.
   5. For **Application and OS Images (Amazon Machine
      Image)**, in the **search** field, enter
      the AMI name that you retrieved.
   6. For **Instance type**, choose t2.medium or
      t2.micro.
   7. For **Key pair (login)**, choose a key pair. If you
      don't specify a key pair, you
   8. Under **Network settings**, for
      **VPC** and **Subnet**, choose
      your VPC and a public subnet.
   9. Under **Network settings**, for **Security
      group**, choose an existing security group, or create a new
      one. Ensure that the security group you choose has the inbound and
      outbound rules defined in [Prerequisites for the tutorial](#wfsx-prerequisites "#wfsx-prerequisites")
   10. Under **Network settings**, for **Auto-assign
       Public IP**, select **Enable**.
   11. Expand **Advanced details**, and then for
       **Domain join directory**, select the ID of the
       Active Directory that you created. This option domain joins your AD when
       the EC2 instance is launched.
   12. Under **Advanced details**, for **IAM
       instance profile** , choose
       **ecsInstanceRole**.
   13. Configure your Amazon ECS container instance with the following user data.
       Under **Advanced Details**, paste the following script
       into the **User data** field, replacing
       `cluster_name` with the name of your
       cluster.

   ```
   <powershell>
   Initialize-ECSAgent -Cluster `windows-fsx-cluster` -EnableTaskIAMRole
   </powershell>
   ```

   14. When you are ready, select the acknowledgment field, and then choose
       **Launch Instances**.
   15. A confirmation page lets you know that your instance is launching.
       Choose **View Instances** to close the confirmation
       page and return to the console.

3. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
4. In the navigation pane, choose **Clusters**, and then choose
   **windows-fsx-cluster**.
5. Choose the **Infrastructure** tab and verify that your
   instance has been registered in the **windows-fsx-cluster**
   cluster.

## Step 7: Register a Windows task

definition

Before you can run Windows containers in your Amazon ECS cluster, you must register a task
definition. The following task definition example displays a simple web page. The task launches two containers that have access to
the FSx file system. The first container writes an HTML file to the file system. The
second container downloads the HTML file from the file system and serves the
webpage.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Task definitions**.
3. Choose **Create new task definition**, **Create new
   task definition with JSON**.
4. In the JSON editor box, replace the values for your task execution role and
   the details about your FSx file system and then choose
   **Save**.

```
{
    "containerDefinitions": [
        {
            "entryPoint": [
                "powershell",
                "-Command"
            ],
            "portMappings": [],
            "command": ["New-Item -Path C:\\fsx-windows-dir\\index.html -ItemType file -Value '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>It Works!</h2> <p>You are using Amazon FSx for Windows File Server file system for persistent container storage.</p>' -Force"],
            "cpu": 512,
            "memory": 256,
            "image": "mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019",
            "essential": false,
            "name": "container1",
            "mountPoints": [
                {
                    "sourceVolume": "fsx-windows-dir",
                    "containerPath": "C:\\fsx-windows-dir",
                    "readOnly": false
                }
            ]
        },
        {
            "entryPoint": [
                "powershell",
                "-Command"
            ],
            "portMappings": [
                {
                    "hostPort": 443,
                    "protocol": "tcp",
                    "containerPort": 80
                }
            ],
            "command": ["Remove-Item -Recurse C:\\inetpub\\wwwroot\\* -Force; Start-Sleep -Seconds 120; Move-Item -Path C:\\fsx-windows-dir\\index.html -Destination C:\\inetpub\\wwwroot\\index.html -Force; C:\\ServiceMonitor.exe w3svc"],
            "mountPoints": [
                {
                    "sourceVolume": "fsx-windows-dir",
                    "containerPath": "C:\\fsx-windows-dir",
                    "readOnly": false
                }
            ],
            "cpu": 512,
            "memory": 256,
            "image": "mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019",
            "essential": true,
            "name": "container2"
        }
    ],
    "family": "fsx-windows",
    "executionRoleArn": "arn:aws:iam::111122223333:role/ecsTaskExecutionRole",
    "volumes": [
        {
            "name": "fsx-windows-dir",
            "fsxWindowsFileServerVolumeConfiguration": {
                "fileSystemId": "fs-0eeb5730b2EXAMPLE",
                "authorizationConfig": {
                    "domain": "example.com",
                    "credentialsParameter": "arn:arn-1234"
                },
                "rootDirectory": "share"
            }
        }
    ]
}
```

## Step 8: Run a task and view the results

Before running the task, verify that the status of your FSx for Windows File Server file system is
**Available**. After it is available, you can run a task using the
task definition that you created. The task starts out by creating containers that
shuffle an HTML file between them using the file system. After the shuffle, a web server
serves the simple HTML page.

###### Note

You might not be able to connect to the website from within a VPN.

###### Run a task and view the results with the Amazon ECS console.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**, and then choose
   **windows-fsx-cluster**.
3. Choose the **Tasks** tab, and then choose **Run new
   task**.
4. For **Launch Type**, choose **EC2**.
5. Under Deployment configuration, for **Task Definition**,
   choose the **fsx-windows**, and then choose
   **Create**.
6. When your task status is **RUNNING**, choose the task
   ID.
7. Under **Containers**, when the container1 status is
   **STOPPED**, select container2 to view the container's
   details.
8. Under **Container details for container2**, select
   **Network bindings** and then click on the external IP
   address that is associated with the container. Your browser will open and
   display the following message.

```
Amazon ECS Sample App
It Works!
You are using Amazon FSx for Windows File Server file system for persistent container storage.
```

###### Note

It may take a few minutes for the message to be displayed. If you don't
see this message after a few minutes, check that you aren't running in a VPN
and make sure that the security group for your container instance allows
inbound network HTTP traffic on port 443.

## Step 9: Clean up

###### Note

It takes 20 to 45 minutes to delete the FSx for Windows File Server file system or the AD. You
must wait until the FSx for Windows File Server file system delete operations are complete before
starting the AD delete operations.

###### Delete FSx for Windows File Server file system.

1. Open the [Amazon FSx console](https://console.aws.amazon.com//fsx/ "https://console.aws.amazon.com//fsx/")
2. Choose the radio button to the left of the FSx for Windows File Server file system that you
   just created.
3. Choose **Actions**.
4. Select **Delete file system**.

###### Delete AD.

1. Open the [Directory Service
   console](https://console.aws.amazon.com//directoryservicev2/ "https://console.aws.amazon.com//directoryservicev2/").
2. Choose the radio button to the left of the AD you just created.
3. Choose **Actions**.
4. Select **Delete directory**.

###### Delete the cluster.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**, and then choose
   **windows-fsx-cluster**.
3. Choose **Delete cluster**.
4. Enter the phrase and then choose **Delete**.

###### Terminate EC2 instance.

1. Open the [Amazon EC2 console](https://console.aws.amazon.com//ec2/ "https://console.aws.amazon.com//ec2/").
2. From the left-hand menu, select **Instances**.
3. Check the box to the left of the EC2 instance you created.
4. Click the **Instance state**, **Terminate
   instance**.

###### Delete secret.

1. Open the [Secrets Manager
   console](https://console.aws.amazon.com//secretsmanager/ "https://console.aws.amazon.com//secretsmanager/").
2. Select the secret you created for this walk through.
3. Click **Actions**.
4. Select **Delete secret**.
