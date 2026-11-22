

# Configure mutual TLS

When you use mutual TLS in verify mode, the load balancer performs X.509v3 client certificate authentication for clients when it negotiates TLS connections.

To utilize mutual TLS verify mode, perform the following:

1. Create a new trust store resource.

1. Upload your certificate authority (CA) bundle and, optionally, revocation lists.

1. Attach the trust store to the listener that is configured to verify client certificates.

Use the following procedures to configure mutual TLS verify mode on your Network Load Balancer.

**Topics**
+ [Create a trust store](#create-trust-store-mtls)
+ [Associate a trust store](#associate-trust-store-mtls)
+ [Replace a CA certificate bundle](#replace-ca-bundle-mtls)
+ [Add a certificate revocation list](#add-crl-mtls)
+ [Delete a certificate revocation list](#delete-crl-mtls)
+ [Delete a trust store](#delete-trust-store-mtls)
+ [Create a TLS listener with mTLS](#create-tls-listener-mtls)
+ [Modify a TLS listener with mTLS](#modify-tls-listener-mtls)
+ [Advanced mTLS listener settings](#advanced-mtls-listener-settings)

## Create a trust store
<a name="create-trust-store-mtls"></a>

If you add a trust store when you create a load balancer or listener, the trust store is automatically associated with the new listener. Otherwise, you must associate it with a listener yourself.

**Prerequisites**
+ To create a trust store, you must have a certificate bundle from your Certificate Authority (CA).

------
#### [ AWS Management Console ]

The following example creates a trust store using the Trust Store portion of the console. Alternatively, you can create the trust store when you create a TLS listener.

**To create a trust store**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, choose **Trust Stores**.

1. Choose **Create trust store**.

1. **Trust store configuration**

   1. For **Trust store name**, enter a name for your trust store.

   1. For **Certificate authority bundle**, enter the Amazon S3 path to the ca certificate bundle to use.

   1. (Optional) Use **Object version** to select a previous version of the ca certificate bundle. Otherwise, the current version is used.

1. (Optional) For **Revocations**, you can add a certificate revocation list to your trust store.

   1. Choose **Add new CRL** and enter the location of the certificate revocation list in Amazon S3.

   1. (Optional) Use **Object version** to select a previous version of the certificate revocation list. Otherwise, the current version is used.

1. (Optional) Expand **Trust store tags** and enter up to 50 tags for your trust store.

1. Choose **Create trust store**.

------
#### [ AWS CLI ]

**To create a trust store**  
Use the [create-trust-store](https://docs.aws.amazon.com/cli/latest/reference/elbv2/create-trust-store.html) command.

```
aws elbv2 create-trust-store \
    --name {{my-trust-store}} \
    --ca-certificates-bundle-s3-bucket {{amzn-s3-demo-bucket}} \
    --ca-certificates-bundle-s3-key {{certificates/ca-bundle.pem}}
```

------
#### [ AWS CloudFormation ]

**To create a trust store**  
Define a resource of type `AWS::ElasticLoadBalancingV2::TrustStore`.

```yaml
Resources:
  myTrustStore:
    Type: 'AWS::ElasticLoadBalancingV2::TrustStore'
    Properties:
      Name: {{my-trust-store}}
      CaCertificatesBundleS3Bucket: {{amzn-s3-demo-bucket}}
      CaCertificatesBundleS3Key: {{certificates/ca-bundle.pem}}
```

------

## Associate a trust store
<a name="associate-trust-store-mtls"></a>

After you create a trust store, you must associate it with a listener before your Network Load Balancer can begin using the trust store. You can have only one trust store associated to each of your TLS listeners, but one trust store can be associated to multiple listeners.

------
#### [ AWS Management Console ]

**To associate a trust store with a listener**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Load Balancers**.

1. Select the name of the load balancer to open its details page.

1. On the **Listeners and rules** tab, select the TLS listener, and then choose **Edit listener**.

1. Under **Client certificate handling**, select **Mutual authentication (mTLS)**, and then choose **Verify with trust store**.

1. For **Trust store**, choose your trust store.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

**To associate a trust store with an existing listener**  
Use the [modify-listener](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-listener.html) command with the `--mutual-authentication` argument.

```
aws elbv2 modify-listener \
    --listener-arn {{listener-arn}} \
    --mutual-authentication Mode=verify,TrustStoreArn={{trust-store-arn}}
```

------
#### [ AWS CloudFormation ]

Update the `AWS::ElasticLoadBalancingV2::Listener` resource.

```yaml
Resources:
  myTLSListener:
    Type: 'AWS::ElasticLoadBalancingV2::Listener'
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: TLS
      Port: 443
      DefaultActions:
        - Type: "forward"
          TargetGroupArn: !Ref myTargetGroup
      SslPolicy: ELBSecurityPolicy-TLS13-1-2-2021-06
      Certificates:
        - CertificateArn: {{certificate-arn}}
      MutualAuthentication:
        Mode: verify
        TrustStoreArn: {{trust-store-arn}}
```

------

## Replace a CA certificate bundle
<a name="replace-ca-bundle-mtls"></a>

The CA certificate bundle is a required component of the trust store. It is a collection of trusted root and intermediate certificates that have been validated by a certificate authority. These validated certificates ensure that the client can trust that the certificate being presented is owned by the load balancer. A trust store can only contain one CA certificate bundle at a time, but you can replace the CA certificate bundle at any time after the trust store is created.

------
#### [ AWS Management Console ]

**To replace a CA certificate bundle**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, under **Load Balancing**, choose **Trust Stores**.

1. Select your trust store.

1. Choose **Actions**, and then choose **Replace CA bundle**.

1. For **CA certificate bundle**, enter the Amazon S3 path to the new bundle.

1. Choose **Replace CA bundle**.

------
#### [ AWS CLI ]

**To replace a CA certificate bundle**  
Use the [modify-trust-store](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-trust-store.html) command.

```
aws elbv2 modify-trust-store \
    --trust-store-arn {{trust-store-arn}} \
    --ca-certificates-bundle-s3-bucket {{amzn-s3-demo-bucket}} \
    --ca-certificates-bundle-s3-key {{certificates/ca-bundle.pem}}
```

------
#### [ AWS CloudFormation ]

Define a resource of type `AWS::ElasticLoadBalancingV2::TrustStore`.

```yaml
Resources:
  myTrustStore:
    Type: 'AWS::ElasticLoadBalancingV2::TrustStore'
    Properties:
      Name: {{my-trust-store}}
      CaCertificatesBundleS3Bucket: {{amzn-s3-demo-bucket-new}}
      CaCertificatesBundleS3Key: {{certificates/new-ca-bundle.pem}}
```

------

## Add a certificate revocation list
<a name="add-crl-mtls"></a>

Optionally, you can create a certificate revocation list (CRL) for a trust store. Revocation lists are released by certificate authorities and contain data for certificates that have been revoked. Network Load Balancers only support certificate revocation lists in the PEM format. When a certificate revocation list is added to a trust store, it is given a revocation ID. The revocation IDs increase for every revocation list added to the trust store, and they can't be changed.

**Important**  
Network Load Balancers do not support revoking certificates that have a negative serial number. If a CRL contains a negative serial number, Network Load Balancers ignore that entry and do not revoke the certificate it identifies. To revoke such a certificate, reissue it with a non-negative serial number.

------
#### [ AWS Management Console ]

**To add a certificate revocation list**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, under **Load Balancing**, choose **Trust Stores**.

1. Select your trust store.

1. On the **Certificate revocation lists** tab, choose **Actions**, and then choose **Add revocation list**.

1. For **Certificate revocation list**, enter the Amazon S3 path to your revocation list.

1. Choose **Add**.

------
#### [ AWS CLI ]

**To add a certificate revocation list**  
Use the [add-trust-store-revocations](https://docs.aws.amazon.com/cli/latest/reference/elbv2/add-trust-store-revocations.html) command.

```
aws elbv2 add-trust-store-revocations \
    --trust-store-arn {{trust-store-arn}} \
    --revocation-contents "RevocationType=CRL,S3Bucket={{amzn-s3-demo-bucket}},S3Key={{crl/revoked-list.pem}}"
```

------
#### [ AWS CloudFormation ]

Define a resource of type `AWS::ElasticLoadBalancingV2::TrustStoreRevocation`.

```yaml
Resources:
  myRevocationContents:
    Type: 'AWS::ElasticLoadBalancingV2::TrustStoreRevocation'
    Properties:
      TrustStoreArn: !Ref myTrustStore
      RevocationContents:
        - RevocationType: CRL
          S3Bucket: {{amzn-s3-demo-bucket}}
          S3Key: {{crl/revoked-list.pem}}
```

------

## Delete a certificate revocation list
<a name="delete-crl-mtls"></a>

When you no longer need a certificate revocation list, you can delete it. When you delete a certificate revocation list from a trust store, its revocation ID is also deleted and is not reused for the life of the trust store.

------
#### [ AWS Management Console ]

**To delete a certificate revocation list**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, under **Load Balancing**, choose **Trust Stores**.

1. Select your trust store.

1. On the **Certificate revocation lists** tab, select the revocation list.

1. Choose **Actions**, and then choose **Remove revocation list**.

1. When prompted for confirmation, enter **confirm**, and then choose **Delete**.

------
#### [ AWS CLI ]

**To delete a certificate revocation list**  
Use the [remove-trust-store-revocations](https://docs.aws.amazon.com/cli/latest/reference/elbv2/remove-trust-store-revocations.html) command.

```
aws elbv2 remove-trust-store-revocations \
    --trust-store-arn {{trust-store-arn}} \
    --revocation-ids {{1}}
```

------

## Delete a trust store
<a name="delete-trust-store-mtls"></a>

When you no longer have use for a trust store, you can delete it. You can't delete a trust store that is associated with a listener.

------
#### [ AWS Management Console ]

**To delete a trust store**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Before you delete the trust store, remove its listener association. Open the listener, choose **Edit**, and turn off **Mutual authentication (mTLS)**. You can also remove the association from the **Associations** tab of the trust store.

1. In the navigation pane, under **Load Balancing**, choose **Trust Stores**.

1. Select your trust store.

1. Choose **Actions**, and then choose **Delete**.

1. When prompted for confirmation, enter **confirm**, and then choose **Delete**.

------
#### [ AWS CLI ]

**To remove the listener association**  
Before you delete the trust store, use the [modify-listener](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-listener.html) command to turn off mutual authentication, which disassociates the trust store.

```
aws elbv2 modify-listener \
    --listener-arn {{listener-arn}} \
    --mutual-authentication Mode=off
```

**To delete a trust store**  
Use the [delete-trust-store](https://docs.aws.amazon.com/cli/latest/reference/elbv2/delete-trust-store.html) command.

```
aws elbv2 delete-trust-store \
    --trust-store-arn {{trust-store-arn}}
```

------

## Create a TLS listener with mTLS
<a name="create-tls-listener-mtls"></a>

You can enable mutual authentication when you create a TLS listener, instead of modifying an existing listener.

------
#### [ AWS Management Console ]

**To create a TLS listener with mTLS**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Load Balancers**.

1. Select the name of the load balancer to open its details page.

1. On the **Listeners and rules** tab, choose **Add listener**.

1. For **Protocol**, choose **TLS**, and then enter the port.

1. For **Default SSL/TLS server certificate**, choose a certificate.

1. Under **Client certificate handling**, select **Mutual authentication (mTLS)**, and then choose **Verify with trust store**.

1. For **Trust store**, choose your trust store.

1. For **Default action**, choose a target group to forward traffic to.

1. Choose **Add**.

------
#### [ AWS CLI ]

**To create a TLS listener with mTLS**  
Use the [create-listener](https://docs.aws.amazon.com/cli/latest/reference/elbv2/create-listener.html) command, specifying the TLS protocol and verify mode.

```
aws elbv2 create-listener \
    --load-balancer-arn {{load-balancer-arn}} \
    --protocol TLS \
    --port {{443}} \
    --certificates CertificateArn={{certificate-arn}} \
    --ssl-policy {{ELBSecurityPolicy-TLS13-1-2-2021-06}} \
    --mutual-authentication Mode=verify,TrustStoreArn={{trust-store-arn}} \
    --default-actions Type=forward,TargetGroupArn={{target-group-arn}}
```

------
#### [ AWS CloudFormation ]

Use the `AWS::ElasticLoadBalancingV2::Listener` resource with a `MutualAuthentication` property.

```yaml
Resources:
  MyTlsListener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      LoadBalancerArn: {{load-balancer-arn}}
      Protocol: TLS
      Port: 443
      Certificates:
        - CertificateArn: {{certificate-arn}}
      MutualAuthentication:
        Mode: verify
        TrustStoreArn: {{trust-store-arn}}
      DefaultActions:
        - Type: forward
          TargetGroupArn: {{target-group-arn}}
```

------

## Modify a TLS listener with mTLS
<a name="modify-tls-listener-mtls"></a>

You can enable or change mutual authentication on an existing TLS listener.

------
#### [ AWS Management Console ]

**To modify a TLS listener with mTLS**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Load Balancers**.

1. Select the name of the load balancer to open its details page.

1. On the **Listeners and rules** tab, select the TLS listener, and then choose **Edit listener**.

1. Under **Client certificate handling**, select **Mutual authentication (mTLS)**, and then choose **Verify with trust store**.

1. For **Trust store**, choose your trust store.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

**To modify a TLS listener with mTLS**  
Use the [modify-listener](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-listener.html) command with the `--mutual-authentication` argument.

```
aws elbv2 modify-listener \
    --listener-arn {{listener-arn}} \
    --mutual-authentication Mode=verify,TrustStoreArn={{trust-store-arn}}
```

------
#### [ AWS CloudFormation ]

Update the `MutualAuthentication` property of the `AWS::ElasticLoadBalancingV2::Listener` resource, and then deploy the updated stack.

```yaml
Resources:
  MyTlsListener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      LoadBalancerArn: {{load-balancer-arn}}
      Protocol: TLS
      Port: 443
      Certificates:
        - CertificateArn: {{certificate-arn}}
      MutualAuthentication:
        Mode: verify
        TrustStoreArn: {{trust-store-arn}}
      DefaultActions:
        - Type: forward
          TargetGroupArn: {{target-group-arn}}
```

------

## Advanced mTLS listener settings
<a name="advanced-mtls-listener-settings"></a>

You can change two optional mTLS behaviors on a TLS listener. Both settings travel in the `MutualAuthenticationAttributes` structure on the listener.

**Note**  
`ClientCertificateIdentityFilters` is also part of the `MutualAuthenticationAttributes` structure. To restrict which client identities the load balancer admits, see [Client certificate identity filters](client-certificate-filters.md).

Expired client certificate handling  
The `IgnoreClientCertificateExpiry` attribute controls whether the load balancer accepts a client certificate whose validity period has passed. By default, the load balancer rejects expired certificates. To accept expired certificates that otherwise chain to a trusted CA, set `IgnoreClientCertificateExpiry` to `true`.

Advertise trust store CA subject names  
The `AdvertiseTrustStoreCaNames` attribute controls whether the load balancer tells connecting clients which CAs it trusts. When you enable this attribute, the load balancer includes the distinguished names of the trusted CAs in the TLS `CertificateRequest` message during the handshake. A client can then automatically select a certificate that a trusted CA issued. By default, this attribute is off. You can enable it on new and existing TLS listeners.

------
#### [ AWS Management Console ]

**To accept expired certificates and advertise CA names**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Load Balancers**.

1. Select the name of the load balancer to open its details page.

1. On the **Listeners and rules** tab, select the TLS listener, and then choose **Edit listener**.

1. In the mutual authentication (mTLS) settings, select **Allow expired client certificates** to accept expired certificates that are still trusted.

1. Select **Advertise trust store CA subject names** to advertise trusted CA names to clients.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

**To accept expired certificates and advertise CA names**  
Use the [modify-listener](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-listener.html) command.

```
aws elbv2 modify-listener \
    --listener-arn {{listener-arn}} \
    --mutual-authentication Mode=verify,TrustStoreArn={{trust-store-arn}},IgnoreClientCertificateExpiry=true,AdvertiseTrustStoreCaNames=on
```

------
#### [ CloudFormation ]

Use the `AWS::ElasticLoadBalancingV2::Listener` resource with a `MutualAuthentication` property.

```yaml
Resources:
  MyTlsListener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      Protocol: TLS
      Port: 443
      MutualAuthentication:
        Mode: verify
        TrustStoreArn: {{trust-store-arn}}
        IgnoreClientCertificateExpiry: true
        AdvertiseTrustStoreCaNames: "on"
```

------