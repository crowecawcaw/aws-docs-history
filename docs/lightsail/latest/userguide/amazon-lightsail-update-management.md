

# Update your Lightsail instances and containers
<a name="amazon-lightsail-update-management"></a>

Amazon Web Services (AWS), Amazon Lightsail, and third-party application vendors periodically update and patch the instance images (also known as *blueprints*) that are available on Lightsail. AWS and Lightsail do not update or patch the operating system or applications on instances after you create them. Lightsail also does not update or patch the operating system and software that you configure on your Lightsail container services. Therefore, we recommend that you regularly update, patch, and secure the operating system and applications on your Amazon Lightsail instances and container services. For more information, see the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/).

**Important**  
**CVE-2026-98432**: A flaw in the Linux kernel's IPv4 networking code can let a remote attacker crash an instance, or possibly corrupt memory, by sending specially timed TCP traffic. This issue affects instances created from the Amazon Linux 2023 (AL2023) and Amazon Linux 2 blueprints. To address it, update the kernel to the following version or later, and then reboot the instance:  
AL2023 (kernel 6.1): `6.1.189-236.400.amzn2023`
Amazon Linux 2 (kernel 4.14): `4.14.355-287.758.amzn2`
Amazon Linux 2 (kernel 5.10, if you installed it yourself): `5.10.271-272.1121.amzn2`
For the update steps, see [Update Amazon Linux on Lightsail instances](update-amazon-linux.md). For affected instances that use other Linux blueprints, see [Address CVE-2026-98432 on Linux-based Lightsail instances](address-cve-2026-98432.md).

**Topics**
+ [Update Amazon Linux on Lightsail instances](update-amazon-linux.md)

## Instance blueprint software support
<a name="instance-blueprint-vendor-links"></a>

The following list of Amazon Lightsail platforms and blueprints links to each vendor’s support page. There, you can view information such as how-to guides, and keeping your operating system and application up to date. You can use any automatic update service or recommended process for installing updates that are provided by the application vendor.

**Windows**
+ [Windows Server 2025, Windows Server 2022, Windows Server 2019, and Windows Server 2016](https://docs.microsoft.com/en-us/windows-server/)
+ [Microsoft SQL Server](https://docs.microsoft.com/en-us/sql/)

**Linux and Unix** – Operating system only
+ [Amazon Linux 2023](update-amazon-linux.md#update-amazon-linux-2023)
+ [Amazon Linux 2](update-amazon-linux.md#update-amazon-linux-2)
+ [Ubuntu](https://ubuntu.com/support/community-support)
+ [Debian](https://www.debian.org/support)
+ [FreeBSD](https://www.freebsd.org/community)
+ [openSUSE](https://en.opensuse.org/)
+ [CentOS](https://docs.centos.org/)

**Linux and Unix** – Operating system plus application
+ [Plesk Hosting Stack on Ubuntu](https://support.plesk.com/)
+ [cPanel & WHM for Linux](https://cpanel.com/support)
+ [WordPress](https://docs.bitnami.com/general/apps/wordpress)
+ [WordPress Multisite](https://docs.bitnami.com/general/apps/wordpress-multisite)
+ [LAMP (PHP 8)](https://docs.bitnami.com/general/infrastructure/lamp)
+ [Node.js](https://docs.bitnami.com/general/infrastructure/nodejs)
+ [Joomla\!](https://docs.bitnami.com/general/apps/joomla)
+ [Magento](https://docs.bitnami.com/general/apps/magento)
+ [MEAN](https://docs.bitnami.com/general/infrastructure/mean)
+ [Drupal](https://docs.bitnami.com/general/apps/drupal)
+ [GitLab CE](https://docs.bitnami.com/general/apps/gitlab)
+ [Redmine](https://docs.bitnami.com/general/apps/redmine)
+ [Nginx](https://docs.bitnami.com/general/infrastructure/nginx)
+ [Ghost](https://docs.bitnami.com/general/apps/ghost)
+ [Django](https://docs.bitnami.com/general/infrastructure/django)
+ [PrestaShop](https://docs.bitnami.com/general/apps/prestashop)