

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Setting up AWS resources through Jira Service Management to natively manage resources
<a name="jsd-it-lifecycle"></a>

The AWS Service Management Connector for Jira Service Management allows Jira Service Management end users to provision, manage, and operate AWS resources natively through Atlassian's Jira Service Management.
+ AWS Config linked resources
+ Suggested AWS Systems Manager remediations for an issue

The Connector provides two fields to use for any issue.
+ *AWS Config Linked Resources*: enables any resource with an entry in AWS Config to have its AWS Config information displayed on the issue in Jira. You can expand and see the information. You can link multiple AWS resources to an issue.
+ *AWS Systems Manager Automation Suggested Remediation*: enables SSM automation documents to be recorded against an issue. They then display, as suggested, ways to correct the issue. When a Jira user views the issue, they can see these suggested remediations and choose to apply them. You can attach multiple suggested remediations to an issue.

You can use the two fields individually, but they work very well together. Upon detecting an incident on an AWS resource or set of resources, setting both allows a Jira user to see the configuration information to confirm or better understand the problem, apply remediations to fix common problems, and then confirm in the AWS Config information that the problem has been fixed.

**To add AWS fields to an existing issue**

1. You must enable the project or projects for the Connector in **Connector Settings** under **Admin -> Manage Add-Ons**, as described in the Connector setup guide.

1. In **Admin**, **Projects**, open the project you want to use these fields.

1. Choose the issue type you want to use in the menu at left.

1. Choose to view **Fields** in the top right (if not already selected). It should then show a list of fields enabled for the screen.

1. Scroll to the bottom where there should be a textbox where you can enter additional fields. Enter **AWS**, then choose the AWS field you want to use.

1.  Choose **Add** to apply. 

1. Repeat the previous step for the other field if you want to use it.

1. Repeat these steps for each issue type you want to use these fields. Some issue types might share screens so the field might already be added for some.

It is important also to make a note of the field ID for the field or fields you are using. Choose ** Admin -> Issues -> Custom fields** and select **Configure** on each field.

Inspect the opened URL to see the numeric field ID. It should be a 5-digit number.

Alternatively, for any issue in a project where you've added the field (following the instructions above), the REST API at `/rest/api/2/issue/PRJ-1/editmeta` (for example, `http://localhost:2990/jira/rest/api/2/issue/PRJ-1/editmeta`) will include information on the fields.

The REST API should contain an entry `customfield_#####: { ..., name: "AWS Config Linked Resources", ... }`, where `#####` is the numeric field ID.

Once these fields are enabled for projects and issue types, use the Jira REST API to create or update issues with values for these fields. You can use tools such as CloudWatch, AppDynamics, Jenkins, or a Systems Manager Automation Document (provided in the next section).

The REST API endpoint to update an issue is `/rest/api/2/issue/issue-key` and the general schema to pass to set a value is as follows:

```
                        { "update": { 
        "customfield_field-ID": [ {
          "set": "value" 
        } ] 
    } }
```

See the examples below, or for more information on the REST API, see [JIRA Developer Documentation : Updating an Issue through the JIRA REST APIs](https://developer.atlassian.com/server/jira/platform/updating-an-issue-via-the-jira-rest-apis-6848604/).

## Sample Use Case: Automatically Creating Issues for IT Lifecycle Management - Remediating non-compliant public S3 buckets
<a name="jsd-sample"></a>

Once you enable the fields to an issue and create the Systems Manager Automation Document, you can set up rules to automatically create Jira issues for common problem categories in AWS. You can also include suggested remediations to make it easy for Jira agents and end users to see problems and fix them.

This demo creates a Config Rule in AWS, which detects public S3 buckets and makes it possible for Jira agents or end users to disable public access directly from Jira.

You should set up prerequisites, roles for the automation and lambda to execute, and the Jira password as a secure string in Systems Manager Parameter Store.

**To store the Jira password securely in Parameter Store**

1. Open the AWS Console and go to **Systems Manager -> Parameter Store**.

1. Choose **Create parameter**.

1. Set the name as **jira\_password**.

1. Set the type as **SecureString**.

1. Set the value as the password for the Jira user to create issues.

1. To save, choose **Create parameter**.

An CloudFormation template assists setting up the role and configuration rule: ****JSMConnector-CreateRemediationIssue-MakePublicBucketsPrivateConfigRule.cfn.yaml****

Install the template, setting the following parameters:
+ **JiraURL**: the base URL to your Jira, such that appending* /rest/..*. after it accesses the REST API
+ **JiraUsername**: the username to log in to Jira (with the password specified in *jira\_password*)
+ **SSMParameterName**: *jira\_password* (the parameter containing the Jira password)
+ **ProjectKey**: the key of the project (the token before the *-n an issue*), such as *PRJ*.
+ **IssueTypeName**: must exactly match the name of the issue type on the project in Jira
+ **JiraAwsAccountName**: the name of the AWS Account as configured in the Connector in Jira
+ **JiraAwsAccountRegion**: the Region of this violating resource, e.g. *us-east-1*
+ **JiraAwsResourceFieldId**: the field ID of the AWS Config Linked Resources field in Jira, such as *customfield\_10011*.
+ **JiraRemediationsFieldId**: the field ID of the **AWS Systems Manager Automation Suggested Remediation** field in Jira, such as *customfield\_10010*.

The Config Rule runs automatically within the period specified. To see it in action immediately:

1. Create a public Amazon S3 bucket.

1. Open the Config Rule in AWS Config and choose **Re-evaluate**. The rule and the automation can take a short while to run, but within a few minutes you should see a new issue in Jira with AWS Config information for the bucket, which is in violation and suggests the **DisableS3BucketPublicReadWrite** automation document as a remediation.