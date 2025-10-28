# Get a Secrets Manager secret value using the C++ AWS SDK

For C++ applications, call the SDK directly with [GetSecretValue](../../../goto/SdkForCpp/secretsmanager-2017-10-17/GetSecretValue.md "../../../goto/SdkForCpp/secretsmanager-2017-10-17/GetSecretValue.md") or [BatchGetSecretValue](../../../goto/SdkForCpp/secretsmanager-2017-10-17/BatchGetSecretValue.md "../../../goto/SdkForCpp/secretsmanager-2017-10-17/BatchGetSecretValue.md").

The following code example shows how to get a Secrets Manager secret value.

**Required permissions:** `secretsmanager:GetSecretValue`

```
//! Retrieve an AWS Secrets Manager encrypted secret.
/*!
  \param secretID: The ID for the secret.
  \return bool: Function succeeded.
 */
bool AwsDoc::SecretsManager::getSecretValue(const Aws::String &secretID,
                                            const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::SecretsManager::SecretsManagerClient secretsManagerClient(clientConfiguration);

    Aws::SecretsManager::Model::GetSecretValueRequest request;
    request.SetSecretId(secretID);

    Aws::SecretsManager::Model::GetSecretValueOutcome getSecretValueOutcome = secretsManagerClient.GetSecretValue(
            request);
    if (getSecretValueOutcome.IsSuccess()) {
        std::cout << "Secret is: "
                  << getSecretValueOutcome.GetResult().GetSecretString() << std::endl;
    }
    else {
        std::cerr << "Failed with Error: " << getSecretValueOutcome.GetError()
                  << std::endl;
    }

    return getSecretValueOutcome.IsSuccess();
}

```
