# Configure a custom domain name for your VPC Lattice service

When you create a new service, VPC Lattice generates a unique Fully Qualified Domain
Name (FQDN) for the service with the following syntax.

```
`service_name`-`service_id`.`partition_id`.vpc-lattice-svcs.`region`.on.aws
```

However, the domain names that VPC Lattice provides are not easy for your users to
remember. Custom domain names are simpler and more intuitive URLs that you can provide
to your users. If you'd prefer to use a custom domain name for your service, such as
`www.parking.example.com` instead of the VPC Lattice generated DNS name, you can configure
it when you create a VPC Lattice service. When a client makes a request using your
custom domain name, the DNS server resolves it to the VPC Lattice generated domain
name.

**Prerequisites**

- You must have a registered domain name for your service. If you don't already
  have a registered domain name, you can register one through Amazon Route 53 or
  any other commercial registrar.
- To receive HTTPS requests, you must provide your own certificate in AWS Certificate Manager.
  VPC Lattice doesn't support a default certificate as a fallback. Therefore, if you
  don't provide an SSL/TLS certificate corresponding to your custom domain name,
  all HTTPS connections to your custom domain name will fail. For more
  information, see [Bring Your Own Certificate (BYOC) for VPC Lattice](service-byoc.md "service-byoc.md").
  **Limitations and considerations**

- You can’t have more than one custom domain name for a service.
- You can’t modify the custom domain name after you've created the
  service.
- The custom domain name must be unique for a service network. This means that a
  service can't be created with a custom domain name that already exists (for
  another service) in the same service network.
  The following procedure shows how to configure a custom domain name for your service.

AWS Management Console###### To configure a custom domain name for your service

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Service**.
3. Choose **Create Service**. You are navigated to
   **Step 1: Create a service**.
4. In the **Custom domain configuration** section,
   choose **Specify a custom domain configuration**.
5. Enter your custom domain name.
6. To serve HTTPS requests, select the SSL/TLS certificate matching your custom
   domain name in **Custom SSL/TLS certificate**. If you don't
   have a certificate yet, or don't want to add one now, you can add a certificate
   when you create your HTTPS listener. However, without a certificate, your custom
   domain name won't be able to serve HTTPS requests. For more information, see
   [Add an HTTPS listener](https-listeners.md#add-https-listener "https-listeners.md#add-https-listener").
7. When you have finished adding all other information for creating the service,
   choose **Create**.

AWS CLI

###### To configure a custom domain name for your service

Use the [create-service](../../../cli/latest/reference/vpc-lattice/create-service.md "../../../cli/latest/reference/vpc-lattice/create-service.md") command.

```
aws vpc-lattice create-service --name `service_name` --custom-domain-name `your_custom_domain_name` --type https --certificate-arn `arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012`
```

In the above command, for `--name`, enter a name for your service. For
`--custom-domain-name`, enter your service's domain name such as,
`parking.example.com`. For `--certificate-arn` enter the ARN
of your certificate in ACM. The certificate ARN is available in your account in
AWS Certificate Manager.

## Associate a custom domain name with your service

First, if you haven't already done so, register your custom domain name. The Internet
Corporation for Assigned Names and Numbers (ICANN) manages domain names on the
internet. You register a domain name using a _domain name
registrar_, an ICANN-accredited organization that manages the registry
of domain names. The website for your registrar will provide detailed instructions
and pricing information for registering your domain name. For more information, see
the following resources:

- To use Amazon Route 53 to register a domain name, see [Registering domain names using
  Route 53](../../../Route53/latest/DeveloperGuide/registrar.md "../../../Route53/latest/DeveloperGuide/registrar.md") in the _Amazon Route 53 Developer Guide_.
- For a list of accredited registrars, see the [Accredited Registrar
  Directory](http://www.internic.net/regist.html "http://www.internic.net/regist.html").

Next, use your DNS service, such as your domain registrar, to create a record to
route queries to your service. For more information, see the documentation for your
DNS service. Alternatively, you can use Route 53 as your DNS service.

If you're using Route 53, you can use an alias record or a CNAME record to route
queries to your service. We recommend that you use an alias record as you can create
an alias record at the top node of a DNS namespace, also known as the zone
apex.

If you're using Route 53, you must first create a _hosted zone_, which
contains information about how to route traffic on the internet for your domain.
After you create the private or public hosted zone, create a record such that
your custom domain name, for example `parking.example.com`, is mapped to
the VPC Lattice auto-generated domain name, for example,
`my-service-02031c045478f6ddf1.7d67968.vpc-lattice-svcs.us-west-2.on.aws`.
Without this mapping, your custom domain name won't work in VPC Lattice.

The following procedures show how to create a private or public hosted zone using Route 53

AWS Management ConsoleTo create an alias record to route queries to your service using Route 53, see
[Routing
traffic to Amazon VPC Lattice service domain endpoint](../../../Route53/latest/DeveloperGuide/routing-to-vpc-lattice-service.md "../../../Route53/latest/DeveloperGuide/routing-to-vpc-lattice-service.md").

Use the VPC Lattice generated domain name for your service, for
instance
`my-service-02031c045478f6ddf1.7d67968.vpc-lattice-svcs.us-west-2.on.aws`
for the **Value**. You can find this auto-generated
domain name in the VPC Lattice console on your service page.

AWS CLI ###### To create an alias record in your hosted zone

1. Obtain the VPC Lattice generated domain name for your service (for example,
   `my-service-02031c045478f6ddf1.7d67968.vpc-lattice-svcs.us-west-2.on.aws`)
   and the hosted zone ID by running the `get-service`
   command.
2. To set the alias, use following command.

```
aws route53 change-resource-record-sets --hosted-zone-id `hosted-zone-id-for-your-service-domain` --change-batch `file://~/Desktop/change-set.json`
```

For the `change-set.json` file, create a JSON file with the content
in the following JSON example, and save it on your local machine. Replace
`file://~/Desktop/change-set.json` in the above
command with the path of the JSON file saved in your local machine. Note
that "Type" in the following JSON can be an A or AAAA record type.

```
{
    "Comment": "my-service-domain.com alias",
    "Changes": [
        {
            "Action": "CREATE",
            "ResourceRecordSet": {
                "Name": "`my-custom-domain-name.com`",
                "Type": "`alias-record-type`",
                "AliasTarget": {
                    "HostedZoneId": "`hosted-zone-id-for-your-service-domain`",
                    "DNSName": "`lattice-generated-domain-name`",
                    "EvaluateTargetHealth": true
                }
            }
        }
    ]
}
```
