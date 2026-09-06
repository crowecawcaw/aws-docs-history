

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Troubleshooting Amazon Timestream for InfluxDB identity and access
<a name="security_iam_troubleshoot-influxdb"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with Timestream for InfluxDB and IAM.

**Topics**
+ [I am not authorized to perform an action in Timestream for InfluxDB](#security_iam_troubleshoot-no-permissions-influxdb)
+ [I want to allow people outside of my AWS account to access my Timestream for InfluxDB resources](#security_iam_troubleshoot-cross-account-access-influxdb)

## I am not authorized to perform an action in Timestream for InfluxDB
<a name="security_iam_troubleshoot-no-permissions-influxdb"></a>

If the AWS Management Console tells you that you're not authorized to perform an action, then you must contact your administrator for assistance. Your administrator is the person that provided you with your user name and password.

The following example error occurs when the `mateojackson` user tries to use the console to view details about a fictional `{{my-example-widget}}` resource but does not have the fictional `timestream-influxdb:{{GetWidget}}` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: timestream-influxdb:{{GetWidget}} on resource: {{my-example-widget}}
```

In this case, Mateo asks his administrator to update his policies to allow him to access the `{{my-example-widget}}` resource using the `timestream-influxdb:{{GetWidget}}` action.

## I want to allow people outside of my AWS account to access my Timestream for InfluxDB resources
<a name="security_iam_troubleshoot-cross-account-access-influxdb"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:
+ [Controlling access to a DB instance in a VPC](timestream-for-influxdb-controlling-access.md)
+ To learn whether Timestream for InfluxDB supports these features, see [How Amazon Timestream for InfluxDB works with IAM](https://docs.aws.amazon.com/timestream/latest/developerguide/security_iam_service-with-iam-influxb.html).
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*. 
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*. 
+ To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*. 
+ To learn the difference between using roles and resource-based policies for cross-account access, see [How IAM roles differ from resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*. 