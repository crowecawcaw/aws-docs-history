

# Edit templates visually with template studio
<a name="template-studio"></a>

Template studio is a template editor in the CloudFormation console. It shows your template as text beside a diagram of the resources that template declares. As you edit the template, the diagram redraws to match. You can validate the template, convert it between YAML and JSON, and save it to Amazon S3 without leaving the console.

The template text is authoritative. The diagram is a visual representation of that text, not a separate editable surface. You make all changes in the template.

## Considerations
<a name="template-studio-considerations"></a>

Keep the following in mind when you work in template studio:
+ You author in the template, not on the diagram. The diagram shows the resources your template declares and how they refer to each other; you can't add or configure a resource by editing the diagram.
+ Your edits are not saved automatically. Template studio asks for confirmation before you navigate away with unsaved changes. If you leave or refresh the page, unsaved changes are discarded. Save to Amazon S3, or copy or download the template, before you leave.
+ Converting a template from YAML to JSON discards its comments, because JSON has no syntax for them. Converting back to YAML doesn't restore them.
+ CloudFormation validation in template studio isn't currently available for drafts larger than 51,200 bytes (50 KiB). The current Validate action sends the draft through the `TemplateBody` parameter, which has this limit. This isn't the overall template-size limit. You can still save the template and use it in a stack operation, subject to CloudFormation quotas. For more information, see [Validate a template](#template-studio-validate).
+ Saving writes the template to a bucket in your account, so templates you save are billed at standard Amazon S3 rates. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).
+ You can download the resources diagram only when the canvas is displayed in the **Canvas** or **Both** view.

## Permissions required for template studio
<a name="template-studio-permissions"></a>

The permissions you need depend on the template source and the actions you perform: 

`cloudformation:GetTemplate`  
Required to open an existing stack's template. Grant access to the stack whose template you want to edit.

`s3:GetObject`  
Required to read a template from Amazon S3 using your credentials. Grant access to the source template object. A presigned URL uses the authorization included in the URL.

`cloudformation:ValidateTemplate`  
Required to choose **Validate**.

`s3:PutObject`  
Required to save a template. Scope this permission to objects in the destination bucket, for example, `arn:aws:s3:::{{destination-bucket}}/*`, rather than all resources.

`s3:CreateBucket`  
Required only when the console creates a missing destination bucket. This can be the console-managed bucket or a bucket name that you specify. Reusing an existing bucket does not require this permission.

`s3:ListBucket`  
Required when saving to an existing bucket that you specify. Template studio uses `HeadBucket` to verify access, the expected bucket owner, and the bucket AWS Region before uploading.  
For the console-managed bucket, this permission is optional. Without it, the save dialog still displays the bucket name. Saving requires `s3:PutObject` and, if the bucket must be created, `s3:CreateBucket`.

## Open template studio
<a name="template-studio-open"></a>

Where you open template studio from determines what it opens with, and what happens after you save.

**To start a new template**

1. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/). 

1. On the navigation bar at the top of the screen, choose the AWS Region you intend to deploy in.

1. In the navigation pane, choose **Template studio**.

**To build a template while creating a stack**

1. On the **Create stack** page, choose **Build with template studio**.

1. Build the template, then choose **Save and continue**.

1. The stack wizard continues with the template you saved, so you don't have to upload it separately.

**To edit the template of an existing stack**

1. On the **Stacks** page, choose the name of the stack.

1. Either update the stack directly or create a change set.

1. On the **Prepare template** page, choose **Open in template studio**. The stack's current template opens.

1. Choose **Save and continue** to return to the update or change set with your edited template.

Elsewhere in the console, wherever a template is displayed, you can choose **Open in template studio** to work on it.

## Work with the template and the diagram
<a name="template-studio-editor-and-canvas"></a>

Template studio opens with the template and the diagram side by side. Use the view control to choose what is on screen:

**Template**  
The template only, at full width. Use this to read or write a template without the diagram.

**Canvas**  
The diagram only, at full width. Use this for a large template where the diagram requires the full width.

**Both**  
The template and the diagram together. Drag the divider between them to give either side more room.

