

# Creating an AWS AppConfig freeform configuration profile (console)
<a name="appconfig-creating-free-form-configuration-and-profile-create-console"></a>

Use the following procedure to create an AWS AppConfig freeform configuration profile and (optionally) a freeform-configuration by using the AWS Systems Manager console.

**To create a freeform configuration profile**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **Applications**, and then choose an application you created in [Creating a namespace for your application in AWS AppConfig](appconfig-creating-namespace.md).

1. Choose the **Configuration profiles and feature flags** tab, and then choose **Create configuration**.

1. In the **Configuration options** section, choose **Freeform configuration**.

1. For **Configuration profile name**, enter a name for the configuration profile.

1. (Optional) Expand **Description** and enter a description.

1. (Optional) Expand **Additional options** and complete the following, as necessary.

   1. In the **Associate extensions** section, choose an extension from the list.

   1. In the **Tags** section, choose **Add new tag**, and then specify a key and optional value. 

1. Choose **Next**.

1. On the **Specify configuration data** page, in the **Configuration definition** section, choose an option.

1. Complete the fields for the option you selected, as described in the following table.



<table>
<thead>
  <tr><th>Option selected</th><th>Details</th></tr>
</thead>
<tbody>
  <tr><td><b>AWS AppConfig hosted configuration</b></td><td>Choose either <b>Text</b>, <b>JSON</b>, or <b>YAML</b>, and enter your configuration in the field. Go to Step 12 in this procedure.</td></tr>
  <tr><td><b>Amazon S3 object</b></td><td>Enter the object URI in the <b>S3 object source</b> field and go to Step 11 in this procedure.</td></tr>
  <tr><td><b>AWS CodePipeline</b></td><td>Choose <b>Next</b> and go to Step 12 in this procedure.</td></tr>
  <tr><td><b>Secrets Manager secret</b></td><td>Choose the secret from the list go to Step 11 in this procedure.</td></tr>
  <tr><td><b>AWS Systems Manager parameter</b></td><td>Choose the parameter from the list and go to Step 11 in this procedure.</td></tr>
  <tr><td><b>AWS Systems Manager document</b></td><td> <ol><li> Choose a document from the list or choose <b>Create new document</b>.  </li><li> If you choose <b>Create new document</b>, for <b>Document name</b>, enter a name. Optionally, expand <b>Version name</b> and enter a name for the document version. </li><li> For <b>Application configuration schema</b>, either choose the JSON schema from the list or choose <b>Create schema</b>. If you choose <b>Create schema</b>, Systems Manager opens the <b>Create schema</b> page. Enter the schema details, and then choose <b>Create application configuration schema</b>. </li><li> In the <b>Content</b> section, choose either <b>YAML</b> or <b>JSON</b> and then enter the configuration data in the field. </li></ol> </td></tr>
</tbody>
</table>


1. In the **Service role** section, choose **New service role** to have AWS AppConfig create the IAM role that provides access to the configuration data. AWS AppConfig automatically populates the **Role name** field based on the name you entered earlier. Or, choose **Existing service role**. Choose the role by using the **Role ARN** list.

1. Optionally, on the **Add validators** page, choose either **JSON Schema** or **AWS Lambda**. If you choose **JSON Schema**, enter the JSON Schema in the field. If you choose **AWS Lambda**, choose the function Amazon Resource Name (ARN) and the version from the list. 
**Important**  
Configuration data stored in SSM documents must validate against an associated JSON Schema before you can add the configuration to the system. SSM parameters do not require a validation method, but we recommend that you create a validation check for new or updated SSM parameter configurations by using AWS Lambda.

1. Choose **Next**.

1. On the **Review and save** page, choose **Save and continue to deploy**.

**Important**  
If you created a configuration profile for AWS CodePipeline, then you must create a pipeline in CodePipeline that specifies AWS AppConfig as the *deploy provider*. You don't need to perform [Deploying feature flags and configuration data in AWS AppConfig](deploying-feature-flags.md). However, you must configure a client to receive application configuration updates as described in [Retrieving configuration data without AWS AppConfig Agent](about-data-plane.md). For information about creating a pipeline that specifies AWS AppConfig as the deploy provider, see [Tutorial: Create a Pipeline that Uses AWS AppConfig as a Deployment Provider](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-AppConfig.html) in the *AWS CodePipeline User Guide*. 

Proceed to [Deploying feature flags and configuration data in AWS AppConfig](deploying-feature-flags.md).