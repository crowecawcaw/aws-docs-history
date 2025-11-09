# Restricting Administrator Access to

the Amazon S3 Bucket for Home Folders and Application Settings Persistence

By default, administrators who can access the Amazon S3 buckets created by WorkSpaces Applications can
view and modify content that is part of users' home folders and persistent
application settings. To restrict administrator access to the S3 buckets that contain
user files, we recommend applying the S3 bucket access policy based on the following
template:

```
{
  "Sid": "RestrictedAccess",
  "Effect": "Deny",
  "NotPrincipal":
  {
    "AWS": [
      "arn:aws:iam::`account`:role/service-role/AmazonAppStreamServiceAccess",
      "arn:aws:sts::`account`:assumed-role/AmazonAppStreamServiceAccess/PhotonSession",
      "arn:aws:iam::`account`:user/`IAM-user-name`"
    ]
  },
    "Action": "s3:*",
    "Resource": "arn:aws:s3:::`home-folder-or-application-settings-persistence-s3-bucket`-`region`-`account`"
  }
 ]
}
```

This policy allows S3 bucket access only to the users specified and to
the WorkSpaces Applications service. For every IAM user who should have access, replicate the
following line:

```
"arn:aws:iam::`account`:user/`IAM-user-name`"
```

In the following example, the policy restricts access to the home folder S3 bucket
for anyone other than IAM users marymajor and johnstiles. It also allows access to
the WorkSpaces Applications service, in AWS Region US West (Oregon) for account ID 123456789012.

```
{
  "Sid": "RestrictedAccess",
  "Effect": "Deny",
  "NotPrincipal":
  {
    "AWS": [
      "arn:aws:iam::123456789012:role/service-role/AmazonAppStreamServiceAccess",
      "arn:aws:sts::123456789012:assumed-role/AmazonAppStreamServiceAccess/PhotonSession",
      "arn:aws:iam::123456789012:user/marymajor",
      "arn:aws:iam::123456789012:user/johnstiles"
    ]
  },
    "Action": "s3:*",
    "Resource": "arn:aws:s3:::appstream2-36fb080bb8-us-west-2-123456789012"
  }
 ]
}
```
