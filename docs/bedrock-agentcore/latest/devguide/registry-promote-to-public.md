

# Promote a record to public discovery

When you promote a record to public discovery, an already-approved record becomes discoverable across organizational boundaries. You take an approved record, associate it with a verified Publisher, and a curator approves the association. This topic describes the preconditions, the association and approval steps, the discoverability rule, how updates are handled, and how to remove a record from public discovery.

The promote-to-public APIs are available only in the `agent-registry-control` namespace.

## Preconditions
<a name="registry-promote-preconditions"></a>

Before you promote a record, make sure the following are true:
+ The record exists and its status is `APPROVED`, so it is already discoverable within your organization. For more information, see [Curating the registry](registry-curating.md).
+ A Publisher exists and its verification status is `ACTIVE`. For more information, see [Publishers](registry-publishers.md).
+ The agent is deployed and serves its metadata at its endpoint. AWS Agent Registry does not host or route the agent.

## Associate a record with a Publisher
<a name="registry-promote-associate"></a>

To start promotion, associate the approved record with the verified Publisher by calling `AssociatePublisher`.

**Warning**  
Associating an approved record with a Publisher, and then having the association approved, makes the record’s content publicly discoverable to every AWS-authenticated caller. Before you promote a record, review its metadata and confirm that none of it is confidential.  
If your registry encrypts record content with a customer managed AWS KMS key, that encryption protects the content at rest only. When you promote a record, AWS Agent Registry reads the record’s content and publishes it to the public discovery plane, where any AWS-authenticated caller can retrieve it. At-rest encryption does not keep a promoted record private.

The association starts in `PUBLIC_ASSOCIATION_IN_PROGRESS`.

### Console
<a name="registry-promote-associate-console"></a>

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the registry that contains the record.

1. Choose the record you want to promote. The record must be in **Approved** status.

1. Choose **Associate with a publisher**.

1. For **Publisher**, choose a Publisher whose status is **Active**.

1. Choose **Associate**.

### AWS CLI
<a name="registry-promote-associate-cli"></a>

The following AWS CLI command associates the record with a verified Publisher. Replace `<recordId>` and `<publisherArn>` with your own values.

```bash
aws agent-registry-control associate-publisher \
  --record-id "<recordId>" \
  --publisher-arn "<publisherArn>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-promote-associate-sdk"></a>

The following example associates the record with a verified Publisher by using the AWS SDK for Python.

```python
import boto3

client = boto3.client('agent-registry-control')

response = client.associate_publisher(
    recordId='<recordId>',
    publisherArn='<publisherArn>'
)
print(f"Association status: {response['associationStatus']}")  # PUBLIC_ASSOCIATION_IN_PROGRESS
```

## Approve the public association
<a name="registry-promote-approval"></a>

The Publisher association is the second, independent approval gate. After you associate a record, the association waits for a curator to approve it. Approving the association is a decision about how the record is represented *outside* your organization. It is distinct from the record approval that governs internal discovery.

A curator approves or rejects the association by calling `UpdatePublisherAssociationApprovalStatus`. On approval, the association transitions to `PUBLIC_ASSOCIATION_APPROVED`, and the record enters the public discovery plane.

**Note**  
You can configure a registry so that public associations are approved automatically. For more information about the record-approval and public-association gates and how they combine, see [Create a registry](registry-create-manage.md#registry-create).

### Console
<a name="registry-promote-approval-console"></a>

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the registry.

1. Choose the record with a pending public association.

1. Choose **Approve association**.

1. Enter a **Reason** for the status change, and then choose **Update**.

### AWS CLI
<a name="registry-promote-approval-cli"></a>

The following AWS CLI command approves the public association.

```bash
aws agent-registry-control update-publisher-association-approval-status \
  --record-id "<recordId>" \
  --publisher-arn "<publisherArn>" \
  --approval-status PUBLIC_ASSOCIATION_APPROVED \
  --status-reason "Reviewed and approved for public discovery" \
  --region us-east-1
```

### AWS SDK
<a name="registry-promote-approval-sdk"></a>

The following example approves the public association by using the AWS SDK for Python.

```python
import boto3

client = boto3.client('agent-registry-control')

response = client.update_publisher_association_approval_status(
    recordId='<recordId>',
    publisherArn='<publisherArn>',
    approvalStatus='PUBLIC_ASSOCIATION_APPROVED',
    statusReason='Reviewed and approved for public discovery'
)
print(f"Association status: {response['associationStatus']}")  # PUBLIC_ASSOCIATION_APPROVED
```

## Discoverability rule
<a name="registry-promote-discoverability-rule"></a>

A record is publicly discoverable only when both of the following are true:
+ The record status is `APPROVED`.
+ The Publisher association status is `PUBLIC_ASSOCIATION_APPROVED`.

If either condition is not met, the record does not appear in public search. A record that is `APPROVED` but has no approved association stays discoverable within your organization only.

## Update a published record
<a name="registry-promote-updates"></a>

Editing a record that is already public creates a new draft revision while the approved revision stays discoverable, the same as for internal records. For more information, see [Record lifecycle](registry-record-lifecycle.md).

When a curator reviews the edited revision, the review re-checks the following:
+  **Metadata quality and safety**, the same checks as internal approval.
+  **Fit with the Publisher.** The record must remain appropriate to publish under the verified Publisher; a record repurposed for a different use might no longer fit.
+  **Continued fitness for public discovery.** 

If the curator approves the edited revision, the record keeps its existing association — you do not re-promote it. If the curator rejects the edited revision, you can revise and resubmit it, associate the record with a different Publisher (disassociate the current one first), or archive the record and create a new one.

## Remove a record from public discovery
<a name="registry-promote-disassociate"></a>

To remove a record from the public discovery plane, call `DisassociatePublisher`. Disassociation removes the record from public search immediately. Internal discoverability is unaffected — the record stays `APPROVED` and discoverable within your organization.

### AWS CLI
<a name="registry-promote-disassociate-cli"></a>

The following AWS CLI command removes the record from public search.

```bash
aws agent-registry-control disassociate-publisher \
  --record-id "<recordId>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-promote-disassociate-sdk"></a>

The following example removes the record from public search by using the AWS SDK for Python.

```python
import boto3

client = boto3.client('agent-registry-control')

client.disassociate_publisher(
    recordId='<recordId>'
)
```

## List Publisher associations
<a name="registry-promote-list"></a>

Use `ListPublisherAssociations` to review the records associated with a Publisher and the status of each association.

### AWS CLI
<a name="registry-promote-list-cli"></a>

The following AWS CLI command lists the Publisher associations.

```bash
aws agent-registry-control list-publisher-associations \
  --publisher-arn "<publisherArn>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-promote-list-sdk"></a>

The following example lists the Publisher associations by using the AWS SDK for Python.

```python
import boto3

client = boto3.client('agent-registry-control')

response = client.list_publisher_associations(
    publisherArn='<publisherArn>'
)
for association in response['associations']:
    print(association['associationStatus'])
```

## Notifications
<a name="registry-promote-notifications"></a>

Public-association events use the same notification mechanism as record approval. You can receive events — such as an association that is pending approval or an association that has been approved — through Amazon EventBridge and route them to your organization’s review and notification systems. For more information, see [Amazon EventBridge integration](registry-eventbridge.md).