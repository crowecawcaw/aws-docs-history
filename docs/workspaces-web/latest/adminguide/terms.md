# Terms to know when using Amazon WorkSpaces Secure Browser

To help you get started with WorkSpaces Secure Browser, you should get familiar with the following
concepts.

**Identity provider (IdP)**

An identity provider verifies your users’ credentials. It then issues authentication
assertions to provide access to a service provider. You can configure your existing IdP to
work with WorkSpaces Secure Browser.

The process for configuring your identity provider (IdP) varies, depending on your
IdP.

You must upload the service provider metadata file to your IdP. Otherwise, your users
won't be able to log in. You must also grant access for your users to use WorkSpaces Secure Browser in your
IdP.

**Identity provider (IdP) metadata document**

WorkSpaces Secure Browser requires specific metadata from your identity provider (IdP) to establish trust.
You can add this metadata to WorkSpaces Secure Browser by uploading a metadata exchange file downloaded from your
IdP.

**Service provider (SP)**

A service provider accepts authentication assertions and provides a service to the user.
WorkSpaces Secure Browser acts as a service provider to users who have been authenticated by their IdP.

**Service provider (SP) metadata document**

You will need to add the service provider metadata details to your identity provider's
(IdP's) configuration interface. The details of this configuration process varies between
providers.

**SAML 2.0**

A standard for exchanging authentication and authorization data between an IdP and a
service provider.

**Virtual Private Cloud (VPC)**

You can use an existing or new VPC, corresponding subnets, and security groups to link
your content with WorkSpaces Secure Browser.

Subnets must with a stable connection to the internet, and the VPC and subnets must also
have a stable connection to any internal and Software as a Service (SaaS) websites for users
to access these resources.

The VPCs, subnets, and security groups listed are taken from the same region as your
WorkSpaces Secure Browser console.

**Trust store**

If a user accessing a web site through WorkSpaces Secure Browser receives a privacy error, such as
NET::ERR_CERT_INVALID, that site might be using a certificate signed by a private certificate
authority (PCA). You may need to add or change the PCAs in your trust store. In addition, if a
user's device requires you to install a specific certificate in order to load a web site, you
will need to add that certificate to your trust store to allow your user to access that site
in WorkSpaces Secure Browser.

Publicly accessible web sites usually don't require any changes to a trust store.

**Web portal**

A web portal provides your users with access to internal and SaaS websites from their
browsers. You can create one web portal in any supported region per account. To request a
limit increase for more than one portal, contact support.

**Web portal endpoint**

The web portal endpoint is the access point your users will launch your web portal from
after signing in with the identity provider configured for the portal.

The endpoint is publicly available on the internet and can be embedded into your
network.
