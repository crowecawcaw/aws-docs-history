# Listing domain validation status

The following example shows how to use the [ListCertificateDomainValidations](../APIReference/API_ListCertificateDomainValidations.md "../APIReference/API_ListCertificateDomainValidations.md") function. The function returns a list of
domain validation summaries—one for each domain on the certificate. Each summary
contains the active validation configuration and (during a migration) the requested
validation configuration with the CNAME record to add to your DNS configuration. The
example shows how to handle pagination with `NextToken`.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;

import com.amazonaws.services.certificatemanager.model.ListCertificateDomainValidationsRequest;
import com.amazonaws.services.certificatemanager.model.ListCertificateDomainValidationsResult;
import com.amazonaws.services.certificatemanager.model.DomainValidationSummary;
import com.amazonaws.services.certificatemanager.model.ValidationConfiguration;
import com.amazonaws.services.certificatemanager.model.ValidationChallenge;
import com.amazonaws.services.certificatemanager.model.DnsValidationChallenge;
import com.amazonaws.services.certificatemanager.model.ResourceRecord;

import java.util.Optional;

public class ListCertificateDomainValidations {

   public static void main(String[] args) {

      // Create a client.
      AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

      String certificateArn =
              "arn:aws:acm:`region`:`account`:"
              + "certificate/`12345678-1234-1234-1234-123456789012`";

      // Page through the results using NextToken.
      String nextToken = null;
      do {
         ListCertificateDomainValidationsRequest req = new ListCertificateDomainValidationsRequest()
                 .withCertificateArn(certificateArn)
                 .withMaxItems(100)
                 .withNextToken(nextToken);

         ListCertificateDomainValidationsResult result = client.listCertificateDomainValidations(req);

         // Print the validation status for each domain.
         for (DomainValidationSummary summary : result.getDomainValidationSummaryList()) {
            System.out.println("Domain: " + summary.getDomainName());

            Optional.ofNullable(summary.getActiveValidationConfiguration())
               .ifPresent(active -> System.out.println("  Active method: "
                       + active.getValidationMethod()
                       + " (status: " + active.getValidationStatus() + ")"));

            Optional.ofNullable(summary.getRequestedValidationConfiguration())
               .ifPresent(requested -> {
                  System.out.println("  Requested method: " + requested.getValidationMethod()
                          + " (status: " + requested.getValidationStatus() + ")");

                  // For DNS migration, print the CNAME record to add to DNS.
                  Optional.ofNullable(requested.getValidationChallenge())
                     .map(ValidationChallenge::getDnsValidationChallenge)
                     .map(DnsValidationChallenge::getResourceRecord)
                     .ifPresent(record -> System.out.println("  Add CNAME: "
                             + record.getName() + " -> " + record.getValue()));
               });
         }

         nextToken = result.getNextToken();
      } while (nextToken != null);
   }
}
```
