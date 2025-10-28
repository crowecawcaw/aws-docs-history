# DynamoDB resource-based policy considerations

When you define resource-based policies for your DynamoDB resources, the following
considerations apply:

**General considerations**

- The maximum size supported for a resource-based policy document is 20 KB. DynamoDB counts whitespaces when calculating the size of a policy against this limit.
- Subsequent updates to a policy for a given resource are blocked for 15 seconds after a
  successful update of the policy for the same resource.
- Currently, you can only attach a resource-based policy to existing streams. You can't
  attach a policy to a stream while creating it.
  **Global table considerations**

- Resource-based policies aren't supported for [Global table version 2017.11.29 (Legacy)](globaltables_HowItWorks.md "globaltables_HowItWorks.md") replicas.
- Within a resource-based policy, if the action for a DynamoDB service-linked role (SLR) to
  replicate data for a global table is denied, adding or deleting a replica will fail with
  an error.
- The [AWS::DynamoDB::GlobalTable](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.md") resource doesn’t support creating a replica and
  adding a resource-based policy to that replica in the same stack update in Regions other
  than the Region where you deploy the stack update.
  **Cross-account considerations**

- Cross-account access using resource-based policies doesn't support encrypted tables
  with AWS managed keys because you can't grant cross-account access to the AWS managed
  KMS policy.
  **AWS CloudFormation considerations**

- Resource-based policies don't support [drift
  detection](../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md"). If you update a resource-based policy outside of the AWS CloudFormation stack
  template, you'll need to update the CloudFormation stack with the changes.
- Resource-based policies don't support out of band changes. If you add, update, or
  delete a policy outside of the CloudFormation template, the change won't be overwritten if
  there are no changes to the policy within the template.

For example, say that your template contains a resource-based policy which you later
update outside of the template. If you don't make any changes to the policy in the
template, the updated policy in DynamoDB won’t be synced with the policy in the
template.

Conversely, say that your template doesn’t contain a resource-based policy, but you
add a policy outside of the template. This policy won’t be removed from DynamoDB as long as
you don’t add it to the template. When you add a policy to the template and update the
stack, the existing policy in DynamoDB will be updated to match the one defined in the
template.
