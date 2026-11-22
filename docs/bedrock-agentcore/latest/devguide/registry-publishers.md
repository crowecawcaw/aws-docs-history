

# Publishers

A Publisher is a verified public identifier under which your organization publishes records for public discovery. This topic explains what a Publisher is, how you prove that your organization owns the identifier, and how a Publisher moves through verification.

**Note**  
In AWS Agent Registry, the word *Publisher* names two different things. The **Publisher persona** is a builder who creates and submits records (see [Key Personas](registry-concepts.md#registry-concept-personas)). The **Publisher construct** described in this topic is a verified public identifier used for public discovery. They are related — a builder publishes records, and a verified identifier is what those records are published under — but they are not the same object. This topic is about the construct.

## What a Publisher is
<a name="registry-publishers-what-is"></a>

A Publisher gives partners and developers in other organizations a verifiable, globally unique name that they can trust. It separates the human-readable record name inside your registry from the domain-based public identifier that external callers see. When you promote a record to public discovery, you publish it under a Publisher, and external callers can confirm which verified identifier stands behind the record.

You create and manage a Publisher with the `CreatePublisher`, `GetPublisher`, `ListPublishers`, and `DeletePublisher` APIs. The `ValidatePublisher` API drives verification, as described in the following sections.

**Note**  
For AWS Agent Registry quotas, including the number of Publishers per account and records per Publisher, see [Quotas for Amazon Bedrock AgentCore](bedrock-agentcore-limits.md).

## Publisher identifier
<a name="registry-publishers-identifier-types"></a>

A Publisher is identified by a domain name with at least two dot-separated levels, for example `example.com`. AWS Agent Registry verifies that your organization controls the domain through an ACME DNS-01 challenge, as described in the following section.

## Prove ownership with ACME DNS-01
<a name="registry-publishers-verification"></a>

Your organization proves that it controls the domain by using the ACME DNS-01 challenge. The flow has three parts:

1. You call `CreatePublisher` with the domain. AWS Agent Registry creates the Publisher in the `ACTION_REQUIRED` state and returns a DNS challenge. The challenge is a TXT record name (based on `_acme-challenge`) and a value.

1. An administrator adds the returned `_acme-challenge` TXT record to the domain’s DNS zone at your DNS provider.

1.  AWS Agent Registry polls DNS for the TXT record at a fixed interval. When it detects the expected value, the Publisher transitions to the verified state.

To re-check verification without waiting for the next polling cycle — for example, right after you add the TXT record — call `ValidatePublisher` to trigger an immediate re-check.

**Note**  
Verification confirms that your organization controls the domain. It does not grant AWS Agent Registry any access to your domain, your DNS zone, or the agent that you later publish under the Publisher.

## Verification states
<a name="registry-publishers-verification-states"></a>

A Publisher reports its verification status through the following states:
+  `ACTION_REQUIRED` — The Publisher needs action before it can be used. Add the `_acme-challenge` TXT record from `CreatePublisher` or `GetPublisher` to your domain’s DNS zone to prove that you control the domain. A newly created Publisher starts in this state. After you add the record, call `ValidatePublisher` to trigger an immediate re-check.
+  `ACTIVE` — Verification succeeded. The Publisher is verified, and you can associate approved records with it to promote them to public discovery.
+  `FAILED` — Verification did not succeed. Check the `_acme-challenge` TXT record in your domain’s DNS zone, then call `ValidatePublisher` to retry.
+  `SUSPENDED` — The Publisher is suspended and can’t be used for public discovery until it is restored.
+  `DELETING` — The Publisher is being deleted.

## Separation of duties
<a name="registry-publishers-separation-of-duties"></a>

Creating and verifying a Publisher is a distinct responsibility from publishing records under it.
+ The **administrator** owns the domains and DNS zones, creates the Publisher, and completes the DNS-01 challenge. For more information, see [Key Personas](registry-concepts.md#registry-concept-personas).
+ The **builder** (the Publisher persona) later associates an approved record with the verified Publisher. This is a separate step, described in [Promote a record to public discovery](registry-promote-to-public.md).

Because AWS Agent Registry is discovery-only, routing and hosting of the agent remain the builder’s responsibility outside the registry.

## Create a Publisher
<a name="registry-publishers-create"></a>

The Publisher APIs are available only in the `agent-registry-control` namespace.

### Console
<a name="registry-publishers-create-console"></a>

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, choose **Publishers**.

1. Choose **Create publisher**.

1. For **Domain**, enter a domain name with at least two levels, such as `example.com`.

1. Choose **Create publisher**. The console displays the DNS challenge to complete for a domain Publisher.

### AWS CLI
<a name="registry-publishers-create-cli"></a>

The following AWS CLI command creates a Publisher.

```bash
aws agent-registry-control create-publisher \
  --value '{"domain":"example.com"}' \
  --region us-east-1
```

### AWS SDK
<a name="registry-publishers-create-sdk"></a>

The following example creates a Publisher by using the AWS SDK for Python.

```python
import boto3

client = boto3.client('agent-registry-control')

response = client.create_publisher(
    value={'domain': 'example.com'}
)
print(f"Publisher ARN: {response['publisherArn']}")
print(f"Status: {response['status']}")  # ACTION_REQUIRED
print(f"DNS-01 challenge to publish: {response['domainChallenge']}")
```

### AWS CloudFormation
<a name="registry-publishers-create-cloudformation"></a>

CloudFormation keeps the `AWS::AgentRegistry::Publisher` resource in `CREATE_IN_PROGRESS` until the Publisher status becomes `ACTIVE`. CloudFormation doesn’t expose resource attributes or stack outputs during creation. Use the AWS Agent Registry API to retrieve the DNS challenge while CloudFormation waits.

Complete domain verification within 36 hours to prevent CloudFormation from timing out. The principal that retrieves the challenge needs the `agent-registry:ListPublishers` and `agent-registry:GetPublisher` permissions.

For template syntax and resource properties, see [AWS::AgentRegistry::Publisher](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-agentregistry-publisher.html) in the * AWS CloudFormation Template Reference*.

This procedure verifies domain ownership for a Publisher that you create with CloudFormation. When verification succeeds, the resource reaches `CREATE_COMPLETE`.

1. Create the CloudFormation stack.

1. Wait until the Publisher resource reaches `CREATE_IN_PROGRESS`.

1. To find the Publisher ARN, replace `example.com` with the domain in your CloudFormation template, and then run the following command:

   ```bash
   aws agent-registry-control list-publishers \
     --region us-east-1 \
     --query "items[?value.domain=='example.com'].publisherArn | [0]" \
     --output text
   ```

1. To retrieve the DNS challenge, replace `<publisherArn>` with the Publisher ARN from the previous step, and then run the following command:

   ```bash
   aws agent-registry-control get-publisher \
     --publisher-arn "<publisherArn>" \
     --region us-east-1 \
     --query '{Status: status, RecordName: domainChallenge.recordName, RecordValue: domainChallenge.recordValue}'
   ```

1. At your DNS provider, create a TXT record that uses `RecordName` as the record name and `RecordValue` as the record value.

1. (Optional) After the DNS record propagates, call `ValidatePublisher` to trigger an immediate verification check.

1. Wait for the Publisher status to become `ACTIVE`.

Expected result: The Publisher status is `ACTIVE`, and the CloudFormation resource reaches `CREATE_COMPLETE`.

## Verify a Publisher
<a name="registry-publishers-verify"></a>

After you add the `_acme-challenge` TXT record, call `ValidatePublisher` to re-check verification immediately instead of waiting for the next polling cycle. In the following examples, replace `<publisherArn>` with the Publisher ARN.

### AWS CLI
<a name="registry-publishers-verify-cli"></a>

The following AWS CLI command re-checks Publisher verification.

```bash
aws agent-registry-control validate-publisher \
  --publisher-arn "<publisherArn>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-publishers-verify-sdk"></a>

The following example re-checks Publisher verification by using the AWS SDK for Python.

```python
import boto3

client = boto3.client('agent-registry-control')

response = client.validate_publisher(
    publisherArn='<publisherArn>'
)
print(f"Status: {response['status']}")
```

## View Publishers
<a name="registry-publishers-view"></a>

Use `GetPublisher` to retrieve one Publisher and its verification status, or `ListPublishers` to list the Publishers in your account. In the following examples, replace `<publisherArn>` with the Publisher ARN.

### AWS CLI
<a name="registry-publishers-view-cli"></a>

The following AWS CLI commands retrieve a Publisher and list the Publishers in your account.

```bash
aws agent-registry-control get-publisher \
  --publisher-arn "<publisherArn>" \
  --region us-east-1

aws agent-registry-control list-publishers \
  --region us-east-1
```

### AWS SDK
<a name="registry-publishers-view-sdk"></a>

The following example retrieves a Publisher by using the AWS SDK for Python.

```python
import boto3

client = boto3.client('agent-registry-control')

response = client.get_publisher(
    publisherArn='<publisherArn>'
)
print(f"{response['publisherArn']} - {response['status']}")
```

## Delete a Publisher
<a name="registry-publishers-delete"></a>

Use `DeletePublisher` to remove a Publisher. Before you delete a Publisher, disassociate any records that are published under it. For more information, see [Promote a record to public discovery](registry-promote-to-public.md). In the following examples, replace `<publisherArn>` with the Publisher ARN.

### AWS CLI
<a name="registry-publishers-delete-cli"></a>

The following AWS CLI command deletes a Publisher.

```bash
aws agent-registry-control delete-publisher \
  --publisher-arn "<publisherArn>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-publishers-delete-sdk"></a>

The following example deletes a Publisher by using the AWS SDK for Python.

```python
import boto3

client = boto3.client('agent-registry-control')

client.delete_publisher(
    publisherArn='<publisherArn>'
)
```