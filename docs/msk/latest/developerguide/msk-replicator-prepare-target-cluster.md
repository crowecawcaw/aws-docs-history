# Prepare the Amazon MSK target cluster

Create an MSK target cluster (provisioned or serverless) with IAM access control
turned on. The target cluster doesn’t require multi-VPC private connectivity turned on.
The target cluster can be in the same AWS Region or a different Region as the source
cluster. Both the source and target clusters must be in the same AWS account. Your
target cluster must have a minimum of three brokers.
