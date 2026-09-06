

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# CodeDeploy Application \| Deploy
<a name="deployment-applications-codedeploy-application-deploy"></a>

Deploy a revision of an existing AWS CodeDeploy application, which are source files CodeDeploy will deploy to your instances or scripts CodeDeploy will run on your instances.

**Full classification:** Deployment \| Applications \| CodeDeploy application \| Deploy

## Change Type Details
<a name="ct-2edc3sd1sqmrb-DACd-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-2edc3sd1sqmrb | 
| Current version | 2.0 | 
| Expected execution duration | 360 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="deployment-applications-codedeploy-application-deploy-info"></a>

### Deploy CodeDeploy application
<a name="ex-cd-app-deploy-col"></a>

#### Deploying a CodeDeploy application with the console
<a name="cd-app-deploy-con"></a>

![Deploy CodeDeploy Application change type showing ID, version 2.0, and automated execution mode.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiCDAppDeployCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

#### Deploying a CodeDeploy application with the CLI
<a name="cd-app-deploy-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-2edc3sd1sqmrb" --change-type-version "2.0" --title "{{Stack-Deploy-CD-App}}" --execution-parameters "{\"Description\":\"{{MyCDAppDeployTest}}\",\"VpcId\":\"{{VPC_ID}}\",\"Name\":\"{{Test}}\",\"TimeoutInMinutes\":60,\"Parameters\":{\"CodeDeployApplicationName\":\"{{TestCDApp}}\",\"CodeDeployDeploymentConfigName\":\"{{CodeDeployDefault.OneAtATime}}\",\"CodeDeployDeploymentGroupName\":\"{{TestCDDepGroup}}\",\"CodeDeployIgnoreApplicationStopFailures\":{{false}},\"CodeDeployRevision\":{\"RevisionType\":\"{{S3}}\",\"S3Location\":{\"S3Bucket\":\"{{amzn-s3-demo-bucket}}\",\"S3BundleType\":\"{{tar}}\",\"S3Key\":\"{{TestKey}}\"}}}}"{{Test}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for the CodeDeploy application deployment CT; this example names it DeployCDAppParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2edc3sd1sqmrb" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeployCDAppParams.json
   ```

1. Modify the JSON file as follows. For example, you can replace the contents with something like this:

   ```
   {
   "Description":                      "{{Deploy WordPress CodeDeploy Application}}",
   "VpcId":                            "{{VPC_ID}}",
   "Name":                             "{{WP CodeDeploy Deployment Group}}",
   "TimeoutInMinutes":                 360,
   "Parameters":   {
       "CodeDeployApplicationName":        "{{WordPressCDApp}}",
       "CodeDeployDeploymentGroupName":    "{{WordPressCDDepGroup}}",
       "CodeDeployIgnoreApplicationStopFailures": {{false}},
       "CodeDeployRevision": {
         "RevisionType": "{{S3}}",
         "S3Location": {
           "S3Bucket": "{{amzn-s3-demo-bucket}}",
           "S3BundleType": "{{zip}}",
           "S3Key": "wordpress.{{zip}}" }
           }
       }
   }
   ```

1. Output the JSON template for CreateRfc to a file in your current folder; this example names it DeployCDAppRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > DeployCDAppRfc.json
   ```

1. Modify and save the DeployCDAppRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{2.0}}",
   "ChangeTypeId":         "ct-2edc3sd1sqmrb",
   "Title":                "{{CD-Deploy-For-CD-APP-Stack-RFC}}"
   }
   ```

1. Create the RFC, specifying the execution parameters file and the DeployCDAppRfc file:

   ```
   aws amscm create-rfc --cli-input-json file://DeployCDAppRfc.json  --execution-parameters file://DeployCDAppParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-cd-app-deploy-tip"></a>

For more information, see [Create a deployment with CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-create.html).

## Execution Input Parameters
<a name="deployment-applications-codedeploy-application-deploy-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-2edc3sd1sqmrb](schemas.md#ct-2edc3sd1sqmrb-schema-section).

## Example: Required Parameters
<a name="deployment-applications-codedeploy-application-deploy-ex-min"></a>

```
{
  "Description": "Stack Description.",
  "VpcId": "vpc-01234567890abcdef",
  "Name": "Name your stack",
  "TimeoutInMinutes": 60,
  "Parameters": {
    "CodeDeployApplicationName": "foobarapp",
    "CodeDeployDeploymentGroupName": "myfoogroup",
    "CodeDeployRevision": {
      "RevisionType": "S3",
      "S3Location": {
        "S3Bucket": "mybucket",
        "S3BundleType": "zip",
        "S3Key": "mykey"
      }
    }
  }
}
```

## Example: All Parameters
<a name="deployment-applications-codedeploy-application-deploy-ex-max"></a>

```
{
  "Description": "Stack Description.",
  "VpcId": "vpc-12345678",
  "Name": "Name your stack",
  "TimeoutInMinutes": 60,
  "Parameters": {
    "CodeDeployApplicationName": "foobarapp",
    "CodeDeployDeploymentConfigName": "CodeDeployDefault.HalfAtATime",
    "CodeDeployDeploymentGroupName": "myfoogroup",
    "CodeDeployIgnoreApplicationStopFailures": false,
    "CodeDeployRevision": {
      "RevisionType": "S3",
      "S3Location": {
        "S3Bucket": "mybucket",
        "S3BundleType": "zip",
        "S3ETag": "1234567",
        "S3Key": "mykey",
        "S3Version": "versionfoo"
      }
    }
  }
}
```