# Route53Configuration

Configures the Route53 record sets for an API.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
  DistributionDomainName: `String`
  EvaluateTargetHealth: `Boolean`
  HostedZoneId: `String`
  HostedZoneName: `String`
  IpV6: `Boolean`
  Region: `String`
  SetIdentifier: `String`
```

## Properties

`DistributionDomainName`

Configures a custom distribution of the API custom domain name.

_Type_: String

_Required_: No

_Default_: Use the API Gateway distribution.

_CloudFormation compatibility_: This property is passed directly to the
`DNSName` property of an `AWS::Route53::RecordSetGroup
 AliasTarget` resource.

_Additional notes_: The domain name of a [CloudFront
distribution](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.md").

`EvaluateTargetHealth`

When EvaluateTargetHealth is true, an alias record inherits the health of the
referenced AWS resource, such as an Elastic Load Balancing load balancer or another record in the
hosted zone.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`EvaluateTargetHealth` property of an
`AWS::Route53::RecordSetGroup AliasTarget` resource.

_Additional notes_: You can't set EvaluateTargetHealth to true
when the alias target is a CloudFront distribution.

`HostedZoneId`

The ID of the hosted zone that you want to create records in.

Specify either `HostedZoneName` or `HostedZoneId`, but not
both. If you have multiple hosted zones with the same domain name, you must specify the
hosted zone using `HostedZoneId`.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`HostedZoneId` property of an `AWS::Route53::RecordSetGroup
 RecordSet` resource.

`HostedZoneName`

The name of the hosted zone that you want to create records in. You must include a
trailing dot (for example, `www.example.com.`) as part of the
`HostedZoneName`.

Specify either `HostedZoneName` or `HostedZoneId`, but not
both. If you have multiple hosted zones with the same domain name, you must specify the
hosted zone using `HostedZoneId`.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`HostedZoneName` property of an `AWS::Route53::RecordSetGroup
 RecordSet` resource.

`IpV6`

When this property is set, AWS SAM creates a `AWS::Route53::RecordSet`
resource and sets [Type](../../../AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.md#cfn-route53-recordset-type "../../../AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.md#cfn-route53-recordset-type") to `AAAA` for the provided HostedZone.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent.

`Region`

_Latency-based resource record sets only:_ The Amazon EC2 Region where you created the resource
that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an
ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type.

When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource
record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the
associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record
set.

Note the following:

- You can only specify one `ResourceRecord` per latency resource record set.
- You can only create one latency resource record set for each Amazon EC2 Region.
- You aren't required to create latency resource record sets for all Amazon EC2 Regions. Route 53 will choose the
  region with the best latency from among the regions that you create latency resource record sets for.
- You can't create non-latency resource record sets that have the same values for the `Name` and
  `Type` elements as latency resource record sets.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `Region` property of an `AWS::Route53::RecordSetGroup` `RecordSet` data
type.

`SetIdentifier`

_Resource record sets that have a routing policy other than simple:_ An identifier that
differentiates among multiple resource record sets that have the same combination of name and type, such as
multiple weighted resource record sets named acme.example.com that have a type of A. In a group of resource
record sets that have the same name and type, the value of `SetIdentifier` must be unique for each
resource record set.

For information about routing policies, see [Choosing a routing policy](../../../Route53/latest/DeveloperGuide/routing-policy.md "../../../Route53/latest/DeveloperGuide/routing-policy.md") in the
_Amazon Route 53 Developer Guide_.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `SetIdentifier` property of an `AWS::Route53::RecordSetGroup` `RecordSet` data
type.

## Examples

### Route 53 Configuration Example

This example shows how to configure Route 53.

#### YAML

```
Domain:
  DomainName: www.example.com
  CertificateArn: arn-example
  EndpointConfiguration: EDGE
  Route53:
    HostedZoneId: Z1PA6795UKMFR9
    EvaluateTargetHealth: true
    DistributionDomainName: xyz

```
