# Get a Secrets Manager secret value using the Ruby AWS SDK

For Ruby applications, call the SDK directly with [`get_secret_value`](../../../sdk-for-ruby/v3/api/Aws/SecretsManager/Client.md#get_secret_value-instance_method "../../../sdk-for-ruby/v3/api/Aws/SecretsManager/Client.md#get_secret_value-instance_method") or [`batch_get_secret_value`](../../../sdk-for-ruby/v3/api/Aws/SecretsManager/Client.md#batch_get_secret_value-instance_method "../../../sdk-for-ruby/v3/api/Aws/SecretsManager/Client.md#batch_get_secret_value-instance_method").

The following code example shows how to get a Secrets Manager secret value.

**Required permissions:** `secretsmanager:GetSecretValue`

```
  # Use this code snippet in your app.
  # If you need more information about configurations or implementing the sample code, visit the AWS docs:
  # https://aws.amazon.com/developer/language/ruby/

  require 'aws-sdk-secretsmanager'

  def get_secret
    client = Aws::SecretsManager::Client.new(region: '<<{{MyRegionName}}>>')

    begin
      get_secret_value_response = client.get_secret_value(secret_id: '<<{{MySecretName}}>>')
    rescue StandardError => e
      # For a list of exceptions thrown, see
      # https://<<{{DocsDomain}}>>/secretsmanager/latest/apireference/API_GetSecretValue.html
      raise e
    end

    secret = get_secret_value_response.secret_string
    # Your code goes here.
  end
```
