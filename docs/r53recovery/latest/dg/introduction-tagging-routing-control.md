#

Tagging for routing control in Amazon Application Recovery Controller (ARC)

Tags are words or phrases (meta data) that you use to identify and organize your AWS resources. You can add multiple
tags to each resource, and each tag includes a key and a value that you define. For example, the key might be environment
and the value might be production. You can search and filter your resources based on the tags you add.

You can tag the following resources in routing control in ARC:

- Clusters
- Control panels
- Safety rules
  Tagging in ARC is available only through the API, for example, by using the AWS CLI.

The following are examples of tagging in routing control by using the AWS CLI.

`aws route53-recovery-control-config --region us-west-2 create-cluster --cluster-name example1-cluster --tags Region=PDX,Stage=Prod`

`aws route53-recovery-control-config --region us-west-2 create-control-panel --control-panel-name example1-control-panel 
 --cluster-arn arn:aws:route53-recovery-control::111122223333:cluster/5678abcd-abcd-5678-abcd-5678abcdefgh --tags Region=PDX,Stage=Prod`

For more information, see
[TagResource](../../../recovery-cluster/latest/api/tags-resourcearn.md "../../../recovery-cluster/latest/api/tags-resourcearn.md") in the
_Recovery Control Configuration API Reference Guide_ for Amazon Application Recovery Controller (ARC).
