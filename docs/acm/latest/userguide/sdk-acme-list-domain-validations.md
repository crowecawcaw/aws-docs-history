

# Listing ACME domain validations
<a name="sdk-acme-list-domain-validations"></a>

The following example shows how to use the [ListAcmeDomainValidations](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeDomainValidations.html) function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.ListAcmeDomainValidationsRequest;
import com.amazonaws.services.certificatemanager.model.ListAcmeDomainValidationsResult;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create the request.
        ListAcmeDomainValidationsRequest req = new ListAcmeDomainValidationsRequest()
            .withAcmeEndpointArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example")
            .withMaxResults(10);

        // List the domain validations.
        ListAcmeDomainValidationsResult result = client.listAcmeDomainValidations(req);
        System.out.println(result);
    }
}
```