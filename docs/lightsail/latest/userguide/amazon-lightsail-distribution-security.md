

# Understand distribution security controls in Amazon Lightsail

Security controls help protect your website or web application from distributed denial of service (DDoS) attacks, common web threats, and security vulnerabilities. You can view and manage the security controls for your distribution on the **Security** tab on your distribution's management page.

**Topics**
+ [DDoS protection](#distribution-security-ddos)
+ [WAF and WAF rule groups](#distribution-security-waf)
+ [Protecting your Lightsail distribution with WAF](#amazon-lightsail-distribution-waf)

## DDoS protection
<a name="distribution-security-ddos"></a>

A DDoS attack can prevent legitimate users from accessing your website or web application by overwhelming it with traffic. DDoS protection detects and automatically mitigates these attacks. DDoS protection is always enabled for your distribution, on all distribution plans, at no extra cost. For more information, see [DDoS protection](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html).

## WAF and WAF rule groups
<a name="distribution-security-waf"></a>

The Web Application Firewall (WAF) uses WAF rule groups to help protect your website or web application from common web threats and security vulnerabilities. WAF is supported on the USD $10.00/month and USD $35.00/month distribution plans. For more information, see [Web Application Firewall (WAF) by distribution plan](amazon-lightsail-distribution-plans.md#distribution-plans-waf).

Each WAF rule group contains multiple rules that inspect requests for a specific type of threat. There are two types of WAF rule groups:
+ **Managed WAF rule groups** – Predefined WAF rule groups that protect against common categories of web threats. You enable or disable them without configuring any settings.
+ **Custom WAF rule groups** – Advanced, specialized WAF rule groups that protect against account takeover, fraudulent account creation, and malicious bots. These rule groups require specific configuration before you can enable them.

By default, all WAF rule groups are disabled. To enable them, see [Enabling WAF for your distribution](#enable-distribution-waf).

### Managed WAF rule groups
<a name="distribution-waf-default-rule-groups"></a>

The following managed WAF rule groups are available:
+ **Core rule set** – Provides protection against exploitation of a wide range of vulnerabilities, including some of the high-risk and commonly occurring vulnerabilities described in OWASP publications, such as the [OWASP Top 10](https://owasp.org/www-project-top-ten/). For more information, see [Core rule set (CRS) managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-baseline.html#aws-managed-rule-groups-baseline-crs).
**Warning**  
This rule group can block file uploads or form submissions larger than 8 KB.
+ **Known bad inputs** – Blocks request patterns that are known to be invalid and associated with the exploitation or discovery of vulnerabilities. This rule group is ideal if you want to reduce the risk of a malicious actor discovering a vulnerable website or web application. For more information, see [Known bad inputs managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-baseline.html#aws-managed-rule-groups-baseline-known-bad-inputs).
+ **Anonymous IP list** – Blocks requests from services that permit the obfuscation of viewer identity, such as VPNs, proxies, Tor nodes, and web hosting providers. This rule group is ideal if you want to filter out viewers who might be trying to hide their identity. For more information, see [Anonymous IP list managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-ip-rep.html#aws-managed-rule-groups-ip-rep-anonymous).
+ **Admin protection** – Blocks external access to exposed administrative pages, which can help reduce the risk of a malicious actor gaining administrative access to your website or web application. For more information, see [Admin protection managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-baseline.html#aws-managed-rule-groups-baseline-admin).
**Warning**  
After you enable this rule group, access administrative pages, such as `/wp-admin`, directly from your origin instead of through your distribution.
+ **SQL database** – Blocks request patterns associated with the exploitation of SQL databases, such as SQL injection attacks. This rule group is ideal if your website or web application interfaces with a SQL database. For more information, see [SQL database managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-use-case.html#aws-managed-rule-groups-use-case-sql-db).
+ **Linux operating system** – Blocks request patterns associated with the exploitation of vulnerabilities specific to Linux, including Linux-specific Local File Inclusion (LFI) attacks. This rule group is ideal if any part of your website or web application runs on Linux. Use it together with the POSIX operating system rule group. For more information, see [Linux operating system managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-use-case.html#aws-managed-rule-groups-use-case-linux-os).
+ **POSIX operating system** – Blocks request patterns associated with the exploitation of vulnerabilities specific to POSIX and POSIX-like operating systems, including LFI attacks. This rule group is ideal if any part of your website or web application runs on Linux or another POSIX-like operating system, such as FreeBSD. For more information, see [POSIX operating system managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-use-case.html#aws-managed-rule-groups-use-case-posix-os).
+ **Windows operating system** – Blocks request patterns associated with the exploitation of vulnerabilities specific to Windows, such as the remote execution of PowerShell commands. This rule group is ideal if any part of your website or web application runs on Windows. For more information, see [Windows operating system managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-use-case.html#aws-managed-rule-groups-use-case-windows-os).
+ **PHP application** – Blocks request patterns associated with the exploitation of vulnerabilities specific to the use of the PHP programming language, including the injection of unsafe PHP functions. This rule group is ideal if PHP is installed on any server that your website or web application uses. For more information, see [PHP application managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-use-case.html#aws-managed-rule-groups-use-case-php-app).
+ **WordPress application** – Blocks request patterns associated with the exploitation of vulnerabilities specific to WordPress sites. This rule group is ideal if your website runs on WordPress. Use it together with the SQL database and PHP application rule groups. For more information, see [WordPress application managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-use-case.html#aws-managed-rule-groups-use-case-wordpress-app).
+ **Amazon IP reputation list** – Blocks requests based on Amazon internal threat intelligence. This rule group is ideal if you want to block IP addresses typically associated with bots or other threats. For more information, see [Amazon IP reputation list managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-ip-rep.html#aws-managed-rule-groups-ip-rep-amazon).

### Custom WAF rule groups
<a name="distribution-waf-advanced-rule-groups"></a>

**Note**  
Custom WAF rule groups are supported only on the USD $35.00/month distribution plan. For more information, see [Web Application Firewall (WAF) by distribution plan](amazon-lightsail-distribution-plans.md#distribution-plans-waf).

The following custom WAF rule groups are available:
+ **Account takeover prevention** – Provides protection against malicious account takeover attempts by inspecting login requests to your login page. It checks login credentials against a database of stolen credentials and blocks clients that send too many suspicious login requests. This rule group is ideal if your website or web application has a login page. It requires that you choose the **Request body type** (**JSON** or **Form encoded**) and provide the **Login path**, **Username field**, and **Password field**. For more information, see [Account takeover prevention (ATP) rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-atp.html).
+ **Account creation fraud prevention** – Provides protection against fraudulent account creation attempts on your website or web application. It detects bulk account creation attempts and blocks new accounts that use compromised credentials. This rule group is ideal if your website or web application lets visitors create accounts. It requires that you choose the **Request body type** (**JSON** or **Form encoded**) and provide the **Account creation path** and **Registration page path**. For more information, see [Account creation fraud prevention (ACFP) rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-acfp.html).
+ **Bot control** – Provides protection against automated bots that can consume excess resources, skew business metrics, cause downtime, or perform malicious activities. This rule group is ideal if you want to manage bot traffic to your website or web application. It requires that you choose an inspection level. Choose **Common** to detect self-identifying bots, such as web scrapers, search engines, and automated browsers. Choose **Targeted** to also detect sophisticated bots. The **Targeted** level can show challenges or CAPTCHA puzzles to your visitors. For more information, see [Bot Control rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html).

## Protecting your Lightsail distribution with WAF
<a name="amazon-lightsail-distribution-waf"></a>

The Web Application Firewall (WAF) helps protect your website or web application from common web threats and security vulnerabilities. When you enable WAF for your distribution, it inspects requests before they reach your instance, container service, load balancer, or bucket.

### Prerequisites
<a name="amazon-lightsail-distribution-waf-prerequisites"></a>

Before you get started, you need to create a Lightsail distribution. For more information, see [Create and configure a distribution](amazon-lightsail-creating-content-delivery-network-distribution.md).

**Note**  
WAF isn't supported on the USD $2.50/month distribution plan. To use WAF, change your distribution to the USD $10.00/month or USD $35.00/month plan. For more information, see [Web Application Firewall (WAF) by distribution plan](amazon-lightsail-distribution-plans.md#distribution-plans-waf).

### Enabling WAF for your distribution
<a name="enable-distribution-waf"></a>

Complete the following procedure to enable WAF for your distribution and select the WAF rule groups that you want to use.

**To enable WAF and rule groups**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose the distribution where you want to enable WAF.

1. Choose the **Security** tab on your distribution's management page.

1. In the **Web Application Firewall (WAF)** section, choose **Enable WAF**. Lightsail doesn't enable any WAF rule groups automatically.

1. In the **WAF rule groups** section, use the toggle in the **Change status** column to enable or disable individual WAF rule groups.

1. (USD $35.00/month distribution plan only) The custom WAF rule groups are **Account takeover prevention**, **Account creation fraud prevention**, and **Bot control**. To use one of these rule groups, choose the edit icon in the **Action** column, configure the required settings, and then enable the rule group. For more information, see [Custom WAF rule groups](#distribution-waf-advanced-rule-groups).

After you enable WAF, you can monitor the requests that your WAF rule groups allow and block. For more information, see [Distribution metrics](amazon-lightsail-viewing-distribution-health-metrics.md#distribution-metrics).

### Disabling WAF for your distribution
<a name="disable-distribution-waf"></a>

Complete the following procedure to disable WAF for your distribution.

**Important**  
When you disable WAF, all of your WAF configuration is permanently deleted, including the WAF rule groups that you enabled and the settings of your custom WAF rule groups. This action can't be undone.

**To disable WAF**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose the distribution where you want to disable WAF.

1. Choose the **Security** tab on your distribution's management page.

1. In the **Web Application Firewall (WAF)** section, choose **Disable WAF**.