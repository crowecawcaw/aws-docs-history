# RevokeSignature

The following Java example shows how to use the [`RevokeSignature`](../api/API_RevokeSignature.md "../api/API_RevokeSignature.md")
operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.RevokeSignatureRequest;

public class RevokeSignature {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingJobId = "`jobID`";
        String revokeReason = "`Reason for revocation`";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("`region`")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // Revoke a signing job
        client.revokeSignature(new RevokeSignatureRequest()
                .withJobId(signingJobId)
                .withReason(revokeReason));
    }
}
```
