

AWS App Runner is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Managing AWS WAF web ACLs
<a name="waf-manage"></a>

Manage the AWS WAF web ACLs for your App Runner service by using one of the following methods:
+ [App Runner console](#waf-manage.console)
+ [AWS CLI](#waf-manage.api)

## App Runner console
<a name="waf-manage.console"></a>

When you [create a service](manage-create.md) or [update an existing one](manage-configure.md) on the App Runner console, you can associate or disassociate an AWS WAF web ACL. 

**Note**  
An App Runner service can be associated with only one web ACL. However, you can associate one web ACL with more than one App Runner service in addition to other AWS resources. 
Before you associate a web ACL, make sure to update your IAM permissions for AWS WAF. For more information, see [Permissions](waf.md#waf.permissions). 

### Associating AWS WAF web ACL
<a name="waf-manage.console.add"></a>

**Important**  
Source IP rules for App Runner private services that are associated with WAF web ACLs *do not adhere to IP based rules*. This is because we currently don't support forwarding request source IP data to App Runner private services associated with WAF. If your App Runner application requires source IP/CIDR incoming traffic control rules, you must use [security group rules for private endpoints](network-pl-manage.md) instead of WAF web ACLs.

**To associate an AWS WAF web ACL**

1. Open the [App Runner console](https://console.aws.amazon.com/apprunner), and in the **Regions** list, select your AWS Region.

1. Based on whether you're creating or updating a service, perform one of the following steps:
   + If you're creating a new service, choose **Create an App Runner service** and go to **Configure Service**.
   + If you're updating an existing service, choose the **Configuration** tab, and then choose **Edit** under **Configure service**.

1. Go to **Web application firewall** under **Security**. 

1. Choose the **Activate** toggle button to view the options.   
![The App Runner console layout, showing the Web Application Firewall options.](http://docs.aws.amazon.com/apprunner/latest/dg/images/console-waf.png)

1. Perform one of the following steps: 
   + **To associate an existing web ACL**: Choose the required web ACL from the **Choose a web ACL** table to associate with your App Runner service.
   + **To create a new web ACL**: Choose **Create web ACL** to create a new web ACL using the AWS WAF console. For more information, see [Creating a web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-creating.html) in the *AWS WAF Developer Guide*. 

     1. Choose the refresh button to view the newly created web ACL in the **Choose a web ACL** table. 

     1. Select the required web ACL. 

1. Choose **Next** if you're creating a new service or **Save changes** if you're updating an existing service. The selected web ACL is associated with your App Runner service. 

1. To verify the web ACL association, choose the **Configuration** tab of your service and go to **Configure service**. Scroll to **Web application firewall** under **Security** to view the details of the web ACL associated with your service. 
**Note**  
When you create a web ACL, a small amount of time passes before the web ACL fully propagates and is available to App Runner. The propagation time can be from a few seconds to a number of minutes. AWS WAF returns a `WAFUnavailableEntityException` when you try to associate a web ACL before it has fully propagated.   
If you refresh the browser or navigate away from the App Runner console before the web ACL is fully propagated, the association fails to occur. However, you can navigate within the App Runner console.

### Disassociating an AWS WAF web ACL
<a name="waf-manage.console.disassociate"></a>

You can disassociate AWS WAF web ACl that you no longer need by [updating](manage-configure.md) your App Runner service. 

**To disassociate an AWS WAF web ACl**

1. Open the [App Runner console](https://console.aws.amazon.com/apprunner), and in the **Regions** list, select your AWS Region.

1. Go to **Configuration** tab of the service you want to update and choose **Edit** under **Configure service**. 

1. Go to **Web application firewall** under **Security**. 

1. Disable the **Activate** toggle button. You receive a message to confirm the deletion.

1. Choose **Confirm**. The web ACL is disassociated from your App Runner service. 
**Note**  
If you want to associate your service with another web ACL, select a web ACL from the **Choose a web ACL** table. App Runner disassociates the current web ACL and starts the process to associate with the selected web ACL. 
If no other App Runner services or resources use a disassociated web ACL, consider deleting the web ACL. Otherwise, you will continue to incur costs. For more information about pricing, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing). For instruction on how to delete a web ACL, see [DeleteWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_DeleteWebACL.html) in the *AWS WAF API Reference*. 
You can't delete a web ACL that's associated with other active App Runner services or other resources. 

## AWS CLI
<a name="waf-manage.api"></a>

You can associate or disassociate an AWS WAF web ACL by using the AWS WAF public APIs. The App Runner service, with which you want to associate or disassociate a web ACL, must be in a valid state.

AWS WAF returns a `WAFNonexistentItemException` error when you call one of the following AWS WAF APIs for an App Runner service which is in an invalid state: 
+  `AssociateWebACL` 
+  `DisassociateWebACL` 
+  `GetWebACLForResource` 

The invalid states for your App Runner service include:
+  `CREATE_FAILED` 
+  `DELETE_FAILED` 
+  `DELETED` 
+  `OPERATION_IN_PROGRESS ` 
**Note**  
`OPERATION_IN_PROGRESS` state is invalid only if your App Runner service is being deleted. 

For more information about AWS WAF public APIs, see [*AWS WAF API Reference Guide*](https://docs.aws.amazon.com/waf/latest/APIReference/Welcome.html).

**Note**  
Update your IAM permissions for AWS WAF. For more information, see [Permissions](waf.md#waf.permissions). 

### Associating AWS WAF web ACL using AWS CLI
<a name="waf-manage.api.add"></a>

**Important**  
Source IP rules for App Runner private services that are associated with WAF web ACLs *do not adhere to IP based rules*. This is because we currently don't support forwarding request source IP data to App Runner private services associated with WAF. If your App Runner application requires source IP/CIDR incoming traffic control rules, you must use [security group rules for private endpoints](network-pl-manage.md) instead of WAF web ACLs.

**To associate an AWS WAF web ACL**

1. Create an AWS WAF web ACL for your service with your preferred set of rule actions to `Allow` or `Block` the web requests to your service. For more information about AWS WAF APIs, see [CreateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateWebACL.html) in the *AWS WAF API Reference Guide*.  
**Example Create a web ACL - Request**  

   ```
   aws wafv2
   create-web-acl
   --region <region>
   --name <web-acl-name>
   --scope {{REGIONAL}}
   --default-action {{Allow={}}}
   --visibility-config <file-name.json>
   # This is the file containing the WAF web ACL rules.
   ```

1. Associate the web ACL that you created with the App Runner service using the `associate-web-acl` AWS WAF public API. For more information about AWS WAF APIs, see [AssociateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_AssociateWebACL.html) in the *AWS WAF API Reference Guide*.
**Note**  
When you create a web ACL, a small amount of time passes before the web ACL fully propagates and is available to App Runner. The propagation time can be from a few seconds to a number of minutes. AWS WAF returns a `WAFUnavailableEntityException` when you try to associate a web ACL before it has fully propagated.   
If you refresh the browser or navigate away from the App Runner console before the web ACL is fully propagated, the association fails to occur. However, you can navigate within the App Runner console.  
**Example Associating a web ACL - Request**  

   ```
   aws wafv2 associate-web-acl
   --resource-arn <apprunner_service_arn>
   --web-acl-arn <web_acl_arn>
   --region <region>
   ```

1. Verify that the web ACL is associated with your App Runner service using the `get-web-acl-for-resource` AWS WAF public API. For more information about AWS WAF APIs, see [GetWebACLForResource](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetWebACLForResource.html) in the *AWS WAF API Reference Guide*.   
**Example Verify web ACL for resource - Request**  

   ```
   aws wafv2 get-web-acl-for-resource
   --resource-arn <apprunner_service_arn>
   --region <region>
   ```

   If there are no web ACLs associated with your service, you receive a blank response.

### Deleting an AWS WAF web ACL using AWS CLI
<a name="waf-manage.api.disassociate"></a>

You can't delete an AWS WAF web ACL if it's associated with an App Runner service.

**To delete an AWS WAF web ACL**

1. Disassociate the web ACL from your App Runner service by using the `disassociate-web-acl` AWS WAF public API. For more information about AWS WAF APIs, see [DisassociateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_DisassociateWebACL.html) in the *AWS WAF API Reference Guide*.   
**Example Disassociating a web ACL - Request**  

   ```
   aws wafv2 disassociate-web-acl
   --resource-arn <apprunner_service_arn>
   --region <region>
   ```

1. Verify that the web ACL is disassociated from your App Runner service using the `get-web-acl-for-resource` AWS WAF public API.   
**Example Verify that the web ACL is disassociated - Request**  

   ```
   aws wafv2 get-web-acl-for-resource
   --resource-arn <apprunner_service_arn>
   --region <region>
   ```

   The disassociated web ACL isn't listed for your App Runner service. If there are no web ACLs associated with your service, you receive a blank response.

1. Delete the disassociated web ACL using the `delete-web-acl` AWS WAF public API. For more information about AWS WAF APIs, see [DeleteWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_DeleteWebACL.html) in the *AWS WAF API Reference Guide*.  
**Example Delete a web ACL - Request**  

   ```
   aws wafv2 delete-web-acl
   --name <web_acl_name>
   --scope {{REGIONAL}}
   --id <web_acl_id>
   --lock-token <web_acl_lock_token>
   --region <region>
   ```

1. Verify that the web ACL is deleted using the `list-web-acl` AWS WAF public API. For more information about AWS WAF APIs, see [ListWebACLs](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListWebACLs.html) in the *AWS WAF API Reference Guide*.  
**Example Verify that the web ACL is deleted - Request**  

   ```
   aws wafv2 list-web-acls 
   --scope {{REGIONAL}}
   --region <region>
   ```

   The deleted web ACL is no longer be listed.
**Note**  
If a web ACL is associated with other active App Runner services or other resources, such as Amazon Cognito user pools, the web ACL can't be deleted. 

### Listing App Runner services that are associated with a web ACL
<a name="waf-manage.api.list"></a>

A web ACL can be associated with multiple App Runner services and other resources. List the App Runner services associated with a web ACL using the `list-resources-for-web-acl` AWS WAF public API. For more information about AWS WAF APIs, see [ListResourcesForWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListResourcesForWebACL.html) in the *AWS WAF API Reference Guide*. 

**Example List App Runner services associated with a web ACL - Request**  

```
aws wafv2 list-resources-for-web-acl
--web-acl-arn <WEB_ACL_ARN>
--resource-type {{APP_RUNNER_SERVICE}}
--region <REGION>
```

**Example List App Runner services associated with a web ACL - Response**  
The following example illustrates the response when there are no App Runner services that are associated with a web ACL.  

```
{
  "ResourceArns": []
}
```

**Example List App Runner services associated with a web ACL - Response**  
The following example illustrates the response when there are App Runner services that are associated with a web ACL.  

```
{
  "ResourceArns": [
    "arn:aws:apprunner:<region>:<aws_account_id>:service/<service_name>/<service_id>"
  ]
}
```

## Testing and logging AWS WAF web ACLs
<a name="waf-manage.testing-and-logging"></a>

When you set a rule action to **Count** in your web ACL, AWS WAF adds the request to a count of requests that match the rule. To test a web ACL with your App Runner service, set rule actions to **Count** and consider the volume of requests that match each rule. For example, you set a rule for the `Block` action that matches a large number of requests that you determine to be normal user traffic. In that case, you might need to reconfigure your rule. For more information, see [Testing and tuning your AWS WAF protections](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html) in the *AWS WAF Developer Guide*. 

You can also configure AWS WAF to log request headers to an Amazon CloudWatch Logs log group, an Amazon Simple Storage Service (Amazon S3) bucket, or an Amazon Data Firehose. For more information, see [Logging web ACL traffic](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html) in the *AWS WAF Developer Guide*. 

To access logs related to the web ACL that's associated with your App Runner service, refer to the following log fields: 
+ `httpSourceName`: Contains `APPRUNNER` 
+ `httpSourceId`: Contains `customeraccountid-apprunnerserviceid`

For more information, see [Log Examples](https://docs.aws.amazon.com/waf/latest/developerguide/logging-examples.html) in the *AWS WAF Developer Guide*. 

**Important**  
Source IP rules for App Runner private services that are associated with WAF web ACLs *do not adhere to IP based rules*. This is because we currently don't support forwarding request source IP data to App Runner private services associated with WAF. If your App Runner application requires source IP/CIDR incoming traffic control rules, you must use [security group rules for private endpoints](network-pl-manage.md) instead of WAF web ACLs.