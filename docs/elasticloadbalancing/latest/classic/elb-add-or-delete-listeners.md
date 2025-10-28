# Configure an HTTPS listener for your Classic Load Balancer

A _listener_ is a process that checks for connection requests. It
is configured with a protocol and a port for front-end (client to load balancer)
connections and a protocol and a port for back-end (load balancer to instance)
connections. For information about the ports, protocols, and listener configurations
supported by Elastic Load Balancing, see [Listeners for your Classic Load Balancer](elb-listener-config.md "elb-listener-config.md").

If you have a load balancer with a listener that accepts HTTP requests on port 80, you
can add a listener that accepts HTTPS requests on port 443. If you specify that the
HTTPS listener sends requests to the instances on port 80, the load balancer terminates
the SSL requests and communication from the load balancer to the instances is not
encrypted. If the HTTPS listener sends requests to the instances on port 443,
communication from the load balancer to the instances is encrypted.

If your load balancer uses an encrypted connection to communicate with instances, you
can optionally enable authentication of the instances. This ensures that the load
balancer communicates with an instance only if its public key matches the key that you
specified to the load balancer for this purpose.

For information about creating a new HTTPS listener, see [Create a Classic Load Balancer with an HTTPS listener](elb-create-https-ssl-load-balancer.md "elb-create-https-ssl-load-balancer.md").

###### Contents

