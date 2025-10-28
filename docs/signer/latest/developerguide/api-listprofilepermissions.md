# ListProfilePermissions

The following Java example shows how to use the [`ListProfilePermissions`](../api/API_ListProfilePermissions.md "../api/API_ListProfilePermissions.md") operation.

```
package com.examples;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSSigner;
import com.amazonaws.services.signer.AWSSignerClient;
import com.amazonaws.services.signer.model.ListProfilePermissionsRequest;
import com.amazonaws.services.signer.model.ListProfilePermissionsResult;
import com.amazonaws.services.signer.model.Permission;

public class ListProfilePermissions {

    public static void main(String[] s) {

        String credentialsProfile = "default";
        String signingProfileName = "`MyProfile`";

        // Create a client.
        final AWSSigner client = AWSSignerClient.builder()
                .withRegion("`region`")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        // List the permissions for a profile
        ListProfilePermissionsResult result = client.listProfilePermissions(new ListProfilePermissionsRequest()
                .withProfileName(signingProfileName));

        // Iterate through the permissions
        for (Permission permission: result.getPermissions()) {
            System.out.println("StatementId: " + permission.getStatementId());
            System.out.println("Principal: " + permission.getPrincipal());
            System.out.println("Action: " + permission.getAction());
            System.out.println("ProfileVersion: " + permission.getProfileVersion());
        }
        System.out.println("RevisionId: " + result.getRevisionId());
    }
}
```
