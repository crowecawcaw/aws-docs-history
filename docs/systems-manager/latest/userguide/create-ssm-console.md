

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Create an SSM document
<a name="create-ssm-console"></a>

After you create the content for your custom SSM document, as described in [Writing SSM document content](documents-creating-content.md#writing-ssm-doc-content), you can use the Systems Manager console to create an SSM document using your content.

**To create an SSM document**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Documents**.

1. Choose **Create command or session**.

1. Enter a descriptive name for the document.

1. (Optional) For **Target type**, specify the type of resources the document can run on.

1. In the **Document type** list, choose the type of document you want to create.

1. Delete the brackets in the **Content** field, and then paste the document content you created earlier.

1. (Optional) In the **Document tags** section, apply one or more tag key name/value pairs to the document.

   Tags are optional metadata that you assign to a resource. Tags allow you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a document to identify the type of tasks it runs, the type of operating systems it targets, and the environment it runs in. In this case, you could specify the following key name/value pairs:
   + `Key=TaskType,Value=MyConfigurationUpdate`
   + `Key=OS,Value=AMAZON_LINUX_2`
   + `Key=Environment,Value=Production`

1. Choose **Create document** to save the document.