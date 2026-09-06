

# Creating an ACME endpoint
<a name="sdk-acme-create-endpoint"></a>

The following example shows how to use the [CreateAcmeEndpoint](https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeEndpoint.html) function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.CreateAcmeEndpointRequest;
import com.amazonaws.services.certificatemanager.model.CreateAcmeEndpointResult;
import com.amazonaws.services.certificatemanager.model.CertificateAuthority;
import com.amazonaws.services.certificatemanager.model.PublicCertificateAuthority;
import com.amazonaws.services.certificatemanager.model.Tag;

import java.util.ArrayList;
import java.util.Arrays;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Configure the certificate authority.
        PublicCertificateAuthority publicCA = new PublicCertificateAuthority()
            .withAllowedKeyAlgorithms(Arrays.asList("RSA_2048", "EC_prime256v1"));

        CertificateAuthority ca = new CertificateAuthority()
            .withPublicCertificateAuthority(publicCA);

        // Specify tags for the endpoint.
        ArrayList<Tag> tags = new ArrayList<>();
        tags.add(new Tag().withKey("Environment").withValue("Production"));

        // Specify tags to apply to certificates issued by this endpoint.
        ArrayList<Tag> certTags = new ArrayList<>();
        certTags.add(new Tag().withKey("IssuedBy").withValue("ACME"));

        // Create the request.
        CreateAcmeEndpointRequest req = new CreateAcmeEndpointRequest()
            .withAuthorizationBehavior("PRE_APPROVED")
            .withContact("REQUIRED")
            .withCertificateAuthority(ca)
            .withTags(tags)
            .withCertificateTags(certTags);

        // Create the ACME endpoint.
        CreateAcmeEndpointResult result = client.createAcmeEndpoint(req);
        System.out.println(result.getAcmeEndpointArn());
    }
}
```