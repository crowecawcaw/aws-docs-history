# Create a listener for your Network Load Balancer

A listener is a process that checks for connection requests. You define a listener
when you create your load balancer, and you can add listeners to your load balancer at
any time.

## Prerequisites

- You must specify a target group for the listener rule. For more
  information, see [Create a target group for your Network Load Balancer](create-target-group.md "create-target-group.md").
- You must specify an SSL certificate for a TLS listener. The load balancer
  uses the certificate to terminate the connection and decrypt requests from
  clients before routing them to targets. For more information, see [Server certificates for your Network Load Balancer](tls-listener-certificates.md "tls-listener-certificates.md").
- You can't use an IPv4 target group with a UDP listener for a
  `dualstack` load balancer.
- QUIC and TCP_QUIC listeners are not allowed on
  `dualstack` load balancers or load balancers with associated security groups.
- QUIC and TCP_QUIC listeners are not allowed on load balancers with associated security groups.
- Only one QUIC or TCP_QUIC listener is allowed on an Network Load Balancer at any given time.
- QUIC and TCP_QUIC listeners are not allowed on an Network Load Balancer that has UDP or TCP_UDP listeners.

## Add a listener

You configure a listener with a protocol and a port for connections from clients
to the load balancer, and a target group for the default listener rule. For more
information, see [Listener configuration](load-balancer-listeners.md#listener-configuration "load-balancer-listeners.md#listener-configuration").

Console

###### To add a listener

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Select the name of the load balancer to open its details page.
4. On the **Listeners** tab, choose **Add listener**.
5. For **Protocol**, choose **TCP**,
   **UDP**, **TCP_UDP**, **TLS**, **QUIC**,
   or **TCP_QUIC**. Keep the default port or type a different port.
6. For **Default action**, choose an available target
   group. If you don't have a target group that meets your needs,
   choose **Create target group** to create one now.
   For more information, see [Create a target group](create-target-group.md "create-target-group.md").
7. [TLS listeners] For **Security policy**, we recommend
   that you keep the default security policy.
8. [TLS listeners] For **Default SSL/TLS server certificate**,
   choose the default certificate. You can select the certificate from one of
   the following sources:
   - If you created or imported a certificate using AWS Certificate Manager, choose
     **From ACM**, then choose the certificate from
     **Certificate (from ACM)**.
   - If you imported a certificate using IAM, choose **From
     IAM**, and then choose the certificate from
     **Certificate (from IAM)**.
   - If you have a certificate, choose **Import certificate**.
     Choose either **Import to ACM** or **Import to
     IAM**. For **Certificate private
     key**, copy and paste the contents of the private key file
     (PEM-encoded). For **Certificate body**, copy and
     paste the contents of the public key certificate file (PEM-encoded).
     For **Certificate Chain**, copy and paste the
     contents of the certificate chain file (PEM-encoded), unless you are
     using a self-signed certificate and it's not important that browsers
     implicitly accept the certificate.

9. [TLS listeners] For **ALPN policy**, choose a policy to
   enable ALPN or choose **None** to disable ALPN. For more
   information, see [ALPN policies](load-balancer-listeners.md#alpn-policies "load-balancer-listeners.md#alpn-policies").
10. Choose **Add**.
11. [TLS listeners] To add certificates to the optional certificate list, see
    [Add certificates to the certificate list](listener-update-certificates.md#add-certificates "listener-update-certificates.md#add-certificates").

AWS CLI

###### To create a target group

If you don't have a target group that you can use for the default action,
use the [create-target-group](../../../cli/latest/reference/elbv2/create-target-group.md "../../../cli/latest/reference/elbv2/create-target-group.md") command to create one now. For
examples, see [Create a target group](create-target-group.md "create-target-group.md").

###### To add a TCP listener

Use the [create-listener](../../../cli/latest/reference/elbv2/create-listener.md "../../../cli/latest/reference/elbv2/create-listener.md") command, specifying the TCP protocol.

```
aws elbv2 create-listener \
    --load-balancer-arn `load-balancer-arn` \
    --protocol TCP \
    --port `80` \
    --default-actions Type=forward,TargetGroupArn=`target-group-arn`
```

###### To add a TLS listener

Use the [create-listener](../../../cli/latest/reference/elbv2/create-listener.md "../../../cli/latest/reference/elbv2/create-listener.md") command specifying the TLS protocol.

```
aws elbv2 create-listener \
    --load-balancer-arn `load-balancer-arn` \
    --protocol TLS \
    --port `443` \
    --certificates CertificateArn=`certificate-arn` \
    --ssl-policy `ELBSecurityPolicy-TLS13-1-2-Res-2021-06` \
    --default-actions Type=forward,TargetGroupArn=`target-group-arn`
```

###### To add a UDP listener

Use the [create-listener](../../../cli/latest/reference/elbv2/create-listener.md "../../../cli/latest/reference/elbv2/create-listener.md") command specifying the UDP protocol.

```
aws elbv2 create-listener \
    --load-balancer-arn `load-balancer-arn` \
    --protocol UDP \
    --port `53` \
    --default-actions Type=forward,TargetGroupArn=`target-group-arn`
```

###### To add a QUIC listener

Use the [create-listener](../../../cli/latest/reference/elbv2/create-listener.md "../../../cli/latest/reference/elbv2/create-listener.md") command specifying the QUIC protocol.

```
aws elbv2 create-listener \
    --load-balancer-arn `load-balancer-arn` \
    --protocol QUIC \
    --port `443` \
    --default-actions Type=forward,TargetGroupArn=`target-group-arn`
```

CloudFormation

###### To add a TCP listener

Define a resource of type [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md") using the
TCP protocol.

```
Resources:
  myTCPListener:
    Type: 'AWS::ElasticLoadBalancingV2::Listener'
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: TCP
      Port: 80
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref myTargetGroup
```

###### To add a TLS listener

Define a resource of type [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md") using the
TLS protocol.

```
Resources:
  myTLSListener:
    Type: 'AWS::ElasticLoadBalancingV2::Listener'
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: TLS
      Port: 443
      SslPolicy: "`ELBSecurityPolicy-TLS13-1-2-Res-2021-06`"
      Certificates:
        - CertificateArn: "`certificate-arn`"
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref myTargetGroup
```

###### To add a UDP listener

Define a resource of type [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md") using the
UDP protocol.

```
Resources:
  myUDPListener:
    Type: 'AWS::ElasticLoadBalancingV2::Listener'
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: UDP
      Port: 53
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref myTargetGroup
```

###### To add a QUIC listener

Define a resource of type [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md") using the
QUIC protocol.

```
Resources:
  myQUICListener:
    Type: 'AWS::ElasticLoadBalancingV2::Listener'
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: QUIC
      Port: 443
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref myTargetGroup
```
