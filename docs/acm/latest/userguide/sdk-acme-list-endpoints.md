

# Listing ACME endpoints
<a name="sdk-acme-list-endpoints"></a>

The following example shows how to use the [ListAcmeEndpoints](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeEndpoints.html) function.

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