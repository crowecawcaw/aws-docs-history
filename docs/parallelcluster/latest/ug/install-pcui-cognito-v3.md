# Amazon Cognito user pool options

The following sections refer to CloudFormation quick-create links or quick-create URLs. A quick-create URL takes you to a
**Create Stack Wizard** where you provide quick-create stack template inputs and deploy the
stack. For more information about CloudFormation quick-create stacks, see [Creating quick-create links for stacks](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stacks-quick-create-links.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stacks-quick-create-links.md") in
the _AWS CloudFormation User Guide_.

To maintain an Amazon Cognito user pool that you can use with multiple AWS ParallelCluster UI (PCUI) instances, consider the following options:

- Use an existing PCUI instance that links to an Amazon Cognito user pool created from a nested CloudFormation stack. This is what is created when you
  deploy the PCUI by using the quick-create link and keep all Amazon Cognito parameters blank.
- First, deploy a standalone Amazon Cognito user pool. Then, deploy a new PCUI instance that's linked to the
  standalone Amazon Cognito user pool that you just deployed. This way, you separate the Amazon Cognito deployment from the PCUI deployment.
  Note that non-nested PCUI CloudFormation stacks are easier to update.
