# Amazon Inspector SBOM Generator comprehensive ecosystem collection

The Amazon Inspector SBOM Generator is a tool for creating a software bill of materials (SBOM) and performing vulnerability scanning for supported packages from operating systems and programming languages.
It supports the scanning of various ecosystems beyond core operating systems, ensuring a robust and detailed analysis of infrastructure components.
By generating an SBOM, you can understand the composition of modern technology stacks, identify vulnerabilities in ecosystem components, and gain visibility into third-party software.

## Supported ecosystems

The ecosystem collection extends SBOM generation beyond packages installed through OS package managers.
This is done through the collection of applications deployed in alternative methods, such as manual installation.
The Amazon Inspector SBOM Generator supports scanning for the following ecosystems:

| Ecosystems           | Applications                                                                                                                                                                                                                                                          |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7-Zip                | 7-Zip archiver (version 21.07 and higher)                                                                                                                                                                                                                             |
| Apache               | Apache httpd<br>Apache tomcat                                                                                                                                                                                                                                         |
| Curl                 | Curl<br>Libcurl                                                                                                                                                                                                                                                       |
| Elasticsearch        | Elasticsearch                                                                                                                                                                                                                                                         |
| Google               | Chrome                                                                                                                                                                                                                                                                |
| Java                 | JDK<br>JRE<br>Amazon Corretto                                                                                                                                                                                                                                         |
| Jenkins              | Jenkins (version 2.400.\<br>• and higher)                                                                                                                                                                                                                             |
| MariaDB and MySQL    | MariaDB Server (10.6+, 11.x, 12.x)<br>Oracle MySQL Server Server (8.0, 8.4, 9.4+)                                                                                                                                                                                     |
| Nginx                | Nginx                                                                                                                                                                                                                                                                 |
| Node                 | Node                                                                                                                                                                                                                                                                  |
| OpenSSH              | OpenSSH (versions 9 and 10)                                                                                                                                                                                                                                           |
| OpenSSL              | OpenSSL                                                                                                                                                                                                                                                               |
| Oracle               | Oracle Database Server                                                                                                                                                                                                                                                |
| PHP                  | PHP (version 8.1 and higher)                                                                                                                                                                                                                                          |
| WordPress            | core<br>plugin<br>theme                                                                                                                                                                                                                                               |
| Node.JS              | node                                                                                                                                                                                                                                                                  |
| Windows applications | PowerShell<br>NuGet CLI<br>Visual Studio Code<br>Microsoft Edge<br>SharePoint Server<br>Microsoft Defender<br>Exchange Server<br>Visual Studio<br>.NET Runtime<br>ASP.NET Core Runtime<br>Microsoft Teams<br>Outlook for Windows<br>Microsoft Office<br>Microsoft 365 |

## 7-Zip ecosystem collection

###### Supported applications

- 7 Zip archiver (version 21.07 or higher)

###### Key features

- Examines 7-Zip binaries to extract the embedded version information.

###### Note

Specifically, it searches for the product version value from the binary.

###### Supported platforms – Windows

- `C:/Program Files/7-Zip/7z.exe`
- `C:/Program Files/7-Zip/7za.exe`
- `C:/Program Files/7-Zip/7zz.exe`
- `C:/Program Files/7-Zip/7zr.exe`
- `C:/Program Files (x86)/7-Zip/7z.exe`
- `C:/Program Files (x86)/7-Zip/7za.exe`
- `C:/Program Files (x86)/7-Zip/7zz.exe`
- `C:/Program Files (x86)/7-Zip/7zr.exe`

###### Example PURL

The following is an example package URL for 7-Zip.

```
pkg:generic/7zip/7zip@25.01
```

## Apache ecosystem collection

This section provides details about Apache httpd and Apache tomcat applicatons.

### Apache httpd

###### Supported applications

- Apache httpd

###### Note

Vulnerability evaluation only applies to Apache httpd version 2.0 and higher.

###### Key features

- Parses the `/include/ap_release.h` file to extract installation macros, which contain major identifier strings, minor identifier strings, and patch identifier strings.

###### Supported platforms

The Amazon Inspector SBOM Generator scans for installations in common installation paths across platforms:

###### Unix

- `/usr/local/apache2/include/`

###### Windows

- `/Apache24/include/`
- `/Program Files/Apache24/include/`
- `/Program Files (x86)/Apache24/include/`

###### Example `ap_release.h` file

The following is an example of content inside an `ap_release.h` file.

