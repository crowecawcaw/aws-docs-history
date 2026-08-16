# Updating a certificate's validation method

The following example shows how to use the [UpdateCertificateOptions](../APIReference/API_UpdateCertificateOptions.md "../APIReference/API_UpdateCertificateOptions.md") function with the `ValidationMethod`
option to migrate an existing email-validated public certificate to DNS validation. The
certificate ARN is preserved during migration. After you call this function, retrieve
the CNAME records by calling the [ListCertificateDomainValidations](../APIReference/API_ListCertificateDomainValidations.md "../APIReference/API_ListCertificateDomainValidations.md") function and add the records to your DNS
configuration within 72 hours.

```
package com.amazonaws.samples;

import com.amazonaws.AmazonClientException;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.regions.Regions;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;

import com.amazonaws.services.certificatemanager.model.CertificateOptions;
import com.amazonaws.services.certificatemanager.model.UpdateCertificateOptionsRequest;
import com.amazonaws.services.certificatemanager.model.UpdateCertificateOptionsResult;

import com.amazonaws.services.certificatemanager.model.ConflictException;
import com.amazonaws.services.certificatemanager.model.InvalidArnException;
import com.amazonaws.services.certificatemanager.model.InvalidStateException;
import com.amazonaws.services.certificatemanager.model.LimitExceededException;
import com.amazonaws.services.certificatemanager.model.ResourceNotFoundException;
import com.amazonaws.services.certificatemanager.model.ValidationException;

public class UpdateCertificateOptions {

   public static void main(String[] args) throws Exception {

      // Retrieve your credentials from the C:\Users\name\.aws\credentials file in Windows
      // or the ~/.aws/credentials in Linux.
      AWSCredentials credentials = null;
      try {
          credentials = new ProfileCredentialsProvider().getCredentials();
      }
      catch (Exception ex) {
          throw new AmazonClientException("Cannot load your credentials from file.", ex);
      }

      // Create a client.
      AWSCertificateManager client = AWSCertificateManagerClientBuilder.standard()
              .withRegion(Regions.`your_region`)
              .withCredentials(new AWSStaticCredentialsProvider(credentials))
              .build();

      // Build a CertificateOptions with ValidationMethod set to DNS, then create the
      // request. The certificate must be an issued public certificate that uses email
      // validation.
      CertificateOptions options = new CertificateOptions()
              .withValidationMethod("DNS");

      UpdateCertificateOptionsRequest req = new UpdateCertificateOptionsRequest()
              .withCertificateArn("arn:aws:acm:`region`:`account`:"
                      + "certificate/`12345678-1234-1234-1234-123456789012`")
              .withOptions(options);

      // Initiate the migration.
      UpdateCertificateOptionsResult result = null;
      try {
         result = client.updateCertificateOptions(req);
      }
      catch (ValidationException ex) {
         // Thrown when the certificate is not an issued public certificate,
         // or when the requested migration path is not supported (for example,
         // DNS to email).
         throw ex;
      }
      catch (ConflictException ex) {
         // Thrown when a migration is already in progress for this certificate.
         throw ex;
      }
      catch (InvalidArnException ex) {
         throw ex;
      }
      catch (InvalidStateException ex) {
         throw ex;
      }
      catch (LimitExceededException ex) {
         throw ex;
      }
      catch (ResourceNotFoundException ex) {
         throw ex;
      }

      // The response is empty on success. After this call returns, retrieve the CNAME
      // records by calling ListCertificateDomainValidations and add them to your DNS
      // configuration within 72 hours.
      System.out.println("Migration initiated. Retrieve CNAME records with "
              + "ListCertificateDomainValidations.");
   }
}
```
