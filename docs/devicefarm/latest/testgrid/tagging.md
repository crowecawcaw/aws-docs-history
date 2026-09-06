

# Tagging AWS Device Farm resources
<a name="tagging"></a>

AWS Device Farm works with the AWS Resource Groups Tagging API. This API allows you to manage resources in your AWS account with *tags*. You can add tags to resources, such as projects and test runs. 

You can use tags to:
+ Organize your AWS bill to reflect your own cost structure. To do this, sign up to get your AWS account bill with tag key values included. Then, to see the cost of combined resources, organize your billing information according to resources with the same tag key values. For example, you can tag several resources with an application name, and then organize your billing information to see the total cost of that application across several services. For more information, see [Cost Allocation and Tagging](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in *About AWS Billing and Cost Management*. 
+ Control access through IAM policies. To do so, create a policy that allows access to a resource or set of resources using a tag value condition.
+ Identify and manage runs that have certain properties as tags, such as the branch used for testing. 

 For more information about tagging resources, see the [Tagging Best Practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) whitepaper. 

**Topics**
+ [Tagging resources](#tagging-resources)
+ [Looking up resources by tag](#tagging-looking-up-resources)
+ [Removing tags from resources](#tagging-removing-tags)

## Tagging resources
<a name="tagging-resources"></a>

The AWS Resource Group Tagging API allows you to add, remove, or modify tags on resources. For more information, see the [AWS Resource Group Tagging API Reference](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/Welcome.html). 

To tag a resource, use the [`TagResources`](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html) operation from the `resourcegroupstaggingapi` endpoint. This operation takes a list of ARNs from supported services and a list of key-value pairs. The value is optional. An empty string indicates that there should be no value for that tag. For example, the following Python example tags a series of project ARNs with the tag `build-config` with the value `release`:

```
import boto3

client = boto3.client('resourcegroupstaggingapi')

client.tag_resources(ResourceARNList=["arn:aws:devicefarm:us-west-2:111122223333:project:123e4567-e89b-12d3-a456-426655440000",
                                      "arn:aws:devicefarm:us-west-2:111122223333:project:123e4567-e89b-12d3-a456-426655441111",
                                      "arn:aws:devicefarm:us-west-2:111122223333:project:123e4567-e89b-12d3-a456-426655442222"]
                     Tags={"build-config":"release", "git-commit":"8fe28cb"})
```

A tag value is not required. To set a tag with no value, use an empty string (`""`) when specifying a value. A tag can only have one value. Any previous value a tag has for a resource will be overwritten with the new value. 

## Looking up resources by tag
<a name="tagging-looking-up-resources"></a>

To look up resources by their tags, use the `GetResources` operation from the `resourcegrouptaggingapi` endpoint. This operation takes a series of filters, none of which are required, and returns the resources that match the given criteria. With no filters, all tagged resources are returned. The `GetResources` operation allows you to filter resources based on
+ Tag value
+ Resource type (for example, `devicefarm:run`)

For more information, see the [AWS Resource Group Tagging API Reference](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/Welcome.html).

The following example looks up Device Farm desktop browser testing sessions (`devicefarm:testgrid-session` resources) with the tag `stack` that have the value `production`:

```
import boto3
client = boto3.client('resourcegroupstaggingapi')
sessions = client.get_resources(ResourceTypeFilters=['devicefarm:testgrid-session'],
                                TagFilters=[
                                  {"Key":"stack","Values":["production"]}
                                ])
```

## Removing tags from resources
<a name="tagging-removing-tags"></a>

To remove a tag, use the `UntagResources` operation, specifying a list of resources and the tags to remove:

```
import boto3
client = boto3.client('resourcegroupstaggingapi')
client.UntagResources(ResourceARNList=["arn:aws:devicefarm:us-west-2:111122223333:project:123e4567-e89b-12d3-a456-426655440000"], TagKeys=["RunCI"])
```