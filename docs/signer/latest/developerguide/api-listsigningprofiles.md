# ListSigningProfiles

The following Java example shows how to use the [`ListSigningProfiles`](../api/API_ListSigningProfiles.md "../api/API_ListSigningProfiles.md") operation.

```
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSsigner;
import com.amazonaws.services.signer.AWSsignerClient;
import com.amazonaws.services.signer.model.ListSigningProfilesRequest;
import com.amazonaws.services.signer.model.ListSigningProfilesResult;
import com.amazonaws.services.signer.model.SigningProfile;

public class ListSigningProfilesTest {

    public static void main(String[] s) {

        final String credentialsProfile = "default";

        // Create a client.
        final AWSsigner client = AWSsignerClient.builder()
                .withRegion("`region`")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        ListSigningProfilesResult result;
        String nextToken = null;
        do {
            result = client.listSigningProfiles(new ListSigningProfilesRequest().withNextToken(nextToken));

            for (SigningProfile profile : result.getProfiles()) {
                System.out.println("Profile Name : " + profile.getProfileName());
                System.out.println("Cert Arn : " + profile.getSigningMaterial().getCertificateArn());
                System.out.println("Profile Status : " + profile.getStatus());
                System.out.println("Platform Id : " + profile.getPlatformId());
            }

            nextToken = result.getNextToken();
        } while (nextToken != null);
    }
}
```