```

//truncated

#define AP_SERVER_BASEVENDOR "Apache Software Foundation"
#define AP_SERVER_BASEPROJECT "Apache HTTP Server"
#define AP_SERVER_BASEPRODUCT "Apache"

#define AP_SERVER_MAJORVERSION_NUMBER 2
#define AP_SERVER_MINORVERSION_NUMBER 4
#define AP_SERVER_PATCHLEVEL_NUMBER   1
#define AP_SERVER_DEVBUILD_BOOLEAN    0

//truncated

```

###### Example PURL

The following is an example package URL for an `Apache httpd` application.

```

Sample PURL: pkg:generic/apache/httpd@2.4.1

```

### Apache tomcat

###### Supported applications

- Apache tomcat

###### Note

Vulnerability evaluation only applies to Apache tomcat version 9.0 and higher.

###### Key features

- Unpacks the `catalina.jar` file to extract installation macros inside the `META-INF/MANIFEST.MF` file, which contains the version string.

###### Supported platforms

The Amazon Inspector SBOM Generator scans for installations in common installation paths across platforms:

###### Linux

- `/opt/tomcat/lib/`
- `/usr/share/tomcat/lib`
- `/var/lib/tomcat/lib/`

###### macOS

- `/Library/Tomcat/lib/`
- `/usr/local/tomcat/lib`

###### Windows

- `/Program Files/Apache Software Foundation`
- `/Program Files (x86)/Apache Software Foundation/`

###### Example `catalina.jar/META-INF/MANIFEST.MF` file

The following is an example of content inside a `catalina.jar/META-INF/MANIFEST.MF` file.

```

//truncated

Implementation-Title: Apache Tomcat
Implementation-Vendor: Apache Software Foundation
Implementation-Version: 10.1.31

//truncated

```

###### Example PURL

The following is an example package URL for an `Apache tomcat` application.

```

Sample PURL: pkg:generic/apache/tomcat@10.1.31

```

## Curl ecosystem collection

This section provides details about Curl and Libcurl applicatons.

### Curl

###### Supported applications

- Curl

###### Supported platforms

- Unix – Linux and macOS
  - /usr/local/bin/curl

###### Key features – Curl

- Examines curl binaries to extract the embedded version information.

###### Note

Specifically, it searches for version strings in the binary executable `.rodata` section (for ELF binaries on Linux), `.rdata` section (for PE binaries on Windows), or \_\_cstring section (for MachO binaries on macOS).

###### Curl version string

The following is an example of a version string embedded in a Curl binary:

```
curl/8.14.1
```

Version `8.14.1` is extracted from the string to identify the `Curl` version.

###### Example PURL (Curl)

The following is an example package URL for a `Curl` version file.

```
Sample PURL: pkg:generic/curl/curl@8.14.1
```

### Libcurl

###### Supported applications

- Libcurl

###### Supported platforms

- Unix – Linux and macOS
  - /usr/local/bin/curl/curlver.h

###### Key features – Libcurl

- Examines curlver.h to extract embedded version information for Libcurl.

###### Note

Specifically, it extracts the version from the defined `LIBCURL_VERSION_MAJOR`, `LIBCURL_VERSION_MINOR`, and `LIBCURL_VERSION_PATCH` variables.

###### Libcurl version string

The following is an example of the version variables in a `curlver.h` file:

```
#define LIBCURL_VERSION_MAJOR 8
    #define LIBCURL_VERSION_MINOR 14
    #define LIBCURL_VERSION_PATCH 1
```

Version `8.14.1` is extracted from these lines to identify the `Libcurl` version.

###### Example PURL (Libcurl)

The following is an example package URL for a `Libcurl` version file.

```
Sample PURL: pkg:generic/curl/libcurl@8.14.1
```

## Elasticsearch ecosystem collection

###### Supported applications

- Elasticsearch

###### Note

Vulnerability evaluation only applies to Elasticsearch version 7.17.0.

###### Key features

- **Version** – Unpacks the `elasticsearch-<specific.version>.jar` file to extract installation macros inside of `META-INF/MANIFEST.MF` files, which contain the Elasticsearch version string.

###### Supported platforms

- **Linux** – `/etc/elasticsearch/lib`, `/opt/elasticsearch/lib/`, and `/usr/share/elasticsearch/lib/`
- **macOS** – `/usr/local/var/lib/elasticsearch/lib/`
- **Windows** – `/elasticsearch/`, `/Program Files (x86)/Elastic/elasticsearch/lib/`, and `/Program Files/Elastic/elasticsearch/lib/`

###### Example `elasticsearch-<specific.version>.jar/META-INF/MANIFEST.MF` file

