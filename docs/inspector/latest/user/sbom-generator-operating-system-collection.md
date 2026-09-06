

# Amazon Inspector SBOM Generator comprehensive operating system collection
<a name="sbom-generator-operating-system-collection"></a>

 The Amazon Inspector SBOM Generator scans different operating systems to guarantee a robust and detailed analysis of system components. Generating an SBOM helps you understand the composition of your operating system, so you can identify vulnerabilities in system managed packages. This topic describes key features of different operating system package collections the Amazon Inspector SBOM Generator supports. For information about the operating systems that Amazon Inspector supports, see [Supported operating systems and programming languages for Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/supported.html). 

## Supported operating system artifacts
<a name="w2aac39c23b7"></a>

 The Amazon Inspector SBOM Generator supports the following operating system artifacts: 


| Platform | Binary | Source | Stream | 
| --- | --- | --- | --- | 
| Alma Linux | N/A | Yes | Yes | 
| Alpine Linux | Yes | Yes | N/A | 
| Amazon Linux | N/A | Yes | N/A | 
| CentOS | N/A | Yes | N/A | 
| Chainguard | Yes | Yes | N/A | 
| Debian | Yes | Yes | N/A | 
| Distroless | Yes | Yes | N/A | 
| Fedora | N/A | Yes | N/A | 
| MinimOS | Yes | Yes | N/A | 
| OpenSUSE | N/A | Yes | N/A | 
| Oracle Linux | N/A | Yes | N/A | 
| Photon OS | N/A | Yes | N/A | 
| RHEL | N/A | Yes | Yes | 
| Rocky Linux | N/A | Yes | Yes | 
| SLES | N/A | Yes | N/A | 
| Ubuntu | Yes | Yes | N/A | 
| Windows | N/A | N/A | N/A | 

## APK-based OS package collection
<a name="w2aac39c23b9"></a>

 This section includes the supported platforms and key features for the APK-based OS package collection. For more information, see [Alpine Package Keeper](https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper) on the Alpine Linux website. 

### Supported platforms
<a name="w2aac39c23b9b5"></a>

 The following are supported platforms. 
+  Alpine Linux 

