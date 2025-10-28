AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Using the AWS Cloud9 Installer for AWS Cloud9 SSH environments

Before you create an AWS Cloud9 SSH development environment, the cloud compute instance (for example an Amazon EC2
instance) or your own server that you want to connect to the environment must meet the [SSH Host Requirements](ssh-settings.md#ssh-settings-requirements "ssh-settings.md#ssh-settings-requirements"). One of these requirements
is that you must download and run the AWS Cloud9 Installer on the instance or server. The AWS Cloud9
Installer is a Linux shell script that checks whether the instance or server is running on an
operating system platform and architecture that AWS Cloud9 supports. If this check succeeds, the
script then attempts to install components and their dependencies that AWS Cloud9 requires to be on
the instance or server.

This topic describes how to download and run this installer script on the target instance
or server.

- [Download and Run the AWS Cloud9 Installer](#installer-download-run "#installer-download-run")
- [Troubleshooting the AWS Cloud9
  Installer](#installer-troubleshooting "#installer-troubleshooting")

## Download and Run the AWS Cloud9 Installer

1. Make sure the cloud compute instance or your own server that you want to connect
   to the environment meets the [SSH Host
   Requirements](ssh-settings.md#ssh-settings-requirements "ssh-settings.md#ssh-settings-requirements"). This includes having specific versions of Python and Node.js
   already installed, setting specific permissions on the directory that you want AWS Cloud9
   to start from after login, and setting up any associated Amazon Virtual Private Cloud.
2. While you are connected to the instance or server, run one of the following
   commands on that instance or server. You will need to install `gcc` before running one of the commands.

```
curl -L https://d3kgj69l4ph6w4.cloudfront.net/static/c9-install-2.0.0.sh | bash
wget -O - https://d3kgj69l4ph6w4.cloudfront.net/static/c9-install-2.0.0.sh | bash
```

3. If a **Done** message displays with no errors, you can [create the SSH environment](create-environment-ssh.md "create-environment-ssh.md").

If an error message displays, see the next section for troubleshooting
information.

## Troubleshooting the AWS Cloud9 Installer

This section describes common issues, possible causes, and recommended solutions for
troubleshooting AWS Cloud9 Installer errors.

If your issue isn't listed, or if you need additional help, see the [AWS Cloud9 Discussion Forum](https://forums.aws.amazon.com/forum.jspa?forumID=268 "https://forums.aws.amazon.com/forum.jspa?forumID=268").
(When you enter this forum, AWS might require you to sign in.) You can also [contact us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") directly.

- [-bash: wget: command not found](#installer-wget-not-found "#installer-wget-not-found")
- [Error: please install make to proceed](#installer-install-make "#installer-install-make")
- [Error: please install gcc to proceed](#installer-install-gcc "#installer-install-gcc")
- [configure: error: curses not found](#installer-install-curses "#installer-install-curses")

### -bash: wget: command not found

**Issue:** When you run the installer script, the following
message displays: `-bash: wget: command not found`.

**Possible cause:** The **`wget`** utility isn't installed on the instance or server.

**Recommended solution:** Run the installer script on the
instance or server with the **`curl`** utility instead.

### Error: please install make to proceed

**Issue:** When you run the installer script, the following
message displays: `Error: please install make to proceed`.

**Possible cause:** The **`make`** utility isn't installed on the instance or server.

**Recommended solution:** Install the **`make`** utility, and then try running the installer script on the instance or server
again.

To install the **`make`** utility, run one of the following commands on your instance or
server.

- For Amazon Linux, Amazon Linux 2, and Red Hat Enterprise Linux (RHEL) running in Amazon EC2:
  **`sudo yum -y groupinstall "Development Tools"`**
- For Ubuntu Server running in Amazon EC2: **`sudo apt install -y build-essential`**
- For SUSE: **`sudo zypper install -y make`**

### Error: please install gcc to proceed

**Issue:** When you run the installer script, the following
message displays: `Error: please install gcc to proceed`.

**Possible cause:** The **`gcc`** utility isn't installed on the instance or server.

**Recommended solution:** Install the **`gcc`** utility, and then try running the installer script on the instance or server
again.

To install the **`gcc`** utility, run one of the following commands on your instance or
server.

- For Amazon Linux, Amazon Linux 2, and Red Hat Enterprise Linux (RHEL) running in Amazon EC2:
  **`sudo yum -y groupinstall "Development Tools"`**
- For Ubuntu Server running in Amazon EC2: **`sudo apt install -y build-essential`**
- For SUSE: **`sudo zypper install -y gcc`**
- For other operating systems, see [Installing GCC](https://gcc.gnu.org/install/ "https://gcc.gnu.org/install/").

### configure: error: curses not found

**Issue:** When you run the installer script, the following
message displays: `configure: error: curses not found`.

**Possible cause:** The **`ncurses`** terminal control library isn't installed on the instance or server.

**Recommended solution:** Install the **`ncurses`** terminal control library (and, on some operating systems, the **`glibc-static`** library), and then try running the installer script on the instance or
server again.

To install the **`ncurses`** terminal control library (and, on some operating systems, the **`glibc-static`** library), run one of the following commands on your instance or
server:

- For Amazon Linux, Amazon Linux 2, and Red Hat Enterprise Linux (RHEL) running in Amazon EC2:
  **`sudo yum -y install ncurses-devel`**
- For SUSE: **`sudo zypper install -y ncurses-devel`** and **`sudo zypper install -y glibc-static`**
