

# Updating an ACME domain validation
<a name="sdk-acme-update-domain-validation"></a>

The following example shows how to use the [UpdateAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateAcmeDomainValidation.html) function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.UpdateAcmeDomainValidationRequest;
import com.amazonaws.services.certificatemanager.model.PrevalidationOptions;
import com.amazonaws.services.certificatemanager.model.DnsPrevalidationOptions;
import com.amazonaws.services.certificatemanager.model.DomainScope;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Configure updated domain scope.
        DomainScope domainScope = new DomainScope()
            .withExactDomain("ENABLED")
            .withSubdomains("DISABLED")
            .withWildcards("DISABLED");

        DnsPrevalidationOptions dnsOptions = new DnsPrevalidationOptions()
            .withDomainScope(domainScope);

        PrevalidationOptions prevalidationOptions = new PrevalidationOptions()
            .withDnsPrevalidation(dnsOptions);

        // Create the request.
        UpdateAcmeDomainValidationRequest req = new UpdateAcmeDomainValidationRequest()
            .withAcmeDomainValidationArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example/acme-domain-validation/dv-example")
            .withPrevalidationOptions(prevalidationOptions);

        // Update the domain validation.
        client.updateAcmeDomainValidation(req);
    }
}
```