# Tips and best practices for WordPress instances in Amazon Lightsail

This guide collects practical tips for keeping a WordPress instance on Amazon Lightsail
fast, stable, and secure.

## Keep your site secure and up to date

### Keep WordPress, themes, and plugins updated

- Apply WordPress core, theme, and plugin updates promptly. Updates often
  include performance and security fixes. For more information, see [Keep Lightsail instances
  and containers secure with update management](amazon-lightsail-update-management.md "amazon-lightsail-update-management.md").
- Remove plugins and themes you are not using. Inactive plugins still add
  maintenance overhead and security surface, and poorly written plugins are a
  frequent cause of high memory usage.
- Test major updates on a snapshot-launched copy of your instance before
  applying them to your live site.

### Back up before you make changes

Before editing configuration files or installing plugins, take a snapshot of your
instance so you can easily restore your application from the snapshot in case
something goes wrong:

- Create a manual snapshot from the Lightsail console, or
- Enable automatic snapshots.

For instructions, see [Back up
Linux/Unix Lightsail instances with snapshots](lightsail-how-to-create-a-snapshot-of-your-instance.md "lightsail-how-to-create-a-snapshot-of-your-instance.md") and [Configure automatic
snapshots](amazon-lightsail-configuring-automatic-snapshots.md "amazon-lightsail-configuring-automatic-snapshots.md").

## Monitoring and troubleshooting

### How do I know if my instance is running out of memory?

Common symptoms include:

- Your site displays **"Error establishing a database
  connection"** (on both the public site and the admin panel).
  This usually means MariaDB has stopped.
- The site loads slowly or times out under modest traffic.

To confirm, connect to your instance over SSH and check current memory use:

```
free -m
```

Look at the `available` column under `Mem:`. This is how
much memory your instance can still use. If `available` is below
**50 MB**, your instance is under heavy memory
pressure and is at risk of OOM-killing processes.

You can also check whether the kernel has terminated a process for running out of
memory (an "OOM kill"):

```
sudo dmesg | grep -i "out of memory"
```

