

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Load Balancer (ELB) Stack \| Replace Listener Certificate
<a name="management-advanced-load-balancer-elb-stack-replace-listener-certificate"></a>

Replace the certificate of an existing Elastic (Classic) Load Balancer (ELB) listener. Use the RemediateDrift parameter to have the automation try to remediate the stack drift, if drift is introduced in the CloudFormation stack that was used to create the load balancer.

**Full classification:** Management \| Advanced stack components \| Load balancer (ELB) stack \| Replace listener certificate

## Change Type Details
<a name="ct-0aqx5t0pgfzbg-MALr-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-0aqx5t0pgfzbg | 
| Current version | 1.0 | 
| Expected execution duration | 60 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="management-advanced-load-balancer-elb-stack-replace-listener-certificate-info"></a>

### Replace an ELB listener certificate
<a name="ex-elb-replace-listener-cert-col"></a>

#### Replacing an ELB listener certificate with the Console
<a name="elb-replace-listener-cert-con"></a>

Screenshot of this change type in the AMS console:

![Replace ELB Listener Certificate change type showing ID ct-0aqx5t0pgfzbg and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiElbReplaceListenerCertCT.png)


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

#### Replacing an ELB listener certificate with the CLI
<a name="elb-replace-listener-cert-cli"></a>

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

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm  create-rfc --change-type-id "ct-0aqx5t0pgfzbg" --change-type-version "1.0" --title "{{Replace listener certificate}}" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-SetClassicLoadBalancerCertificate\",\"Region\": \"{{us-east-1}}\",\"Parameters\":{\"LoadBalancerName\":[\"{{testalb}}\"],\"SSLCertificateArn\":[\"{{arn:aws:acm:us-east-1:123456789012:certificate/c96c73cd-d082-4fa9-bbf2-09d8600d84ad}}\"],"LoadBalancerPort":[\"{{443}}\"],\"RemediateStackDrift\":[\"{{True}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it ReplaceListCertParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-0aqx5t0pgfzbg" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ReplaceListCertParams.json
   ```

1. Modify and save the ReplaceListCertParams file. The values given in the example reflect a deployment of a Public ELB, with the health check thresholds relaxed and the ELBScheme set to `true` (for a public ELB). Note that the `Name` you set here is not the actual ELB name, you can find that name in the console as the ELB instance name. Not all optional parameters are shown in the example.

   ```
   {
       "DocumentName": "AWSManagedServices-SetClassicLoadBalancerCertificate",
       "Region": "us-east-1",
       "Parameters": {
           "LoadBalancerName": [
               "{{testalb}}"
           ],
           "SSLCertificateArn": [
               "arn:aws:acm:us-east-1:123456789012:certificate/c96c73cd-d082-4fa9-bbf2-09d8600d84ad"
           ],
           "LoadBalancerPort":[
                "443"
            ]
           "RemediateStackDrift": [
               "True"
           ]
       }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it ReplaceListCertRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > ReplaceListCertRfc.json
   ```

1. Modify and save the ReplaceListCertRfc.json file. For example, you can replace the contents with something like this: 

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",	
   "ChangeTypeId":         "ct-0aqx5t0pgfzbg",
   "Title":                "{{My-ELB-Create-RFC}}"
   }
   ```

1. Create the RFC, specifying the ReplaceListCertRfc file and the ReplaceListCertParams file:

   ```
   aws amscm create-rfc --cli-input-json file://ReplaceListCertRfc.json --execution-parameters file://ReplaceListCertParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

1. To view the load balancer, look in the execution output: Use the `stack_id` to view the ELB in the Cloud Formation console or to create a Delete Stack RFC, use the ELBCName value to programmatically access the ELB.

#### Tips
<a name="ex-elb-replace-listener-cert-tip"></a>

 For information about Application Load Balancers, see [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html). 

## Execution Input Parameters
<a name="management-advanced-load-balancer-elb-stack-replace-listener-certificate-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-0aqx5t0pgfzbg](schemas.md#ct-0aqx5t0pgfzbg-schema-section).

## Example: Required Parameters
<a name="management-advanced-load-balancer-elb-stack-replace-listener-certificate-ex-min"></a>

```
{
    "DocumentName": "AWSManagedServices-SetClassicLoadBalancerCertificate",
    "Region": "us-east-1",
    "Parameters": {
        "LoadBalancerName": [
            "testclassiclb"
        ],
        "SSLCertificateArn": [
            "arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012"
        ]
    }
}
```

## Example: All Parameters
<a name="management-advanced-load-balancer-elb-stack-replace-listener-certificate-ex-max"></a>

```
{
    "DocumentName": "AWSManagedServices-SetClassicLoadBalancerCertificate",
    "Region": "us-east-1",
    "Parameters": {
        "LoadBalancerName": [
            "testclassiclb"
        ],
        "LoadBalancerPort": [
            "443"
        ],
        "RemediateStackDrift": [
            "False"
        ],
        "SSLCertificateArn": [
            "arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012"
        ]
    }
}
```