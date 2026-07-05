# Updating an ACME endpoint

The following example shows how to use the [UpdateAcmeEndpoint](../APIReference/API_UpdateAcmeEndpoint.md "../APIReference/API_UpdateAcmeEndpoint.md") function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.UpdateAcmeEndpointRequest;
import com.amazonaws.services.certificatemanager.model.CertificateAuthority;
import com.amazonaws.services.certificatemanager.model.PublicCertificateAuthority;

import java.util.Arrays;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Configure an updated certificate authority.
        PublicCertificateAuthority publicCA = new PublicCertificateAuthority()
            .withAllowedKeyAlgorithms(Arrays.asList("RSA_2048", "EC_prime256v1", "EC_secp384r1"));

        CertificateAuthority ca = new CertificateAuthority()
            .withPublicCertificateAuthority(publicCA);

        // Create the request.
        UpdateAcmeEndpointRequest req = new UpdateAcmeEndpointRequest()
            .withAcmeEndpointArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example")
            .withContact("NOT_REQUIRED")
            .withCertificateAuthority(ca);

        // Update the ACME endpoint.
        client.updateAcmeEndpoint(req);
    }
}
```
