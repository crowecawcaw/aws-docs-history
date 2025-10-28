# TagResource

The following Java example shows how to use the [`TagResource`](../api/API_TagResource.md "../api/API_TagResource.md")
operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.TagResourceRequest;

import java.util.Collections;

public class TagResource {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingProfileArn = "arn:aws:signer:`region`:`account`:/signing-profiles/`MyProfile`";
        String tagKey = "Key";
        String tagValue = "Value";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("`region`")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // Add a tag to a signing profile
        client.tagResource(new TagResourceRequest()
                .withResourceArn(signingProfileArn)
                .withTags(Collections.singletonMap(tagKey, tagValue)));
    }
}
```
