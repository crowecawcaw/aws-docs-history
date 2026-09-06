

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Document conventions
<a name="docconventions"></a>

The following are common typographical conventions for the *AWS Systems Manager User Guide*. 

**Differentiated examples for local operating systems or command line languages**  
We use tabs to present different examples of commands based on a user's local operating system type. For Linux and macOS examples, we use the backslash (`\` ) character to break long commands into multiple lines. For Windows Server examples, we use the caret (`^`) character to break commands into multiple lines.  
Example:  

```
aws ssm send-command \
    --document-name "AWS-RunShellScript" \
    --targets "Key=instanceids,Values={{i-02573cafcfEXAMPLE}}" \
    --parameters "commands=echo HelloWorld"
```

```
aws ssm send-command ^
    --document-name "AWS-RunShellScript" ^
    --targets "Key=instanceids,Values={{i-02573cafcfEXAMPLE}}" ^
    --parameters "commands=echo HelloWorld"
```

**Elements in the user interface**  
Formatting: Text in bold  
Example: Choose **File**, **Properties**.

**User input (text that a user types)**  
Formatting: Text in a monospace font  
Example: For the name, type **my-new-resource**.

**Placeholder text for a required value**  
Formatting: Text in {{italics}}  
Example:  

```
aws ec2 register-image --image-location {{amzn-s3-demo-bucket}}/image.manifest.xml
```