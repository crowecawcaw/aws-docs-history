

# Prerequisites
<a name="prerequisites"></a>

**Topics**
+ [Create an AWS account with an administrative user](#aws-account)
+ [Create an Amazon EC2 SSH key pair](#create-ssh-key-pair)
+ [Increase service quotas](#increase-service-quotas)
+ [Create a Cognito user pool (optional)](#create-cognito-user-pool)
+ [Create a custom domain (optional)](#create-public-domain)
+ [Create a domain (GovCloud only)](#create-domain-govcloud)
+ [Provide external resources](#external-resources)
+ [Configure LDAPS in your environment (optional)](#configure-ldaps)
+ [Set up a Service Account for Microsoft Active Directory](#service-account-ms-ad)
+ [Configure a private VPC (optional)](#private-vpc)

## Create an AWS account with an administrative user
<a name="aws-account"></a>

You must have an AWS account with an administrative user:

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup).

1. Follow the online instructions.

   Part of the sign-up procedure involves receiving a phone call or text message and entering a verification code on the phone keypad.

   When you sign up for an AWS account, an *AWS account root user* is created. The root user has access to all AWS services and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks).

## Create an Amazon EC2 SSH key pair
<a name="create-ssh-key-pair"></a>

If you do not have an Amazon EC2 SSH key pair, you must create one. For more information, see [Create a key pair using Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html) in the *Amazon EC2 User Guide*. 

## Increase service quotas
<a name="increase-service-quotas"></a>

As a best practice, [increase the service quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) for:
+ [ Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html)
  + Increase the Elastic IP address quota per NAT gateway from five to eight.
  + Increase the NAT gateways per Availability Zone from five to ten.
+ [ Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) 
  + Increase the EC2-VPC Elastic IPs from five to ten.

Your AWS account has default quotas for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased. For more information, see [Quotas for AWS services in this product](plan-your-deployment.md#quotas-for-aws-services-in-this-product).

## Create a Cognito user pool (optional)
<a name="create-cognito-user-pool"></a>

You have the option to import an existing Cognito User Pool for user and client authentication when you install RES. Otherwise, RES will create a new Cognito User Pool automatically. The pre-existing user pool must have the following sign-up custom attributes:


| Name | Type | Min value/length | Max value/length | Mutable | 
| --- | --- | --- | --- | --- | 
| custom:aws\_region | String |  |  | TRUE | 
| custom:cluster\_name | String |  |  | TRUE | 
| custom:password\_last\_set  | Number |  |  | TRUE | 
| custom:password\_max\_age | Number |  |  | TRUE | 
| custom:uid | Number | 2000200001 | 4294967294 | TRUE | 

## Create a custom domain (optional)
<a name="create-public-domain"></a>

As a best practice, use a custom domain for the product for a user-friendly URL. You can provide a custom domain and *optionally* provide a certificate for it. 

There is a process in the External Resources stack to create a certificate for a custom domain which you provide. You can skip the steps here if you have a domain and want to use the certificate generation capabilities of the External Resources stack.

Or, follow these steps to register a domain using Amazon Route 53 and import a certificate for the domain using AWS Certificate Manager.

1. Follow the directions to [register a domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html#register_new_console) with Route 53. You should receive a confirmation email.

1. Retrieve the hosted zone for your domain. Route 53 creates this automatically.

   1. Open the Route 53 console.

   1. Choose **Hosted zones** from the left navigation.

   1. Open the hosted zone created for your domain name and copy the **Hosted zone ID**.

1. Open AWS Certificate Manager and follow these steps to [request a domain certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html). Ensure you are in the Region where you plan to deploy the solution.

1. Choose **List certificates** from the navigation, and find your certificate request. The request should be pending.

1. Choose your **Certificate ID** to open the request.

1. From the **Domains** section, choose **Create records in Route 53**. It will take approximately ten minutes for the request to process.

1. Once the certificate is issued, copy the **ARN** from the **Certificate status** section.

## Create a domain (GovCloud only)
<a name="create-domain-govcloud"></a>

If you are deploying in an AWS GovCloud Region and you are using a custom domain for Research and Engineering Studio, you must complete these prerequisite steps.

1. Deploy the [ Certificate CloudFormation stack](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/security/public_certs/assets/main.yaml) in the commercial-partition AWS Account where the public hosted domain was created.

1. From the **Certificate CloudFormation Outputs**, find and note the `CertificateARN` and `PrivateKeySecretARN`. 

1. In the GovCloud partition account, create a secret with the value of the `CertificateARN` output. Note the new secret ARN and add two tags to the secret so `vdc-gateway` can access the secret value: 

   1. res:ModuleName = virtual-desktop-controller 

   1. res:EnvironmentName = [environment name] (This could be res-demo.) 

1. In the GovCloud partition account, create a secret with the value of the `PrivateKeySecretARN` output. Note the new secret ARN and add two tags to the secret so `vdc-gateway` can access the secret value: 

   1. res:ModuleName = virtual-desktop-controller

   1. res:EnvironmentName = [environment name] (This could be res-demo.)

## Provide external resources
<a name="external-resources"></a>

Research and Engineering Studio on AWS expects the following external resources to exist when it is deployed.
+ **Networking (VPC, Public Subnets, and Private Subnets)**

  This is where you will run the EC2 instances used to host the RES environment, the Active Directory (AD), and shared storage.
+ **Storage (Amazon EFS)**

  The storage volumes contain files and data needed for the virtual desktop infrastructure (VDI).
+ **Directory service (AWS Directory Service for Microsoft Active Directory) **

  The directory service authenticates users to the RES environment.
+ **A secret that contains the Active Directory service account username and password formatted as a key-value pair (username, password)**

  Research and Engineering Studio accesses [secrets](secrets-management.md) that you provide, including the service account password, using [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html).

**Warning**  
You must provide a valid email address for all Active Directory (AD) users whom you want to sync.

**Tip**  
If you are deploying a demo environment and do not have these external resources available, you can use AWS High Performance Compute recipes to generate the external resources. See the following section, [Create external resources](create-external-resources.md), to deploy resources in your account.   
For demo deployments in an AWS GovCloud Region, you must complete the prerequisite steps in [Create a domain (GovCloud only)](#create-domain-govcloud).

## Configure LDAPS in your environment (optional)
<a name="configure-ldaps"></a>

If you plan to use LDAPS communication in your environment, you must complete these steps to create and attach certificates to the AWS Managed Microsoft AD (AD) domain controller to provide communication between AD and RES. 

1. Follow the steps provided in [How to enable server-side LDAPS for your AWS Managed Microsoft AD](https://aws.amazon.com/blogs/security/how-to-enable-ldaps-for-your-aws-microsoft-ad-directory/). You can skip this step if you have already enabled LDAPS.

1. After confirming that LDAPS is configured on the AD, export the AD certificate:

   1. Go to your Active Directory server.

   1. Open PowerShell as an administrator.

   1. Run `certmgr.msc` to open the certificate list.

   1. Open the certificate list by first opening the Trusted Root Certification Authorities and then Certificates.

   1. Select and hold (or right-click) the certificate with the same name as your AD server and choose **All tasks** and then **Export**.

   1. Select **Base-64 encoded X.509 (.CER)** and choose **Next**.

   1. Select a directory and then choose **Next**.

1. Create a secret in AWS Secrets Manager:

   When creating your Secret in the Secrets Manager, choose **Other type of secrets** under **secret type** and paste your PEM encoded certificate in the **Plaintext** field. 

1. Note the ARN created and input it as the `DomainTLSCertificateSecretARN` parameter in [Step 1: Launch the product](launch-the-product.md).

## Set up a Service Account for Microsoft Active Directory
<a name="service-account-ms-ad"></a>

If you choose Microsoft Active Directory (AD) as the identity source for RES, you have a Service Account in your AD that allows for programmatic access. You must pass a secret with the Service Account's credentials as part of your RES installation. The secret must have the format shown here.

![Example username and password format](http://docs.aws.amazon.com/res/latest/ug/images/res-secret-value-example.png)


Also note that the `username` field doesn't support NT-style logon names of the format `DOMAIN\username`.

The Service Account is responsible for the following functions:
+ Sync users from the AD: RES must sync users from the AD to allow them to log in to the web portal. The syncing process uses the service account to query the AD using LDAP(s) to determine which users and groups are available.
+ Join the AD domain: this is an optional operation for Linux virtual desktops and infrastructure hosts where the instance joins the AD domain. In RES, this is controlled with the `DisableADJoin` parameter. This parameter is set to False by default, which means that Linux virtual desktops will attempt to join the AD domain in the default configuration.
+ Connect to the AD: Linux virtual desktops and infrastructure hosts will connect to the AD domain if they do not join it (`DisableADJoin` = True). For this functionality to work, the Service Account also needs read access for users and groups in the `UsersOU` and `GroupsOU`.

The service account requires the following permissions:
+ To sync users and connect to AD → Read access for users and groups in the `UsersOU` and `GroupsOU`.
+ To join the AD domain → create `Computer` objects in the `ComputersOU`.

The script at [ https://github.com/aws-samples/aws-hpc-recipes/blob/main/recipes/res/res\_demo\_env/assets/service\_account.ps1](https://github.com/aws-samples/aws-hpc-recipes/blob/main/recipes/res/res_demo_env/assets/service_account.ps1) provides an example of how to grant proper Service Account permissions. You can modify it based on your own AD.

## Configure a private VPC (optional)
<a name="private-vpc"></a>

Deploying Research and Engineering Studio in an isolated VPC offers enhanced security to meet your organization's compliance and governance requirements. However, the standard RES deployment relies on internet access for installing dependencies. To install RES in a private VPC, you will need to satisfy the following prerequisites:

**Topics**
+ [Prepare Amazon Machine Images (AMIs)](#prep-ami)
+ [Set up VPC endpoints](#private-vpc-endpoints)
+ [Connect to services without VPC endpoints](#connect-services-without-endpoints)
+ [Set private VPC deployment parameters](#vpc-deployment-parameters)

### Prepare Amazon Machine Images (AMIs)
<a name="prep-ami"></a>

1. Download the dependencies at [ https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/latest/res-installation-scripts.tar.gz](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/latest/res-installation-scripts.tar.gz). To deploy in an isolated VPC, the RES infrastructure requires the availability of dependencies without having public internet access.
**Important**  
Replace **latest** in the download URI with with the exact version number (for example, **2025.06**) if your RES environment version is not the latest.

1. Create an IAM role with Amazon S3 read-only access and trusted identity as Amazon EC2.

   1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

   1. From **Roles**, choose **Create role**.

   1. On the **Select trusted entity** page:
      + Under **Trusted entity type**, choose AWS service.
      + For **Use case** under **Service or use case**, choose **EC2** and choose **Next**. 

   1. On **Add permissions**, select the following permission policies and then choose **Next**:
      + AmazonS3ReadOnlyAccess
      + AmazonSSMManagedInstanceCore
      + EC2InstanceProfileForImageBuilder

   1. Add a **Role name** and **Description**, and then choose **Create role**.

1. Create the EC2 image builder component:

   1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder](https://console.aws.amazon.com/imagebuilder).

   1. Under **Saved resources**, choose **Components** and choose **Create component**.

   1. On the **Create component** page, enter the following details:
      + For **Component type**, choose **Build**.
      + For **Component details** choose:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/res/latest/ug/prerequisites.html)

   1. On the **Create component** page, choose **Define document content**.

      1. Before entering the definition document content, you will need a file URI for the tar.gz file. Upload the tar.gz file provided by RES to an Amazon S3 bucket and copy the file's URI from the bucket properties.

      1. Enter the following:
**Note**  
`AddEnvironmentVariables` is optional, and you may remove it if you do not require custom environment variables in your infrastructure hosts.  
If you are setting up `http_proxy` and `https_proxy` environment variables, the `no_proxy` parameters are required to prevent the instance from using proxy to query localhost, instance metadata IP addresses, and the services that support VPC endpoints.

         ```
         #  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
         #
         #  Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
         #  with the License. A copy of the License is located at
         #
         #      http://www.apache.org/licenses/LICENSE-2.0
         #
         #  or in the 'license' file accompanying this file. This file is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES
         #  OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions
         #  and limitations under the License.
         name: research-and-engineering-studio-infrastructure
         description: An RES EC2 Image Builder component to install required RES software dependencies for infrastructure hosts.
         schemaVersion: 1.0
         
         parameters:
           - AWSRegion:
               type: string
               description: RES Environment AWS Region
         phases:
           - name: build
             steps:
                - name: DownloadRESInstallScripts
                  action: S3Download
                  onFailure: Abort
                  maxAttempts: 3
                  inputs:
                     - source: '{{<s3 tar.gz file uri>}}'
                       destination: '/root/bootstrap/res-installation-scripts/res-installation-scripts.tar.gz'
                - name: RunInstallScript
                  action: ExecuteBash
                  onFailure: Abort
                  maxAttempts: 3
                  inputs:
                     commands:
                         - 'cd /root/bootstrap/res-installation-scripts'
                         - 'tar -xf res-installation-scripts.tar.gz'
                         - 'cd scripts/infrastructure-host'
                         - '/bin/bash install.sh'
                - name: AddEnvironmentVariables
                  action: ExecuteBash
                  onFailure: Abort
                  maxAttempts: 3
                  inputs:
                     commands:
                         - |
                           echo -e "
                           http_proxy=http://{{<ip>}}:{{<port>}}
                           https_proxy=http://{{<ip>}}:{{<port>}}
                           no_proxy=127.0.0.1,169.254.169.254,169.254.170.2,localhost,{{ AWSRegion }}.res,{{ AWSRegion }}.vpce.amazonaws.com,{{ AWSRegion }}.elb.amazonaws.com,s3.{{ AWSRegion }}.amazonaws.com,s3.dualstack.{{ AWSRegion }}.amazonaws.com,ec2.{{ AWSRegion }}.amazonaws.com,ec2.{{ AWSRegion }}.api.aws,ec2messages.{{ AWSRegion }}.amazonaws.com,ssm.{{ AWSRegion }}.amazonaws.com,ssmmessages.{{ AWSRegion }}.amazonaws.com,kms.{{ AWSRegion }}.amazonaws.com,secretsmanager.{{ AWSRegion }}.amazonaws.com,sqs.{{ AWSRegion }}.amazonaws.com,elasticloadbalancing.{{ AWSRegion }}.amazonaws.com,sns.{{ AWSRegion }}.amazonaws.com,logs.{{ AWSRegion }}.amazonaws.com,logs.{{ AWSRegion }}.api.aws,elasticfilesystem.{{ AWSRegion }}.amazonaws.com,fsx.{{ AWSRegion }}.amazonaws.com,dynamodb.{{ AWSRegion }}.amazonaws.com,api.ecr.{{ AWSRegion }}.amazonaws.com,.dkr.ecr.{{ AWSRegion }}.amazonaws.com,kinesis.{{ AWSRegion }}.amazonaws.com,.data-kinesis.{{ AWSRegion }}.amazonaws.com,.control-kinesis.{{ AWSRegion }}.amazonaws.com,events.{{ AWSRegion }}.amazonaws.com,cloudformation.{{ AWSRegion }}.amazonaws.com,sts.{{ AWSRegion }}.amazonaws.com,application-autoscaling.{{ AWSRegion }}.amazonaws.com,monitoring.{{ AWSRegion }}.amazonaws.com,ecs.{{ AWSRegion }}.amazonaws.com,.execute-api.{{ AWSRegion }}.amazonaws.com
                            " >> /etc/environment
         ```

   1. Choose **Create component**.

1. Create an Image Builder image recipe.

   1. On the **Create recipe** page, enter the following:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/res/latest/ug/prerequisites.html)

   1. Choose **Create recipe**.

1. Create Image Builder infrastructure configuration.

   1. Under **Saved resources**, choose **Infrastructure configurations**.

   1. Choose **Create infrastructure configuration**.

   1. On the **Create infrastructure configuration** page, enter the following:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/res/latest/ug/prerequisites.html)

   1. Choose **Create infrastructure configuration**.

1. Create a new EC2 Image Builder pipeline:

   1. Go to **Image pipelines**, and choose **Create image pipeline**.

   1. On the **Specify pipeline details** page, enter the following and choose **Next**:
      + Pipeline name and optional description
      + For **Build schedule**, set a schedule or choose **Manual** if you want to start the AMI baking process manually.

   1. On the **Choose recipe** page, choose **Use existing recipe** and enter the **Recipe name** created previously. Choose **Next**.

   1. On the **Define image process** page, select the default workflows and choose **Next**.

   1. On the **Define infrastructure configuration** page, choose **Use existing infrastructure configuration** and enter the name of the previously created infrastructure configuration. Choose **Next**.

   1. On the **Define distribution settings** page, consider the following for your selections:
      + The output image must reside in the same region as the deployed RES environment, so that RES can properly launch infrastructure host instances from it. Using service defaults, the output image will be created in the region where the EC2 Image Builder service is being used.
      + If you want to deploy RES in multiple regions, you can choose **Create a new distribution settings** and add more regions there.

   1. Review your selections and choose **Create pipeline**.

1. Run the EC2 Image Builder pipeline:

   1. From **Image pipelines**, find and select the pipeline you created.

   1. Choose **Actions**, and select **Run pipeline**.

      The pipeline may take approximately 45 minutes to an hour to create an AMI image.

1. Note the AMI ID for the generated AMI and use it as the input for the InfrastructureHostAMI parameter in [Step 1: Launch the product](launch-the-product.md).

### Set up VPC endpoints
<a name="private-vpc-endpoints"></a>

 To deploy RES and launch virtual desktops, AWS services require access to your private subnet. You must set up VPC endpoints to provide the required access, and you will need to repeat these steps for each endpoint. 

1. If endpoints have not previously been configured, follow the instructions provided in [ Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html).

1. Select one private subnet in each of the two availability zones.



- **[ Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-vpc-endpoints.html)**
  - com.amazonaws.{{region}}.application-autoscaling

- **[AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-vpce-bucketnames.html)**
  - com.amazonaws.{{region}}.cloudformation

- **[ Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-and-interface-VPC.html)**
  - com.amazonaws.{{region}}.monitoring

- **[ Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.html)**
  - com.amazonaws.{{region}}.logs

- **[Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/privatelink-interface-endpoints.html)**
  - com.amazonaws.{{region}}.dynamodb (Requires gateway endpoint)

- **[Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interface-vpc-endpoints.html)**
  - com.amazonaws.{{region}}.ec2

- **[Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/vpc-endpoints.html)**
  - com.amazonaws.{{region}}.ecr.api
  - com.amazonaws.{{region}}.ecr.dkr

- **[Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/efs-vpc-endpoints.html)**
  - com.amazonaws.{{region}}.elasticfilesystem

- **[Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/load-balancer-vpc-endpoints.html)**
  - com.amazonaws.{{region}}.elasticloadbalancing

- **[Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-related-service-vpc.html)**
  - com.amazonaws.{{region}}.events

- **Amazon FSx**
  - com.amazonaws.{{region}}.fsx

- **[AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/kms-vpc-endpoint.html)**
  - com.amazonaws.{{region}}.kms

- **[Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/vpc.html)**
  - com.amazonaws.{{region}}.kinesis-streams

- **[AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc-endpoints.html)**
  - com.amazonaws.{{region}}.lambda

- **[Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html)**
  - com.amazonaws.{{region}}.s3 (Requires a gateway endpoint that is created by default in RES.)<br />Additional Amazon S3 interface endpoints are required for cross-mounting buckets in an isolated environment. See [ Accessing Amazon Simple Storage Service interface endpoints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html#accessing-s3-interface-endpoints).

- **[AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html)**
  - com.amazonaws.{{region}}.secretsmanager

- **[ Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)**
  - com.amazonaws.{{region}}.ecs

- **[ Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/send-email-set-up-vpc-endpoints.html)**
  - com.amazonaws.{{region}}.email-smtp (Not supported in the following Availability Zones: use-1-az2, use1-az3, use1-az5, usw1-az2, usw2-az4, apne2-az4, cac1-az3, and cac1-az4.)

- **[AWS Security Token Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_sts_vpce.html)**
  - com.amazonaws.{{region}}.sts

- **[Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-vpc.html)**
  - com.amazonaws.{{region}}.sns

- **[ Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-internetwork-traffic-privacy.html#sqs-vpc-endpoints)**
  - com.amazonaws.{{region}}.sqs

- **[AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-setting-up-vpc.html)**
  - com.amazonaws.{{region}}.ec2messages
  - com.amazonaws.{{region}}.ssm
  - com.amazonaws.{{region}}.ssmmessages



### Connect to services without VPC endpoints
<a name="connect-services-without-endpoints"></a>

To integrate with services that do not support VPC endpoints, you can set up a proxy server in a public subnet of your VPC. Follow these steps to create a proxy server with the minimum necessary access for a Research and Engineering Studio deployment using AWS Identity Center as your identity provider.

1. Launch a Linux instance in the public subnet of the VPC you will use for your RES deployment.
   + Linux family – Amazon Linux 2 or Amazon Linux 3
   + Architecture – x86
   + Instance type – t2.micro or higher
   + Security group – TCP on port 3128 from 0.0.0.0/0

1. Connect to the instance to set up a proxy server.

   1. Open the http connection.

   1. Allow connection to the following domains from all relevant subnets:
      + .amazonaws.com (for generic AWS services)
      + .amazoncognito.com (for Amazon Cognito)
      + .awsapps.com (for Identity Center)
      + .signin.aws (for Identity Center)
      + .amazonaws-us-gov.com (for Gov Cloud)

   1. Deny all other connections.

   1. Activate and start the proxy server.

   1. Note the PORT on which the proxy server listens.

1. Configure your route table to allow access to the proxy server.

   1. Go to your VPC console and identify the route tables for the subnets you will be using for Infrastructure Hosts and VDI hosts.

   1. Edit route table to allow all incoming connections to go to the proxy server instance created in the previous steps.

   1. Do this for route tables for all the subnets (without internet access) which you are going to use for Infrastructure/VDIs.

1. Modify the security group of the proxy server EC2 instance and make sure it allows inbound TCP connections on the PORT on which the proxy server is listening.

### Set private VPC deployment parameters
<a name="vpc-deployment-parameters"></a>

In [Step 1: Launch the product](launch-the-product.md), you are expected to input certain parameters in the CloudFormation template. Be sure to set the following parameters as noted to successfully deploy into the private VPC you just configured.


| Parameter | Input | 
| --- |--- |
| InfrastructureHostAMI | Use the infrastructure AMI ID created in [Prepare Amazon Machine Images (AMIs)](#prep-ami). | 
| IsLoadBalancerInternetFacing | Set to false. | 
| LoadBalancerSubnets | Choose private subnets without internet access. | 
| InfrastructureHostSubnets | Choose private subnets without internet access. | 
| VdiSubnets | Choose private subnets without internet access. | 
| ClientIP | You can choose your VPC CIDR to allow access for all VPC IP addresses. | 
| HttpProxy | Example: http://10.1.2.3:123 | 
| HttpsProxy | Example: http://10.1.2.3:123 | 
| NoProxy | Example:<pre>127.0.0.1,169.254.169.254,169.254.170.2,localhost,us-east-1.res,us-east-1.vpce.amazonaws.com,us-east-1.elb.amazonaws.com,s3.us-east-1.amazonaws.com,s3.dualstack.us-east-1.amazonaws.com,ec2.us-east-1.amazonaws.com,ec2.us-east-1.api.aws,ec2messages.us-east-1.amazonaws.com,ssm.us-east-1.amazonaws.com,ssmmessages.us-east-1.amazonaws.com,kms.us-east-1.amazonaws.com,secretsmanager.us-east-1.amazonaws.com,sqs.us-east-1.amazonaws.com,elasticloadbalancing.us-east-1.amazonaws.com,sns.us-east-1.amazonaws.com,logs.us-east-1.amazonaws.com,logs.us-east-1.api.aws,elasticfilesystem.us-east-1.amazonaws.com,fsx.us-east-1.amazonaws.com,dynamodb.us-east-1.amazonaws.com,api.ecr.us-east-1.amazonaws.com,.dkr.ecr.us-east-1.amazonaws.com,kinesis.us-east-1.amazonaws.com,.data-kinesis.us-east-1.amazonaws.com,.control-kinesis.us-east-1.amazonaws.com,events.us-east-1.amazonaws.com,cloudformation.us-east-1.amazonaws.com,sts.us-east-1.amazonaws.com,application-autoscaling.us-east-1.amazonaws.com,monitoring.us-east-1.amazonaws.com,ecs.us-east-1.amazonaws.com,.execute-api.us-east-1.amazonaws.com </pre> | 