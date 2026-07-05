# Deleting an ACME external account binding

The following example shows how to use the [DeleteAcmeExternalAccountBinding](../APIReference/API_DeleteAcmeExternalAccountBinding.md "../APIReference/API_DeleteAcmeExternalAccountBinding.md") function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.DeleteAcmeExternalAccountBindingRequest;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create the request.
        DeleteAcmeExternalAccountBindingRequest req = new DeleteAcmeExternalAccountBindingRequest()
            .withAcmeExternalAccountBindingArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example/acme-external-account-binding/eab-example");

        // Delete the external account binding.
        client.deleteAcmeExternalAccountBinding(req);
    }
}
```
