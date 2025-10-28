# RevokeSigningProfile

The following Java example shows how to use the [`RevokeSigningProfile`](../api/API_RevokeSigningProfile.md "../api/API_RevokeSigningProfile.md") operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.RevokeSigningProfileRequest;

import java.time.Instant;
import java.util.Date;

public class RevokeSigningProfile {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingProfileName = "`MyProfile`";
        String signingProfileVersion = "`version`";
        String revokeReason = "`Reason for revocation`";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("`region`")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // Revoke a signing profile
        client.revokeSigningProfile(new RevokeSigningProfileRequest()
                .withProfileName(signingProfileName)
                .withProfileVersion(signingProfileVersion)
                .withReason(revokeReason)
                .withEffectiveTime(Date.from(Instant.now())));
    }
}
```
