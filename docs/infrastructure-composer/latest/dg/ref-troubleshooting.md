

# AWS Infrastructure Composer troubleshooting
<a name="ref-troubleshooting"></a>

**Note**  
End of support notice: On December 7, 2026, the standalone AWS Infrastructure Composer console will no longer be available. We have replaced Infrastructure Composer with an improved visual IaC editor on the AWS console pages where it was previously embedded. The full Infrastructure Composer experience remains available via the AWS Toolkit for Visual Studio Code. For more information, see [AWS Infrastructure Composer end of support](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/infrastructure-composer-end-of-support.html).

The topics in this section provide guidance on troubleshooting error messages when using AWS Infrastructure Composer.

**Topics**
+ [Error messages](#ref-troubleshooting-error)

## Error messages
<a name="ref-troubleshooting-error"></a>

### "Can't open this folder"
<a name="ref-troubleshooting-error-open"></a>

*Example error*:

!["Can't open this folder" error message displayed in Infrastructure Composer](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_ref_ts_01.png)


**Possible cause: Infrastructure Composer is unable to access a sensitive directory using **local sync** mode.**  
To learn more about this error, see [Data Infrastructure Composer gains access to](reference-fsa.md#reference-fsa-access).  
Try connecting to a different local directory or using Infrastructure Composer with **local sync** deactivated.

### "Incompatible template"
<a name="ref-troubleshooting-error-incompatible"></a>

*Example error*: When loading a new project in Infrastructure Composer, you see the following:

**Possible cause: Your project contains an externally referenced file that isn’t supported in Infrastructure Composer.**  
To learn about supported external files in Infrastructure Composer, see [Reference external files](using-composer-external-files.md).

**Possible cause: Your project links to an external file in a different local directory.**  
Move your externally referenced file to a subdirectory of the directory that you select to use with Infrastructure Composer **local sync** mode.

### "The provided folder contains an existing template.yaml"
<a name="ref-troubleshooting-error-existing"></a>

When attempting to activate **local sync**, you see the following error:

!["The provided folder contains an existing template.yaml" error message in Infrastructure Composer](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_ls_01.png)


**Possible cause: Your selected folder already contains a template.yaml file.**  
Select another directory that doesn’t contain an application template, or create a new directory.

### "Your browser doesn't have permissions to save your project in that folder..."
<a name="ref-troubleshooting-error-permissions"></a>

**Possible cause: Infrastructure Composer is unable to access a sensitive directory using local sync mode.**  
To learn more about this error, see [Data Infrastructure Composer gains access to](reference-fsa.md#reference-fsa-access).  
Try connecting to a different local directory or use Infrastructure Composer with **local sync** deactivated.