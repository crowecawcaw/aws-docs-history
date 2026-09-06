

# Amazon S3 template snippets
<a name="quickref-s3"></a>

Use these Amazon S3 sample templates to help describe your Amazon S3 buckets with CloudFormation. For more examples, see the [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html#aws-resource-s3-bucket--examples) section in the `AWS::S3::Bucket` resource.

**Topics**
+ [Creating an Amazon S3 bucket with defaults](#scenario-s3-bucket)
+ [Creating an Amazon S3 bucket for website hosting and with a `DeletionPolicy`](#scenario-s3-bucket-website)
+ [Creating a static website using a custom domain](#scenario-s3-bucket-website-customdomain)

## Creating an Amazon S3 bucket with defaults
<a name="scenario-s3-bucket"></a>

This example uses a [AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html) to create a bucket with default settings.

### JSON
<a name="quickref-s3-example-1.json"></a>

```
1. "myS3Bucket" : {
2.       "Type" : "AWS::S3::Bucket"
3.       }
```

### YAML
<a name="quickref-s3-example-1.yaml"></a>

```
1. MyS3Bucket:
2.     Type: AWS::S3::Bucket
```

## Creating an Amazon S3 bucket for website hosting and with a `DeletionPolicy`
<a name="scenario-s3-bucket-website"></a>

This example creates a bucket as a website and disables Block Public Access (public read permissions are required for buckets set up for website hosting). A public bucket policy is then added to the bucket. Because this bucket resource has a `DeletionPolicy` attribute set to `Retain`, CloudFormation will not delete this bucket when it deletes the stack. The `Output` section uses `Fn::GetAtt` to retrieve the `WebsiteURL` attribute and `DomainName` attribute of the `S3Bucket` resource.

**Note**  
The following examples assume the `BlockPublicPolicy` and `RestrictPublicBuckets` Block Public Access settings have been disabled at the account level. 

### JSON
<a name="quickref-s3-example-2.json"></a>

```
 1. {
 2.     "AWSTemplateFormatVersion": "2010-09-09",
 3.     "Resources": {
 4.         "S3Bucket": {
 5.             "Type": "AWS::S3::Bucket",
 6.             "Properties": {
 7.                 "PublicAccessBlockConfiguration": {
 8.                     "BlockPublicAcls": false,
 9.                     "BlockPublicPolicy": false,
10.                     "IgnorePublicAcls": false,
11.                     "RestrictPublicBuckets": false
12.                 },
13.                 "WebsiteConfiguration": {
14.                     "IndexDocument": "index.html",
15.                     "ErrorDocument": "error.html"
16.                 }
17.             },
18.             "DeletionPolicy": "Retain",
19.             "UpdateReplacePolicy": "Retain"
20.         },
21.         "BucketPolicy": {
22.             "Type": "AWS::S3::BucketPolicy",
23.             "Properties": {
24.                 "PolicyDocument": {
25.                     "Id": "MyPolicy",
26.                     "Version": "2012-10-17", 		 	 	 
27.                     "Statement": [
28.                         {
29.                             "Sid": "PublicReadForGetBucketObjects",
30.                             "Effect": "Allow",
31.                             "Principal": "*",
32.                             "Action": "s3:GetObject",
33.                             "Resource": {
34.                                 "Fn::Join": [
35.                                     "",
36.                                     [
37.                                         "arn:aws:s3:::",
38.                                         {
39.                                             "Ref": "S3Bucket"
40.                                         },
41.                                         "/*"
42.                                     ]
43.                                 ]
44.                             }
45.                         }
46.                     ]
47.                 },
48.                 "Bucket": {
49.                     "Ref": "S3Bucket"
50.                 }
51.             }
52.         }
53.     },
54.     "Outputs": {
55.         "WebsiteURL": {
56.             "Value": {
57.                 "Fn::GetAtt": [
58.                     "S3Bucket",
59.                     "WebsiteURL"
60.                 ]
61.             },
62.             "Description": "URL for website hosted on S3"
63.         },
64.         "S3BucketSecureURL": {
65.             "Value": {
66.                 "Fn::Join": [
67.                     "",
68.                     [
69.                         "https://",
70.                         {
71.                             "Fn::GetAtt": [
72.                                 "S3Bucket",
73.                                 "DomainName"
74.                             ]
75.                         }
76.                     ]
77.                 ]
78.             },
79.             "Description": "Name of S3 bucket to hold website content"
80.         }
81.     }
82. }
```

### YAML
<a name="quickref-s3-example-2.yaml"></a>

```
 1. AWSTemplateFormatVersion: 2010-09-09
 2. Resources:
 3.   S3Bucket:
 4.     Type: AWS::S3::Bucket
 5.     Properties:
 6.       PublicAccessBlockConfiguration:
 7.         BlockPublicAcls: false
 8.         BlockPublicPolicy: false
 9.         IgnorePublicAcls: false
10.         RestrictPublicBuckets: false
11.       WebsiteConfiguration:
12.         IndexDocument: index.html
13.         ErrorDocument: error.html
14.     DeletionPolicy: Retain
15.     UpdateReplacePolicy: Retain
16.   BucketPolicy:
17.     Type: AWS::S3::BucketPolicy
18.     Properties:
19.       PolicyDocument:
20.         Id: MyPolicy
21.         Version: 2012-10-17 		 	 	 
22.         Statement:
23.           - Sid: PublicReadForGetBucketObjects
24.             Effect: Allow
25.             Principal: '*'
26.             Action: 's3:GetObject'
27.             Resource: !Join 
28.               - ''
29.               - - 'arn:aws:s3:::'
30.                 - !Ref S3Bucket
31.                 - /*
32.       Bucket: !Ref S3Bucket
33. Outputs:
34.   WebsiteURL:
35.     Value: !GetAtt 
36.       - S3Bucket
37.       - WebsiteURL
38.     Description: URL for website hosted on S3
39.   S3BucketSecureURL:
40.     Value: !Join 
41.       - ''
42.       - - 'https://'
43.         - !GetAtt 
44.           - S3Bucket
45.           - DomainName
46.     Description: Name of S3 bucket to hold website content
```

## Creating a static website using a custom domain
<a name="scenario-s3-bucket-website-customdomain"></a>

You can use Route 53 with a registered domain. The following sample assumes that you have already created a hosted zone in Route 53 for your domain. The example creates two buckets for website hosting. The root bucket hosts the content, and the other bucket redirects `www.{{domainname}}.com` requests to the root bucket. The record sets map your domain name to Amazon S3 endpoints. 

You will also need to add a bucket policy, as shown in the examples above.

For more information about using a custom domain, see [Tutorial: Configuring a static website using a custom domain registered with Route 53](https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-custom-domain-walkthrough.html) in the *Amazon Simple Storage Service User Guide*.

**Note**  
The following examples assume the `BlockPublicPolicy` and `RestrictPublicBuckets` Block Public Access settings have been disabled at the account level. 

### JSON
<a name="quickref-s3-example-3.json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Mappings" : {
        "RegionMap" : {
            "us-east-1" : { "S3hostedzoneID" : "Z3AQBSTGFYJSTF", "websiteendpoint" : "s3-website-us-east-1.amazonaws.com" },
            "us-west-1" : { "S3hostedzoneID" : "Z2F56UZL2M1ACD", "websiteendpoint" : "s3-website-us-west-1.amazonaws.com" },
            "us-west-2" : { "S3hostedzoneID" : "Z3BJ6K6RIION7M", "websiteendpoint" : "s3-website-us-west-2.amazonaws.com" },            
            "eu-west-1" : { "S3hostedzoneID" : "Z1BKCTXD74EZPE", "websiteendpoint" : "s3-website-eu-west-1.amazonaws.com" },
            "ap-southeast-1" : { "S3hostedzoneID" : "Z3O0J2DXBE1FTB", "websiteendpoint" : "s3-website-ap-southeast-1.amazonaws.com" },
            "ap-southeast-2" : { "S3hostedzoneID" : "Z1WCIGYICN2BYD", "websiteendpoint" : "s3-website-ap-southeast-2.amazonaws.com" },
            "ap-northeast-1" : { "S3hostedzoneID" : "Z2M4EHUR26P7ZW", "websiteendpoint" : "s3-website-ap-northeast-1.amazonaws.com" },
            "sa-east-1" : { "S3hostedzoneID" : "Z31GFT0UA1I2HV", "websiteendpoint" : "s3-website-sa-east-1.amazonaws.com" }
        }
    },
    "Parameters": {
        "RootDomainName": {
            "Description": "Domain name for your website (example.com)",
            "Type": "String"
        }
    },
    "Resources": {
        "RootBucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "BucketName" : {"Ref":"RootDomainName"},
                "PublicAccessBlockConfiguration": {
                    "BlockPublicAcls": false,
                    "BlockPublicPolicy": false,
                    "IgnorePublicAcls": false,
                    "RestrictPublicBuckets": false
                },
                "WebsiteConfiguration": {
                    "IndexDocument":"index.html",
                    "ErrorDocument":"404.html"
                }
            }
        },
        "WWWBucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "BucketName": {
                    "Fn::Join": ["", ["www.", {"Ref":"RootDomainName"}]]
                },
                "AccessControl": "BucketOwnerFullControl",
                "WebsiteConfiguration": {
                    "RedirectAllRequestsTo": {
                        "HostName": {"Ref": "RootBucket"}
                    }
                }
            }
        },
        "myDNS": {
            "Type": "AWS::Route53::RecordSetGroup",
            "Properties": {
                "HostedZoneName": {
                    "Fn::Join": ["", [{"Ref": "RootDomainName"}, "."]]
                },
                "Comment": "Zone apex alias.",
                "RecordSets": [
                    {
                        "Name": {"Ref": "RootDomainName"},
                        "Type": "A",
                        "AliasTarget": {
                            "HostedZoneId": {"Fn::FindInMap" : [ "RegionMap", { "Ref" : "AWS::Region" }, "S3hostedzoneID"]},
                            "DNSName": {"Fn::FindInMap" : [ "RegionMap", { "Ref" : "AWS::Region" }, "websiteendpoint"]}
                        }
                    },
                    {
                        "Name": {
                            "Fn::Join": ["", ["www.", {"Ref":"RootDomainName"}]]
                        },
                        "Type": "CNAME",
                        "TTL" : "900",
                        "ResourceRecords" : [
                            {"Fn::GetAtt":["WWWBucket", "DomainName"]}
                        ]
                    }
                ]
            }
        }
    },
    "Outputs": {
        "WebsiteURL": {
            "Value": {"Fn::GetAtt": ["RootBucket", "WebsiteURL"]},
            "Description": "URL for website hosted on S3"
        }
    }
}
```

### YAML
<a name="quickref-s3-example-3.yaml"></a>

```
Parameters:
  RootDomainName:
    Description: Domain name for your website (example.com)
    Type: String
