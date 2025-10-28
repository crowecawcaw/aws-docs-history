# Tag a Network Load Balancer

Tags help you to categorize your Network Load Balancers in different ways. For example, you
can tag a resource by purpose, owner, or environment.

You can add multiple tags to each Network Load Balancer. If you add a tag with a key that is
already associated with the Network Load Balancer, it updates the value of that tag.

When you are finished with a tag, you can remove it from your Network Load Balancer.

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

###### To update the tags for a load balancer

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Select the check box for the Network Load Balancer.
4. On the **Tags** tab, choose **Manage tags**.
5. To add a tag, choose **Add tag** and enter the tag key and
   tag value. Allowed characters are letters, spaces, numbers (in UTF-8), and
   the following special characters: + - = . \_ : / @. Do not use leading or
   trailing spaces. Tag values are case-sensitive.
6. To update a tag, enter new values in **Key** or
   **Value**.
7. To delete a tag, choose **Remove** next to the tag.
8. Choose **Save changes**.

AWS CLI

###### To add tags

Use the [add-tags](../../../cli/latest/reference/elbv2/add-tags.md "../../../cli/latest/reference/elbv2/add-tags.md") command. The following example
adds two tags.

```
aws elbv2 add-tags \
    --resource-arns `load-balancer-arn` \
    --tags "Key=`project`,Value=`lima`" "Key=`department`,Value=`digital-media`"
```

###### To remove tags

Use the [remove-tags](../../../cli/latest/reference/elbv2/remove-tags.md "../../../cli/latest/reference/elbv2/remove-tags.md") command. The following example
removes the tags with the specified keys.

```
aws elbv2 remove-tags \
    --resource-arns `load-balancer-arn` \
    --tag-keys `project` `department`
```

CloudFormation

###### To add tags

Define a resource of type [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md") resource
to include the `Tags` property.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-nlb
      Type: network
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      Tags:
        - Key: '`project`'
          Value: '`lima`'
        - Key: '`department`'
          Value: '`digital-media`'
```
