# Use checksums to work with an Amazon S3 object using an AWS SDK

The following code example shows how to use checksums to work with an Amazon S3 object.


Java


**SDK for Java 2.x**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples").
 


The code examples use a subset of the following imports.



```

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.core.exception.SdkException;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.ChecksumAlgorithm;
import software.amazon.awssdk.services.s3.model.ChecksumMode;
import software.amazon.awssdk.services.s3.model.CompletedMultipartUpload;
import software.amazon.awssdk.services.s3.model.CompletedPart;
import software.amazon.awssdk.services.s3.model.CreateMultipartUploadResponse;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;
import software.amazon.awssdk.services.s3.model.UploadPartRequest;
import software.amazon.awssdk.services.s3.model.UploadPartResponse;
import software.amazon.awssdk.services.s3.waiters.S3Waiter;
import software.amazon.awssdk.transfer.s3.S3TransferManager;
import software.amazon.awssdk.transfer.s3.model.FileUpload;
import software.amazon.awssdk.transfer.s3.model.UploadFileRequest;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.ByteBuffer;
import java.nio.file.Paths;
import java.security.DigestInputStream;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.Base64;
import java.util.List;
import java.util.Objects;
import java.util.UUID;


```

Specify a checksum algorithm for the `putObject` method when you [build the `PutObjectRequest`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/model/PutObjectRequest.Builder.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/model/PutObjectRequest.Builder.html").



```
    public void putObjectWithChecksum() {
        s3Client.putObject(b -> b
                .bucket(bucketName)
                .key(key)
                .checksumAlgorithm(ChecksumAlgorithm.CRC32),
            RequestBody.fromString("This is a test"));
    }


```

Verify the checksum for the `getObject` method when you [build the GetObjectRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/model/GetObjectRequest.Builder.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/model/GetObjectRequest.Builder.html").



```
    public GetObjectResponse getObjectWithChecksum() {
        return s3Client.getObject(b -> b
                .bucket(bucketName)
                .key(key)
                .checksumMode(ChecksumMode.ENABLED))
            .response();
    }


```

Pre-calculate a checksum for the `putObject` method when you [build the `PutObjectRequest`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/model/PutObjectRequest.Builder.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/model/PutObjectRequest.Builder.html").



```
    public void putObjectWithPrecalculatedChecksum(String filePath) {
        String checksum = calculateChecksum(filePath, "SHA-256");

        s3Client.putObject((b -> b
                .bucket(bucketName)
                .key(key)
                .checksumSHA256(checksum)),
            RequestBody.fromFile(Paths.get(filePath)));
    }


```

Use the [S3 Transfer Manager](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/transfer-manager.html "https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/transfer-manager.html") on top of the [AWS CRT-based S3 client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/crt-based-s3-client.html "https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/crt-based-s3-client.html") to transparently perform a multipart upload when the size of the content exceeds a threshold. The default threshold size is 8 MB.

 You can specify a checksum algorithm for the SDK to use. By default, the SDK uses the CRC32 algorithm.



```
    public void multipartUploadWithChecksumTm(String filePath) {
        S3TransferManager transferManager = S3TransferManager.create();
        UploadFileRequest uploadFileRequest = UploadFileRequest.builder()
            .putObjectRequest(b -> b
                .bucket(bucketName)
                .key(key)
                .checksumAlgorithm(ChecksumAlgorithm.SHA1))
            .source(Paths.get(filePath))
            .build();
        FileUpload fileUpload = transferManager.uploadFile(uploadFileRequest);
        fileUpload.completionFuture().join();
        transferManager.close();
    }


```

Use the [S3Client API](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3Client.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3Client.html") 
 or (S3AsyncClient API) to perform a multipart upload. If you specify
 an additional checksum, you must specify the algorithm to use on the initiation of the upload.
 You must also specify the algorithm for each part request and provide the checksum calculated
 for each part after it is
 uploaded.



```
    public void multipartUploadWithChecksumS3Client(String filePath) {
        ChecksumAlgorithm algorithm = ChecksumAlgorithm.CRC32;

        // Initiate the multipart upload.
        CreateMultipartUploadResponse createMultipartUploadResponse = s3Client.createMultipartUpload(b -> b
            .bucket(bucketName)
            .key(key)
            .checksumAlgorithm(algorithm)); // Checksum specified on initiation.
        String uploadId = createMultipartUploadResponse.uploadId();

        // Upload the parts of the file.
        int partNumber = 1;
        List<CompletedPart> completedParts = new ArrayList<>();
        ByteBuffer bb = ByteBuffer.allocate(1024 * 1024 * 5); // 5 MB byte buffer

        try (RandomAccessFile file = new RandomAccessFile(filePath, "r")) {
            long fileSize = file.length();
            long position = 0;
            while (position < fileSize) {
                file.seek(position);
                long read = file.getChannel().read(bb);

                bb.flip(); // Swap position and limit before reading from the buffer.
                UploadPartRequest uploadPartRequest = UploadPartRequest.builder()
                    .bucket(bucketName)
                    .key(key)
                    .uploadId(uploadId)
                    .checksumAlgorithm(algorithm) // Checksum specified on each part.
                    .partNumber(partNumber)
                    .build();

                UploadPartResponse partResponse = s3Client.uploadPart(
                    uploadPartRequest,
                    RequestBody.fromByteBuffer(bb));

                CompletedPart part = CompletedPart.builder()
                    .partNumber(partNumber)
                    .checksumCRC32(partResponse.checksumCRC32()) // Provide the calculated checksum.
                    .eTag(partResponse.eTag())
                    .build();
                completedParts.add(part);

                bb.clear();
                position += read;
                partNumber++;
            }
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }

        // Complete the multipart upload.
        s3Client.completeMultipartUpload(b -> b
            .bucket(bucketName)
            .key(key)
            .uploadId(uploadId)
            .multipartUpload(CompletedMultipartUpload.builder().parts(completedParts).build()));
    }


```


* For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.




	+ [CompleteMultipartUpload](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CompleteMultipartUpload "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CompleteMultipartUpload")
	+ [CreateMultipartUpload](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CreateMultipartUpload "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CreateMultipartUpload")
	+ [UploadPart](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/UploadPart "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/UploadPart")




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
