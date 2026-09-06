

# Managing custom authorizers
<a name="custom-auth-manage"></a>

 You can manage your authorizers by using the following APIs. 
+ [ListAuthorizers](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuthorizers.html): Show all authorizers in your account.
+  [DescribeAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuthorizer.html): Displays properties of the specified authorizer. These values include creation date, last modified date, and other attributes.
+ [SetDefaultAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_SetDefaultAuthorizer.html): Specifies the default authorizer for your AWS IoT Core data endpoints. AWS IoT Core uses this authorizer if a device doesn't pass AWS IoT Core credentials and doesn't specify an authorizer. For more information about using AWS IoT Core credentials, see [Client authentication](client-authentication.md).
+ [UpdateAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateAuthorizer.html):  Changes the status, token key name, or public keys for the specified authorizer.
+  [DeleteAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteAuthorizer.html): Deletes the specified authorizer. 

**Note**  
 You can't update an authorizer's signing requirement. This means that you can't disable signing in an existing authorizer that requires it. You also can't require signing in an existing authorizer that doesn't require it. 