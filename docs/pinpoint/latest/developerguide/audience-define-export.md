**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Export endpoints from Amazon Pinpoint to Amazon S3 buckets

To get all of the information that Amazon Pinpoint has about your audience, you can export the
endpoint definitions that belong to a project. When you export, Amazon Pinpoint places the
endpoint definitions in an Amazon S3 bucket that you specify. Exporting endpoints is useful when
you want to:

- View the latest data about new and existing endpoints that your client application
  registered with Amazon Pinpoint.
- Synchronize the endpoint data in Amazon Pinpoint with your own Customer Relationship
  Management (CRM) system.
- Create reports about or analyze your customer data.

###### Note

Content delivered to Amazon S3 buckets might contain customer content. If you need to delete
endpoint data that you exported to an Amazon S3 bucket, you must do so in Amazon S3 For more information
about removing sensitive data, see [How Do I
Empty an S3 Bucket?](../../../AmazonS3/latest/userguide/empty-bucket.md "../../../AmazonS3/latest/userguide/empty-bucket.md") or [How Do
I Delete an S3 Bucket?](../../../AmazonS3/latest/userguide/delete-bucket.md "../../../AmazonS3/latest/userguide/delete-bucket.md").

## Before you begin

Before you can export endpoints, you need the following resources in your AWS
account:

- An Amazon S3 bucket. To create a bucket, see [Create a bucket](../../../AmazonS3/latest/userguide/creating-bucket.md "../../../AmazonS3/latest/userguide/creating-bucket.md") in the _Amazon Simple Storage Service User Guide_.
- An AWS Identity and Access Management (IAM) role that grants Amazon Pinpoint write permissions for your Amazon S3
  bucket. To create the role, see [IAM role for exporting endpoints or
  segments](permissions-export-endpoints.md "permissions-export-endpoints.md").

## Examples

The following examples demonstrate how to export endpoints from an Amazon Pinpoint project, and
then download those endpoints from your Amazon S3 bucket.

AWS CLI You can use Amazon Pinpoint by running commands with the AWS CLI.

###### Example Create export job command

To export the endpoints in your Amazon Pinpoint project, use the [`create-export-job`](../../../cli/latest/reference/pinpoint/create-export-job.md "../../../cli/latest/reference/pinpoint/create-export-job.md") command:

```
`$` `aws pinpoint create-export-job \`
`>` `--application-id `application-id` \`
`>` `--export-job-request \`
`>` `S3UrlPrefix=s3://`bucket-name/prefix/`,\`
`>` `RoleArn=`iam-export-role-arn``

```

Where:

- `application-id` is the
  ID of the Amazon Pinpoint project that contains the endpoints.
- `bucket-name/prefix/` is
  the name of your Amazon S3 bucket and, optionally, a prefix that
  helps you organize the objects in your bucket hierarchically.
  For example, a useful prefix might be
  `pinpoint/exports/endpoints/`.
- `iam-export-role-arn` is
  the Amazon Resource Name (ARN) of an IAM role that grants
  Amazon Pinpoint write access to the bucket.
  The response to this command provides details about the export
  job:

```
{
    "ExportJobResponse": {
        "CreationDate": "2018-06-04T22:04:20.585Z",
        "Definition": {
            "RoleArn": "iam-export-role-arn",
            "S3UrlPrefix": "s3://s3-bucket-name/prefix/"
        },
        "Id": "7390e0de8e0b462380603c5a4df90bc4",
        "JobStatus": "CREATED",
        "Type": "EXPORT"
    }
}
```

The response provides the job ID with the `Id` attribute.
You can use this ID to check the current status of the export
job.

###### Example Get export job command

To check the current status of an export job, use the [`get-export-job`](../../../cli/latest/reference/pinpoint/get-export-job.md "../../../cli/latest/reference/pinpoint/get-export-job.md") command:

```
`$` `aws pinpoint get-export-job \`
`>` `--application-id `application-id` \`
`>` `--job-id `job-id``
```

Where:

- `application-id` is the ID
  the Amazon Pinpoint project that you exported the endpoints from.
- `job-id` is the ID of the
  job that you're checking.

The response to this command provides the current state of the export
job:

```
{
    "ExportJobResponse": {
        "ApplicationId": "application-id",
        "CompletedPieces": 1,
        "CompletionDate": "2018-05-08T22:16:48.228Z",
        "CreationDate": "2018-05-08T22:16:44.812Z",
        "Definition": {},
        "FailedPieces": 0,
        "Id": "6c99c463f14f49caa87fa27a5798bef9",
        "JobStatus": "COMPLETED",
        "TotalFailures": 0,
        "TotalPieces": 1,
        "TotalProcessed": 215,
        "Type": "EXPORT"
    }
}
```

