# The `awsApplication` tag

The `awsApplication` tag is a tag that AppRegistry vends when you create
an AppRegistry application. This tag marks resources as belonging to an application.
This tag consists of a key-value pair, where the key is `awsApplication` and
value is the Amazon Resource Name (ARN) of an application.

**To help you manage and monitor your applications,
AWS highly recommends you ensure all of your application resources
are tagged with the `awsApplication` tag**. Review [Tutorial:
Existing AppRegistry application resources and the `awsApplication` tag](existing-customer-usecases.md "existing-customer-usecases.md") for instructions.

The `awsApplication` tag provides additional features and capabilities for your applications and
resources, including:

- [Access to application monitoring
  and management](../../../awsconsolehelpdocs/latest/gsg/aws-myApplications.md#myApp-benefits "../../../awsconsolehelpdocs/latest/gsg/aws-myApplications.md#myApp-benefits") in myApplications dashboard in the AWS Management Console
- Viewing details about your application's costs, security findings, alarms, metrics and usage
- Filtering by application in integrated AWS services, such as AWS Cost Explorer and AWS Security Hub CSPM
  For AppRegistry applications created before November 8th, 2023, AppRegistry creates the `awsApplication` tag
  after you perform your first resource association. You can then apply the `awsApplication` tag
  to any other resources you want to add to the application.
  For AppRegistry applications created after November 8th, 2023, AppRegistry creates the `awsApplication` tag
  when you create the application.

As of September 18th, 2024 for **existing** AppRegistry users, the following behaviors apply:

- For existing AppRegistry applications which include resources without the `awsApplication` tag applied,
  AWS does not retroactively apply the tag.
- For existing AppRegistry applications, if you use the `AssociateResource` AppRegistry API, AWS does not
  automatically apply the tag unless you define the `options` parameter value as `APPLY_APPLICATION_TAG`.
- For existing AppRegistry applications, if you use the AppRegistry console to add a new resource
  to the application, AWS automatically applies the `awsApplication` tag to that new resource.
- For new applications created in the AppRegistry console, AWS automatically applies the `awsApplication` tag
  to all resources added to the application.
- For new applications created with myApplications in the AWS Management Console, AWS automatically applies the `awsApplication` tag
  to all resources added to the application.
