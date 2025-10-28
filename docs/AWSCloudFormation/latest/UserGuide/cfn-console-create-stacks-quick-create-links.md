# Use quick-create links to

create CloudFormation stacks

Quick-create links provide a streamlined method to launch CloudFormation stacks directly from
URLs in the CloudFormation console. By specifying the template URL, stack name, and template
parameters as URL query parameters, you can prepopulate a single **Create
stack** page and expedite stack creation. This simplifies the process of
creating stacks by reducing both the number of wizard pages and the amount of required user
input. It also optimizes template reuse, as you can create multiple URLs that specify
different values for the same template.

## URL format

The quick-create link follows this URL format:

```
https://`region-code`.console.aws.amazon.com/cloudformation/home?region=`region-code`#/stacks/create/review
   ?templateURL=`TemplateURL`
   &stackName=`StackName`
   &param_`parameterName`=`parameterValue`
```

CloudFormation supports the following URL query parameters:

Template URL

Required. The `templateURL` parameter specifies the URL of the
stack template located in an Amazon S3 bucket. To avoid access issues with a
presigned S3 URL, make sure that you URL-encode the URL.

Supported S3 URL formats:

- `https://s3.`region-code`.amazonaws.com/`bucket-name`/`template-name``
- `https://`bucket-name`.s3.`region-code`.amazonaws.com/`template-name``
- `https://s3-`region-code`.amazonaws.com/`bucket-name`/`template-name``
  (legacy format)

Stack name

Optional. Use the `stackName` parameter to specify the name of
the CloudFormation stack to be created. A stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an
alphabetic character and can't be longer than 128 characters.

Template parameters

Optional. For parameters in the stack template that aren't a
`NoEcho` parameter type, use the format
`param_`parameterName``in the
 URL query string. The URL parameter must include the`param\_` prefix, and the parameter name segment must exactly match the parameter name
 in the template. For example:`param_DBName`.

CloudFormation ignores parameters that don't exist in the template, and any
parameters defined with their `NoEcho` property set to
`true` types (typically, user names and passwords). URL
parameters override default values that are specified in the template. You
can include as many parameters as needed.

###### Important

Rather than embedding sensitive information directly in your CloudFormation templates, we recommend you use dynamic parameters in the stack template to
reference sensitive information that is stored and managed outside of CloudFormation, such as in the AWS Systems Manager Parameter Store or AWS Secrets Manager.

For more information, see the [Do not embed credentials in your templates](security-best-practices.md#creds "security-best-practices.md#creds") best practice.

All query parameter names are case sensitive. Users can overwrite these values in the
console before creating the stack.

## Example

The following example is based on the [WordPress basic single instance](https://s3.us-east-2.amazonaws.com/cloudformation-templates-us-east-2/WordPress_Single_Instance.template "https://s3.us-east-2.amazonaws.com/cloudformation-templates-us-east-2/WordPress_Single_Instance.template") sample template. The query string includes
the required `templateURL` parameter and the `stackName`,
`DBName`, `InstanceType`, and `KeyName`
parameters.

The following URL has line breaks added for clarity.

```
https://us-east-2.console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review
   ?templateURL=https://s3.us-east-2.amazonaws.com/cloudformation-templates-us-east-2/WordPress_Single_Instance.template
   &stackName=MyWPBlog
   &param_DBName=mywpblog
   &param_InstanceType=t2.medium
```

The following URL includes the same parameters as the previous example, but the line
breaks are removed. This is the actual URL format.

```
https://us-east-2.console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://s3.us-east-2.amazonaws.com/cloudformation-templates-us-east-2/WordPress_Single_Instance.template&stackName=MyWPBlog&param_DBName=mywpblog&param_InstanceType=t2.medium
```

## Creating a stack using a quick-create

link

When you open a quick-create link, you are directed to the CloudFormation console. The
console opens directly to the **Quick create stack** page, with the
supplied values automatically used for the parameters.

###### To create a stack using a quick-create link (console)

1.  On the **Quick create stack** page, for
    **Template**, **Template URL**, confirm
    the template URL is correct.
2.  Expand the **View template** section to verify the
    template.
3.  For **Stack name**, verify the prepopulated stack
    name.
4.  Review the **Parameters** section. Verify that the
    prepopulated parameter values are correct. Fill in any required parameters that
    weren't specified in the URL. Modify any prepopulated values if needed.
5.  Next, you can configure the following settings:

        * **Tags** — Organize resources with key-value
         pairs.
        * **Permissions** — Choose the IAM service
         role for stack operations.
        * **Stack failure options** — Choose to roll
         back (default) or preserve resources.
        * **Stack policy** — Control resource update
         permissions.
        * **Rollback configuration** — Configure CloudWatch
         alarm-based rollback.
        * **Notification options** — Set up Amazon SNS
         notifications for stack events.
        * **Stack creation options** — Define maximum
         stack creation time and enable termination protection to prevent
         accidental deletions.

    For more information, see [Configure stack options](cfn-console-create-stack.md#configure-stack-options "cfn-console-create-stack.md#configure-stack-options").

6.  For **Capabilities**, complete any required acknowledgements.
    For example, if your template contains IAM resources, select **I
    acknowledge that this template may create IAM resources** to
    specify that you want to use IAM resources in the template. For more
    information, see [Acknowledging IAM resources in CloudFormation
    templates](control-access-with-iam.md#using-iam-capabilities "control-access-with-iam.md#using-iam-capabilities").
7.  (Optional) You can create a change set to preview the configuration of the
    stack before creating it. Choose **Create change set** and
    follow the directions. For more information, see [Preview the configuration of your
    stack](cfn-console-create-stack.md#cfn-console-create-stacks-changesets "cfn-console-create-stack.md#cfn-console-create-stacks-changesets").
8.  When you're ready, choose **Create stack** to launch the
    stack and then monitor the stack creation progress in the
    **Events** tab. For more information, see [Monitor stack progress](monitor-stack-progress.md "monitor-stack-progress.md").
