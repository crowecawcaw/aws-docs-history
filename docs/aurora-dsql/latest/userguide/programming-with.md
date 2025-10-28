# Programming with Aurora DSQL

Aurora DSQL provides you with the following tools to manage your Aurora DSQL resources
programmatically.

**AWS Command Line Interface (AWS CLI)**

You can create and manage your resources by using the AWS CLI in a
command-line shell. The AWS CLI provides direct access to the APIs for
AWS services, such as Aurora DSQL. For syntax and examples for the commands for
Aurora DSQL, see [dsql](../../../cli/latest/reference/dsql.md "../../../cli/latest/reference/dsql.md") in the _AWS CLI Command
Reference_.

**AWS software development kits (SDKs)**

AWS provides SDKs for many popular technologies and programming
languages. They make it easier for you to call AWS services from within
your applications in that language or technology. For more information about these SDKs, see [Tools for developing and managing applications on AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").

**Aurora DSQL API**

This API is another programming interface for Aurora DSQL. When using this API,
you must format every HTTPS request correctly and add a valid digital
signature to every request. For more information, see [Aurora DSQL API reference](CHAP_api_reference.md "CHAP_api_reference.md").

**AWS CloudFormation**

The [AWS::DSQL::Cluster](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dsql-cluster.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dsql-cluster.md") is an AWS CloudFormation resource that enables you to
create and manage Aurora DSQL clusters as part of your infrastructure as code.
AWS CloudFormation helps you define your entire AWS environment in code, making it
easier to provision, update, and replicate your infrastructure in a
consistent and reliable way.

When you use the AWS::DSQL::Cluster resource in your AWS CloudFormation templates, you can declaratively provision Aurora DSQL clusters alongside your other cloud resources. This helps ensure that your data infrastructure deploys and manages alongside the rest of your application stack.
