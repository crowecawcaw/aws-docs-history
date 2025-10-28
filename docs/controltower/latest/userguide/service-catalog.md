# Provision accounts through AWS Service Catalog

AWS Service Catalog enables IT administrators to create, manage, and distribute portfolios of
approved products to end users, who then have access to the products they need in a
personalized portal. Typical products include servers, databases, websites, or
applications that are deployed using AWS resources.

You can control the users that have access to specific products, which allows you to
enforce compliance with organizational business standards, manage product lifecycles,
and help users find and launch products with confidence. For more information, see
_[Service Catalog Administrator Guide](../../../servicecatalog/latest/adminguide.md "../../../servicecatalog/latest/adminguide.md")_.

In AWS Control Tower, your central cloud administrators and your end users can provision custom
accounts in your landing zone using AWS Service Catalog products, called _custom blueprints_. For more
information, see [Step2. Create the AWS Service Catalog product](afc-setup-steps.md#step-2-create-blueprint-product "afc-setup-steps.md#step-2-create-blueprint-product").

You can interact with AWS Control Tower accounts through the AWS Service Catalog console and APIs. For more information, see [Interact with AWS Control Tower
accounts from AWS Service Catalog](handle-accounts-with-service-catalog.md "handle-accounts-with-service-catalog.md")

AWS Control Tower also can make use of the Service Catalog APIs to further automate account provisioning
and updating. For details, see [the AWS Service Catalog Developer
Guide](../../../servicecatalog/latest/dg/what-is-service-catalog.md "../../../servicecatalog/latest/dg/what-is-service-catalog.md").