The diagram groups related resources and draws a connection wherever one resource refers to another through `Ref`, `Fn::GetAtt`, `Fn::Sub`, or `DependsOn`. A resource that nothing references appears on its own, which makes an accidentally disconnected resource easy to spot.

**Note**  
For example, three functions can assume the same IAM role. The diagram shows the role inside each function, but the template declares only one role. Check the template to see how many resources exist.

## Convert between YAML and JSON
<a name="template-studio-format"></a>

The format you save in determines the file name and content type of the object that template studio writes to Amazon S3.

**To convert the template you are editing**

1. Choose the format control, which names the format you are currently in.

1. Choose the other format.

1. Converting from YAML to JSON asks you to confirm, because comments can't be carried over. Choose **Convert** to continue.

**Important**  
JSON has no syntax for comments. When you convert a YAML template that contains comments to JSON, those comments are removed, and converting back to YAML doesn't restore them. Copy anything you want to keep before you convert.

The format control is unavailable while the template can't be read, because there is nothing complete enough to convert. Fix the template first.

## Syntax problems as you type
<a name="template-studio-diagnostics"></a>

The editor checks the template's syntax while you write it and underlines what it can't read: an unclosed bracket, a misplaced indent, a duplicate key. Hover over an underline to see the problem. Where one line has several problems, they are numbered so you can tell them apart.

This is a check of the template's *syntax*, not of its contents. The editor doesn't know which resource types exist or which properties they take, so a template that is perfectly well-formed YAML can still be wrong in ways only CloudFormation can tell you about. Choose **Validate** for that.

## Validate a template
<a name="template-studio-validate"></a>

Validation checks the template's syntax with the editor and checks the template with CloudFormation before you use it in a stack operation. Both checks use the current draft, including changes you haven't saved. A successful CloudFormation check doesn't override syntax errors reported by the editor.

**Note**  
Template studio sends the draft to the [`ValidateTemplate`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ValidateTemplate.html) API using the `TemplateBody` parameter. This parameter has a 51,200-byte (50 KiB) limit.  
For a draft above this limit, template studio doesn't send the CloudFormation request. The CloudFormation check is unavailable, but this doesn't mean the template is invalid. The editor can still report syntax errors.  
The same API supports templates up to 1 MB through `TemplateURL`. Template studio doesn't upload edited drafts for URL-based validation. You can save the template to Amazon S3 and validate it through a stack operation, subject to CloudFormation quotas.

**To validate the template you are editing**

1. Choose **Validate**.

1. A template that passes both checks is reported as **Valid**.

1. If either check finds errors, review them in the validation message. Editor errors include line and column numbers. Correct the errors in the editor and validate again.

## Save a template to Amazon S3
<a name="template-studio-save"></a>

CloudFormation reads templates for stack operations from Amazon S3, so saving is what makes your template available to the rest of the console.

Use dynamic references to secrets stored in Secrets Manager or secure strings in Systems Manager Parameter Store instead of including plaintext secrets in saved templates. For more information, see [Get values stored in other services using dynamic references](dynamic-references.md).

**To save the template you are editing**

1. Choose **Save and continue**.

1. Check the destination. By default, the template goes to the Amazon S3 bucket that CloudFormation manages for uploaded templates in the current AWS Region. If that bucket doesn't exist yet, CloudFormation creates it when you save and reuses it for templates you save later.

   1. To choose your own destination instead, choose **Use a different bucket** and enter a **Bucket name**. The bucket is created if it doesn't already exist.

1. Choose **Confirm and continue**.

**Note**  
Templates stored in Amazon S3 are billed at standard Amazon S3 rates, whichever bucket holds them. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

Saving does not require a successful validation result. When validation finds errors, template studio asks you to confirm that you want to save anyway. Saving does not fix those errors; review and correct them before using the template in a stack operation.

## Copy or download a template or diagram
<a name="template-studio-copy-download"></a>

Choose **Template actions** to take the template or the diagram out of the console:

**Copy template**  
Copies the template as it appears in the editor to your clipboard.

**Download template**  
Saves the template as a file, in the format you are currently editing in.

**Download resources diagram**  
Saves the diagram as a PNG image. Because the image is a capture of the diagram, this is available only when the diagram is on screen.