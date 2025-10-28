# PutSigningProfile

**Code signing for AWS IoT**

The following Java examples show how to use the [`PutSigningProfile`](../api/API_PutSigningProfile.md "../api/API_PutSigningProfile.md")
operation to create a new signing profile. Code signing profiles can be used in the [`StartSigningJob`](../api/API_StartSigningJob.md "../api/API_StartSigningJob.md")
operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.PutSigningProfileRequest;
import com.amazonaws.services.signer.model.SigningMaterial;

public class PutSigningProfile {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String codeSigningProfileName = "`MyProfile`";
        String codeSigningCertificateArn = "arn:aws:acm:`region`:`123456789`:certificate/`certID`";

        // Create a client.
        AWSSigner client = AWSSignerClient.builder()
            .withRegion("`region`")
            .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
            .build();

        // creating a code signing profile.
        client.putSigningProfile(new PutSigningProfileRequest()
            .withProfileName(codeSigningProfileName)
            .withSigningMaterial(new SigningMaterial()
                .withCertificateArn(codeSigningCertificateArn))
        .withPlatformId(signingPlatformId));
    }
}
```

**Code signing for AWS Lambda**

The next example shows how to use the [`PutSigningProfileProfile`](url-signer-api.md "url-signer-api.md") operation to create a new signing profile
for AWS Lambda. Code signing profiles can be used in the [`StartSigningJob`](../api/API_StartSigningJob.md "../api/API_StartSigningJob.md")
operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.PutSigningProfileRequest;

public class PutSigningProfile {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingProfileName = "MyProfile";
        String signingPlatformId = "AWSLambda-SHA384-ECDSA";

        // Create a client.
        AWSSigner client = AWSSignerClient.builder()
                .withRegion("us-west-2")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // Create a code signing profile.
        client.putSigningProfile(new PutSigningProfileRequest()
                .withProfileName(signingProfileName)
                .withPlatformId(signingPlatformId));
    }
}
```