The response provides the job status with the `JobStatus`
attribute. When the job status value is `COMPLETED`, you can get
your exported endpoints from your Amazon S3 bucket.

###### Example S3 CP command

To download your exported endpoints, use the Amazon S3 [`cp`](../../../cli/latest/reference/s3/cp.md "../../../cli/latest/reference/s3/cp.md")
command:

```
`$` `aws s3 cp s3://`bucket-name/prefix/key.gz` `/local/directory/``
```

Where:

- `bucket-name/prefix/key`
  is the location of the .gz file that Amazon Pinpoint added to your bucket
  when you exported your endpoints. This file contains the
  exported endpoint definitions. For example, in the URL `https://PINPOINT-EXAMPLE-BUCKET.s3.us-west-2.amazonaws.com/Exports/example.csv`, `PINPOINT-EXAMPLE-BUCKET` is the name of the bucket and `Exports/example.csv` is the key. For more information on **Keys**, see [Keys](../../../AmazonS3/latest/userguide/Welcome.md#BasicsKeys "../../../AmazonS3/latest/userguide/Welcome.md#BasicsKeys") in the _Amazon S3 User Guide_.
- `/local/directory/` is
  the file path to the local directory that you want to download
  the endpoints to.

AWS SDK for JavaYou can use the Amazon Pinpoint API in your Java applications by using the client that's provided by the AWS SDK for Java.

###### Example Code

To export endpoints from an Amazon Pinpoint project, initialize a
`CreateExportJobRequest` object. Then, pass this object
to the `createExportJob` method of the
`AmazonPinpoint` client.

To download the exported endpoints from Amazon Pinpoint, use the
`getObject` method of the `AmazonS3`
client.

```
import software.amazon.awssdk.core.ResponseBytes;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.pinpoint.PinpointClient;
import software.amazon.awssdk.services.pinpoint.model.ExportJobRequest;
import software.amazon.awssdk.services.pinpoint.model.PinpointException;
import software.amazon.awssdk.services.pinpoint.model.CreateExportJobRequest;
import software.amazon.awssdk.services.pinpoint.model.CreateExportJobResponse;
import software.amazon.awssdk.services.pinpoint.model.GetExportJobResponse;
import software.amazon.awssdk.services.pinpoint.model.GetExportJobRequest;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.ListObjectsV2Request;
import software.amazon.awssdk.services.s3.model.ListObjectsV2Response;
import software.amazon.awssdk.services.s3.model.S3Object;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;
import software.amazon.awssdk.services.s3.model.S3Exception;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

```

