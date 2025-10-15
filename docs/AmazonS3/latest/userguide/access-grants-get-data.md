# Accessing S3 data using credentials vended by S3 Access Grants

After a grantee [obtains temporary
 credentials](access-grants-credentials.md "access-grants-credentials.md") through their access grant, they can use these temporary credentials
 to call Amazon S3 API operations to access your data. 

Grantees can access S3 data by using the AWS Command Line Interface (AWS CLI), the AWS SDKs, and the Amazon S3 REST
 API. Additionally, you can use the AWS [Python](https://github.com/aws/boto3-s3-access-grants-plugin "https://github.com/aws/boto3-s3-access-grants-plugin") and [Java](https://github.com/aws/aws-s3-accessgrants-plugin-java-v2 "https://github.com/aws/aws-s3-accessgrants-plugin-java-v2") plugins to call S3 Access Grants

After the grantee obtains their temporary credentials from S3 Access Grants, they can set up a
 profile with these credentials to retrieve the data. 

To install the AWS CLI, see [Installing the
 AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html") in the *AWS Command Line Interface User Guide*.

To use the following example commands, replace the ``user input
 placeholders`` with your own information.

###### Example – Set up a profile


```
aws configure set aws_access_key_id "`$accessKey`" --profile `access-grants-consumer-access-profile`
aws configure set aws_secret_access_key "`$secretKey`" --profile `access-grants-consumer-access-profile`
aws configure set aws_session_token "`$sessionToken`" --profile `access-grants-consumer-access-profile`
```
To use the following example command, replace the ``user input
 placeholders`` with your own information.

###### Example – Get the S3 data

The grantee can use the [get-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/get-object.html "https://docs.aws.amazon.com/cli/latest/reference/s3api/get-object.html") AWS CLI command to access the data. The
 grantee can also use [put-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-object.html "https://docs.aws.amazon.com/cli/latest/reference/s3api/put-object.html"), [ls](https://docs.aws.amazon.com/cli/latest/reference/s3/ls.html "https://docs.aws.amazon.com/cli/latest/reference/s3/ls.html"), and other
 S3 AWS CLI commands. 


```
aws s3api get-object \
--bucket `amzn-s3-demo-bucket1` \
--key `myprefix` \
--region `us-east-2` \
--profile `access-grants-consumer-access-profile`
```
This section provides examples of how grantees can access your S3 data by using the AWS
 SDKs.


Java
The following Java code example gets an object from an S3 bucket. For
 instructions on creating and testing a working sample, see [Getting
 Started](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/getting-started.html "https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/getting-started.html") in the *AWS SDK for Java Developer
 Guide*.



```

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.GetObjectRequest;
import com.amazonaws.services.s3.model.ResponseHeaderOverrides;
import com.amazonaws.services.s3.model.S3Object;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class GetObject2 {

    public static void main(String[] args) throws IOException {
        Regions clientRegion = Regions.DEFAULT_REGION;
        String bucketName = "*** Bucket name ***";
        String key = "*** Object key ***";

        S3Object fullObject = null, objectPortion = null, headerOverrideObject = null;
        try {
            AmazonS3 s3Client = AmazonS3ClientBuilder.standard()
                    .withRegion(clientRegion)
                    .withCredentials(new ProfileCredentialsProvider())
                    .build();

            // Get an object and print its contents.
            System.out.println("Downloading an object");
            fullObject = s3Client.getObject(new GetObjectRequest(bucketName, key));
            System.out.println("Content-Type: " + fullObject.getObjectMetadata().getContentType());
            System.out.println("Content: ");
            displayTextInputStream(fullObject.getObjectContent());

            // Get a range of bytes from an object and print the bytes.
            GetObjectRequest rangeObjectRequest = new GetObjectRequest(bucketName, key)
                    .withRange(0, 9);
            objectPortion = s3Client.getObject(rangeObjectRequest);
            System.out.println("Printing bytes retrieved.");
            displayTextInputStream(objectPortion.getObjectContent());

            // Get an entire object, overriding the specified response headers, and print
            // the object's content.
            ResponseHeaderOverrides headerOverrides = new ResponseHeaderOverrides()
                    .withCacheControl("No-cache")
                    .withContentDisposition("attachment; filename=example.txt");
            GetObjectRequest getObjectRequestHeaderOverride = new GetObjectRequest(bucketName, key)
                    .withResponseHeaders(headerOverrides);
            headerOverrideObject = s3Client.getObject(getObjectRequestHeaderOverride);
            displayTextInputStream(headerOverrideObject.getObjectContent());
        } catch (AmazonServiceException e) {
            // The call was transmitted successfully, but Amazon S3 couldn't process
            // it, so it returned an error response.
            e.printStackTrace();
        } catch (SdkClientException e) {
            // Amazon S3 couldn't be contacted for a response, or the client
            // couldn't parse the response from Amazon S3.
            e.printStackTrace();
        } finally {
            // To ensure that the network connection doesn't remain open, close any open
            // input streams.
            if (fullObject != null) {
                fullObject.close();
            }
            if (objectPortion != null) {
                objectPortion.close();
            }
            if (headerOverrideObject != null) {
                headerOverrideObject.close();
            }
        }
    }

    private static void displayTextInputStream(InputStream input) throws IOException {
        // Read the text input stream one line at a time and display each line.
        BufferedReader reader = new BufferedReader(new InputStreamReader(input));
        String line = null;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
        System.out.println();
    }
}


```



## Supported S3 actions in S3 Access Grants


A grantee can use the temporary credential vended by S3 Access Grants to perform S3 actions on the S3 data they have access to. The following is a list of allowable S3 actions that a grantee can perform. Which actions are allowable depends on the level of permission granted in the access grant, either `READ`, `WRITE`, or `READWRITE`. 


###### Note

In addition to the Amazon S3 permissions listed below, Amazon S3 can call the AWS Key Management Service (AWS KMS) [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html") (`kms:decrypt`) `READ` permission or the AWS KMS [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html") (`kms:generateDataKey`) `WRITE` permission. These permissions don't allow direct access to the AWS KMS key.




| S3 IAM action | API action & doc | S3 Access Grants Permission | S3 resource |
| --- | --- | --- | --- |
| `s3:GetObject` | [GetObject](../API/API_GetObject.md "../API/API_GetObject.md") | `READ` | Object |
| `s3:GetObjectVersion` | [GetObject](../API/API_GetObject.md "../API/API_GetObject.md") | `READ` | Object |
| `s3:GetObjectAcl` | [GetObjectAcl](../API/API_GetObjectAcl.md "../API/API_GetObjectAcl.md") | `READ` | Object |
| `s3:GetObjectVersionAcl` | [GetObjectAcl](../API/API_GetObjectAcl.md "../API/API_GetObjectAcl.md") | `READ` | Object |
| `s3:ListMultipartUploads` | [ListParts](../API/API_ListParts.md "../API/API_ListParts.md") | `READ` | Object |
| `s3:PutObject` | [PutObject](../API/API_PutObject.md "../API/API_PutObject.md"), [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md"), [UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md"), [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"), [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md") | `WRITE` | Object |
| `s3:PutObjectAcl` | [PutObjectAcl](../API/API_PutObjectAcl.md "../API/API_PutObjectAcl.md") | `WRITE` | Object |
| `s3:PutObjectVersionAcl` | [PutObjectAcl](../API/API_PutObjectAcl.md "../API/API_PutObjectAcl.md") | `WRITE` | Object |
| `s3:DeleteObject` | [DeleteObject](../API/API_DeleteObject.md "../API/API_DeleteObject.md") | `WRITE` | Object |
| `s3:DeleteObjectVersion` | [DeleteObject](../API/API_DeleteObject.md "../API/API_DeleteObject.md") | `WRITE` | Object |
| `s3:AbortMultipartUpload` | [AbortMultipartUpload](../API/API_AbortMultipartUpload.md "../API/API_AbortMultipartUpload.md") | `WRITE` | Object |
| `s3:ListBucket` | [HeadBucket](../API/API_HeadBucket.md "../API/API_HeadBucket.md"), [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md"), [ListObjects](../API/API_ListObjects.md "../API/API_ListObjects.md") | `READ` | Bucket |
| `s3:ListBucketVersions` | [ListObjectVersions](../API/API_ListObjectVersions.md "../API/API_ListObjectVersions.md") | `READ` | Bucket |
| `s3:ListBucketMultipartUploads` | [ListMultipartUploads](../API/API_ListMultipartUploads.md "../API/API_ListMultipartUploads.md") | `READ` | Bucket |
