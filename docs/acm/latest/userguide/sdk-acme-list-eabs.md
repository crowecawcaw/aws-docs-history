# Listing ACME external account bindings

The following example shows how to use the [ListAcmeExternalAccountBindings](../APIReference/API_ListAcmeExternalAccountBindings.md "../APIReference/API_ListAcmeExternalAccountBindings.md") function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.ListAcmeExternalAccountBindingsRequest;
import com.amazonaws.services.certificatemanager.model.ListAcmeExternalAccountBindingsResult;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create the request.
        ListAcmeExternalAccountBindingsRequest req = new ListAcmeExternalAccountBindingsRequest()
            .withAcmeEndpointArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example")
            .withMaxResults(10);

        // List the external account bindings.
        ListAcmeExternalAccountBindingsResult result = client.listAcmeExternalAccountBindings(req);
        System.out.println(result);
    }
}
```
