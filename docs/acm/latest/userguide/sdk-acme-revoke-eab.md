

# Revoking an ACME external account binding
<a name="sdk-acme-revoke-eab"></a>

The following example shows how to use the [RevokeAcmeExternalAccountBinding](https://docs.aws.amazon.com/acm/latest/APIReference/API_RevokeAcmeExternalAccountBinding.html) function.

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