Mappings:
  RegionMap:
    us-east-1:
      S3hostedzoneID: Z3AQBSTGFYJSTF
      websiteendpoint: s3-website-us-east-1.amazonaws.com
    us-west-1:
      S3hostedzoneID: Z2F56UZL2M1ACD
      websiteendpoint: s3-website-us-west-1.amazonaws.com
    us-west-2:
      S3hostedzoneID: Z3BJ6K6RIION7M
      websiteendpoint: s3-website-us-west-2.amazonaws.com
    eu-west-1:
      S3hostedzoneID: Z1BKCTXD74EZPE
      websiteendpoint: s3-website-eu-west-1.amazonaws.com
    ap-southeast-1:
      S3hostedzoneID: Z3O0J2DXBE1FTB
      websiteendpoint: s3-website-ap-southeast-1.amazonaws.com
    ap-southeast-2:
      S3hostedzoneID: Z1WCIGYICN2BYD
      websiteendpoint: s3-website-ap-southeast-2.amazonaws.com
    ap-northeast-1:
      S3hostedzoneID: Z2M4EHUR26P7ZW
      websiteendpoint: s3-website-ap-northeast-1.amazonaws.com
    sa-east-1:
      S3hostedzoneID: Z31GFT0UA1I2HV
      websiteendpoint: s3-website-sa-east-1.amazonaws.com
