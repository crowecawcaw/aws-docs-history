# Data encryption using KMS

ROSA uses AWS KMS to securely manage keys for encrypted data.
Control plane, infrastructure, and worker node volumes are encrypted by default using the AWS managed KMS key provided by Amazon EBS.
This KMS key has the alias `aws/ebs`.
Persistent volumes that use the default gp3 storage class are also encrypted by default using this KMS key.

Newly created ROSA clusters are configured to use the default gp3 storage class to encrypt persistent volumes.
Persistent volumes created by using any other storage class are only encrypted if the storage class is configured to be encrypted.
For more information about ROSA pre-built storage classes, see [Configuring persistent storage](https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/storage/configuring-persistent-storage#persistent-storage-aws "https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/storage/configuring-persistent-storage#persistent-storage-aws") in the Red Hat documentation.

During cluster creation, you can choose to encrypt the persistent volumes in your cluster using the default Amazon EBS-provided key, or specify your own customer managed symmetric KMS key.
For more information about creating keys, see [Creating symmetric encryption KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS KMS Developer Guide_.

You can also encrypt persistent volumes for individual containers within a cluster by defining a KMS key.
This is useful when you have explicit compliance and security guidelines when deploying to AWS.
For more information, see [Encrypting container persistent volumes on AWS with a KMS key](https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/storage/configuring-persistent-storage#aws-container-persistent-volumes-encrypt_persistent-storage-aws "https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/storage/configuring-persistent-storage#aws-container-persistent-volumes-encrypt_persistent-storage-aws") in the Red Hat documentation.

The following points should be considered when encrypting persistent volumes using your own KMS keys:

- When you use KMS encryption with your own KMS key, the key must exist in the same AWS Region as your cluster.
- There is a cost associated with creating and using your own KMS keys. For more information, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").
