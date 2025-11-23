# Tagging `EnabledControl` resources in AWS Control Tower

You can add tags to `EnabledControl` resources by means of CloudFormation
templates, through the AWS Control Tower console, and by calling the AWS Control Tower APIs.

###### Note

The AWS Control Tower `GetEnabledControl`, `EnableControl`, and `ListTagsforResource` API
operations rely on the `EnabledControl` resource tagging functionality for
proper drift reporting.

**Required permissions**

When you configure resource tags with CloudFormation, you must add the new
`ListTagsforResource` IAM permission to the policy for the customer-managed
role that you use to update your controls. If you do not add the permission, the CloudFormation
template may have the tags, but CloudFormation cannot see them without the ability to call
`ListTagsforResource`. If you already have created a role that updates your
AWS Control Tower landing zone, that role probably has this permission in place already, because the same
permission is required to view tags associated with the landing zone resource.

**Step 1: Add the permissions**

To tag a resource, update a tag, and enable proper drift reporting, three permissions are
required, as shown in the example that follows.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "controltower:TagResource",
 "controltower:ListTagsForResource",
 "controltower:UntagResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

**CloudFormation drift**

If you do not add the proper permissions, you can experience some side-effects that we
refer to as _false positive or false negative CloudFormation drift_. During
CloudFormation drift, the **Detect drift** command in the CloudFormation console may not
give reliable results. You also can encounter these side effects if you modify your
CloudFormation resource outside the CloudFormation console.

###### We strongly recommend

If you provision a resource, including a tag, with CloudFormation, it is important to update
the resource through CloudFormation only.

When you experience _false positive_ CloudFormation drift, the CloudFormation
console shows a **Modified** status (drifted) for a resource, although you
are not aware of making any modifications. In this situation, the status means that you have
not added the `ListTagsforResource` permission. When the permission is not
present in the role, the `ReadHandler` cannot read the tags. CloudFormation returns an error, because it cannot tell
whether the resource actually was modified. The error is surfaced as
**Modified** status.

When you experience _false negative drift_ the CloudFormation console shows
a resource as unmodified, when in fact, it has been modified. This situation means that the
AWS Control Tower `EnabledControl` resource has tags, but CloudFormation cannot retrieve those
tags. In this case, two things must have occurred: the resource has been modified outside
CloudFormation, which is not a recommended practice, and also the `ListTagsforResource`
permission was not added to the policy.

**Step 2. Add the tags to the resource**

Here is an example CloudFormation resource template with tags added.

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myEnabledControlTest:
    Type: 'AWS::ControlTower::EnabledControl'
    Properties:
      ControlIdentifier: 'arn:aws:controltower:us-west-2::control/ZTCMZEXAMPLE'
      TargetIdentifier: 'arn:aws:organizations::012345678901:ou/o-exampleou/ou-xxxx-f35g82v9'
      Tags:
        - Key: "K1"
          Value: "V1"
      Parameters:
        - Key: AllowedRegions
          Value:
            - us-west-2
            - us-west-1
            - us-east-1
```

For more information, see [`EnabledControl`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.md") in the _AWS CloudFormation User
Guide_.
