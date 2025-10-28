# Tagging an EC2 instance with AWS CloudFormation for Accelerate

The following is an example of how you can apply the tag
**ams:rt:ams-managed** with the value **true** to an
Amazon EC2 instance managed by AWS CloudFormation. The **ams:rt:ams-managed** tag opts you in
to having your resources monitored by AMS Accelerate.

```

 Type: AWS::EC2::Instance

Properties:
  InstanceType: "t3.micro"

  # ...other properties...

  Tags:
    - Key: "ams:rt:ams-managed"
      Value: "true"

```
