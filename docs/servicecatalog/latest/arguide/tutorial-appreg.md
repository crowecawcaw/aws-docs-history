# Tutorial: Create your first application and attribute group in AppRegistry

The procedures in this topic describe how to get started with AppRegistry.

In the first section, you learn how to create an application and attribute group, as well as how to add an attribute group and application resource to an application.

In the second section, you learn how to discover information about applications and attribute groups.

###### Note

The procedures in topic show you how to complete AppRegistry tasks in the AWS CLI.
You can use the information from the following procedures to complete the AppRegistry tasks in the AWS Management Console by following the appropriate links.

###### Topics

- [Create your first application and attribute group](#tutorial-register "#tutorial-register")
- [Discover information about your applications](#query-appreg "#query-appreg")

## Create your first application and attribute group

The first two procedures in this section describe how to create an application and attribute group.
The following procedures in this section describe how to add an attribute group and application resource to an application.

### Create an application

The procedure in this section shows how to create an application in the AWS CLI.
For information about creating an application in the console, see [Creating applications](create-apps.md "create-apps.md").

The example describes how to format a command from the perspective of an application builder.

- To create an application in the AWS CLI, run the following command:

```
aws servicecatalog-appregistry create-application --name "CC_Payments_App" --description "Real-time payments service for processing customer orders."
```

######

Example: Output

The following shows the output you might encounter.

```
{
        "application": {
            "id": "`your-resource-id`",
            "arn": "arn:aws:servicecatalog:`your-Region`:`your-account-id`:/applications/`your-resource-id`",
            "name": "CC_Payments_App",
            "description": "Real-time payments service for processing customer orders.",
            "creationTime": "2023-12-12T20:17:20.017000+00:00",
            "lastUpdateTime": "2023-12-12T20:17:20.017000+00:00",
            "applicationTag": {
                "awsApplication": "arn:aws:resource-groups:`your-Region`:`your-account-id`:group/CC_Payments_App/`your-resource-id`"
            }
        }
}
```

###### Note

When you create an application, AppRegistry vends a user tag called the `awsApplication` tag on your behalf.
You can add this tag to resources, so you can identify which resources are associated with an application.
For more information, see [the `awsApplication` tag](overview-appreg.md#ar-user-tags "overview-appreg.md#ar-user-tags").

### Create an attribute group

The procedures in this section show how to create two attribute groups.
For information about creating an attribute group in the console,
see [Creating attribute groups](create-attr-groups.md "create-attr-groups.md").

The examples describe how to format commands from the perspective of an administrator and application builder.

###### Note

The following command and output is for an attribute group an administrator might create to share in multiple accounts.

- To create an attribute group in the AWS CLI from the administrator's perspective, run the following command:

```
aws servicecatalog-appregistry create-attribute-group --name "Corp_Application_Classification_High" --description "Applications classified as high." --attributes '{"ApplicationResilience":"high","DataSecurity":"high","DataSensitivity":"high"}'
```

###### Example: Output

The following shows the output you might encounter.

```
{
  "attributeGroup": {
    "id": "`your-resource-id`",
    "arn": "arn:aws:servicecatalog:`your-Region`:`your-account-id`:/attribute-groups/`your-resource-id`",
    "name": "Corp_Application_Classification_High",
    "description": "Applications classified as high.",
    "creationTime": "2023-12-12T20:14:27.413000+00:00",
    "lastUpdateTime": "2023-12-12T20:14:27.413000+00:00",
    "tags": {}
  }
}
```

###### Note

The following command and output is for an attribute group an application builder might create to track information about an application.

- To create an attribute group in the AWS CLI from the application builder's perspective, run the following command:

```
aws servicecatalog-appregistry create-attribute-group --name "Commerce_Payments" --description "24X7 real-time payments processing." --attributes '{"Team":"payments","app-type":"processing","SLA":"0.1h","Runtime":"Java-12","Support":{"Phone":"XXX-XXX-XXXX","Email":"support@app.com"},"Compliance":["SOC-1","PCI"]}}'
```

###### Example: Output

The following shows the output you might encounter.

```
{
    "attributeGroup": {
        "id": "`your-resource-id`",
        "arn": "arn:aws:servicecatalog:`your-Region`:`your-account-id`:/attribute-groups/`your-resource-id`",
        "name": "Commerce_Payments",
        "description": "24X7 real-time payments processing.",
        "creationTime": "2023-12-12T20:15:49.658000+00:00",
        "lastUpdateTime": "2023-12-12T20:15:49.658000+00:00",
        "tags": {}
    }
}
```

### Add an attribute group to an application

The procedure in this section shows how to add an attribute group with an application.
For information about associating an attribute group with an application in the console,
see [Associating and disassociating attribute groups](associate-attr-groups.md "associate-attr-groups.md").

The example includes information from the application and attribute group you created from the application builder's perspective.

- To add an attribute group to an application, run the following command:

```
aws servicecatalog-appregistry associate-attribute-group --application "CC_Payments_App" --attribute-group "Commerce_Payments"
```

###### Example: Output

The following shows the output you might encounter.

```
{
"applicationArn": "arn:aws:servicecatalog:`your-Region`:`your-account-id`:/applications/`your-resource-id`",
"attributeGroupArn": "arn:aws:servicecatalog:`your-Region`:`your-account-id`:/attribute-groups/`your-resource-id`"
}
```

#### Add AWS CloudFormation stack resource to an application

The procedure in this section shows how to add an AWS CloudFormation stack resource to an application in the AWS CLI.
For information about associating an AWS CloudFormation stack resource with an application in the console,
see [Associating and disassociating application resources](associate-resources.md "associate-resources.md").

The example includes information from the application you created from the application builder's perspective and a AWS CloudFormation stack resource you must create separately.

###### Important

To complete this tutorial, you must create a AWS CloudFormation stack resource named **cc_payment_app_cfn_stackCODE**.
For information about how to create a AWS CloudFormation stack resource,
see [Creating a stack](associate-attr-groups.md "associate-attr-groups.md") in the _AWS CloudFormation User Guide_

- To add an AWS CloudFormation stack resource to an application, run the following command:

```
aws servicecatalog-appregistry associate-resource --application CC_Payments_App --resource-type CFN_STACK --resource cc_payment_app_cfn_stackCODE --apply-tag cc_payment_application
```

###### Example: Output

The following shows the output you might encounter.

```
{
  "applicationArn": "arn:aws:servicecatalog:`your-Region`: XXXXXXXXXX:/applications/`your-resource-id`",
  "resourceArn": "arn:aws:cloudformation:`you-Region`: XXXXXXXXXX:stack/cc_payment_app_cfn_stack/`your-resource-id`"
}
```

## Discover information about your applications

The procedures in this section describe how you can use AppRegistry to find information about applications and attribute groups.

### View your applications

The following shows how to view a list of your applications using the AWS CLI.
For information about viewing your applications in the console, see [Managing applications](create-app.md "create-app.md").

If you created an application other than the application described in the previous section, the output in this procedure will look different.

###### Note

The following command will only show the applications in your current AWS Region.

- To view a your applications in your application registry, run the following command:

```
aws servicecatalog-appregistry list-applications
```

###### Example: Output

The following shows the output you might encounter.

```
{
    "applications": [
        {
            "id": "`your-resource-id`",
            "arn": "arn:aws:servicecatalog:`your-Region`:`your-account-id`:/applications/`your-resource-id`",
            "name": "CC_Payments_App",
            "description": "Real-time payments service for processing customer orders.",
            "creationTime": "2023-12-12T20:17:20.017000+00:00",
            "lastUpdateTime": "2023-12-12T20:17:20.017000+00:00"
        }
    ]
}
```

### View your attribute groups

The following shows how to view a list of your attribute groups using the AWS CLI.
For information about viewing your attribute groups in the console, see [Managing attribute groups](associate-attributes.md "associate-attributes.md").

If you created an attribute group other than the attribute groups described in the previous section, the output in this procedure will look different.

###### Note

The following command will only show the attribute groups in your current AWS Region.

- To view your attribute groups, run the following command:

```
aws servicecatalog-appregistry list-attribute-groups
```

###### Example: Output

The following shows the output you might encounter.

```
{
    "attributeGroups": [
        {
            "id": "`your-resource-id`",
            "arn": "arn:aws:servicecatalog:`your-Region`:`your-account-id`:/attribute-groups/`your-resource-id`",
            "name": "Corp_Application_Classification_High",
            "description": "Applications classified as high.",
            "creationTime": "2023-12-12T20:14:27.413000+00:00",
            "lastUpdateTime": "2023-12-12T20:14:27.413000+00:00"
        },
        {
            "id": "`your-resource-id`",
            "arn": "arn:aws:servicecatalog:`your-Region`:`your-account-id`:/attribute-groups/`your-resource-id`",
            "name": "Commerce_Payments",
            "description": "24X7 real-time payments processing.",
            "creationTime": "2023-12-12T20:15:49.658000+00:00",
            "lastUpdateTime": "2023-12-12T20:15:49.658000+00:00"
        }
    ]
}
```

### View an attribute group that's been added to an application

The following shows how to view an attribute group that's been added to an application in the AWS CLI.
For information about how to do this in the console, see [Using application details](access-app-details.md "access-app-details.md").

The output in this procedure shows the attribute group you created from the application builder's perspective in the previous section.

- To view an attribute group that's been added to an application, run the following command:

```
aws servicecatalog-appregistry list-associated-attribute-groups --application "CC_Payments_App"
```

###### Example: Output

The following shows the output you might encounter.

```
{
    "attributeGroups": [
        "`your-resource-id`"
    ]
}
```
