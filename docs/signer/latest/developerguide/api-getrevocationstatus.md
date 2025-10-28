# GetRevocationStatus

The following Java example shows how to use the [`GetRevocationStatus`](../api/API_GetRevocationStatus.md "../api/API_GetRevocationStatus.md")
operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.GetRevocationStatusRequest;
import com.amazonaws.services.signer.model.GetRevocationStatusResult;

import java.time.Instant;
import java.util.Arrays;
import java.util.Date;

public class GetRevocationStatus {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        Date signatureTimestamp = Date.from(Instant.now());
        String platformId = "Notation-OCI-SHA384-ECDSA";
        String certificateHash = "`136eb997783e8d18a073e5977238765c39f1ca9bc919cf7ccab4430e5e5c39b756f21aa8c1687e536365f5916a47473`"
                               + "`326c4931465816650759563436d1705657bad8ac49d370d6ea64404716e92fa2d65dcdf5bf5caa99743a8bf60594efe`";
        String jobArn = "arn:aws:signer:`region`:`account`:/signing-jobs/`jobID`";
        String profileVersionArn = "arn:aws:signer:`region`:`account`:/signing-profiles/`MyProfile`/version";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("us-west-2")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // Get the revocation status
        GetRevocationStatusResult response = client.getRevocationStatus(new GetRevocationStatusRequest()
                .withSignatureTimestamp(signatureTimestamp)
                .withPlatformId(platformId)
                .withCertificateHashes(Arrays.asList(certificateHash))
                .withJobArn(jobArn)
                .withProfileVersionArn(profileVersionArn));

        // Print revoked resources
        System.out.println(response.getRevokedEntities());
    }
}
```
