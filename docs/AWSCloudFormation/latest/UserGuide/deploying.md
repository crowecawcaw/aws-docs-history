# Deploy applications on Amazon EC2

You can use CloudFormation to automatically install, configure, and start applications on Amazon EC2
instances. Doing so enables you to easily duplicate deployments and update existing
installations without connecting directly to the instance, which can save you a lot of time and
effort.

CloudFormation includes a set of helper scripts (`cfn-init`, `cfn-signal`,
`cfn-get-metadata`, and `cfn-hup`) that are based on
`cloud-init`. You call these helper scripts from your CloudFormation templates to
install, configure, and update applications on Amazon EC2 instances that are in the same template.
For more information, see the [CloudFormation helper scripts reference](../TemplateReference/cfn-helper-scripts-reference.md "../TemplateReference/cfn-helper-scripts-reference.md") in the
_CloudFormation Template Reference Guide_.

In the [getting started tutorial](gettingstarted.md "gettingstarted.md"), you
created a simple web server using `UserData` with a basic bash script. While this
worked for a simple "Hello World" page, real applications often need more sophisticated
configuration, including:

- Multiple software packages installed in the correct order.
- Complex configuration files created with specific content.
- Services started and configured to run automatically.
- Error handling and validation of the setup process.
  CloudFormation's helper scripts provide a more robust and maintainable way to configure EC2
  instances compared to basic bash scripts in `UserData`. The `cfn-init`
  helper script reads configuration data from your template's metadata and applies it
  systematically to your instance.

In this tutorial, you'll learn how to use the `cfn-init` helper script and
monitor the bootstrapping process.

###### Note

CloudFormation is free, but you'll be charged for the Amazon EC2 resources you create. However, if
you're new to AWS, you can take advantage of the [Free
Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") to minimize or eliminate costs during this learning process.

###### Topics

