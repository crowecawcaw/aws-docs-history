# Tags for your Application Load Balancer target group

Tags help you to categorize your target groups in different ways, for example, by
purpose, owner, or environment.

You can add multiple tags to each target group. Tag keys must be unique for each
target group. If you add a tag with a key that is already associated with the target
group, it updates the value of that tag.

When you are finished with a tag, you can remove it.

###### Restrictions

- Maximum number of tags per resource—50
- Maximum key length—127 Unicode characters
- Maximum value length—255 Unicode characters
- Tag keys and values are case-sensitive. Allowed characters are letters,
  spaces, and numbers representable in UTF-8, plus the following special
  characters: + - = . \_ : / @. Do not use leading or trailing spaces.
- Do not use the `aws:` prefix in your tag names or values because it
  is reserved for AWS use. You can't edit or delete tag names or values with
  this prefix. Tags with this prefix do not count against your tags per resource
  limit.

Console

###### To manage the tags for a target group

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Tags** tab, choose **Manage
   tags** and do one or more of the following:
   1. To update a tag, enter new values for
      **Key** and
      **Value**.
   2. To add a tag, choose **Add tag** and
      enter values for **Key** and
      **Value**.
   3. To delete a tag, choose **Remove** next
      to the tag.

5. Choose **Save changes**.

AWS CLI

###### To add tags

Use the [add-tags](../../../cli/latest/reference/elbv2/add-tags.md "../../../cli/latest/reference/elbv2/add-tags.md") command. The following example
adds two tags.

```
aws elbv2 add-tags \
    --resource-arns `target-group-arn` \
    --tags "Key=`project`,Value=`lima`" "Key=`department`,Value=`digital-media`"
```

###### To remove tags

Use the [remove-tags](../../../cli/latest/reference/elbv2/remove-tags.md "../../../cli/latest/reference/elbv2/remove-tags.md") command. The following example
removes the tags with the specified keys.

```
aws elbv2 remove-tags \
    --resource-arns `target-group-arn` \
    --tag-keys `project` `department`
```

CloudFormation

###### To add tags

Update the [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource
to include the `Tags` property.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      Protocol: HTTP
      Port: 80
      TargetType: ip
      VpcId: !Ref myVPC
      Tags:
        - Key: '`project`'
          Value: '`lima`'
        - Key: '`department`'
          Value: '`digital-media`'
```
