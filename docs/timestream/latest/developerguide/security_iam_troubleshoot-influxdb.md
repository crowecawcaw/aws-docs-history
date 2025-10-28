For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Troubleshooting Amazon Timestream for InfluxDB identity and access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with Timestream for InfluxDB and IAM.

###### Topics

- [I am not authorized to perform an action in
  Timestream for InfluxDB](#security_iam_troubleshoot-no-permissions-influxdb "#security_iam_troubleshoot-no-permissions-influxdb")
- [I want to allow people outside of my AWS account
  to access my Timestream for InfluxDB resources](#security_iam_troubleshoot-cross-account-access-influxdb "#security_iam_troubleshoot-cross-account-access-influxdb")

## I am not authorized to perform an action in

Timestream for InfluxDB

If the AWS Management Console tells you that you're not authorized to perform an action, then you must contact your
administrator for assistance. Your administrator is the person that provided you with your user name and
password.

The following example error occurs when the `mateojackson` user tries to use the console to view
details about a fictional `my-example-widget` resource but does not have the
fictional `timestream-influxdb:`GetWidget`` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: timestream-influxdb:`GetWidget` on resource: `my-example-widget`
```

In this case, Mateo asks his administrator to update his policies to allow him to access the
`my-example-widget` resource using the
`timestream-influxdb:`GetWidget`` action.

## I want to allow people outside of my AWS account

to access my Timestream for InfluxDB resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:

- [Controlling access to a DB instance in a VPC](timestream-for-influxdb-controlling-access.md "timestream-for-influxdb-controlling-access.md")
- To learn whether Timestream for InfluxDB supports these features, see [How Amazon Timestream for InfluxDB works with IAM](security_iam_service-with-iam-influxb.md "security_iam_service-with-iam-influxb.md").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing
  access to an IAM user in another AWS account that you own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [How IAM roles differ from resource-based policies](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User Guide_.