Resources:
  RootBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Ref RootDomainName
      PublicAccessBlockConfiguration:
        BlockPublicAcls: false
        BlockPublicPolicy: false
        IgnorePublicAcls: false
        RestrictPublicBuckets: false
      WebsiteConfiguration:
        IndexDocument: index.html
        ErrorDocument: 404.html
  WWWBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub
        - www.${Domain}
        - Domain: !Ref RootDomainName
      AccessControl: BucketOwnerFullControl
      WebsiteConfiguration:
        RedirectAllRequestsTo:
          HostName: !Ref RootBucket
  myDNS:
    Type: AWS::Route53::RecordSetGroup
    Properties:
      HostedZoneName: !Sub 
        - ${Domain}.
        - Domain: !Ref RootDomainName
      Comment: Zone apex alias.
      RecordSets:
        - Name: !Ref RootDomainName
          Type: A
          AliasTarget:
            HostedZoneId: !FindInMap [ RegionMap, !Ref 'AWS::Region', S3hostedzoneID]
            DNSName: !FindInMap [ RegionMap, !Ref 'AWS::Region', websiteendpoint]
        - Name: !Sub
            - www.${Domain}
            - Domain: !Ref RootDomainName
          Type: CNAME
          TTL: 900
          ResourceRecords:
            - !GetAtt WWWBucket.DomainName
Outputs:
  WebsiteURL:
    Value: !GetAtt RootBucket.WebsiteURL
    Description: URL for website hosted on S3
```