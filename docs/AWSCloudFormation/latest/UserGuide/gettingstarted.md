# Creating your first stack

This topic walks you through creating your first CloudFormation stack using the AWS Management Console. By
following this tutorial, you'll learn how to provision basic AWS resources, monitor stack
events, and generate outputs.

For this example, the CloudFormation template is written in YAML. YAML is a human-readable
format that's widely used for defining infrastructure as code. As you learn more about
CloudFormation, you might also encounter other templates in JSON format, but for this tutorial,
YAML is chosen for its readability.

###### Note

CloudFormation is free, but you'll be charged for the Amazon EC2 and Amazon S3 resources you create.
However, if you're new to AWS, you can take advantage of the [Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") to minimize or eliminate costs during this learning
process.

###### Topics

- [Prerequisites](#getting-started-prerequisites "#getting-started-prerequisites")
- [Create a CloudFormation stack with the
  console](#getting-started-create-stack "#getting-started-create-stack")
- [Monitor stack creation](#getting-started-monitor-stack-creation "#getting-started-monitor-stack-creation")
- [Test the web server](#getting-started-test-web-server "#getting-started-test-web-server")
- [Troubleshooting](#getting-started-troubleshooting "#getting-started-troubleshooting")
- [Clean up](#getting-started-clean-up "#getting-started-clean-up")
- [Next steps](#getting-started-next-steps "#getting-started-next-steps")

## Prerequisites

- You must have access to an AWS account with an IAM user or role that has
  permissions to use Amazon EC2, Amazon S3, and CloudFormation, or administrative user access.
- You must have a Virtual Private Cloud (VPC) that has access to the internet. This
  walkthrough template requires a default VPC, which comes automatically with newer
  AWS accounts. If you don't have a default VPC, or if it was deleted, see the
  troubleshooting section in this topic for alternative solutions.

## Create a CloudFormation stack with the

console

###### To create a Hello world CloudFormation stack with the console

1.  Open the [CloudFormation
    console](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2.  Choose **Create Stack**.
3.  On the **Create stack** page, choose **Build from
    Infrastructure Composer**, and then **Create in Infrastructure Composer**.
    This takes you to Infrastructure Composer in CloudFormation console mode where you can upload and validate
    the example template.
4.  To upload and validate the example template, do the following:
    1. Choose **Template**. Then, copy and paste the following
       CloudFormation template into the template editor:

    ```
    AWSTemplateFormatVersion: 2010-09-09
    Description: CloudFormation Template for WebServer with Security Group and EC2 Instance

    Parameters:
      LatestAmiId:
        Description: The latest Amazon Linux 2 AMI from the Parameter Store
        Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
        Default: '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2'

      InstanceType:
        Description: WebServer EC2 instance type
        Type: String
        Default: t2.micro
        AllowedValues:
          - t3.micro
          - t2.micro
        ConstraintDescription: must be a valid EC2 instance type.

      MyIP:
        Description: Your IP address in CIDR format (e.g. 203.0.113.1/32).
        Type: String
        MinLength: '9'
        MaxLength: '18'
        Default: 0.0.0.0/0
        AllowedPattern: '^(\d{1,3}\.){3}\d{1,3}\/\d{1,2}$'
        ConstraintDescription: must be a valid IP CIDR range of the form x.x.x.x/x.

    Resources:
      WebServerSecurityGroup:
        Type: AWS::EC2::SecurityGroup
        Properties:
          GroupDescription: Allow HTTP access via my IP address
          SecurityGroupIngress:
            - IpProtocol: tcp
              FromPort: 80
              ToPort: 80
              CidrIp: !Ref MyIP

      WebServer:
        Type: AWS::EC2::Instance
        Properties:
          ImageId: !Ref LatestAmiId
          InstanceType: !Ref InstanceType
          SecurityGroupIds:
            - !Ref WebServerSecurityGroup
          UserData: !Base64 |
            #!/bin/bash
            yum update -y
            yum install -y httpd
            systemctl start httpd
            systemctl enable httpd
            echo "<html><body><h1>Hello World!</h1></body></html>" > /var/www/html/index.html

    Outputs:
      WebsiteURL:
        Value: !Join
          - ''
          - - http://
            - !GetAtt WebServer.PublicDnsName
        Description: Website URL
    ```

    Before you move to the next step, let's take a moment to take a look at the
    template and understand some key CloudFormation concepts.

        * The `Parameters` section
         declares values that can be passed to the template when you create the
         stack. Resources specified later in the template reference these values
         and use the data. Parameters are an effective way to specify information
         that you don't want to store in the template itself. They're also a way
         to specify information that might be unique to the specific application
         or configuration you are deploying.
        * The template defines the following parameters:




        	+ `LatestAmiId` –
        	 Retrieves the latest Amazon Linux 2 AMI ID from the AWS Systems Manager
        	 Parameter Store.
        	+ `InstanceType`
        	 – Allows selection of the EC2 instance type (default:
        	 `t2.micro`, allowed: `t3.micro`,
        	 `t2.micro`).
        	+ `MyIP` –
        	 Specifies the IP address range for HTTP access (default: 0.0.0.0/0,
        	 allowing access from any IP).
        * The `Resources` section
         contains the definitions of the AWS resources you want to create with
         the template. Resource declarations are an efficient way to specify all
         these configuration settings at once. When you include resource
         declarations in a template, you can create and configure all the declared
         resources by using that template to create a stack. You can also create
         new stacks from the same template to launch identical configurations of
         resources.
        * This template creates the following resources:




        	+ `WebServerSecurityGroup` – An EC2
        	 security group that allows inbound HTTP traffic on port 80 from the
        	 specified IP range.
        	+ `WebServer` –
        	 An EC2 instance with the following configuration:




        		- Uses the latest Amazon Linux 2 AMI
        		- Applies the selected instance type
        		- Adds the `WebServerSecurityGroup` to the
        		 `SecurityGroupIds` property
        		- Includes a user data script to install Apache HTTP
        		 Server
        * A logical name is specified at the beginning of each resource and
         parameter declaration. For example, `WebServerSecurityGroup`
         is the logical name assigned to the EC2 security group resource. The
         `Ref` function is then used to reference resources and
         parameters by their logical names in other parts of the template. When
         one resource references another resource, this creates a dependency
         between them.
        * The `Outputs` section
         defines custom values that are returned after the stack creation. You can
         use the output values to return information from the resources in the
         stack, such as resource identifiers or URLs.
        * The template defines one output:




        	+ `WebsiteURL` –
        	 The URL of the deployed web server, constructed using the EC2
        	 instance's public DNS name. The `Join` function helps
        	 combine the fixed `http://` with the variable
        	 `PublicDnsName` into a single string, making it easy
        	 to output the full URL of the web server.

    2. Choose **Validate** to make sure the YAML code is valid
       before uploading the template.
    3. Next, choose **Create template** to create the template and
       add it to an S3 bucket.
    4. From the dialog box that opens, make a note of the name of the S3 bucket so
       you can delete it later. Then, choose **Confirm and continue to
       CloudFormation**. This takes you to the CloudFormation console where the S3
       path to your template is now specified.

5.  On the **Create stack** page, choose
    **Next**.
6.  On the **Specify stack details** page, type a name in the
    **Stack name** field. The stack name can't contain spaces. For
    this example, use `MyTestStack`.
7.  Under **Parameters**, specify parameter values as follows:
    - **LatestAmiId**: This is set by default to the latest
      Amazon Linux 2 AMI.
    - **InstanceType**: Choose either
      **t2.micro** or **t3.micro** for the EC2
      instance type.

    ###### Note

    If you're new to AWS, you can use the free tier to launch and use a
    `t2.micro` instance for free for 12 months (in Regions where
    `t2.micro` is unavailable, you can use a `t3.micro`
    instance under the free tier).
    - **MyIP**: Specify your actual public IP address with a
      `/32` suffix. The `/32` suffix is used in CIDR
      notation to specify that a single IP address is allowed. It essentially means
      allow traffic to and from this specific IP address, and no others.

8.  Choose **Next** twice to go to the **Review and
    create** page. For this tutorial, you can leave the defaults on the
    **Configure stack options** page as they are.
9.  Review the information for the stack. When you're satisfied with the settings,
    choose **Submit**.

## Monitor stack creation

After you choose **Submit**, CloudFormation begins creating the resources
that are specified in the template. Your new stack, `MyTestStack`,
appears in the list at the top portion of the **CloudFormation** console.
Its status should be `CREATE_IN_PROGRESS`. You can see detailed status for a
stack by viewing its events.

###### To view the events for the stack

1. On the CloudFormation console, choose the stack `MyTestStack` in
   the list.
2. In the stack details pane, choose the **Events** tab.

The console automatically refreshes the event list with the most recent events
every 60 seconds.

The **Events** tab displays each major step in the creation of the
stack sorted by the time of each event, with latest events on top.

The first event (at the bottom of the event list) is the start of the stack creation
process:

`2024-12-23 18:54 UTC-7 MyTestStack CREATE_IN_PROGRESS User initiated`

Next are events that mark the beginning and completion of the creation of each resource.
For example, creation of the EC2 instance results in the following entries:

`2024-12-23 18:59 UTC-7 WebServer CREATE_COMPLETE`

`2024-12-23 18:54 UTC-7 WebServer CREATE_IN_PROGRESS Resource creation
 initiated`

The `CREATE_IN_PROGRESS` event is logged when CloudFormation reports that it has
begun to create the resource. The `CREATE_COMPLETE` event is logged when the
resource is successfully created.

When CloudFormation has successfully created the stack, you will see the following event at
the top of the **Events** tab:

`2024-12-23 19:17 UTC-7 MyTestStack CREATE_COMPLETE`

If CloudFormation can't create a resource, it reports a `CREATE_FAILED` event
and, by default, rolls back the stack and deletes any resources that have been created. The
**Status Reason** column displays the issue that caused the
failure.

After the stack is created, you can go to the **Resources** tab to view
the EC2 instance and security group you created.

## Test the web server

After the stack is successfully created, navigate to the **Outputs**
tab in the CloudFormation console. Look for the **WebsiteURL** field. This
will contain the public URL of your EC2 instance.

Open a browser and go to the URL listed under **WebsiteURL**. You
should see a simple "Hello World!" message displayed in the browser.

This confirms that your EC2 instance is running Apache HTTP Server and serving a basic
web page.

## Troubleshooting

If you experience a rollback during stack creation, it might be due to a missing VPC.
Here's how to resolve this issue.

### No default VPC

available

The template in this walkthrough requires a default VPC. If your stack creation fails
because of VPC or subnet availability errors, you might not have a default VPC in your
account. You have the following options:

- Create a new default VPC – You can create
  a new default VPC through the Amazon VPC console. For instructions, see [Create
  a default VPC](../../../vpc/latest/userguide/work-with-default-vpc.md#create-default-vpc "../../../vpc/latest/userguide/work-with-default-vpc.md#create-default-vpc") in the _Amazon VPC User Guide_.
- Modify the template to specify a subnet –
  If you have a non-default VPC, you can modify the template to explicitly specify
  the VPC and subnet IDs. Add the following parameter to the template:

```
  SubnetId:
    Description: The subnet ID to launch the instance into
    Type: AWS::EC2::Subnet::Id

```

Then, update the `WebServer` resource to include the subnet
ID:

```
  WebServer:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !Ref LatestAmiId
      InstanceType: !Ref InstanceType
      SecurityGroupIds:
        - !Ref WebServerSecurityGroup
      SubnetId: !Ref SubnetId
      UserData: !Base64 |
        #!/bin/bash
        yum update -y
        yum install -y httpd
        systemctl start httpd
        systemctl enable httpd
        echo "<html><body><h1>Hello World!</h1></body></html>" > /var/www/html/index.html

```

When creating the stack, you'll need to specify a subnet that has internet
access for the web server to be reachable.

## Clean up

To make sure you aren't charged for any unwanted services, you can clean up by deleting
the stack and its resources. You can also delete the S3 bucket that stores the stack's
template.

###### To delete the stack and its resources

1. Open the [CloudFormation
   console](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the **Stacks** page, select the option next to the name of the
   stack you created (`MyTestStack`) and then choose
   **Delete**.
3. When prompted for confirmation, choose **Delete**.
4. Monitor the progress of the stack deletion process on the
   **Event** tab. The status for `MyTestStack`
   changes to `DELETE_IN_PROGRESS`. When CloudFormation completes the deletion of
   the stack, it removes the stack from the list.

If you are done working with the example template and no longer need your Amazon S3 bucket,
delete it. Before you can delete a bucket, you must first empty it. Emptying a bucket
deletes all objects in it.

###### To empty and delete the Amazon S3 bucket

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane on the left side of the console, choose
   **Buckets**.
3. In the **Buckets** list, select the option next to the name of
   the bucket that you created for this tutorial, and then choose
   **Empty**.
4. On the **Empty bucket** page, confirm that you want to empty the
   bucket by typing `permanently delete` into the text field, and
   then choose **Empty**.
5. Monitor the progress of the bucket emptying process on the **Empty bucket:
   Status** page.
6. To return to your bucket list, choose **Exit**.
7. Select the option next to the name of the bucket, and then choose
   **Delete**.
8. When prompted for confirmation, type the name of the bucket and then choose
   **Delete bucket**.
9. Monitor the progress of the bucket deletion process from the
   **Buckets** list. When Amazon S3 completes the deletion of the bucket,
   it removes the bucket from the list.

## Next steps

Congratulations! You successfully created a stack, monitored its creations, and used its
output.

To continue learning:

- Learn more about templates so that you can create your own. For more information,
  see [Working with CloudFormation templates](template-guide.md "template-guide.md").
- Try the [Getting Started with AWS CloudFormation](https://catalog.us-east-1.prod.workshops.aws/workshops/df7f72cf-4f10-4664-acb6-b30dc8d4bcf0/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/df7f72cf-4f10-4664-acb6-b30dc8d4bcf0/en-US") workshop for more hands-on practice with
  template creation.
- For a shortened version of [Getting Started with AWS CloudFormation](https://catalog.us-east-1.prod.workshops.aws/workshops/df7f72cf-4f10-4664-acb6-b30dc8d4bcf0/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/df7f72cf-4f10-4664-acb6-b30dc8d4bcf0/en-US"), see [Deploy applications on Amazon EC2](deploying.md "deploying.md"). This topic describes the same scenario
  of using a CloudFormation helper script, `cfn-init`, to bootstrap an Amazon EC2
  instance.
