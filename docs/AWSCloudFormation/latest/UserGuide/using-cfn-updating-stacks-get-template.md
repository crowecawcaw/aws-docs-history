# Update your stack template

To modify the resources or properties in a CloudFormation stack, you must update the stack's
 template. Start with the existing template for that stack and make your changes to it. If you
 have the template stored in a source control system, use a copy of that as your starting
 point. Otherwise, you can get a copy of the template from CloudFormation.

If you only want to change the parameters or settings of the stack (like a stack's Amazon SNS
 topic), you can reuse the existing template without getting a copy.

You can update a CloudFormation stack template by using a text editor or [Infrastructure Composer](infrastructure-composer-for-cloudformation.md "infrastructure-composer-for-cloudformation.md").

###### To update an existing stack template by using Infrastructure Composer

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the **Stacks** page, choose the name of the stack to
 update.
3. Choose the **Template** tab, and then choose **View in
 Infrastructure Composer**.


CloudFormation opens the template in Infrastructure Composer.
4. Update your template using one of the following methods:




	* **Canvas** interface: Here, you can drag and drop from the
	 **Resources** pallete. Configure resources by double-clicking
	 on a card to open the **Resource properties** panel. Connect
	 resources as needed. For detailed instructions on using the
	 **Canvas** interface, see [How to compose
	 in AWS Infrastructure Composer](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-basics.html "https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-basics.html").
	* **Template** interface: Switch from the
	 **Canvas** to the **Template** interface.
	 Make in-line updates to the template code. Toggle between JSON to YAML formats as
	 needed.
5. Choose **Validate** to check for any syntax errors in the
 template.
6. When you are ready to export changes to CloudFormation, choose **Update
 template**.
###### To update an existing stack template by using the AWS CLI

1. To get the template for the stack you want to update, use the [get-template](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/get-template.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/get-template.html") CLI
 command.
2. Copy the template, paste it into a text file, modify it, and save it. Copy
 *only* the template. The command encloses the template in
 quotation marks, but don't copy the quotation marks surrounding the template. The
 template itself starts with an open brace and ends with the final close brace. Specify
 changes to the stack's resources in this file.
Keep in mind the following points as you make changes to your template:


* You can't add, modify, or delete a parameter that's used by a resource that doesn't
 support updates.
* For most resources, changing the logical name of a resource is equivalent to deleting
 that resource and replacing it with a new one. Any other resources that depend on the
 renamed resource also need to be updated and might cause them to be replaced. Other
 resources require you to update a property (not just the logical name) in order to
 initiate an update.
* Some resources may have constraints about what values you can set for certain
 properties. For example, changes to the `AllocatedStorage` property for an
 RDS database instance must be greater than the current value. If your update violates
 these rules, that part will fail.
* Updating one resource can also affect others that reference it. If you use functions
 like [The Ref function](resources-section-structure.md#resource-properties-ref "resources-section-structure.md#resource-properties-ref")
 or [The Fn::GetAtt
 function](resources-section-structure.md#resource-properties-getatt "resources-section-structure.md#resource-properties-getatt") to set a property based on another resource, CloudFormation will update the referencing
 resource too when the referenced one changes.
* For information about the effects of updating particular resource properties, see the
 [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html"). For each property, the effects of an update will be one of
 the following:




	+ *Update requires*: [No interruption](using-cfn-updating-stacks-update-behaviors.md#update-no-interrupt "using-cfn-updating-stacks-update-behaviors.md#update-no-interrupt")
	+ *Update requires*: [Some interruptions](using-cfn-updating-stacks-update-behaviors.md#update-some-interrupt "using-cfn-updating-stacks-update-behaviors.md#update-some-interrupt")
	+ *Update requires*: [Replacement](using-cfn-updating-stacks-update-behaviors.md#update-replacement "using-cfn-updating-stacks-update-behaviors.md#update-replacement")
* You can verify the JSON or YAML syntax of your template by using the [validate-template](service_code_examples.md#validate-template-sdk "service_code_examples.md#validate-template-sdk") CLI command
 or by specifying your template on the console. The console performs validation
 automatically. However, these methods only verify the syntax of your template and don't
 validate the property values that you specified for a resource are valid for that
 resource. For more complex validations or to check for best practices, you might also
 use additional tools like [CloudFormation Linter (cfn-lint)](https://github.com/aws-cloudformation/cfn-lint "https://github.com/aws-cloudformation/cfn-lint") and [CloudFormation Rain (rain
 fmt)](https://github.com/aws-cloudformation/rain "https://github.com/aws-cloudformation/rain").
###### Note

Sometimes CloudFormation won't allow certain changes you try to make, and it will tell you
 the change isn't permitted. This message might occur asynchronously, however, because
 resources are created and updated by CloudFormation in a non-deterministic order by
 default.
