# Accessing your development endpoint

When you create a development endpoint in a virtual private cloud (VPC), AWS Glue returns only a
private IP address. The public IP address field is not populated. When you create a non-VPC
development endpoint, AWS Glue returns only a public IP address.

If your development endpoint has a **Public address**, confirm that it is
reachable with the SSH private key for the development endpoint, as in the following
example.

```

ssh -i `dev-endpoint-private-key.pem` glue@`public-address`

```

Suppose that your development endpoint has a **Private address**, your VPC
subnet is routable from the public internet, and its security groups allow inbound access from
your client. In this case, follow these steps to attach an _Elastic IP address_
to a development endpoint to allow access from the internet.

###### Note

If you want to use Elastic IP addresses, the subnet that is being used requires an internet
gateway associated through the route table.

###### To access a development endpoint by attaching an Elastic IP address

1. Open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. In the navigation pane, choose **Dev endpoints**, and navigate to the
   development endpoint details page. Record the **Private address** for use in
   the next step.
3. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
4. In the navigation pane, under **Network & Security**, choose
   **Network Interfaces**.
5. Search for the **Private DNS (IPv4)** that corresponds to the
   **Private address** on the AWS Glue console development endpoint details page.

You might need to modify which columns are displayed on your Amazon EC2 console. Note the
**Network interface ID** (ENI) for this address (for example,
`eni-12345678`). 6. On the Amazon EC2 console, under **Network & Security**, choose
**Elastic IPs**. 7. Choose **Allocate new address**, and then choose
**Allocate** to allocate a new Elastic IP address. 8. On the **Elastic IPs** page, choose the newly allocated **Elastic
IP**. Then choose **Actions**, **Associate
address**. 9. On the **Associate address** page, do the following:

    * For **Resource type**, choose **Network
     interface**.
    * In the **Network interface** box, enter the **Network interface
     ID** (ENI) for the private address.
    * Choose **Associate**.

10. Confirm that the newly associated Elastic IP address is reachable with the SSH private key
    that is associated with the development endpoint, as in the following example.

```

ssh -i `dev-endpoint-private-key.pem` glue@`elastic-ip`

```

For information about using a bastion host to get SSH access to the development endpoint’s
private address, see the AWS Security Blog post [Securely Connect to Linux Instances Running in a Private Amazon VPC](https://aws.amazon.com/blogs/security/securely-connect-to-linux-instances-running-in-a-private-amazon-vpc/ "https://aws.amazon.com/blogs/security/securely-connect-to-linux-instances-running-in-a-private-amazon-vpc/").
