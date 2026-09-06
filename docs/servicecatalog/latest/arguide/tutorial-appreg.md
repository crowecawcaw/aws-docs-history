

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Tutorial: Create your first application and attribute group in AppRegistry
<a name="tutorial-appreg"></a>

 The procedures in this topic describe how to get started with AppRegistry. 

 In the first section, you learn how to create an application and attribute group, as well as how to add an attribute group and application resource to an application. 

 In the second section, you learn how to discover information about applications and attribute groups. 

**Note**  
 The procedures in topic show you how to complete AppRegistry tasks in the AWS CLI. You can use the information from the following procedures to complete the AppRegistry tasks in the AWS Management Console by following the appropriate links. 

**Topics**
+ [Create your first application and attribute group](#tutorial-register)
+ [Discover information about your applications](#query-appreg)

## Create your first application and attribute group
<a name="tutorial-register"></a>

 The first two procedures in this section describe how to create an application and attribute group. The following procedures in this section describe how to add an attribute group and application resource to an application. 

### Create an application
<a name="w2aac11c13c13b5"></a>

 The procedure in this section shows how to create an application in the AWS CLI. For information about creating an application in the console, see [Creating applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-apps.html). 

 The example describes how to format a command from the perspective of an application builder. 
+  To create an application in the AWS CLI, run the following command: 

```
aws servicecatalog-appregistry create-application --name "CC_Payments_App" --description "Real-time payments service for processing customer orders."
```

**Example: Output**  
The following shows the output you might encounter.

```
{
        "application": {
            "id": "{{your-resource-id}}",
            "arn": "arn:aws:servicecatalog:{{your-Region}}:{{your-account-id}}:/applications/{{your-resource-id}}",
            "name": "CC_Payments_App",
            "description": "Real-time payments service for processing customer orders.",
            "creationTime": "2023-12-12T20:17:20.017000+00:00",
            "lastUpdateTime": "2023-12-12T20:17:20.017000+00:00",
            "applicationTag": {
                "awsApplication": "arn:aws:resource-groups:{{your-Region}}:{{your-account-id}}:group/CC_Payments_App/{{your-resource-id}}"
            }
        }
}
```

**Note**  
 When you create an application, AppRegistry vends a user tag called the `awsApplication` tag on your behalf. You can add this tag to resources, so you can identify which resources are associated with an application. For more information, see [the `awsApplication` tag](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html#ar-user-tags). 

### Create an attribute group
<a name="w2aac11c13c13b7"></a>

 The procedures in this section show how to create two attribute groups. For information about creating an attribute group in the console, see [Creating attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-attr-groups.html). 

 The examples describe how to format commands from the perspective of an administrator and application builder. 

**Note**  
 The following command and output is for an attribute group an administrator might create to share in multiple accounts. 
+  To create an attribute group in the AWS CLI from the administrator's perspective, run the following command: 

```
aws servicecatalog-appregistry create-attribute-group --name "Corp_Application_Classification_High" --description "Applications classified as high." --attributes '{"ApplicationResilience":"high","DataSecurity":"high","DataSensitivity":"high"}'
```

**Example: Output**  
 The following shows the output you might encounter. 

```
{
  "attributeGroup": {
    "id": "{{your-resource-id}}",
    "arn": "arn:aws:servicecatalog:{{your-Region}}:{{your-account-id}}:/attribute-groups/{{your-resource-id}}",
    "name": "Corp_Application_Classification_High",
    "description": "Applications classified as high.",
    "creationTime": "2023-12-12T20:14:27.413000+00:00",
    "lastUpdateTime": "2023-12-12T20:14:27.413000+00:00",
    "tags": {}
  }
}
```

**Note**  
 The following command and output is for an attribute group an application builder might create to track information about an application. 
+  To create an attribute group in the AWS CLI from the application builder's perspective, run the following command: 

```
aws servicecatalog-appregistry create-attribute-group --name "Commerce_Payments" --description "24X7 real-time payments processing." --attributes '{"Team":"payments","app-type":"processing","SLA":"0.1h","Runtime":"Java-12","Support":{"Phone":"XXX-XXX-XXXX","Email":"support@app.com"},"Compliance":["SOC-1","PCI"]}}'
```

**Example: Output**  
 The following shows the output you might encounter. 

```
{
    "attributeGroup": {
        "id": "{{your-resource-id}}",
        "arn": "arn:aws:servicecatalog:{{your-Region}}:{{your-account-id}}:/attribute-groups/{{your-resource-id}}",
        "name": "Commerce_Payments",
        "description": "24X7 real-time payments processing.",
        "creationTime": "2023-12-12T20:15:49.658000+00:00",
        "lastUpdateTime": "2023-12-12T20:15:49.658000+00:00",
        "tags": {}
    }
}
```

### Add an attribute group to an application
<a name="w2aac11c13c13b9"></a>

 The procedure in this section shows how to add an attribute group with an application. For information about associating an attribute group with an application in the console, see [Associating and disassociating attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-attr-groups.html). 

 The example includes information from the application and attribute group you created from the application builder's perspective. 
+  To add an attribute group to an application, run the following command: 

```
aws servicecatalog-appregistry associate-attribute-group --application "CC_Payments_App" --attribute-group "Commerce_Payments" 
```

**Example: Output**  
 The following shows the output you might encounter. 

```
{
"applicationArn": "arn:aws:servicecatalog:{{your-Region}}:{{your-account-id}}:/applications/{{your-resource-id}}",
"attributeGroupArn": "arn:aws:servicecatalog:{{your-Region}}:{{your-account-id}}:/attribute-groups/{{your-resource-id}}"
}
```

#### Add AWS CloudFormation stack resource to an application
<a name="w2aac11c13c13b9c15"></a>

 The procedure in this section shows how to add an CloudFormation stack resource to an application in the AWS CLI. For information about associating an CloudFormation stack resource with an application in the console, see [Associating and disassociating application resources](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-resources.html). 

 The example includes information from the application you created from the application builder's perspective and a CloudFormation stack resource you must create separately. 

**Important**  
 To complete this tutorial, you must create a CloudFormation stack resource named **cc\_payment\_app\_cfn\_stackCODE**. For information about how to create a CloudFormation stack resource, see [Creating a stack](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-attr-groups.html) in the *CloudFormation User Guide* 
+  To add an CloudFormation stack resource to an application, run the following command: 

```
aws servicecatalog-appregistry associate-resource --application CC_Payments_App --resource-type CFN_STACK --resource cc_payment_app_cfn_stackCODE --apply-tag cc_payment_application
```

**Example: Output**  
 The following shows the output you might encounter. 

```
{
  "applicationArn": "arn:aws:servicecatalog:{{your-Region}}: XXXXXXXXXX:/applications/{{your-resource-id}}",
  "resourceArn": "arn:aws:cloudformation:{{you-Region}}: XXXXXXXXXX:stack/cc_payment_app_cfn_stack/{{your-resource-id}}"
}
```

## Discover information about your applications
<a name="query-appreg"></a>

 The procedures in this section describe how you can use AppRegistry to find information about applications and attribute groups. 

### View your applications
<a name="w2aac11c13c15b5"></a>

 The following shows how to view a list of your applications using the AWS CLI. For information about viewing your applications in the console, see [Managing applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-app.html). 

 If you created an application other than the application described in the previous section, the output in this procedure will look different. 

**Note**  
 The following command will only show the applications in your current AWS Region. 
+  To view a your applications in your application registry, run the following command: 

```
aws servicecatalog-appregistry list-applications
```

**Example: Output**  
 The following shows the output you might encounter. 

```
{
    "applications": [
        {
            "id": "{{your-resource-id}}",
            "arn": "arn:aws:servicecatalog:{{your-Region}}:{{your-account-id}}:/applications/{{your-resource-id}}",
            "name": "CC_Payments_App",
            "description": "Real-time payments service for processing customer orders.",
            "creationTime": "2023-12-12T20:17:20.017000+00:00",
            "lastUpdateTime": "2023-12-12T20:17:20.017000+00:00"
        }
    ]
}
```

### View your attribute groups
<a name="w2aac11c13c15b7"></a>

 The following shows how to view a list of your attribute groups using the AWS CLI. For information about viewing your attribute groups in the console, see [Managing attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-attributes.html). 

 If you created an attribute group other than the attribute groups described in the previous section, the output in this procedure will look different. 

**Note**  
 The following command will only show the attribute groups in your current AWS Region. 
+  To view your attribute groups, run the following command: 

```
aws servicecatalog-appregistry list-attribute-groups
```

**Example: Output**  
 The following shows the output you might encounter. 

```
{
    "attributeGroups": [
        {
            "id": "{{your-resource-id}}",
            "arn": "arn:aws:servicecatalog:{{your-Region}}:{{your-account-id}}:/attribute-groups/{{your-resource-id}}",
            "name": "Corp_Application_Classification_High",
            "description": "Applications classified as high.",
            "creationTime": "2023-12-12T20:14:27.413000+00:00",
            "lastUpdateTime": "2023-12-12T20:14:27.413000+00:00"
        },
        {
            "id": "{{your-resource-id}}",
            "arn": "arn:aws:servicecatalog:{{your-Region}}:{{your-account-id}}:/attribute-groups/{{your-resource-id}}",
            "name": "Commerce_Payments",
            "description": "24X7 real-time payments processing.",
            "creationTime": "2023-12-12T20:15:49.658000+00:00",
            "lastUpdateTime": "2023-12-12T20:15:49.658000+00:00"
        }
    ]
}
```

### View an attribute group that's been added to an application
<a name="w2aac11c13c15b9"></a>

 The following shows how to view an attribute group that's been added to an application in the AWS CLI. For information about how to do this in the console, see [Using application details](https://docs.aws.amazon.com/servicecatalog/latest/arguide/access-app-details.html). 

 The output in this procedure shows the attribute group you created from the application builder's perspective in the previous section. 
+  To view an attribute group that's been added to an application, run the following command: 

```
aws servicecatalog-appregistry list-associated-attribute-groups --application "CC_Payments_App"
```

**Example: Output**  
 The following shows the output you might encounter. 

```
{
    "attributeGroups": [
        "{{your-resource-id}}"
    ]
}
```