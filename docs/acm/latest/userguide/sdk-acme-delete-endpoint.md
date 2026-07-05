# Deleting an ACME endpoint

The following example shows how to use the [DeleteAcmeEndpoint](../APIReference/API_DeleteAcmeEndpoint.md "../APIReference/API_DeleteAcmeEndpoint.md") function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.DeleteAcmeEndpointRequest;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create the request.
        DeleteAcmeEndpointRequest req = new DeleteAcmeEndpointRequest()
            .withAcmeEndpointArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example");

        // Delete the ACME endpoint.
        client.deleteAcmeEndpoint(req);
    }
}
```
