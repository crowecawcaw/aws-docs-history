

# Update PHP on Lightsail instances to address CVE-2026-109618 and CVE-2026-109619
<a name="amazon-lightsail-update-php-security-vulnerabilities"></a>

On October 21, 2026, the PHP project released security updates that fix two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, both rated Critical with a CVSS v4.0 score of 9.2 out of 10. Both vulnerabilities can allow an unauthenticated attacker to run code remotely on a server that uses PHP to serve web requests.
+ **CVE-2026-109618**: When PHP runs out of memory while handling a request, it can leave internal request data partially set up, which later cleanup may treat as valid.
+ **CVE-2026-109619**: Internal state from one request can survive after its memory is freed, and a later request handled by the same PHP worker may use it.

The following PHP versions contain the fix:


| PHP release line | Fixed version | 
| --- | --- | 
| 8.2 | 8.2.35 | 
| 8.3 | 8.3.36 | 
| 8.4 | 8.4.27 | 
| 8.5 | 8.5.12 | 

**Note**  
We recommend that you use PHP 8.2 or later. PHP 8.1 and older no longer receive updates from the PHP project. However, the Sury PHP repository (packages.sury.org) has published fixes for these vulnerabilities for PHP 5.6 through 8.1 on Debian. If you can't upgrade to PHP 8.2 or later right away, you can install these fixes from the Sury repository, and then plan to upgrade to a supported version. For the commands to add the Sury repository, see [Add the Sury PHP package repository and install PHP-FPM](#php-cve-bitnami-add-sury-repo).  
The Sury PHP repository is a third-party repository. It is not owned or maintained by AWS. For more information, see the [Sury website](https://deb.sury.org/).

If your Lightsail instance runs PHP, we recommend that you update it as soon as possible. To find out whether your instance is affected, see [Which instances are affected](#php-cve-affected-instances). For details about the vulnerabilities, see the [PHP security advisory](https://www.php.net/index.php#2026-10-20-1) on the PHP website.

**CVE-2026-115560 isn't fixed yet**  
On October 23, 2026, the PHP project disclosed CVE-2026-115560, which the versions in the preceding table don't fix. Until a fixed PHP version is released, set `session.upload_progress.enabled = 0` in `php.ini`, as the PHP project recommends. Only applications that change `session.serialize_handler` to `php` at runtime are affected. For more information, see the [PHP informational advisory](https://www.php.net/archive/2026.php#2026-10-23-1).

**Contents**
+ [Which instances are affected](#php-cve-affected-instances)
+ [Before you begin](#php-cve-before-you-begin)
+ [Update PHP on instances created from Lightsail blueprints](#php-cve-lightsail-blueprints)
+ [Update PHP on instances created from Bitnami blueprints](#php-cve-bitnami-blueprints)
+ [Update PHP on Windows Server instances](#php-cve-windows)
+ [Additional resources](#php-cve-resources)

## Which instances are affected
<a name="php-cve-affected-instances"></a>

Your instance may be affected if it runs PHP. This includes instances created from the following blueprints:
+ **Blueprints packaged by Lightsail**: WordPress, WordPress Multisite, LAMP, and Nginx.
+ **Blueprints packaged by Bitnami**: WordPress, WordPress Multisite, LAMP, and other PHP-based applications.
+ **Any instance where you installed PHP yourself**, including Linux and Windows Server instances.

Instances created from the Node.js and Ruby on Rails blueprints, and operating system blueprints such as Ubuntu and Amazon Linux, do not include PHP unless you installed PHP on the instance.

To check whether PHP is installed and which version it runs, connect to your instance using SSH and run `php -v`. On instances created from Bitnami blueprints, run `/opt/bitnami/php/bin/php -v`.

If you create a new instance from a blueprint that includes PHP, follow the steps in [Update PHP on instances created from Lightsail blueprints](#php-cve-lightsail-blueprints) after you create it to make sure that it runs a fixed PHP version.

## Before you begin
<a name="php-cve-before-you-begin"></a>

Before you make any changes to your instance, create a snapshot of it. If something goes wrong during the update, you can create a new instance from the snapshot to restore your site. For more information, see [Back up Linux/Unix Lightsail instances with snapshots](lightsail-how-to-create-a-snapshot-of-your-instance.md).

## Update PHP on instances created from Lightsail blueprints
<a name="php-cve-lightsail-blueprints"></a>

Follow these steps for instances created from the following blueprints packaged by Lightsail: WordPress, WordPress Multisite, LAMP, and Nginx. These instances install PHP from the operating system package repositories, so you can update PHP with the standard package manager.

1. Create a snapshot of your instance as a backup.

1. Connect to your instance using SSH. For more information, see [Connect to Linux or Unix instances on Lightsail](lightsail-how-to-connect-to-your-instance-virtual-private-server.md).

1. Update PHP:

   ```
   sudo apt update
   sudo apt upgrade
   ```

1. Restart the web server so that it loads the updated PHP.
   + WordPress, WordPress Multisite, and LAMP:

     ```
     sudo systemctl restart apache2
     ```
   + Nginx:

     ```
     sudo systemctl restart php8.2-fpm
     ```

1. Confirm the installed version:

   ```
   php -v
   ```

   The version shown should be the fixed version for your PHP release line or newer: 8.2.35, 8.3.36, 8.4.27, or 8.5.12.

## Update PHP on instances created from Bitnami blueprints
<a name="php-cve-bitnami-blueprints"></a>

Bitnami blueprints include their own copy of PHP under `/opt/bitnami/php`. This copy is not updated by `apt upgrade`.

### Recommended: Move to a Lightsail blueprint
<a name="php-cve-bitnami-migrate"></a>

We recommend that you move your application to an instance created from a blueprint packaged by Lightsail, such as WordPress or LAMP. PHP on these instances can be updated with `apt upgrade`, now and for future security updates. For more information, see [Migrating from Bitnami blueprints to Lightsail blueprints](migrate-from-bitnami-to-lightsail-blueprints.md).

1. Create a snapshot of your current instance as a backup.

1. Create a new instance from the matching blueprint packaged by Lightsail.

1. Move your site content and database to the new instance.

1. Move your static IP address to the new instance and confirm that your site works.

1. Delete the old instance when you no longer need it.

### Alternative: Replace the Bitnami PHP in place
<a name="php-cve-bitnami-in-place"></a>

If you can't move to a new instance, you can install a package-managed PHP alongside the Bitnami copy and point the Bitnami web server at it. After this change, you can keep PHP up to date with `apt upgrade`. Create a snapshot of your instance before you make any changes, and test your site afterward.

These steps change several configuration files on your instance. If you're not comfortable running them yourself, you can use an AI assistant to guide you through each step and help with any errors. Review each command before you run it, and don't share passwords or other secrets with the assistant.

1. **Create a snapshot** of your instance as a backup.

1. **Check your current PHP version.** Run the following command and note the PHP release line in the output (for example, 8.2). In the next step, you install the same release line to avoid compatibility issues with your themes and plugins.

   ```
   /opt/bitnami/php/bin/php -v
   ```

1. <a name="php-cve-bitnami-add-sury-repo"></a>**Add the Sury PHP package repository and install PHP-FPM.** Debian's own repositories only provide one PHP release line, so add the Sury PHP repository (packages.sury.org), which provides all supported PHP release lines for Debian. Run the following commands. The first line of the commands reads the release line of your Bitnami PHP, the same one that you checked in the previous step (for example, `8.2`), and saves it in the `PHP_VERSION` variable, so that you install the same release line.
**Important**  
The Sury PHP repository is a third-party repository. It is not owned or maintained by AWS. For more information, see the [Sury website](https://deb.sury.org/).

   ```
   PHP_VERSION=$(/opt/bitnami/php/bin/php -r 'echo PHP_MAJOR_VERSION.".".PHP_MINOR_VERSION;')
   echo "Installing PHP ${PHP_VERSION}"
   sudo apt update
   sudo apt install -y ca-certificates curl gnupg lsb-release
   curl -fsSL https://packages.sury.org/php/apt.gpg | sudo gpg --dearmor -o /usr/share/keyrings/sury-php.gpg
   echo "deb [signed-by=/usr/share/keyrings/sury-php.gpg] https://packages.sury.org/php/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/php.list > /dev/null
   sudo apt update
   sudo apt install -y --no-install-recommends php${PHP_VERSION}-fpm php${PHP_VERSION}-cli php${PHP_VERSION}-mysql php${PHP_VERSION}-curl php${PHP_VERSION}-gd php${PHP_VERSION}-mbstring php${PHP_VERSION}-xml php${PHP_VERSION}-zip php${PHP_VERSION}-intl php${PHP_VERSION}-bcmath php${PHP_VERSION}-bz2 php${PHP_VERSION}-gmp php${PHP_VERSION}-ldap php${PHP_VERSION}-soap php${PHP_VERSION}-sqlite3 php${PHP_VERSION}-tidy
   ```

   The `--no-install-recommends` option prevents apt from installing a second Apache web server alongside the Bitnami one. If your application uses other extensions, such as `imagick` or `memcached` on PrestaShop, install them with `sudo apt install php${PHP_VERSION}-{{name}}`.
**Note**  
The `PHP_VERSION` variable is used in the following steps. Run the remaining steps in the same SSH session.

1. **Point PHP at the Bitnami database socket.** Bitnami WordPress and LAMP instances include a local database server that uses a non-default socket location. Most instances use MariaDB, with the socket at `/opt/bitnami/mariadb/tmp/mysql.sock`. Some older instances use MySQL, with the socket at `/opt/bitnami/mysql/tmp/mysql.sock`. The socket file exists only while the database is running, so make sure that the database is running before you continue. To check, run `sudo /opt/bitnami/ctlscript.sh status`.

   Run the following commands. They use the MariaDB socket if it exists, and otherwise use the MySQL socket, then set it in the new PHP's configuration:

   ```
   DB_SOCKET=/opt/bitnami/mariadb/tmp/mysql.sock
   [ -S "$DB_SOCKET" ] || DB_SOCKET=/opt/bitnami/mysql/tmp/mysql.sock
   sudo sed -i -E "s|^;?\s*pdo_mysql.default_socket\s*=.*|pdo_mysql.default_socket = ${DB_SOCKET}|; s|^;?\s*mysqli.default_socket\s*=.*|mysqli.default_socket = ${DB_SOCKET}|" /etc/php/${PHP_VERSION}/fpm/php.ini
   grep -E '^(pdo_mysql|mysqli)\.default_socket' /etc/php/${PHP_VERSION}/fpm/php.ini
   ```

   The last command should show both settings pointing to the Bitnami database socket.

1. **Create a PHP-FPM pool that runs as the Bitnami web server user.** Run the following commands to add a pool that runs as user and group `daemon` and listens on a new socket, then start the service. These steps apply to all Bitnami blueprints that serve PHP through Apache or Nginx, such as WordPress, WordPress Multisite, LAMP, and Nginx.

   ```
   sudo tee /etc/php/${PHP_VERSION}/fpm/pool.d/bitnami.conf > /dev/null <<'EOF'
   [bitnami]
   listen = /opt/bitnami/php/var/run/ww2.sock
   user = daemon
   group = daemon
   listen.owner = daemon
   listen.group = daemon
   pm = dynamic
   pm.max_children = 5
   pm.start_servers = 2
   pm.min_spare_servers = 1
   pm.max_spare_servers = 3
   pm.max_requests = 5000
   EOF
   sudo systemctl enable php${PHP_VERSION}-fpm
   sudo systemctl restart php${PHP_VERSION}-fpm
   ls -l /opt/bitnami/php/var/run/ww2.sock
   ```

   The last command should show the new socket file.

   The `pm.*` values are examples for a small instance. Adjust them to match your instance size and traffic, then restart PHP-FPM with `sudo systemctl restart php${PHP_VERSION}-fpm`. For details about each setting, see the [PHP-FPM configuration documentation](https://www.php.net/manual/en/install.fpm.configuration.php).

1. **Point the Bitnami web server at the new PHP.** Run the following commands to switch the Bitnami Apache or Nginx configuration from the Bitnami PHP socket (`www.sock`) to the new one (`ww2.sock`), then restart the web server. The commands keep a backup of each changed file with a `.bak` extension.

   ```
   for f in $(sudo grep -rl '/opt/bitnami/php/var/run/www.sock' /opt/bitnami/apache2/conf /opt/bitnami/nginx/conf 2>/dev/null); do
     sudo cp "$f" "$f.bak"
     sudo sed -i 's|/opt/bitnami/php/var/run/www.sock|/opt/bitnami/php/var/run/ww2.sock|g' "$f"
   done
   sudo grep -rn 'ww2.sock' /opt/bitnami/apache2/conf /opt/bitnami/nginx/conf 2>/dev/null
   if [ -d /opt/bitnami/nginx ]; then WEB=nginx; else WEB=apache; fi
   sudo /opt/bitnami/ctlscript.sh restart $WEB
   ```

   The `grep` command should show the new socket in the web server configuration. To undo this change, copy the `.bak` files back and restart the web server.

1. **Use the new PHP on the command line.** The Bitnami PHP directory comes before the system directories in your `PATH`, so the `php` command still runs the Bitnami PHP. Put the system directory first for your user, then confirm that `php` now points to the new PHP:

   ```
   echo 'export PATH="/usr/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   hash -r
   which php
   php -v
   ```

   `which php` should show `/usr/bin/php`, and `php -v` should show the fixed version for your PHP release line.

1. **Confirm the PHP version that your web server uses.** The `php -v` command only checks the command-line PHP. To check the PHP version that your web server uses to serve your site, run the following commands. They create a temporary test file, request it, and then delete it.

   First, set `DOCROOT` to the folder that your web server serves your site from:
   + WordPress and WordPress Multisite:

     ```
     DOCROOT=/opt/bitnami/wordpress
     ```
   + LAMP:

     ```
     DOCROOT=/opt/bitnami/apache/htdocs
     ```
   + Drupal:

     ```
     DOCROOT=/opt/bitnami/drupal
     ```
   + Joomla:

     ```
     DOCROOT=/opt/bitnami/joomla
     ```
   + Magento:

     ```
     DOCROOT=/opt/bitnami/magento/pub
     ```
   + PrestaShop:

     ```
     DOCROOT=/opt/bitnami/prestashop
     ```
   + Nginx:

     ```
     DOCROOT=/opt/bitnami/nginx/html
     ```
   + Other PHP-based applications: the folder that contains your application's files, usually under `/opt/bitnami`.

   Then run the following commands:

   ```
   echo '<?php echo PHP_VERSION, " ", PHP_SAPI, " ", php_ini_loaded_file();' | sudo tee "$DOCROOT/v.php" > /dev/null
   curl -s http://localhost/v.php; echo
   sudo rm -f "$DOCROOT/v.php"
   ```

   The output should show the fixed version for your PHP release line, `fpm-fcgi`, and a `php.ini` path under `/etc/php/`. If the path is `/opt/bitnami/php/etc/php.ini`, the web server is still using the Bitnami PHP.

   For WordPress and WordPress Multisite instances, you can also check in the WordPress admin dashboard. Go to **Tools**, **Site Health**, **Info**, **Server**. **PHP version** should show the fixed version, and **Server API** should show FPM/FastCGI.

1. **Keep PHP up to date.** Run `sudo apt update` and `sudo apt upgrade` to install future PHP security updates.

## Update PHP on Windows Server instances
<a name="php-cve-windows"></a>

Lightsail Windows Server blueprints do not include PHP. If you installed PHP yourself, first create a snapshot of your instance as a backup. Then update PHP using the same method that you used to install it:
+ If you installed PHP from the official Windows builds, download the fixed version for your PHP release line from the [PHP for Windows downloads page](https://windows.php.net/download/) and replace your existing installation. Keep your existing `php.ini` file.
+ If you installed PHP through a package manager or a bundled web stack, use that tool to update PHP.

After updating, restart your web server (for example, IIS or Apache) and run `php -v` to confirm the version.

## Additional resources
<a name="php-cve-resources"></a>
+ [PHP security advisory](https://www.php.net/index.php#2026-10-20-1)
+ [GitHub advisory for CVE-2026-109618 (GHSA-w8hw-w9fx-j79w)](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w)
+ [GitHub advisory for CVE-2026-109619 (GHSA-6wmf-4rv5-p3rp)](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp)
+ [PHP release announcements](https://www.php.net/archive/2026.php)
+ [Back up Linux/Unix Lightsail instances with snapshots](lightsail-how-to-create-a-snapshot-of-your-instance.md)
+ [Connect to Linux or Unix instances on Lightsail](lightsail-how-to-connect-to-your-instance-virtual-private-server.md)