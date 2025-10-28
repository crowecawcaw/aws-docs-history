# Pricing for EBS direct APIs

## Pricing for APIs

The price that you pay to use the EBS direct APIs depends on the requests you make. For more
information, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/").

- **ListChangedBlocks** and ListSnapshotBlocks APIs are charged
  per request. For example, if you make 100,000 ListSnapshotBlocks API requests in a Region that
  charges $0.0006 per 1,000 requests, you will be charged $0.06 ($0.0006 per 1,000 requests x
  100).
- **GetSnapshotBlock** is charged per block returned. For
  example, if you make 100,000 GetSnapshotBlock API requests in a Region that charges $0.003
  per 1,000 blocks returned, you will be charged $0.30 ($0.003 per 1,000 blocks returned x 100).
- **PutSnapshotBlock** is charged per block written. For
  example, if you make 100,000 PutSnapshotBlock API requests in a Region that charges $0.006
  per 1,000 blocks written, you will be charged $0.60 ($0.006 per 1,000 blocks written x 100).

## Networking costs

###### Data transfer costs

Data transferred directly between EBS direct APIs and Amazon EC2 instances in the same AWS Region is free
when using [non-FIPS endpoints](../../../general/latest/gr/ebs-service.md#ebs_direct_apis "../../../general/latest/gr/ebs-service.md#ebs_direct_apis"). For more information, see [AWS service endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md"). If other AWS services are in
the path of your data transfer, you will be charged their associated data processing costs. These
services include, but are not limited to, PrivateLink endpoints, NAT Gateway and Transit Gateway.

###### VPC interface endpoints

If you are using EBS direct APIs from Amazon EC2 instances or AWS Lambda functions in private
subnets, you can use VPC interface endpoints, instead of using NAT gateways, to reduce
network data transfer costs. For more information, see [Create a private connection between a VPC and EBS direct APIs](ebs-apis-vpc-endpoints.md "ebs-apis-vpc-endpoints.md").
