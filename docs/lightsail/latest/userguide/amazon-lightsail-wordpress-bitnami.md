

# WordPress by Bitnami

**This blueprint packaged by Bitnami was deprecated on November 19, 2026**  
You can no longer create new instances with this blueprint. Existing instances and snapshots are not affected; you can keep using them and can still create new instances from snapshots. You are responsible for keeping the software on these instances up to date. When creating new instances, we recommend using the equivalent blueprint packaged by Lightsail if available. [Learn more](amazon-lightsail-faq-bitnami-blueprints.md)  
If you have an existing instance that uses a blueprint packaged by Bitnami and want to migrate to a blueprint packaged by Lightsail, see [Migrating from Bitnami blueprints to Lightsail blueprints](migrate-from-bitnami-to-lightsail-blueprints.md).

This section covers topics related to instances that use WordPress packaged by Bitnami. If you're not sure which vendor packaged your blueprint, see [Identify your blueprint vendor](#identify-wordpress-blueprint-vendor). If your instance uses the WordPress blueprint packaged by Lightsail, see [WordPress](amazon-lightsail-wordpress.md) instead.

**Topics**
+ [Secure your WordPress site with HTTPS on Lightsail](amazon-lightsail-enabling-https-on-wordpress-bitnami.md)
+ [Secure your WordPress site with HTTPS on Lightsail with bncert](amazon-lightsail-enabling-https-on-wordpress-with-bncert.md)
+ [Secure your Lightsail WordPress instance with free Let's Encrypt SSL certificates and certbot](amazon-lightsail-using-lets-encrypt-certificates-with-wordpress.md)
+ [Transfer WordPress data to a MySQL managed database in Lightsail](amazon-lightsail-connect-wordpress-to-mysql-bitnami.md)
+ [Connect a Lightsail WordPress instance to an Amazon Aurora database](amazon-lightsail-connect-wordpress-to-aurora-bitnami.md)
+ [Connect a WordPress website on Lightsail to Amazon S3 with WP Offload Media](amazon-lightsail-connect-wordpress-to-s3-bitnami.md)
+ [Configure WordPress with a Lightsail content delivery network](amazon-lightsail-configure-wordpress-for-distribution-bitnami.md)
+ [Connect a WordPress instance to a Lightsail bucket for static content](amazon-lightsail-connecting-buckets-to-wordpress.md)
+ [Identify your blueprint vendor](#identify-wordpress-blueprint-vendor)

## Identify your blueprint vendor
<a name="identify-wordpress-blueprint-vendor"></a>

Before you begin, confirm which vendor packaged your instance blueprint. Navigate to your instance's management page in the Lightsail console and check the blueprint information in the header. It shows either "Lightsail" or "Bitnami" as the vendor.

The following example shows an instance that uses WordPress packaged by Lightsail:

![Blueprint vendor on the instance management page.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/headers/blueprint-vendor.png)
