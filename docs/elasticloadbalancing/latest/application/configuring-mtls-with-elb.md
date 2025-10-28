# Configuring mutual TLS on an Application Load Balancer

To use mutual TLS passthrough mode, you need only configure the listener to accept any
certificates from clients. When you use mutual TLS passthrough,
the Application Load Balancer sends the whole client certificate chain to the target using HTTP headers, which enables you to implement
corresponding authentication and authorization logic in your application. For more information, see
[Create an HTTPS listener for your Application Load Balancer](create-https-listener.md "create-https-listener.md").

When you use mutual TLS in verify mode, the Application Load Balancer performs X.509 client certificate authentication
for clients when a load balancer negotiates TLS connections.

To utilize mutual TLS verify mode, perform the following:

- Create a new trust store resource.
- Upload your certificate authority (CA) bundle and, optionally, revocation lists.
- Attach the trust store to the listener that is configured to verify client certificates.
  Use the following procedures to configure mutual TLS verify mode on your Application Load Balancer.

###### Tasks

- [Create a trust store](#create-trust-store "#create-trust-store")
- [Associate a trust store](#associate-trust-store "#associate-trust-store")
- [Replace a CA certificate bundle](#replace-ca-cert-bundle "#replace-ca-cert-bundle")
- [Add a certificate revocation list](#add-cert-revocation-list "#add-cert-revocation-list")
- [Delete a certificate revocation list](#delete-cert-revocation-list "#delete-cert-revocation-list")
- [Delete a trust store](#delete-trust-store "#delete-trust-store")

## Create a trust store

If you add a trust store when you create a load balancer or listener, the trust store
is automatically associated with the new listener. Otherwise, you must associate it with a
listener yourself.

###### Prerequisites

- To create a trust store, you must have a certificate bundle from your Certificate Authority (CA).

Console
The following example creates a trust store using the **Trust Store**
portion of the console. Alternatively, you can create the trust store when you create
an HTTP listener.

###### To create a trust store

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Trust Stores**.
3. Choose **Create trust store**.
4. **Trust store configuration**
   1. For **Trust store name**, enter a name for your trust store.
   2. For **Certificate authority bundle**, enter the Amazon S3 path to the ca certificate bundle to use.
   3. (Optional) Use **Object version** to select a previous version of the
      ca certificate bundle. Otherwise, the current version is used.

5. (Optional) For **Revocations**, you can add a certificate revocation list to your trust store.
   1. Choose **Add new CRL** and enter the location of the certificate revocation list in Amazon S3.
   2. (Optional) Use **Object version** to select a previous version of the certificate revocation list.
      Otherwise, the current version is used.

6. (Optional) Expand **Trust store tags** and enter up to 50 tags for your trust store.
7. Choose **Create trust store**.

AWS CLI

###### To create a trust store

Use the [create-trust-store](../../../cli/latest/reference/elbv2/create-trust-store.md "../../../cli/latest/reference/elbv2/create-trust-store.md") command.

```
aws elbv2 create-trust-store \
    --name `my-trust-store` \
    --ca-certificates-bundle-s3-bucket `amzn-s3-demo-bucket` \
    --ca-certificates-bundle-s3-key `certificates/ca-bundle.pem`
```

CloudFormation

###### To create a trust store

Define a resource of type [AWS::ElasticLoadBalancingV2::TrustStore](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-truststore.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-truststore.md").

```
Resources:
  myTrustStore:
    Type: 'AWS::ElasticLoadBalancingV2::TrustStore'
    Properties:
      Name: `my-trust-store`
      CaCertificatesBundleS3Bucket: `amzn-s3-demo-bucket`
      CaCertificatesBundleS3Key: `certificates/ca-bundle.pem`
```

## Associate a trust store

After you create a trust store, you must associate it with a listener before your
Application Load Balancer can begin using the trust store. You can have only one trust store associated to
each of your secure listeners, but one trust store can be associated to
multiple listeners.

Console
You can associate a trust store with an existing listener, as shown in the following
procedure. Alternatively, you can associate a trust store while creating an HTTPS
listener. For more information, see [Create an
HTTPS listener](create-https-listener.md "create-https-listener.md").

###### To associate a trust store

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer.
4. On the **Listeners and rules** tab, choose the link in the
   **Protocol:Port** column to open the details page
   for the secure listener.
5. On the **Security** tab, choose **Edit secure listener
   settings**.
6. If mutual TLS is not enabled, select **Mutual authentication (mTLS)**
   under **Client certificate handling** and then choose
   **Verify with trust store**.
7. For **Trust store**, choose the trust store.
8. Choose **Save changes**.

AWS CLI

###### To associate a trust store

Use the [modify-listener](../../../cli/latest/reference/elbv2/modify-listener.md "../../../cli/latest/reference/elbv2/modify-listener.md") command.

```
aws elbv2 modify-listener \
    --listener-arn `listener-arn` \
    --mutual-authentication "Mode=verify,TrustStoreArn=`trust-store-arn`"
```

CloudFormation

###### To associate a trust store

Update the [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md") resource.

```
Resources:
  myHTTPSListener:
    Type: 'AWS::ElasticLoadBalancingV2::Listener'
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: HTTPS
      Port: 443
      DefaultActions:
        - Type: "forward"
          TargetGroupArn: !Ref myTargetGroup
      SslPolicy: ELBSecurityPolicy-TLS13-1-2-2021-06
      Certificates:
        - CertificateArn: certificate-arn
      MutualAuthentication:
        - Mode: verify
          TrustStoreArn: `trust-store-arn`
```

## Replace a CA certificate bundle

The CA certificate bundle is a required component of the trust store.
It's a collection of trusted root and intermediate certificates that have
been validated by a certificate authority. These validated certificates
ensure the client can trust the certificate being presented is owned by
the load balancer.

A trust store can only contain one CA certificate bundle at a time, but
you can replace the CA certificate bundle at any time after the trust store
is created.

Console

###### To replace a CA certificate bundle

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Trust Stores**.
3. Select the trust store.
4. Choose **Actions**, **Replace CA bundle**.
5. On the **Replace CA bundle** page, under **Certificate
   authority bundle**, enter the Amazon S3 location of the desired CA bundle.
6. (Optional) Use **Object version** to select a previous version
   of the certificate revocation list. Otherwise, the current version is used.
7. Select **Replace CA bundle**.

AWS CLI

###### To replace a CA certificate bundle

Use the [modify-trust-store](../../../cli/latest/reference/elbv2/modify-trust-store.md "../../../cli/latest/reference/elbv2/modify-trust-store.md") command.

```
aws elbv2 modify-trust-store \
    --trust-store-arn `trust-store-arn` \
    --ca-certificates-bundle-s3-bucket `amzn-s3-demo-bucket-new` \
    --ca-certificates-bundle-s3-key `certificates/new-ca-bundle-pem`
```

CloudFormation

###### To update the CA certificate bundle

Define a resource of type [AWS::ElasticLoadBalancingV2::TrustStore](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-truststore.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-truststore.md").

```
Resources:
  myTrustStore:
    Type: 'AWS::ElasticLoadBalancingV2::TrustStore'
    Properties:
      Name: my-trust-store
      CaCertificatesBundleS3Bucket: `amzn-s3-demo-bucket-new`
      CaCertificatesBundleS3Key: `certificates/new-ca-bundle.pem`
```

## Add a certificate revocation list

Optionally, you can create a certificate revocation list for a trust store.
Revocation lists are released by certificate authorities and contain data
for certificates that have been revoked. Application Load Balancers only support certificate
revocation lists in the PEM format.

When a certificate revocation list is added to a trust store, it's given a
revocation ID. The revocation IDs increase for every revocation list added to
the trust store, and they can't be changed.

Application Load Balancers can't revoke certificates that have a negative serial number within
a certificate revocation list.

Console

###### To add a revocation list

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Trust Stores**.
3. Select the trust store to view it's details page.
4. On the **Certificate revocation lists** tab, select
   **Actions**, **Add revocation list**.
5. On the **Add revocation list** page, under
   **Certificate revocation list** enter the Amazon S3 location
   of the desired certificate revocation list
6. (Optional) Use **Object version** to select a previous version
   of the certificate revocation list. Otherwise the current version is used.
7. Select **Add revocation list**

AWS CLI

###### To add a revocation list

Use the [add-trust-store-revocations](../../../cli/latest/reference/elbv2/add-trust-store-revocations.md "../../../cli/latest/reference/elbv2/add-trust-store-revocations.md") command.

```
aws elbv2 add-trust-store-revocations \
    --trust-store-arn `trust-store-arn` \
    --revocation-contents "S3Bucket=`amzn-s3-demo-bucket`,S3Key=`crl/revoked-list.crl`,RevocationType=CRL"
```

CloudFormation

###### To add a revocation list

Define a resource of type [AWS::ElasticLoadBalancingV2::TrustStoreRevocation](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-truststorerevocation.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-truststorerevocation.md").

```
Resources:
  myRevocationContents:
    Type: 'AWS:ElasticLoadBalancingV2::TrustStoreRevocation'
    Properties:
      TrustStoreArn: !Ref myTrustStore
      RevocationContents:
        - RevocationType: CRL
          S3Bucket: `amzn-s3-demo-bucket`
          S3Key: `crl/revoked-list.crl`
```

## Delete a certificate revocation list

When you no longer need a certificate revocation list, you can delete it. When you
delete a certificate revocation list from a trust store, it's revocation ID is also
deleted and is not reused for the life of the trust store.

Console

###### To delete a revocation list

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Trust Stores**.
3. Select the trust store.
4. On the **Certificate revocation lists** tab, choose **Actions**,
   **Delete revocation list**.
5. When prompted for confirmation, enter `confirm`.
6. Choose **Delete**.

AWS CLI

###### To delete a revocation list

Use the [remove-trust-store-revocations](../../../cli/latest/reference/elbv2/remove-trust-store-revocations.md "../../../cli/latest/reference/elbv2/remove-trust-store-revocations.md") command.

```
aws elbv2 remove-trust-store-revocations \
    --trust-store-arn `trust-store-arn` \
    --revocation-ids `id-1` `id-2` `id-3`
```

## Delete a trust store

When you no longer have use for a trust store, you can delete it.
You can't delete a trust store that is associated with a listener.

Console

###### To delete a trust store

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Trust Stores**.
3. Select the trust store.
4. Choose **Delete**.
5. When prompted for confirmation, enter `confirm` and
   then choose **Delete**.

AWS CLI

###### To delete a trust store

Use the [delete-trust-store](../../../cli/latest/reference/elbv2/delete-trust-store.md "../../../cli/latest/reference/elbv2/delete-trust-store.md") command.

```
aws elbv2 delete-trust-store \
    --trust-store-arn `trust-store-arn`
```
