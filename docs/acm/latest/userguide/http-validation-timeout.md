# Validation timeout

HTTP validation may time out if the content isn't available within the expected time
frame. To troubleshoot validation issues, follow these steps.

###### To troubleshoot validation timeout

1. Do one of the following to check which domains are pending validation:
   1. Open the ACM console and view the certificate details page. Look for domains
      marked as **Pending validation**.
   2. Call the `DescribeCertificate` API operation to view the validation
      status of each domain.

2. For each pending domain, verify that the validation content is accessible from the
   internet.
