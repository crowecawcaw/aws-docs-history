

# Creating an ACME external account binding
<a name="sdk-acme-create-eab"></a>

The following example shows how to use the [CreateAcmeExternalAccountBinding](https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeExternalAccountBinding.html) function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.CreateAcmeExternalAccountBindingRequest;
import com.amazonaws.services.certificatemanager.model.CreateAcmeExternalAccountBindingResult;
import com.amazonaws.services.certificatemanager.model.Expiration;
import com.amazonaws.services.certificatemanager.model.Tag;

import java.util.ArrayList;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Configure expiration.
        Expiration expiration = new Expiration()
            .withValue(7L)
            .withType("DAYS");

        // Specify tags.
        ArrayList<Tag> tags = new ArrayList<>();
        tags.add(new Tag().withKey("Environment").withValue("Production"));

        // Create the request.
        CreateAcmeExternalAccountBindingRequest req = new CreateAcmeExternalAccountBindingRequest()
            .withAcmeEndpointArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example")
            .withRoleArn("arn:aws:iam::123456789012:role/AcmeClientRole")
            .withExpiration(expiration)
            .withTags(tags);

        // Create the external account binding.
        CreateAcmeExternalAccountBindingResult result = client.createAcmeExternalAccountBinding(req);
        System.out.println(result);
    }
}
```