AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Retrieving a list of buckets or regional buckets in Amazon S3 compatible storage on Snowball Edge on a Snowball Edge

Use the `list-regional-buckets` or `list-buckets` to list
Amazon S3 compatible storage on Snowball Edge buckets using the AWS CLI.

###### Example of retrieving a list of buckets or regional buckets with AWS CLI

s3api syntax

```
 aws s3api list-buckets --endpoint-url https://`s3api-endpoint-ip` --profile `your-profile`
```

For more information about the `list-buckets` command, see [list-buckets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-buckets.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-buckets.html") in the AWS CLI Command Reference

s3control syntax

```
aws s3control list-regional-buckets --account-id `123456789012` --endpoint-url https://`s3ctrlapi-endpoint-ip` --profile `your-profile`s
```

For more information about the `list-regional-buckets` command, see
[list-regional-buckets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-regional-buckets.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-regional-buckets.html") in the
AWS CLI Command Reference.

The following SDK for Java example gets a list of buckets on Snowball Edge
devices. For more information, see [ListBuckets](../../../AmazonS3/latest/API/API_ListBuckets.md "../../../AmazonS3/latest/API/API_ListBuckets.md") in the Amazon Simple Storage Service API Reference.

```

  import com.amazonaws.services.s3.model.*;
  public void listBuckets() {
    ListBucketsRequest reqListBuckets = new ListBucketsRequest()
    .withAccountId(AccountId)
    ListBucketsResult respListBuckets = s3APIClient.RegionalBuckets(reqListBuckets);
    System.out.printf("ListBuckets Response: %s%n", respListBuckets.toString());
  }

```

The following PowerShell example gets a list of buckets on Snowball Edge
devices.

```

   Get-S3CRegionalBucketList -AccountId `012345678910` -Endpoint "https://`snowball_ip`" -Region snow

```

The following .NET example gets a list of buckets on Snowball Edge
devices.

```

using Amazon.S3Control;
using Amazon.S3Control.Model;

namespace SnowTest;

internal class Program
{
    static async Task Main(string[] args)
    {
        var config = new AmazonS3ControlConfig
        {
            ServiceURL = "https://`snowball_ip`",
            AuthenticationRegion = "snow" // Note that this is not RegionEndpoint
        };

        var client = new AmazonS3ControlClient(config);

        var response = await client.ListRegionalBucketsAsync(new ListRegionalBucketsRequest()
        {
            AccountId = "012345678910"
        });
    }
}

```
