# Accelerate tags using CloudFormation

###### Note

Make sure you have set Resource Tagger to read-only mode first before applying tags using CloudFormation, otherwise Resource Tagger
may modify the tags based on the configuration profile. For information on setting Resource Tagger to read-only mode, and guidelines
on providing your own tags, see [Accelerate tags without Resource Tagger](acc-mem-tags-no-rt.md "acc-mem-tags-no-rt.md").

To apply tags using CloudFormation, you can apply tags at the stack level (see
[CloudFormation Resource Tags](../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md")) or, at the individual resource level, (for example, see
[Creating EC2 Instance Tags](../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.md#cfn-ec2-instance-tags "../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.md#cfn-ec2-instance-tags")).

The following is an example of how you can apply AMS Accelerate alarm management tags to an Amazon EC2
instance managed by CloudFormation:

```
Type: AWS::EC2::Instance
Properties:
 InstanceType: "t3.micro"

 # ...other properties...

 Tags:
   - Key: "aws:rt:ams-monitoring-policy"
     Value: "ams-monitored"
   - Key: "aws:rt:ams-monitoring-policy-platform"
     Value: "ams-monitored-linux"
```

The following is an example of how you can apply AMS Accelerate alarm management tags to an Auto
Scaling group managed by CloudFormation. Note that the Auto Scaling group will propagate its tags to
Amazon EC2 instances that are created by it:

```
Type: AWS::AutoScaling::AutoScalingGroup
Properties:
 AutoScalingGroupName: "TestASG"

 # ...other properties...

 Tags:
   - Key: "aws:rt:ams-monitoring-policy"
     Value: "ams-monitored"
   - Key: "aws:rt:ams-monitoring-policy-platform"
     Value: "ams-monitored-linux"

```
