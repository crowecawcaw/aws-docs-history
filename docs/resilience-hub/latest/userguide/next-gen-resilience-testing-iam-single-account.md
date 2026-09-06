

# Single-account execution role
<a name="next-gen-resilience-testing-iam-single-account"></a>

For a single-account test, create one execution role with a trust policy that allows AWS FIS to assume it and a permissions policy for the test template that you use.

The execution role must trust the AWS FIS service. The trust policy is the same for every test template. The `aws:SourceAccount` and `aws:SourceArn` conditions protect against the [confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html), so that only experiments owned by your account can assume the role.

```
{
  "Version": "2012-10-17"		 	 	 ,
  "Statement": [
    {
      "Sid": "FISTrustPolicy",
      "Effect": "Allow",
      "Principal": {
        "Service": "fis.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{account-id}}"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:fis:*:{{account-id}}:experiment/*"
        }
      }
    }
  ]
}
```

Attach the permissions policy for the test template that your test uses.

**Topics**
+ [Availability Zone: recovery](next-gen-resilience-testing-iam-sa-az-recovery.md)
+ [Dependency validation](next-gen-resilience-testing-iam-sa-dependency-validation.md)
+ [Multi-Region: isolation](next-gen-resilience-testing-iam-sa-multi-region-isolation.md)
+ [Multi-Region: recovery](next-gen-resilience-testing-iam-sa-multi-region-recovery.md)
+ [Create the role and attach it to your test](next-gen-resilience-testing-iam-sa-create.md)