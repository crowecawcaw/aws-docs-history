

# Creating an ACME domain validation
<a name="sdk-acme-create-domain-validation"></a>

The following example shows how to use the [CreateAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeDomainValidation.html) function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.CreateAcmeDomainValidationRequest;
import com.amazonaws.services.certificatemanager.model.CreateAcmeDomainValidationResult;
import com.amazonaws.services.certificatemanager.model.PrevalidationOptions;
import com.amazonaws.services.certificatemanager.model.DnsPrevalidationOptions;
import com.amazonaws.services.certificatemanager.model.DomainScope;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Configure domain scope.
        DomainScope domainScope = new DomainScope()
            .withExactDomain("ENABLED")
            .withSubdomains("ENABLED")
            .withWildcards("ENABLED");

        // Configure DNS prevalidation options.
        DnsPrevalidationOptions dnsOptions = new DnsPrevalidationOptions()
            .withDomainScope(domainScope)
            .withHostedZoneId("Z1234567890");

        PrevalidationOptions prevalidationOptions = new PrevalidationOptions()
            .withDnsPrevalidation(dnsOptions);

        // Create the request.
        CreateAcmeDomainValidationRequest req = new CreateAcmeDomainValidationRequest()
            .withAcmeEndpointArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example")
            .withDomainName("example.com")
            .withPrevalidationOptions(prevalidationOptions);

        // Create the domain validation.
        CreateAcmeDomainValidationResult result = client.createAcmeDomainValidation(req);
        System.out.println(result.getAcmeDomainValidationArn());
    }
}
```