- [Prerequisites](#add-listener-prerequisites "#add-listener-prerequisites")
- [Add an HTTPS listener using the
  console](#add-listener-console "#add-listener-console")
- [Add an HTTPS listener using the AWS CLI](#add-listener-cli "#add-listener-cli")

## Prerequisites

To enable HTTPS support for an HTTPS listener, you must deploy an SSL server
certificate on your load balancer. The load balancer uses the certificate to
terminate and then decrypt requests before sending them to the instances. If you do
not have an SSL certificate, you can create one. For more information, see [SSL/TLS certificates for Classic Load Balancers](ssl-server-cert.md "ssl-server-cert.md").

## Add an HTTPS listener using the

console

You can add an HTTPS listener to an existing load balancer.

###### To add an HTTPS listener to your load balancer using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Listeners** tab, choose
   **Manage listeners**.
5. On the **Manage listeners** page, in the **Listeners** section, choose
   **Add listener**.
6. For **Listener protocol**, select **HTTPS** .

###### Important

By default, the **Instance protocol** is HTTP. If you want to set up
back-end instance authentication, change **Instance protocol** to HTTPS
. 7. For **Security policy**, we recommend that you
use the latest predefined security policy. If you need to use a different
predefined security policy or create a custom policy, see [Update the SSL Negotiation
Configuration](ssl-config-update.md#ssl-config-update-console "ssl-config-update.md#ssl-config-update-console"). 8. For **Default SSL cert**, choose
**Edit**, and then do one of the following:

    * If you created or imported a certificate using AWS Certificate Manager, choose
     **From ACM**, select the certificate from
     the list, and then choose
     **Save changes**.


    ###### Note

    This option is available only in Regions that support
     AWS Certificate Manager.
    * If you imported a certificate using IAM, choose **From IAM**,
     select the certificate from from the list, and
     then choose **Save changes**.
    * If you have an SSL certificate to import to ACM, select **Import**
     and **To ACM**. In **Certificate private key**, copy and paste
     the contents of the PEM-encoded private key file. In
     **Certificate body**, copy and paste the
     contents of the PEM-encoded public key certificate file. In
     **Certificate chain - optional**, copy and paste the
     contents of the PEM-encoded certificate chain file, unless you are
     using a self-signed certificate and it's not important that browsers
     implicitly accept the certificate.
    * If you have an SSL certificate to import but ACM is not
     supported in this Region, select **Import** and **To IAM**.
     In **Certificate name** type the name of
     the certificate. In **Certificate private key**, copy and paste
     the contents of the PEM-encoded private key file. In
     **Certificate body**, copy and paste the
     contents of the PEM-encoded public key certificate file. In
     **Certificate chain - optional**, copy and paste the
     contents of the PEM-encoded certificate chain file, unless you are
     using a self-signed certificate and it's not important that browsers
     implicitly accept the certificate.
    * Choose **Save changes**.

9. For **Cookie stickiness**, the default is **Disabled**. To change this
   choose **Edit**. If choosing **Generated by load balancer**, an
   **Expiration period** must be specified. If choosing **Generated by
   application**, a **Cookie name** must be specified. After making your
   selection choose **Save changes**.
10. (Optional) Choose **Add listener** to add additional
    listeners.
11. Choose **Save changes** to add the listeners you just
    configured.
12. (Optional) To set up back-end instance authentication for an existing load
    balancer, you must use the AWS CLI or an API, as this task is not supported
    using the console. For more information, see [Configure Back-end Instance
    Authentication](elb-create-https-ssl-load-balancer.md#configure_backendauth_clt "elb-create-https-ssl-load-balancer.md#configure_backendauth_clt").

## Add an HTTPS listener using the AWS CLI

You can add an HTTPS listener to an existing load balancer.

###### To add an HTTPS listener to your load balancer using the AWS CLI

1. Get the Amazon Resource Name (ARN) of the SSL certificate. For
   example:

**ACM**

```
arn:aws:acm:`region`:`123456789012`:certificate/`12345678-1234-1234-1234-123456789012`
```

**IAM**

```
arn:aws:iam::`123456789012`:server-certificate/`my-server-certificate`
```

2. Use the following [create-load-balancer-listeners](../../../cli/latest/reference/elb/create-load-balancer-listeners.md "../../../cli/latest/reference/elb/create-load-balancer-listeners.md") command to add a listener to
   your load balancer that accepts HTTPS requests on port 443 and sends the
   requests to the instances on port 80 using HTTP:

```
`aws elb create-load-balancer-listeners --load-balancer-name `my-load-balancer` --listeners Protocol=HTTPS,LoadBalancerPort=443,InstanceProtocol=HTTP,InstancePort=80,SSLCertificateId=`ARN``
```

If you want to set up back-end instance authentication, use the following
command to add a listener that accepts HTTPS requests on port 443 and sends
the requests to the instances on port 443 using HTTPS:

```
`aws elb create-load-balancer-listeners --load-balancer-name `my-load-balancer` --listeners Protocol=HTTPS,LoadBalancerPort=443,InstanceProtocol=HTTPS,InstancePort=443,SSLCertificateId=`ARN``
```

3. (Optional) You can use the following [describe-load-balancers](../../../cli/latest/reference/elb/describe-load-balancers.md "../../../cli/latest/reference/elb/describe-load-balancers.md") command to view the updated details of
   your load balancer:

```
`aws elb describe-load-balancers --load-balancer-name `my-load-balancer``
```

The following is an example response:

```
{
    "LoadBalancerDescriptions": [
        {
            ...
            "ListenerDescriptions": [
                {
                    "Listener": {
                        "InstancePort": 80,
                        "SSLCertificateId": "`ARN`",
                        "LoadBalancerPort": 443,
                        "Protocol": "HTTPS",
                        "InstanceProtocol": "HTTP"
                    },
                    "PolicyNames": [
                        "ELBSecurityPolicy-2016-08"
                    ]
                },
                {
                    "Listener": {
                        "InstancePort": 80,
                        "LoadBalancerPort": 80,
                        "Protocol": "HTTP",
                        "InstanceProtocol": "HTTP"
                    },
                    "PolicyNames": []
                }
            ],
            ...
        }
    ]
}
```

4. (Optional) Your HTTPS listener was created using the default security
   policy. If you want to specify a different predefined security policy or a
   custom security policy, use the [create-load-balancer-policy](../../../cli/latest/reference/elb/create-load-balancer-policy.md "../../../cli/latest/reference/elb/create-load-balancer-policy.md") and [set-load-balancer-policies-of-listener](../../../cli/latest/reference/elb/set-load-balancer-policies-of-listener.md "../../../cli/latest/reference/elb/set-load-balancer-policies-of-listener.md") commands. For more
   information, see [Update the SSL negotiation configuration
   using the AWS CLI](ssl-config-update.md#ssl-config-update-cli "ssl-config-update.md#ssl-config-update-cli").
5. (Optional) To set up back-end instance authentication, use the [set-load-balancer-policies-for-backend-server](../../../cli/latest/reference/elb/set-load-balancer-policies-for-backend-server.md "../../../cli/latest/reference/elb/set-load-balancer-policies-for-backend-server.md") command. For more
   information, see [Configure
   Back-end Instance Authentication](elb-create-https-ssl-load-balancer.md#configure_backendauth_clt "elb-create-https-ssl-load-balancer.md#configure_backendauth_clt").