**Note**  
 For APK-based systems, the Amazon Inspector SBOM Generator collects package metadata from the [`/lib/apk/db/`](https://wiki.alpinelinux.org/wiki/Apk_spec) file. 

### Key features
<a name="w2aac39c23b9b7"></a>
+  **Package name collection** – Extracts the name of each installed package 
+  **Version collection** – Extracts the version of each installed package 
+  **Source package identification** – Identifies the source package for each installed package 

### Example
<a name="w2aac39c23b9b9"></a>

 The following snippet is an example of an APK database file. 

```
C:Q1JlboSJkrN4qkDcokr4zenpcWEXQ=
P:zlib
V:1.2.13-r1
A:x86_64
S:54253
I:110592
T:A compression/decompression Library
U:https://zlib.net/
L:Zlib
o:zlib
```

## DPKG-based OS package collection
<a name="w2aac39c23c11"></a>

 This section includes the supported platforms and key features for the DPKG-based OS package collection. For more information, see [Debian Package](https://wiki.debian.org/dpkg) on the Debian website. 

### Supported platforms
<a name="w2aac39c23c11b5"></a>

 The following platforms are supported. 
+  Debian 
+  Ubuntu 

**Note**  
 For DPKG-based systems, the Amazon Inspector SBOM Generator collects package metadata from the [`/var/lib/dpkg/status`](https://www.debian.org/doc/manuals/debian-reference/ch02.en.html) file. 

### Key features
<a name="w2aac39c23c11b7"></a>

 The following are key features for DPKG-based OS packages. 
+  **Package name collection** – Extracts the name of each installed package 
+  **Version collection** – Extracts the version of each installed package 
+  **[Source package identification](https://www.debian.org/doc/debian-policy/ch-source.html)** – Identifies the source package for each installed package 

### Example
<a name="w2aac39c23c11b9"></a>

 The following snippet is an example of a `/var/lib/dpkg/` file. 

```
Package: zlib1g
Status: install ok installed
Priority: optional
Section: libs
Installed-Size: 168
Maintainer: Mark Brown <broonie@debian.org>
Architecture: amd64
Multi-Arch: same
Source: zlib
Version: 1:1.2.13.dfsg-1
Provides: libz1
Depends: libc6 (>= 2.14)
Breaks: libxml2 (<< 2.7.6.dfsg-2), texlive-binaries (<< 2009-12)
Conflicts: zlib1 (<= 1:1.0.4-7)
Description: compression library - runtime
 zlib is a library implementing the deflate compression method found
 in gzip and PKZIP.  This package includes the shared library.
Homepage: http://zlib.net/
```

## RPM-based OS package collection
<a name="w2aac39c23c13"></a>

 This section includes the supported platforms and key features for the RPM-based OS package collection. For more information, see [RPM Package Manager](https://rpm.org/) on the RPM website. 

### Supported platforms
<a name="w2aac39c23c13b5"></a>

 The following platforms are supported. 
+  Alma Linux 
+  Amazon Linux 
+  CentOS 
+  Fedora 
+  OpenSUSE 
+  Oracle Linux 
+  PhotonOS 
+  RedHat Enterprise Linux 
+  Rocky Linux 
+  SUSE Linux Enterprise Server 

**Note**  
 For RPM-based systems, the Amazon Inspector SBOM Generator collects package metadata from the [`/var/lib/rpm`](https://access.redhat.com/solutions/439953) file. 

### Key features
<a name="w2aac39c23c13b7"></a>

 The following are key features for RPM-based OS package collections. 
+  **Package name collection** – Extracts the name of each installed package 
+  **Version collection** – Extracts the version of each installed package 
+  **[Source package identification](https://www.debian.org/doc/debian-policy/ch-source.html)** – Identifies the source package for each installed package 
+  **[Stream support](https://www.redhat.com/en/blog/introduction-appstreams-and-modules-red-hat-enterprise-linux)** – Extracts stream metadata of each installed package 

### Example
<a name="w2aac39c23c13b9"></a>

 The following is an example of an RPM database file snippet. 

```
/usr/lib/sysimage/rpm/rpmdb.sqlite
/usr/lib/sysimage/rpm/Packages
/usr/lib/sysimage/rpm/Packages.db
/var/lib/rpm/rpmdb.sqlite
/var/lib/rpm/Packages
/var/lib/rpm/Packages.db
```

## Windows OS version collection
<a name="w2aac39c23c15"></a>

 Unlike Linux-based operating systems, Windows does not use a package management system for the operating system itself. The Amazon Inspector SBOM Generator collects only the Windows OS version information. For Windows application scanning, use the windows-apps scanner instead. The windows-apps scanner collects information about installed applications on Windows systems. For more information, See [Microsoft applications ecosystem collection](sbom-generator-ecosystem-collection.md#microsoft-app-ecosystem-collection). 

### Key features
<a name="w2aac39c23c15b5"></a>
+  **OS version collection** – Extracts the Windows OS version from the Windows Registry. The extracted OS version is used for vulnerability detection for Windows OS. 

### Registry keys and values
<a name="w2aac39c23c15b7"></a>

 The following Windows Registry keys and values are used to collect OS name and version information. 
+ **Registry Key** 

  ```
  HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion
  ```
+  **Registry Value** 
  +  ProductName – OS name and edition (e.g., "Windows Server 2025 Datacenter") 
  +  CurrentMajorVersionNumber – the major version of OS 
  +  CurrentMinorVersionNumber – The minor version of OS 
  +  CurrentBuild – The build number of OS 
  +  UBR – The revision number of OS 

## Chainguard image package collection
<a name="w2aac39c23c17"></a>

 This section includes the supported platforms and key features for Chainguard image package collection. For more information, see [Images](https://edu.chainguard.dev/chainguard/chainguard-images/) on the Chainguard website. 

### Supported platforms
<a name="w2aac39c23c17b5"></a>

 The following platforms are supported 
+  Wolfi Linux 

**Note**  
 For Chainguard images, the Amazon Inspector SBOM Generator collects package metadata from the `/lib/apk/db/installed` file. 

### Key features
<a name="w2aac39c23c17b7"></a>

 The following are key features. 
+  **Package name collection** – Extracts the name of each installed package 
+  **Version collection** – Extracts the version of each installed package 
+  **Source package identification** – Identifies the source package for each installed package 

### Example
<a name="w2aac39c23c17b9"></a>

 The following snippet is an example of a Chainguard image file. 

```
P:wolfi-keys
V:1-r8
A:x86_64
L:MIT
T:Wolfi signing keyring
o:wolfi-keys
```

## Distroless image package collection
<a name="w2aac39c23c19"></a>

 Distroless containers are container images that exclude package managers, shells, and other utilities in Linux distributions. Distroless containers only include essential dependencies required to run the application and improve performance and security. 

**Note**  
 For [Distroless images](https://edu.chainguard.dev/chainguard/chainguard-images/about/getting-started-distroless/), the Amazon Inspector SBOM Generator collects package metadata from the `/var/lib/dpkg/status.d` file. Only Debian and Ubuntu-based distributions are supported. These can be identified by the `NAME` field in the `/etc/os-release` file system, which shows "Debian" or "Ubuntu." 

### Key features
<a name="w2aac39c23c19b7"></a>
+  **Package name collection** – Extracts the name of each installed package 
+  **Version collection** – Extracts the version of each installed package 

### Example
<a name="w2aac39c23c19b9"></a>

 The following is an example of a Distroless image file. 

```
Package: tzdata
Version: 2021a-1+deb11u10
Architecture: all
Maintainer: GNU Libc Maintainers <debian-glibc@lists.debian.org>
Installed-Size: 3413
Depends: debconf (>= 0.5) | debconf-2.0
Provides: tzdata-bullseye
Section: localization
Priority: required
Multi-Arch: foreign
Homepage: https://www.iana.org/time-zones
Description: time zone and daylight-saving time data
 This package contains data required for the implementation of
 standard local time for many representative locations around the
 globe. It is updated periodically to reflect changes made by
 political bodies to time zone boundaries, UTC offsets, and
 daylight-saving rules.
```

## MinimOS package collection
<a name="w2aac39c23c21"></a>

 This section includes the supported platforms and key features for Minimus image package collection. For more information, see the [Minimus](https://www.minimus.io/) website. 

**Supported platforms**  
 The following platforms are supported. 
+  MinimOS 

**Note**  
 For Minimus images, the Amazon Inspector SBOM Generator collects package metadata from the `/lib/apk/db/installed` file. 

**Key features**  
 The following are key features. 
+  Package name collection – Extracts the name of each installed package 
+  Version collection – Extracts the name of each installed package 
+  Source package identification – Identifies the source package for each installed package 

 The following is a snippet of a Minimus image file. 

```
P:ca-certificates-bundle
V:20241121-r1
A:aarch64
L:MPL-2.0 AND MIT
T:
o:ca-certificates
```

## Docker Hardened Images package collection
<a name="w2aac39c23c23"></a>

 [Docker Hardened Images](https://docs.docker.com/dhi/) (DHI) are minimal, security-hardened container images. The Amazon Inspector SBOM Generator detects DHI images and namespaces their packages under `dhi` so that vulnerabilities are matched against the hardened distribution. 

### Detection
<a name="w2aac39c23c23b5"></a>

 DHI version 2 images report `ID=dhi` in the `/etc/os-release` file, with `ID_LIKE=alpine` or `ID_LIKE=debian` indicating the underlying base operating system. The Amazon Inspector SBOM Generator detects DHI images directly from this `ID` value and does not parse the `PRETTY_NAME` field. 

**Example `/etc/os-release` file**  
 The following is an example of an `/etc/os-release` file for a Debian-based DHI image. 

```
ID=dhi
ID_LIKE=debian
```

### Package namespace
<a name="w2aac39c23c23b7"></a>

 Every package in a DHI image is namespaced under `dhi`, yielding a Package URL of the form `pkg:deb/dhi/<name>@<version>` or `pkg:apk/dhi/<name>@<version>`. The PURL type (`deb` or `apk`) reflects the underlying base operating system. 

**Example PURL**  
 The following are example package URLs for packages in DHI images. 

```
# Debian-based DHI image
pkg:deb/dhi/<name>@<version>

# Alpine-based DHI image
pkg:apk/dhi/<name>@<version>
```

### Hardened-image markers
<a name="w2aac39c23c23b9"></a>

 When the Amazon Inspector SBOM Generator detects `ID=dhi`, it annotates the image with hardened-image markers: 
+  The operating-system component name is annotated with `<base> (Docker Hardened Image)` – for example, `Debian GNU/Linux (Docker Hardened Image)`. 
+  The container or operating-system component carries the `amazon:inspector:sbom_generator:hardened_image:vendor` property with a value of `Docker`. 

**Note**  
 DHI detection applies to container, localhost, and volume scans. 