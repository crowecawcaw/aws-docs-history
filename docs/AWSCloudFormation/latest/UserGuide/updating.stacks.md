# Update a CloudFormation stack

###### Note

This tutorial builds on concepts from the [Deploy applications on Amazon EC2](deploying.md "deploying.md") tutorial. If you haven't completed that tutorial,
we recommend doing so first to understand EC2 bootstrapping with CloudFormation.

This topic demonstrates a simple progression of updates to a running stack. We will walk
through the following steps:

1. Create the initial stack – Create a stack using a
   base Amazon Linux 2 AMI, installing the Apache Web Server and a simple PHP application
   using the CloudFormation helper scripts.
2. Update the application – Update one of the files
   in the application and deploy the software using CloudFormation.
3. Add a key pair – Add an Amazon EC2 key pair to the
   instance, and then update the security group to allow SSH access to the instance.
4. Update the instance type – Change the instance
   type of the underlying Amazon EC2 instance.
5. Update the AMI – Change the Amazon Machine Image
   (AMI) for the Amazon EC2 instance in your stack.

###### Note

CloudFormation is free, but you'll be charged for the Amazon EC2 resources you create. However, if
you're new to AWS, you can take advantage of the [Free
Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") to minimize or eliminate costs during this learning process.

###### Topics

- [Step 1: Create the initial stack](#update-stack-initial-stack "#update-stack-initial-stack")
- [Step 2: Update the application](#update-stack-update-application "#update-stack-update-application")
- [Step 3: Add SSH access with a key pair](#update-stack-add-key-pair "#update-stack-add-key-pair")
- [Step 4: Update the instance type](#update-stack-update-instance-type "#update-stack-update-instance-type")
- [Step 5: Update the AMI](#update-stack-update-ami "#update-stack-update-ami")
- [Availability and impact considerations](#update.walkthrough.impact "#update.walkthrough.impact")
- [Related resources](#update.walkthrough.related "#update.walkthrough.related")

## Step 1: Create the initial stack

We'll begin by creating a stack that we can use throughout the rest of this topic. We have
provided a simple template that launches a single instance PHP web application hosted on the
Apache Web Server and running on an Amazon Linux 2 AMI.

The Apache Web Server, PHP, and the simple PHP application are all
installed by the CloudFormation helper scripts that are installed by default on the Amazon Linux 2 AMI. The
following template snippet shows the metadata that describes the packages and files to
install, in this case the Apache Web Server and the PHP infrastructure from the
Yum repository for the Amazon Linux 2 AMI. The snippet also shows the
`Services` section, which ensures that the Apache Web Server is
running.

```
WebServerInstance:
  Type: AWS::EC2::Instance
  Metadata:
    AWS::CloudFormation::Init:
      config:
        packages:
          yum:
            httpd: []
            php: []
        files:
          /var/www/html/index.php:
            content: |
              <?php
              echo '<h1>Hello World!</h1>';
              ?>
            mode: '000644'
            owner: apache
            group: apache
        services:
          systemd:
            httpd:
              enabled: true
              ensureRunning: true
```

The application itself is a "Hello World" example that's entirely defined within the
template. For a real-world application, the files may be stored on Amazon S3, GitHub, or another
repository and referenced from the template. CloudFormation can download packages (such as RPMs or
RubyGems), and reference individual files and expand `.zip` and
`.tar` files to create the application artifacts on the Amazon EC2
instance.

The template enables and configures the `cfn-hup` daemon to listen for changes
to the configuration defined in the metadata for the Amazon EC2 instance. By using the
`cfn-hup` daemon, you can update application software, such as the version of
Apache or PHP, or you can update the PHP application file itself from CloudFormation. The
following snippet from the same Amazon EC2 resource in the template shows the pieces necessary to
configure `cfn-hup` to call `cfn-init` every two minutes to notice and
apply updates to the metadata. Otherwise, the `cfn-init` only runs once at start
up.

```
files:
  /etc/cfn/cfn-hup.conf:
    content: !Sub |
      [main]
      stack=${AWS::StackId}
      region=${AWS::Region}
      # The interval used to check for changes to the resource metadata in minutes. Default is 15
      interval=2
    mode: '000400'
    owner: root
    group: root
  /etc/cfn/hooks.d/cfn-auto-reloader.conf:
    content: !Sub |
      [cfn-auto-reloader-hook]
      triggers=post.update
      path=Resources.WebServerInstance.Metadata.AWS::CloudFormation::Init
      action=/opt/aws/bin/cfn-init -s ${AWS::StackId} -r WebServerInstance --region ${AWS::Region}
      runas=root
services:
  systemd:
    cfn-hup:
      enabled: true
      ensureRunning: true
      files:
        - /etc/cfn/cfn-hup.conf
        - /etc/cfn/hooks.d/cfn-auto-reloader.conf
```

To complete the stack, in the `Properties` section of the Amazon EC2 instance
definition, the `UserData` property contains the `cloud-init` script
that calls `cfn-init` to install the packages and files. For more information, see
the [CloudFormation helper scripts reference](../TemplateReference/cfn-helper-scripts-reference.md "../TemplateReference/cfn-helper-scripts-reference.md") in the _CloudFormation Template Reference Guide_. The template also
creates an Amazon EC2 security group.

```
AWSTemplateFormatVersion: 2010-09-09

Parameters:
  LatestAmiId:
    Description: The latest Amazon Linux 2 AMI from the Parameter Store
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2'

  InstanceType:
    Description: WebServer EC2 instance type
    Type: String
    Default: t3.micro
    AllowedValues:
      - t3.nano
      - t3.micro
      - t3.small
      - t3.medium
      - t3a.nano
      - t3a.micro
      - t3a.small
      - t3a.medium
      - m5.large
      - m5.xlarge
      - m5.2xlarge
      - m5a.large
      - m5a.xlarge
      - m5a.2xlarge
      - c5.large
      - c5.xlarge
      - c5.2xlarge
      - r5.large
      - r5.xlarge
      - r5.2xlarge
      - r5a.large
      - r5a.xlarge
      - r5a.2xlarge
    ConstraintDescription: must be a valid EC2 instance type.

Resources:
  WebServerInstance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !Ref LatestAmiId
      InstanceType: !Ref InstanceType
      SecurityGroupIds:
        - !Ref WebServerSecurityGroup
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash -xe
          # Get the latest CloudFormation package
          yum update -y aws-cfn-bootstrap
          # Run cfn-init
          /opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource WebServerInstance --region ${AWS::Region} || error_exit 'Failed to run cfn-init'
          # Start up the cfn-hup daemon to listen for changes to the EC2 instance metadata
          /opt/aws/bin/cfn-hup || error_exit 'Failed to start cfn-hup'
          # Signal success or failure
          /opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerInstance --region ${AWS::Region}
    Metadata:
      AWS::CloudFormation::Init:
        config:
          packages:
            yum:
              httpd: []
              php: []
          files:
            /var/www/html/index.php:
              content: |
                <?php
                echo "<h1>Hello World!</h1>";
                ?>
              mode: '000644'
              owner: apache
              group: apache
            /etc/cfn/cfn-hup.conf:
              content: !Sub |
                [main]
                stack=${AWS::StackId}
                region=${AWS::Region}
                # The interval used to check for changes to the resource metadata in minutes. Default is 15
                interval=2
              mode: '000400'
              owner: root
              group: root
            /etc/cfn/hooks.d/cfn-auto-reloader.conf:
              content: !Sub |
                [cfn-auto-reloader-hook]
                triggers=post.update
                path=Resources.WebServerInstance.Metadata.AWS::CloudFormation::Init
                action=/opt/aws/bin/cfn-init -s ${AWS::StackId} -r WebServerInstance --region ${AWS::Region}
                runas=root
          services:
            systemd:
              httpd:
                enabled: true
                ensureRunning: true
              cfn-hup:
                enabled: true
                ensureRunning: true
                files:
                  - /etc/cfn/cfn-hup.conf
                  - /etc/cfn/hooks.d/cfn-auto-reloader.conf
    CreationPolicy:
      ResourceSignal:
        Timeout: PT5M

  WebServerSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Enable HTTP access via port 80
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0

Outputs:
  WebsiteURL:
    Value: !Sub 'http://${WebServerInstance.PublicDnsName}'
    Description: URL of the web application
```

###### To launch a stack from this template

1. Copy the template and save it locally on your system as a text file. Note the location
   because you'll need to use the file in a subsequent step.
2. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
3. Choose **Create stack, With new resources (standard)**.
4. Choose **Choose an existing template**.
5. Under **Specify template**, choose **Upload a template
   file** and browse to the file that you created in the first step, and then
   choose **Next**.
6. On the **Specify stack details** page, enter
   `UpdateTutorial` as the stack name.
7. Under **Parameters**, keep all parameters the same and choose
   **Next** twice.
8. On the **Review and create** screen, choose
   **Submit**.

After the status of your stack is `CREATE_COMPLETE`, the
**Outputs** tab will display the URL of your website. If you choose the
value of the `WebsiteURL` output, you will see your new PHP application
working.

## Step 2: Update the application

Now that we have deployed the stack, let's update the application. We'll make a simple
change to the text that's printed out by the application. To do so, we'll add an echo command
to the index.php file as shown in this template snippet:

```
files:
  /var/www/html/index.php:
    content: |
      <?php
      echo "<h1>Hello World!</h1>";
      `echo "<p>This is an updated version of our application.</p>";`
      ?>
    mode: '000644'
    owner: apache
    group: apache
```

Use a text editor to manually edit the template file that you saved locally.

Now, update the stack.

###### To update the stack with your updated template

1. In the CloudFormation console, select your `UpdateTutorial`
   stack.
2. Choose **Update, Make a direct update**.
3. Choose **Replace existing template**.
4. Under **Specify template**, choose **Upload a template
   file** and upload your modified template file, and then choose
   **Next**.
5. On the **Specify stack details** page, keep all parameters the same
   and choose **Next** twice.
6. On the **Review** page, review the changes. Under
   **Changes**, you should see that CloudFormation will update the
   `WebServerInstance` resource.
7. Choose **Submit**.

When your stack is in the `UPDATE_COMPLETE` state, you can choose the
`WebsiteURL` output value again to verify that the changes to your application
have taken effect. By default, the `cfn-hup` daemon runs every 2 minutes, so it may
take up to 2 minutes for the application to change once the stack has been updated.

To see the set of resources that were updated, go to the CloudFormation console. On the
**Events** tab, look at the stack events. In this particular case, the
metadata for the Amazon EC2 instance `WebServerInstance` was updated, which caused
CloudFormation to also reevaluate the other resources (`WebServerSecurityGroup`) to
ensure that there were no other changes. None of the other stack resources were modified.
CloudFormation will update only those resources in the stack that are affected by any changes to
the stack. Such changes can be direct, such as property or metadata changes, or they can be
due to dependencies or data flows through `Ref`, `GetAtt`, or other
intrinsic template functions. For more information, see [Intrinsic function reference](../TemplateReference/intrinsic-function-reference.md "../TemplateReference/intrinsic-function-reference.md").

This simple update illustrates the process. However, you can make much more complex
changes to the files and packages that are deployed to your Amazon EC2 instances. For example, you
might decide that you need to add MySQL to the instance, along with PHP support for MySQL. To
do so, simply add the additional packages and files along with any additional services to the
configuration and then update the stack to deploy the changes.

```
packages:
  yum:
    httpd: []
    php: []
    `mysql: []`
    `php-mysql: []`
    `mysql-server: []`
    `mysql-libs: []`

  `...`

services:
  systemd:
    httpd:
      enabled: true
      ensureRunning: true
    cfn-hup:
      enabled: true
      ensureRunning: true
      files:
        - /etc/cfn/cfn-hup.conf
        - /etc/cfn/hooks.d/cfn-auto-reloader.conf
    `mysqld:`
      `enabled: true`
      `ensureRunning: true`
```

You can update the CloudFormation metadata to update to new versions of the packages used by
the application. In the previous examples, the version property for each package is empty,
indicating that `cfn-init` should install the latest version of the package.

```
packages:
  yum:
    httpd: []
    php: []
```

You can optionally specify a version string for a package. If you change the version
string in subsequent update stack calls, the new version of the package will be deployed.
Here's an example of using version numbers for RubyGems packages. Any package that supports
versioning can have specific versions.

```
packages:
  rubygems:
    mysql: []
    rubygems-update:
      - "1.6.2"
    rake:
      - "0.8.7"
    rails:
      - "2.3.11"
```

## Step 3: Add SSH access with a key pair

You can also update a resource in the template to add properties that weren't originally
specified in the template. To illustrate that, we'll add an Amazon EC2 key pair to an existing EC2
instance and then open up port 22 in the Amazon EC2 security group so that you can use Secure Shell
(SSH) to access the instance.

###### To add SSH access to an existing Amazon EC2 instance

1. Add two additional parameters to the template to pass in the name of an existing Amazon EC2
   key pair and SSH location.

```
Parameters:
  KeyName:
    Description: Name of an existing EC2 KeyPair to enable SSH access to the instance
    Type: AWS::EC2::KeyPair::KeyName
    ConstraintDescription: must be the name of an existing EC2 KeyPair.

  SSHLocation:
    Description: The IP address that can be used to SSH to the EC2 instances in CIDR format (e.g. 203.0.113.1/32)
    Type: String
    MinLength: 9
    MaxLength: 18
    Default: 0.0.0.0/0
    AllowedPattern: '^(\d{1,3}\.){3}\d{1,3}\/\d{1,2}$'
    ConstraintDescription: must be a valid IP CIDR range of the form x.x.x.x/x.
```

2. Add the `KeyName` property to the Amazon EC2 instance.

```
WebServerInstance:
  Type: AWS::EC2::Instance
  Properties:
    ImageId: !Ref LatestAmiId
    InstanceType: !Ref InstanceType
    KeyName: !Ref KeyName
    SecurityGroupIds:
      - !Ref WebServerSecurityGroup
```

3. Add port 22 and the SSH location to the ingress rules for the Amazon EC2 security
   group.

```
WebServerSecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: Enable HTTP access via port 80 and SSH access via port 22
    SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 80
        ToPort: 80
        CidrIp: 0.0.0.0/0
      - IpProtocol: tcp
        FromPort: 22
        ToPort: 22
        CidrIp: !Ref SSHLocation
```

4. Update the stack using the same steps as explained in [Step 2: Update the application](#update-stack-update-application "#update-stack-update-application").

## Step 4: Update the instance type

Now let's demonstrate how to update the underlying infrastructure by changing the instance
type.

The stack we have built so far uses a t3.micro Amazon EC2 instance. Let's suppose that your
newly created website is getting more traffic than a t3.micro instance can handle, and now you
want to move to an m5.large Amazon EC2 instance type. If the architecture of the instance type
changes, the instance must be created with a different AMI. However, both the t3.micro and
m5.large use the same CPU architectures and run Amazon Linux 2 (x86_64) AMIs . For more information,
see [Compatibility for changing the instance type](../../../AWSEC2/latest/UserGuide/resize-limitations.md "../../../AWSEC2/latest/UserGuide/resize-limitations.md") in the
_Amazon EC2 User Guide_.

Let's use the template that we modified in the previous step to change the instance type.
Because `InstanceType` was an input parameter to the template, we don't need to
modify the template; we can change the value of the parameter on the **Specify stack
details** page.

###### To update the stack with a new parameter value

1. In the CloudFormation console, select your `UpdateTutorial`
   stack.
2. Choose **Update, Make a direct update**.
3. Choose **Use existing template**, and then choose
   **Next**.
4. On the **Specify stack details** page, change the value of the
   **InstanceType** text box from `t3.micro` to
   `m5.large`. Then, choose **Next** twice.
5. On the **Review** page, review the changes. Under
   **Changes**, you should see that CloudFormation will update the
   `WebServerInstance` resource.
6. Choose **Submit**.

You can dynamically change the instance type of an EBS-backed Amazon EC2 instance by starting
and stopping the instance. CloudFormation tries to optimize the change by updating the instance
type and restarting the instance, so the instance ID doesn't change. When the instance is
restarted, however, the public IP address of the instance does change. To ensure that the
Elastic IP address is bound correctly after the change, CloudFormation will also update the
Elastic IP address. You can see the changes in the CloudFormation console on the
**Events** tab.

To check the instance type from the AWS Management Console, open the Amazon EC2 console, and locate your
instance there.

## Step 5: Update the AMI

Now let's update our stack to use Amazon Linux 2023, which is the next generation of Amazon Linux.

Updating the AMI is a major change that requires replacing the instance. We can't simply
start and stop the instance to modify the AMI; CloudFormation considers this a change to an
immutable property of the resource. In order to make a change to an immutable property,
CloudFormation must launch a replacement resource, in this case a new Amazon EC2 instance running the
new AMI.

Let's look at how we might update our stack template to use Amazon Linux 2023. The key changes
include updating the AMI parameter and changing from `yum` to `dnf`
package manager.

```
AWSTemplateFormatVersion: 2010-09-09

Parameters:
  LatestAmiId:
    Description: The latest Amazon Linux 2023 AMI from the Parameter Store
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: '/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64'

  InstanceType:
    Description: WebServer EC2 instance type
    Type: String
    Default: t3.micro
    AllowedValues:
      - t3.nano
      - t3.micro
      - t3.small
      - t3.medium
      - t3a.nano
      - t3a.micro
      - t3a.small
      - t3a.medium
      - m5.large
      - m5.xlarge
      - m5.2xlarge
      - m5a.large
      - m5a.xlarge
      - m5a.2xlarge
      - c5.large
      - c5.xlarge
      - c5.2xlarge
      - r5.large
      - r5.xlarge
      - r5.2xlarge
      - r5a.large
      - r5a.xlarge
      - r5a.2xlarge
    ConstraintDescription: must be a valid EC2 instance type.

  KeyName:
    Description: Name of an existing EC2 KeyPair to enable SSH access to the instance
    Type: AWS::EC2::KeyPair::KeyName
    ConstraintDescription: must be the name of an existing EC2 KeyPair.

  SSHLocation:
    Description: The IP address that can be used to SSH to the EC2 instances in CIDR format (e.g. 203.0.113.1/32)
    Type: String
    MinLength: 9
    MaxLength: 18
    Default: 0.0.0.0/0
    AllowedPattern: '^(\d{1,3}\.){3}\d{1,3}\/\d{1,2}$'
    ConstraintDescription: must be a valid IP CIDR range of the form x.x.x.x/x.

Resources:
  WebServerInstance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !Ref LatestAmiId
      InstanceType: !Ref InstanceType
      KeyName: !Ref KeyName
      SecurityGroupIds:
        - !Ref WebServerSecurityGroup
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash -xe
          # Get the latest CloudFormation package
          dnf update -y aws-cfn-bootstrap
          # Run cfn-init
          /opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource WebServerInstance --region ${AWS::Region} || error_exit 'Failed to run cfn-init'
          # Start up the cfn-hup daemon to listen for changes to the EC2 instance metadata
          /opt/aws/bin/cfn-hup || error_exit 'Failed to start cfn-hup'
          # Signal success or failure
          /opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerInstance --region ${AWS::Region}
    Metadata:
      AWS::CloudFormation::Init:
        config:
          packages:
            dnf:
              httpd: []
              php: []
          files:
            /var/www/html/index.php:
              content: |
                <?php
                echo "<h1>Hello World!</h1>";
                echo "<p>This is an updated version of our application.</p>";
                echo "<p>Running on Amazon Linux 2023!</p>";
                ?>
              mode: '000644'
              owner: apache
              group: apache
            /etc/cfn/cfn-hup.conf:
              content: !Sub |
                [main]
                stack=${AWS::StackId}
                region=${AWS::Region}
                # The interval used to check for changes to the resource metadata in minutes. Default is 15
                interval=2
              mode: '000400'
              owner: root
              group: root
            /etc/cfn/hooks.d/cfn-auto-reloader.conf:
              content: !Sub |
                [cfn-auto-reloader-hook]
                triggers=post.update
                path=Resources.WebServerInstance.Metadata.AWS::CloudFormation::Init
                action=/opt/aws/bin/cfn-init -s ${AWS::StackId} -r WebServerInstance --region ${AWS::Region}
                runas=root
          services:
            systemd:
              httpd:
                enabled: true
                ensureRunning: true
              cfn-hup:
                enabled: true
                ensureRunning: true
                files:
                  - /etc/cfn/cfn-hup.conf
                  - /etc/cfn/hooks.d/cfn-auto-reloader.conf
    CreationPolicy:
      ResourceSignal:
        Timeout: PT5M

  WebServerSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Enable HTTP access via port 80 and SSH access via port 22
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: !Ref SSHLocation

Outputs:
  WebsiteURL:
    Value: !Sub 'http://${WebServerInstance.PublicDnsName}'
    Description: URL of the web application
```

Update the stack using the same steps as explained in [Step 2: Update the application](#update-stack-update-application "#update-stack-update-application").

After the new instance is running, CloudFormation updates the other resources in the stack to
point to the new resource. When all new resources are created, the old resource is deleted, a
process known as `UPDATE_CLEANUP`. This time, you will notice that the instance ID
and application URL of the instance in the stack has changed as a result of the update. The
events in the **Event** table contain a description "Requested update has a
change to an immutable property and hence creating a new physical resource" to indicate that a
resource was replaced.

Alternatively: If you have application code written into the AMI that you want to update,
you can use the same stack update mechanism to update the AMI to load your new
application.

###### To update the AMI with custom application code

1. Create your new AMI containing your application or operating system changes. For more
   information, see [Create an Amazon EBS-backed
   AMI](../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md "../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md") in the _Amazon EC2 User Guide_.
2. Update your template to incorporate the new AMI ID.
3. Update the stack using the same steps as explained in [Step 2: Update the application](#update-stack-update-application "#update-stack-update-application").

When you update the stack, CloudFormation detects that the AMI ID has changed, and then it
triggers a stack update in the same way as we initiated the one above.

## Availability and impact considerations

Different properties have different impacts on the resources in the stack. You can use
CloudFormation to update any property; however, before you make any changes, you should consider
these questions:

1. How does the update affect the resource itself? For example, updating an alarm
   threshold will render the alarm inactive during the update. As we have seen, changing the
   instance type requires that the instance be stopped and restarted. CloudFormation uses the
   update or modify actions for the underlying resources to make changes to resources. To
   understand the impact of updates, you should check the documentation for the specific
   resources.
2. Is the change mutable or immutable? Some changes to resource properties, such as
   changing the AMI on an Amazon EC2 instance, aren't supported by the underlying services. In the
   case of mutable changes, CloudFormation will use the Update or Modify type APIs for the
   underlying resources. For immutable property changes, CloudFormation will create new resources
   with the updated properties and then link them to the stack before deleting the old
   resources. Although CloudFormation tries to reduce the down time of the stack resources,
   replacing a resource is a multistep process, and it will take time. During stack
   reconfiguration, your application will not be fully operational. For example, it may not
   be able to serve requests or access a database.

## Related resources

For more information about using CloudFormation to start applications and on integrating with
other configuration and deployment services such as Puppet and Opscode
Chef, see the following whitepapers:

- [Bootstrapping applications via CloudFormation](https://s3.amazonaws.com/cloudformation-examples/BoostrappingApplicationsWithAWSCloudFormation.pdf "https://s3.amazonaws.com/cloudformation-examples/BoostrappingApplicationsWithAWSCloudFormation.pdf")
- [Integrating CloudFormation with Opscode Chef](https://s3.amazonaws.com/cloudformation-examples/IntegratingAWSCloudFormationWithOpscodeChef.pdf "https://s3.amazonaws.com/cloudformation-examples/IntegratingAWSCloudFormationWithOpscodeChef.pdf")
- [Integrating CloudFormation with Puppet](https://s3.amazonaws.com/cloudformation-examples/IntegratingAWSCloudFormationWithPuppet.pdf "https://s3.amazonaws.com/cloudformation-examples/IntegratingAWSCloudFormationWithPuppet.pdf")
