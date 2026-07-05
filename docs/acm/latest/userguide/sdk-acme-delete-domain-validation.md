# Deleting an ACME domain validation

The following example shows how to use the [DeleteAcmeDomainValidation](../APIReference/API_DeleteAcmeDomainValidation.md "../APIReference/API_DeleteAcmeDomainValidation.md") function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.DeleteAcmeDomainValidationRequest;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create the request.
        DeleteAcmeDomainValidationRequest req = new DeleteAcmeDomainValidationRequest()
            .withAcmeDomainValidationArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example/acme-domain-validation/dv-example");

        // Delete the domain validation.
        client.deleteAcmeDomainValidation(req);
    }
}
```
