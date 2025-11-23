# Amazon Inspector Dockerfile checks

This section describes how to use the Amazon Inspector SBOM Generator to scan Dockerfiles and Docker container images for misconfigurations that introduce security vulnerabilities.

###### Topics

- [Using Sbomgen Dockerfile checks](#w2aac39c13b7 "#w2aac39c13b7")
- [Supported Dockerfile checks](#w2aac39c13b9 "#w2aac39c13b9")

## Using Sbomgen Dockerfile checks

Dockerfile checks are conducted automatically when a file named `Dockerfile` or `*.Dockerfile` is discovered and when a Docker image is scanned.

You can disable Dockerfile checks using the `--skip-scanners dockerfile` argument.
You also can combine Dockerfile checks with any available scanner, such as OS or 3rd-party packages.

###### Example Docker check commands

The following example commands show how to generate SBOMs for Dockerfiles and Docker container images, as well as for OS and 3rd-party packages.

```
# generate SBOM only containing Docker checks for Dockerfiles in a local directory
./inspector-sbomgen directory --path ./project/ --scanners dockerfile

# generate SBOM for container image will by default include Dockerfile checks
./inspector-sbomgen container --image image:tag

# generate SBOM only containing Docker checks for specific Dockerfiles and Alpine, Debian, and Rhel OS packages in a local directory
/inspector-sbomgen directory --path ./project/ --scanners dockerfile,dpkg,alpine-apk,rhel-rpm

# generate SBOM only containing Docker checks for specific Dockerfiles in a local directory
./inspector-sbomgen directory --path ./project/ --skip-scanners dockerfile
```

###### Example file component

The following is an example of a Dockerfile finding for a file component.

```
{
     "bom-ref": "comp-2",
      "name": "dockerfile:data/docker/Dockerfile",
      "properties": [
        {
          "name": "amazon:inspector:sbom_scanner:dockerfile_finding:IN-DOCKER-001",
          "value": "affected_lines:27-27"
        }
      ],
      "type": "file"
    },
```

###### Example vulnerability response component

The following is an example of a Dockerfile finding for a vulnerability response component.

```
{
      "advisories": [
        {
          "url": "https://docs.docker.com/develop/develop-images/instructions/"
        }
      ],
      "affects": [
        {
          "ref": "comp-2"
        }
      ],
      "analysis": {
        "state": "in_triage"
      },
      "bom-ref": "vuln-13",
      "created": "2024-03-27T14:36:39Z",
      "description": "apt-get layer caching: Using apt-get update alone in a RUN statement causes caching issues and subsequent apt-get install instructions to fail.",
      "id": "IN-DOCKER-001",
      "ratings": [
        {
          "method": "other",
          "severity": "info",
          "source": {
            "name": "AMAZON_INSPECTOR",
            "url": "https://aws.amazon.com/inspector/"
          }
        }
      ],
      "source": {
        "name": "AMAZON_INSPECTOR",
        "url": "https://aws.amazon.com/inspector/"
      },
      "updated": "2024-03-27T14:36:39Z"
    },
```

###### Note

If you invoke Sbomgen without the `--scan-sbom` flag, you can only view raw Dockerfile findings.

## Supported Dockerfile checks

Sbomgen Dockerfile checks are supported for the following:

- The Sudo binary package
- Debian APT utilities
- Hardcoded secrets
- Root containers
- Runtime weakening command flags
- Runtime weakening environment variables

Each of these Dockerfile checks has a corresponding severity rating, which is noted at the top of the following topics.

###### Note

The recommendations described in the following topics are based on industry best practices.

### The Sudo binary package

###### Note

The severity rating for this check is **Info**.

We recommend not installing or using the Sudo binary package because it has unpredictable TTY and signal-forwarding behavior.
For more information, see [User](https://docs.docker.com/build/building/best-practices/#user "https://docs.docker.com/build/building/best-practices/#user") in the Docker Docs website.
If your use case requires functionality similar the Sudo binary package, we recommened using [Gosu](https://github.com/tianon/gosu "https://github.com/tianon/gosu").

### Debian APT utilities

###### Note

The severity rating for this check is **High**.

The following are best practices for using Debian APT utilities.

######

Combining `apt-get` commands in a single `Run` statement to avoid caching issues

We recommend combining `apt-get` commands in a single RUN statement inside of your Docker container.
Using `apt-get update` by itself results in caching issues and subsequent `apt-get install` instructions to fail.
For more information, see [apt-get](https://docs.docker.com/build/building/best-practices/#apt-get "https://docs.docker.com/build/building/best-practices/#apt-get") in the Docker Docs website.

###### Note

The caching behavior described also can occur inside of your Docker container if the Docker container software is out of date.

###### Using the APT command-line utility in a non-interactive manner

We recommend using the APT command-line utility interactively.
The APT command-line utility is designed as an end-user tool, and its behavior changes between versions.
For more information, see [Script Usage and differences from other APT tools](https://manpages.debian.org/stretch/apt/apt.8.en.html#SCRIPT_USAGE_AND_DIFFERENCES_FROM_OTHER_APT_TOOLS "https://manpages.debian.org/stretch/apt/apt.8.en.html#SCRIPT_USAGE_AND_DIFFERENCES_FROM_OTHER_APT_TOOLS") in the Debian website.

### Hard-coded secrets

###### Note

The severity rating for this check is **Critical**.

Confidential information in your Dockerfile is considered a hard-coded secret.
The following hard-coded secrets can be identified through Sbomgen Docker file checks:

- AWS access key IDs – `AKIAIOSFODNN7EXAMPLE`
- AWS secret keys – `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`
- DockerHub personal access tokens – `dckr_pat_thisisa27charexample1234567`
- GitHub personal access tokens – `ghp_examplev61wY7Pj1YnotrealUoY123456789`
- GitLab personal access tokens – `glpat-12345example12345678`

### Root containers

###### Note

The severity marker for this check is **Info**.

We recommend running Docker containers without root privileges.
For containerized workloads that cannot run without root privileges, we recommend building your applications using a principle with the least amount of privileges.
For more information, see [User](https://docs.docker.com/build/building/best-practices/#user "https://docs.docker.com/build/building/best-practices/#user") in the Docker Docs website.

### Runtime weakening environment variables

###### Note

The severity rating for this check is **High**.

Several command line utilities or programming language runtimes support bypassing secure defaults, which allows execution through insecure methods.

###### NODE_TLS_REJECT_UNAUTHORIZED=0

When Node.js processes run with `NODE_TLS_REJECT_UNAUTHORIZED` set to `0`, TLS certificate validation is disabled.
For more information, see [NODE_TLS_REJECT_UNAUTHORIZED=0](https://nodejs.org/api/cli.html#node_tls_reject_unauthorizedvalue "https://nodejs.org/api/cli.html#node_tls_reject_unauthorizedvalue") in the Node.js website.

###### GIT_SSL_NO_VERIFY=\*

When git command line processes run with `GIT_SSL_NO_VERIFY` set, Git skips verifying TLS certificates.
For more information, see [Environment variables](https://git-scm.com/book/en/v2/Git-Internals-Environment-Variables "https://git-scm.com/book/en/v2/Git-Internals-Environment-Variables") in the Git website.

###### PIP_TRUSTED_HOST=\*

When Python pip command line processes run with `PIP_TRUSTED_HOST` set, Pip skips verifying TLS certificates on the specified domain.
For more information, see [--trusted-host](https://pip.pypa.io/en/stable/cli/pip/#cmdoption-trusted-host "https://pip.pypa.io/en/stable/cli/pip/#cmdoption-trusted-host") in the Pip website.

###### NPM_CONFIG_STRICT_SSL=false

When Node.js npm command line processes run with `NPM_CONFIG_STRICT_SSL` set to false, the Node Package Manager (npm) utility will connect to the NPM registry without validating TLS certificates.
For more information, see [strict-ssl](https://docs.npmjs.com/cli/v10/using-npm/config#strict-ssl "https://docs.npmjs.com/cli/v10/using-npm/config#strict-ssl") in the npm Docs website website.

### Runtime weakening command flags

###### Note

The severity rating for this check is **High**.

Similar to runtime weakening environment variables, several command line utilities or programming language runtimes support bypassing secure defaults, which allows execution through insecure methods.

###### `npm ––strict-ssl=false`

When Node.js npm command line processes are run with the `--strict-ssl=false` flag, the Node Package Manager (npm) utility connects to the NPM registry without validating TLS certificates.
For more information, see [strict-ssl](https://docs.npmjs.com/cli/v10/using-npm/config#strict-ssl "https://docs.npmjs.com/cli/v10/using-npm/config#strict-ssl") in the npm Docs website.

###### `apk ––allow-untrusted`

When the Alpine Package Keeper utility is run with the `--allow-untrusted` flag, `apk` will install packages with no or untrusted signatures.
For more information, see [the following repository](https://gitlab.alpinelinux.org/alpine/apk-tools/-/blob/f9eaeb6429325eeb5a17ed771fd477be9227fe15/doc/apk.8.scd#L114-115 "https://gitlab.alpinelinux.org/alpine/apk-tools/-/blob/f9eaeb6429325eeb5a17ed771fd477be9227fe15/doc/apk.8.scd#L114-115") in the Apline website.

###### `apt-get ––allow-unauthenticated`

When the Debian `apt-get` package utility is run with the `--allow-unauthenticated` flag, `apt-get` doesn't check package validity.
For more information, see [APT-Get(8)](https://manpages.debian.org/stretch/apt/apt-get.8.en.html "https://manpages.debian.org/stretch/apt/apt-get.8.en.html") in the Debian website.

###### `pip ––trusted-host`

When the Python pip utility is run with the `--trusted-host` flag, the specified hostname will bypass TLS certificate validation.
For more information, see [--trusted-host](https://pip.pypa.io/en/stable/cli/pip/#cmdoption-trusted-host "https://pip.pypa.io/en/stable/cli/pip/#cmdoption-trusted-host") in the Pip website.

###### `rpm ––nodigest, ––nosignature, ––noverify, ––nofiledigest`

When the RPM-based package manager `rpm` is run with the `--nodigest`, `--nosignature`, `--noverify`, and `--nofiledigest` flags, the RPM package manager doesn't validate package headers, signatures, or files when installing a package.
For more information, see the following [RPM manual page](https://rpm-software-management.github.io/rpm/man/ "https://rpm-software-management.github.io/rpm/man/") in the RPM website.

###### `yum-config-manager ––setopt=sslverify false`

When the RPM-based package manager `yum-config-manager` is run with the `--setopt=sslverify` flag set to false, the YUM package manager doesn't validate TLS certificates.
For more information, see the following [YUM manual page](https://man7.org/linux/man-pages/man5/yum.conf.5.html "https://man7.org/linux/man-pages/man5/yum.conf.5.html") in the Man7 website.

###### `yum ––nogpgcheck`

When the RPM-based package manager `yum` is run with the `--nogpgcheck` flag, the YUM package manager skips checking GPG signatures on packages.
For more information, see [yum(8)](https://man7.org/linux/man-pages/man8/yum.8.html "https://man7.org/linux/man-pages/man8/yum.8.html") in the Man7 website.

###### `curl ––insecure, curl –k`

When `curl` is run with the `--insecure` or `-k` flag, TLS certificate validation is disabled.
By default, every secure connection that `curl` makes is verified to be secure before the transfer takes place.
This option makes `curl` skip the verification step and proceed without checking.
For more information, see the following [Curl manual page](https://curl.se/docs/manpage.html#-k "https://curl.se/docs/manpage.html#-k") in the Curl website.

###### `wget ––no-check-certificate`

When `wget` is run with the `--no-check-certificate` flag, TLS certificate validation is disabled.
For more information, see the following [Wget manual page](https://www.gnu.org/software/wget/manual/wget.html#index-SSL-certificate_002c-check "https://www.gnu.org/software/wget/manual/wget.html#index-SSL-certificate_002c-check") in the GNU website.

### Removal checks for OS package databases within containers

###### Note

The severity rating for this check is **Info**.

The removal of an operating system package database reduces the ability to scan the complete inventory of a container image's software.
These databases should be left intact during container build steps.

Removal checks for an OS package database is supported for the following package managers:

###### Alpine Package Keeper (APK)

Container images utilizing the APK package manager for installed software must make sure APK system files are not removed during a build.
For more information, see the [APK manpages](https://man.archlinux.org/man/apk.8.en#System_files "https://man.archlinux.org/man/apk.8.en#System_files") system files documentation on the Arch Linux website.

###### Debian Package Manager (DPKG)

Containers utilizing the DPKG package manager, such as Debian, Ubuntu, or Distroless based images, must make sure the DPKG database are not removed during a container build.
For more information, see the [DPKG manpages](https://manpages.ubuntu.com/manpages/trusty/man1/dpkg.1.html#files "https://manpages.ubuntu.com/manpages/trusty/man1/dpkg.1.html#files") system files documentation on the Ubuntu website.

###### RPM Package Manager (RPM)

Containers utilizing the RPM Package Manager (yum/dnf), such as Amazon Linux or Red Hat Enterprise Linux, must make sure the RPM database is not removed during a container build.
For more information, see the [RPM manpages](https://rpm-software-management.github.io/rpm/man/rpm-common.8#FILES "https://rpm-software-management.github.io/rpm/man/rpm-common.8#FILES") system files documentation on the RPM website.
