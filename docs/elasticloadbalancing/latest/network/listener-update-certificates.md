# Update a TLS listener for your

Network Load Balancer

After you create a TLS listener, you can replace the default certificate, add or
remove certificates from the certificate list, update the security policy, or update the
ALPN policy.

###### Tasks

- [Replace the default certificate](#replace-default-certificate "#replace-default-certificate")
- [Add certificates to the certificate list](#add-certificates "#add-certificates")
- [Remove certificates from the certificate list](#remove-certificates "#remove-certificates")
- [Update the security policy](#update-security-policy "#update-security-policy")
- [Update the ALPN policy](#update-alpn-policy "#update-alpn-policy")

## Replace the default certificate

You can replace the default certificate for your TLS listener as needed.
For more information, see [Default certificate](tls-listener-certificates.md#default-certificate "tls-listener-certificates.md#default-certificate").

Console

###### To replace the default certificate

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer.
4. On the **Listeners** tab, choose the text in the **Protocol:Port**
   column to open the detail page for the listener.
5. On the **Certificates** tab, choose **Change default**.
6. Within the **ACM and IAM certificates** table, select a new default certificate.
7. (Optional) By default, we select **Add previous default certificate to listener certificate list**.
   We recommend that you keep this option selected, unless you currently have no listener certificates for SNI
   and rely on TLS session resumption.
8. Choose **Save as default**.

AWS CLI

###### To replace the default certificate

Use the [modify-listener](../../../cli/latest/reference/elbv2/modify-listener.md "../../../cli/latest/reference/elbv2/modify-listener.md") command.

```
aws elbv2 modify-listener \
    --listener-arn `listener-arn` \
    --certificates CertificateArn=`new-default-certificate-arn`
```

CloudFormation

###### To replace the default certificate

Update the [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md") resource with the
new default certificate.

```
Resources:
  myTLSListener:
    Type: 'AWS::ElasticLoadBalancingV2::Listener'
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: TLS
      Port: 443
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref myTargetGroup
      SslPolicy: "ELBSecurityPolicy-TLS13-1-2-2021-06"
      Certificates:
        - CertificateArn: "`new-default-certificate-arn`"
```

## Add certificates to the certificate list

You can add certificates to the certificate list for your listener using the
following procedure. When you first create a TLS listener, the certificate list is
empty. You can add the default certificate to the certificate list to ensure that
this certificate is used with the SNI protocol even if it is replaced as the default
certificate. For more information, see [Certificate list](tls-listener-certificates.md#sni-certificate-list "tls-listener-certificates.md#sni-certificate-list").

Console

###### To add certificates to the certificate list

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Listeners** tab, choose the text in the
   **Protocol:Port** column to open the detail page for the
   listener.
5. Choose the **Certificates** tab.
6. To add the default certificate to the list, choose **Add default to list**.
7. To add nondefault certificates to the list, do the following:
   1. Choose **Add certificate**.
   2. To add certificates that are already managed by ACM or IAM, select the
      check boxes for the certificates and choose **Include as pending
      below**.
   3. To add a certificate that isn't managed by ACM or IAM, choose
      **Import certificate**, complete the form, and choose
      **Import**.
   4. Choose **Add pending certificates**.

AWS CLI

###### To add certificates to the certificate list

Use the [add-listener-certificates](../../../cli/latest/reference/elbv2/add-listener-certificates.md "../../../cli/latest/reference/elbv2/add-listener-certificates.md") command.

```
aws elbv2 add-listener-certificates \
    --listener-arn `listener-arn` \
    --certificates \
        CertificateArn=`certificate-arn-1` \
        CertificateArn=`certificate-arn-2` \
        CertificateArn=`certificate-arn-3`
```

CloudFormation

###### To add certificates to the certificate list

Define a resource of type [AWS::ElasticLoadBalancingV2::ListenerCertificate](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenercertificate.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenercertificate.md").

```
Resources:
  myCertificateList:
    Type: 'AWS::ElasticLoadBalancingV2::ListenerCertificate'
    Properties:
      ListenerArn: !Ref myTLSListener
      Certificates:
        - CertificateArn: "`certificate-arn-1`"
        - CertificateArn: "`certificate-arn-2`"
        - CertificateArn: "`certificate-arn-3`"

  myTLSListener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: TLSS
      Port: 443
      SslPolicy: "ELBSecurityPolicy-TLS13-1-2-2021-06"
      Certificates:
        - CertificateArn: "*certificate-arn-1*"
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref myTargetGroup
```

## Remove certificates from the certificate list

You can remove certificates from the certificate list for a TLS listener using the
following procedure. After you remove a certificate, the listener can no longer
create connections using that certificate. To ensure that clients are not impacted,
add a new certificate to the list and confirm that connections are working before
you remove a certificate from the list.

To remove the default certificate for a TLS listener, see [Replace the default certificate](#replace-default-certificate "#replace-default-certificate").

Console

###### To remove certificates from the certificate list

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Listeners** tab, choose the text in the
   **Protocol:Port** column to open the detail page for the
   listener.
5. On the **Certificates** tab, select the check boxes for
   the certificates and choose **Remove**.
6. When prompted for confirmation, enter `confirm`
   and choose **Remove**.

AWS CLI

###### To remove certificates from the certificate list

Use the [remove-listener-certificates](../../../cli/latest/reference/elbv2/remove-listener-certificates.md "../../../cli/latest/reference/elbv2/remove-listener-certificates.md") command.

```
aws elbv2 remove-listener-certificates \
    --listener-arn `listener-arn` \
    --certificates CertificateArn=`certificate-arn`
```

## Update the security policy

When you create a TLS listener, you can select the security policy that meets your
needs. When a new security policy is added, you can update your TLS listener to use
the new security policy. Network Load Balancers do not support custom security policies. For more
information, see [Security policies for your Network Load Balancer](describe-ssl-policies.md "describe-ssl-policies.md").

Updating the security policy can result in disruptions if the load balancer is
handling a high volume of traffic. To decrease the possibility of disruptions when
your load balancer is handling a high volume of traffic, create an additional load
balancer to help handle the traffic or request an LCU reservation.

Console

###### To update the security policy

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Listeners** tab, choose the text in the
   **Protocol:Port** column to open the detail page for the
   listener.
5. Choose **Actions**, **Edit listener**.
6. In the **Secure listener settings** section, under
   **Security policy**, choose a new security policy.
7. Choose **Save changes**.

AWS CLI

###### To update the security policy

Use the [modify-listener](../../../cli/latest/reference/elbv2/modify-listener.md "../../../cli/latest/reference/elbv2/modify-listener.md") command.

```
aws elbv2 modify-listener \
    --listener-arn `listener-arn` \
    --ssl-policy `ELBSecurityPolicy-TLS13-1-2-Res-2021-06`
```

CloudFormation

###### To update the security policy

Update the [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md") resource with the
new security policy.

```
Resources:
  myTLSListener:
    Type: 'AWS::ElasticLoadBalancingV2::Listener'
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: TLS
      Port: 443
      SslPolicy: "`ELBSecurityPolicy-TLS13-1-2-2021-06`"
      Certificates:
        - CertificateArn: "*default-certificate-arn*"
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref myTargetGroup
```

## Update the ALPN policy

You can update the ALPN policy for your TLS listener as needed. For
more information, see [ALPN policies](load-balancer-listeners.md#alpn-policies "load-balancer-listeners.md#alpn-policies").

Console

###### To update the ALPN policy

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Listeners** tab, choose the text in the
   **Protocol:Port** column to open the detail page for the
   listener.
5. Choose **Actions**, **Edit listener**.
6. In the **Secure listener settings** section, for
   **ALPN policy**, choose a policy to enable ALPN or
   choose **None** to disable ALPN.
7. Choose **Save changes**.

AWS CLI

###### To update the ALPN policy

Use the [modify-listener](../../../cli/latest/reference/elbv2/modify-listener.md "../../../cli/latest/reference/elbv2/modify-listener.md") command.

```
aws elbv2 modify-listener \
    --listener-arn `listener-arn` \
    --alpn-policy `HTTP2Preferred`
```

CloudFormation

###### To update the ALPN policy

Update the [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md") resource to
include the ALPN policy.

```
Resources:
  myTLSListener:
    Type: 'AWS::ElasticLoadBalancingV2::Listener'
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: TLS
      Port: 443
      SslPolicy: "ELBSecurityPolicy-TLS13-1-2-Res-2021-06"
      AlpnPolicy:
        - `HTTP2Preferred`
      Certificates:
        - CertificateArn: "*certificate-arn*"
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref myTargetGroup
```
