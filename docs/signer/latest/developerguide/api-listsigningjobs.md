# ListSigningJobs

The following Java example shows how to use the [`ListSigningJobs`](../api/API_ListSigningJobs.md "../api/API_ListSigningJobs.md")
operations. This operation lists all of the signing jobs that you have performed in your
account. Call the [`StartSigningJob`](../api/API_StartSigningJob.md "../api/API_StartSigningJob.md") operation before you call
`ListSigningJobs`. You can also call [`DescribeSigningJob`](../api/API_DescribeSigningJob.md "../api/API_DescribeSigningJob.md")
and specify a `jobId` to see information about a specific signing job created by
calling `StartSigningJob`.

```
package com.amazonaws.samples;

import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.ListSigningJobsRequest;
import com.amazonaws.services.signer.model.ListSigningJobsResult;

import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.client.builder.AwsClientBuilder.EndpointConfiguration;

import com.amazonaws.services.signer.model.ValidationException;
import com.amazonaws.services.signer.model.AccessDeniedException;
import com.amazonaws.services.signer.model.ThrottlingException;
import com.amazonaws.services.signer.model.InternalServiceErrorException;
import com.amazonaws.AmazonClientException;

/**
* This sample demonstrates how to use the ListSigningJobs operation in the
* AWS Signer service.
*
* Input Parameters:
*
* status      - String that specifies the status that you want to use for filtering.
*               This can be:
*                  - InProgress
*                  - Failed
*                  - Succeeded
* platform    - String that contains the name of the microcontroller platform that
*               you want to use for filtering.
* requestedBy - IAM  principal that requested the signing job.
* maxResults  - Use this parameter when paginating results to specify the maximum
*               number of items to return in the response. If additional items exist
*               beyond the number you specify, the nextToken element is sent in the
*               response. Use the nextToken value in a subsequent request to retrieve
*               additional items.
* nextToken   - Use this parameter only when paginating results and only in a
*               subsequent request after you receive a response with truncated results.
*               Set it to the value of `nextToken` from the response you
*               just received.
*
*/

public class ListSigningJobs {

   public static void main(String[] args) throws Exception{

      // Retrieve your credentials from the `C:\Users\name\.aws\credentials` file in Windows
      // or the `~/.aws/credentials` file in Linux.
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
      ListSigningJobsRequest req = new ListSigningJobsRequest()
            .withStatus("Succeeded")
            .withPlatform("`platform`")
            .withMaxResults(10);

      // Create a result object.
      ListSigningJobsResult result = null;
      try {
         result = client.listSigningJobs(req);
      }
      catch (ValidationException ex)
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

      // Display the information for your signing job.
      System.out.println(result.toString());

   }
}
```
