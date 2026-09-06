

# Blueprints packaged by Bitnami
<a name="amazon-lightsail-faq-bitnami-blueprints"></a>

## What is happening with Bitnami blueprints on Lightsail?
<a name="what-is-happening-with-bitnami-blueprints"></a>

Starting May 19, 2026, Lightsail will not provide newer versions of blueprints packaged by Bitnami. On November 19, 2026, WordPress, WordPress Multisite, LAMP, Nginx, and Node.js blueprints packaged by Bitnami will be deprecated. On May 19, 2027, Joomla, Magento, MEAN, Drupal, GitLab, Redmine, Ghost, Django, and PrestaShop blueprints packaged by Bitnami will be deprecated.

Your existing instances will continue to run without disruption, even after the deprecation dates. You can also continue to create new instances from existing snapshots of instances using blueprints packaged by Bitnami at any time through the Lightsail console or API, including after the deprecation date. However, after the deprecation date, you can no longer choose the deprecated blueprint to create new instances through the Lightsail console or API.

## Will my existing instances using blueprints packaged by Bitnami be affected?
<a name="will-existing-bitnami-instances-be-affected"></a>

No. Your existing instances will continue running without any disruption, even after the deprecation dates. You can keep using your current instances using blueprints by Bitnami.

## Can I still create new instances using a Bitnami blueprint after the deprecation date?
<a name="can-i-create-instances-after-bitnami-deprecation"></a>

After the deprecation date, you can no longer choose the deprecated blueprint to create new instances through the Lightsail console or API. However, you can continue to create new instances from existing snapshots of instances using blueprints packaged by Bitnami at any time through the Lightsail console or API, including after the deprecation date.

Snapshots are point-in-time backups that let you restore your instance from a good known state, and provide a reliable recovery mechanism. To learn more, see [Create a snapshot of your instance](lightsail-how-to-create-a-snapshot-of-your-instance.md).

## Do I need to migrate my existing application to a new instance?
<a name="do-i-need-to-migrate-bitnami-instances"></a>

No. As long as you regularly update, patch, and secure the operating system and applications on your instance, you do not need to migrate your existing application.

The deprecation does not require you to modify your operating model. If you were updating your operating system and application regularly, you can continue doing that. If you were migrating your application to a new instance every time Lightsail released an updated blueprint, then you can consider migrating now as well. To learn more about how you can migrate your existing application, refer to [Migrating from Bitnami blueprints to Lightsail blueprints](migrate-from-bitnami-to-lightsail-blueprints.md).

## Am I responsible for applying updates and patches to my existing instances that use blueprints packaged by Bitnami?
<a name="am-i-responsible-for-updates-bitnami-instances"></a>

Yes. Your operational model for maintaining existing instances is not affected. You are responsible for keeping your running instances up-to-date by applying any software updates and security patches. The nature of this responsibility model provides flexibility and control. To learn more, refer to [Update management](amazon-lightsail-update-management.md).

When creating a new instance through the Lightsail console or API, we recommend using a blueprint packaged by Lightsail to get the up-to-date blueprint. Blueprints packaged by Lightsail are available for WordPress, WordPress Multisite, LAMP, Nginx, and Node.js.