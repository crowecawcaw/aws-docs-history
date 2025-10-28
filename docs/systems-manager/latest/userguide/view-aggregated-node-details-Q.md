# Exploring nodes using text prompts in

Amazon Q

Using Systems Manager integration with Amazon Q Developer, you can use text prompts to view information
created by generative AI about your managed nodes.

Amazon Q Developer is a generative AI-powered conversational assistant that can help you to understand, build, extend, and operate AWS applications. To accelerate your building
on AWS, the model that powers Amazon Q is augmented with high-quality AWS content to produce more complete, actionable, and referenced answers. For more information, see [What is Amazon Q Developer?](../../../amazonq/latest/aws-builder-use-ug/what-is.md "../../../amazonq/latest/aws-builder-use-ug/what-is.md") in the _Amazon Q Developer User Guide_.

The integration between Systems Manager and Amazon Q lets you quickly get visibility and control
over large, distributed environments across multiple AWS accounts and Regions. You can
use natural language querying to quickly search node data, and then identify issues and
take action faster.

When you ask a natural language question about managed nodes or managed instances,
Amazon Q uses the Systems Manager `ListNodes` action and creates filters based on your
textual input to retrieve results.

For example, say that you give Amazon Q the following prompt:

`List my managed nodes running Red Hat Enterprise Linux
 9.2`

Amazon Q determines what filters to include in a request, and then runs a query similar
to the following:

```
aws ssm list-nodes \
    --filters Key=PlatformName,Values='Red Hat Enterprise Linux',Type=Equal Key=PlatformVersion,Values=9.2,Type=Equal
```

Amazon Q then generates a report about Red Hat Enterprise Linux instances in your account, listing
information such as the number of instances, their IDs, and their Regions.

You can also view a JSON summary of each instance's details, as well open a link to
view the entire lists of EC2 instances or managed nodes in the Systems Manager **Explore
nodes** page. The **Explore nodes** displays results that
match the filter criteria you included in your prompt. From there, you can change or
refine the filters for your request, as described in [Exploring nodes](view-aggregated-node-details.md "view-aggregated-node-details.md").

###### Topics

- [Learning to craft effective
  prompts to ask Amazon Q about your fleet](view-aggregated-node-details-Q-prompts.md "view-aggregated-node-details-Q-prompts.md")
- [Exploring managed nodes using
  Amazon Q](explore-managed-nodes-using-Q.md "explore-managed-nodes-using-Q.md")
