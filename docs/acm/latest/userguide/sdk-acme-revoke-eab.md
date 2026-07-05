# Revoking an ACME external account binding

The following example shows how to use the [RevokeAcmeExternalAccountBinding](../APIReference/API_RevokeAcmeExternalAccountBinding.md "../APIReference/API_RevokeAcmeExternalAccountBinding.md") function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.RevokeAcmeExternalAccountBindingRequest;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create the request.
        RevokeAcmeExternalAccountBindingRequest req = new RevokeAcmeExternalAccountBindingRequest()
            .withAcmeExternalAccountBindingArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example/acme-external-account-binding/eab-example");

        // Revoke the external account binding.
        client.revokeAcmeExternalAccountBinding(req);
    }
}
```
