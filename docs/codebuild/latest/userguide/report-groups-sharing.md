

# Share report groups
<a name="report-groups-sharing"></a>

Report group sharing allows multiple AWS accounts or users to view a report group, its unexpired reports, and the test results of its reports. In this model, the account that owns the report group (owner) shares a report group with other accounts (consumers). A consumer cannot edit a report group. A report expires 30 days after it is created.

**Topics**
+ [Share a report group](#report-groups-sharing-share)
+ [Related services](#report-groups-sharing-related)
+ [Access report groups shared with you](report-groups-sharing-access-prereqs.md)
+ [Unshare a shared report group](report-groups-sharing-unshare.md)
+ [Identify a shared report group](report-groups-sharing-identify.md)
+ [Shared report group permissions](report-groups-sharing-perms.md)

## Share a report group
<a name="report-groups-sharing-share"></a>

 When you share a report group, the consumer is granted read-only access to the report group and its reports. The consumer can use the AWS CLI to view the report group, its reports, and the test case results for each report. The consumer cannot: 
+  View a shared report group or its reports in the CodeBuild console. 
+  Edit a shared report group. 
+  Use the ARN of the shared report group in a project to run a report. A project build that specifies a shared report group fails. 

You can use the CodeBuild console to add a report group to an existing resource share. If you want to add the report group to a new resource share, you must first create it in the [AWS RAM console](https://console.aws.amazon.com/ram).

To share a report group with organizational units or an entire organization, you must enable sharing with AWS Organizations. For more information, see [Enable sharing with AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html) in the *AWS RAM User Guide*.

You can use the CodeBuild console, AWS RAM console, or AWS CLI to share report groups that you own.

**Prerequisite**  
To share a report group, your AWS account must own it. You cannot share a report group that has been shared with you.

**To share a report group that you own (CodeBuild console)**

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home).

1. In the navigation pane, choose **Report groups**.

1.  Choose the project you want to share, and then choose **Share**. For more information, see [Create a resource share](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-create) in the *AWS RAM User Guide*. 

**To share report groups that you own (AWS RAM console)**  
See [Creating a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-create) in the *AWS RAM User Guide*.

**To share report groups that you own (AWS RAM command)**  
Use the [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) command.

 **To share a report group that you own (CodeBuild command)** 

Use the [put-resource-policy](https://docs.aws.amazon.com/cli/latest/reference/codebuild/put-resource-policy.html) command:

1. Create a file named `policy.json` and copy the following into it. 

------
#### [ JSON ]

****  

   ```
   {
      "Version":"2012-10-17",		 	 	 
      "Statement":[{
        "Effect":"Allow",
        "Principal":{
          "AWS":"{{111122223333}}"
        },
        "Action":[
          "codebuild:BatchGetReportGroups",
          "codebuild:BatchGetReports",
          "codebuild:ListReportsForReportGroup",
          "codebuild:DescribeTestCases"],
        "Resource":"{{arn:aws:iam::*:role/Service*}}"
      }]
    }
   ```

------

1. Update `policy.json` with the report group ARN and identifiers to share it with. The following example grants read-only access to the report group with the ARN `arn:aws:codebuild:us-west-2:123456789012:report-group/my-report-group` to Alice and the root user for the AWS account identified by 123456789012. 

------
#### [ JSON ]

****  

   ```
   {
      "Version":"2012-10-17",		 	 	 
      "Statement":[{
        "Effect":"Allow",
        "Principal":{
          "AWS": [
             "arn:aws:iam::123456789012:user/Alice",
             "123456789012"
           ]
        },
        "Action":[
          "codebuild:BatchGetReportGroups",
          "codebuild:BatchGetReports",
          "codebuild:ListReportsForReportGroup",
          "codebuild:DescribeTestCases"],
        "Resource":"arn:aws:codebuild:us-west-2:123456789012:report-group/my-report-group"
      }]
    }
   ```

------

1. Run the following command. 

   ```
   aws codebuild put-resource-policy --resource-arn {{report-group-arn}} --policy file://policy.json
   ```

## Related services
<a name="report-groups-sharing-related"></a>

Report group sharing integrates with AWS Resource Access Manager (AWS RAM), a service that makes it possible for you to share your AWS resources with any AWS account or through AWS Organizations. With AWS RAM, you share resources that you own by creating a *resource share* that specifies the resources and the consumers to share them with. Consumers can be individual AWS accounts, organizational units in AWS Organizations, or an entire organization in AWS Organizations.

For more information, see the *[AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/)*.