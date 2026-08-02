# Traffic Policy Document Format

When you create a traffic policy programmatically by using the Amazon Route 53 API, one of the AWS SDKs, the AWS CLI, or
AWS Tools for Windows PowerShell, you specify the definition of the traffic policy in a `Document` element in JSON format.

For more information about traffic policies, see
[Using Traffic Flow to Route DNS Traffic](traffic-flow.md "traffic-flow.md") in the
_Amazon Route 53 Developer Guide_.

###### Topics

- [Basic Syntax](#traffic-policy-document-format-basic "#traffic-policy-document-format-basic")
- [Syntax for Endpoint Definitions](#traffic-policy-document-format-endpoints "#traffic-policy-document-format-endpoints")
- [Syntax for Rule Definitions](#traffic-policy-document-format-rules "#traffic-policy-document-format-rules")
- [Examples](#traffic-policy-document-format-examples "#traffic-policy-document-format-examples")

## Basic Syntax

Here is the basic syntax for a traffic policy document:

```
{
   "AWSPolicyFormatVersion": "2015-10-01 | 2023-05-09",
   "RecordType": "`DNS type for all resource record sets created by this traffic policy`",
   "StartEndpoint | StartRule": "`ID that you assign to an endpoint or rule`",
   "Endpoints": {
      "`Endpoint ID that you assign`": {
         `Endpoint definition`
      },
      ...
   },
   "Rules": {
      "`Rule ID that you assign`": {
         `Rule definition`
      },
      ...
   }
}
```

The basic syntax for a traffic policy document contains the following objects:

**AWSPolicyFormatVersion**

The version of the traffic policy format, the latest version that supports AWS Local
Zones; `2023-05-09`.

Previous version is also supported; `2015-10-01`.

**RecordType**
The DNS type of all of the resource record sets that Amazon Route 53 will create based on this traffic policy. If you want to route traffic
to the following AWS resources, choose the applicable value:

- **CloudFront distribution** – Choose **A: IP address in
  IPv4 format** or **AAAA: IP address in IPv6
  format**.
- **ELB Application load balancer** – Choose either
  **A: IP address in IPv4 format** or
  **AAAA: IP address in IPv6 format**.
- **ELB Classic load balancer** – Choose either
  **A: IP address in IPv4 format** or
  **AAAA: IP address in IPv6 format**.
- **ELB Network load balancer** – Choose either
  **A: IP address in IPv4 format** or
  **AAAA: IP address in IPv6 format**.
- **Elastic Beanstalk environment** – Choose **A:
  IP address in IPv4 format** or **AAAA: IP
  address in IPv6 format**.
- **Amazon S3 bucket configured as a website endpoint**:
  Choose **A: IP address in IPv4 format**.

If you want to route traffic to other resources, choose the applicable type for the resource. For example, if you
want to route traffic to mail servers, specify `MX`. For the list of DNS types that Route 53 supports, see
[Supported DNS Resource Record Types](ResourceRecordTypes.md "ResourceRecordTypes.md") in the _Amazon Route 53 Developer Guide_.

**StartEndpoint | StartRule**
Whether you want the starting point for the traffic policy to be an endpoint or a rule, and the ID that
you assigned to the endpoint or rule elsewhere in the traffic policy document.

**Endpoints**
The definitions of the endpoints that you want to use in this traffic policy. For more information,
see [Syntax for Endpoint Definitions](#traffic-policy-document-format-endpoints "#traffic-policy-document-format-endpoints").

**Rules**
The definitions of the rules that you want to use in this traffic policy. For more information,
see [Syntax for Rule Definitions](#traffic-policy-document-format-rules "#traffic-policy-document-format-rules").

## Syntax for Endpoint Definitions

Here is the syntax for the endpoint definitions that you specify in a traffic policy document:

```
{
   "Type": value | cloudfront | application-load-balancer | elastic-load-balancer | network-load-balancer | elastic-beanstalk | s3-website,
   "Region": "AWS region that you created your Amazon S3 bucket in"
   "Value": "value applicable to the type of endpoint"
}
```

The syntax for an endpoint definition contains the following objects:

**Type**
Specify the applicable value:

**value**
To route traffic to a resource other than the ones in the following list, specify
`value` for `Type`.

**cloudfront**
To route traffic to a CloudFront distribution, specify `cloudfront` for `Type`.

**application-load-balancer**
To route traffic to an Application Load Balancer, specify `application-load-balancer` for `Type`.

**elastic-load-balancer**
To route traffic to an ELB Classic load balancer, specify `elastic-load-balancer`
for `Type`.

**network-load-balancer**
To route traffic to an ELB Network load balancer, specify `network-load-balancer` for `Type`.

**elastic-beanstalk**
To route traffic to an Elastic Beanstalk environment, specify `elastic-beanstalk` for `Type`.

**s3-website**
To route traffic to an Amazon S3 bucket that is configured as a website endpoint, specify `s3-website`
for `Type`.

**Region**
To route traffic to an Amazon S3 bucket that is configured as a website endpoint, specify the Region in which you
created the bucket for `Region`. For any other resource, omit `Region`.

**Value**
Specify the applicable value:

**value**
To route traffic to a resource other than the ones listed below, specify the value that corresponds with the value
that you specified for `RecordType`. For example, if you specified `A` for `RecordType`,
specify an IP address in IPv4 format for `Value`.

**cloudfront**
If you specified `cloudfront` for `Type`, specify the domain name that CloudFront
assigned to your CloudFront distribution when you created it, for example, `d111111abcdef8.cloudfront.net`.

**application-load-balancer**
If you specified `application-load-balancer` for `Type`, specify the DNS name for your load balancer.
For example, `exampleAlb-1283637735.us-east-1.elb.amazonaws.com`.

**elastic-load-balancer**
If you specified `elastic-load-balancer` for `Type`, specify the DNS name
for your load balancer. Use the value that begins with `dualstack`, for example,
`dualstack.my-load-balancer-1234567890.us-west-2.elb.amazonaws.com`.

**network-load-balancer**
If you specified `network-load-balancer` for `Type`, specify the DNS name for your load balancer.
For example, `exampleNlb-74f87b114e21682a.elb.us-east-1.amazonaws.com`.

**elastic-beanstalk**
If you specified `elastic-beanstalk` for `Type`, specify the domain name for your Elastic Beanstalk environment.
For example, `example-beanstalk-env-1.eba-ns4qrife.us-east-1.elasticbeanstalk.com`.

**s3-website**
If you specified `s3-website` for `Type`, specify the name of your Amazon S3 bucket,
for example, `example.com.s3-website-us-east-1.amazonaws.com`.

###### Important

When you create a traffic policy instance based on this traffic policy, the bucket that you specify here
must match the domain name (such as www.example.com) that you specify for `Name` in the
[CreateTrafficPolicyInstance](../APIReference/API_CreateTrafficPolicyInstance.md "../APIReference/API_CreateTrafficPolicyInstance.md")
request. If `Value` and `Name` don't match, Amazon S3 won't respond to DNS queries for the domain name.

## Syntax for Rule Definitions

There are different syntaxes for the rule definitions that you specify in a traffic policy document, depending on the
type of routing policy that you want to use: failover, geolocation, geoproximity, latency, multivalue answer, or weighted.

###### Topics

- [Failover Rules](#traffic-policy-document-format-rules-failover "#traffic-policy-document-format-rules-failover")
- [Geolocation Rules](#traffic-policy-document-format-rules-geo "#traffic-policy-document-format-rules-geo")
- [Geoproximity Rules](#traffic-policy-document-format-rules-geoproximity "#traffic-policy-document-format-rules-geoproximity")
- [Latency Rules](#traffic-policy-document-format-rules-latency "#traffic-policy-document-format-rules-latency")
- [Multivalue Answer Rules](#traffic-policy-document-format-rules-multivalue-answer "#traffic-policy-document-format-rules-multivalue-answer")
- [Weighted Rules](#traffic-policy-document-format-rules-weighted "#traffic-policy-document-format-rules-weighted")

### Failover Rules

For more information, see [Configuring DNS Failover](dns-failover-configuring.md "dns-failover-configuring.md")
in the _Amazon Route 53 Developer Guide_.

```
{
   "RuleType": "failover",
   "Primary": {
      "EndpointReference | RuleReference": "`ID that you assigned to the rule or endpoint that this rule routes traffic to`",
      "EvaluateTargetHealth": "true" | "false",
      "HealthCheck": "`optional health check ID`"
   },
   "Secondary": {
      "EndpointReference | RuleReference": "`ID that you assigned to the rule or endpoint that this rule routes traffic to`",
      "EvaluateTargetHealth": "true" | "false",
      "HealthCheck": "`optional health check ID`"
   }
}
```

When you define a failover rule, you specify the following objects:

**RuleType**
Specify `failover`.

**Primary | Secondary**
For the `Primary` object, specify settings for the rule or endpoint that you want
to route traffic to whenever the corresponding resources are available.

For the `Secondary` object, specify settings for the rule or endpoint that you want
to route traffic to whenever the primary resources are not available.

**EndpointReference | RuleReference**
Whether you want to route traffic to an endpoint or to another rule, and the ID that you assigned
to the endpoint or rule elsewhere in the traffic policy document.

**EvaluateTargetHealth**
A Boolean that indicates whether you want Amazon Route 53 to evaluate the health of the endpoint
and route traffic only to healthy endpoints. For more information, see
[EvaluateTargetHealth](../APIReference/API_AliasTarget.md#Route53-Type-AliasTarget-EvaluateTargetHealth "../APIReference/API_AliasTarget.md#Route53-Type-AliasTarget-EvaluateTargetHealth")
in the documentation about [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md").

**HealthCheck**
If you want to associate a health check with the endpoint or rule, specify the ID of the
health check. For more information, see
[HealthCheckId](../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-HealthCheckId "../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-HealthCheckId")
in the documentation about [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md").

### Geolocation Rules

When you add a geolocation rule, you configure your traffic policy to route your traffic based on the geographic location
of your users. For more information, see [Geolocation Routing](routing-policy.md#routing-policy-geo "routing-policy.md#routing-policy-geo")
in the _Amazon Route 53 Developer Guide_.

```
{
   "RuleType": "geo",
   "Locations": [
      {
         "EndpointReference | RuleReference": "`ID that you assigned to the rule or endpoint that this rule routes traffic to`",
         "IsDefault": "true" | "false",
         "Continent": "`continent name`,
         "Country": "`country name`,
         "Subdivision": "`subdivision name`,
         "EvaluateTargetHealth": "true" | "false",
         "HealthCheck": "`optional health check ID`"
      },
      ...
   ]
}
```

When you define a geolocation rule, you specify the following objects:

**RuleType**
Specify `geo`.

**Locations**
Specify one set of values (`EndpointReference` | `RuleReference`, `IsDefault`,
`Continent`, `Country`, `Subdivision`, `EvaluateTargetHealth`, and
`HealthCheck`) for each of the geographic locations that you want to route traffic to.

**EndpointReference | RuleReference**
Whether you want to route traffic to an endpoint or to another rule, and the ID that you assigned
to the endpoint or rule elsewhere in the traffic policy document.

**IsDefault**
A Boolean that indicates whether this set of values represents the default location. If you
specify `*` as the value of the `CountryCode`
element in a geographic location, the value of `IsDefault`
element for this location is set to `True` by default and you
can't specify `True` as the value for the
`IsDefault` element in other geographic locations for the
same geolocation rule. For more information about specifying
`*` as the value for the `CountryCode` element, see the
following entry for `Continent, Country, Subdivision`.

**Continent, Country, Subdivision**
Values that indicate the geographic location of users whose traffic you want to route to a rule or endpoint.
For more information, see the following element descriptions in the documentation about
[ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md"):

- `GeoLocation`
- `ContinentCode`
- `CountryCode`
- `SubdivisionCode`

For more information, see [Location](resource-record-sets-values-geo.md#rrsets-values-geo-location "resource-record-sets-values-geo.md#rrsets-values-geo-location") in the _Amazon Route 53_ Developer
Guide.

###### Important

Geolocation works by mapping IP addresses to locations. However, some IP addresses aren't mapped to geographic locations,
so even if you create geographic locations that cover all seven continents, Route 53 will receive some DNS queries from locations that it can't identify.
We recommend that you create a geographic location for which the value of `Country` is `*`.
Two groups of queries are routed to the resource that you specify in this record: queries that come from locations for which you haven't created geographic
locations and queries from IP addresses that aren't mapped to a location. If you don't create a `*` geographic location, Route 53 returns a "no answer"
response for queries from un-mapped locations.

**EvaluateTargetHealth**
A Boolean that indicates whether you want Amazon Route 53 to evaluate the health of the endpoint
and route traffic only to healthy endpoints. For more information, see
[EvaluateTargetHealth](../APIReference/API_AliasTarget.md#Route53-Type-AliasTarget-EvaluateTargetHealth "../APIReference/API_AliasTarget.md#Route53-Type-AliasTarget-EvaluateTargetHealth")
in the documentation about [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md").

**HealthCheck**
If you want to associate a health check with the endpoint or rule, specify the ID of the
health check. For more information, see
[HealthCheckId](../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-HealthCheckId "../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-HealthCheckId")
in the documentation about [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md").

### Geoproximity Rules

When you add a geoproximity rule, you configure Amazon Route 53 to route traffic to your resources based on the geographic location
of your resources. You can also optionally choose to route more traffic or less to a given endpoint or rule by specifying a bias.
You use a bias to expand or shrink the size of the geographic region from which traffic is routed to an endpoint or rule.
For more information, see [Geoproximity Routing](routing-policy.md#routing-policy-geoproximity "routing-policy.md#routing-policy-geoproximity")
in the _Amazon Route 53 Developer Guide_.

The following example is for `AWSPolicyFormatVersion 2023-05-09` only:

```
{
   "RuleType": "geoproximity",
   "GeoproximityLocations": [
      {
         "EndpointReference | RuleReference": "ID that you assigned to the endpoint or rule that this rule routes traffic to",
         "Location":{
            "Type": "Region | LocalZone",
            "LocationName": "AWS Region | AWS Local Zone"
         },
         "Bias": "optional value to expand or shrink the geographic region for this rule, -99 to 99",
         "EvaluateTargetHealth": "true | false",
         "HealthCheck": "optional health check ID"
      },
      {
         "EndpointReference | RuleReference": "ID that you assigned to the endpoint or rule that this rule routes traffic to",
         "Location":{
            "Type": "Coordinate",
            "Latitude": "location south (negative) or north (positive) of the equator, -90 to 90 degrees",
            "Longitude": "location west (negative) or east (positive) of the prime meridian, -180 to 180 degrees"
         },
         "Bias": "optional value to expand or shrink the geographic region for this rule, -99 to 99",
         "EvaluateTargetHealth": "true | false",
         "HealthCheck": "optional health check ID"
      }
   ]
}
```

The following example is for `AWSPolicyFormatVersion 2015-10-01` only:

```
{
   "RuleType": "geoproximity",
   "GeoproximityLocations": [
      {
         "EndpointReference | RuleReference": "`ID that you assigned to the endpoint or rule that this rule routes traffic to`",
         "Region": "`AWS Region`",
         "Bias": "`optional value to expand or shrink the geographic region for this rule, -99 to 99`",
         "EvaluateTargetHealth": "true | false",
         "HealthCheck": "`optional health check ID`"
      },
      {
         "EndpointReference | RuleReference": "`ID that you assigned to the endpoint or rule that this rule routes traffic to`",
         "Latitude": "`location south (negative) or north (positive) of the equator, -90 to 90 degrees`",
         "Longitude": "`location west (negative) or east (positive) of the prime meridian, -180 to 180 degrees`",
         "Bias": "`optional value to expand or shrink the geographic region for this rule, -99 to 99`",
         "EvaluateTargetHealth": "true | false",
         "HealthCheck": "`optional health check ID`"
      }
   ]
}
```

When you define a geoproximity rule, you specify the following objects:

**RuleType**
Specify `geoproximity`.

**GeoproximityLocations**
Specify one set of values for each resource that you want to route traffic to. You can specify
a **Location** field, which supports AWS Regions, Local Zones, and latitudes
and longitudes in `AWSPolicyFormatVersion 2023-05-09`. You can also
specify either an AWS Region or the latitude and longitude of a
geographic location in `AWSPolicyFormatVersion 2015-10-01`.

**EndpointReference | RuleReference**
Whether you want to route traffic to an endpoint or to another rule, and the ID that you assigned
to the endpoint or rule elsewhere in the traffic policy document.

**Location (`AWSPolicyFormatVersion 2023-05-09` only)**
The Location field supports AWS Regions, Local Zones, and latitudes and longitudes with the
following format:

For Local Zones: `"Location": { "Type": "LocalZone", "LocationName":
 "aws:route53:us-east-1-atl-1a" }`

For Regions: `"Location": {
 "Type": "Region",
 "LocationName": "aws:route53:us-east-1"
 },`

For coordinates: `"Location": {
 "Type": "Coordinate",
 "Latitude": "38.9",
 "Longitude": "-77.01"
 },`

For a list of valid region codes, see
[Region](../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-Region "../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-Region")
in the documentation about [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md").

For available Local Zones, see [AWS Local Zones locations](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/").

**Region (`AWSPolicyFormatVersion 2015-10-01` only)**
If your endpoint is an AWS resource, specify the AWS Region that you created the resource in. Use the following format:

`aws:route53:``region-code`

For a list of valid region codes, see
[Region](../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-Region "../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-Region")
in the documentation about [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md").

**Latitude and Longitude (`AWSPolicyFormatVersion 2015-10-01` only)**
If your endpoint is not an AWS resource, enter the latitude and longitude of the location of the resource.
Note the following:

- Latitude represents the location south (negative) or north (positive) of the equator.
  Valid values are -90 degrees to 90 degrees.
- Longitude represents the location west (negative) or east (positive) of the prime meridian.
  Valid values are -180 degrees to 180 degrees.
- You can get latitude and longitude from some online mapping applications. For example, in Google Maps,
  the URL for a location specifies the latitude and longitude:

https://www.google.com/maps/@**47.6086111**,**-122.3409953**,20z

- You can enter up to two decimals of precision, for example, `47.61`. If you specify a value
  with greater precision, Route 53 returns an error. For latitude and for longitude at the equator, 0.01 degree is
  approximately 0.69 miles.

**Bias**
Specify a value for `Bias` if you want to route more traffic to an endpoint from nearby endpoints
(positive values) or route less traffic to an endpoint (negative values). The range of valid values is -99 to 99;
the default value is 0.

###### Important

The value of `Bias` is relative, based on the location of other resources, rather than absolute,
based on distance. As a result, the effect of a change is difficult to predict. For example, depending on where your
resources are, changing the bias from `10` to `15` can mean the difference between adding or
subtracting a significant amount of traffic from the New York City metropolitan area. We recommend that you
change the bias in small increments and evaluate the results, and then make additional changes if appropriate.

**EvaluateTargetHealth**
A Boolean that indicates whether you want Route 53 to evaluate the health of the endpoint
and route traffic only to healthy endpoints. For more information, see
[EvaluateTargetHealth](../APIReference/API_AliasTarget.md#Route53-Type-AliasTarget-EvaluateTargetHealth "../APIReference/API_AliasTarget.md#Route53-Type-AliasTarget-EvaluateTargetHealth")
in the documentation about [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md").

**HealthCheck**
If you want to associate a health check with the endpoint or rule, specify the ID of the
health check. For more information, see
[HealthCheckId](../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-HealthCheckId "../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-HealthCheckId")
in the documentation about [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md").

### Latency Rules

When you add a latency rule, you configure your traffic policy to route your traffic based on the latency (the time delay) between
your users and the AWS regions where you've created AWS resources such as ELB load balancers and Amazon S3 buckets.
For more information, see [Latency Routing](routing-policy.md#routing-policy-latency "routing-policy.md#routing-policy-latency")
in the _Amazon Route 53 Developer Guide_.

```
{
   "RuleType": "latency",
   "Regions": [
      {
         "EndpointReference | RuleReference": "`ID that you assigned to the rule or endpoint that this rule routes traffic to`",
         "Region": "`AWS region that you want to route traffic to`",
         "EvaluateTargetHealth": "true" | "false",
         "HealthCheck": "`optional health check ID`"
      },
      ...
   ]
}
```

When you define a latency rule, you specify the following objects:

**RuleType**
Specify `latency`.

**Regions**
Specify one set of values (`EndpointReference` | `RuleReference`, `Region`,
`EvaluateTargetHealth`, and `HealthCheck`) for each of the Regions that you want to
route traffic to.

**EndpointReference | RuleReference**
Whether you want to route traffic to an endpoint or to another rule, and the ID that you assigned
to the endpoint or rule elsewhere in the traffic policy document.

**Region**
The region code for the AWS Region that you created the resource in. For a list of valid region codes, see
[Region](../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-Region "../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-Region")
in the documentation about [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md").

**EvaluateTargetHealth**
A Boolean that indicates whether you want Amazon Route 53 to evaluate the health of the endpoint
and route traffic only to healthy endpoints. For more information, see
[EvaluateTargetHealth](../APIReference/API_AliasTarget.md#Route53-Type-AliasTarget-EvaluateTargetHealth "../APIReference/API_AliasTarget.md#Route53-Type-AliasTarget-EvaluateTargetHealth")
in the documentation about [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md").

**HealthCheck**
If you want to associate a health check with the endpoint or rule, specify the ID of the
health check. For more information, see
[HealthCheckId](../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-HealthCheckId "../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-HealthCheckId")
in the documentation about [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md").

### Multivalue Answer Rules

When you add a multivalue answer rule, you configure your traffic policy to route traffic approximately randomly to your
healthy resources. Amazon Route 53 responds to DNS queries with up to eight healthy records; if you have eight or fewer healthy records,
Route 53 responds to all DNS queries with all the healthy records. For more information, see
[MultiValueAnswer](../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-MultiValueAnswer "../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-MultiValueAnswer").

```
{
   "RuleType": "multivalue",
   "Items": [
      {
         "EndpointReference": "`ID that you assigned to the endpoint that this rule routes traffic to`",
         "HealthCheck": "`optional health check ID`"
      },
      ...
   ]
}
```

When you define a multivalue answer rule, you specify the following objects:

**RuleType**
Specify `multivalue`.

**Items**
Specify one set of values (`EndpointReference` and `HealthCheck`) for each of the
multivalue answer rules or endpoints that you want to route traffic to.

**EndpointReference**
The ID that you assigned to the endpoint elsewhere in the traffic policy document.

**HealthCheck**
If you want to associate a health check with the endpoint, specify the ID of the health check.
For more information, see
[HealthCheckId](../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-HealthCheckId "../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-HealthCheckId").

### Weighted Rules

When you add a weighted rule, you configure your traffic policy to route traffic based on proportions that you specify. For example,
you might specify weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20ths of your traffic, on average, is routed to the first
endpoint or rule, 5/20ths is routed both to the second and third endpoints or rules, and 6/20ths is routed to the last endpoint or rule.
For more information, see [Weighted Routing](routing-policy.md#routing-policy-weighted "routing-policy.md#routing-policy-weighted")
in the _Amazon Route 53 Developer Guide_.

```
{
   "RuleType": "weighted",
   "Items": [
      {
         "EndpointReference | RuleReference": "`ID that you assigned to the rule or endpoint that this rule routes traffic to`",
         "Weight": "`value between 0 and 255`",
         "EvaluateTargetHealth": "true" | "false",
         "HealthCheck": "`optional health check ID`"
      },
      ...
   ]
}
```

When you define a weighted rule, you specify the following objects:

**RuleType**
Specify `weighted`.

**Items**
Specify one set of values (`EndpointReference` | `RuleReference`, `Weight`,
`EvaluateTargetHealth`, and `HealthCheck`) for each of the weighted rules or endpoints that you want to
route traffic to.

**EndpointReference | RuleReference**
Whether you want to route traffic to an endpoint or to another rule, and the ID that you assigned
to the endpoint or rule elsewhere in the traffic policy document.

**Weight**
A value between 0 and 255 that determines the proportion of traffic that is routed to the corresponding
endpoint or rule. For more information, see
[Weight](../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-Weight "../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-Weight")
in the documentation about [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md").

**EvaluateTargetHealth**
A Boolean that indicates whether you want Amazon Route 53 to evaluate the health of the endpoint
and route traffic only to healthy endpoints. For more information, see
[EvaluateTargetHealth](../APIReference/API_AliasTarget.md#Route53-Type-AliasTarget-EvaluateTargetHealth "../APIReference/API_AliasTarget.md#Route53-Type-AliasTarget-EvaluateTargetHealth")
in the documentation about [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md").

**HealthCheck**
If you want to associate a health check with the endpoint or rule, specify the ID of the
health check. For more information, see
[HealthCheckId](../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-HealthCheckId "../APIReference/API_ResourceRecordSet.md#Route53-Type-ResourceRecordSet-HealthCheckId")
in the documentation about [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md").

## Examples

The following examples show how to use failover, geolocation, geoproximity, latency, and weighted rules, and how to use multiple types of
rules in the same traffic policy.

###### Topics

- [Failover Example](#traffic-policy-document-format-examples-failover "#traffic-policy-document-format-examples-failover")
- [Geolocation Example](#traffic-policy-document-format-examples-geolocation "#traffic-policy-document-format-examples-geolocation")
- [Geoproximity Examples](#traffic-policy-document-format-examples-proximity "#traffic-policy-document-format-examples-proximity")
- [Latency Example](#traffic-policy-document-format-examples-latency "#traffic-policy-document-format-examples-latency")
- [Weighted Example](#traffic-policy-document-format-examples-weighted "#traffic-policy-document-format-examples-weighted")
- [Example with Failover, Latency, and Geolocation Rules](#traffic-policy-document-format-examples-combined "#traffic-policy-document-format-examples-combined")

### Failover Example

```
{
   "AWSPolicyFormatVersion":"2015-10-01",
   "RecordType":"A",
   "StartRule":"site_switch",
   "Endpoints":{
      "my_elb":{
         "Type":"elastic-load-balancer",
         "Value":"elb-111111.us-east-1.elb.amazonaws.com"
      },
      "site_down_banner":{
         "Type":"s3-website",
         "Region":"us-east-1",
         "Value":"www.example.com"
      }
   },
   "Rules":{
      "site_switch":{
         "RuleType":"failover",
         "Primary":{
            "EndpointReference":"my_elb"
         },
         "Secondary":{
            "EndpointReference":"site_down_banner"
         }
      }
   }
}
```

### Geolocation Example

```
{
  "AWSPolicyFormatVersion":"2015-10-01",
  "RecordType":"A",
  "StartRule":"geo_dest",
  "Endpoints":{
    "english":{
      "Type":"value",
      "Value":"192.0.2.1"
    },
    "french":{
      "Type":"value",
      "Value":"192.0.2.2"
    },
    "german":{
      "Type":"value",
      "Value":"192.0.2.3"
    }
  },
  "Rules":{
    "geo_dest":{
      "RuleType":"geo",
      "Locations":[
        {
          "EndpointReference":"english",
          "Country":"*",
          "HealthCheck":"11111111-1111-1111-1111-111111111111"
        },
        {
          "EndpointReference":"french",
          "Country":"FR",
          "IsDefault":false,
          "HealthCheck":"22222222-2222-2222-2222-222222222222"
        },
        {
          "EndpointReference":"french",
          "Country":"BE",
          "IsDefault":false,
          "HealthCheck":"22222222-2222-2222-2222-222222222222"
        },
        {
          "EndpointReference":"german",
          "Country":"DE",
          "IsDefault":false,
          "HealthCheck":"33333333-3333-3333-3333-333333333333"
        }
      ]
    }
  }
}
```

### Geoproximity Examples

```
{
  "AWSPolicyFormatVersion":"2015-10-01",
  "RecordType":"A",
  "StartRule":"geoprox-rule",
  "Endpoints":{
    "aws-us-west-1-region":{
      "Type":"elastic-load-balancer",
      "Value":"elb-123456.us-east-1.elb.amazonaws.com"
    },
    "london-data-center":{
      "Type":"value",
      "Value":"192.0.2.1"
    }
  },
  "Rules":{
    "geoprox-rule":{
      "RuleType": "geoproximity",
      "GeoproximityLocations": [
        {
          "EndpointReference": "aws-us-west-1-region",
          "Region": "aws:route53:us-west-1",
          "Bias": "10",
          "HealthCheck": "11111111-1111-1111-1111-111111111111"
        },
        {
          "EndpointReference": "london-data-center",
          "Latitude": "51.50",
          "Longitude": "-0.16",
          "Bias": "0",
          "HealthCheck": "22222222-2222-2222-2222-222222222222"
        }
      ]
    }
  }
}
```

```
{
  "AWSPolicyFormatVersion":"2023-05-09",
  "RecordType":"A",
  "StartRule":"geoprox-rule",
  "Endpoints":{
    "aws-us-west-1-region":{
      "Type":"elastic-load-balancer",
      "Value":"elb-123456.us-west-1.elb.amazonaws.com"
    },
    "aws-us-east-1-atl-local-zone":{
      "Type":"elastic-load-balancer",
      "Value":"elb-123456.us-east-1.elb.amazonaws.com"
    },
    "london-data-center":{
      "Type":"value",
      "Value":"192.0.2.1"
    }
  },
  "Rules":{
    "geoprox-rule":{
      "RuleType": "geoproximity",
      "GeoproximityLocations": [
        {
          "EndpointReference": "aws-us-west-1-region",
          "Location": {
            "Type": "Region",
            "LocationName": "aws:route53:us-west-1"
          },
          "Bias": "-10",
          "HealthCheck": "11111111-1111-1111-1111-111111111111"
        },
        {
          "EndpointReference": "aws-us-east-1-atl-local-zone",
          "Location": {
            "Type": "LocalZone",
            "LocationName": "aws:route53:us-east-1-atl-1a"
          },
          "Bias": "10",
          "HealthCheck": "22222222-2222-2222-2222-222222222222"
        },
        {
          "EndpointReference": "london-data-center",
          "Location": {
            "Type": "Coordinate",
            "Latitude": "51.50",
            "Longitude": "-0.16"
          },
          "Bias": "0",
          "HealthCheck": "33333333-3333-3333-3333-333333333333"
        }
      ]
    }
  }
}
```

### Latency Example

```
{
  "AWSPolicyFormatVersion":"2015-10-01",
  "RecordType":"A",
  "StartRule":"region_selector",
  "Endpoints":{
    "us_lb":{
      "Type":"elastic-load-balancer",
      "Value":"elb-123456.us-east-1.elb.amazonaws.com"
    },
    "europe_lb":{
      "Type":"elastic-load-balancer",
      "Value":"elb-654321.eu-west-1.elb.amazonaws.com"
    }
  },
  "Rules":{
    "region_selector":{
      "RuleType":"latency",
      "Regions":[
        {
          "Region":"us-east-1",
          "EndpointReference":"us_lb"
        },
        {
          "Region":"eu-west-1",
          "EndpointReference":"europe_lb"
        }
      ]
    }
  }
}
```

### Weighted Example

```
{
  "AWSPolicyFormatVersion":"2015-10-01",
  "RecordType":"A",
  "StartRule":"round_robin",
  "Endpoints":{
    "srv1":{
      "Type":"value",
      "Value":"192.0.2.1"
    },
    "srv2":{
      "Type":"value",
      "Value":"192.0.2.2"
    },
    "srv3":{
      "Type":"value",
      "Value":"192.0.2.3"
    }
  },
  "Rules":{
    "round_robin":{
      "RuleType":"weighted",
      "Items":[
        {
          "EndpointReference":"srv1",
          "Weight":"3",
          "HealthCheck":"11111111-1111-1111-1111-111111111111"
        },
        {
          "EndpointReference":"srv2",
          "Weight":"1",
          "HealthCheck":"22222222-2222-2222-2222-222222222222"
        },
        {
          "EndpointReference":"srv3",
          "Weight":"1",
          "HealthCheck":"33333333-3333-3333-3333-333333333333"
        }
      ]
    }
  }
}
```

### Example with Failover, Latency, and Geolocation Rules

```
{
  "AWSPolicyFormatVersion":"2015-10-01",
  "RecordType":"A",
  "StartRule":"geo_restriction",
  "Endpoints":{
    "east_coast_lb1":{
      "Type":"elastic-load-balancer",
      "Value":"elb-111111.us-east-1.elb.amazonaws.com"
    },
    "east_coast_lb2":{
      "Type":"elastic-load-balancer",
      "Value":"elb-222222.us-east-1.elb.amazonaws.com"
    },
    "west_coast_lb1":{
      "Type":"elastic-load-balancer",
      "Value":"elb-111111.us-west-1.elb.amazonaws.com"
    },
    "west_coast_lb2":{
      "Type":"elastic-load-balancer",
      "Value":"elb-222222.us-west-1.elb.amazonaws.com"
    },
    "denied_message":{
      "Type":"s3-website",
      "Region":"us-east-1",
      "Value":"video.example.com"
    }
  },
  "Rules":{
    "geo_restriction":{
      "RuleType":"geo",
      "Locations":[
        {
          "EndpointReference":"denied_message",
          "IsDefault":true
        },
        {
          "RuleReference":"region_selector",
          "Country":"US"
        }
      ]
    },
    "region_selector":{
      "RuleType":"latency",
      "Regions":[
        {
          "Region":"us-east-1",
          "RuleReference":"east_coast_region"
        },
        {
          "Region":"us-west-1",
          "RuleReference":"west_coast_region"
        }
      ]
    },
    "east_coast_region":{
      "RuleType":"failover",
      "Primary":{
        "EndpointReference":"east_coast_lb1"
      },
      "Secondary":{
        "EndpointReference":"east_coast_lb2"
      }
    },
    "west_coast_region":{
      "RuleType":"failover",
      "Primary":{
        "EndpointReference":"west_coast_lb1"
      },
      "Secondary":{
        "EndpointReference":"west_coast_lb2"
      }
    }
  }
}
```
