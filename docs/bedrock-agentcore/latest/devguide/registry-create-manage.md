

# Create and manage registries
<a name="registry-create-manage"></a>

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

## Create a registry
<a name="registry-create"></a>

### Console
<a name="registry-create-console"></a>

**Example**  

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, under **Discover**, choose **Registry**.

1. In the **Registries** section, choose **Create registry**.

1. For **Name**, enter a name for your registry. The name must start with a letter or digit. Valid characters are a-z, A-Z, 0-9, \_ (underscore), - (hyphen), . (dot), and / (forward slash). The name can have up to 64 characters.

1. (Optional) Expand **Additional details** and enter a **Description** (1–4,096 characters).

1. (Optional) Expand **Discovery Authorization** to configure how consumers authorize when discovering records in the registry — searching, browsing the approved-record catalog, batch-getting approved records, and invoking the registry’s MCP endpoint (Inbound Authorization). Choose ** AWS IAM** to use standard AWS credentials, or **JSON Web tokens (JWT)** to use your corporate identity provider credentials. If you choose JWT, you can either quick create with Cognito, or bring your own IdP by providing the discovery URL, audience, scope, custom claims and clients.

1. Under **Record approval**, choose whether to enable **Auto-approval**. When auto-approval is off, a curator must review and approve each record before it becomes searchable.

1. (Optional) Expand **Tags** to add tags to the registry. Tags are key-value pairs that help you categorize, search, and manage your registries. Each tag consists of a required key and an optional value.

1. (Optional) Expand **KMS key** to configure encryption at rest with a customer managed key. By default, your registry is encrypted with an AWS owned key. To use your own key, select **Customize encryption settings (advanced)** and enter the ARN of your KMS key, or choose **Create an AWS KMS key** to create a new key. The KMS key cannot be changed after the registry is created. For more information, see [Data protection in AWS Agent Registry](registry-data-protection.md).

1. Choose **Create registry**.

