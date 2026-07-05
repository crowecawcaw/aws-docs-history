# Listing ACME endpoints

The following example shows how to use the [ListAcmeEndpoints](../APIReference/API_ListAcmeEndpoints.md "../APIReference/API_ListAcmeEndpoints.md") function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.ListAcmeEndpointsRequest;
import com.amazonaws.services.certificatemanager.model.ListAcmeEndpointsResult;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create the request.
        ListAcmeEndpointsRequest req = new ListAcmeEndpointsRequest()
            .withMaxResults(10);

        // List the ACME endpoints.
        ListAcmeEndpointsResult result = client.listAcmeEndpoints(req);
        System.out.println(result);
    }
}
```
