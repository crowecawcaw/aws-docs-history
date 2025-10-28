# Installing Elemental Live on

qualified hardware

This section is for IT administrators who perform the first-time installation of AWS Elemental Live
software on a hardware unit that is considered _qualified
hardware_. For information about hardware that AWS Elemental considers to be
qualified hardware, contact your AWS Elemental Sales representative or contact AWS Elemental Support
through the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter").

To install Elemental Live, you work on two systems:

- A Windows, macOS, or Linux _workstation_ that has access to the public
  internet.

- The _hardware unit_
  (Elemental Live node) that you are setting up. This unit doesn't
  need access to the internet. In fact, we recognize that usually
  this unit won't have access.
  **Prerequisite knowledge**

We assume that you know how to do the following:

- Log in to the AWS Elemental hardware unit over Secure Shell (SSH) in
  order to run install commands via the command line
  interface.
- Use Windows Share (on a Windows workstation), Samba (on a
  macOS workstation), or a utility such as SCP (on a Linux
  workstation) to move files.
- Access recently downloaded files on your workstation.

###### Note

In this procedure, we show how
to install version 2.25.4 of the Elemental Live. Wherever an instruction shows
2.25.4, modify your commands to specify the version that you are installing.

###### Topics

- [Step A: Prepare hardware and
  download files](install-lv-ig-prep.md "install-lv-ig-prep.md")
- [Step B: Install
  (kickstart) the operating system software](install-lv-ig-install-ks.md "install-lv-ig-install-ks.md")
- [Step C: Install the
  Elemental Live software](install-lv-ig-install-sw.md "install-lv-ig-install-sw.md")
- [Step D: Set up
  licenses](install-lv-ig-licensing.md "install-lv-ig-licensing.md")
- [Step E: Complete node
  configuration](install-lv-ig-complete.md "install-lv-ig-complete.md")