The following is an example of an `elasticsearch-<specific.version>.jar/META-INF/MANIFEST.MF` file.

```
//truncated

Manifest-Version: 1.0
Module-Origin: git@github.com:elastic/elasticsearch.git
X-Compile-Elasticsearch-Version: 8.19.0-SNAPSHOT
X-Compile-Lucene-Version: 9.12.1
X-Compile-Elasticsearch-Snapshot: true

//truncated
```

###### Example PURL

The following is an example package URL for an `elasticsearch-<specific.version>.jar/META-INF/MANIFEST.MF` file.

```
pkg:generic/elastic/elasticsearch@8.19.0-SNAPSHOT
```

## Google ecosystem collection

###### Supported applications

- Google Chrome
- Puppeteer (supports the puppeteer library; puppeteer-core is not included)

###### Note

Puppeteer supports the puppeteer library.
Puppeteer core is not included.

###### Supported artifacts

Amazon Inspector collects Google Chrome information from the following:

- The `chrome/VERSION` file (build source)
- The `chrome.exe` file (Windows Chrome installation)
- The `puppeteer` file (installation)

For each of the supported artifacts, the Sbomgen parses and collects either chrome file or the puppeteer file.
For puppeteer installations, the corresponding Chromium version is collected based on the puppeteer version.
For more information, see [Supported browsers](https://pptr.dev/supported-browsers "https://pptr.dev/supported-browsers") on the Puppeteer website.

When the `PUPPETEER_SKIP_CHROMIUM_DOWNLOAD` environment variable is set to `true`, evaluation is skipped, and the `skip_chromium_download=true` qualifier is added to the Puppeteer package URL.

###### Example `chrome/VERSION` version file

The following is an example of the `chrome/VERSION` version file.

```

MAJOR=130
MINOR=0
BUILD=6723
PATCH=58

```

###### Example PURL

The following is an example package URL for a `chrome/VERSION` version file.

```
Sample PURL: pkg:generic/google/chrome@131.0.6778.87
```

###### Example `puppeteer` version file

The following is an example of the `puppeteer` version file.

```
{
"name": "puppeteer",
"version": "23.9.0",
"description": "A high-level API to control headless Chrome over the DevTools Protocol",
"keywords": [
  "puppeteer",
  "chrome",
  "headless",
  "automation"
]
}
```

###### Example PURL

The following is an example package URL for a `puppeteer` version file.

```
Sample PURL: pkg:generic/google/puppeteer@23.9.0
```

###### Example PURL

The following is an example package URL with skip qualifier for a `puppeteer` version file.

```
pkg:generic/google/puppeteer@22.15.0?distro=linux&skip_chromium_download=true
```

## Java ecosystem collection

###### Supported applications

- Oracle JDK
- Oracle JRE
- Amazon Corretto

###### Key features

- Extracts the string of the Java installation.
- Identifies the directory path that contains the Java runtime.
- Identifies the vendor as Oracle JDK, Oracle JRE, and Amazon Corretto.

The Amazon Inspector SBOM Generator scans for Java installations across the following installation paths and platforms:

- macOS: `/Library/Java/JavaVirtualMachines`
- Linux 32-bit: `/usr/lib/jvm`
- Linux 64-bit: `/usr/lib64/jvm`
- Linux (generic): `/usr/java and /opt/java`

###### Example Java version information

The folllowing is an example of an Oracle Java release.

```

// Amazon Corretto
IMPLEMENTOR="Amazon.com Inc."
IMPLEMENTOR_VERSION="Corretto-17.0.11.9.1"
JAVA_RUNTIME_VERSION="17.0.11+9-LTS"
JAVA_VERSION="17.0.11"
JAVA_VERSION_DATE="2024-04-16"
LIBC="default"
MODULES="java.base java.compiler java.datatransfer java.xml java.prefs java.desktop java.instrument java.logging java.management java.security.sasl java.naming java.rmi java.management.rmi java.net.http java.scripting java.security.jgss java.transaction.xa java.sql java.sql.rowset java.xml.crypto java.se java.smartcardio jdk.accessibility jdk.internal.jvmstat jdk.attach jdk.charsets jdk.compiler jdk.crypto.ec jdk.crypto.cryptoki jdk.dynalink jdk.internal.ed jdk.editpad jdk.hotspot.agent jdk.httpserver jdk.incubator.foreign jdk.incubator.vector jdk.internal.le jdk.internal.opt jdk.internal.vm.ci jdk.internal.vm.compiler jdk.internal.vm.compiler.management jdk.jartool jdk.javadoc jdk.jcmd jdk.management jdk.management.agent jdk.jconsole jdk.jdeps jdk.jdwp.agent jdk.jdi jdk.jfr jdk.jlink jdk.jpackage jdk.jshell jdk.jsobject jdk.jstatd jdk.localedata jdk.management.jfr jdk.naming.dns jdk.naming.rmi jdk.net jdk.nio.mapmode jdk.random jdk.sctp jdk.security.auth jdk.security.jgss jdk.unsupported jdk.unsupported.desktop jdk.xml.dom jdk.zipfs"
OS_ARCH="x86_64"
OS_NAME="Darwin"
SOURCE=".:git:7917f11551e8+"

// JDK
IMPLEMENTOR="Oracle Corporation"
JAVA_VERSION="19"
JAVA_VERSION_DATE="2022-09-20"
LIBC="default"
MODULES="java.base java.compiler java.datatransfer java.xml java.prefs java.desktop java.instrument java.logging java.management java.security.sasl java.naming java.rmi java.management.rmi java.net.http java.scripting java.security.jgss java.transaction.xa java.sql java.sql.rowset java.xml.crypto java.se java.smartcardio jdk.accessibility jdk.internal.jvmstat jdk.attach jdk.charsets jdk.zipfs jdk.compiler jdk.crypto.ec jdk.crypto.cryptoki jdk.dynalink jdk.internal.ed jdk.editpad jdk.hotspot.agent jdk.httpserver jdk.incubator.concurrent jdk.incubator.vector jdk.internal.le jdk.internal.opt jdk.internal.vm.ci jdk.internal.vm.compiler jdk.internal.vm.compiler.management jdk.jartool jdk.javadoc jdk.jcmd jdk.management jdk.management.agent jdk.jconsole jdk.jdeps jdk.jdwp.agent jdk.jdi jdk.jfr jdk.jlink jdk.jpackage jdk.jshell jdk.jsobject jdk.jstatd jdk.localedata jdk.management.jfr jdk.naming.dns jdk.naming.rmi jdk.net jdk.nio.mapmode jdk.random jdk.sctp jdk.security.auth jdk.security.jgss jdk.unsupported jdk.unsupported.desktop jdk.xml.dom"
OS_ARCH="x86_64"
OS_NAME="Darwin"
SOURCE=".:git:53b4a11304b0 open:git:967a28c3d85f"

```

###### Example PURL

The following is an example package URL for an Oracle Java release.

```

Sample PURL:
# Amazon Corretto
pkg:generic/amazon/amazon-corretto@21.0.3
# Oracle JDK
pkg:generic/oracle/jdk@11.0.16
# Oracle JRE
pkg:generic/oracle/jre@20

```

## Jenkins ecosystem collection

###### Supported applications

- Jenkins Core

###### Note

Vulnerability evaluation applies to Jenkins version 2.400.\* and higher.

###### Key features

- Extracts version information from `jenkins.war` file by reading the `META-INF/MANIFEST.M` file, which contains the Jenkins version string.

The Amazon Inspector SBOM Generator looks for Jenkins installations in common installation paths across platforms:

###### Linux

- `/usr/share/jenkins/jenkins.war`
- /usr/share/java/jenkins.war

###### macOS

- `/opt/homebrew/opt/jenkins-lts/libexec/jenkins.war`

###### Windows

- `/Program Files/Jenkins/Jenkins.war`
- `/Program Files (x86)/Jenkins/Jenkins.war`

###### Example files

The following are examples of `jenkins.war/META-INF/MANIFEST.MF` files for different releases.

```
Manifest-Version: 1.0
Created-By: Maven WAR Plugin 3.4.0
Build-Jdk-Spec: 21
Implementation-Title: Jenkins war
Main-Class: executable.Main
Implementation-Version: 2.516.2
Jenkins-Version: 2.516.2
```

```
Manifest-Version: 1.0
Jenkins-Version: 2.414.1
Implementation-Title: Jenkins
Implementation-Version: 2.414.1
Built-By: kohsuke
Created-By: Apache Maven 3.8.6
```

###### Sample PURLs

The following are package URLs for version 2.516.2 of the Jenkins LTS release and version 2.414 of the Jenkins automation server release.

```
LTS: pkg:generic/jenkins/jenkins-core-lts@2.516.2.1
Regular: pkg:generic/jenkins/jenkins-core@2.414
```

## MariaDB and MySQL ecosystem collection

### MariaDB

###### Supported applications

- MariaDB Server (10.6+, 11.x, 12.x)

###### Key features

- Extracts version information from database server binaries and header files using database-specific patterns.
- Identifies the directory path containing the database server installation.
- Automatically distinguishes between MariaDB and MySQL installations using data-driven file type detection.

The SBOM Generator looks for the MariaDB installation in common installation paths across platforms:

###### Linux

- `/usr/bin/mariadbd`
- `/usr/sbin/mariadbd`
- `/usr/local/bin/mariadbd`

###### macOS

- `C:/Program Files (x86)/MariaDB/include/mysql/mariadb_version.h (MariaDB)`
- `C:/Program Files/MariaDB/include/mysql/mariadb_version.h (MariaDB)`

###### Windows

- `C:/Program Files (x86)/MariaDB/include/mysql/mariadb_version.h (MariaDB)`
- `C:/Program Files/MariaDB/include/mysql/mariadb_version.h (MariaDB)`

###### Example PURL

The following is an example package URL for a MariaDB server.

```
# MariaDB Server

pkg:generic/mysql/mariadb-server@10.11.8
```

### MySQL ecosystem collection

###### Supported applications

- Oracle MySQL Server Server (8.0, 8.4, 9.4+)

###### Key features

- Extracts version information from database server binaries and header files using database-specific patterns.
- Identifies the directory path containing the database server installation.
- Automatically distinguishes between MySQL and MariaDB installations using data-driven file type detection.

The SBOM Generator looks for the MySQL installation in common installation paths across platforms:

###### Linux

- `/usr/local/bin/mysqld`
- `/usr/bin/mysqld`
- `/usr/sbin/mysqld`

###### macOS

- `/usr/local/mysql/include/mysql_version.h (MySQL)`

###### Windows

- `C:/Program Files/MySQL/MySQL Server/include/mysql_version.h (MySQL)`
- `C:/Program Files (x86)/MySQL/MySQL Server/include/mysql_version.h (MySQL)`

###### Example PURL

The following is an example package URL for a MySQL server.

```
# Oracle MySQL Server

pkg:generic/mysql/mysql-server@8.0.43
```

## Nginx ecosystem collection

###### Supported applications

- Nginx

###### Supported platforms

The following are supported platforms.

###### Linux

- /usr/sbin/nginx
- /usr/local/nginx
- /usr/local/etc/nginx
- /usr/local/nginx/nginx
- /usr/local/nginx/sbin/nginx
- /etc/nginx/nginx

###### Windows

- C:\nginx\nginx.exe
- C:\nginx-x.y.z\nginx.exe (x.y.z is an arbitrary version)

###### macOS

- /usr/local/etc/nginx/nginx

###### Key features

This collection examines binaries to extract embedded version information.
It searches for version strings in the binary executable `.rodata` section (for ELF binaries on Linux), `.rdata` section (for PE binaries on Windows), or `__ctring` section (for MachO binaries).

###### Example version string

The following is an example of a version string embedded in an Nginx binary.

```
nginx version: nginx/1.27.5
```

Version `1.27.5` is extracted to identify the Nginx version.

###### Example PURL

The following is an example package URL for Nginx.

```
Sample PURL: pkg:generic/nginx/nginx@1.27.5
```

## Node.JS runtime collection

###### Supported applications

- node runtime binary for Node.JS

###### Supported platforms

The following are supported platforms. (\* is an arbitrary version)

###### Linux

- /usr/local/bin/node
- /usr/bin/node
- /nodejs/bin/node
- ~/.nvm/versions/node/\*/bin/node
- ~/.local/share/fnm/node-versions/\*/installation/bin/node
- ~/.asdf/installs/nodejs/\*/bin/node
- ~/.local/share/mise/installs/node/\*/bin/node
- ~/.volta/tools/image/node/\*/bin/node

###### Windows

- C:\Program Files\nodejs\node.exe
- C:\Program Files (x86)\nodejs\node.exe
- ~\AppData\Roaming\fnm\node-versions\\\*\installation\node.exe

###### macOS

- /opt/homebrew/Cellar/node/\*/bin/node

###### Key features

This collection examines binaries to extract embedded version information.
It searches for version strings in the binary executable `.rodata` section (for ELF binaries on Linux), `.rdata` section (for PE binaries on Windows), or `__ctring` section (for MachO binaries).

###### Example version string

The following is an example of a version string embedded in an Node.JS runtime binary.

```
node.js/v24.11.1
```

Version `24.11.1` is extracted to identify the Node.JS runtime version.

###### Example PURL

The following is an example package URL for Node.JS.

```
Sample PURL: pkg:generic/nodejs/node@24.11.1
```

## OpenSSH ecosystem collection

###### Supported applications

- OpenSSH (Version 9)
- OpenSSH (Version 10)

###### Supported platforms Linux/macOS

- `/usr/sbin/sshd`
- `/usr/local/sbin/sshd`

###### Supported platforms Windows

- `C:/Windows/System32/OpenSSH/sshd.exe`
- `C:/Program Files/OpenSSH/sshd.exe`
- `C:/Program Files (x86)/OpenSSH/sshd.exe`
- `C:/OpenSSH/sshd.exe`

###### Key features

- Examines `sshd` binaries to extract embedded verion information.
- Looks for version strings in the binary executable `.rodata` section (for ELF binaries on Linux, `__cstring` section (for Mach-O binaries on MacOs), or `.rdata` section (for PE binaries on Windows).

###### Example version string

The following is an example of a version string embedded in an OpenSSH binary.

```
OpenSSH_9.9p2
```

Version `9.9p2` is extracted to identify the OpenSSH version.

###### Example PURL

The following is an example package URL for OpenSSH.

```
Sample PURL: pkg:generic/openssh/openssh@9.9p2
```

## OpenSSL ecosystem Collection

###### Supported applications

Support for OpenSSL libraries and development packages is limited to software built with official OpenSSL for 3.0.0 releases and above.
The software also must follow semantic versioning.
Custom or forked OpenSSL variants and versions lower than 3.0.0 are not supported.

The Amazon Inspector SBOM Generator extracts key package information for each installed OpenSSL instance.

###### Key features

- Extracts the base SEMVER version string from the OpenSSL header file
- Identifies the directory path containing the OpenSSL installation

The Amazon Inspector SBOM Generator looks for OpenSSL installations by scanning for the `opensslv.h` file in common installation paths across platforms.

###### Example installation path for Linux/Unix

The following is an example installation path for Linux/Unix.

```
/usr/local/include/openssl/opensslv.h
/usr/local/ssl/include/openssl/opensslv.h
/usr/local/openssl/include/openssl/opensslv.h
/usr/local/opt/openssl/include/openssl/opensslv.h
/usr/include/openssl/opensslv.h
```

The Amazon Inspector SBOM Generator extracts version information by parsing the `opensslv.h` file and looking for the version definitions.

```
# define OPENSSL_VERSION_MAJOR  3
# define OPENSSL_VERSION_MINOR  4
# define OPENSSL_VERSION_PATCH  0
```

###### Example PURL

The following is an example package URL for the OpenSSL version.

```
Sample PURL: pkg:generic/openssl/openssl@3.4.0
```

## Oracle Database Server collection

###### Supported applications

- Oracle Database

###### Supported platforms Linux

- `/opt/oracle`
- `/u01/app/oracle`

###### Note

Vulnerability evaluation applies only to Oracle Database Server version 19 and higher.

###### Key features

- Examines Oracle binaries to extract embedded version information.
- Looks for version strings in the binary executable `.rodata` section (for ELF binaries on Linux).
- Version information follows a specific format that includes the RDBMS version string.

###### Example version string

The following is an example of a version string embedded in an Oracle Database binary:

```
RDBMS_23.7.0.25.01DBRU_LINUX.X64_240304
```

Version `23.7.0.25.01` is extracted to identify the Oracle Database version.

###### Example PURL

The following is an example package URL for Oracle Database.

```
Sample PURL: pkg:generic/oracle/database@23.7.0.25.01
```

## PHP ecosystem collection

###### Supported applications

- PHP (version 8.1 and higher)

###### Key features

- Extracts version information from PHP binary executables using embedded version strings.
- Identifies the directory path containing the PHP binary.
- Automatically detects both standard PHP binaries and versioned installations, such as `php8.1`, `php8.2`, and `php8.3`.

The Amazon Inspector SBOM Generator looks for PHP installations in common installation paths across platforms:

###### Linux

- `usr/bin/php8.1 through /usr/bin/php8.9`
- `/usr/sbin/php8.1 through /usr/sbin/php8.9`
- `/usr/local/bin/php, /usr/bin/php, /usr/sbin/php`
- `/usr/local/bin/php8.1 through /usr/local/bin/php8.9` (versioned binaries)

###### macOS

- `/opt/homebrew/bin/php`
- `/usr/bin/php`
- `/usr/local/bin/php`

###### Windows

- `C:/php/php.exe`
- `C:/php8.1/php.exe through C:/php8.9/php.exe` (versioned directories)

###### Example PHP version extraction

The Amazon Inspector SBOM Generator extracts version information from PHP binaries by searching for embedded version strings using the following pattern.

```
X-Powered-By: PHP/8.4.12
```

`8.4.12` is extracted from this pattern to identify the PHP version.

###### Example PURL

The following is an example package URL for a PHP pattern.

```
pkg:generic/php/php@8.4.12
```

## WordPress ecosystem collection

###### Supported components

- WordPress core
- WordPress plugins
- WordPress themes

###### Key features

- WordPress core – parses the `/wp-includes/version.php` file to extract version value from $wp_version variable.
- WordPress plugins – parses the `/wp-content/plugins/<WordPress Plugin>/readme.txt` file or `/wp-content/plugins/<WordPress Plugin>/readme.md` file to extract the `Stable` tag as the version string.
- WordPress themes – parses the `/wp-content/themes/<WordPress Theme>/style.css` file to extract the version from the version metadata.

###### Example `version.php` file

The following is an example of a WordPress core `version.php` file.

```

// truncated

/**
* The WordPress version string.
*
* Holds the current version number for WordPress core. Used to bust caches
* and to enable development mode for scripts when running from the /src directory.
*
* @global string $wp_version
*/
$wp_version = '6.5.5';

// truncated

```

###### Example PURL

The following is an example package URL for WordPress core.

```

Sample PURL: pkg:generic/wordpress/core/wordpress@6.5.5

```

###### Example `readme.txt` file

The following is an example of a WordPress plugin `readme.txt` file.

```

=== Plugin Name ===
Contributors: (this should be a list of wordpress.org userid's)
Donate link: https://example.com/
Tags: tag1, tag2
Requires at least: 4.7
Tested up to: 5.4
Stable tag: 4.3
Requires PHP: 7.0
License: GPLv2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html

// truncated

```

###### Example PURL

The following is an example package URL for a WordPress plugin.

```

Sample PURL: pkg:generic/wordpress/plugin/exclusive-addons-for-elementor@1.0.0

```

###### Example `style.css` file

The following is an example of a WordPress theme `style.css` file.

```

/*
Author: the WordPress team
Author URI: https://wordpress.org
Description: Twenty Twenty-Four is designed to be flexible, versatile and applicable to any website. Its collection of templates and patterns tailor to different needs, such as presenting a business, blogging and writing or showcasing work. A multitude of possibilities open up with just a few adjustments to color and typography. Twenty Twenty-Four comes with style variations and full page designs to help speed up the site building process, is fully compatible with the site editor, and takes advantage of new design tools introduced in WordPress 6.4.
Requires at least: 6.4
Tested up to: 6.5
Requires PHP: 7.0
Version: 1.2
License: GNU General Public License v2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html
Text Domain: twentytwentyfour
Tags: one-column, custom-colors, custom-menu, custom-logo, editor-style, featured-images, full-site-editing, block-patterns, rtl-language-support, sticky-post, threaded-comments, translation-ready, wide-blocks, block-styles, style-variations, accessibility-ready, blog, portfolio, news
*/

```

###### Example PURL

The following is an example package URL for a WordPress theme.

```

Sample PURL: pkg:generic/wordpress/theme/avada@1.0.0

```

## Windows applicaitons ecosystem collection

###### Supported Windows Applications

- PowerShell
- NuGet CLI
- Visual Studio Code
- Microsoft Edge
- SharePoint Server
- Microsoft Defender
- Exchange Server
- Visual Studio
- .NET Runtime
- ASP.NET Core Runtime
- Microsoft Teams
- Outlook for Windows
- Microsoft Office
- Microsoft 365

###### Key features

- PowerShell – Examines the `pwsh.exe` file to extract the embedded version information.
- NuGet CLI – Examines the `nuget.exe` file to extract the embedded version information.
- Visual Studio Code – Examines the `Code.exe` file to extract the embedded version information.
- Microsoft Edge – Examines the `msedge.exe` file to extract the embedded version information.
- SharePoint Server – Examines the `Microsoft.SharePoint.dll` file to extract the embedded version information.
- Microsoft Defender – Examines the `MsMpEng.exe` file to extract the embedded version information.
- Exhange Server – Examines the `Exsetup.exe` file to extract the embedded version information.
- Visual Studio – Parses the `state.json` file to retrieve the version string from the `catalogInfo.productDisplayVersion` field.
- .NET Runtime – Searches for `Microsoft.NETCore.App.deps.json` file in installation paths and extracts the version string from the following file path pattern.

```
Microsoft.NETCore.App/<VERSION>/Microsoft.NETCore.App.deps.json
```

- ASP.NET Runtime – Searches for `Microsoft.AspNetCore.App.deps.json` file in installation paths and extracts the version string from the following file path pattern.

```
Microsoft.AspNetCore.App/<VERSION>/Microsoft.AspNetCore.App.deps.json
```

- Outlook for Windows – Parses Windows Registry, and extracts version from the following registry key.

```
HKLM\SOFTWARE\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppModel\PackageRepository\Packages\Microsoft.OutlookForWindows_<VERSION>_<ARCH>__8wekyb3d8bbwe
```

- Microsoft Teams – Parses Windows Registry, and extracts version from the following registry key.

```
HKLM\SOFTWARE\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppModel\PackageRepository\Packages\MSTeams_<VERSION>_<ARCH>__8wekyb3d8bbwee
```

- Microsoft Office 365 / Microsoft 365 – Parses Windows Registry, and extracts version from the following registry key and value.
  - Registry Key

  ```
  KEY_LOCAL_MACHINES\SOFTWARE\Microsoft\Office\ClickToRun\Configuration
  ```

  - Registry Value
    - VersionToReport – Microsoft Office Version
    - ProductReleaseIds – List of product IDs. This is used to identify installed Office products. For more information about product IDs, see [product IDs](https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/office-suite-issues/product-ids-supported-office-deployment-click-to-run "https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/office-suite-issues/product-ids-supported-office-deployment-click-to-run") on the Microsoft website.

- Microsoft Office Suite – Collects installed each Office applications by examining the following executable files:
  - `EXCEL.EXE` – Microsoft Excel
  - `WINWORD.EXE` – Microsoft Word
  - `POWERPNT.EXE` – Microsoft PowerPoint
  - `OUTLOOK.EXE` – Microsoft Outlook
    Version number in the Windows Registry is used as authoritative version number for each installed Office applications.

###### Example `state.json` file

The following is an example of a `state.json` file to use to collect installed Visual Studio version.

```
{
    "icon": {
        "mimeType": "image/svg+xml",
        "fileName": "product.svg"
    },
    "updateDate": "2025-11-06T05:05:35.6517471Z",
    "installDate": "2025-11-06T05:05:35.6527436Z",
    "enginePath": "C:\\Program Files (x86)\\Microsoft Visual Studio\\Installer\\resources\\app\\ServiceHub\\Services\\Microsoft.VisualStudio.Setup.Service",
    "installationName": "VisualStudio/17.14.19+36623.8",
    "catalogInfo": {
        "id": "VisualStudio/17.14.19+36623.8",
        "buildBranch": "d17.14",
        "buildVersion": "17.14.36623.8",
        "localBuild": "build-lab",
        "manifestName": "VisualStudio",
        "manifestType": "installer",
        "productDisplayVersion": "17.14.19",
// truncated
```

Example PURL

The following is an example package URL for each Windows applications.

```
// PowerShell
Sample PURL: pkg:generic/microsoft/powershell@7.5.3

// NuGet CLI
Sample PURL: pkg:generic/microsoft/nuget@6.14.0

// Visual Studio Code
Sample PURL: pkg:generic/microsoft/visualstudiocode@1.104.2

// Microsoft Edge
Sample PURL: pkg:generic/microsoft/edge@140.0.3485.94

// SharePoint Server
Sample PURL: pkg:generic/microsoft/sharepoint@23.38.219.1

// Microsoft Defender
Sample PURL: pkg:generic/microsoft/defender@4.18.23110.3

// Exchange Server
Sample PURL: pkg:generic/microsoft/exchangeserver@15.2.2562.17

// Visual Studio
Sample PURL: pkg:generic/microsoft/visualstudio@17.14.19

// .NET Runtime
Sample PURL: pkg:generic/microsoft/dotnet@8.0.18

// ASP.NET Core Runtime
Sample PURL: pkg:generic/microsoft/aspdotnet@8.0.18

// Microsoft Teams
Sample PURL: pkg:generic/microsoft/teams@25241.203.3947.4411

// Outlook for Windows
Sample PURL: pkg:generic/microsoft/outlookforwindows@1.2025.916.400

// Microsoft 365 / Office 365
Sample PURL: pkg:generic/microsoft/office@16.0.19127.20264?product_ids=O365HomePremRetail

// Microsoft Word
Sample PURL: pkg:generic/microsoft/word@16.0.19127.20264

// Microsoft Excel
Sample PURL: pkg:generic/microsoft/excel@16.0.19127.20264

// Microsoft PowerPoint
Sample PURL: pkg:generic/microsoft/powerpoint@16.0.19127.20264

// Microsoft Outlook
Sample PURL: pkg:generic/microsoft/outlook@16.0.19127.20264
```
