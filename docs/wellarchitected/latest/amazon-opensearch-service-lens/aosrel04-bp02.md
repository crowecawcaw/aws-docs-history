# AOSREL04-BP02 Implement an Index State Management (ISM) policy

to generate snapshots for your crucial indices

Protect your critical Amazon OpenSearch Service indices by implementing an
ISM policy that generates snapshots for disaster recovery, which
helps you comply with regulatory requirements and simplify the
recovery process.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome:** Your crucial
indices are protected by an ISM policy that generates snapshots for
disaster recovery.

**Benefits of establishing this best
practice:** By establishing a manual snapshot repository
and using ISM and SM, you maintain full control over your Amazon OpenSearch Service data, and you can comply with regulatory
requirements and data retention policies. Additionally, it can
simplify disaster recovery processes by having a centralized
repository for snapshots.

## Implementation guidance

ISM automates index lifecycle tasks, including alias rollovers,
snapshots, storage tier transitions, and deletion of old indices.

It is recommended that you review [AOSPERF01 and AOSPERF02](architecture-selection.md "architecture-selection.md") to
familiarize yourself with sharding strategies before you implement
ISM policies.

Additionally, consult
[Index
State Management in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/ism.md "../../../opensearch-service/latest/developerguide/ism.md"),
[Tutorial:
Automating Index State Management processes](../../../opensearch-service/latest/developerguide/ism-tutorial.md "../../../opensearch-service/latest/developerguide/ism-tutorial.md") and
[Index
State Management](https://opensearch.org/docs/latest/im-plugin/ism/index/ "https://opensearch.org/docs/latest/im-plugin/ism/index/") pages for samples and full details about
implementing ISM policies.

### Implementation steps

- Open OpenSearch Dashboards for your domain.
- From the left sidebar, select **Index Management**, then
  **Create policy**.
- Use the
  [visual
  editor](https://opensearch.org/docs/latest/im-plugin/ism/index/#visual-editor "https://opensearch.org/docs/latest/im-plugin/ism/index/#visual-editor") or
  [JSON
  editor](https://opensearch.org/docs/latest/im-plugin/ism/index/#json-editor "https://opensearch.org/docs/latest/im-plugin/ism/index/#json-editor") to create policies. We recommend using the
  visual editor as it offers a more structured way of defining
  policies.
- After you create a policy, attach it to one or more indexes:

```
POST _plugins/_ism/add/my-index
        {
        "policy_id": "my-policy-id"
        }
```

## Resources

- [Creating
  index snapshots in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/managedomains-snapshots.md "../../../opensearch-service/latest/developerguide/managedomains-snapshots.md")
- [Registering
  a manual snapshot repository](../../../opensearch-service/latest/developerguide/managedomains-snapshots.md#managedomains-snapshot-registerdirectory "../../../opensearch-service/latest/developerguide/managedomains-snapshots.md#managedomains-snapshot-registerdirectory")
- [Take
  manual snapshots and restore in a different domain spanning
  across various Regions and accounts in Amazon OpenSearch Service](https://aws.amazon.com/blogs/big-data/take-manual-snapshots-and-restore-in-a-different-domain-spanning-across-various-regions-and-accounts-in-amazon-opensearch-service/ "https://aws.amazon.com/blogs/big-data/take-manual-snapshots-and-restore-in-a-different-domain-spanning-across-various-regions-and-accounts-in-amazon-opensearch-service/")
