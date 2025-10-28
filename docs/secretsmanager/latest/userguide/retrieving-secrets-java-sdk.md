# Get a Secrets Manager secret value using the Java AWS SDK

In applications, you can retrieve your secrets by calling `GetSecretValue` or `BatchGetSecretValue`in any of the AWS SDKs. However, we recommend that you cache your secret values by using client-side caching. Caching secrets improves speed and reduces your costs.

- If you store database credentials in the secret, use the [Secrets Manager SQL connection drivers](retrieving-secrets_jdbc.md "retrieving-secrets_jdbc.md") to connect to a
  database using the credentials in the secret.
- For other types of secrets, use the [Secrets Manager Java-based caching component](retrieving-secrets_cache-java.md "retrieving-secrets_cache-java.md") or call the SDK directly with [`GetSecretValue`](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/model/GetSecretValueResult.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/model/GetSecretValueResult.md") or [`BatchGetSecretValue`](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/model/BatchGetSecretValueResult.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/model/BatchGetSecretValueResult.md").
  The following code examples show how to use `GetSecretValue`.

**Required permissions:** `secretsmanager:GetSecretValue`

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.secretsmanager.SecretsManagerClient;
import software.amazon.awssdk.services.secretsmanager.model.GetSecretValueRequest;
import software.amazon.awssdk.services.secretsmanager.model.GetSecretValueResponse;
import software.amazon.awssdk.services.secretsmanager.model.SecretsManagerException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 *
 * We recommend that you cache your secret values by using client-side caching.
 *
 * Caching secrets improves speed and reduces your costs. For more information,
 * see the following documentation topic:
 *
 * https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html
 */
public class GetSecretValue {
    public static void main(String[] args) {
        final String usage = """

                Usage:
                    <secretName>\s

                Where:
                    secretName - The name of the secret (for example, tutorials/MyFirstSecret).\s
                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String secretName = args[0];
        Region region = Region.US_EAST_1;
        SecretsManagerClient secretsClient = SecretsManagerClient.builder()
                .region(region)
                .build();

        getValue(secretsClient, secretName);
        secretsClient.close();
    }

    public static void getValue(SecretsManagerClient secretsClient, String secretName) {
        try {
            GetSecretValueRequest valueRequest = GetSecretValueRequest.builder()
                    .secretId(secretName)
                    .build();

            GetSecretValueResponse valueResponse = secretsClient.getSecretValue(valueRequest);
            String secret = valueResponse.secretString();
            System.out.println(secret);

        } catch (SecretsManagerException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}

```
