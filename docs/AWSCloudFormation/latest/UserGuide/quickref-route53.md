# Route 53 template snippets

###### Topics

- [Amazon Route 53 resource record set using
  hosted zone name or ID](#scenario-route53-recordset-by-host "#scenario-route53-recordset-by-host")
- [Using RecordSetGroup to set up weighted
  resource record sets](#scenario-recordsetgroup-weighted "#scenario-recordsetgroup-weighted")
- [Using RecordSetGroup to set up an alias
  resource record set](#scenario-recordsetgroup-zoneapex "#scenario-recordsetgroup-zoneapex")
- [Alias resource record
  set for a CloudFront distribution](#scenario-user-friendly-url-for-cloudfront-distribution "#scenario-user-friendly-url-for-cloudfront-distribution")

## Amazon Route 53 resource record set using

hosted zone name or ID

When you create an Amazon Route 53 resource record set, you must specify the hosted zone where
you want to add it. CloudFormation provides two ways to specify a hosted zone:

- You can explicitly specify the hosted zone using the `HostedZoneId`
  property.
- You can have CloudFormation find the hosted zone using the `HostedZoneName`
  property. If you use the `HostedZoneName` property and there are multiple
  hosted zones with the same name, CloudFormation doesn't create the stack.

### Adding RecordSet using HostedZoneId

This example adds an Amazon Route 53 resource record set containing an `SPF` record
for the domain name `mysite.example.com` that uses the `HostedZoneId`
property to specify the hosted zone.

#### JSON

```
"myDNSRecord" : {
  "Type" : "AWS::Route53::RecordSet",
  "Properties" :
  {
    "HostedZoneId" : "Z3DG6IL3SJCGPX",
    "Name" : "mysite.example.com.",
    "Type" : "SPF",
    "TTL" : "900",
    "ResourceRecords" : [ "\"v=spf1 ip4:192.168.0.1/16 -all\"" ]
  }
}
```

#### YAML

```
myDNSRecord:
  Type: AWS::Route53::RecordSet
  Properties:
    HostedZoneId: Z3DG6IL3SJCGPX
    Name: mysite.example.com.
    Type: SPF
    TTL: '900'
    ResourceRecords:
    - '"v=spf1 ip4:192.168.0.1/16 -all"'
```

### Adding RecordSet using

HostedZoneName

This example adds an Amazon Route 53 resource record set for the domain name
"mysite.example.com" using the `HostedZoneName` property to specify the hosted
zone.

#### JSON

```
"myDNSRecord2" : {
            "Type" : "AWS::Route53::RecordSet",
            "Properties" : {
                "HostedZoneName" : "example.com.",
                "Name" : "mysite.example.com.",
                "Type" : "A",
                "TTL" : "900",
                "ResourceRecords" : [
                    "192.168.0.1",
                    "192.168.0.2"
                ]
            }
        }
```

#### YAML

```
myDNSRecord2:
  Type: AWS::Route53::RecordSet
  Properties:
    HostedZoneName: example.com.
    Name: mysite.example.com.
    Type: A
    TTL: '900'
    ResourceRecords:
    - 192.168.0.1
    - 192.168.0.2

```

## Using RecordSetGroup to set up weighted

resource record sets

This example uses an [AWS::Route53::RecordSetGroup](../TemplateReference/aws-resource-route53-recordsetgroup.md "../TemplateReference/aws-resource-route53-recordsetgroup.md") to set up two CNAME records for the "example.com."
hosted zone. The `RecordSets` property contains the CNAME record sets for the
"mysite.example.com" DNS name. Each record set contains an identifier
(`SetIdentifier`) and weight (`Weight`). The proportion of internet
traffic that's routed to the resources is based on the following calculations:

- `Frontend One`: `140/(140+60)` = `140/200` =
  70%
- `Frontend Two`: `60/(140+60)` = `60/200` = 30%

For more information about weighted resource record sets, see [Weighted routing](../../../Route53/latest/DeveloperGuide/routing-policy-weighted.md "../../../Route53/latest/DeveloperGuide/routing-policy-weighted.md") in
the _Amazon Route 53 Developer Guide_.

### JSON

```
        "myDNSOne" : {
            "Type" : "AWS::Route53::RecordSetGroup",
            "Properties" : {
                "HostedZoneName" : "example.com.",
                "Comment" : "Weighted RR for my frontends.",
                "RecordSets" : [
                  {
                    "Name" : "mysite.example.com.",
                    "Type" : "CNAME",
                    "TTL" : "900",
                    "SetIdentifier" : "Frontend One",
                    "Weight" : "140",
                    "ResourceRecords" : ["example-ec2.amazonaws.com"]
                  },
                  {
                    "Name" : "mysite.example.com.",
                    "Type" : "CNAME",
                    "TTL" : "900",
                    "SetIdentifier" : "Frontend Two",
                    "Weight" : "60",
                    "ResourceRecords" : ["example-ec2-larger.amazonaws.com"]
                  }
                  ]
            }
        }
```

### YAML

```
myDNSOne:
  Type: AWS::Route53::RecordSetGroup
  Properties:
    HostedZoneName: example.com.
    Comment: Weighted RR for my frontends.
    RecordSets:
    - Name: mysite.example.com.
      Type: CNAME
      TTL: '900'
      SetIdentifier: Frontend One
      Weight: '140'
      ResourceRecords:
      - example-ec2.amazonaws.com
    - Name: mysite.example.com.
      Type: CNAME
      TTL: '900'
      SetIdentifier: Frontend Two
      Weight: '60'
      ResourceRecords:
      - example-ec2-larger.amazonaws.com
```

## Using RecordSetGroup to set up an alias

resource record set

The following examples use an [AWS::Route53::RecordSetGroup](../TemplateReference/aws-resource-route53-recordsetgroup.md "../TemplateReference/aws-resource-route53-recordsetgroup.md") to set up an alias resource record set named
`example.com` that routes traffic to an ELB Version 1 (Classic) load balancer and
a Version 2 (Application or Network) load balancer. The [AliasTarget](../TemplateReference/aws-properties-route53-recordset-aliastarget.md "../TemplateReference/aws-properties-route53-recordset-aliastarget.md")
property specifies the hosted zone ID and DNS name for the `myELB`
`LoadBalancer` by using the `GetAtt` intrinsic function.
`GetAtt` retrieves different properties of `myELB` resource, depending
on whether you're routing traffic to a Version 1 or Version 2 load balancer:

- Version 1 load balancer: `CanonicalHostedZoneNameID` and
  `DNSName`
- Version 2 load balancer: `CanonicalHostedZoneID` and
  `DNSName`

For more information about alias resource record sets, see [Choosing between alias and non-alias records](../../../Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.md "../../../Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.md") in the _Route 53 Developer
Guide_.

### JSON for version 1 load balancer

```
      "myELB" : {
        "Type" : "AWS::ElasticLoadBalancing::LoadBalancer",
        "Properties" : {
            "AvailabilityZones" : [ "us-east-1a" ],
            "Listeners" : [ {
                "LoadBalancerPort" : "80",
                "InstancePort" : "80",
                "Protocol" : "HTTP"
            } ]
        }
      },
      "myDNS" : {
        "Type" : "AWS::Route53::RecordSetGroup",
        "Properties" : {
          "HostedZoneName" : "example.com.",
          "Comment" : "Zone apex alias targeted to myELB LoadBalancer.",
          "RecordSets" : [
            {
              "Name" : "example.com.",
              "Type" : "A",
              "AliasTarget" : {
                  "HostedZoneId" : { "Fn::GetAtt" : ["myELB", "CanonicalHostedZoneNameID"] },
                  "DNSName" : { "Fn::GetAtt" : ["myELB","DNSName"] }
              }
            }
          ]
        }
    }
```

### YAML for version 1 load balancer

```
myELB:
  Type: AWS::ElasticLoadBalancing::LoadBalancer
  Properties:
    AvailabilityZones:
    - "us-east-1a"
    Listeners:
    - LoadBalancerPort: '80'
      InstancePort: '80'
      Protocol: HTTP
myDNS:
  Type: AWS::Route53::RecordSetGroup
  Properties:
    HostedZoneName: example.com.
    Comment: Zone apex alias targeted to myELB LoadBalancer.
    RecordSets:
    - Name: example.com.
      Type: A
      AliasTarget:
        HostedZoneId: !GetAtt 'myELB.CanonicalHostedZoneNameID'
        DNSName: !GetAtt 'myELB.DNSName'
```

### JSON for version 2 load

balancer

```
      "myELB" : {
        "Type" : "AWS::ElasticLoadBalancing::LoadBalancer",
        "Properties" : {
            "Subnets" : [
                {"Ref": "SubnetAZ1"},
                {"Ref" : "SubnetAZ2"}
            ]
        }
      },
      "myDNS" : {
        "Type" : "AWS::Route53::RecordSetGroup",
        "Properties" : {
          "HostedZoneName" : "example.com.",
          "Comment" : "Zone apex alias targeted to myELB LoadBalancer.",
          "RecordSets" : [
            {
              "Name" : "example.com.",
              "Type" : "A",
              "AliasTarget" : {
                  "HostedZoneId" : { "Fn::GetAtt" : ["myELB", "CanonicalHostedZoneID"] },
                  "DNSName" : { "Fn::GetAtt" : ["myELB","DNSName"] }
              }
            }
          ]
        }
    }
```

### YAML for version 2 load

balancer

```
myELB:
  Type: AWS::ElasticLoadBalancingV2::LoadBalancer
  Properties:
    Subnets:
    - Ref: SubnetAZ1
    - Ref: SubnetAZ2
myDNS:
  Type: AWS::Route53::RecordSetGroup
  Properties:
    HostedZoneName: example.com.
    Comment: Zone apex alias targeted to myELB LoadBalancer.
    RecordSets:
    - Name: example.com.
      Type: A
      AliasTarget:
        HostedZoneId: !GetAtt 'myELB.CanonicalHostedZoneID'
        DNSName: !GetAtt 'myELB.DNSName'
```

## Alias resource record

set for a CloudFront distribution

The following example creates an alias A record that points a custom domain name to an
existing CloudFront distribution. `myHostedZoneID` is assumed to be either a reference to
an actual `AWS::Route53::HostedZone` resource in the same template or a parameter.
`myCloudFrontDistribution` refers to an
`AWS::CloudFront::Distribution` resource within the same template. The alias
record uses the standard CloudFront hosted zone ID (`Z2FDTNDATAQYW2`) and automatically
resolves the distribution’s domain name using `Fn::GetAtt`. This setup allows web
traffic to be routed from the custom domain to the CloudFront distribution without requiring an IP
address.

###### Note

When you create alias resource record sets, you must specify `Z2FDTNDATAQYW2`
for the `HostedZoneId` property. Alias resource record sets for CloudFront can't be
created in a private zone.

### JSON

```
{
    "myDNS": {
        "Type": "AWS::Route53::RecordSetGroup",
        "Properties": {
            "HostedZoneId": {
                "Ref": "myHostedZoneID"
            },
            "RecordSets": [
                {
                    "Name": {
                        "Ref": "myRecordSetDomainName"
                    },
                    "Type": "A",
                    "AliasTarget": {
                        "HostedZoneId": "Z2FDTNDATAQYW2",
                        "DNSName": {
                            "Fn::GetAtt": [
                                "myCloudFrontDistribution",
                                "DomainName"
                            ]
                        },
                        "EvaluateTargetHealth": false
                    }
                }
            ]
        }
    }
}
```

### YAML

```
myDNS:
  Type: AWS::Route53::RecordSetGroup
  Properties:
    HostedZoneId: !Ref myHostedZoneID
    RecordSets:
      - Name: !Ref myRecordSetDomainName
        Type: A
        AliasTarget:
          HostedZoneId: Z2FDTNDATAQYW2
          DNSName: !GetAtt
            - myCloudFrontDistribution
            - DomainName
          EvaluateTargetHealth: false
```
