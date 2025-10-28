# GetSigningProfile

The following Java example shows how to use the [`GetSigningProfile`](../api/API_SetSigningProfile.md "../api/API_SetSigningProfile.md")
operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.GetSigningProfileRequest;
import com.amazonaws.services.signer.model.GetSigningProfileResult;

/**
* This examples demonstrates retreiving a signing profile's information.
*/
public class GetSigningProfile {

    public static void main(String[] s) {

        final String credentialsProfile = "default";
        final String codeSigningProfileName = "`MyProfile`";

    // Create a client.
    final AWSSigner client = AWSSignerClient.builder()
        .withRegion("`region`")
        .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
        .build();

    // Get a signing profile.
    GetSigningProfileResult getSigningProfileResult = client.getSigningProfile(new
        GetSigningProfileRequest().withProfileName(codeSigningProfileName));

    System.out.println("Profile Name : " + getSigningProfileResult.getProfileName());
    System.out.println("Certificate Arn : " + getSigningProfileResult.getSigningMaterial().getCertificateArn());
    System.out.println("Platform : " + getSigningProfileResult.getPlatform());
    }
}
```
