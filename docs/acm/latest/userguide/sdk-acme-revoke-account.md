

# Revoking an ACME account
<a name="sdk-acme-revoke-account"></a>

The following example shows how to use the [RevokeAcmeAccount](https://docs.aws.amazon.com/acm/latest/APIReference/API_RevokeAcmeAccount.html) function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.RevokeAcmeAccountRequest;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create the request.
        RevokeAcmeAccountRequest req = new RevokeAcmeAccountRequest()
            .withAcmeEndpointArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example")
            .withAccountUrl("https://acme.example.com/acme/acct/12345");

        // Revoke the ACME account.
        client.revokeAcmeAccount(req);
    }
}
```