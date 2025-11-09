# Create and verify a domain

A domain name verification is an entity that allows you to prove your ownership of a
given domain. As a resource provider you can use the domain and it’s subdomains as
custom domain names for your resource configurations. Resource consumers can see the
verification status of your custom domain name when they describe the resource
configuration.

## Start the domain verification

You start the domain name verification using VPC Lattice, and then you use your
DNS zone to complete the process.

AWS Management Console###### To start the domain name verification

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **PrivateLink and Lattice**,
   choose **Domain verifications**
3. Choose **Start domain verification**.
4. For **Domain name**, enter a domain name that you own.
5. (Optional) To add a tag, choose **Add new tag** and enter the
   tag key and the tag value.
6. Choose **Start domain name verification**.

After the successful start of your domain name verification, VPC Lattice returns the
`Id` and the `txtMethodConfig`. You use the
`txtMethodConfig` to complete the verification of your domain name.

AWS CLI
The following `start-domain-verification` command starts a
domain name verification:

```
aws vpc-lattice start-domain-verification \
  --domain-name example.com
```

The output looks like the following:

```
{
    "id": "dv-aaaa0000000111111",
    "arn": "arn:aws:vpc-lattice:us-west-2:111122223333:domainverification/dv-aaaa0000000111111",
    "domainName": "example.com",
    "status": "PENDING",
    "txtMethodConfig": {
        "value": "vpc-lattice:1111aaaaaaa",
        "name": "_11111aaaaaaaaa"
    }
}
```

VPC Lattice returns the `Id` and the `txtMethodConfig`. You use the
`txtMethodConfig` to complete the verification of your domain name. In
this example, the `txtMethodConfig` is the following:

```
txtMethodConfig": {
        "value": "vpc-lattice:1111aaaaaaa",
        "name": "_11111aaaaaaaaa"
    }
```

## Complete the domain name verification

To complete the domain name verification, you add a TXT record in your DNS zone.
If you use Route 53, use your domain name's hosted zone. When you verify a domain name,
any subdomains are also verified. For instance, if you verify
`example.com`, you can associate a resource configuration with
`alpha.example.com` and `beta.example.com` without
performing any additional verification.

To create a TXT record using the AWS Management Console, see
[Creating
records by using the Amazon Route 53 console](../../../Route53/latest/DeveloperGuide/resource-record-sets-creating.md "../../../Route53/latest/DeveloperGuide/resource-record-sets-creating.md").

###### To create a TXT record using the AWS CLI for Route 53

1. Use the [change-resource-record-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/r53/change-resource-record-sets.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/r53/change-resource-record-sets.html") command with the following example
   `TXT-record.json` file:

```
{
  "Changes": [
    {
      "Action": "CREATE",
      "ResourceRecordSet": {
        "Name": "_11111aaaaaaaaa",
        "Type": "TXT",
        "ResourceRecords": [
          {
           "value": "vpc-lattice:1111aaaaaaa"
          }
        ]
      }
    }
  ]
}
```

2. Use the following AWS CLI command to add the TXT record from the previous step to a Route 53 hosted zone:

```
aws route53 change-resource-record-sets \
  --hosted-zone-id ABCD123456 \
  --change-batch `file://path/to/your/TXT-record.json`
```

Replace the `hosted-zone-id` with the Route 53 Hosted Zone ID of the hosted
zone in your account. The change-batch parameter value points to a JSON file
(TXT-record.json) in a folder (path/to/your).

To check the verification status of your domain name, you can use the VPC Lattice
console or the `get-domain-verification` command.

Once you verify your domain name, it stays verified until you delete it. If you
delete the TXT record from your DNS zone, VPC Lattice deletes the
`verification-id` and you need to reverify the domain name. If you
delete the TXT record in your DNS zone, VPC Lattice sets your domain name verification
status to `UNVERIFIED`. This doesn’t impact any existing resource
endpoints, service network endpoints, or service network VPC associations to your
resource configurations. To reverify your domain name, start the domain name
verification process over.
