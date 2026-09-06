

# ListTagsForResource
<a name="api-listtagsforresource"></a>

The following Java example shows how to use the [`ListTagsForResource`](https://docs.aws.amazon.com/signer/latest/api/API_ListTagsForResource.html) operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.ListTagsForResourceRequest;
import com.amazonaws.services.signer.model.ListTagsForResourceResult;

import java.util.Map;

public class ListTagsForResource {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingProfileArn = "arn:aws:signer:{{region}}:{{account}}:/signing-profiles/{{MyProfile}}";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("{{region}}")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // List the tags for a signing profile
        ListTagsForResourceResult result = client.listTagsForResource(
                new ListTagsForResourceRequest().withResourceArn(signingProfileArn));

        // Iterate through the tags
        for (Map.Entry<String, String> tag: result.getTags().entrySet()) {
            System.out.println("Key: " + tag.getKey());
            System.out.println("Value: " + tag.getValue());
        }
    }
}
```