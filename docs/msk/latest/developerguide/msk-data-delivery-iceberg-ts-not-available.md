

# Channel not available on cluster
<a name="msk-data-delivery-iceberg-ts-not-available"></a>
+ **Symptom:** The Channel tab is not visible, or `CreateChannel` returns an error.
+ **Causes:** Cluster uses Standard brokers; cluster is Amazon MSK Serverless; Region doesn't support Amazon MSK Express brokers.
+ **Resolution:** Channel is only available on Amazon MSK Express brokers within Amazon MSK Provisioned clusters. Verify the cluster type under **Cluster settings**. If needed, create a new Amazon MSK Provisioned cluster with Express brokers.