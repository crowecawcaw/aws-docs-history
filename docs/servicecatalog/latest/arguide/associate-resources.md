# Associating and disassociating application resources

An application resource is an object within an AWS service that you can tag with [the `awsApplication` tag](overview-appreg.md#ar-user-tags "overview-appreg.md#ar-user-tags"), which is an AWS user tag that AppRegistry vends on your behalf.
The following procedures describe how to associate and disassociated application resources.

###### Note

For AppRegistry applications created before November 8th, 2023, AppRegistry creates the `awsApplication` tag
after you perform your first resource association. This tag’s value is a unique identifier for the application.
You can then apply the `awsApplication` tag to any other resources you want to add to the application.
For AppRegistry applications created after November 8th, 2023, AppRegistry creates the `awsApplication` tag
when you create the application.

###### Topics

- [Associate application resources in a new application](#w2aab9b7c19c21b9 "#w2aab9b7c19c21b9")
- [Associate application resources in an existing application](#w2aab9b7c19c21c11 "#w2aab9b7c19c21c11")
- [Disassociate application resources from an application](#w2aab9b7c19c21c13 "#w2aab9b7c19c21c13")

##

Associate application resources in a new application

The following procedure describes how to associate application resources
in a new application.

###### To associate application resources in a new application.

1. Open the AWS Service Catalog console
   at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/")
2. From the navigation pane,
   choose **AppRegistry**,
   and then choose **Applications**.
   You're directed
   to the **Applications** screen.
3. On **Applications**,
   choose **Create application**.
4. Under **Application name and description**,
   enter a name and optional description
   for your application.
5. Under **Resource collections**,
   choose one or more provisioned products or CloudFormation stacks
   to associate
   to your application.
6. Choose **Create application**.

##

Associate application resources in an existing application

The following procedure describes how to associate application resources in an existing application.

###### To associate application resources in an existing application

1. Open the AWS Service Catalog console
   at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/")
2. From the left navigation pane,
   choose **AppRegistry**,
   and then choose **Applications**.
   You're directed
   to the **Applications** screen.
3. On **Applications**,
   choose the name
   of the application
   that you want
   to associate resources
   to.
   Or select the name
   of application
   that you want
   to associate resources
   to,
   and choose **View**.
   You're directed
   to the **Application details** screen.
4. Choose **Resource collections**,
   and then choose **Associate resource collection**.
5. Under **Resource collections**,
   choose one or more provisioned products or CloudFormation stacks
   to associate
   to your application.
6. Choose **Save changes**.

###### Note

If you share an application
with this account,
and the application has read-only permissions,
associate and disassociate actions are disabled
for resource collections.

##

Disassociate application resources from an application

The following procedure describes how to disassociate application resources
from an existing application.

###### To disassociate application resources from an existing application

1. Open the AWS Service Catalog console
   at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/")
2. From the navigation pane,
   choose **AppRegistry**,
   and then choose **Applications**.
   You're directed
   to the **Applications** screen.
3. On **Applications**,
   choose the name
   of the application
   that you want
   to disassociate resources
   from.
   Or select the name
   of the application
   that you want
   to disassociate resources from,
   and choose **View**.
   You're directed
   to the **Application details** screen.
4. Choose **Resource collections**,
   select the resource
   that you want
   to disassociate
   from the application,
   and then choose **Disassociate**.
5. Confirm your disassociation,
   and then choose **Ok**.

###### Note

If you share an application
with this account,
and the application has read-only permissions,
associate and disassociate actions are disabled
for resource collections.
