# Directory bucket naming rules

When you create a directory bucket in Amazon S3, the following bucket naming rules apply. For
general purpose bucket naming rules, see [General purpose bucket naming rules](bucketnamingrules.md "bucketnamingrules.md").

A directory bucket name consists of a base name that you provide, and a suffix that

contains the ID of the AWS Zone (an Availability Zone or a Local Zone) that your bucket is located in and
`--x-s3`. The `zone-id` can be the ID of an Availability Zone or a Local Zone.

```
`base-name`--`zoneid`--x-s3
```

For example, the following directory bucket name contains the Availability Zone ID `usw2-az1`:

```
`bucket-base-name`--usw2-az1--x-s3
```

###### Note

When you create a directory bucket by using the console, a suffix is automatically
added to the base name that you provide. This suffix includes the Zone
ID of the Zone (Availability Zone or Local Zone) that you chose.

When you create a directory bucket by using an API, you must provide the full
suffix, including the Zone ID, in your request. For a list of
Zone IDs, see [Endpoints](s3-express-networking.md#s3-express-endpoints "s3-express-networking.md#s3-express-endpoints").

The following naming rules apply for directory buckets.

- Be unique within the chosen Zone (AWS Availability Zone or AWS Local Zone).
- Name must be between 3 (min) and 63 (max) characters long, including the suffix.
- Consists only of lowercase letters, numbers and hyphens (-).
- Begin and end with a letter or number.
- Must include the following suffix:
  `--`zone-id`--x-s3`.
- Bucket names must not start with the prefix `xn--`.
- Bucket names must not start with the prefix `sthree-`.
- Bucket names must not start with the prefix
  `sthree-configurator`.
- Bucket names must not start with the prefix `amzn-s3-demo-`.
- Bucket names must not end with the suffix `-s3alias`. This suffix
  is reserved for access point alias names. For more information, see [Access point aliases](access-points-naming.md#access-points-alias "access-points-naming.md#access-points-alias").
- Bucket names must not end with the suffix `--ol-s3`. This suffix is
  reserved for Object Lambda Access Point alias names. For more information, see [How to use a bucket-style alias for your S3 bucket Object Lambda Access Point](olap-use.md#ol-access-points-alias "olap-use.md#ol-access-points-alias").
- Bucket names must not end with the suffix `.mrap`. This suffix is
  reserved for Multi-Region Access Point names. For more information, see [Rules for naming Amazon S3 Multi-Region Access Points](multi-region-access-point-naming.md "multi-region-access-point-naming.md").
