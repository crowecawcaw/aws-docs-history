

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# AWS Identity and Access Management in AppRegistry
<a name="ar-iam"></a>

You must have credentials to access AWS Service Catalog AppRegistry. These credentials grant permission to access AWS resources, such as AWS Service Catalog portfolios or products. AppRegistry integrates with AWS Identity and Access Management (IAM). You can grant administrators the required permissions to create and manage products. You can grant end users the required permissions to launch products and manage provisioned products. Administrators and end users create and manage these polcies. Alternatively, AWS can create and manage them. To control access, you attach these policies to the roles and groups that you use with AppRegistry. For more information, see see [IAM identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the *IAM User Guide*. 

**Topics**
+ [Audience](#security-iam-audience)
+ [Troubleshooting AppRegistry identity and access](#security_iam_troubleshoot)
+ [Using service-linked roles for AWS Service Catalog AppRegistry](slr-appregistry.md)

## Audience
<a name="security-iam-audience"></a>

The permissions that you have through AWS Identity and Access Management (IAM) might depend on you AppRegistry role. 

 **Administrator** – If you're an AppRegistry administrator, you must have full access to the administrator console and IAM permissions that allow you to perform tasks, such as creating and managing portfolios and products, managing constraints, and granting access to end users. 

 **IAM administrator** – If you're an IAM administrator, you might want to learn details about how you can write policies to manage access to AppRegistry. To view example AppRegistry identity-based policies that you can use in IAM, see [AWS managed policies](https://docs.aws.amazon.com/servicecatalog/latest/arguide/managed-policies.html). 

## Troubleshooting AppRegistry identity and access
<a name="security_iam_troubleshoot"></a>

 The following information might help you diagnose and fix common issues that you can encounter when working with AppRegistry and AWS Identity and Access Management (IAM). 

### I'm unauthorized to perform an action in AppRegistry
<a name="troubleshoot-one"></a>

 If the AWS Management Console warns you that you're not authorized to perform an action, contact your administrator for assistance. Your administrator is the person who created your sign-in credentials. 

 ** Example: warning message ** 

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: awes:GetWidget on resource: my-example-widget
```

 In the example, an error occurs when user `mateojackson` attempts to view details about the resource `my-example-widget`, but is unauthorized to perform the action `awes:GetPermission`. 

### I'm getting an access denied message when associating application resources
<a name="troubleshoot-default-message"></a>

 When you associate application resources with values for stacks or query tags that aren't supported, you receive a default error message: 

 ** Example: default error message ** 

```
An error occurred (AccessDeniedException) when calling the AssociateResource operation: User: arn:aws:sts::[{{account number}}]:assumed-role/PringleTestRole/{{yingdon-Isengard}} is not authorized to perform: servicecatalog:AssociateResource on resource: arn:aws:servicecatalog:{{us-west-2}}:[{{account number}}]:/applications/[application id] with an explicit deny
```

 For more information, see the following: 
+  [AssociateResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_AssociateResource.html) in the *AWS Service Catalog Developer Guide* 
+  [DisassociateResource](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_DisassociateResource.html) in the *AWS Service Catalog Developer Guide* 
+  [Controlling the resource tag values associated to applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/control-tags.html) in the *AppRegistry Administrator Guide* 