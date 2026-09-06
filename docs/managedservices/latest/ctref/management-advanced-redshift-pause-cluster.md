

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Redshift \| Pause Cluster
<a name="management-advanced-redshift-pause-cluster"></a>

Pause an Amazon Redshift cluster. If a recent snapshot is not available, a temporary manual snapshot is created with a retention period of one day. This snapshot is deleted towards the end of execution for both success and failure scenarios. It is safe for AMS to delete this snapshot as pausing the cluster creates an automated snapshot by default.

**Full classification:** Management \| Advanced stack components \| Redshift \| Pause cluster

## Change Type Details
<a name="ct-1n323w7eu27u9-MARp-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-1n323w7eu27u9 | 
| Current version | 1.0 | 
| Expected execution duration | 180 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="management-advanced-redshift-pause-cluster-info"></a>

### Pause cluster
<a name="ex-redshift-cluster-pause-col"></a>

#### Pausing a Redshift cluster with the Console
<a name="redshift-cluster-pause-con"></a>

Screenshot of this change type in the AMS console:

![Pause Redshift Cluster change type showing description, ID ct-1n323w7eu27u9, and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiRedshiftPauseClusterCT.png)


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

#### Pausing a Redshift cluster with the CLI
<a name="redshift-cluster-pause-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1n323w7eu27u9" --change-type-version "1.0" --title "{{Pause Amazon Redshift cluster}}" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-PauseRedshiftCluster\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"ClusterIdentifier\":[\"{{my-redshift-cluster}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type (ct-1n323w7eu27u9) to a JSON file named PauseRdshftClusterParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-1n323w7eu27u9" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > PauseRdshftClusterParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   Oracle example:

   ```
   {
     "DocumentName" : "AWSManagedServices-PauseRedshiftCluster",
     "Region" : "{{us-east-1}}",
     "Parameters" : {
       "ClusterIdentifier" : [
         "{{my-redshift-cluster}}"
       ]
     }
   }
   ```

1. Output the JSON template to a file in your current folder; this example names it PauseRdshftClusterRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > PauseRdshftClusterRfc.json
   ```

1. Modify and save the PauseRdshftClusterRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-1n323w7eu27u9",
   "Title":                "{{Pause Amazon Redshift cluster}}"
   }
   ```

1. Create the RFC, specifying the execution parameters file and the PauseRdshftClusterRfc file:

   ```
   aws amscm create-rfc --cli-input-json file://PauseRdshftClusterRfc.json --execution-parameters file://PauseRdshftClusterParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-redshift-cluster-pause-tip"></a>

To learn more about AWS Redshift, see [ Amazon Redshift](https://aws.amazon.com/redshift/).

## Execution Input Parameters
<a name="management-advanced-redshift-pause-cluster-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-1n323w7eu27u9](schemas.md#ct-1n323w7eu27u9-schema-section).

## Example: Required Parameters
<a name="management-advanced-redshift-pause-cluster-ex-min"></a>

```
Example not available.
```

## Example: All Parameters
<a name="management-advanced-redshift-pause-cluster-ex-max"></a>

```
{
    "DocumentName": "AWSManagedServices-PauseRedshiftCluster",
    "Region": "us-east-1",
    "Parameters": {
      "ClusterIdentifier": ["myredcluster1"]
    }
}
```