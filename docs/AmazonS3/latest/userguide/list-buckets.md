# Listing Amazon S3 general purpose buckets

To return a list of general purpose buckets that you own, you can use [ListBuckets](../API/API_ListBuckets.md "../API/API_ListBuckets.md").
You can list your buckets by using the Amazon S3 console, the AWS Command Line Interface, or the AWS SDKs. For
`ListBuckets` requests using the AWS CLI, AWS SDKs, and Amazon S3 REST API,
AWS accounts that use the default service quota for buckets (10,000 buckets), support both
paginated and unpaginated requests. Regardless of how many buckets you have in your account,
you can create page sizes between 1 and 10,000 buckets to list all of your buckets. For
paginated requests, `ListBuckets` requests return both the bucket names and the
corresponding AWS Regions for each bucket. The following AWS Command Line Interface and AWS SDK examples show
you how to use pagination in your `ListBuckets` request. Note that some AWS
SDKs assist with pagination.

###### Permissions

To list all of your general purpose buckets, you must have the `s3:ListAllMyBuckets`
permission. If you're encountering an
`HTTP Access Denied (403 Forbidden)` error, see [Troubleshoot access denied (403
Forbidden) errors in Amazon S3](troubleshoot-403-errors.md "troubleshoot-403-errors.md").

###### Important

We strongly recommend using only paginated `ListBuckets` requests. Unpaginated `ListBuckets` requests are only supported for
AWS accounts set to the default general purpose bucket quota of 10,000. If you have an approved
general purpose bucket quota above 10,000, you must send paginated `ListBuckets` requests to list your account’s buckets.
All unpaginated `ListBuckets` requests will be rejected for AWS accounts with a general purpose bucket quota
greater than 10,000.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. On the **General purpose buckets** tab, you can see a
   list of your general purpose buckets.
4. To find buckets by name, enter a bucket name in the **Find buckets by name** field.
   To use the AWS CLI to generate a listing of general purpose buckets, you can use the
   `ls` or `list-buckets` commands. The following examples
   show you how to create a paginated `list-buckets` request and an
   unpaginated `ls` request. To use these examples, replace the
   `user input placeholders`.

###### Example – List all the buckets in your account by using `ls`

(unpaginated)

The following example command lists all the general purpose buckets in your account
in a single non-paginated call. This call returns a list of all buckets in your
account (up to 10,000 results):

```
$ aws s3 ls
```

For more information and examples, see [List bucket and objects](../../../cli/latest/userguide/cli-services-s3-commands.md#using-s3-commands-listing-buckets "../../../cli/latest/userguide/cli-services-s3-commands.md#using-s3-commands-listing-buckets").

###### Example – List all the buckets in your account by using `ls`

(paginated)

The following example command makes one or more paginated calls to list all
the general purpose buckets in your account, returning 100 buckets per page:

```
$ aws s3 ls --page-size `100`
```

For more information and examples, see [List bucket and objects](../../../cli/latest/userguide/cli-services-s3-commands.md#using-s3-commands-listing-buckets "../../../cli/latest/userguide/cli-services-s3-commands.md#using-s3-commands-listing-buckets").

###### Example – List all the buckets in your account (paginated)

The following example provides a paginated `list-buckets` command
to list all the general purpose buckets in your account. The `--max-items` and
`--page-size` options limit the number of buckets listed to 100
per page.

```
$ aws s3api list-buckets /
    --max-items `100` /
    --page-size `100`
```

If the number of items output (`--max-items`) is fewer than the
total number of items returned by the underlying API calls, the output includes
a continuation token, specified by the `starting-token` argument,
that you can pass to a subsequent command to retrieve the next set of items. The
following example shows how to use the `starting-token` value
returned by the previous example. You can specify the `starting-code`
to retrieve the next 100 buckets.

```
$ aws s3api list-buckets /
    --max-items `100` /
    --page-size `100` /
    --starting-token `eyJNYXJrZXIiOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAxfQ==`
```

###### Example – List all the buckets in an AWS Region (paginated)

The following example command uses the `--bucket-region` parameter
to list up to 100 buckets in an account that are in the `us-east-2`
Region. Requests made to a Regional endpoint that is different from the value
specified in the `--bucket-region` parameter are not supported. For
example, if you want to limit the response to your buckets in
`us-east-2`, you must make your request to an endpoint in
`us-east-2`.

```
$ aws s3api list-buckets /
    --region `us-east-2` /
    --max-items `100` /
    --page-size `100` /
    --bucket-region `us-east-2`
```

###### Example – List all the buckets that begin with a specific bucket name prefix

(paginated)

The following example command lists up to 100 buckets that have a name
starting with the `amzn-s3-demo-bucket`
prefix.

```
$ aws s3api list-buckets /
    --max-items `100` /
    --page-size `100` /
    --prefix `amzn-s3-demo-bucket`
```

The following examples show you how to list your general purpose buckets by using the AWS SDKs

SDK for Python

###### Example – ListBuckets request (paginated)

```
import boto3

s3 = boto3.client('s3')
response = s3.list_buckets(MaxBuckets=`100`)
```

###### Example – ListBuckets response (paginated)

```
import boto3

s3 = boto3.client('s3')
response = s3.list_buckets(MaxBuckets=1,ContinuationToken="`eyJNYXJrZXIiOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAxfQ==EXAMPLE`--")
```

SDK for Java
For examples of how to list buckets with the AWS SDK for Java, see [List buckets](../API/s3_example_s3_ListBuckets_section.md "../API/s3_example_s3_ListBuckets_section.md") in the _Amazon S3 API Reference_.

SDK for Go

```
package main
import (
 "context"
 "fmt"
 "log"
 "github.com/aws/aws-sdk-go-v2/aws"
 "github.com/aws/aws-sdk-go-v2/config"
 "github.com/aws/aws-sdk-go-v2/service/s3"
)
func main() {
 cfg, err := config.LoadDefaultConfig(context.TODO(), config.WithRegion("`us-east-2`"))
 if err != nil {
  log.Fatal(err)
 }
 client := s3.NewFromConfig(cfg)
 maxBuckets := `1000`
 resp, err := client.ListBuckets(context.TODO(), management portals3.ListBucketsInput{MaxBuckets: aws.Int32(int32(maxBuckets))})
 if err != nil {
  log.Fatal(err)
 }
 fmt.Println("S3 Buckets:")
 for _, bucket := range resp.Buckets {
     fmt.Println("- Name:", *bucket.Name)
     fmt.Println("-BucketRegion", *bucket.BucketRegion)
 }
 fmt.Println(resp.ContinuationToken == nil)
 fmt.Println(resp.Prefix == nil)
}
```
