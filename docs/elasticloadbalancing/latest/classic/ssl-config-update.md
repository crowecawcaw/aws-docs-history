# Update the SSL negotiation configuration of your

Classic Load Balancer

ELB provides security policies that have predefined SSL negotiation configurations
to use to negotiate SSL connections between clients and your load balancer. If you are
using the HTTPS/SSL protocol for your listener, you can use one of the predefined
security policies, or use your own custom security policy.

For more information about the security policies, see [SSL negotiation configurations for Classic Load Balancers](elb-ssl-security-policy.md "elb-ssl-security-policy.md"). For
information about the configurations of the security policies provided by ELB, see
[Predefined SSL security policies for Classic Load Balancers](elb-security-policy-table.md "elb-security-policy-table.md").

If you create an HTTPS/SSL listener without associating a security policy, ELB
associates the default predefined security policy, `ELBSecurityPolicy-2016-08`, with
your load balancer.

If you prefer, you can create a custom configuration.
We strongly recommend that you test your security policy before you upgrade your
load balancer configuration.

The following examples show you how to update the SSL negotiation configuration for an
HTTPS/SSL listener. Note that the change does not affect requests that were received by
a load balancer node and are pending routing to a healthy instance, but the updated
configuration will be used with new requests that are received.

###### Contents

