# DescribeSigningJob

The following Java example shows you how to use the [`DescribeSigningJob`](../api/API_DescribeSigningJob.md "../api/API_DescribeSigningJob.md")
operation. Call the [`StartSigningJob`](url-signer-api.md "url-signer-api.md") operation before calling
`DescribeSigningJob`. `StartSigningJob` returns a `jobId`
value that you use when you call `DescribeSigningJob`.

```
package com.amazonaws.samples;

import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.DescribeSigningJobRequest;
import com.amazonaws.services.signer.model.DescribeSigningJobResult;

import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.client.builder.AwsClientBuilder.EndpointConfiguration;

import com.amazonaws.services.signer.model.ResourceNotFoundException;
import com.amazonaws.services.signer.model.AccessDeniedException;
import com.amazonaws.services.signer.model.InternalServiceErrorException;
import com.amazonaws.AmazonClientException;

/**
* This sample demonstrates how to use the DescribeSigningJob operation in the
* AWS Signer service.
*
* Input Parameters:
*
*   jobId  - String that contains the ID of the job that was returned by the
*            StartSigningJob operation.
*
*/


public class DescribeSigningJob {

   public static void main(String[] args) throws Exception {

      // Retrieve your credentials from the `C:\Users\name\.aws\credentials` file
      // in Windows or the `~/.aws/credentials` file in Linux.
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
      DescribeSigningJobRequest req = new DescribeSigningJobRequest()
            .withJobId("`jobID`");

      // Create a result object.
      DescribeSigningJobResult result = null;
      try {
         result = client.describeSigningJob(req);
      }
      catch (ResourceNotFoundException ex)
      {
         throw ex;
      }
      catch (AccessDeniedException ex)
      {
         throw ex;
      }
      catch (InternalServiceErrorException ex)
      {
         throw ex;
      }

      // Display the information for your signing job.
      System.out.println(result.toString());

   }
}
```
