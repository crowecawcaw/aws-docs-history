

# AOSOPS01-BP01 Employ Index State Management (ISM) to manage logs or time series data
<a name="aosops01-bp01"></a>

 Manage large volumes of log or time series data efficiently with automated index lifecycle tasks. 

 **Level of risk exposed if this best practice is not established**: High 

 **Desired outcome**: ISM is employed to manage the life-cycle of logs or time series data. 

 **Benefits of establishing this best practice:** 
+  **Automate index lifecycle tasks:** Employing ISM can automate index lifecycle tasks such as alias rollovers, snapshots, storage tier transitions, and deletion of old indices, which helps reduce manual effort and improves efficiency and reliability of your domain. 
+  **Manage log or time series data:** ISM is particularly useful for managing large volumes of log or time series data by automating the process of transitioning old indices to lower-cost storage tiers or deleting them when they are no longer needed. 

## Implementation guidance
<a name="implementation-guidance"></a>

 ISM automates index lifecycle tasks, including alias rollovers, snapshots, storage tier transitions, and deletion of old indices. 

 It is recommended that you review [AOSPERF01 and AOSPERF02](https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/architecture-selection.html) to familiarize yourself with sharding strategies before you implement ISM policies. 

 Additionally, consult [Index State Management in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ism.html), [Tutorial: Automating Index State Management processes](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ism-tutorial.html) and [Index State Management](https://opensearch.org/docs/latest/im-plugin/ism/index/) pages for samples and full details about implementing ISM policies. 

### Implementation steps
<a name="implementation-steps"></a>
+  Open OpenSearch Dashboards for your domain. 
+  From the left sidebar, select **Index Management**, then **Create policy**. 
+  Use the [visual editor](https://opensearch.org/docs/latest/im-plugin/ism/index/#visual-editor) or [JSON editor](https://opensearch.org/docs/latest/im-plugin/ism/index/#json-editor) to create policies. We recommend using the visual editor as it offers a more structured way of defining policies. 
+  After you create a policy, attach it to one or more indexes: 

```
POST _plugins/_ism/add/my-index
        {
        "policy_id": "my-policy-id"
        }
```

## Resources
<a name="resources"></a>
+  [Index State Management in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ism.html) 
+  [Tutorial: Automating Index State Management processes](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ism-tutorial.html) 
+  [Index State Management](https://opensearch.org/docs/latest/im-plugin/ism/index/) 