- [Prerequisites](#bootstrapping-tutorial-prerequisites "#bootstrapping-tutorial-prerequisites")
- [Understanding bootstrap
  concepts](#bootstrapping-tutorial-understand-concepts "#bootstrapping-tutorial-understand-concepts")
- [Start with a simple bootstrap
  example](#bootstrapping-tutorial-simple-example "#bootstrapping-tutorial-simple-example")
- [Adding files and commands](#bootstrapping-tutorial-add-complexity "#bootstrapping-tutorial-add-complexity")
- [Adding network security](#bootstrapping-tutorial-security-group "#bootstrapping-tutorial-security-group")
- [The complete bootstrap
  template](#bootstrapping-tutorial-complete-template "#bootstrapping-tutorial-complete-template")
- [Create the stack using the
  console](#bootstrapping-tutorial-create-stack "#bootstrapping-tutorial-create-stack")
- [Monitor the bootstrap
  process](#bootstrapping-tutorial-validate-bootstrap "#bootstrapping-tutorial-validate-bootstrap")
- [Test the bootstrapped web
  server](#bootstrapping-tutorial-test-web-server "#bootstrapping-tutorial-test-web-server")
- [Troubleshooting bootstrap
  issues](#bootstrapping-tutorial-troubleshooting "#bootstrapping-tutorial-troubleshooting")
- [Clean up resources](#bootstrapping-tutorial-clean-up "#bootstrapping-tutorial-clean-up")
- [Next steps](#bootstrapping-tutorial-next-steps "#bootstrapping-tutorial-next-steps")

## Prerequisites

- You must have completed the [Creating your first stack](gettingstarted.md "gettingstarted.md") tutorial or have equivalent experience with
  CloudFormation basics.
- You must have access to an AWS account with an IAM user or role that has
  permissions to use Amazon EC2 and CloudFormation, or administrative user access.
- You must have a Virtual Private Cloud (VPC) that has access to the internet. This
  tutorial template requires a default VPC, which comes automatically with newer
  AWS accounts. If you don't have a default VPC, or if it was deleted, see the
  troubleshooting section in the [Creating your first stack](gettingstarted.md "gettingstarted.md") tutorial for alternative solutions.

## Understanding bootstrap

concepts

Let's understand the key concepts that make bootstrapping work before creating the
template.

### The `cfn-init` helper

script

CloudFormation provides Python helper scripts that you can use to install software and start
services on an Amazon EC2 instance. The `cfn-init` script reads resource metadata from
your template and applies the configuration to your instance.

The process works as follows:

1. You define the configuration in the `Metadata` section of your EC2
   resource.
2. You call `cfn-init` from the `UserData` script.
3. `cfn-init` reads the metadata and applies the configuration.
4. Your instance is configured according to your specifications.

### Metadata structure

The configuration is defined in a specific structure within your EC2 instance.

```
Resources:
  EC2Instance:
    Type: AWS::EC2::Instance
    Metadata:                       # Metadata section for the resource
      AWS::CloudFormation::Init:    # Required key that cfn-init looks for
        config:                     # Configuration name (you can have multiple)
          packages:                 # Install packages
          files:                    # Create files
          commands:                 # Run commands
          services:                 # Start/stop services
```

The `cfn-init` script processes these sections in a specific order: packages,
groups, users, sources, files, commands, and then services.

## Start with a simple bootstrap

example

Let's start with a minimal bootstrap example that just installs and starts Apache.

```
Resources:
  EC2Instance:
    Type: AWS::EC2::Instance
    Metadata:
      AWS::CloudFormation::Init:
        config:
          packages:                 # Install Apache web server
            yum:
              httpd: []
          services:                 # Start Apache and enable it to start on boot
            systemd:
              httpd:
                enabled: true
                ensureRunning: true
    Properties:
      ImageId: !Ref LatestAmiId
      InstanceType: !Ref InstanceType
      UserData: !Base64             # Script that runs when instance starts
        Fn::Sub: |
          #!/bin/bash
          yum install -y aws-cfn-bootstrap
          /opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource EC2Instance --region ${AWS::Region}
```

This simple example demonstrates the core concepts:

- `packages` section installs the `httpd` package using
  yum. This works on Amazon Linux and other Linux distributions that use
  yum.
- `services` section ensures `httpd` starts and runs
  automatically.
- `UserData` installs the latest bootstrap tools and calls
  `cfn-init`.

## Adding files and commands

Now, let's enhance our example by adding a custom web page and a log file in the
`/var/log` directory on the EC2 instance.

### Creating files

The `files` section allows you to create files on the instance with specific
content. The vertical pipe (`|`) allows you to pass a literal block of text (HTML
code) as the content of the file (`/var/www/html/index.html`).

```
files:
  /var/www/html/index.html:
    content: |
      <body>
        <h1>Congratulations, you have successfully launched the AWS CloudFormation sample.</h1>
      </body>
```

### Running commands

The `commands` section lets you run shell commands during the bootstrap
process. This command creates a log file at `/var/log/welcome.txt` on the
EC2 instance. To view it, you need an Amazon EC2 key pair to use for SSH access and an IP address
range that can be used to SSH to the instance (not covered here).

```
commands:
  createWelcomeLog:
    command: "echo 'cfn-init ran successfully!' > /var/log/welcome.txt"
```

## Adding network security

Since we're setting up a web server, we need to allow web traffic (HTTP) to reach our EC2
instance. To do this, we'll create a security group that allows incoming traffic on port 80
from your IP address. EC2 instances also need to send traffic out to the internet, for
example, to install package updates. By default, security groups allow all outgoing traffic.
We'll then associate this security group with our EC2 instance using the
`SecurityGroupIds` property.

```
WebServerSecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: Allow HTTP access from my IP address
    SecurityGroupIngress:
      - IpProtocol: tcp
        Description: HTTP
        FromPort: 80
        ToPort: 80
        CidrIp: !Ref MyIP
```

## The complete bootstrap

template

Now, let's put all the pieces together. Here's the complete template that combines all the
concepts we've discussed.

```
AWSTemplateFormatVersion: 2010-09-09
Description: Bootstrap an EC2 instance with Apache web server using cfn-init

Parameters:
  LatestAmiId:
    Description: The latest Amazon Linux 2 AMI from the Parameter Store
    Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    Default: '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2'

  InstanceType:
    Description: EC2 instance type
    Type: String
    Default: t2.micro
    AllowedValues:
      - t3.micro
      - t2.micro
    ConstraintDescription: must be a valid EC2 instance type.

  MyIP:
    Description: Your IP address in CIDR format (e.g. 203.0.113.1/32)
    Type: String
    MinLength: 9
    MaxLength: 18
    Default: 0.0.0.0/0
    AllowedPattern: '^(\d{1,3}\.){3}\d{1,3}\/\d{1,2}$'
    ConstraintDescription: must be a valid IP CIDR range of the form x.x.x.x/x.

Resources:
  WebServerSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow HTTP access from my IP address
      SecurityGroupIngress:
        - IpProtocol: tcp
          Description: HTTP
          FromPort: 80
          ToPort: 80
          CidrIp: !Ref MyIP

  WebServer:
    Type: AWS::EC2::Instance
    Metadata:
      AWS::CloudFormation::Init:
        config:
          packages:
            yum:
              httpd: []
          files:
            /var/www/html/index.html:
              content: |
                <body>
                  <h1>Congratulations, you have successfully launched the AWS CloudFormation sample.</h1>
                </body>
          commands:
            createWelcomeLog:
              command: "echo 'cfn-init ran successfully!' > /var/log/welcome.txt"
          services:
            systemd:
              httpd:
                enabled: true
                ensureRunning: true
    Properties:
      ImageId: !Ref LatestAmiId
      InstanceType: !Ref InstanceType
      SecurityGroupIds:
        - !Ref WebServerSecurityGroup
      UserData: !Base64
        Fn::Sub: |
          #!/bin/bash
          yum install -y aws-cfn-bootstrap
          /opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource WebServer --region ${AWS::Region}
      Tags:
        - Key: Name
          Value: Bootstrap Tutorial Web Server

Outputs:
  WebsiteURL:
    Value: !Sub 'http://${WebServer.PublicDnsName}'
    Description: EC2 instance public DNS name
```

## Create the stack using the

console

The following procedure involves uploading the sample stack template from a file. Open a
text editor on your local machine and add the template. Save the file with the name
`samplelinux2stack.template`.

###### To launch the stack template

1. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. Choose **Create stack**, **With new resources
   (standard)**.
3. Under **Specify template**, choose **Upload a template
   file**, **Choose file** to upload the
   `samplelinux2stack.template` file.
4. Choose **Next**.
5. On the **Specify stack details** page, type
   `BootstrapTutorialStack` as the stack name.
6. Under **Parameters**, do the following.
   - **LatestAmiId**: Leave the default value.
   - **InstanceType**: Choose either **t2.micro** or
     **t3.micro** for the EC2 instance type.
   - **MyIP**: Enter your public IP address with a `/32`
     suffix.

7. Choose **Next** twice, then **Submit** to create the
   stack.

## Monitor the bootstrap

process

Bootstrap processes take longer than simple EC2 launches because additional software is
being installed and configured.

###### To monitor bootstrap progress

1. In the CloudFormation console, select your stack and open the **Events**
   tab.
2. Watch for the `WebServer CREATE_IN_PROGRESS` event. The bootstrap process
   begins after the instance launches.
3. The bootstrap process typically takes a few minutes. You'll see `WebServer
CREATE_COMPLETE` when it's finished.

If you want to see what's happening during the bootstrap process, you can check the
instance logs.

###### To view bootstrap logs (optional)

1. Open the [EC2 console](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/") and find your
   instance.
2. Select the instance, and then choose **Actions**, **Monitor
   and troubleshoot**, **Get system log** to see the bootstrap
   progress.
3. If you don't see the logs immediately, wait and refresh the page.

## Test the bootstrapped web

server

When your stack shows `CREATE_COMPLETE`, test your web server.

###### To test the web server

1. In the CloudFormation console, go to the **Outputs** tab for your
   stack.
2. Click on the **WebsiteURL** value to open your web server in a new
   tab.
3. You should see your custom web page with the message `Congratulations, you have
successfully launched the AWS CloudFormation sample`.

###### Note

If the page doesn't load immediately, wait a minute and try again. The bootstrap process
may still be completing even after the stack shows `CREATE_COMPLETE`.

## Troubleshooting bootstrap

issues

If your bootstrap process fails or your web server isn't working, here are common issues
and solutions.

### Common issues

- Stack creation fails – Check the
  **Events** tab for specific error messages.
- Web server not accessible – Verify your IP
  address is correct in the `MyIP` parameter. Remember to include
  `/32` at the end.
- Bootstrap process fails – The instance may
  launch but `cfn-init` fails. Check the system logs as described in the
  monitoring section.

## Clean up resources

To avoid ongoing charges, you can clean up by deleting the stack and its resources.

###### To delete the stack and its resources

1. Open the [CloudFormation
   console](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the **Stacks** page, select the option next to the name of the
   stack you created (`BootstrapTutorialStack`) and then choose
   **Delete**.
3. When prompted for confirmation, choose **Delete**.
4. Monitor the progress of the stack deletion process on the **Event**
   tab. The status for `BootstrapTutorialStack` changes to
   `DELETE_IN_PROGRESS`. When CloudFormation completes the deletion of the stack, it
   removes the stack from the list.

## Next steps

Congratulations! You've successfully learned how to bootstrap EC2 instances with
CloudFormation. You now understand:

- How to use `cfn-init` helper scripts
- How to structure metadata for bootstrapping
- How to install packages, create files, run commands, and manage services
- How to monitor for bootstrap issues

To continue learning:

- Learn how to update a running stack and use the `cfn-hup` helper script.
  For more information, see [Update a CloudFormation stack](updating.stacks.md "updating.stacks.md").
- Learn how to bootstrap a Windows stack. For more information, see [Bootstrapping Windows-based
  CloudFormation stacks](cfn-windows-stacks-bootstrapping.md "cfn-windows-stacks-bootstrapping.md").
- Explore more complex bootstrap scenarios with multiple configuration sets. For more
  information, see [cfn-init](../TemplateReference/cfn-init.md "../TemplateReference/cfn-init.md") and
  [AWS::CloudFormation::Init](../TemplateReference/aws-resource-init.md "../TemplateReference/aws-resource-init.md") in the _CloudFormation Template Reference Guide_.
- Learn about `cfn-signal` for reporting bootstrap completion status. For
  more information, see [cfn-signal](../TemplateReference/cfn-signal.md "../TemplateReference/cfn-signal.md") in
  the _CloudFormation Template Reference Guide_.
