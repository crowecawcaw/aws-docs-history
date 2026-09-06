

# Configure KMS key for a registry
<a name="registry-configure-encryption"></a>

The KMS key determines how your registry encrypts data at rest. You can choose between an AWS owned key or a customer managed key that you store in your account and manage through AWS KMS. You can only configure the KMS key during registry creation. You cannot change the KMS key after the registry is created.

**Important**  
You cannot change the KMS key after the registry is created. Make sure that you select the correct key before creating the registry.

## Console
<a name="registry-configure-encryption-console"></a>

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#/registries/create) and choose **Create registry**.

1. Complete the required fields (**Name**, and optionally **Description**, **Discovery Authorization**, **Record approval**, and **Tags**).

1. Expand the **KMS key - optional** section.

1. Under **KMS key selection**, your data is encrypted by default with a key that we own and manage for you. To choose a different key, customize your encryption settings:
   +  ** AWS owned key (default)** — Leave the **Customize encryption settings (advanced)** checkbox unselected. We own and manage the KMS key.
   +  **Customer managed key** — Select the **Customize encryption settings (advanced)** checkbox. In the **Choose an AWS KMS key** field, enter an ARN or choose **Create an AWS KMS key** to open the AWS KMS console and create a new key.

1. Choose **Create registry**.

To confirm the encryption type after creation, view the registry details page and check the **KMS key** section.

## AWS CLI
<a name="registry-configure-encryption-cli"></a>

The following example creates a registry with a customer managed key:

```
aws agent-registry-control create-registry \
  --name "MyEncryptedRegistry" \
  --description "Registry with customer managed encryption" \
  --encryption-configuration '{"kmsKeyArn":"arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"}' \
  --region us-east-1
```

To create a registry with the default AWS owned key, omit the `--encryption-configuration` parameter:

```
aws agent-registry-control create-registry \
  --name "MyRegistry" \
  --description "Registry with default encryption" \
  --region us-east-1
```

## AWS SDK
<a name="registry-configure-encryption-sdk"></a>

The following Python example creates a registry with a customer managed key:

```
import boto3

client = boto3.client('agent-registry-control')

response = client.create_registry(
    name='MyEncryptedRegistry',
    description='Registry with customer managed encryption',
    encryptionConfiguration={
        'kmsKeyArn': 'arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'
    }
)

print(f"Registry ID: {response['registryId']}")
```

To create a registry with the default AWS owned key, omit the `encryptionConfiguration` parameter:

```
import boto3

client = boto3.client('agent-registry-control')

response = client.create_registry(
    name='MyRegistry',
    description='Registry with default encryption'
)

print(f"Registry ID: {response['registryId']}")
```

## Verify encryption configuration
<a name="registry-configure-encryption-verify"></a>

To verify the KMS key configuration of an existing registry, use `GetRegistry`:

```
import boto3

client = boto3.client('agent-registry-control')

response = client.get_registry(
    registryId='<registryId>'
)

encryption_config = response.get('encryptionConfiguration')
if encryption_config:
    print(f"KMS Key ARN: {encryption_config['kmsKeyArn']}")
else:
    print("Encryption: AWS owned key (default)")
```

If your `GetRegistry` response doesn’t include an `encryptionConfiguration` parameter, your registry is configured to encrypt data at rest with an AWS owned key.