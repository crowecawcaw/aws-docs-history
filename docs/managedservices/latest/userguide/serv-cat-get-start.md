# Getting started with Service Catalog

To get started with Service Catalog in AMS, submit a service request through the AMS console
to request access to Service Catalog. Upon submission of the request, three IAM roles will be deployed into
your account(s) along with
an AMS managed stack containing the CloudFormation macro that invokes the AMS `Transform`
(described previously) so we can register the products in our systems, and to perform operations
against the infrastructure provisioned through Service Catalog. The three IAM roles deployed include a role for IT admins to
manage products as Service Catalog admins; a role for application owners and end-users to configure, launch,
and manage products; and a role that will be used as a launch constraint, that defines the permissions
that Service Catalog will use while launching or updating the your product.
