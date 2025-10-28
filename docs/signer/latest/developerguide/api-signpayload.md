# SignPayload

The following Java example shows how to use the [`SignPayload`](../api/API_SignPayload.md "../api/API_SignPayload.md")
operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.SignPayloadRequest;

import java.nio.ByteBuffer;

public class SignPayload{

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingProfileName = "`MyProfile`";
        String payloadFormat = "application/vnd.cncf.notary.payload.v1+json";
        String payload = "{\n" +
            "  \"targetArtifact\": {\n" +
            "    \"mediaType\": \"application/vnd.docker.distribution.manifest.v2+json\",\n" +
            "    \"digest\": \"sha256:`73c803930ea3ba1e54bc25c2bdc53edd0284c62ed651fe7b00369da519a3c333`\",\n" +
            "    \"size\": 16724,\n" +
            "    \"annotations\": {\n" +
            "        \"io.wabbit-networks.buildId\": \"123\"" +
            "    }\n" +
            "  }\n" +
            "}";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("`region`")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // Sign a payload
        client.signPayload(new SignPayloadRequest()
                .withProfileName(signingProfileName)
                .withPayloadFormat(payloadFormat)
                .withPayload(ByteBuffer.wrap(payload.getBytes())));
    }
}
```
