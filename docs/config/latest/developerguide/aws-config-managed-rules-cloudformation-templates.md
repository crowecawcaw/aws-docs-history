# Creating AWS Config Managed

Rules With AWS CloudFormation Templates

###### Important

You must first create and start the AWS Config configuration recorder in order to create AWS Config managed
rules with AWS CloudFormation. For more information, see [Managing the Configuration Recorder](stop-start-recorder.md "stop-start-recorder.md").

For supported AWS Config managed rules, you can use the AWS CloudFormation templates to create the rule for
your account or update an existing AWS CloudFormation stack. A stack is a collection of related resources
that you provision and update as a single unit. When you launch a stack with a template, the
AWS Config managed rule is created for you. The templates create only the rule, and don't create
additional AWS resources.

###### Note

When AWS Config managed rules are updated, the templates are updated for the latest changes.
To save a specific version of a template for a rule, download the template, and upload
it to your S3 bucket.

For more information about working with AWS CloudFormation templates, see [Getting Started with AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/GettingStarted.md "../../../AWSCloudFormation/latest/UserGuide/GettingStarted.md") in the
_AWS CloudFormation User Guide_.

###### To launch an AWS CloudFormation stack for an AWS Config managed rule

1. Go to the [CloudFormation
   console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation") and create a new stack.
2. For **Specify template**:
   - If you downloaded the template, choose **Upload a template
     file**, and then **Choose file** to upload the
     template.
   - You can also choose **Amazon S3 URL**, and enter the
     template URL
     `http://s3.amazonaws.com/aws-configservice-us-east-1/cloudformation-templates-for-managed-rules/`THE_RULE_IDENTIFIER`.template`.

###### Note

The rule identifier should be written in ALL_CAPS_WITH_UNDERSCORES. For
example, CLOUDWATCH_LOG_GROUP_ENCRYPTED instead of
cloudwatch-log-group-encrypted.

For some rules, the rule identifier is different from the rule name. Make sure
to use the rule identifier. For example, the rule identifier for restricted-ssh
is INCOMING_SSH_DISABLED. 3. Choose **Next**. 4. For **Specify stack details**, type a stack name and enter
parameter values for the AWS Config rule. For example, if you are using the
`DESIRED_INSTANCE_TYPE` managed rule template, you can specify the
instance type such as "m4.large". 5. Choose **Next**. 6. For **Options**, you can create tags or configure other advanced
options. These are not required. 7. Choose **Next**. 8. For **Review**, verify that the template, parameters, and other
options are correct. 9. Choose **Create**. The stack is created in a few minutes. You can
view the created rule in the [AWS Config
console](https://console.aws.amazon.com/config "https://console.aws.amazon.com/config").
You can use the templates to create a single stack for AWS Config managed rules or update an
existing stack in your account. If you delete a stack, the managed rules created from that
stack are also deleted. For more information, see [Working with Stacks](../../../AWSCloudFormation/latest/UserGuide/stacks.md "../../../AWSCloudFormation/latest/UserGuide/stacks.md") in the _AWS CloudFormation User Guide_.
