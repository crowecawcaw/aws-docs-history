# Alternative tools for patching

In addition to AWS Systems Manager, there are other automated patching tools that you might use, which are listed below. This list is not exhaustive, but is meant to give you a starting point for doing your own research if you decide to consider alternate tools.

## SUSE Manager

SUSE Manager is an infrastructure management tool for Linux systems. With SUSE manager, you can automate software management of SLES< RHEL and OEL operating systems. For more information, and a list of Amazon EC2 instances, see [SUSE Manager 4.0 Documentation](https://documentation.suse.com/external-tree/en-us/suma/4.0/suse-manager/index.html "https://documentation.suse.com/external-tree/en-us/suma/4.0/suse-manager/index.html").

## Repository Mirroring Tool (For SUSE Linux)

Repository Monitoring Tool (RMT) is a service from SUSE Linux that helps manage private repositories by downloading updates and distributing them across the landscape. This reduces network bandwidth usage and allows you to set more restrictive firewall policies. For more information, see the SUSE Linux [Repository Mirroring Tool Guide](https://documentation.suse.com/sles/15-SP1/single-html/SLES-rmt/index.html "https://documentation.suse.com/sles/15-SP1/single-html/SLES-rmt/index.html").

## Red Hat Satellite (For Red Hat Linux)

Red Hat Satellite is a system management solution that enables you to deploy, configure, and maintain your systems across physical, virtual, and cloud environments. Satellite Server synchronizes the content from the Red Hat Customer Portal and other sources, and provides functionality such as fine-grained lifecycle management, user and group role-based access control, integrated subscription management, as well as advanced GUI, CLI, or API access. For more information, see the [Red Hat Customer Portal](https://access.redhat.com/ "https://access.redhat.com/").

## KernelCare (For Red Hat Linux)

KernelCare is a live patching system that patches Linux kernel vulnerabilities automatically, with no reboots. It works with all major Linux distributions, such as RHEL, CentOS, Amazon Linux, and Ubuntu. It also interoperates with common vulnerability scanners such as Nessus, Tenable, Rapid7, and Qualys. For more information, see [KernelCare](https://aws.amazon.com/marketplace/pp/prodview-aksvbtgd4utj2 "https://aws.amazon.com/marketplace/pp/prodview-aksvbtgd4utj2") on AWS Marketplace.

## Zypper Package Manager (For SUSE Linux)

Zypper is a command-line package manager for installing updating, and removing packages. It can also be used to manage repositories. Zypper offers advantages over graphical package managers such as scripting actions. For more information, see the [Zypper package manager](https://documentation.suse.com/smart/linux/html/concept-zypper/index.html "https://documentation.suse.com/smart/linux/html/concept-zypper/index.html") documentation.
