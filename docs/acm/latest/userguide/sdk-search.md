

# Searching certificates
<a name="sdk-search"></a>

The following Java example shows how to use the [SearchCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_SearchCertificates.html) function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.SearchCertificatesRequest;
import com.amazonaws.services.certificatemanager.model.SearchCertificatesResponse;
import com.amazonaws.services.certificatemanager.model.CertificateFilterStatement;
import com.amazonaws.services.certificatemanager.model.CertificateFilter;
import com.amazonaws.services.certificatemanager.model.AcmCertificateMetadataFilter;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.regions.Regions;

import com.amazonaws.AmazonClientException;

/**
 * This sample demonstrates how to use the SearchCertificates function in the AWS Certificate
 * Manager service.
 *
 * Input parameters:
 *   FilterStatement - Optional filter to narrow search results.
 *   MaxResults - The maximum number of certificates to return in the response.
 *   NextToken - Use when paginating results.
 *   SortBy - The field to sort results by (default: CREATED_AT).
 *   SortOrder - The sort order (default: ASCENDING).
 *
 * Output parameters:
 *   Results - A list of certificate search results.
 *   NextToken - Use to show additional results when paginating a truncated list.
 *
 */

public class AWSCertificateManagerExample {

   public static void main(String[] args) throws Exception{

      // Retrieve your credentials from the C:\Users\name\.aws\credentials file in Windows
      // or the ~/.aws/credentials file in Linux.
      AWSCredentials credentials = null;
      try {
          credentials = new ProfileCredentialsProvider().getCredentials();
      }
      catch (Exception ex) {
          throw new AmazonClientException("Cannot load the credentials from file.", ex);
      }

      // Create a client.
      AWSCertificateManager client = AWSCertificateManagerClientBuilder.standard()
              .withRegion(Regions.{{US_EAST_1}})
              .withCredentials(new AWSStaticCredentialsProvider(credentials))
              .build();

      // Create a request object and set the parameters.
      SearchCertificatesRequest req = new SearchCertificatesRequest();
      req.setMaxResults(10);

      // Optional: Filter by certificate status
      CertificateFilterStatement filter = CertificateFilterStatement.builder()
              .withFilter(CertificateFilter.builder()
                      .withAcmCertificateMetadataFilter(AcmCertificateMetadataFilter.builder()
                              .withStatus("ISSUED")
                              .build())
                      .build())
              .build();
      req.setFilterStatement(filter);

      // Search for certificates.
      SearchCertificatesResponse result = null;
      try {
         result = client.searchCertificates(req);
      }
      catch (Exception ex)
      {
         throw ex;
      }

      // Display the certificate list.
      System.out.println(result);
   }
}
```

The preceding sample creates output similar to the following.

```
{
    Results: [{
        CertificateArn: arn:aws:acm:{{region}}:{{account}}:certificate/{{12345678-1234-1234-1234-123456789012}},
        X509Attributes: {
            Issuer: {
                CommonName: Example CA,
                Country: US,
                Organization: Example Corp
            },
            Subject: {
                CommonName: {{www.example1.com}}
            },
            ExtendedKeyUsages: [TLS_WEB_SERVER_AUTHENTICATION, TLS_WEB_CLIENT_AUTHENTICATION],
            KeyAlgorithm: RSA_2048,
            KeyUsages: [DIGITAL_SIGNATURE, KEY_ENCIPHERMENT],
            SerialNumber: {{serial_number}},
            NotAfter: 2025-02-14T23:59:59+00:00,
            NotBefore: 2024-01-15T00:00:00+00:00
        },
        CertificateMetadata: {
            AcmCertificateMetadata: {
                CreatedAt: 2024-01-15T12:00:00+00:00,
                IssuedAt: 2024-01-15T12:05:00+00:00,
                Exported: false,
                InUse: true,
                RenewalEligibility: ELIGIBLE,
                Status: ISSUED,
                Type: AMAZON_ISSUED,
                ValidationMethod: DNS
            }
        }
    },
    {
        CertificateArn: arn:aws:acm:{{region}}:{{account}}:certificate/{{12345678-1234-1234-1234-123456789013}},
        X509Attributes: {
            Issuer: {
                CommonName: Example CA,
                Country: US,
                Organization: Example Corp
            },
            Subject: {
                CommonName: {{www.example2.com}}
            },
            ExtendedKeyUsages: [TLS_WEB_SERVER_AUTHENTICATION],
            KeyAlgorithm: EC_prime256v1,
            KeyUsages: [DIGITAL_SIGNATURE],
            SerialNumber: {{serial_number}},
            NotAfter: 2026-06-30T23:59:59+00:00,
            NotBefore: 2025-01-01T00:00:00+00:00
        },
        CertificateMetadata: {
            AcmCertificateMetadata: {
                CreatedAt: 2025-01-01T10:00:00+00:00,
                ImportedAt: 2025-01-01T10:00:00+00:00,
                Exported: false,
                InUse: false,
                RenewalEligibility: INELIGIBLE,
                Status: ISSUED,
                Type: IMPORTED
            }
        }
    }]
}
```