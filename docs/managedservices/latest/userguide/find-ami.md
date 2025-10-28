# Find AMI IDs, AMS

An Amazon Machine Image, or AMI, is a template for Amazon EC2 instances, created from an Amazon EC2 instance. AWS provides updated AMIs (with patches,
for example) every month; however, AWS Managed Services (AMS) requires AMIs that have been modified for AMS use. AMS releases new AMIs that you can use shortly after
Patch Tuesday every month.

Amazon Machine Images (AMIs) are instance configuration templates that are used to create EC2 instances in AWS. AMS requires that specific AMIs be used for AMS-managed resources.
The change types for creating EC2 instances and EC2 Auto Scaling groups require that you specify an AMI for AMS to use as the basis for the instances that the change type creates. AMS recommends that
you always select the most recent AMI available to you.

To learn more about AWS AMIs, see
[AWS AMI Design](https://aws.amazon.com/answers/configuration-management/aws-ami-design/ "https://aws.amazon.com/answers/configuration-management/aws-ami-design/").

When creating an Amazon EC2 stack or Amazon EC2 Auto Scaling group for your AMS account, you must specify an AMI by **AmiId**. You're limited
to AMIs that begin with "customer-" and we recommend that you always choose the most recent AMI.

To find the most recent AMI for your account, you can search with an AMS SKMS CLI command or use the AMS console details page for relevant VPC:

- Use the AMS console: Available AMIs are listed on the **AMI** page in the AMS console.
  Select from AMIs with names that begin with "customer-".
- Use the AMS SKMS API/CLI ListAmis operation.

###### Note

The AMS CLI must be installed for these commands to work. To install the AMS API or CLI, go to the AMS console **Developers Resources**
page. For reference material on the AMS CM API or AMS SKMS API, see the AMS Information Resources section in the User Guide. You may need to add a `--profile` option for
authentication; for example, `aws amsskms `ams-cli-command` --profile SAML`. You may also need to add the `--region` option as all AMS
commands run out of us-east-1; for example `aws amscm `ams-cli-command` --region=us-east-1`.

Here is a CLI example with a `query` option that restricts the results to customer AMIs:

```
aws amsskms list-amis --vpc-id `VPC_ID` --query "Amis.sort_by(@,&Name)[?starts_with(Name,'customer')].[Name,AmiId]" --output table
```

This example uses the `filter` option with the `query` option to find Windows AMIs that start with "customer":

```
aws amsskms list-amis --vpc-id `VPC_ID` --query "Amis.sort_by(@,&Name)[?starts_with(Name,'customer')].[Name,AmiId]" --filter Attribute=Platform,Value=windows --output table
```

- For information about using CLI queries, see [How to Filter the Output with the --query Option](../../../cli/latest/userguide/controlling-output.md#controlling-output-filter "../../../cli/latest/userguide/controlling-output.md#controlling-output-filter") and the query language reference, [JMESPath Specification](http://jmespath.org/specification.html "http://jmespath.org/specification.html").
