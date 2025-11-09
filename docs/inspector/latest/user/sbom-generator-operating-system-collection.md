# Amazon Inspector SBOM Generator comprehensive operating system collection

The Amazon Inspector SBOM Generator scans different operating systems to guarantee a robust and detailed analysis of system components.
Generating an SBOM helps you understand the composition of your operating system, so you can identify vulnerabilities in system managed packages.
This topic describes key features of different operating system package collections the Amazon Inspector SBOM Generator supports.
For information about the operating systems that Amazon Inspector supports, see [Supported operating systems and programming languages for Amazon Inspector](supported.md "supported.md").

## Supported operating system artifacts

The Amazon Inspector SBOM Generator supports the following operating system artifacts:

| Platform     | Binary | Source | Stream |
| ------------ | ------ | ------ | ------ |
| Alma Linux   | N/A    | Yes    | Yes    |
| Alpine Linux | Yes    | Yes    | N/A    |
| Amazon Linux | N/A    | Yes    | N/A    |
| CentOS       | N/A    | Yes    | N/A    |
| Chainguard   | Yes    | Yes    | N/A    |
| Debian       | Yes    | Yes    | N/A    |
| Distroless   | Yes    | Yes    | N/A    |
| Fedora       | N/A    | Yes    | N/A    |
| MinimOS      | Yes    | Yes    | N/A    |
| OpenSUSE     | N/A    | Yes    | N/A    |
| Oracle Linux | N/A    | Yes    | N/A    |
| Photon OS    | N/A    | Yes    | N/A    |
| RHEL         | N/A    | Yes    | Yes    |
| Rocky Linux  | N/A    | Yes    | Yes    |
| SLES         | N/A    | Yes    | N/A    |
| Ubuntu       | Yes    | Yes    | N/A    |

## APK-based OS package collection

This section includes the supported platforms and key features for the APK-based OS package collection.
For more information, see [Alpine Package Keeper](https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper "https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper") on the Alpine Linux website.

### Supported platforms

The following are supported platforms.

- Alpine Linux

###### Note

For APK-based systems, the Amazon Inspector SBOM Generator collects package metadata from the [`/lib/apk/db/`](https://wiki.alpinelinux.org/wiki/Apk_spec "https://wiki.alpinelinux.org/wiki/Apk_spec") file.

### Key features

- **Package name collection** – Extracts the name of each installed package
- **Version collection** – Extracts the version of each installed package
- **Source package identification** – Identifies the source package for each installed package

### Example

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

This section includes the supported platforms and key features for the DPKG-based OS package collection.
For more information, see [Debian Package](https://wiki.debian.org/dpkg "https://wiki.debian.org/dpkg") on the Debian website.

### Supported platforms

The following platforms are supported.

- Debian
- Ubuntu

###### Note

For DPKG-based systems, the Amazon Inspector SBOM Generator collects package metadata from the [`/var/lib/dpkg/status`](https://www.debian.org/doc/manuals/debian-reference/ch02.en.html "https://www.debian.org/doc/manuals/debian-reference/ch02.en.html") file.

### Key features

The following are key features for DPKG-based OS packages.

- **Package name collection** – Extracts the name of each installed package
- **Version collection** – Extracts the version of each installed package
- **[Source package identification](https://www.debian.org/doc/debian-policy/ch-source.html "https://www.debian.org/doc/debian-policy/ch-source.html")** – Identifies the source package for each installed package

### Example

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

This section includes the supported platforms and key features for the RPM-based OS package collection.
For more information, see [RPM Package Manager](https://rpm.org/ "https://rpm.org/") on the RPM website.

### Supported platforms

The following platforms are supported.

- Alma Linux
- Amazon Linux
- CentOS
- Fedora
- OpenSUSE
- Oracle Linux
- PhotonOS
- RedHat Enterprise Linux
- Rocky Linux
- SUSE Linux Enterprise Server

###### Note

For RPM-based systems, the Amazon Inspector SBOM Generator collects package metadata from the [`/var/lib/rpm`](https://access.redhat.com/solutions/439953 "https://access.redhat.com/solutions/439953") file.

### Key features

The following are key features for RPM-based OS package collections.

- **Package name collection** – Extracts the name of each installed package
- **Version collection** – Extracts the version of each installed package
- **[Source package identification](https://www.debian.org/doc/debian-policy/ch-source.html "https://www.debian.org/doc/debian-policy/ch-source.html")** – Identifies the source package for each installed package
- **[Stream support](https://www.redhat.com/en/blog/introduction-appstreams-and-modules-red-hat-enterprise-linux "https://www.redhat.com/en/blog/introduction-appstreams-and-modules-red-hat-enterprise-linux")** – Extracts stream metadata of each installed package

### Example

The following is an example of an RPM database file snippet.

```

/usr/lib/sysimage/rpm/rpmdb.sqlite
/usr/lib/sysimage/rpm/Packages
/usr/lib/sysimage/rpm/Packages.db
/var/lib/rpm/rpmdb.sqlite
/var/lib/rpm/Packages
/var/lib/rpm/Packages.db

```

## Chainguard image package collection

This section includes the supported platforms and key features for Chainguard image package collection.
For more information, see [Images](https://edu.chainguard.dev/chainguard/chainguard-images/ "https://edu.chainguard.dev/chainguard/chainguard-images/") on the Chainguard website.

### Supported platforms

The following platforms are supported

- Wolfi Linux

###### Note

For Chainguard images, the Amazon Inspector SBOM Generator collects package metadata from the `/lib/apk/db/installed` file.

### Key features

The following are key features.

- **Package name collection** – Extracts the name of each installed package
- **Version collection** – Extracts the version of each installed package
- **Source package identification** – Identifies the source package for each installed package

### Example

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

Distroless containers are container images that exclude package managers, shells, and other utilities in Linux distributions.
Distroless containers only include essential dependencies required to run the application and improve performance and security.

###### Note

For [Distroless images](https://edu.chainguard.dev/chainguard/chainguard-images/about/getting-started-distroless/ "https://edu.chainguard.dev/chainguard/chainguard-images/about/getting-started-distroless/"), the Amazon Inspector SBOM Generator collects package metadata from the `/var/lib/dpkg/status.d` file.
Only Debian and Ubuntu-based distributions are supported.
These can be identified by the `NAME` field in the `/etc/os-release` file system, which shows "Debian" or "Ubuntu."

### Key features

- **Package name collection** – Extracts the name of each installed package
- **Version collection** – Extracts the version of each installed package

### Example

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

This section includes the supported platforms and key features for Minimus image package collection.
For more information, see the [Minimus](https://www.minimus.io/ "https://www.minimus.io/") website.

###### Supported platforms

The following platforms are supported.

- MinimOS

###### Note

For Minimus images, the Amazon Inspector SBOM Generator collects package metadata from the `/lib/apk/db/installed` file.

###### Key features

The following are key features.

- Package name collection – Extracts the name of each installed package
- Version collection – Extracts the name of each installed package
- Source package identification – Identifies the source package for each installed package

The following is a snippet of a Minimus image file.

```
P:ca-certificates-bundle
V:20241121-r1
A:aarch64
L:MPL-2.0 AND MIT
T:
o:ca-certificates
```
