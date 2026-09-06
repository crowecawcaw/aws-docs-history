

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Adding manual evidence in AWS Audit Manager
<a name="upload-evidence"></a>



Audit Manager can automatically collect evidence for many controls. However, some controls might require evidence that can't be collected automatically. In such cases, you can manually add your own evidence.

Consider the following examples:
+ Some controls relate to the provision of physical records (such as signatures), or events that aren’t generated in the cloud (such as observations and interviews). In these cases, you can manually add files as evidence. For instance, if a control requires information about your organizational structure, you can upload a copy of your company’s org chart as manual evidence.
+ Some controls represent a vendor risk assessment question. A risk assessment question might require documentation as evidence (such as an org chart). Or, it might only need a simple text response (such as a list of job titles). For the latter, you can respond to the question and save your response as manual evidence.

You can also use the manual upload feature to manage evidence from multiple environments. If your company uses a hybrid cloud model or multicloud model, you can upload evidence from your on-premises environment, an environment hosted in the cloud, or your SaaS applications. This enables you to organize your evidence (regardless of where it came from) by storing it within the structure of an Audit Manager assessment, where each piece of evidence is mapped to a specific control.

## Key points
<a name="upload-evidence-key-points"></a>

When it comes to adding manual evidence to your assessments in Audit Manager, you have three methods to choose from. 

1. **Importing a file from Amazon S3 - **This method is ideal when you have evidence files stored in an S3 bucket, such as documentation, reports, or other artifacts that can't be automatically collected by Audit Manager. By importing these files directly from S3, you can seamlessly integrate this manual evidence with the automatically collected evidence.

1. **Uploading a file from your browser** - If you have evidence files locally stored on your computer or network, you can manually upload them to Audit Manager using this method. This approach is particularly useful when you need to include physical records, such as scanned documents or images, that aren't available in digital format within your AWS environment.

1. **Adding free-form text as evidence** - In some cases, the evidence you need to provide is not in the form of a file but rather a text response or explanation. This method allows you to enter free-form text directly into Audit Manager. This can be especially helpful when responding to vendor risk assessment questions.

## Additional resources
<a name="upload-evidence-additional-resources"></a>
+ For instructions on how to add manual evidence to an assessment control, see the following resources. Keep in mind you can only use one method at a time.
  + [Importing manual evidence files from Amazon S3](import-from-s3.md)
  + [Uploading manual evidence files from your browser](upload-from-computer.md)
  + [Entering free-form text responses as manual evidence](enter-text-response.md)
+ To learn which file formats you can use, see [Supported file formats for manual evidence](supported-manual-evidence-files.md).
+ To learn more about the different types of evidence in Audit Manager, see [](concepts.md#evidence) in the *Concepts and terminology* section of this guide. 
+ For troubleshooting assistance, see [I can’t upload manual evidence to a control](control-issues.md#cannot-upload-manual-evidence).