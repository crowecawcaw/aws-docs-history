# StartSigningJob

The following Java example shows how to use the [`StartSigningJob`](../api/API_StartSigningJob.md "../api/API_StartSigningJob.md")
operation. You must call `StartSigningJob` before you call any other AWS Signer
API operation. `StartSigningJob` returns a `jobId` value that you can
use when calling [`DescribeSigningJob`](../api/API_DescribeSigningJob.md "../api/API_DescribeSigningJob.md") operation.

```
package com.amazonaws.samples;

import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.Source;
import com.amazonaws.services.signer.model.S3Source;
import com.amazonaws.services.signer.model.Destination;
import com.amazonaws.services.signer.model.S3Destination;
import com.amazonaws.services.signer.model.StartSigningJobRequest;
import com.amazonaws.services.signer.model.StartSigningJobResult;

import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.client.builder.AwsClientBuilder.EndpointConfiguration;

import com.amazonaws.services.signer.model.ValidationException;
import com.amazonaws.services.signer.model.ResourceNotFoundException;
import com.amazonaws.services.signer.model.AccessDeniedException;
import com.amazonaws.services.signer.model.ThrottlingException;
import com.amazonaws.services.signer.model.InternalServiceErrorException;
import com.amazonaws.AmazonClientException;

/**
* This sample demonstrates how to use the StartSigningJob operation in the
* AWS Signer service.
*
* Input Parameters:
*
* source             - Structure that contains the following:
*                          - Name of the Amazon S3 bucket to which you copied your
*                            code image
*                          - Name of the file that contains your code image
*                          - Amazon S3 version number of your file
* destination        - Structure that contains the following:
*                          - Name of the Amazon S3 bucket that AWS Signer can use for
*                            your signed code
*                          - Optional Amazon S3 bucket prefix
*
*/

public class StartSigningJob {

   public static void main(String[] args) throws Exception{

      // Define variables.
      String bucketSrc = "`amzn-s3-demo-source-bucket`";
      String key = "`Code-Image-File`";
      String objectVersion = "`Source-S3-File-Version`";
      String bucketDest = "`amzn-s3-demo-destination-bucket`";
      S3Source s3src = new S3Source()
          .withBucketName(bucketSrc)
          .withKey(key)
          .withVersion(objectVersion);
      Source src = new Source().withS3(s3src);
      S3Destination s3Dest = new S3Destination().withBucketName(bucketDest);
      Destination dest = new Destination().withS3(s3Dest);
      String signingProfileName = "`MyProfile`";

      // Retrieve your credentials from the C:\Users\name\.aws\credentials file in
      // Windows or the ~/.aws/credentials in Linux.
      AWSCredentials credentials = null;
      try {
          credentials = new ProfileCredentialsProvider().getCredentials();
      }
      catch (Exception ex) {
          throw new AmazonClientException("Cannot load your credentials from file.", ex);
      }

      // Specify the endpoint and region.
      EndpointConfiguration endpoint =
            new EndpointConfiguration("`https://endpoint`","`region`");


      // Create a client.
      AWSSigner client = AWSSignerClient.builder()
            .withEndpointConfiguration(endpoint)
            .withCredentials(new AWSStaticCredentialsProvider(credentials))
            .build();


      // Create a request object.
      StartSigningJobRequest req = new StartSigningJobRequest()
            .withSource(src)
            .withDestination(dest)
            .withProfileName(signingProfileName);

      // Create a result object.
      StartSigningJobResult result = null;
      try {
         result = client.startSigningJob(req);
      }
      catch (ValidationException ex)
      {
         throw ex;
      }
      catch (ResourceNotFoundException ex)
      {
         throw ex;
      }
      catch (AccessDeniedException ex)
      {
         throw ex;
      }
      catch (ThrottlingException ex)
      {
         throw ex;
      }
      catch (InternalServiceErrorException ex)
      {
         throw ex;
      }

      // Display the job ID.
      System.out.println("Job ID: " + result.getJobId());

   }
}
```