1. Open the [Amazon Bedrock AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the navigation pane, under **Discover**, choose **Registry**.

1. In the **Registries** section, choose **Create registry**.

1. For **Name**, enter a name for your registry. The name must start with a letter or digit. Valid characters are a-z, A-Z, 0-9, \_ (underscore), - (hyphen), . (dot), and / (forward slash). The name can have up to 64 characters.

1. (Optional) Expand **Additional details** and enter a **Description** (1–4,096 characters).

1. (Optional) Expand **Search API Authorization** to configure how consumers authorize when searching the registry (Inbound Authorization). Choose ** AWS IAM** to use standard AWS credentials, or **JSON Web tokens (JWT)** to use your corporate identity provider credentials. If you choose JWT, you can either quick create with Cognito, or bring your own IdP by providing the discovery URL, audience, scope, custom claims and clients.

1. Under **Record approval**, choose whether to enable **Auto-approval**. When auto-approval is off, a curator must review and approve each record before it becomes searchable.

1. (Optional) Expand **KMS key** to configure encryption at rest with a customer managed key. By default, your registry is encrypted with an AWS owned key. To use your own key, select **Customize encryption settings (advanced)** and enter the ARN of your KMS key, or choose **Create an AWS KMS key** to create a new key. The KMS key cannot be changed after the registry is created. For more information, see [Data protection in AWS Agent Registry](registry-data-protection.md).

1. Choose **Create registry**.

The registry status starts as **Creating** and transitions to **Ready** when provisioning completes.

**Note**  
For JWT enabled registries, At least one **JWT authorization configuration** field is required: allowed audiences, allowed clients, allowed scopes, or custom claims. If you configure more than one, AWS Agent Registry verifies all of them.

### AWS CLI
<a name="registry-create-cli"></a>

 **IAM-based registry:** 

**Example**  

```
aws agent-registry-control create-registry \
  --name "MyRegistry" \
  --description "Production registry" \
  --region us-east-1
```

```
aws bedrock-agentcore-control create-registry \
  --name "MyRegistry" \
  --description "Production registry" \
  --region us-east-1
```

 **JWT-based registry:** 

**Example**  

```
aws agent-registry-control create-registry \
  --name "MyOAuthRegistry" \
  --discovery-configuration '{"authorizerType": "CUSTOM_JWT", "authorizerConfiguration": {"customJWTAuthorizer": {"discoveryUrl": "https://cognito-idp.us-east-1.amazonaws.com/<poolId>/.well-known/openid-configuration", "allowedClients": ["<appClientId>"]}}}' \
  --region us-east-1
```

```
aws bedrock-agentcore-control create-registry \
  --name "MyOAuthRegistry" \
  --authorizer-type CUSTOM_JWT \
  --authorizer-configuration '{"customJWTAuthorizer": {"discoveryUrl": "https://cognito-idp.us-east-1.amazonaws.com/<poolId>/.well-known/openid-configuration", "allowedClients": ["<appClientId>"]}}' \
  --region us-east-1
```

#### Registry with a customer managed key
<a name="_registry_with_a_customer_managed_key"></a>

**Example**  

```
aws agent-registry-control create-registry \
  --name "MyEncryptedRegistry" \
  --description "Registry with customer managed encryption" \
  --encryption-configuration '{"kmsKeyArn":"arn:aws:kms:us-east-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"}' \
  --region us-east-1
```

```
aws bedrock-agentcore-control create-registry \
  --name "MyEncryptedRegistry" \
  --description "Registry with customer managed encryption" \
  --encryption-configuration '{"kmsKeyArn":"arn:aws:kms:us-east-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"}' \
  --region us-east-1
```

**Note**  
You can only set the `--encryption-configuration` parameter during registry creation. You cannot change the KMS key after the registry is created. If you omit this parameter, the registry uses an AWS owned key by default.

### AWS SDK
<a name="registry-create-sdk"></a>

 **IAM-based registry:** 

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.create_registry(
    name='MyRegistry',
    description='Production registry'
)
print(response['registryArn'])
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.create_registry(
    name='MyRegistry',
    description='Production registry'
)
print(response['registryArn'])
```

 **JWT-based registry:** 

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.create_registry(
    name='MyOAuthRegistry',
    discoveryConfiguration={
        'authorizerType': 'CUSTOM_JWT',
        'authorizerConfiguration': {
            'customJWTAuthorizer': {
                'discoveryUrl': 'https://cognito-idp.us-east-1.amazonaws.com/<poolId>/.well-known/openid-configuration',
                'allowedClients': ['<appClientId>']
            }
        }
    }
)
print(response['registryArn'])
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.create_registry(
    name='MyOAuthRegistry',
    authorizerType='CUSTOM_JWT',
    authorizerConfiguration={
        'customJWTAuthorizer': {
            'discoveryUrl': 'https://cognito-idp.us-east-1.amazonaws.com/<poolId>/.well-known/openid-configuration',
            'allowedClients': ['<appClientId>']
        }
    }
)
print(response['registryArn'])
```

#### Registry with a customer managed key
<a name="_registry_with_a_customer_managed_key_2"></a>

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.create_registry(
    name='MyEncryptedRegistry',
    description='Registry with customer managed encryption',
    encryptionConfiguration={
        'kmsKeyArn': 'arn:aws:kms:us-east-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222'
    }
)
print(response['registryArn'])
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.create_registry(
    name='MyEncryptedRegistry',
    description='Registry with customer managed encryption',
    encryptionConfiguration={
        'kmsKeyArn': 'arn:aws:kms:us-east-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222'
    }
)
print(response['registryArn'])
```

## List registries
<a name="registry-list"></a>

### Console
<a name="registry-list-console"></a>

**Example**  

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, under **Discover**, choose **Registry**.

1. The **Registries** table displays all registries in your account with the following columns:

   1.  **Name** — The registry name (linked to the detail page).

   1.  **Description** — The registry description, if provided.

   1.  **Auth type** — The inbound authorization method (AWS\_IAM or CUSTOM\_JWT).

   1.  **Status** — The current status (Creating, Ready, Updating, Deleting, or a failure state).

   1.  **ARN** — The registry Amazon Resource Name.

   1.  **Created** — The creation timestamp.

   1.  **Last updated** — The last modification timestamp.

1. Use the **Find registries** search bar to filter by name.

1. Use the pagination controls to navigate through results.

1. Open the [Amazon Bedrock AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the navigation pane, under **Discover**, choose **Registry**.

1. The **Registries** table displays all registries in your account with the following columns:

   1.  **Name** — The registry name (linked to the detail page).

   1.  **Description** — The registry description, if provided.

   1.  **Authorization type** — The inbound authorization method (AWS\_IAM or CUSTOM\_JWT).

   1.  **Status** — The current status (Creating, Ready, Updating, Deleting, or a failure state).

   1.  **ARN** — The registry Amazon Resource Name.

   1.  **Created** — The creation timestamp.

   1.  **Last updated** — The last modification timestamp.

1. Use the **Find registries** search bar to filter by name.

1. Use the pagination controls to navigate through results.

### AWS CLI
<a name="registry-list-cli"></a>

**Example**  

```
aws agent-registry-control list-registries \
  --region us-east-1
```

```
aws bedrock-agentcore-control list-registries \
  --region us-east-1
```

### AWS SDK
<a name="registry-list-sdk"></a>

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.list_registries()
for registry in response['registries']:
    print(f"{registry['name']} - {registry['status']} - {registry['registryArn']}")
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.list_registries()
for registry in response['registries']:
    print(f"{registry['name']} - {registry['status']} - {registry['registryArn']}")
```

## View registry details
<a name="registry-view-details"></a>

### Console
<a name="registry-view-console"></a>

**Example**  

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, under **Discover**, choose **Registry**.

1. Choose the registry name from the **Registries** table.

1. The registry detail page displays the following collapsible sections:

   1.  **Registry details** — Displays Name, Status, Description, Auto-approval (Enabled or Disabled), Registry ARN, Last updated date, and Created date.

   1.  **Registry records** — Shows status summary counters (Total submitted, Pending approval, Approved, Deprecated, Rejected) and a records table for records submitted to this registry. From here you can create, view, or manage records.

   1.  **Discovery Authorization** (Inbound Authorization) — Shows the current authorization type (AWS\_IAM or CUSTOM\_JWT) and, for JWT-authorized registries, the JWT authorizer configuration.

   1.  **Sample code** — Provides sample code for common operations (create, approve, list, and discover records) that you can copy and adapt.

   1.  **Tags** — Shows the tags associated with the registry as a key-value table. To add, remove, or modify tags, choose **Edit** in this section to open the **Edit tags** page.

1. To modify the registry, choose **Edit**. To delete the registry, choose **Delete**.

1. To search or browse approved records in this registry, choose **Record directory** in the top-right of the page (or in the navigation pane). See [Get started with Agent Registry](registry-get-started.md) for the discovery walkthrough.

1. Open the [Amazon Bedrock AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the navigation pane, under **Discover**, choose **Registry**.

1. Choose the registry name from the **Registries** table.

1. The registry detail page has two tabs:

   1.  **Manage records** — View and manage registry records.

   1.  **Search records** — Search for approved records in the registry.

1. The **Registry details** section displays: Name, Status, Description, Auto-approval (Enabled or Disabled), Registry ARN, Last updated date, Created date.

1. The **Registry records** section shows status summary counters (Total submitted, Pending approval, Approved, Deprecated, Rejected) and a records table.

1. The **Search API Authorization** (Inbound Authorization) section shows the current authorization type.

### AWS CLI
<a name="registry-view-cli"></a>

**Example**  

```
aws agent-registry-control get-registry \
  --registry-id "<registryId>" \
  --region us-east-1
```

```
aws bedrock-agentcore-control get-registry \
  --registry-id "<registryId>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-view-sdk"></a>

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.get_registry(
    registryId='<registryId>'
)
print(f"Name: {response['name']}")
print(f"Status: {response['status']}")
print(f"ARN: {response['registryArn']}")
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.get_registry(
    registryId='<registryId>'
)
print(f"Name: {response['name']}")
print(f"Status: {response['status']}")
print(f"ARN: {response['registryArn']}")
```

## Update a registry
<a name="registry-update"></a>

### Console
<a name="registry-update-console"></a>

**Example**  

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, under **Discover**, choose **Registry**.

1. Select the radio button next to the registry you want to edit, then choose **Edit**. Alternatively, choose the registry name and then choose **Edit**.

1. On the **Edit registry** page, update any of the following:

   1.  **Name** — Change the registry name (same naming rules as creation).

   1.  **Description** — Under **Additional details**, update or add a description.

   1.  **Record approval** — Toggle **Auto-approval** on or off. Changes only affect records submitted after the update.

   1.  **Discovery Authorization** — For JWT-authorized registries, update the JWT authorizer configuration (allowed clients, audiences, scopes, or custom claims). The inbound authorization type itself (IAM or JWT) cannot be changed after the registry is created.

1. Choose **Save changes**.

1. Open the [Amazon Bedrock AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the navigation pane, under **Discover**, choose **Registry**.

1. Select the radio button next to the registry you want to edit, then choose **Edit**. Alternatively, choose the registry name and then choose **Edit**.

1. On the **Edit registry** page, update any of the following:

   1.  **Name** — Change the registry name (same naming rules as creation).

   1.  **Description** — Under **Additional details**, update or add a description.

   1.  **Record approval** — Toggle **Auto-approval** on or off. Changes only affect records submitted after the update.

1. Choose **Save changes**.

**Note**  
Tags are not edited from the **Edit registry** page. To modify tags, go to the registry detail page, choose **Edit** in the **Tags** section, add or remove tags on the **Edit tags** page, and choose **Save changes**. (Tags are only supported in the AWS Agent Registry console.)

**Note**  
Updating auto-approval config from OFF to ON only affects records submitted after the change. Existing records already 'Pending Approval' are not affected and must still be approved or rejected by calling UpdateRegistryRecordStatus API. Changing the config from ON to OFF only affects records that are published to 'Pending Approval' after the change is made.

**Note**  
The inbound authorization type (IAM or JWT) and the JWT discovery URL cannot be changed after the registry is created. For JWT-authorized registries, you can only update the authorizer configuration (allowed clients, audiences, scopes, custom claims).

### AWS CLI
<a name="registry-update-cli"></a>

**Example**  

```
aws agent-registry-control update-registry \
  --registry-id "<registryId>" \
  --description '{"optionalValue": "Updated description"}' \
  --region us-east-1
```

```
aws bedrock-agentcore-control update-registry \
  --registry-id "<registryId>" \
  --description '{"optionalValue": "Updated description"}' \
  --region us-east-1
```

### AWS SDK
<a name="registry-update-sdk"></a>

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.update_registry(
    registryId='<registryId>',
    description={'optionalValue': 'Updated description'}
)
print(f"Updated: {response['name']} - Status: {response['status']}")
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.update_registry(
    registryId='<registryId>',
    description={'optionalValue': 'Updated description'}
)
print(f"Updated: {response['name']} - Status: {response['status']}")
```

## Delete a registry
<a name="registry-delete"></a>

### Console
<a name="registry-delete-console"></a>

**Example**  

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, under **Discover**, choose **Registry**.

1. Select the radio button next to the registry you want to delete, then choose **Delete**.

1. In the confirmation dialog, review the warning: you must first delete all registry records before deleting the registry.

1. Type **delete** in the confirmation field.

1. Choose **Delete**.

1. Open the [Amazon Bedrock AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the navigation pane, under **Discover**, choose **Registry**.

1. Select the radio button next to the registry you want to delete, then choose **Delete**.

1. In the confirmation dialog, review the warning: you must first delete all registry records before deleting the registry.

1. Type **delete** in the confirmation field.

1. Choose **Delete**.

The registry status changes to **Deleting**. A success banner confirms when deletion completes.

### AWS CLI
<a name="registry-delete-cli"></a>

**Example**  

```
aws agent-registry-control delete-registry \
  --registry-id "<registryId>" \
  --region us-east-1
```

```
aws bedrock-agentcore-control delete-registry \
  --registry-id "<registryId>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-delete-sdk"></a>

**Example**  

```
import boto3

client = boto3.client('agent-registry-control')

response = client.delete_registry(
    registryId='<registryId>'
)
print(f"Status: {response['status']}")  # DELETING
```

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.delete_registry(
    registryId='<registryId>'
)
print(f"Status: {response['status']}")  # DELETING
```