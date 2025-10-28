# UntagResource

The following Java example shows how to use the [`UntagResource`](url-signer-api.md "url-signer-api.md")
operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.UntagResourceRequest;

import java.util.Collections;

public class UntagResource {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingProfileArn = "arn:aws:signer:`region`:`account`:/signing-profiles/`MyProfile`";
        String tagKey = "Key";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("`region`")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // Remove a tag from a signing profile
        client.untagResource(new UntagResourceRequest()
                .withResourceArn(signingProfileArn)
                .withTagKeys(Collections.singletonList(tagKey)));
    }
}
```
