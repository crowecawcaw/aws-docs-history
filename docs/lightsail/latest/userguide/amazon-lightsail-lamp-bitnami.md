

# LAMP by Bitnami

**This blueprint packaged by Bitnami was deprecated on November 19, 2026**  
You can no longer create new instances with this blueprint. Existing instances and snapshots are not affected; you can keep using them and can still create new instances from snapshots. You are responsible for keeping the software on these instances up to date. When creating new instances, we recommend using the equivalent blueprint packaged by Lightsail if available. [Learn more](amazon-lightsail-faq-bitnami-blueprints.md)  
If you have an existing instance that uses a blueprint packaged by Bitnami and want to migrate to a blueprint packaged by Lightsail, see [Migrating from Bitnami blueprints to Lightsail blueprints](migrate-from-bitnami-to-lightsail-blueprints.md).

This section covers topics related to instances that use LAMP packaged by Bitnami. If you're not sure which vendor packaged your blueprint, see [Identify your blueprint vendor](#identify-blueprint-vendor). If your instance uses the LAMP blueprint packaged by Lightsail, see [LAMP](amazon-lightsail-lamp-lightsail.md) instead.

**Topics**
+ [Launch and configure instances that use LAMP packaged by Bitnami](amazon-lightsail-quick-start-guide-lamp-bitnami.md)
+ [Enable HTTPS on instances that use LAMP packaged by Bitnami with Let's Encrypt and Certbot](amazon-lightsail-using-lets-encrypt-certificates-with-lamp.md)
+ [Connect instances that use LAMP packaged by Bitnami to an Aurora database](amazon-lightsail-connect-lamp-instance-to-aurora-database.md)
+ [Identify your blueprint vendor](#identify-blueprint-vendor)

## Identify your blueprint vendor
<a name="identify-blueprint-vendor"></a>

Before you begin, confirm which vendor packaged your instance blueprint. Navigate to your instance's management page in the Lightsail console and check the blueprint information in the header. It shows either "Lightsail" or "Bitnami" as the vendor.

The following example shows an instance that uses WordPress packaged by Lightsail:

![Blueprint vendor on the instance management page.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/headers/blueprint-vendor.png)
