# Getting ACME external account binding credentials

The following example shows how to use the [GetAcmeExternalAccountBindingCredentials](../APIReference/API_GetAcmeExternalAccountBindingCredentials.md "../APIReference/API_GetAcmeExternalAccountBindingCredentials.md") function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.GetAcmeExternalAccountBindingCredentialsRequest;
import com.amazonaws.services.certificatemanager.model.GetAcmeExternalAccountBindingCredentialsResult;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create the request.
        GetAcmeExternalAccountBindingCredentialsRequest req = new GetAcmeExternalAccountBindingCredentialsRequest()
            .withAcmeExternalAccountBindingArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example/acme-external-account-binding/eab-example");

        // Get the credentials.
        GetAcmeExternalAccountBindingCredentialsResult result = client.getAcmeExternalAccountBindingCredentials(req);

        // Retrieve the key ID and MAC key from the response.
        System.out.println("KeyId: " + result.getKeyId());
        System.out.println("MacKey: " + result.getMacKey());
    }
}
```
