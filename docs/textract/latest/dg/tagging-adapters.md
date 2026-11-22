

# Tagging resources

With Amazon Textract, you can tag resources like adapters and Amazon Textract Insights projects, blueprints, and jobs for the purposes of managing secure access. A tag is a label made of a key and a value. You can also use tags to organize resources by purpose, owner, or environment. To tag resources, use an AWS SDK or the AWS CLI. The topics in this section demonstrate how to manage your tags using the CLI.

You can tag Amazon Textract Insights projects, blueprints, and jobs when you create them, or later with `TagResource`. You can then use tags in IAM policies to control who can act on those resources. For the resources you can tag, their ARN formats, the condition keys, the required permissions, tag restrictions, and examples, see [Tagging Amazon Textract Insights resources](insights-tagging.md). For tagging errors, see [Troubleshooting](insights-troubleshooting.md).