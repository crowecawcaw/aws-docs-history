# RemoveProfilePermission

The following Java example shows how to use the [`RemoveProfilePermission`](../api/API_RemoveProfilePermission.md "../api/API_RemoveProfilePermission.md") operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.ListProfilePermissionsRequest;
import com.amazonaws.services.signer.model.ListProfilePermissionsResult;
import com.amazonaws.services.signer.model.RemoveProfilePermissionRequest;

public class RemoveProfilePermission {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingProfileName = "`MyProfile`";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("`region`")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // Get the latest revisionId for the profile
        ListProfilePermissionsResult result = client.listProfilePermissions(new ListProfilePermissionsRequest()
                .withProfileName(signingProfileName));

        // Remove a specific permission from the profile
        client.removeProfilePermission(new RemoveProfilePermissionRequest()
                .withProfileName(signingProfileName)
                .withStatementId("statement1")
                .withRevisionId(result.getRevisionId()));
    }
}
```
