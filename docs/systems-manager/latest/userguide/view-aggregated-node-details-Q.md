

# Exploring nodes using text prompts in AWS assistant

Using Systems Manager integration with the AWS assistant, you can use text prompts to view information created by generative AI about your managed nodes. 

The AWS assistant is a generative AI-powered conversational assistant that can help you to understand, build, extend, and operate AWS applications. To accelerate your building on AWS, the model that powers the AWS assistant is augmented with high-quality AWS content to produce more complete, actionable, and referenced answers. For more information, see [What is AWS assistant?](https://docs.aws.amazon.com/assistant/latest/userguide/what-is.html) in the *AWS assistant User Guide*. 

The integration between Systems Manager and the AWS assistant lets you quickly get visibility and control over large, distributed environments across multiple AWS accounts and Regions. You can use natural language querying to quickly search node data, and then identify issues and take action faster.

When you ask a natural language question about managed nodes or managed instances, the AWS assistant uses the Systems Manager `ListNodes` action and creates filters based on your textual input to retrieve results.

For example, say that you give the AWS assistant the following prompt:

**List my managed nodes running Red Hat Enterprise Linux 9.2**

The AWS assistant determines what filters to include in a request, and then runs a query similar to the following:

```sh
aws ssm list-nodes \
    --filters Key=PlatformName,Values='Red Hat Enterprise Linux',Type=Equal Key=PlatformVersion,Values=9.2,Type=Equal
```

The AWS assistant then generates a report about Red Hat Enterprise Linux instances in your account, listing information such as the number of instances, their IDs, and their Regions.

You can also view a JSON summary of each instance's details, as well open a link to view the entire lists of EC2 instances or managed nodes in the Systems Manager **Explore nodes** page. The **Explore nodes** displays results that match the filter criteria you included in your prompt. From there, you can change or refine the filters for your request, as described in [Exploring nodes](view-aggregated-node-details.md).

**Topics**
+ [Learning to craft effective prompts to ask AWS assistant about your fleet](view-aggregated-node-details-Q-prompts.md)
+ [Exploring managed nodes using AWS assistant](explore-managed-nodes-using-Q.md)