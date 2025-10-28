# AddProfilePermission

The following Java example shows how to use the [`AddProfilePermission`](../api/API_AddProfilePermission.md "../api/API_AddProfilePermission.md") operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.AddProfilePermissionRequest;
import com.amazonaws.services.signer.model.AddProfilePermissionResult;

public class AddProfilePermission {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingProfileName = "`MyProfile`";
        String signingProfileVersion = "SeFHjuJAjV";
        String principal = "`account`";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("`region`")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // Add the first permission to the profile - no revisionId required.
        // Applies to all versions of the profile
        AddProfilePermissionResult result = client.addProfilePermission(new AddProfilePermissionRequest()
                .withProfileName(signingProfileName)
                .withStatementId("statement1")
                .withPrincipal(principal)
                .withAction("signer:StartSigningJob"));

        // Add the second permission to the profile - revisionId required.
        // Optionally specify a profile version to lock the permission to a specific profile version
        client.addProfilePermission(new AddProfilePermissionRequest()
                .withProfileName(signingProfileName)
                .withProfileVersion(signingProfileVersion)
                .withStatementId("statement2")
                .withPrincipal(principal)
                .withAction("signer:GetSigningProfile")
                .withRevisionId(result.getRevisionId()));
    }
}
```
