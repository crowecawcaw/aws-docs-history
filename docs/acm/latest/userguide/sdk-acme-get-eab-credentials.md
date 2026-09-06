

# Getting ACME external account binding credentials
<a name="sdk-acme-get-eab-credentials"></a>

The following example shows how to use the [GetAcmeExternalAccountBindingCredentials](https://docs.aws.amazon.com/acm/latest/APIReference/API_GetAcmeExternalAccountBindingCredentials.html) function.

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