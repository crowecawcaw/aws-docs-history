

# Create launch templates with CloudFormation
<a name="quickref-ec2-launch-templates"></a>

This section provides an example for creating an Amazon EC2 launch template using CloudFormation. Launch templates allow you to create templates for configuring and provisioning Amazon EC2 instances within AWS. With launch templates, you can store launch parameters so that you do not have to specify them every time you launch an instance. For more examples, see the [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-launchtemplate.html#aws-resource-ec2-launchtemplate--examples) section in the `AWS::EC2::LaunchTemplate` resource.

For more information about launch templates, see [Store instance launch parameters in Amazon EC2 launch templates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*. 

For information about creating launch templates for use with Auto Scaling groups, see [Auto Scaling launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html) in the *Amazon EC2 Auto Scaling User Guide*.

**Topics**
+ [Create a launch template that specifies security groups, tags, user data, and an IAM role](#scenario-as-launch-template)

## Create a launch template that specifies security groups, tags, user data, and an IAM role
<a name="scenario-as-launch-template"></a>

This snippet shows an [AWS::EC2::LaunchTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-launchtemplate.html) resource that contains the configuration information to launch an instance. You specify values for the `ImageId`, `InstanceType`, `SecurityGroups`, `UserData`, and `TagSpecifications` properties. The `SecurityGroups` property specifies an existing EC2 security group and a new security group. The `Ref` function gets the ID of the [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html) resource `myNewEC2SecurityGroup` that's declared elsewhere in the stack template. 

The launch template includes a section for custom user data. You can pass in configuration tasks and scripts that run when an instance launches in this section. In this example, the user data installs the AWS Systems Manager Agent and starts the agent.

The launch template also includes an IAM role that allows applications running on instances to perform actions on your behalf. This example shows an [AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html) resource for the launch template, which uses the `IamInstanceProfile` property to specify the IAM role. The `Ref` function gets the name of the [AWS::IAM::InstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html) resource `myInstanceProfile`. To configure the permissions of the IAM role, you specify a value for the `ManagedPolicyArns` property.

### JSON
<a name="quickref-launch-template-example-1.json"></a>

```
 1. {
 2.   "Resources":{
 3.     "myLaunchTemplate":{
 4.       "Type":"AWS::EC2::LaunchTemplate",
 5.       "Properties":{
 6.         "LaunchTemplateName":{ "Fn::Sub": "${AWS::StackName}-launch-template" },
 7.         "LaunchTemplateData":{
 8.           "ImageId":"{{ami-02354e95b3example}}",
 9.           "InstanceType":"{{t3.micro}}",
10.           "IamInstanceProfile":{
11.             "Name":{
12.               "Ref":"myInstanceProfile"
13.             }
14.           },
15.           "SecurityGroupIds":[
16.             {
17.               "Ref":"{{myNewEC2SecurityGroup}}"
18.             },
19.             "{{sg-083cd3bfb8example}}"
20.           ],
21.           "UserData":{
22.             "Fn::Base64":{
23.               "Fn::Join": [
24.                 "", [
25.                   "{{#!/bin/bash\n}}",
26.                   "{{cd /tmp\n}}",
27.                   "{{yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm\n}}",
28.                   "{{systemctl enable amazon-ssm-agent\n}}",
29.                   "{{systemctl start amazon-ssm-agent\n}}"
30.                 ]
31.               ]
32.             }
33.           },
34.           "TagSpecifications":[
35.             {
36.               "ResourceType":"instance",
37.               "Tags":[
38.                 {
39.                   "Key":"{{environment}}",
40.                   "Value":"{{development}}"
41.                 }
42.               ]
43.             },
44.             {
45.               "ResourceType":"volume",
46.               "Tags":[
47.                 {
48.                   "Key":"{{environment}}",
49.                   "Value":"{{development}}"
50.                 }
51.               ]
52.             }
53.           ]
54.         }
55.       }
56.     },
57.     "myInstanceRole":{
58.       "Type":"AWS::IAM::Role",
59.       "Properties":{
60.         "RoleName":"InstanceRole",
61.         "AssumeRolePolicyDocument":{
62.           "Version": "2012-10-17",		 	 	 
63.           "Statement":[
64.             {
65.               "Effect":"Allow",
66.               "Principal":{
67.                 "Service":[
68.                   "ec2.amazonaws.com"
69.                 ]
70.               },
71.               "Action":[
72.                 "sts:AssumeRole"
73.               ]
74.             }
75.           ]
76.         },
77.         "ManagedPolicyArns":[
78.           "arn:aws:iam::aws:policy/{{myCustomerManagedPolicy}}"
79.         ]
80.       }
81.     },
82.     "myInstanceProfile":{
83.       "Type":"AWS::IAM::InstanceProfile",
84.       "Properties":{
85.         "Path":"/",
86.         "Roles":[
87.           {
88.             "Ref":"myInstanceRole"
89.           }
90.         ]
91.       }
92.     }
93.   }
94. }
```

### YAML
<a name="quickref-launch-template-example-1.yaml"></a>

```
 1. ---
 2. Resources:
 3.   myLaunchTemplate:
 4.     Type: AWS::EC2::LaunchTemplate
 5.     Properties:
 6.       LaunchTemplateName: !Sub ${AWS::StackName}-launch-template
 7.       LaunchTemplateData:
 8.         ImageId: {{ami-02354e95b3example}}
 9.         InstanceType: {{t3.micro}}
10.         IamInstanceProfile:
11.           Name: !Ref myInstanceProfile
12.         SecurityGroupIds:
13.         - !Ref {{myNewEC2SecurityGroup}}
14.         - {{sg-083cd3bfb8example}}
15.         UserData:
16.           Fn::Base64: !Sub |
17.             {{#!/bin/bash
18.             cd /tmp
19.             yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm
20.             systemctl enable amazon-ssm-agent
21.             systemctl start amazon-ssm-agent}}
22.         TagSpecifications:
23.         - ResourceType: instance
24.           Tags:
25.           - Key: {{environment}}
26.             Value: {{development}}
27.         - ResourceType: volume
28.           Tags:
29.           - Key: {{environment}}
30.             Value: {{development}}
31.   myInstanceRole:
32.     Type: AWS::IAM::Role
33.     Properties:
34.       RoleName: InstanceRole
35.       AssumeRolePolicyDocument:
36.         Version: '2012-10-17'
37.         Statement:
38.         - Effect: 'Allow'
39.           Principal:
40.             Service:
41.             - 'ec2.amazonaws.com'
42.           Action:
43.           - 'sts:AssumeRole'
44.       ManagedPolicyArns:
45.         - 'arn:aws:iam::aws:policy/{{myCustomerManagedPolicy}}'
46.   myInstanceProfile:
47.     Type: AWS::IAM::InstanceProfile
48.     Properties:
49.       Path: '/'
50.       Roles:
51.       - !Ref myInstanceRole
```