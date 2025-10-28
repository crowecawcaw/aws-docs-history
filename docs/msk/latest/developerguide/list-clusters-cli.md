# List clusters using the AWS CLI

To get a bootstrap broker for an Amazon MSK cluster, you need the cluster Amazon
Resource Name (ARN). If you don't have the ARN for your cluster, you can find it by
listing all clusters. See [Get the bootstrap brokers for an
Amazon MSK cluster](msk-get-bootstrap-brokers.md "msk-get-bootstrap-brokers.md").

```
aws kafka list-clusters
```
