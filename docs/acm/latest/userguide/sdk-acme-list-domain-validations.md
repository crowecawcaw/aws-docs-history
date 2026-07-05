# Listing ACME domain validations

The following example shows how to use the [ListAcmeDomainValidations](../APIReference/API_ListAcmeDomainValidations.md "../APIReference/API_ListAcmeDomainValidations.md") function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.ListAcmeDomainValidationsRequest;
import com.amazonaws.services.certificatemanager.model.ListAcmeDomainValidationsResult;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create the request.
        ListAcmeDomainValidationsRequest req = new ListAcmeDomainValidationsRequest()
            .withAcmeEndpointArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example")
            .withMaxResults(10);

        // List the domain validations.
        ListAcmeDomainValidationsResult result = client.listAcmeDomainValidations(req);
        System.out.println(result);
    }
}
```
