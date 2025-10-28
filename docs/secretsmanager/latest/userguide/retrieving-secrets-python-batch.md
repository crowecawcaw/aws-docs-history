# Get a batch of Secrets Manager secret values using the Python AWS SDK

The following code example shows how to get a batch of Secrets Manager secret values.

**Required permissions:**

- `secretsmanager:BatchGetSecretValue`
- `secretsmanager:GetSecretValue` permission for each secret you want to retrieve.
- If you use filters, you must also have `secretsmanager:ListSecrets`.
  For an example permissions policy, see [Example: Permission to retrieve a group of secret values in a batch](auth-and-access_iam-policies.md#auth-and-access_examples_batch "auth-and-access_iam-policies.md#auth-and-access_examples_batch").

###### Important

If you have a VPCE policy that denies permission to retrieve an individual secret in the group you are retrieving, `BatchGetSecretValue` will not return any secret values, and it will return an error.

```
class BatchGetSecretsWrapper:
    def __init__(self, secretsmanager_client):
        self.client = secretsmanager_client


    def batch_get_secrets(self, filter_name):
        """
        Retrieve multiple secrets from AWS Secrets Manager using the batch_get_secret_value API.
        This function assumes the stack mentioned in the source code README has been successfully deployed.
        This stack includes 7 secrets, all of which have names beginning with "mySecret".

        :param filter_name: The full or partial name of secrets to be fetched.
        :type filter_name: str
        """
        try:
            secrets = []
            response = self.client.batch_get_secret_value(
                Filters=[{"Key": "name", "Values": [f"{filter_name}"]}]
            )
            for secret in response["SecretValues"]:
                secrets.append(json.loads(secret["SecretString"]))
            if secrets:
                logger.info("Secrets retrieved successfully.")
            else:
                logger.info("Zero secrets returned without error.")
            return secrets
        except self.client.exceptions.ResourceNotFoundException:
            msg = f"One or more requested secrets were not found with filter: {filter_name}"
            logger.info(msg)
            return msg
        except Exception as e:
            logger.error(f"An unknown error occurred:\n{str(e)}.")
            raise



```