If you see entries mentioning `mariadbd` or `mysqld`, your
database is being terminated under memory pressure, and the steps in [Improve memory performance](#wordpress-improve-memory-performance "#wordpress-improve-memory-performance")
should help.

### Does my instance already have automatic memory tuning?

The newer Lightsail WordPress blueprint includes a service that detects the
instance's memory size and applies the swap, MariaDB, and Apache/PHP settings
described in this guide automatically each time the instance starts, including after
you start or reboot it. To check whether your instance has it, connect over SSH and
run:

```
systemctl status lightsail-memory-config
```

If the service exists, your instance already manages these settings automatically
and you do not need to apply them manually. If the command reports that the unit
could not be found, follow the steps in [Improve memory
performance](#wordpress-improve-memory-performance "#wordpress-improve-memory-performance").

## Optimize performance

### Choose the right bundle for your workload

The most effective way to improve WordPress performance is to run on an instance
bundle with enough memory for your workload. WordPress itself is lightweight;
however plugins, themes, and the database can consume significant memory.

- **512 MB – 1 GB RAM (Lightsail nano and micro
  instance bundles):** Suitable for small blogs and low-traffic
  sites with a minimal set of plugins. These instances are the most likely to
  experience memory pressure, and benefit most from the tuning below.
- **2 GB RAM and up:** Recommended if you run
  page builders (such as Elementor or Divi), WooCommerce, or many active
  plugins.

As your site grows and needs more resources, you can upgrade to a larger bundle by
[creating a snapshot and launching a new, larger instance from it](how-to-create-larger-instance-from-snapshot-using-console.md "how-to-create-larger-instance-from-snapshot-using-console.md").

### Improve memory performance

###### Note

The newer Lightsail WordPress blueprint applies size-aware memory tuning
automatically each time the instance starts, so most of the manual steps in this
section are handled for you if you are creating a new Lightsail WordPress
instance.

If your site displays "Error establishing a database connection" when you (or your
visitors) try to load a page, or you see log messages indicating MariaDB was killed
due to out of memory (such as `Out of memory: Killed process ...
 (mariadbd)` in the system log), your instance is most likely running out
of memory. On smaller instances, the Linux kernel may terminate the MariaDB database
process (an "OOM kill") when memory is exhausted.

The three steps below reduce memory pressure by adding swap space and bounding how
much memory the database and web server are allowed to use. Each step helps on its
own, so you can apply only the ones you need, or all three for the greatest effect.
Before you start, make sure you have the latest snapshot of your instance. See [Back up before you make changes](#wordpress-back-up-before-changes "#wordpress-back-up-before-changes")
for more details.

###### Important

These steps require connecting to your instance over SSH and running commands
with `sudo`. Restarting the database and web server briefly interrupts
your site (a few seconds); therefore make the changes during a low-traffic
window.

To connect to your instance, use the browser-based SSH client in the Lightsail
console, or see [Connect to your Linux or Unix instance](lightsail-how-to-connect-to-your-instance-virtual-private-server.md "lightsail-how-to-connect-to-your-instance-virtual-private-server.md").

#### Step 1: Add a swap file

A swap file gives the operating system room to offload inactive memory to disk,
which helps prevent out-of-memory crashes on instances with less than about 1.5
GB of RAM. We recommend adding swap on nano or micro bundles, and it is usually
unnecessary on larger ones.

First, check whether swap is already active:

```
cat /proc/swaps
```

If the only line printed is the header (no swap entries listed), no swap is
configured:

```
Filename                Type        Size       Used    Priority
```

Create a 650 MB swap file:

```
sudo dd if=/dev/zero of=/mnt/.lightsail.swap bs=1K count=665600 status=progress
sudo chmod 600 /mnt/.lightsail.swap
sudo mkswap /mnt/.lightsail.swap
sudo swapon /mnt/.lightsail.swap
```

To make the swap file persist across reboots, add it to
`/etc/fstab`:

```
echo '/mnt/.lightsail.swap none swap sw 0 0' | sudo tee -a /etc/fstab
```

Confirm swap is now active:

```
cat /proc/swaps
```

The swap file now appears in the output:

```
Filename                Type        Size       Used    Priority
/mnt/.lightsail.swap    file        665596     0       -2
```

#### Step 2: Tune the MariaDB database

`innodb_buffer_pool_size` is the largest single memory consumer in
MariaDB. If the default pool size is too large compared to the instance memory,
it can contribute to out-of-memory crashes.

Find the recommended `innodb_buffer_pool_size` for your instance
from the [recommended
configuration table](#wordpress-recommended-memory-values "#wordpress-recommended-memory-values"), then create a dedicated configuration file with
that value (replace `16M` in the example with your value):

```
sudo tee /etc/mysql/mariadb.conf.d/90-lightsail-memory.cnf > /dev/null <<'EOF'
[mysqld]
innodb_buffer_pool_size = 16M
EOF
```

To execute the change, run the following command that restarts the
database:

```
sudo systemctl restart mariadb
```

#### Step 3: Tune Apache and PHP

Apache is the web server that handles incoming requests to your WordPress site.
By default, it allows up to 150 simultaneous worker processes
(`MaxRequestWorkers`). On a small instance, each PHP worker can
use tens of megabytes, which can exhaust memory under load. To limit the number
of workers to match your instance, and bound how much memory a single PHP request
may use, set the Apache `mpm_prefork` limits (values shown are for a
micro instance; check the [recommended configuration table](#wordpress-recommended-memory-values "#wordpress-recommended-memory-values") for your instance):

```
sudo tee /etc/apache2/mods-available/mpm_prefork.conf > /dev/null <<'EOF'
<IfModule mpm_prefork_module>
    StartServers            1
    MinSpareServers         1
    MaxSpareServers         3
    MaxRequestWorkers       5
    MaxConnectionsPerChild  5000
</IfModule>
EOF
```

Set the PHP `memory_limit` (512 MB is a safe upper bound for all
sizes). First detect your PHP version, then write the configuration file:

```
PHP_VERSION=$(php -r 'echo PHP_MAJOR_VERSION.".".PHP_MINOR_VERSION;')
sudo mkdir -p /etc/php/${PHP_VERSION}/apache2/conf.d
sudo tee /etc/php/${PHP_VERSION}/apache2/conf.d/90-lightsail-memory.ini > /dev/null <<'EOF'
memory_limit = 512M
EOF
```

Apply both changes by restarting Apache:

```
sudo systemctl restart apache2
```

#### Recommended values by instance memory

Use the values below based on your instance's total RAM. To check your
instance's memory, run `free -m` and look at the `total`
column, or refer to your bundle size in the Lightsail console.

Recommended memory configuration by instance RAM| Instance memory (RAM) | MariaDB `innodb_buffer_pool_size` | Apache `MaxRequestWorkers` | PHP `memory_limit` | Swap file |
| --- | --- | --- | --- | --- |
| Up to ~1.5 GB | 16M | 5 | 512M | Yes (650 MB) |
| ~1.5–3 GB | 256M | 10 | 512M | No |
| ~3–6 GB | 256M | 25 | 512M | No |
| ~6–13 GB | 2048M | 50 | 512M | No |
| ~13–26 GB | 2048M | 125 | 512M | No |
| More than ~26 GB | 4096M | 250 | 512M | No |

### Use caching to reduce load

Caching reduces how often WordPress has to query the database and run PHP, which
lowers both CPU and memory usage:

- **Page caching:** Install a caching plugin
  such as W3 Total Cache or WP Super Cache to serve static copies of your
  pages.
- **Object caching:** If your site has many
  logged-in users, runs WooCommerce, or uses dynamic content that changes
  often (such as forums or membership areas), an object cache plugin (such as
  [Redis Object
  Cache](https://wordpress.org/plugins/redis-cache/ "https://wordpress.org/plugins/redis-cache/") or APCu-based caches) stores frequently-used query results
  in memory and reduces repeated database lookups.
- **A content delivery network (CDN):** Offload
  static assets (images, CSS, JavaScript) to a CDN such as [Lightsail Distribution](amazon-lightsail-creating-content-delivery-network-distribution.md "amazon-lightsail-creating-content-delivery-network-distribution.md") so they are not served by your
  instance.
