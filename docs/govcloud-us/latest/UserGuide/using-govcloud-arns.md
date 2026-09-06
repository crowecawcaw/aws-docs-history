

# Amazon Resource Names (ARNs) in GovCloud (US) Regions
<a name="using-govcloud-arns"></a>

Amazon Resource Names (ARNs) uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS, such as in IAM policies, Amazon S3 bucket names, and API calls. In AWS GovCloud (US) Regions, ARNs have an identifier that is different from the one in other standard AWS Regions. For all other standard regions, ARNs begin with:

```
arn:aws
```

In the AWS GovCloud (US) Regions, ARNs begin with:

```
arn:aws-us-gov
```

If an ARN requires you to specify a Region:
+ For the AWS GovCloud (US-West) Region, use `us-gov-west-1`.
+ For AWS GovCloud (US-East) Region, use `us-gov-east-1`.

For additional information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference *.