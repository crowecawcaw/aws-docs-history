# Managing domain configurations

This topic covers key operations for you to manage your domain configuration
resources. You can also manage the lifecycles of existing configurations by using the
following APIs: [ListDomainConfigurations](../apireference/API_ListDomainConfigurations.md "../apireference/API_ListDomainConfigurations.md"), [DescribeDomainConfiguration](../apireference/API_DescribeDomainConfiguration.md "../apireference/API_DescribeDomainConfiguration.md"), [UpdateDomainConfiguration](../apireference/API_UpdateDomainConfiguration.md "../apireference/API_UpdateDomainConfiguration.md"), and [DeleteDomainConfiguration](../apireference/API_DeleteDomainConfiguration.md "../apireference/API_DeleteDomainConfiguration.md").

###### In this topic:

- [Viewing domain
  configurations](#iot-custom-endpoints-managing-view "#iot-custom-endpoints-managing-view")
- [Updating domain
  configurations](#iot-custom-endpoints-managing-update "#iot-custom-endpoints-managing-update")
- [Deleting domain
  configurations](#iot-custom-endpoints-managing-delete "#iot-custom-endpoints-managing-delete")
- [Rotating certificates in custom domains](#iot-custom-endpoints-managing-certificates "#iot-custom-endpoints-managing-certificates")

## Viewing domain

configurations

To return a paginated list of all domain configurations in your AWS account, use
the [ListDomainConfigurations](../apireference/API_ListDomainConfigurations.md "../apireference/API_ListDomainConfigurations.md") API . You can see the details of a particular
domain configuration using the [DescribeDomainConfiguration](../apireference/API_DescribeDomainConfiguration.md "../apireference/API_DescribeDomainConfiguration.md") API. This API takes a single
`domainConfigurationName` parameter and returns the details of the
specified configuration.

**Example**

## Updating domain

configurations

To update the status or the custom authorizer of your domain configuration, use
the [UpdateDomainConfiguration](../apireference/API_UpdateDomainConfiguration.md "../apireference/API_UpdateDomainConfiguration.md") API. You can set the status to
`ENABLED` or `DISABLED`. If you disable the domain
configuration, devices connected to that domain receive an authentication error.
Currently you can't update the server certificate in your domain configuration. To
change the certificate of a domain configuration, you must delete and recreate
it.

**Example**

## Deleting domain

configurations

Before you delete a domain configuration, use the [UpdateDomainConfiguration](../apireference/API_UpdateDomainConfiguration.md "../apireference/API_UpdateDomainConfiguration.md") API to set the status to
`DISABLED`. This helps you avoid accidentally deleting the endpoint.
After you disable the domain configuration, delete it by using the [DeleteDomainConfiguration](../apireference/API_DeleteDomainConfiguration.md "../apireference/API_DeleteDomainConfiguration.md") API. You must place AWS-managed domains in
`DISABLED` status for 7 days before you can delete them. You can
place custom domains in `DISABLED` status and then delete them at
once.

**Example**

After you delete a domain configuration, AWS IoT Core no longer serves the server
certificate associated with that custom domain.

## Rotating certificates in custom domains

You may need to periodically replace your server certificate with an updated certificate. The rate at which you do this depends on the validity period
of your certificate.
If you generated your server certificate by using AWS Certificate Manager (ACM), you can set the certificate to renew automatically.
When ACM renews your certificate, AWS IoT Core automatically picks up the new certificate. You don't have to perform any additional action.
If you imported your server certificate from a different source, you can rotate it by reimporting it to ACM.
For information about reimporting certificates, see [Reimport a certificate](../../../acm/latest/userguide/import-reimport.md "../../../acm/latest/userguide/import-reimport.md").

###### Note

AWS IoT Core only picks up certificate updates under the following conditions.

- The new certificate has the same ARN as the old one.
- The new certificate has the same signing algorithm, common name, or subject alternative name as the old one.
