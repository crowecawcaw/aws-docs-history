Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Tagging Amazon Forecast Resources

A _tag_ is a label that you optionally define and associate with AWS resources, including certain types of Amazon Forecast resources. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. For example, you can use tags to apply policies or automation, or to identify resources that are subject to certain compliance requirements. You can add tags to the following types of Forecast resources:

- Dataset groups
- Datasets
- Dataset import jobs
- Predictors
- Predictor export jobs
- Forecasts
- Forecast export jobs
- What-if Analyses
- What-if Forecasts
- What-if Forecast export jobs
  A resource can have as many as 50 tags.

## Managing Tags

Each tag consists of a required tag key and an optional tag value, both of which you define. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor for a tag key. For example, if you have two versions of a Forecast dataset import job (one for internal testing and another for production), you might assign an `Environment` tag key to both projects. The value of the `Environment` tag key might be `Test` for one version of the dataset import job and `Production` for the other version.

A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, numbers, white space, or one of the following symbols: \_ . : / = + -. The following additional restrictions apply to tags:

- Tag keys and values are case sensitive.
- For each associated resource, each tag key must be unique and it can have only one value.
- Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for keys, because it is reserved for AWS use.
  You cannot edit or delete tag keys with this prefix. Values can have this prefix.
  If a tag value has `aws` as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags.
  Tags with only the key prefix of `aws` do not count against your tags per resource limit.
- You can't update or delete a resource based only on its tags. You must also specify the Amazon Resource Name (ARN) or resource ID, depending on the operation that you use.
- You can associate tags with public or shared resources. However, the tags are available only for your AWS account, not any other accounts that share the resource. In addition, the tags are available only for resources that are located in the specified AWS Region for your AWS account.

To add, display, update, and remove tag keys and values from Forecast resources, you can use the AWS Command Line Interface (AWS CLI), the Forecast API, or an AWS SDK.

## Using Tags in IAM Policies

After you start implementing tags, you can apply tag-based, resource-level permissions to
AWS Identity and Access Management (IAM) policies and API operations. This includes operations that support adding tags
to resources when resources are created. By using tags in this way, you can implement granular
control of which groups and users in your AWS account have permission to create and tag
resources, and which groups and users have permission to create, update, and remove tags more
generally.

For example, you can create a policy that allows a user to have full access to all of the
Forecast resources where their name is a value in the `Owner` tag for the
resource.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ModifyResourceIfOwner",
 "Effect": "Allow",
 "Action": "forecast:*",
 "Resource": "*",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "aws:ResourceTag/Owner": "${aws:username}"
 }
 }
 }
 ]
}`

```

The following example shows how to create a policy to allow creating and deleting a
dataset. These operations are allowed only if the user name is `johndoe`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "forecast:CreateDataset",
 "forecast:DeleteDataset"
 ],
 "Resource": "arn:aws:forecast:*:*:dataset/*",
 "Condition": {
 "StringEquals": {"aws:username" : "johndoe"}
 }
 },
 {
 "Effect": "Allow",
 "Action": "forecast:DescribeDataset",
 "Resource": "*"
 }
 ]
}`

```

If you define tag-based, resource-level permissions, the permissions take effect
immediately. This means that your resources are more secure as soon as they're created, and you
can quickly start enforcing the use of tags for new resources. You can also use resource-level
permissions to control which tag keys and values can be associated with new and existing
resources. For more information, see [Controlling
Access Using Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _AWS IAM User Guide_.

## Adding Tags to Resources

The following examples show how to add a tag to Forecast resources by using the [AWS CLI](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md") and the AWS Management Console.

AWS CLI
To add a tag when creating a new Forecast resource with the AWS CLI, use the appropriate
`create` command for the resource and include the `tags` parameter and
values. For example, the following command from the creates a new dataset group named
`myDatasetGroup` for a CUSTOM domain, and adds the following tags: An `Environment` tag key with a `Test` tag
value, and a `Owner` tag key and a `xyzCorp` value.

```
aws forecast create-dataset-group \
--dataset-group-name myDatasetGroup \
--dataset-arns arn:aws:forecast:`region`:`acct-id`:dataset/`dataset_name` \
--domain CUSTOM \
--tags Key=Environment,Value=Test Key=Owner,Value=xyzCorp
```

For information about the commands that you can use to create a Forecast resource, see the
[Forecast AWS CLI Command Reference](../../../cli/latest/reference/forecast.md "../../../cli/latest/reference/forecast.md").

To add a tag to an existing resource, use the `tag-resource` command and specify the ARN of the
resource and provide the tag key and value in the `tags-model` parameter.

```
aws forecast tag-resource \
--resource-arn `resource ARN` \
--tags Key=`key`,Value=`value`
```

AWS Management Console
When you create a resource in Forecast, you can add optional tags. The following
example adds a tag to a dataset group. Adding tags to other resources follows a similar pattern.

###### To add tags to a new dataset group

1. Sign in to the AWS Management Console and open the Amazon Forecast console at [https://console.aws.amazon.com/forecast/](https://console.aws.amazon.com/forecast/ "https://console.aws.amazon.com/forecast/").
2. Choose **Create dataset group**.
3. For **Dataset group name**, enter a name.
4. For **Forecasting domain**, choose a domain.
5. Choose **Add new tag**.
6. For **Key** and **Value**, enter appropriate
   values.

For example, `Environment` and `Test`,
respectively. 7. To add more tags, choose **Add new tag**.

You can add up to 50 tags to a resource. 8. Choose **Next** to continue creating your resource.

## Additional Information

For more information about tagging, see the following resources.

- [AWS Tagging Principles](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the _AWS General Reference_
- [AWS Tagging Strategies](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf "https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf") (downloadable PDF)
- [AWS Access Control](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _AWS IAM User Guide_
- [AWS Tagging Policies](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") in the _AWS Organizations User Guide_
