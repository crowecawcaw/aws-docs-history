# AWS Identity and Access Management template snippets

This section contains AWS Identity and Access Management template snippets.

###### Topics

- [Declaring an IAM user resource](#scenario-iam-user "#scenario-iam-user")
- [Declaring an IAM access key resource](#scenario-iam-accesskey "#scenario-iam-accesskey")
- [Declaring an IAM group resource](#scenario-iam-group "#scenario-iam-group")
- [Adding users to a group](#scenario-iam-addusertogroup "#scenario-iam-addusertogroup")
- [Declaring an IAM policy](#scenario-iam-policy "#scenario-iam-policy")
- [Declaring an Amazon S3 bucket policy](#scenario-bucket-policy "#scenario-bucket-policy")
- [Declaring an Amazon SNS topic policy](#scenario-sns-policy "#scenario-sns-policy")
- [Declaring an Amazon SQS policy](#scenario-sqs-policy "#scenario-sqs-policy")
- [IAM role template examples](#scenarios-iamroles "#scenarios-iamroles")

###### Important

When creating or updating a stack using a template containing IAM resources, you must
acknowledge the use of IAM capabilities. For more information, see [Acknowledging IAM resources in CloudFormation
templates](control-access-with-iam.md#using-iam-capabilities "control-access-with-iam.md#using-iam-capabilities").

## Declaring an IAM user resource

This snippet shows how to declare an [AWS::IAM::User](../TemplateReference/aws-resource-iam-user.md "../TemplateReference/aws-resource-iam-user.md") resource to create an IAM user. The user is
declared with the path (`"/"`) and a login profile with the password
(`myP@ssW0rd`).

The policy document named `giveaccesstoqueueonly` gives the user permission
to perform all Amazon SQS actions on the Amazon SQS queue resource `myqueue`, and denies
access to all other Amazon SQS queue resources. The `Fn::GetAtt` function gets the
Arn attribute of the [AWS::SQS::Queue](../TemplateReference/aws-resource-sqs-queue.md "../TemplateReference/aws-resource-sqs-queue.md") resource `myqueue`.

The policy document named `giveaccesstotopiconly` is added to the user to
give the user permission to perform all Amazon SNS actions on the Amazon SNS topic resource
`mytopic` and to deny access to all other Amazon SNS resources. The
`Ref` function gets the ARN of the [AWS::SNS::Topic](../TemplateReference/aws-resource-sns-topic.md "../TemplateReference/aws-resource-sns-topic.md") resource `mytopic`.

### JSON

```
"myuser" : {
   "Type" : "AWS::IAM::User",
   "Properties" : {
      "Path" : "/",
      "LoginProfile" : {
         "Password" : "myP@ssW0rd"
      },
      "Policies" : [ {
         "PolicyName" : "giveaccesstoqueueonly",
         "PolicyDocument" : {
            "Version": "2012-10-17",
            "Statement" : [ {
               "Effect" : "Allow",
               "Action" : [ "sqs:*" ],
               "Resource" : [ {
                  "Fn::GetAtt" : [ "myqueue", "Arn" ]
               } ]
            }, {
               "Effect" : "Deny",
               "Action" : [ "sqs:*" ],
               "NotResource" : [ {
                  "Fn::GetAtt" : [ "myqueue", "Arn" ]
               } ]
            }
         ] }
      }, {
         "PolicyName" : "giveaccesstotopiconly",
         "PolicyDocument" : {
            "Version": "2012-10-17",
            "Statement" : [ {
               "Effect" : "Allow",
               "Action" : [ "sns:*" ],
               "Resource" : [ { "Ref" : "mytopic" } ]
            }, {
               "Effect" : "Deny",
               "Action" : [ "sns:*" ],
               "NotResource" : [ { "Ref" : "mytopic" } ]
            } ]
         }
      } ]
   }
}
```

### YAML

```
myuser:
  Type: AWS::IAM::User
  Properties:
    Path: "/"
    LoginProfile:
      Password: myP@ssW0rd
    Policies:
    - PolicyName: giveaccesstoqueueonly
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
        - Effect: Allow
          Action:
          - sqs:*
          Resource:
          - !GetAtt myqueue.Arn
        - Effect: Deny
          Action:
          - sqs:*
          NotResource:
          - !GetAtt myqueue.Arn
    - PolicyName: giveaccesstotopiconly
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
        - Effect: Allow
          Action:
          - sns:*
          Resource:
          - !Ref mytopic
        - Effect: Deny
          Action:
          - sns:*
          NotResource:
          - !Ref mytopic
```

## Declaring an IAM access key resource

###

This snippet shows an [AWS::IAM::AccessKey](../TemplateReference/aws-resource-iam-accesskey.md "../TemplateReference/aws-resource-iam-accesskey.md") resource. The `myaccesskey`
resource creates an access key and assigns it to an IAM user that is declared as an
[AWS::IAM::User](../TemplateReference/aws-resource-iam-user.md "../TemplateReference/aws-resource-iam-user.md") resource in the template.

#### JSON

```
"myaccesskey" : {
   "Type" : "AWS::IAM::AccessKey",
   "Properties" : {
      "UserName" : { "Ref" : "myuser" }
   }
}
```

#### YAML

```
myaccesskey:
  Type: AWS::IAM::AccessKey
  Properties:
    UserName:
      !Ref myuser
```

###

You can get the secret key for an `AWS::IAM::AccessKey` resource using the
`Fn::GetAtt` function. One way to retrieve the secret key is to put it
into an `Output` value. You can get the access key using the `Ref`
function. The following `Output` value declarations get the access key and
secret key for `myaccesskey`.

#### JSON

```
"AccessKeyformyaccesskey" : {
   "Value" : { "Ref" : "myaccesskey" }
},
"SecretKeyformyaccesskey" : {
   "Value" : {
      "Fn::GetAtt" : [ "myaccesskey", "SecretAccessKey" ]
   }
}
```

#### YAML

```
AccessKeyformyaccesskey:
  Value:
    !Ref myaccesskey
SecretKeyformyaccesskey:
  Value: !GetAtt myaccesskey.SecretAccessKey
```

###

You can also pass the AWS access key and secret key to an Amazon EC2 instance or Auto
Scaling group defined in the template. The following [AWS::EC2::Instance](../TemplateReference/aws-resource-ec2-instance.md "../TemplateReference/aws-resource-ec2-instance.md") declaration uses the
`UserData` property to pass the access key and secret key for the
`myaccesskey` resource.

#### JSON

```
"myinstance" : {
   "Type" : "AWS::EC2::Instance",
   "Properties" : {
      "AvailabilityZone" : "us-east-1a",
      "ImageId" : "ami-0ff8a91507f77f867",
      "UserData" : {
         "Fn::Base64" : {
            "Fn::Join" : [
               "", [
                  "ACCESS_KEY=", {
                     "Ref" : "myaccesskey"
                  },
                  "&",
                  "SECRET_KEY=",
                  {
                     "Fn::GetAtt" : [
                        "myaccesskey",
                        "SecretAccessKey"
                     ]
                  }
               ]
            ]
         }
      }
   }
}
```

#### YAML

```
myinstance:
  Type: AWS::EC2::Instance
  Properties:
    AvailabilityZone: "us-east-1a"
    ImageId: ami-0ff8a91507f77f867
    UserData:
      Fn::Base64: !Sub "ACCESS_KEY=${myaccesskey}&SECRET_KEY=${myaccesskey.SecretAccessKey}"
```

## Declaring an IAM group resource

This snippet shows an [AWS::IAM::Group](../TemplateReference/aws-resource-iam-group.md "../TemplateReference/aws-resource-iam-group.md") resource. The group has a path
(`"/myapplication/"`). The policy document named `myapppolicy` is
added to the group to allow the group's users to perform all Amazon SQS actions on the Amazon SQS
queue resource myqueue and deny access to all other Amazon SQS resources except
`myqueue`.

To assign a policy to a resource, IAM requires the Amazon Resource Name (ARN) for the
resource. In the snippet, the `Fn::GetAtt` function gets the ARN of the [AWS::SQS::Queue](../TemplateReference/aws-resource-sqs-queue.md "../TemplateReference/aws-resource-sqs-queue.md") resource queue.

### JSON

```
"mygroup" : {
   "Type" : "AWS::IAM::Group",
   "Properties" : {
      "Path" : "/myapplication/",
      "Policies" : [ {
         "PolicyName" : "myapppolicy",
         "PolicyDocument" : {
            "Version": "2012-10-17",
            "Statement" : [ {
               "Effect" : "Allow",
               "Action" : [ "sqs:*" ],
               "Resource" : [ {
                  "Fn::GetAtt" : [ "myqueue", "Arn" ]
               } ]
            },
            {
               "Effect" : "Deny",
               "Action" : [ "sqs:*" ],
               "NotResource" : [ { "Fn::GetAtt" : [ "myqueue", "Arn" ] } ]
            }
         ] }
      } ]
   }
}
```

### YAML

```
mygroup:
  Type: AWS::IAM::Group
  Properties:
    Path: "/myapplication/"
    Policies:
    - PolicyName: myapppolicy
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
        - Effect: Allow
          Action:
          - sqs:*
          Resource: !GetAtt myqueue.Arn
        - Effect: Deny
          Action:
          - sqs:*
          NotResource: !GetAtt myqueue.Arn
```

## Adding users to a group

The [AWS::IAM::UserToGroupAddition](../TemplateReference/aws-resource-iam-usertogroupaddition.md "../TemplateReference/aws-resource-iam-usertogroupaddition.md") resource adds users to a group.
In the following snippet, the `addUserToGroup` resource adds the following users
to an existing group named `myexistinggroup2`: the existing user
`existinguser1` and the user `myuser` which is declared as an
[AWS::IAM::User](../TemplateReference/aws-resource-iam-user.md "../TemplateReference/aws-resource-iam-user.md") resource in the template.

### JSON

```
"addUserToGroup" : {
   "Type" : "AWS::IAM::UserToGroupAddition",
   "Properties" : {
      "GroupName" : "myexistinggroup2",
      "Users" : [ "existinguser1", { "Ref" : "myuser" } ]
   }
}
```

### YAML

```
addUserToGroup:
  Type: AWS::IAM::UserToGroupAddition
  Properties:
    GroupName: myexistinggroup2
    Users:
    - existinguser1
    - !Ref myuser
```

## Declaring an IAM policy

This snippet shows how to create a policy and apply it to multiple groups using an
[AWS::IAM::Policy](../TemplateReference/aws-resource-iam-policy.md "../TemplateReference/aws-resource-iam-policy.md") resource named `mypolicy`. The
`mypolicy` resource contains a `PolicyDocument` property that
allows `GetObject`, `PutObject`, and `PutObjectAcl`
actions on the objects in the S3 bucket represented by the ARN
`arn:aws:s3:::myAWSBucket`. The `mypolicy` resource applies the
policy to an existing group named `myexistinggroup1` and a group
`mygroup` that's declared in the template as an [AWS::IAM::Group](../TemplateReference/aws-resource-iam-group.md "../TemplateReference/aws-resource-iam-group.md") resource. This example shows how to apply a
policy to a group using the `Groups` property; however, you can alternatively
use the `Users` property to add a policy document to a list of users.

### JSON

```
"mypolicy" : {
   "Type" : "AWS::IAM::Policy",
   "Properties" : {
      "PolicyName" : "mygrouppolicy",
      "PolicyDocument" : {
         "Version": "2012-10-17",
         "Statement" : [ {
            "Effect" : "Allow",
            "Action" : [
               "s3:GetObject" , "s3:PutObject" , "s3:PutObjectAcl" ],
            "Resource" : "arn:aws:s3:::myAWSBucket/*"
         } ]
      },
      "Groups" : [ "myexistinggroup1", { "Ref" : "mygroup" } ]
   }
}
```

### YAML

```
mypolicy:
  Type: AWS::IAM::Policy
  Properties:
    PolicyName: mygrouppolicy
    PolicyDocument:
      Version: '2012-10-17'
      Statement:
      - Effect: Allow
        Action:
        - s3:GetObject
        - s3:PutObject
        - s3:PutObjectAcl
        Resource: arn:aws:s3:::myAWSBucket/*
    Groups:
    - myexistinggroup1
    - !Ref mygroup
```

## Declaring an Amazon S3 bucket policy

This snippet shows how to create a policy and apply it to an Amazon S3 bucket using the
[AWS::S3::BucketPolicy](../TemplateReference/aws-resource-s3-bucket.md "../TemplateReference/aws-resource-s3-bucket.md") resource. The
`mybucketpolicy` resource declares a policy document that allows the
`user1` IAM user to perform the `GetObject` action on all
objects in the S3 bucket to which this policy is applied. In the snippet, the
`Fn::GetAtt` function gets the ARN of the `user1` resource. The
`mybucketpolicy` resource applies the policy to the
`AWS::S3::BucketPolicy` resource mybucket. The `Ref` function gets
the bucket name of the `mybucket` resource.

### JSON

```
"mybucketpolicy" : {
   "Type" : "AWS::S3::BucketPolicy",
   "Properties" : {
      "PolicyDocument" : {
         "Id" : "MyPolicy",
         "Version": "2012-10-17",
         "Statement" : [ {
            "Sid" : "ReadAccess",
            "Action" : [ "s3:GetObject" ],
            "Effect" : "Allow",
            "Resource" : { "Fn::Join" : [
                  "", [ "arn:aws:s3:::", { "Ref" : "mybucket" } , "/*" ]
               ] },
            "Principal" : {
               "AWS" : { "Fn::GetAtt" : [ "user1", "Arn" ] }
            }
         } ]
      },
      "Bucket" : { "Ref" : "mybucket" }
   }
}
```

### YAML

```
mybucketpolicy:
  Type: AWS::S3::BucketPolicy
  Properties:
    PolicyDocument:
      Id: MyPolicy
      Version: '2012-10-17'
      Statement:
      - Sid: ReadAccess
        Action:
        - s3:GetObject
        Effect: Allow
        Resource: !Sub "arn:aws:s3:::${mybucket}/*"
        Principal:
          AWS: !GetAtt user1.Arn
    Bucket: !Ref mybucket
```

## Declaring an Amazon SNS topic policy

This snippet shows how to create a policy and apply it to an Amazon SNS topic using the
[AWS::SNS::TopicPolicy](../TemplateReference/aws-resource-sns-topicpolicy.md "../TemplateReference/aws-resource-sns-topicpolicy.md") resource. The `mysnspolicy`
resource contains a `PolicyDocument` property that allows the [AWS::IAM::User](../TemplateReference/aws-resource-iam-user.md "../TemplateReference/aws-resource-iam-user.md") resource `myuser` to perform the
`Publish` action on an [AWS::SNS::Topic](../TemplateReference/aws-resource-sns-topic.md "../TemplateReference/aws-resource-sns-topic.md") resource `mytopic`. In the
snippet, the `Fn::GetAtt` function gets the ARN for the `myuser`
resource and the `Ref` function gets the ARN for the `mytopic`
resource.

### JSON

```
"mysnspolicy" : {
   "Type" : "AWS::SNS::TopicPolicy",
   "Properties" : {
      "PolicyDocument" :  {
         "Id" : "MyTopicPolicy",
         "Version": "2012-10-17",
         "Statement" : [ {
            "Sid" : "My-statement-id",
            "Effect" : "Allow",
            "Principal" : {
               "AWS" : { "Fn::GetAtt" : [ "myuser", "Arn" ] }
            },
            "Action" : "sns:Publish",
            "Resource" : "*"
         } ]
      },
      "Topics" : [ { "Ref" : "mytopic" } ]
   }
}
```

### YAML

```
mysnspolicy:
  Type: AWS::SNS::TopicPolicy
  Properties:
    PolicyDocument:
      Id: MyTopicPolicy
      Version: '2012-10-17'
      Statement:
      - Sid: My-statement-id
        Effect: Allow
        Principal:
          AWS: !GetAtt myuser.Arn
        Action: sns:Publish
        Resource: "*"
    Topics:
    - !Ref mytopic
```

## Declaring an Amazon SQS policy

This snippet shows how to create a policy and apply it to an Amazon SQS queue using the
[AWS::SQS::QueuePolicy](../TemplateReference/aws-resource-sqs-queuepolicy.md "../TemplateReference/aws-resource-sqs-queuepolicy.md") resource. The
`PolicyDocument` property allows the existing user `myapp`
(specified by its ARN) to perform the `SendMessage` action on an existing queue,
which is specified by its URL, and an [AWS::SQS::Queue](../TemplateReference/aws-resource-sqs-queue.md "../TemplateReference/aws-resource-sqs-queue.md") resource myqueue. The [Ref](resources-section-structure.md#resource-properties-ref "resources-section-structure.md#resource-properties-ref") function gets the URL for the
`myqueue` resource.

### JSON

```
"mysqspolicy" : {
   "Type" : "AWS::SQS::QueuePolicy",
   "Properties" : {
      "PolicyDocument" : {
         "Id" : "MyQueuePolicy",
         "Version": "2012-10-17",
         "Statement" : [ {
            "Sid" : "Allow-User-SendMessage",
            "Effect" : "Allow",
            "Principal" : {
               "AWS" : "arn:aws:iam::123456789012:user/myapp"
            },
            "Action" : [ "sqs:SendMessage" ],
            "Resource" : "*"
         } ]
      },
      "Queues" : [
         "https://sqs.us-east-2`aws-region`.amazonaws.com/123456789012/myexistingqueue",
         { "Ref" : "myqueue" }
      ]
   }
}
```

### YAML

```
mysqspolicy:
  Type: AWS::SQS::QueuePolicy
  Properties:
    PolicyDocument:
      Id: MyQueuePolicy
      Version: '2012-10-17'
      Statement:
      - Sid: Allow-User-SendMessage
        Effect: Allow
        Principal:
          AWS: arn:aws:iam::123456789012:user/myapp
        Action:
        - sqs:SendMessage
        Resource: "*"
    Queues:
    - https://sqs.`aws-region`.amazonaws.com/123456789012/myexistingqueue
    - !Ref myqueue
```

## IAM role template examples

This section provides CloudFormation template examples for IAM roles for EC2
instances.

For more information, see [IAM roles for Amazon EC2](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md") in the
_Amazon EC2 User Guide_.

### IAM role with EC2

In this example, the instance profile is referenced by the
`IamInstanceProfile` property of the EC2 instance. Both the instance
policy and role policy reference [AWS::IAM::Role](../TemplateReference/aws-resource-iam-role.md "../TemplateReference/aws-resource-iam-role.md").

#### JSON

```
{
   "AWSTemplateFormatVersion": "2010-09-09",
   "Resources": {
      "myEC2Instance": {
         "Type": "AWS::EC2::Instance",
         "Version": "2009-05-15",
         "Properties": {
            "ImageId": "ami-0ff8a91507f77f867",
            "InstanceType": "m1.small",
            "Monitoring": "true",
            "DisableApiTermination": "false",
            "IamInstanceProfile": {
               "Ref": "RootInstanceProfile"
            }
         }
      },
      "RootRole": {
         "Type": "AWS::IAM::Role",
         "Properties": {
            "AssumeRolePolicyDocument": {
               "Version": "2012-10-17",
               "Statement": [ {
                  "Effect": "Allow",
                  "Principal": {
                     "Service": [ "ec2.amazonaws.com" ]
                  },
                  "Action": [ "sts:AssumeRole" ]
               } ]
            },
            "Path": "/"
         }
      },
      "RolePolicies": {
         "Type": "AWS::IAM::Policy",
         "Properties": {
            "PolicyName": "root",
            "PolicyDocument": {
               "Version": "2012-10-17",
               "Statement": [ {
                  "Effect": "Allow",
                  "Action": "*",
                  "Resource": "*"
               } ]
            },
            "Roles": [ { "Ref": "RootRole" } ]
         }
      },
      "RootInstanceProfile": {
         "Type": "AWS::IAM::InstanceProfile",
         "Properties": {
            "Path": "/",
            "Roles": [ { "Ref": "RootRole" } ]
         }
      }
   }
}
```

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  myEC2Instance:
    Type: AWS::EC2::Instance
    Version: '2009-05-15'
    Properties:
      ImageId: ami-0ff8a91507f77f867
      InstanceType: m1.small
      Monitoring: 'true'
      DisableApiTermination: 'false'
      IamInstanceProfile:
        !Ref RootInstanceProfile
  RootRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - ec2.amazonaws.com
          Action:
          - sts:AssumeRole
      Path: "/"
  RolePolicies:
    Type: AWS::IAM::Policy
    Properties:
      PolicyName: root
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
        - Effect: Allow
          Action: "*"
          Resource: "*"
      Roles:
      - !Ref RootRole
  RootInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: "/"
      Roles:
      - !Ref RootRole
```

### IAM role with Auto Scaling group

In this example, the instance profile is referenced by the
`IamInstanceProfile` property of an Amazon EC2 Auto Scaling launch
configuration.

#### JSON

```
{
   "AWSTemplateFormatVersion": "2010-09-09",
   "Resources": {
      "myLCOne": {
         "Type": "AWS::AutoScaling::LaunchConfiguration",
         "Version": "2009-05-15",
         "Properties": {
            "ImageId": "ami-0ff8a91507f77f867",
            "InstanceType": "m1.small",
            "InstanceMonitoring": "true",
            "IamInstanceProfile": { "Ref": "RootInstanceProfile" }
         }
      },
      "myASGrpOne": {
         "Type": "AWS::AutoScaling::AutoScalingGroup",
         "Version": "2009-05-15",
         "Properties": {
            "AvailabilityZones": [ "us-east-1a" ],
            "LaunchConfigurationName": { "Ref": "myLCOne" },
            "MinSize": "0",
            "MaxSize": "0",
            "HealthCheckType": "EC2",
            "HealthCheckGracePeriod": "120"
         }
      },
      "RootRole": {
         "Type": "AWS::IAM::Role",
         "Properties": {
            "AssumeRolePolicyDocument": {
               "Version": "2012-10-17",
               "Statement": [ {
                  "Effect": "Allow",
                  "Principal": {
                     "Service": [ "ec2.amazonaws.com" ]
                  },
                  "Action": [ "sts:AssumeRole" ]
               } ]
            },
            "Path": "/"
         }
      },
      "RolePolicies": {
         "Type": "AWS::IAM::Policy",
         "Properties": {
            "PolicyName": "root",
            "PolicyDocument": {
               "Version": "2012-10-17",
               "Statement": [ {
                  "Effect": "Allow",
                  "Action": "*",
                  "Resource": "*"
               } ]
            },
            "Roles": [ { "Ref": "RootRole" } ]
         }
      },
      "RootInstanceProfile": {
         "Type": "AWS::IAM::InstanceProfile",
         "Properties": {
            "Path": "/",
            "Roles": [ { "Ref": "RootRole" } ]
         }
      }
   }
}
```

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  myLCOne:
    Type: AWS::AutoScaling::LaunchConfiguration
    Version: '2009-05-15'
    Properties:
      ImageId: ami-0ff8a91507f77f867
      InstanceType: m1.small
      InstanceMonitoring: 'true'
      IamInstanceProfile:
        !Ref RootInstanceProfile
  myASGrpOne:
    Type: AWS::AutoScaling::AutoScalingGroup
    Version: '2009-05-15'
    Properties:
      AvailabilityZones:
      - "us-east-1a"
      LaunchConfigurationName:
        !Ref myLCOne
      MinSize: '0'
      MaxSize: '0'
      HealthCheckType: EC2
      HealthCheckGracePeriod: '120'
  RootRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - ec2.amazonaws.com
          Action:
          - sts:AssumeRole
      Path: "/"
  RolePolicies:
    Type: AWS::IAM::Policy
    Properties:
      PolicyName: root
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
        - Effect: Allow
          Action: "*"
          Resource: "*"
      Roles:
      - !Ref RootRole
  RootInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: "/"
      Roles:
      - !Ref RootRole
```
