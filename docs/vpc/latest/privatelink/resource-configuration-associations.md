# Manage associations for a VPC Lattice

resource configuration

Consumer accounts with which you share a resource configuration with and clients in
your account can access the resource configuration either directly using a resource VPC
endpoint or through a service-network endpoint. As a result your resource configuration
will have endpoint associations and service network associations.

## Manage service network resource

associations

Create or delete a service network association.

###### Note

If you receive an access-denied message while creating the association between
the service network and resource configuration, check your AWS RAM policy version
and ensure that it is version 2. For more information, see the [AWS RAM user
guide](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md").

###### To manage a service-network association using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **PrivateLink and
   Lattice**, choose **Resource
   configurations**.
3. Select the name of the resource configuration to open its details
   page.
4. Select **Service network associations** tab.
5. Choose **Create associations**.
6. Select a service network from **VPC Lattice service
   networks**. To create a service network, choose
   **Create a VPC Lattice network**.
7. (Optional) To add a tag, expand **Service association
   tags**, choose **Add new tag**, and enter a
   tag key and tag value.
8. (Optional) To enable private DNS names for this service network resource
   association choose **enable private DNS name**. For more
   information, see
   [Custom domain names for service network owners](resource-configuration.md#resource-configuration-custom-domain-name-service-network-owners "resource-configuration.md#resource-configuration-custom-domain-name-service-network-owners").
9. Choose **Save changes**.
10. To delete an association, select the check box for the association and
    then choose **Actions**, **Delete**. When
    prompted for confirmation, enter `confirm` and then
    choose **Delete**.

###### To create a service network association using the AWS CLI

Use the [create-service-network-resource-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-service-network-resource-association.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-service-network-resource-association.html") command.

###### To delete a service network association using the AWS CLI

Use the [delete-service-network-resource-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/delete-service-network-resource-association.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/delete-service-network-resource-association.html") command.

## Manage resource VPC endpoint

associations

Consumer accounts with access to your resource configuration or clients in
your account can access the resource configuration using a resource VPC
endpoint. If your resource configuration has a custom domain name, you can use enable private
DNS to allow VPC Lattice to provision private hosted zones for your resource endpoint or
service-network endpoint. With this, clients can directly curl the domain name to access
the resource configuration. For more information, see
[Custom domain names for resource consumers](resource-configuration.md#custom-domain-name-resource-consumers "resource-configuration.md#custom-domain-name-resource-consumers").

AWS Management Console1. To create a new endpoint association, go to **PrivateLink and
Lattice** in the left navigation pane and choose
**Endpoints**. 2. Choose **Create endpoints**. 3. Select the resource configuration you want to connect to your VPC. 4. Select the VPC, subnets and security groups. 5. (Optional) To turn on private DNS and configure DNS options,
select **Enable DNS name**. 6. (Optional) To tag you VPC endpoint, choose **Add new
tag**, and enter a tag key and tag value. 7. Choose **Create endpoint**.

AWS CLI
The following [create-vpc-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint.html") command creates a VPC endpoint that
uses private DNS. The private DNS preferences are set to
`VERIFIED_AND_SELECTED` and the selected domains are
`example.com` and `example.org`. VPC Lattice only
provisions private hosted zones for any verified domains or
`example.com` or `example.org`.

```
aws ec2 create-vpc-endpoint \
  --vpc-endpoint-type Resource \
  --vpc-id vpc-111122223333aabbc \
  --subnet-ids subnet-0011aabbcc2233445 \
  --resource-configuration-arn arn:aws:vpc-lattice:us-west-2:111122223333:resourceconfiguration/rcfg-07129f3acded87625 \
  --private-dns-enabled \
  --private-dns-preferences VERIFIED_DOMAINS_AND_SPECIFIED_DOMAINS \
  --private-domains-set example.com, example.org
```

###### To create a VPC endpoint association using the AWS CLI

Use the [create-vpc-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint.html") command.

###### To delete a VPC endpoint association using the AWS CLI

Use the [delete-vpc-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc-endpoint.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc-endpoint.html") command.
