# ListSigningPlatforms

The following Java example shows how to use the [`ListSigningPlatforms`](../api/API_ListSigningPlatforms.md "../api/API_ListSigningPlatforms.md") operation.

```
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSsigner;
import com.amazonaws.services.signer.AWSsignerClient;
import com.amazonaws.services.signer.model.ListSigningPlatformsRequest;
import com.amazonaws.services.signer.model.ListSigningPlatformsResult;
import com.amazonaws.services.signer.model.SigningPlatform;

public class ListSigningPlatforms {

    public static void main(String[] s) {

        final String credentialsProfile = "default";

        // Create a client.
        final AWSsigner client = AWSsignerClient.builder()
                .withRegion("`region`")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        ListSigningPlatformsResult result;
        String nextToken = null;
        do {
            result = client.listSigningPlatforms(new ListSigningPlatformsRequest().withNextToken(null));

            for (SigningPlatform platform : result.getPlatforms()) {
                System.out.println("Display Name : " + platform.getDisplayName());
                System.out.println("Platform Id : " + platform.getPlatformId());
                System.out.println("Signing Configuration : " + platform.getSigningConfiguration());
            }

            nextToken = result.getNextToken();
        } while (nextToken != null);
    }
}
```
