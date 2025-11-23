# Set up automatic scaling for your Amazon MSK cluster

You can use the Amazon MSK console, the Amazon MSK API, or CloudFormation to implement automatic scaling
for storage. CloudFormation support is available through [Application Auto Scaling](../../../AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.md").

###### Note

You can't implement automatic scaling when you create a cluster. You must first create the
cluster, and then create and enable an auto-scaling policy for it. However, you can
create the policy while Amazon MSK service creates your cluster.

###### Topics

- [Set up automatic scaling using the Amazon MSK
  AWS Management Console](msk-autoexpand-setup-console.md "msk-autoexpand-setup-console.md")
- [Set up automatic scaling using the CLI](msk-autoexpand-setup-cli.md "msk-autoexpand-setup-cli.md")
- [Set up automatic-scaling for Amazon MSK using the API](msk-autoexpand-setup-api.md "msk-autoexpand-setup-api.md")