- [Update the SSL negotiation configuration
  using the console](#ssl-config-update-console "#ssl-config-update-console")
- [Update the SSL negotiation configuration
  using the AWS CLI](#ssl-config-update-cli "#ssl-config-update-cli")

## Update the SSL negotiation configuration

using the console

By default, ELB associates the latest predefined policy with your load balancer.
When a new predefined policy is added, we recommend that you update your load
balancer to use the new predefined policy. Alternatively, you can select a different
predefined security policy or create a custom policy.

###### To update SSL negotiation configuration for an HTTPS/SSL load

balancer using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Listeners** tab, choose **Manage listeners**.
5. On the **Manage listeners** page, locate the listener to be updated, choose **Edit** under **Security policy** select a security policy using one of the following options:
   - Keep the default policy,
     **ELBSecurityPolicy-2016-08**, and then choose
     **Save changes**.
   - Select a predefined policy other than the default, and then choose
     **Save changes**.
   - Select **Custom** and enable at
     least one protocol and one cipher as follows:
     1. For **SSL Protocols**, select one or more
        protocols to enable.
     2. For **SSL Options**, select
        **Server Order Preference** to use the
        order listed in the [Predefined SSL security policies for Classic Load Balancers](elb-security-policy-table.md "elb-security-policy-table.md") for SSL
        negotiation.
     3. For **SSL Ciphers**, select one or more
        ciphers to enable. If you already have an SSL certificate,
        you must enable the cipher that was used to create the
        certificate, because DSA and RSA ciphers are specific to the
        signing algorithm.
     4. Choose **Save changes**.

## Update the SSL negotiation configuration

using the AWS CLI

You can use the default predefined security policy, `ELBSecurityPolicy-2016-08`,
a different predefined security policy, or a custom security policy.

###### To use a predefined SSL security policy

1. Use the following [describe-load-balancer-policies](../../../cli/latest/reference/elb/describe-load-balancer-policies.md "../../../cli/latest/reference/elb/describe-load-balancer-policies.md") command to list the predefined
   security policies provided by ELB. The syntax that you use depends on the
   operating system and shell that you are using.

Linux

```
`aws elb describe-load-balancer-policies --query 'PolicyDescriptions[?PolicyTypeName==`SSLNegotiationPolicyType`].{PolicyName:PolicyName}' --output table`
```

Windows

```
`aws elb describe-load-balancer-policies --query "PolicyDescriptions[?PolicyTypeName==`SSLNegotiationPolicyType`].{PolicyName:PolicyName}" --output table`
```

The following is example output:

```
------------------------------------------
|      DescribeLoadBalancerPolicies      |
+----------------------------------------+
|               PolicyName               |
+----------------------------------------+
|  ELBSecurityPolicy-2016-08             |
|  ELBSecurityPolicy-TLS-1-2-2017-01     |
|  ELBSecurityPolicy-TLS-1-1-2017-01     |
|  ELBSecurityPolicy-2015-05             |
|  ELBSecurityPolicy-2015-03             |
|  ELBSecurityPolicy-2015-02             |
|  ELBSecurityPolicy-2014-10             |
|  ELBSecurityPolicy-2014-01             |
|  ELBSecurityPolicy-2011-08             |
|  ELBSample-ELBDefaultCipherPolicy      |
|  ELBSample-OpenSSLDefaultCipherPolicy  |
+----------------------------------------+
```

To determine which ciphers are enabled for a policy, use the following
command:

```
aws elb describe-load-balancer-policies --policy-names `ELBSecurityPolicy-2016-08` --output table
```

For information about the configuration for the predefined security
policies, see [Predefined SSL security policies for Classic Load Balancers](elb-security-policy-table.md "elb-security-policy-table.md"). 2. Use the [create-load-balancer-policy](../../../cli/latest/reference/elb/create-load-balancer-policy.md "../../../cli/latest/reference/elb/create-load-balancer-policy.md") command to create an SSL
negotiation policy using one of the predefined security policies that you
described in the previous step. For example, the following command uses the
default predefined security policy:

```
`aws elb create-load-balancer-policy --load-balancer-name `my-loadbalancer`
--policy-name `my-SSLNegotiation-policy` --policy-type-name SSLNegotiationPolicyType
--policy-attributes AttributeName=Reference-Security-Policy,AttributeValue=ELBSecurityPolicy-2016-08`
```

If you exceed the limit on the number of policies for the load balancer,
use the [delete-load-balancer-policy](../../../cli/latest/reference/elb/delete-load-balancer-policy.md "../../../cli/latest/reference/elb/delete-load-balancer-policy.md") command to delete any unused
policies. 3. (Optional) Use the following [describe-load-balancer-policies](../../../cli/latest/reference/elb/describe-load-balancer-policies.md "../../../cli/latest/reference/elb/describe-load-balancer-policies.md") command to verify that the
policy is created:

```
`aws elb describe-load-balancer-policies --load-balancer-name `my-loadbalancer` --policy-name `my-SSLNegotiation-policy``
```

The response includes the description of the policy. 4. Use the following [set-load-balancer-policies-of-listener](../../../cli/latest/reference/elb/set-load-balancer-policies-of-listener.md "../../../cli/latest/reference/elb/set-load-balancer-policies-of-listener.md") command to enable the
policy on load balancer port 443:

```
`aws elb set-load-balancer-policies-of-listener --load-balancer-name `my-loadbalancer` --load-balancer-port 443 --policy-names `my-SSLNegotiation-policy``
```

###### Note

The `set-load-balancer-policies-of-listener` command
replaces the current set of policies for the specified load balancer
port with the the specified set of policies. The
`--policy-names` list must include all policies to be
enabled. If you omit a policy that is currently enabled, it is
disabled. 5. (Optional) Use the following [describe-load-balancers](../../../cli/latest/reference/elb/describe-load-balancers.md "../../../cli/latest/reference/elb/describe-load-balancers.md") command to verify that the new policy
is enabled for the load balancer port:

```
`aws elb describe-load-balancers --load-balancer-name `my-loadbalancer``
```

The response shows that the policy is enabled on port 443.

```
...
  {
      "Listener": {
          "InstancePort": 443,
          "SSLCertificateId": "`ARN`",
          "LoadBalancerPort": 443,
          "Protocol": "HTTPS",
          "InstanceProtocol": "HTTPS"
      },
      "PolicyNames": [
          "my-SSLNegotiation-policy"
      ]
  }
...
```

When you create a custom security policy, you must enable at least one protocol
and one cipher. The DSA and RSA ciphers are specific to the signing algorithm and
are used to create the SSL certificate. If you already have an SSL certificate, be
sure to enable the cipher that was used to create the certificate. The name of your
custom policy must not begin with `ELBSecurityPolicy-` or
`ELBSample-`, as these prefixes are reserved for the names of the
predefined security policies.

###### To use a custom SSL security policy

1. Use the [create-load-balancer-policy](../../../cli/latest/reference/elb/create-load-balancer-policy.md "../../../cli/latest/reference/elb/create-load-balancer-policy.md") command to create an SSL
   negotiation policy using a custom security policy. For example:

```
`aws elb create-load-balancer-policy --load-balancer-name `my-loadbalancer`
 --policy-name `my-SSLNegotiation-policy` --policy-type-name SSLNegotiationPolicyType
 --policy-attributes AttributeName=Protocol-TLSv1.2,AttributeValue=true
 AttributeName=Protocol-TLSv1.1,AttributeValue=true
 AttributeName=DHE-RSA-AES256-SHA256,AttributeValue=true
 AttributeName=Server-Defined-Cipher-Order,AttributeValue=true`
```

If you exceed the limit on the number of policies for the load balancer,
use the [delete-load-balancer-policy](../../../cli/latest/reference/elb/delete-load-balancer-policy.md "../../../cli/latest/reference/elb/delete-load-balancer-policy.md") command to delete any unused
policies. 2. (Optional) Use the following [describe-load-balancer-policies](../../../cli/latest/reference/elb/describe-load-balancer-policies.md "../../../cli/latest/reference/elb/describe-load-balancer-policies.md") command to verify that the
policy is created:

```
`aws elb describe-load-balancer-policies --load-balancer-name `my-loadbalancer` --policy-name `my-SSLNegotiation-policy``
```

The response includes the description of the policy. 3. Use the following [set-load-balancer-policies-of-listener](../../../cli/latest/reference/elb/set-load-balancer-policies-of-listener.md "../../../cli/latest/reference/elb/set-load-balancer-policies-of-listener.md") command to enable the
policy on load balancer port 443:

```
`aws elb set-load-balancer-policies-of-listener --load-balancer-name `my-loadbalancer` --load-balancer-port 443 --policy-names `my-SSLNegotiation-policy``
```

###### Note

The `set-load-balancer-policies-of-listener` command
replaces the current set of policies for the specified load balancer
port with the the specified set of policies. The
`--policy-names` list must include all policies to be
enabled. If you omit a policy that is currently enabled, it is
disabled. 4. (Optional) Use the following [describe-load-balancers](../../../cli/latest/reference/elb/describe-load-balancers.md "../../../cli/latest/reference/elb/describe-load-balancers.md") command to verify that the new policy
is enabled for the load balancer port:

```
`aws elb describe-load-balancers --load-balancer-name `my-loadbalancer``
```

The response shows that the policy is enabled on port 443.

```
...
  {
      "Listener": {
          "InstancePort": 443,
          "SSLCertificateId": "`ARN`",
          "LoadBalancerPort": 443,
          "Protocol": "HTTPS",
          "InstanceProtocol": "HTTPS"
      },
      "PolicyNames": [
          "my-SSLNegotiation-policy"
      ]
  }
...
```
