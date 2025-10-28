# Create a URL signature using

Java

In addition to the following code example, you can use [the `CloudFrontUrlSigner` utility class in the AWS SDK for Java (version 1)](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloudfront/CloudFrontUrlSigner.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloudfront/CloudFrontUrlSigner.md") to create [CloudFront signed
URLs](private-content-signed-urls.md "private-content-signed-urls.md").

For more examples, see [Create signed URLs and cookies using an AWS SDK](../../../code-library/latest/ug/cloudfront_example_cloudfront_CloudFrontUtilities_section.md "../../../code-library/latest/ug/cloudfront_example_cloudfront_CloudFrontUtilities_section.md") in the
_AWS SDK Code Examples Code Library_.

###### Note

Creating a signed URL is just one part of the process of [serving private content with CloudFront](PrivateContent.md "PrivateContent.md"). For more
information about the entire process, see [Use signed URLs](private-content-signed-urls.md "private-content-signed-urls.md").

The following example shows how to create a CloudFront signed URL.

###### Example Java policy and

signature encryption methods

```
package org.example;

import java.time.Instant;
import java.time.temporal.ChronoUnit;
import software.amazon.awssdk.services.cloudfront.CloudFrontUtilities;
import software.amazon.awssdk.services.cloudfront.model.CannedSignerRequest;
import software.amazon.awssdk.services.cloudfront.url.SignedUrl;

public class Main {

    public static void main(String[] args) throws Exception {
        CloudFrontUtilities cloudFrontUtilities = CloudFrontUtilities.create();
        Instant expirationDate = Instant.now().plus(7, ChronoUnit.DAYS);
        String resourceUrl = "https://a1b2c3d4e5f6g7.cloudfront.net";
        String keyPairId = "K1UA3WV15I7JSD";
        CannedSignerRequest cannedRequest = CannedSignerRequest.builder()
                .resourceUrl(resourceUrl)
                .privateKey(new java.io.File("/path/to/private_key.pem").toPath())
                .keyPairId(keyPairId)
                .expirationDate(expirationDate)
                .build();
        SignedUrl signedUrl = cloudFrontUtilities.getSignedUrlWithCannedPolicy(cannedRequest);
        String url = signedUrl.url();
        System.out.println(url);

    }
}

```

See also:

- [Create a URL signature using Perl](CreateURLPerl.md "CreateURLPerl.md")
- [Create a URL signature using PHP](CreateURL_PHP.md "CreateURL_PHP.md")
- [Create a URL signature using C# and the .NET
  Framework](CreateSignatureInCSharp.md "CreateSignatureInCSharp.md")