```
import software.amazon.awssdk.core.ResponseBytes;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.pinpoint.PinpointClient;
import software.amazon.awssdk.services.pinpoint.model.ExportJobRequest;
import software.amazon.awssdk.services.pinpoint.model.PinpointException;
import software.amazon.awssdk.services.pinpoint.model.CreateExportJobRequest;
import software.amazon.awssdk.services.pinpoint.model.CreateExportJobResponse;
import software.amazon.awssdk.services.pinpoint.model.GetExportJobResponse;
import software.amazon.awssdk.services.pinpoint.model.GetExportJobRequest;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.ListObjectsV2Request;
import software.amazon.awssdk.services.s3.model.ListObjectsV2Response;
import software.amazon.awssdk.services.s3.model.S3Object;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;
import software.amazon.awssdk.services.s3.model.S3Exception;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

/**
 * To run this code example, you need to create an AWS Identity and Access
 * Management (IAM) role with the correct policy as described in this
 * documentation:
 * https://docs.aws.amazon.com/pinpoint/latest/developerguide/audience-data-export.html
 *
 * Also, set up your development environment, including your credentials.
 *
 * For information, see this documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */

public class ExportEndpoints {
    public static void main(String[] args) {
        final String usage = """

                This program performs the following steps:

                1. Exports the endpoints to an Amazon S3 bucket.
                2. Downloads the exported endpoints files from Amazon S3.
                3. Parses the endpoints files to obtain the endpoint IDs and prints them.
                Usage: ExportEndpoints <applicationId> <s3BucketName> <iamExportRoleArn> <path>

                Where:
                  applicationId - The ID of the Amazon Pinpoint application that has the endpoint.
                  s3BucketName - The name of the Amazon S3 bucket to export the JSON file to.\s
                  iamExportRoleArn - The ARN of an IAM role that grants Amazon Pinpoint write permissions to the S3 bucket.  path - The path where the files downloaded from the Amazon S3 bucket are written (for example, C:/AWS/).
                """;

        if (args.length != 4) {
            System.out.println(usage);
            System.exit(1);
        }

        String applicationId = args[0];
        String s3BucketName = args[1];
        String iamExportRoleArn = args[2];
        String path = args[3];
        System.out.println("Deleting an application with ID: " + applicationId);

        Region region = Region.US_EAST_1;
        PinpointClient pinpoint = PinpointClient.builder()
                .region(region)
                .build();

        S3Client s3Client = S3Client.builder()
                .region(region)
                .build();

        exportAllEndpoints(pinpoint, s3Client, applicationId, s3BucketName, path, iamExportRoleArn);
        pinpoint.close();
        s3Client.close();
    }

    public static void exportAllEndpoints(PinpointClient pinpoint,
            S3Client s3Client,
            String applicationId,
            String s3BucketName,
            String path,
            String iamExportRoleArn) {

        try {
            List<String> objectKeys = exportEndpointsToS3(pinpoint, s3Client, s3BucketName, iamExportRoleArn,
                    applicationId);
            List<String> endpointFileKeys = objectKeys.stream().filter(o -> o.endsWith(".gz"))
                    .collect(Collectors.toList());
            downloadFromS3(s3Client, path, s3BucketName, endpointFileKeys);

        } catch (PinpointException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }

    public static List<String> exportEndpointsToS3(PinpointClient pinpoint, S3Client s3Client, String s3BucketName,
            String iamExportRoleArn, String applicationId) {

        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd-HH_mm:ss.SSS_z");
        String endpointsKeyPrefix = "exports/" + applicationId + "_" + dateFormat.format(new Date());
        String s3UrlPrefix = "s3://" + s3BucketName + "/" + endpointsKeyPrefix + "/";
        List<String> objectKeys = new ArrayList<>();
        String key;

        try {
            // Defines the export job that Amazon Pinpoint runs.
            ExportJobRequest jobRequest = ExportJobRequest.builder()
                    .roleArn(iamExportRoleArn)
                    .s3UrlPrefix(s3UrlPrefix)
                    .build();

            CreateExportJobRequest exportJobRequest = CreateExportJobRequest.builder()
                    .applicationId(applicationId)
                    .exportJobRequest(jobRequest)
                    .build();

            System.out.format("Exporting endpoints from Amazon Pinpoint application %s to Amazon S3 " +
                    "bucket %s . . .\n", applicationId, s3BucketName);

            CreateExportJobResponse exportResult = pinpoint.createExportJob(exportJobRequest);
            String jobId = exportResult.exportJobResponse().id();
            System.out.println(jobId);
            printExportJobStatus(pinpoint, applicationId, jobId);

            ListObjectsV2Request v2Request = ListObjectsV2Request.builder()
                    .bucket(s3BucketName)
                    .prefix(endpointsKeyPrefix)
                    .build();

            // Create a list of object keys.
            ListObjectsV2Response v2Response = s3Client.listObjectsV2(v2Request);
            List<S3Object> objects = v2Response.contents();
            for (S3Object object : objects) {
                key = object.key();
                objectKeys.add(key);
            }

            return objectKeys;

        } catch (PinpointException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return null;
    }

    private static void printExportJobStatus(PinpointClient pinpointClient,
            String applicationId,
            String jobId) {

        GetExportJobResponse getExportJobResult;
        String status;

        try {
            // Checks the job status until the job completes or fails.
            GetExportJobRequest exportJobRequest = GetExportJobRequest.builder()
                    .jobId(jobId)
                    .applicationId(applicationId)
                    .build();

            do {
                getExportJobResult = pinpointClient.getExportJob(exportJobRequest);
                status = getExportJobResult.exportJobResponse().jobStatus().toString().toUpperCase();
                System.out.format("Export job %s . . .\n", status);
                TimeUnit.SECONDS.sleep(3);

            } while (!status.equals("COMPLETED") && !status.equals("FAILED"));

            if (status.equals("COMPLETED")) {
                System.out.println("Finished exporting endpoints.");
            } else {
                System.err.println("Failed to export endpoints.");
                System.exit(1);
            }

        } catch (PinpointException | InterruptedException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }

    // Download files from an Amazon S3 bucket and write them to the path location.
    public static void downloadFromS3(S3Client s3Client, String path, String s3BucketName, List<String> objectKeys) {

        String newPath;
        try {
            for (String key : objectKeys) {
                GetObjectRequest objectRequest = GetObjectRequest.builder()
                        .bucket(s3BucketName)
                        .key(key)
                        .build();

                ResponseBytes<GetObjectResponse> objectBytes = s3Client.getObjectAsBytes(objectRequest);
                byte[] data = objectBytes.asByteArray();

                // Write the data to a local file.
                String fileSuffix = new SimpleDateFormat("yyyyMMddHHmmss").format(new Date());
                newPath = path + fileSuffix + ".gz";
                File myFile = new File(newPath);
                OutputStream os = new FileOutputStream(myFile);
                os.write(data);
            }
            System.out.println("Download finished.");

        } catch (S3Exception | NullPointerException | IOException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
}

```

