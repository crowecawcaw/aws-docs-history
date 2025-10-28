# Tagging an AutoScaling Group (ASG) with AWS CloudFormation for Accelerate

The following is an example of how you can apply the tag
**ams:rt:ams-managed** with the value **true** to an
Auto Scaling group managed by AWS CloudFormation. Note that the Auto Scaling group will propagate its
tags to Amazon EC2 instances that are created by it. The **ams:rt:ams-managed**
tag opts you in to having your resources monitored by AMS Accelerate.

```

  Type: AWS::AutoScaling::AutoScalingGroup
Properties:
  AutoScalingGroupName: "SampleASG"

  # ...other properties...

  Tags:
    - Key: "ams:rt:ams-managed"
      Value: "true"

```
