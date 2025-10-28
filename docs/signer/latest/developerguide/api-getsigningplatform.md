# GetSigningPlatform

The following Java example shows how to use the [`GetSigningPlatform`](../api/API_GetSigningPlatform.md "../api/API_GetSigningPlatform.md")
operation.

```
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.signer.AWSsigner;
import com.amazonaws.services.signer.AWSsignerClient;
import com.amazonaws.services.signer.model.GetSigningPlatformRequest;
import com.amazonaws.services.signer.model.GetSigningPlatformResult;

public class GetSigningPlatform {


    public static void main(String[] s) {

        String credentialsProfile = "default";
        String codeSigningPlatformId = "aws-signer-platform-id";

        // Create a client.
        AWSsigner client = AWSsignerClient.builder()
                .withRegion("`region`")
                .withCredentials(new ProfileCredentialsProvider(credentialsProfile))
                .build();

        GetSigningPlatformResult result = client.getSigningPlatform(
                new GetSigningPlatformRequest().withPlatformId(codeSigningPlatformId));

        System.out.println("Display Name : " + result.getDisplayName());
        System.out.println("Platform Id : " + result.getPlatformId());
        System.out.println("Signing Configuration : " + result.getSigningConfiguration());
    }
}
```
