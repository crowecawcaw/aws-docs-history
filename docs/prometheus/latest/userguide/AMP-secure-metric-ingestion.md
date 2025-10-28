# Secure the ingestion of your

metrics

Amazon Managed Service for Prometheus provides ways of helping you secure the ingestion of your metrics.

## Using AWS PrivateLink with Amazon Managed Service for Prometheus

The network traffic of ingesting the metrics into Amazon Managed Service for Prometheus can be done over a
public internet endpoint, or by a VPC endpoint through AWS PrivateLink. Using
AWS PrivateLink ensures that the network traffic from your VPCs is secured within the
AWS network without going over the public internet. To create an AWS PrivateLink VPC
endpoint for Amazon Managed Service for Prometheus, see [Using Amazon Managed Service for Prometheus with interface VPC endpoints](AMP-and-interface-VPC.md "AMP-and-interface-VPC.md").

## Authentication and authorization

AWS Identity and Access Management (IAM) is a web service that helps you
securely control access to AWS resources. You use IAM to control who is
authenticated (signed in) and authorized (has permissions) to use resources.
Amazon Managed Service for Prometheus integrates with IAM to help you keep your data secure. When you set up
Amazon Managed Service for Prometheus, you need to create some IAM roles that enable it to ingest metrics from
Prometheus servers, and that enable Grafana servers to query the metrics that are
stored in your Amazon Managed Service for Prometheus workspaces. For more information about IAM, see [What is
IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md").

Another AWS security feature that can help you set up Amazon Managed Service for Prometheus is the AWS
Signature Version 4 signing process (AWS SigV4). Signature Version 4 is the
process to add authentication information to AWS requests sent by HTTP. For
security, most requests to AWS must be signed with an access key, which consists
of an access key ID and secret access key. These two keys are commonly referred to
as your security credentials. For more information about SigV4, see [Signature
Version 4 signing process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md").
