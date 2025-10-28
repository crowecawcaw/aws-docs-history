# AOSOPS01-BP01 Employ Index State Management (ISM) to manage

logs or time series data

Manage large volumes of log or time series data efficiently with
automated index lifecycle tasks.

**Level of risk exposed if this best practice
is not established**: High

**Desired outcome**: ISM is employed
to manage the life-cycle of logs or time series data.

**Benefits of establishing this best
practice:**

- **Automate index lifecycle
  tasks:** Employing ISM can automate index lifecycle
  tasks such as alias rollovers, snapshots, storage tier
  transitions, and deletion of old indices, which helps reduce
  manual effort and improves efficiency and reliability of your
  domain.
- **Manage log or time series
  data:** ISM is particularly useful for managing large
  volumes of log or time series data by automating the process of
  transitioning old indices to lower-cost storage tiers or
  deleting them when they are no longer needed.

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

- [Index
  State Management in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/ism.md "../../../opensearch-service/latest/developerguide/ism.md")
- [Tutorial:
  Automating Index State Management processes](../../../opensearch-service/latest/developerguide/ism-tutorial.md "../../../opensearch-service/latest/developerguide/ism-tutorial.md")
- [Index
  State Management](https://opensearch.org/docs/latest/im-plugin/ism/index/ "https://opensearch.org/docs/latest/im-plugin/ism/index/")
