AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Configuring container deployment

This topic contains information about the files that are used for configuring deployment of
application containers.

###### Container deployment files

- [deployment.json file](#config-deployment-json "#config-deployment-json")

## deployment.json file

When you run the **[containerize](cmd-containerize.md "cmd-containerize.md")** command, a
`deployment.json` file is created for the application specified
in the `--application-id` parameter. The **generate
app-deployment** command uses this file, along with others, to generate
application deployment artifacts. All of the fields in this file are configurable as
needed so that you can customize your application container deployment before running
the **generate app-deployment** command.

###### Important

The `deployment.json` file includes sections for both Amazon ECS and
Amazon EKS. If your application is suitable for App Runner, there is a section for that too.
Set the Boolean value deployment flag for the section that matches your target
container management service to **true**. Set the other
flags to **false**. The flag to deploy to Amazon ECS is
`createEcsArtifacts`, the flag to deploy to Amazon EKS is
`createEksArtifacts`, and the flag to deploy to App Runner is
`createAppRunnerArtifacts`.

The application `deployment.json` file includes the following
content. While all fields are configurable, the following fields should not be changed:
`a2CTemplateVersion`, `applicationId`, and
`imageName`. For key-value pairs that do not apply to your deployment,
set string values to an empty string, numeric values to zero, and Boolean values to
false.

- exposedPorts (array of objects, required) – An
  array of JSON objects representing the ports that should be exposed when the container is
  running. Each object consists of the following fields:
  - localPort (number) – A port to expose for
    container communication.
  - protocol (string) – The
    application protocol for the exposed port, for example, "http".

- environment (array of objects) –
  Environment variables to be passed on to the target container management
  deployment. For Amazon ECS deployments, the key-value pairs update the Amazon ECS task
  definition. For Amazon EKS deployments, the key-value pairs update the Kubernetes
  `deployment.yml` file.
- ecrParameters (object) – Contains parameters needed
  to register application container images in Amazon ECR.
  - ecrRepoTag (string, required) – The version
    tag to use for registering an application container image in Amazon ECR.

- ecsParameters (object) – Contains
  parameters needed for deployment to Amazon ECS. _The `createEcsArtifacts`
  parameter is always required. Other parameters in this section that are
  marked as required apply only to Amazon ECS deployment._
  - createEcsArtifacts (Boolean, required) – A flag
    that indicates if you are targeting Amazon ECS for deployment.
  - ecsFamily (string, required) – An
    ID for the Amazon ECS family in the Amazon ECS task definition. We recommend
    setting this value to the application ID.
  - cpu (number, required\*)
    – The hard limit for the number of vCPUs to present for the task.
    When the task definition is registered, the number of CPU units is
    determined by multiplying the number of vCPUs by 1024.

  _\* This parameter is required for Linux containers, but is not
  supported for Windows containers._
  - memory (number or string, required\*)
    – The hard limit of memory (in MiB) to present to the task. You
    can express this value as an integer in the Amazon ECS task definition, using
    MiB, for example, 1024. You can also express the value as a string
    including the unit GB, for example, 1 GB. When the task definition is
    registered, a GB value is converted to an integer indicating the
    MiB.

  _\* This parameter is required for Linux containers, but is not
  supported for Windows containers._

  ###### Note

  In the Amazon ECS task definition, task size consists of the `cpu`
  and `memory` parameters. The configuration for task size,
  in part, depends on where your tasks are hosted – on an EC2
  instance, or in Fargate. For more information about setting the
  task size for your Amazon ECS task definition, see [Task definition parameters](../../../AmazonECS/latest/developerguide/task_definition_parameters.md#task_size "../../../AmazonECS/latest/developerguide/task_definition_parameters.md#task_size") in the
  _Amazon Elastic Container Service Developer Guide_.
  - dockerSecurityOption (string) –
    For .NET applications, this is the gMSA Credspec location value for the
    Amazon ECS task definition.
  - enableCloudwatchLogging (Boolean,
    required\*) – A flag that sets the Amazon ECS task definition to turn
    on CloudWatch logging for your Windows application container. _If set
    to true, the `enableLogging` field in the
    `analysis.json` file must have a valid
    value._

  _\* This parameter is required for Windows containers, but is not supported for
  Linux containers._
  - publicApp (Boolean, required) – A flag to
    configure the CloudFormation templates with a public endpoint for your application
    when it runs.
  - stackName (string, required) – A name to use
    as a prefix to your CloudFormation stack Amazon Resource Name (ARN). We recommend
    using the application ID for this.
  - resourceTags (array of objects) –
    Custom tags, expressed as key/value pairs that are added to resources
    during deployment. For Amazon ECS deployments, the key-value pairs update the
    Amazon ECS task definition.

  ###### Note

  An example tag is generated when the `deployment.json`
  file is created. If the example tag isn't removed or changed before
  deployment, it's ignored by default.
  - reuseResources (object) – Contains shared
    resource identifiers that can be used throughout your CloudFormation templates.
    - vpcId (string) – The VPC
      ID, if you want to bring your own VPC or to reuse an existing
      VPC that App2Container created for a prior deployment.
    - reuseExistingA2cStack (object)
      – Contains references so that you can reuse AWS CloudFormation
      resources that App2Container has already created.
      - cfnStackName (string) – The name or
        ID (ARN) of the CloudFormation stack created with App2Container for the containerized
        application.
      - microserviceUriPath (string) – Used
        to create application forwarding rules in your load balancer.

      ###### Note

      The load balancer does not strip off this prefix when it forwards
      traffic. Your application must be able to handle requests coming in
      with the prefix.

    - sshKeyPairName (string) – The name
      of the EC2 key pair to use for the instances that your container runs on.
    - acmCertificateArn (string)
      – The AWS Certificate Manager certificate ARN used to provide HTTPS
      connectivity to your Application Load Balancer.

    ###### Note

    The certificate can be imported or provisioned as follows:

        * To import an IIS certificate into ACM, see [How
         to import PFX-formatted certificates into AWS Certificate Manager using OpenSSL](https://aws.amazon.com/blogs/security/how-to-import-pfx-formatted-certificates-into-aws-certificate-manager-using-openssl/ "https://aws.amazon.com/blogs/security/how-to-import-pfx-formatted-certificates-into-aws-certificate-manager-using-openssl/").
        * To provision a certificate in ACM, see [Issuing and Managing Certificates](../../../acm/latest/userguide/gs.md "../../../acm/latest/userguide/gs.md")
         in the AWS Certificate Manager User Guide.

    If you use an HTTPS endpoint for your load balancer, this
    parameter is required. For more information about ACM, see
    [What is AWS Certificate Manager](../../../acm/latest/userguide.md "../../../acm/latest/userguide.md") in the
    AWS Certificate Manager User Guide.

  - gMSAParameters (object) – Contains parameters
    used by the CloudFormation template to create gMSA-related artifacts for .NET applications
    that are deployed on EC2 instances. The gMSAParameters are not valid for deployments to
    Fargate, and will generate an error when the **generate app-deployment**
    command runs.
    - domainSecretsArn (string)
      – The Secrets Manager ARN for the domain credentials to join
      the Amazon ECS nodes to gMSA Active Directory.
    - domainDNSName (string) –
      The DNS name of the gMSA Active Directory for Amazon ECS nodes to
      join.
    - domainNetBIOSName (string)
      – The NetBIOS name of the Active Directory for Amazon ECS
      nodes to join.
    - createGMSA (Boolean, required)
      – A flag to create a group Managed Service Account (gMSA)
      Active Directory security group and account, using the name
      supplied in the `gMSAName` field.
    - gMSAName (string) – The name of the
      gMSA Active Directory that the container should use for access.

  - deployTarget (string, required)
    – Identifies which Amazon ECS container launch type runs the task.
    Valid values depend on your application environment, as follows:
    - _.NET applications running on Windows_ –
      `ec2`, `fargate`.
    - _Java applications running on Linux_ –
      `fargate`.

  ###### Note

  The default value that is generated for the **deployTarget** parameter for .NET applications
  running on Windows is `ec2`. To deploy your application
  to Fargate, you can edit the `deployment.json`
  file, and change that value to `fargate`.

  If your .NET application meets the following criteria, you can deploy
  to Fargate.

      - The base operating system for your container is Windows 2019.
       If you are using a worker machine for containerization, this means
       that the worker machine must be running Windows 2019.
      - Your application must not use gMSA.

  - dependentApps (array of objects) –
    For complex Windows applications, this array of JSON objects contains identifying
    details for dependent applications. App2Container does not generate this array. For complex
    Windows applications that incorporate dependent applications, you must add details
    to this array for each dependent application. You can include up to two dependent
    applications in the array.
    - appId (string, required) – The
      application ID that App2Container generated for this dependent
      application.
    - privateRootDomain (string, required)
      – The private domain name that's used for creating the
      hosted zone.
    - dnsRecordName (string, required) –
      The DNS record name of the application. This is combined with the privateRootDomain
      to construct the endpoint for the dependent application.

- fireLensParameters (object) – Contains
  parameters needed to use FireLens with your Linux application to route your
  application logs for Amazon ECS tasks. _The `enableFireLensLogging`
  parameter is always required. Other parameters in this section that are marked
  as required apply only when FireLens is used for log routing._

###### Note

This section is not included for applications running on Windows.

    + enableFireLensLogging (Boolean, required)
     – A flag for using FireLens for Amazon ECS to configure application log
     routing for containers.
    + logDestinations (array of objects) –
     A list of unique target destinations for application log routing. If more
     than one destination is configured, App2Container creates a custom file that
     contains the FireLens configuration. Otherwise, the destination
     parameters are used directly in the Amazon ECS task definition and CloudFormation
     templates.




    	- service (string) – The
    	 AWS service to route logs to. *Valid values are
    	 "cloudwatch", "firehose", and "kinesis".*
    	- regexFilter (string) –
    	 A Ruby regular expression to match against log content to determine
    	 where to route the log.
    	- streamName (string) – The name
    	 of the log delivery stream that will be created at the destination.

- eksParameters (object) – Contains
  parameters needed for deployment to Amazon EKS. _The `createEksArtifacts`
  parameter is always required. Other parameters in this section that are
  marked as required apply only to Amazon EKS deployments._
  - createEksArtifacts (Boolean, required) – A flag
    that indicates if you are targeting Amazon EKS for deployment.
  - stackName (string, required) – A
    name to use as a prefix to your CloudFormation stack ID ARN. We
    recommend using the application ID for this.
  - cpu (number, required) – The hard
    limit for the number of vCPUs to present for the application container.
    The minimum value is .25, and the maximum value is 1.5. If there are no
    overrides, the default value is 1.5.
  - memory (number, required) – The hard
    limit of memory (in MiB) for the application container. Express this
    value as an integer, for example, 1024.
  - ingress (string, required) – The type
    of load balancer to use for the deployment. Specify one of the following
    values:
    - `alb` – Provisions an Application Load Balancer in the
      VPC for the deployment.
    - `nginx` – Provisions a Network Load Balancer in the VPC,
      and an NGINX ingress in the Kubernetes cluster for the
      deployment.

  ###### Note

  If you upgrade from a previous App2Container deployment, the load balancer URL might change.
  - dnsRecordName (string) – The fully qualified domain name
    (FQDN) for a DNS record for the deployed application, for example _hello.example.com_.
    If you specify this parameter, then App2Container creates the DNS record in a private hosted zone in Amazon Route 53.
    If you also specify the `rootDomain` parameter, then App2Container creates the DNS record in the
    specified root domain.
  - applicationPath (string) – The location of the application from
    the root of the web server, as accessed from the public URL, for example _/my-application_.
  - reuseResources (object) – Contains shared resource
    identifiers that can be used throughout your CloudFormation templates.
    - vpcId (string) – The VPC
      ID, if you want to bring your own VPC or to reuse an existing
      VPC that App2Container created for a prior deployment. _If you
      bring a custom VPC, you must have two or more private
      subnets in two or more Availability Zones. In this case, you
      can optionally have two or more public subnets in the same
      two Availability Zones._

    ###### Note

    For each private subnet in the reused VPC, you must
    configure a route to the internet using a NAT gateway. For
    more information about cluster networking for Amazon EKS, see
    [De-mystifying cluster networking for Amazon EKS worker
    nodes](https://aws.amazon.com/blogs/containers/de-mystifying-cluster-networking-for-amazon-eks-worker-nodes/ "https://aws.amazon.com/blogs/containers/de-mystifying-cluster-networking-for-amazon-eks-worker-nodes/").
    - cfnStackName (string) – The name or
      ID (ARN) of the CloudFormation stack created with App2Container for the containerized
      application.
    - sshKeyPairName (string)
      – The name of the Amazon EC2 key pair to use for the instances
      that your container runs on.
    - resourceTags (array of objects) –
      Custom tags, expressed as key/value pairs that are added to resources
      during deployment. For Amazon EKS deployments, the key/value pairs update the
      Kubernetes `deployment.yml` file.

    ###### Note

    An example tag is generated when the `deployment.json` file is created. If
    you don't remove or change the example tag before
    deployment, the tag is ignored by default.
    - rootDomain (string) – The name of a
      root domain (hosted zone) in Amazon Route 53, for example _example.com_.
      If you specify the `rootDomain`, then App2Container creates the DNS record
      that points to it.
    - acmCertificateArn (string) –
      The AWS Certificate Manager certificate ARN used to provide HTTPS connectivity
      to your Application Load Balancer. If you don't specify a value
      for acmCertificateArn, App2Container can
      only deploy HTTP applications.

    ###### Note

    The certificate can be imported or provisioned as follows:

        * To import an IIS certificate into ACM, see [How
         to import PFX-formatted certificates into AWS Certificate Manager using OpenSSL](https://aws.amazon.com/blogs/security/how-to-import-pfx-formatted-certificates-into-aws-certificate-manager-using-openssl/ "https://aws.amazon.com/blogs/security/how-to-import-pfx-formatted-certificates-into-aws-certificate-manager-using-openssl/").
        * To provision a certificate in ACM, see [Issuing and Managing Certificates](../../../acm/latest/userguide/gs.md "../../../acm/latest/userguide/gs.md")
         in the AWS Certificate Manager User Guide.

    If you use an HTTPS endpoint for your load balancer, this parameter
    is required. For more information about ACM, see [What is AWS Certificate Manager](../../../acm/latest/userguide.md "../../../acm/latest/userguide.md") in the
    AWS Certificate Manager User Guide.

  - gMSAParameters (object) – Contains parameters
    used by the CloudFormation template to create gMSA-related artifacts for .NET applications.
    - domainSecretsArn (string)
      – The Secrets Manager ARN for the domain credentials to join
      the Amazon EKS nodes to gMSA Active Directory.
    - domainDNSName (string) –
      The DNS name of the gMSA Active Directory for Amazon EKS nodes to
      join.
    - domainNetBIOSName (string)
      – The NetBIOS name of the Active Directory for Amazon EKS
      nodes to join.
    - createGMSA (Boolean, required)
      – A flag to create a group Managed Service Account (gMSA)
      Active Directory security group and account, using the name
      supplied in the `gMSAName` field.
    - gMSAAccountName (string) – The name of the
      gMSA Active Directory that the container should use for access.

  - dependentApps (array of objects) –
    For complex Windows applications, this array of JSON objects contains identifying
    details for dependent applications. App2Container does not generate this array. For complex
    Windows applications that incorporate dependent applications, you must add details
    to this array for each dependent application. You can include up to two dependent
    applications in the array.
    - appId (string, required) – The
      application ID that App2Container generated for this dependent
      application.
    - privateRootDomain (string, required)
      – The private domain name that's used for creating the
      hosted zone.
    - dnsRecordName (string, required) –
      The DNS record name of the application. This is combined with the privateRootDomain
      to construct the endpoint for the dependent application.

- appRunnerParameters (object) – Contains
  parameters needed for deployment of Linux applications to an AWS App Runner environment. _The
  `createAppRunnerArtifacts` parameter is always required. Other parameters in
  this section that are marked as required apply only to App Runner deployments._

###### Note

This section is not included for applications running on Windows.

    + createAppRunnerArtifacts (Boolean, required) –
     A flag that indicates if you are targeting App Runner for deployment.
    + stackName (string, required) – The name of the
     AWS CloudFormation stack. *We recommend including the application ID in the stack name.*
    + serviceName (string, required) – The name of the
     service in App Runner. *We recommend using the application ID for the service name.*
    + autoDeploymentsEnabled (Boolean, required) –
     If set to true, an update to the Amazon ECR repository also updates the service in App Runner. If
     set to false, you can manually update the service using the App Runner console or API, or
     `apprunner` commands in the AWS CLI.
    + resourceTags (array of objects) –
     Custom tags, expressed as key/value pairs that are added to resources
     during deployment. For App Runner deployments, the key/value pairs update
     both of the resources that are created in the `apprunner.yml`
     AWS CloudFormation template.


    ###### Note

    An example tag is generated when the `deployment.json` file is created. If
     the example tag isn't removed or changed before deployment, the tag
     is ignored by default.

###### Note

When the **containerize** command runs, it determines if your
application is suitable for App Runner, and adds `appRunnerParameters`
to the `deployment.json` file if it is. If your
application is not suitable for App Runner, the `appRunnerParameters`
are ignored.

### Examples

The following example shows a `deployment.json` file for a Java
application running on Linux, with default settings to deploy to an Amazon ECS
environment.

```
{
       "a2CTemplateVersion": "3.1",
       "applicationId": "java-tomcat-6e6f3a87",
       "imageName": "java-tomcat-6e6f3a87",
       "exposedPorts": [
              {
                     "localPort": 8080,
                     "protocol": "tcp6"
              },
              {
                     "localPort": 8009,
                     "protocol": "tcp6"
              },
              {
                     "localPort": 8005,
                     "protocol": "tcp6"
              }
       ],
       "environment": [],
       "ecrParameters": {
              "ecrRepoTag": "latest"
       },
       "ecsParameters": {
              "createEcsArtifacts": true,
              "ecsFamily": "java-tomcat-6e6f3a87",
              "cpu": 2,
              "memory": 4096,
              "dockerSecurityOption": "",
              "enableCloudwatchLogging": false,
              "publicApp": true,
              "stackName": "app2container-java-tomcat-6e6f3a87-ECS",
              "resourceTags": [
                     {
                            "key": "example-key",
                            "value": "example-value"
                     }
              ],
              "reuseResources": {
                     "vpcId": "",
                     "reuseExistingA2cStack": {
                            "cfnStackName": "",
                            "microserviceUrlPath": ""
                     },
                     "sshKeyPairName": "",
                     "acmCertificateArn": ""
              },
              "gMSAParameters": {
                     "createGMSA": false,
                     "domainSecretsArn": "",
                     "domainDNSName": "",
                     "domainNetBIOSName": "",
                     "gMSAName": "",
                     "ADSecurityGroupName": ""
              },
              "deployTarget": "fargate"
       },
       "fireLensParameters": {
             "enableFireLensLogging": true,
             "logDestinations": [
                    {
                            "service": "cloudwatch",
                            "matchRegex": "^.*INFO.*$",
                            "streamName": "Info"
                    },
                    {
                            "service": "cloudwatch",
                            "matchRegex": "^.*WARN.*$",
                            "streamName": "Warn"
                    }
             ]
       },
       "eksParameters": {
              "createEksArtifacts": false,
              "stackName": "java-tomcat-6e6f3a87",
              "reuseResources": {
                     "vpcId": "",
                     "cfnStackName": "",
                     "sshKeyPairName": ""
              },
              "gMSAParameters": {
                     "createGMSA": false,
                     "domainSecretsArn": "",
                     "domainDNSName": "",
                     "domainNetBIOSName": "",
                     "gMSAAccountName": "",
                     "ADSecurityGroupName": ""
              }
       },
       "appRunnerParameters": {
             "createAppRunnerArtifacts": false,
             "stackName": "a2c-java-tomcat-6e6f3a87-AppRunner",
             "autoDeploymentsEnabled": true,
             "resourceTags": [
                   {
                         "key": "example-key",
                         "value": "example-value"
                   }
             ]
       }
}
```

The following example shows a `deployment.json` file for a .NET
application running on Windows. The application has been configured to
deploy to an Amazon ECS Fargate environment.

```
{
       "a2CTemplateVersion": "3.1",
       "applicationId": "iis-smarts-51d2dbf8",
       "imageName": "iis-smarts-51d2dbf8",
       "exposedPorts": [
              {
                     "localPort": 8080,
                     "protocol": "http"
              }
       ],
       "environment": [],
       "ecrParameters": {
              "ecrRepoTag": "latest"
       },
       "ecsParameters": {
              "createEcsArtifacts": true,
              "ecsFamily": "iis-smarts-51d2dbf8",
              "cpu": 2,
              "memory": 4096,
              "dockerSecurityOption": "",
              "enableCloudwatchLogging": false,
              "publicApp": true,
              "stackName": "iis-smarts-51d2dbf8-ECS",
              "resourceTags": [
                     {
                            "key": "example-key",
                            "value": "example-value"
                     }
              ],
              "reuseResources": {
                     "vpcId": "vpc-0abc1defa2345b67c",
                     "reuseExistingA2cStack": {
                            "cfnStackName": "",
                            "microserviceUrlPath": ""
                     },
                     "sshKeyPairName": "",
                     "acmCertificateArn": ""
              },
              "gMSAParameters": {
                     "domainSecretsArn": "",
                     "domainDNSName": "",
                     "domainNetBIOSName": "",
                     "createGMSA": false,
                     "gMSAName": ""
              },
              "deployTarget": "fargate",
              "dependentApps" : []
       },
       "eksParameters": {
              "createEksArtifacts": false,
              "stackName": "iis-smarts-51d2dbf8-EKS",
              "reuseResources": {
                     "vpcId": "",
                     "reuseExistingA2cStack": {
                            "cfnStackName": "",
                            "microserviceUrlPath": ""
                     },
                     "sshKeyPairName": ""
              },
              "gMSAParameters": {
                     "createGMSA": false,
                     "domainSecretsArn": "",
                     "domainDNSName": "",
                     "domainNetBIOSName": "",
                     "gMSAAccountName": ""
              },
              "dependentApps" : []
       }
}
```

For complex Windows .NET web applications that consist of a root application and up to
two dependent applications, each application is defined separately. Each
application has its own `deployment.json` file.

The following example shows the `deployment.json` file for the
root application in a complex .NET web service running on Windows, followed by
`deployment.json` files for the two dependent applications that
it refers to. The applications are deployed to an Amazon ECS environment running together
in the same VPC.

- **Root application example**

```
{
       "a2CTemplateVersion": "3.1",
       "applicationId": "iis-smarts-51d2dbf8",
       "imageName": "iis-smarts-51d2dbf8",
       "exposedPorts": [
              {
                     "localPort": 8080,
                     "protocol": "http"
              }
       ],
       "environment": [],
       "ecrParameters": {
              "ecrRepoTag": "latest"
       },
       "ecsParameters": {
              "createEcsArtifacts": true,
              "ecsFamily": "iis-smarts-51d2dbf8",
              "cpu": 2,
              "memory": 4096,
              "dockerSecurityOption": "",
              "enableCloudwatchLogging": false,
              "publicApp": true,
              "stackName": "iis-smarts-51d2dbf8-ECS",
              "resourceTags": [
                     {
                            "key": "example-key",
                            "value": "example-value"
                     }
              ],
              "reuseResources": {
                     "vpcId": "vpc-0abc1defa2345b67c",
                     "reuseExistingA2cStack": {
                            "cfnStackName": "",
                            "microserviceUrlPath": ""
                     },
                     "sshKeyPairName": "",
                     "acmCertificateArn": ""
              },
              "gMSAParameters": {
                     "createGMSA": false,
                     "domainSecretsArn": "",
                     "domainDNSName": "",
                     "domainNetBIOSName": "",
                     "gMSAName": ""
              },
              "deployTarget": "ec2",
              "dependentApps" : [
                {
                    "appId":"iis-appB-ab800cde",
                    "privateRootDomain": "dependent-app1.test1.com",
                    "dnsRecordName":"appB"
                },
                {
                    "appId":"service-appC-9fghi90j",
                    "privateRootDomain": "dependent-app2.test1.com",
                    "dnsRecordName":"appC"
                }
            ]
       },
       "eksParameters": {
              "createEksArtifacts": false,
              "stackName": "iis-smarts-51d2dbf8",
              "reuseResources": {
                     "vpcId": "",
                     "reuseExistingA2cStack": {
                            "cfnStackName": "",
                            "microserviceUrlPath": ""
                     },
                     "sshKeyPairName": "",
                     "acmCertificateArn": ""
              },
              "gMSAParameters": {
                     "createGMSA": false,
                     "domainSecretsArn": "",
                     "domainDNSName": "",
                     "domainNetBIOSName": "",
                     "gMSAAccountName": ""
              },
              "dependentApps" : []
       }
}
```

- **Dependent application B**

```
{
       "a2CTemplateVersion": "3.1",
       "applicationId": "iis-appB-ab800cde",
       "imageName": "iis-appB-ab800cde",
       "exposedPorts": [
              {
                     "localPort": 8080,
                     "protocol": "http"
              }
       ],
       "environment": [],
       "ecrParameters": {
              "ecrRepoTag": "latest"
       },
       "ecsParameters": {
              "createEcsArtifacts": true,
              "ecsFamily": "iis-appB-ab800cde",
              "cpu": 2,
              "memory": 4096,
              "dockerSecurityOption": "",
              "enableCloudwatchLogging": false,
              "publicApp": true,
              "stackName": "iis-appB-ab800cde-ECS",
              "resourceTags": [
                     {
                            "key": "example-key",
                            "value": "example-value"
                     }
              ],
              "reuseResources": {
                     "vpcId": "vpc-0abc1defa2345b67c",
                     "reuseExistingA2cStack": {
                            "cfnStackName": "",
                            "microserviceUrlPath": ""
                     },
                     "sshKeyPairName": "",
                     "acmCertificateArn": ""
              },
              "gMSAParameters": {
                     "createGMSA": false,
                     "domainSecretsArn": "",
                     "domainDNSName": "",
                     "domainNetBIOSName": "",
                     "gMSAName": ""
              },
              "deployTarget": "ec2",
              "dependentApps" : []
       },
       "eksParameters": {
              "createEksArtifacts": false,
              "stackName": "",
              "reuseResources": {
                     "vpcId": "",
                     "reuseExistingA2cStack": {
                            "cfnStackName": "",
                            "microserviceUrlPath": ""
                     },
                     "sshKeyPairName": ""
              },
              "gMSAParameters": {
                     "createGMSA": false,
                     "domainSecretsArn": "",
                     "domainDNSName": "",
                     "domainNetBIOSName": "",
                     "gMSAAccountName": ""
              },
              "dependentApps" : []
       }
}
```

- **Dependent application C**

```
{
       "a2CTemplateVersion": "3.1",
       "applicationId": "service-appC-9fghi90j",
       "imageName": "service-appC-9fghi90j",
       "exposedPorts": [
              {
                     "localPort": 8080,
                     "protocol": "http"
              }
       ],
       "environment": [],
       "ecrParameters": {
              "ecrRepoTag": "latest"
       },
       "ecsParameters": {
              "createEcsArtifacts": true,
              "ecsFamily": "service-appC-9fghi90j",
              "cpu": 2,
              "memory": 4096,
              "dockerSecurityOption": "",
              "enableCloudwatchLogging": false,
              "publicApp": true,
              "stackName": "service-appC-9fghi90j-ECS",
              "resourceTags": [
                     {
                            "key": "example-key",
                            "value": "example-value"
                     }
              ],
              "reuseResources": {
                     "vpcId": "vpc-0abc1defa2345b67c",
                     "reuseExistingA2cStack": {
                            "cfnStackName": "",
                            "microserviceUrlPath": ""
                     },
                     "sshKeyPairName": "",
                     "acmCertificateArn": ""
              },
              "gMSAParameters": {
                     "createGMSA": false,
                     "domainSecretsArn": "",
                     "domainDNSName": "",
                     "domainNetBIOSName": "",
                     "gMSAName": ""
              },
              "deployTarget": "ec2",
              "dependentApps" : []
       },
       "eksParameters": {
              "createEksArtifacts": false,
              "stackName": "service-appC-9fghi90j",
              "reuseResources": {
                     "vpcId": "",
                     "reuseExistingA2cStack": {
                            "cfnStackName": "",
                            "microserviceUrlPath": ""
                     },
                     "sshKeyPairName": ""
              },
              "gMSAParameters": {
                     "createGMSA": false,
                     "domainSecretsArn": "",
                     "domainDNSName": "",
                     "domainNetBIOSName": "",
                     "gMSAAccountName": ""
              },
              "dependentApps" : []
       }
}
```