For the full SDK example, see [ExportEndpoints.java](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/pinpoint/src/main/java/com/example/pinpoint/ExportEndpoints.java "https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/pinpoint/src/main/java/com/example/pinpoint/ExportEndpoints.java") on [GitHub](https://github.com/ "https://github.com/").

HTTP You can use Amazon Pinpoint by making HTTP requests directly to the REST API.

###### Example POST export job request

To export the endpoints in your Amazon Pinpoint project, issue a `POST`
request to the [Export jobs](../apireference/apps-application-id-jobs-export.md "../apireference/apps-application-id-jobs-export.md") resource:

```
POST /v1/apps/`application_id`/jobs/export HTTP/1.1
Content-Type: application/json
Accept: application/json
Host: pinpoint.us-east-1.amazonaws.com
X-Amz-Date: 20180606T001238Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20180606/us-east-1/mobiletargeting/aws4_request, SignedHeaders=accept;cache-control;content-length;content-type;host;postman-token;x-amz-date, Signature=c25cbd6bf61bd3b3667c571ae764b9bf2d8af61b875cacced95d1e68d91b4170
Cache-Control: no-cache

{
  "S3UrlPrefix": "s3://`bucket-name/prefix`",
  "RoleArn": "`iam-export-role-arn`"
}
```

Where:

- `application-id` is the
  ID of the Amazon Pinpoint project that contains the endpoints.
- `bucket-name/prefix` is
  the name of your Amazon S3 bucket and, optionally, a prefix that
  helps you organize the objects in your bucket hierarchically.
  For example, a useful prefix might be
  `pinpoint/exports/endpoints/`.
- `iam-export-role-arn` is
  the Amazon Resource Name (ARN) of an IAM role that grants
  Amazon Pinpoint write access to the bucket.
  The response to this request provides details about the export
  job:

```
{
    "Id": "611bdc54c75244bfa51fe7001ddb2e36",
    "JobStatus": "CREATED",
    "CreationDate": "2018-06-06T00:12:43.271Z",
    "Type": "EXPORT",
    "Definition": {
        "S3UrlPrefix": "s3://bucket-name/prefix",
        "RoleArn": "iam-export-role-arn"
    }
}
```

The response provides the job ID with the `Id` attribute.
You can use this ID to check the current status of the export
job.

###### Example GET export job request

To check the current status of an export job, issue a `GET`
request to the [Export job](../apireference/apps-application-id-jobs-export-job-id.md "../apireference/apps-application-id-jobs-export-job-id.md") resource:

```
GET /v1/apps/`application_id`/jobs/export/`job_id` HTTP/1.1
Content-Type: application/json
Accept: application/json
Host: pinpoint.us-east-1.amazonaws.com
X-Amz-Date: 20180606T002443Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20180606/us-east-1/mobiletargeting/aws4_request, SignedHeaders=accept;cache-control;content-type;host;postman-token;x-amz-date, Signature=c25cbd6bf61bd3b3667c571ae764b9bf2d8af61b875cacced95d1e68d91b4170
Cache-Control: no-cache
```

Where:

- `application-id` is the
  ID the Amazon Pinpoint project that you exported the endpoints
  from.
- `job-id` is the ID of
  the job that you're checking.
  The response to this request provides the current state of the export
  job:

```
{
    "ApplicationId": "application_id",
    "Id": "job_id",
    "JobStatus": "COMPLETED",
    "CompletedPieces": 1,
    "FailedPieces": 0,
    "TotalPieces": 1,
    "CreationDate": "2018-06-06T00:12:43.271Z",
    "CompletionDate": "2018-06-06T00:13:01.141Z",
    "Type": "EXPORT",
    "TotalFailures": 0,
    "TotalProcessed": 217,
    "Definition": {}
}
```

The response provides the job status with the `JobStatus`
attribute. When the job status value is `COMPLETED`, you can
get your exported endpoints from your Amazon S3 bucket.

## Related information

To find the endpoint ID for a specific endpoint, you must determine which segment the endpoint
belongs to, and then export the segment from Amazon Pinpoint. The exported data includes the
endpoint ID for each endpoint. You can export a segment to a file by using the Amazon Pinpoint
console. For more information about exporting segments, see
[Exporting Segments](../userguide/segments-exporting.md "../userguide/segments-exporting.md") in the
_Amazon Pinpoint User Guide_.

For more information about the Export Jobs resource in the Amazon Pinpoint API, including the
supported HTTP methods and request parameters, see [Export jobs](../apireference/apps-application-id-jobs-export.md "../apireference/apps-application-id-jobs-export.md") in the _Amazon Pinpoint API Reference_.
