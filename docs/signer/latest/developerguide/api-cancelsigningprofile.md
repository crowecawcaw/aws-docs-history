# CancelSigningProfile

The following Java example shows how to use the [`CancelSigningProfile`](../api/API_CancelSigningProfile.md "../api/API_CancelSigningProfile.md") operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.CancelSigningProfileRequest;

/**
* This examples demonstrates how to program a CancelSigningProfile operation .
*/
public class CancelSigningProfile {

    public static void main(String[] s) {

        final String credentialsProfile = "default";
        final String codeSigningProfileName = "`MyProfile`";


        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
            .withRegion("`region`")
            .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
            .build();

        // cancel a signing profile
        client.cancelSigningProfile(new CancelSigningProfileRequest().withProfileName(codeSigningProfileName));
    }
}
```
