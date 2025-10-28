# Update an HTTPS listener for your Application Load Balancer

After you create an HTTPS listener, you can replace the default certificate, update
the certificate list, or replace the security policy.

###### Tasks

- [Replace the default certificate](#replace-default-certificate "#replace-default-certificate")
- [Add certificates to the certificate list](#add-certificates "#add-certificates")
- [Remove certificates from the certificate list](#remove-certificates "#remove-certificates")
- [Update the security policy](#update-security-policy "#update-security-policy")
- [HTTP header modification](#update-header-modification "#update-header-modification")

## Replace the default certificate

You can replace the default certificate for your listener using the following
procedure. For more information, see [Default certificate](https-listener-certificates.md#default-certificate "https-listener-certificates.md#default-certificate").

Console

###### To replace the default certificate

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer.
4. On the **Listeners and rules** tab, choose the text in the **Protocol:Port**
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

Update the [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md").

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
        - CertificateArn: `new-default-certificate-arn`
```

## Add certificates to the certificate list

You can add certificates to the certificate list for your listener using the
following procedure. If you created the listener using the AWS Management Console, we added the
default certificate to the certificate list for you. Otherwise, the certificate list
is empty. Adding the default certificate to the certificate list ensures that
this certificate is used with the SNI protocol even if it is replaced as the default
certificate. For more information, see [SSL certificates for your Application Load Balancer](https-listener-certificates.md "https-listener-certificates.md").

Console

###### To add certificates to the certificate list

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer.
4. On the **Listeners and rules** tab, choose the text in the **Protocol:Port**
   column to open the detail page for the listener.
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

###### To add a certificate to the certificate list

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
```

## Remove certificates from the certificate list

You can remove certificates from the certificate list for an HTTPS listener using
the following procedure. After you remove a certificate, the listener can no longer
create connections using that certificate. To ensure that clients are not impacted,
add a new certificate to the list and confirm that connections are working before
you remove a certificate from the list.

To remove the default certificate for a TLS listener, see [Replace the default certificate](#replace-default-certificate "#replace-default-certificate").

Console

###### To remove certificates from the certificate list

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer.
4. On the **Listeners and rules** tab, select the text in the **Protocol:Port**
   column to open the detail page for the listener.
5. On the **Certificates** tab, select the check boxes for
   the certificates and choose **Remove**.
6. When prompted for confirmation, enter `confirm` and
   choose **Remove**.

AWS CLI

###### To remove a certificate from the certificate list

Use the [remove-listener-certificates](../../../cli/latest/reference/elbv2/remove-listener-certificates.md "../../../cli/latest/reference/elbv2/remove-listener-certificates.md") command.

```
aws elbv2 remove-listener-certificates \
    --listener-arn `listener-arn` \
    --certificates CertificateArn=`certificate-arn`
```

## Update the security policy

When you create an HTTPS listener, you can select the security policy that meets
your needs. When a new security policy is added, you can update your HTTPS listener
to use the new security policy. Application Load Balancers do not support custom security policies. For
more information, see [Security policies for your Application Load Balancer](describe-ssl-policies.md "describe-ssl-policies.md").

Updating the security policy can result in disruptions if the load balancer is
handling a high volume of traffic. To decrease the possibility of disruptions when
your load balancer is handling a high volume of traffic, create an additional load
balancer to help handle the traffic or request an LCU reservation.

###### Using FIPS policies on your Application Load Balancer

All secure listeners attached to an Application Load Balancer must use either FIPS security
policies or non-FIPS security policies; they cannot be mixed. If an existing
Application Load Balancer has two or more listeners using non-FIPS policies and you want the listeners
to use FIPS security policies instead, remove all listeners until there is only one.
Change the security policy of the listener to FIPS and then create additional listeners
using FIPS security policies. Alternatively, you can create a new Application Load Balancer with new
listeners using only FIPS security policies.

Console

###### To update the security policy

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer.
4. On the **Listeners and rules** tab, select the text in the **Protocol:Port**
   column to open the detail page for the listener.
5. On the **Security** tab, choose **Edit secure listener settings**.
6. In the **Secure listener settings** section, under **Security policy**,
   choose a new security policy.
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
  myHTTPSListener:
    Type: 'AWS::ElasticLoadBalancingV2::Listener'
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: HTTPS
      Port: 443
      DefaultActions:
        - Type: "forward"
          TargetGroupArn: !Ref myTargetGroup
      SslPolicy: `ELBSecurityPolicy-TLS13-1-2-2021-06`
      Certificates:
        - CertificateArn: certificate-arn
```

## HTTP header modification

HTTP header modification enables you to rename specific load
balancer generated headers, insert specific response headers,
and disable server response header. Application Load Balancers support header
modification for both request and response headers.

For more information, see
[Enable HTTP header modification for your Application Load Balancer](enable-header-modification.md "enable-header-modification.md").
