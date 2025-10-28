# Create a VPC endpoint for AWS STS

To start using AWS STS with your VPC, create an interface VPC endpoint for AWS STS. For more
information, see [Access an AWS service
using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the _Amazon VPC User
Guide_.

After you create the VPC endpoint, you must use the matching regional endpoint to send
your AWS STS requests. AWS STS recommends that you use both the `setRegion` and
`setEndpoint` methods to make calls to a Regional endpoint. You can use the
`setRegion` method alone for manually enabled Regions, such as Asia Pacific
(Hong Kong). In this case, the calls are directed to the STS Regional endpoint. To learn how
to manually enable a Region, see [Managing AWS
Regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md") in the _AWS General Reference_. If you use the
`setRegion` method alone for Regions enabled by default, the calls are
directed to the global endpoint of `https://sts.amazonaws.com`.

When you use regional endpoints, AWS STS calls other AWS services using either public
endpoints or private interface VPC endpoints, whichever are in use. For example, assume that
you have created an interface VPC endpoint for AWS STS and have already requested temporary
credentials from AWS STS from resources that are located in your VPC. In that case, these
credentials begin flowing through the interface VPC endpoint by default. For more
information about making Regional requests using AWS STS, see [Manage AWS STS in an AWS Region](id_credentials_temp_enable-regions.md "id_credentials_temp_enable-regions.md").
