# Enabling and using S3 Transfer Acceleration

You can use Amazon S3 Transfer Acceleration to transfer files quickly and securely over long distances
 between your client and an S3 general purpose bucket. You can enable Transfer Acceleration using the S3 console, the
 AWS Command Line Interface (AWS CLI), API, or the AWS SDKs.

This section provides examples of how to enable Amazon S3 Transfer Acceleration on a bucket and use
 the acceleration endpoint for the enabled bucket. 

For more information about Transfer Acceleration requirements, see [Configuring fast, secure file transfers using
 Amazon S3 Transfer Acceleration](transfer-acceleration.md "transfer-acceleration.md").

###### Note

If you want to compare accelerated and non-accelerated upload speeds, open the  [Amazon S3 Transfer Acceleration Speed Comparison tool](https://s3-accelerate-speedtest.s3-accelerate.amazonaws.com/en/accelerate-speed-comparsion.html "https://s3-accelerate-speedtest.s3-accelerate.amazonaws.com/en/accelerate-speed-comparsion.html").

The Speed Comparison tool uses multipart upload to transfer a file from your browser to
 various AWS Regions with and without Amazon S3 transfer acceleration. You can compare the upload
 speed for direct uploads and transfer accelerated uploads by Region. 

###### To enable transfer acceleration for an S3 general purpose bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the **General purpose buckets** list, choose the name of the bucket that you want to
 enable transfer acceleration for.
4. Choose **Properties**.
5. Under **Transfer acceleration**, choose
 **Edit**.
6. Choose **Enable**, and choose **Save changes**.
###### To access accelerated data transfers

1. After Amazon S3 enables transfer acceleration for your bucket, view the
 **Properties** tab for the bucket.
2. Under **Transfer acceleration**, **Accelerated
 endpoint** displays the transfer acceleration endpoint for your bucket. Use this
 endpoint to access accelerated data transfers to and from your bucket. 


If you suspend transfer acceleration, the accelerate endpoint no longer works.
The following are examples of AWS CLI commands used for Transfer Acceleration. For
 instructions on setting up the AWS CLI, see [Developing with Amazon S3 using the
 AWS CLI](../API/setup-aws-cli.md "../API/setup-aws-cli.md") in the *Amazon S3 API Reference*.


### Enabling Transfer Acceleration on a
 bucket


Use the AWS CLI [put-bucket-accelerate-configuration](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-bucket-accelerate-configuration.html "https://docs.aws.amazon.com/cli/latest/reference/s3api/put-bucket-accelerate-configuration.html") command to enable or
 suspend Transfer Acceleration on a bucket. 


The following example sets `Status=Enabled` to enable Transfer Acceleration on
 a bucket named ``amzn-s3-demo-bucket``. To suspend Transfer Acceleration, use
 `Status=Suspended`.



```
`$` aws s3api put-bucket-accelerate-configuration --bucket `amzn-s3-demo-bucket` --accelerate-configuration Status=Enabled
```

### Using Transfer Acceleration


You can direct all Amazon S3 requests made by `s3` and `s3api`
 AWS CLI commands to the accelerate endpoint: `s3-accelerate.amazonaws.com`. To
 do this, set the configuration value `use_accelerate_endpoint` to
 `true` in a profile in your AWS Config file. Transfer Acceleration must be enabled
 on your bucket to use the accelerate endpoint. 


All requests are sent using the virtual style of bucket
 addressing: ``amzn-s3-demo-bucket`.s3-accelerate.amazonaws.com`. Any
 `ListBuckets`, `CreateBucket`, and `DeleteBucket`
 requests are not sent to the accelerate endpoint because the endpoint doesn't support
 those operations. 


For more information about `use_accelerate_endpoint`, see [AWS CLI S3 Configuration](https://docs.aws.amazon.com/cli/latest/topic/s3-config.html "https://docs.aws.amazon.com/cli/latest/topic/s3-config.html")
 in the *AWS CLI Command Reference*.


The following example sets `use_accelerate_endpoint` to `true`
 in the default profile.



```
`$` aws configure set default.s3.use_accelerate_endpoint true
```

If you want to use the accelerate endpoint for some AWS CLI commands but not others,
 you can use either one of the following two methods: 



* Use the accelerate endpoint for any `s3` or `s3api`
 command by setting the `--endpoint-url` parameter to
 `https://s3-accelerate.amazonaws.com`.
* Set up separate profiles in your AWS Config file. For example, create one profile
 that sets `use_accelerate_endpoint` to `true` and a profile
 that does not set `use_accelerate_endpoint`. When you run a command,
 specify which profile you want to use, depending upon whether you want to use the
 accelerate endpoint.

### Uploading an object to a
 bucket enabled for Transfer Acceleration


The following example uploads a file to a bucket named
 ``amzn-s3-demo-bucket`` that's been enabled for Transfer Acceleration by using the
 default profile that has been configured to use the accelerate endpoint.



```
`$` aws s3 cp `file.txt` s3://``amzn-s3-demo-bucket`/key-name` --region `region`
```

The following example uploads a file to a bucket enabled for Transfer Acceleration by
 using the `--endpoint-url` parameter to specify the accelerate
 endpoint.



```
`$` aws configure set s3.addressing_style virtual
`$` aws s3 cp `file.txt` s3://``amzn-s3-demo-bucket`/key-name` --region `region` --endpoint-url https://s3-accelerate.amazonaws.com
```

The following are examples of using Transfer Acceleration to upload objects to Amazon S3 using
 the AWS SDK. Some of the AWS SDK supported languages (for example, Java
 and .NET) use an accelerate endpoint client configuration flag so you don't
 need to explicitly set the endpoint for Transfer Acceleration to
 ``bucket-name`.s3-accelerate.amazonaws.com`.


Java
To use an accelerate endpoint to upload an object to Amazon S3 with the AWS SDK for Java, you can:



* Create an S3Client that is configured to use accelerate endpoints. All buckets that the client accesses must have Transfer Acceleration enabled.
* Enable Transfer Acceleration on a specified bucket. This step is necessary only if the bucket you specify doesn't already have Transfer Acceleration enabled.
* Verify that transfer acceleration is enabled for the specified bucket.
* Upload a new object to the specified bucket using the bucket's accelerate endpoint.

For more information about using Transfer Acceleration, see [Getting started with
 Amazon S3 Transfer Acceleration](transfer-acceleration-getting-started.md "transfer-acceleration-getting-started.md").


The following code example shows how to configure Transfer Acceleration with the AWS SDK for Java.



```
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.BucketAccelerateStatus;
import software.amazon.awssdk.services.s3.model.GetBucketAccelerateConfigurationRequest;
import software.amazon.awssdk.services.s3.model.PutBucketAccelerateConfigurationRequest;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;
import software.amazon.awssdk.services.s3.model.AccelerateConfiguration;
import software.amazon.awssdk.services.s3.model.S3Exception;
import software.amazon.awssdk.core.exception.SdkClientException;

public class TransferAcceleration {
    public static void main(String[] args) {
        Region clientRegion = Region.US_EAST_1;
        String bucketName = "*** Provide bucket name ***";
        String keyName = "*** Provide key name ***";

        try {
            // Create an Amazon S3 client that is configured to use the accelerate endpoint.
            S3Client s3Client = S3Client.builder()
                    .region(clientRegion)
                    .credentialsProvider(ProfileCredentialsProvider.create())
                    .accelerate(true)
                    .build();

            // Enable Transfer Acceleration for the specified bucket.
            s3Client.putBucketAccelerateConfiguration(
                    PutBucketAccelerateConfigurationRequest.builder()
                            .bucket(bucketName)
                            .accelerateConfiguration(AccelerateConfiguration.builder()
                                    .status(BucketAccelerateStatus.ENABLED)
                                    .build())
                            .build());

            // Verify that transfer acceleration is enabled for the bucket.
            String accelerateStatus = s3Client.getBucketAccelerateConfiguration(
                    GetBucketAccelerateConfigurationRequest.builder()
                            .bucket(bucketName)
                            .build())
                    .status().toString();
            System.out.println("Bucket accelerate status: " + accelerateStatus);

            // Upload a new object using the accelerate endpoint.
            s3Client.putObject(PutObjectRequest.builder()
                            .bucket(bucketName)
                            .key(keyName)
                            .build(),
                    RequestBody.fromString("Test object for transfer acceleration"));
            System.out.println("Object \"" + keyName + "\" uploaded with transfer acceleration.");
        } catch (S3Exception e) {
            // The call was transmitted successfully, but Amazon S3 couldn't process
            // it, so it returned an error response.
            e.printStackTrace();
        } catch (SdkClientException e) {
            // Amazon S3 couldn't be contacted for a response, or the client
            // couldn't parse the response from Amazon S3.
            e.printStackTrace();
        }
    }
}
```


.NET
The following example shows how to use the AWS SDK for .NET to enable Transfer Acceleration
 on a bucket. For information about setting up and running the code examples, see
 [Getting Started with the AWS SDK for .NET](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/net-dg-setup.html "https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/net-dg-setup.html") in the *AWS SDK for .NET Developer
 Guide*. 



```
using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
using System;
using System.Threading.Tasks;

namespace Amazon.DocSamples.S3
{
    class TransferAccelerationTest
    {
        private const string bucketName = "*** bucket name ***";
        // Specify your bucket region (an example region is shown).
        private static readonly RegionEndpoint bucketRegion = RegionEndpoint.USWest2;
        private static IAmazonS3 s3Client;
        public static void Main()
        {
            s3Client = new AmazonS3Client(bucketRegion);
            EnableAccelerationAsync().Wait();
        }

        static async Task EnableAccelerationAsync()
        {
                try
                {
                    var putRequest = new PutBucketAccelerateConfigurationRequest
                    {
                        BucketName = bucketName,
                        AccelerateConfiguration = new AccelerateConfiguration
                        {
                            Status = BucketAccelerateStatus.Enabled
                        }
                    };
                    await s3Client.PutBucketAccelerateConfigurationAsync(putRequest);

                    var getRequest = new GetBucketAccelerateConfigurationRequest
                    {
                        BucketName = bucketName
                    };
                    var response = await s3Client.GetBucketAccelerateConfigurationAsync(getRequest);

                    Console.WriteLine("Acceleration state = '{0}' ", response.Status);
                }
                catch (AmazonS3Exception amazonS3Exception)
                {
                    Console.WriteLine(
                        "Error occurred. Message:'{0}' when setting transfer acceleration",
                        amazonS3Exception.Message);
                }
        }
    }
}

```

When uploading an object to a bucket that has Transfer Acceleration enabled, you
 specify using the acceleration endpoint at the time of creating a client.




```
var client = new AmazonS3Client(new AmazonS3Config
            {
                RegionEndpoint = TestRegionEndpoint,
                UseAccelerateEndpoint = true
            }
```


JavaScript
For an example of enabling Transfer Acceleration by using the AWS SDK for JavaScript, see [PutBucketAccelerateConfiguration command](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/PutBucketAccelerateConfigurationCommand/ "https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/PutBucketAccelerateConfigurationCommand/") in the
 *AWS SDK for JavaScript API Reference*.



Python (Boto)
For an example of enabling Transfer Acceleration by using the SDK for Python, see [put\_bucket\_accelerate\_configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_bucket_accelerate_configuration "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_bucket_accelerate_configuration") in the
 *AWS SDK for Python (Boto3) API Reference*.



Other
For information about using other AWS SDKs, see [Sample Code and Libraries](https://aws.amazon.com/code/ "https://aws.amazon.com/code/"). 



Use the REST API `PutBucketAccelerateConfiguration` operation to enable accelerate configuration on an existing bucket. 

For more information, see [PutBucketAccelerateConfiguration](../API/API_PutBucketAccelerateConfiguration.md "../API/API_PutBucketAccelerateConfiguration.md") in the *Amazon Simple Storage Service API Reference*.
