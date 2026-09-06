

# Describing an ACME endpoint
<a name="sdk-acme-describe-endpoint"></a>

The following example shows how to use the [DescribeAcmeEndpoint](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeEndpoint.html) function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.DescribeAcmeEndpointRequest;
import com.amazonaws.services.certificatemanager.model.DescribeAcmeEndpointResult;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create the request.
        DescribeAcmeEndpointRequest req = new DescribeAcmeEndpointRequest()
            .withAcmeEndpointArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example");

        // Describe the ACME endpoint.
        DescribeAcmeEndpointResult result = client.describeAcmeEndpoint(req);
        System.out.println(result);
    }
}
```