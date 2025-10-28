# Get started with Amazon MSK

encryption

When creating an MSK cluster, you can specify encryption settings in JSON format. The following is an example.

```
{
   "EncryptionAtRest": {
       "DataVolumeKMSKeyId": "arn:aws:kms:us-east-1:123456789012:key/abcdabcd-1234-abcd-1234-abcd123e8e8e"
    },
   "EncryptionInTransit": {
        "InCluster": true,
        "ClientBroker": "TLS"
    }
}
```

For `DataVolumeKMSKeyId`, you can specify a [customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") or the
AWS managed key for MSK in your account
(`alias/aws/kafka`).
If you don't specify `EncryptionAtRest`, Amazon MSK still encrypts your data at
rest under the AWS managed key. To determine which key your cluster is using, send a
`GET` request or invoke the `DescribeCluster` API operation.

For `EncryptionInTransit`, the default value of `InCluster` is
true, but you can set it to false if you don't want Amazon MSK to encrypt your data as it
passes between brokers.

To specify the encryption mode for data in transit between clients and brokers, set
`ClientBroker` to one of three values: `TLS`,
`TLS_PLAINTEXT`, or `PLAINTEXT`.

###### Topics

- [Specify encryption settings when creating a Amazon MSK cluster](msk-working-with-encryption-cluster-create.md "msk-working-with-encryption-cluster-create.md")
- [Test Amazon MSK TLS encryption](msk-working-with-encryption-test-tls.md "msk-working-with-encryption-test-tls.md")
