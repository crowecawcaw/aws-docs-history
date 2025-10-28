# Tutorial: Get started with Lightsail for Research virtual computers

Use this tutorial to get started with Amazon Lightsail for Research virtual computers. You'll learn how to
create, connect to, and use a virtual computer. In Lightsail for Research, a virtual computer is a research
workstation that you create and manage in the AWS Cloud. Virtual computers are based on
Lightsail Linux instances with the Ubuntu operating system. On your virtual computer, you can
preconfigure a research application like JupyterLab, RStudio, Scilab, and more.

The virtual computer that you create in this tutorial will incur usage fees from the time
that you create the virtual computer until you delete it. Deletion is the final step of this
tutorial. For more information about pricing, see [Lightsail for Research pricing](https://aws.amazon.com/lightsail/pricing/#lightsail-for-research "https://aws.amazon.com/lightsail/pricing/#lightsail-for-research").

###### Topics

- [Step 1: Complete the prerequisites](#getting-started-prerequisite "#getting-started-prerequisite")
- [Step 2: Create a virtual computer](#getting-started-step1 "#getting-started-step1")
- [Step 3: Launch a virtual computer's application](#getting-started-step2 "#getting-started-step2")
- [Step 4: Connect to your virtual computer](#getting-started-step3 "#getting-started-step3")
- [Step 5: Add storage to your virtual computer](#getting-started-step4 "#getting-started-step4")
- [Step 6: Create a snapshot](#getting-started-step5 "#getting-started-step5")
- [Step 7: Clean up](#getting-started-cleanup "#getting-started-cleanup")

## Step 1: Complete the prerequisites

If you're a new AWS customer, complete the setup prerequisites before you start using
Amazon Lightsail for Research. For more information, see [Setting up Amazon Lightsail for Research](setting-up.md "setting-up.md").

## Step 2: Create a virtual computer

You can create a virtual computer by using the [Lightsail for Research console](https://lfr.console.aws.amazon.com/ls/research "https://lfr.console.aws.amazon.com/ls/research") as described in the
following procedure. This tutorial is intended to help you quickly launch your first virtual
computer. We also recommend exploring the available applications and hardware plans. For more
information, see [Choose application images and hardware plans for
Lightsail for Research](blueprints-plans.md "blueprints-plans.md") and [Create a Lightsail for Research virtual computer](create-computer.md "create-computer.md").

1. Sign in to the [Lightsail for Research console](https://lfr.console.aws.amazon.com/ls/research "https://lfr.console.aws.amazon.com/ls/research").
2. On the home page, choose **Create virtual computer**.
3. Select an AWS Region for your virtual computer.

Choose a AWS Region that is closest to your physical location to reduce latency. 4. Choose an application, also known as a blueprint in the Lightsail API.

The application you choose is installed and configured on your virtual computer when you
create it. 5. Choose a hardware plan, also known as a bundle in the Lightsail API.

Hardware plans offer different amounts of processing power including vCPU cores, memory,
storage, and monthly data transfer. Lightsail for Research offers standard plans and GPU plans for virtual
computers. Choose a standard plan when the computational requirement of your work is low.
Choose a GPU plan when that requirement is high, such as when running machine learning models
or other computationally intensive tasks. 6. Enter a name for your virtual computer. 7. Choose **Create virtual computer** in the **Summary**
panel.

After your new virtual computer is up and running, continue to the next step of this
tutorial to learn how to launch the computer's application.

## Step 3: Launch a virtual computer's application

After you create a virtual computer and it's in a _Running_ state, you
can launch a virtual session in your web browser. With the session, you can interact with and
manage the application that's installed on your virtual computer.

1. Choose **Virtual computers** in the navigation pane of the Lightsail for Research
   console.
2. Locate the name of the virtual computer that you created in **Step
   1**, and choose **Launch application**. For example,
   **Launch JupyterLab**. An application session opens in a new web browser
   window.

###### Important

If your web browser has a pop-up blocker installed, you might need to allow pop-ups from
the **aws.amazon.com** domain before opening your session.

To learn how to connect to your virtual computer, continue to the next step of this
tutorial.

## Step 4: Connect to your virtual computer

You can connect to your virtual computer using the following methods:

- Use the browser-based Amazon DCV client available in the Lightsail for Research console. With Amazon DCV, you can use
  a graphical user interface (GUI) to interact with your research application and your virtual
  computer’s operating system.

You can also access your virtual computer’s command line interface and transfer files by
using the browser-based Amazon DCV client.

- Use a secure shell (SSH) client such as OpenSSH, PuTTY, or Windows Subsystem for Linux to
  access your virtual computer’s command line interface. With an SSH client, you can edit scripts
  and configuration files.
- Use Secure Copy (SCP) to securely transfer files between your local computer and your
  virtual computer. With SCP, you can start your work locally and continue it on your virtual
  computer. You can also download files from your virtual computer to copy your work to your
  local computer.

You must provide your virtual computer's key pair to connect to it using SSH or to transfer
files using SCP. A key pair is a set of security credentials that you use to prove your identity
when connecting to a Lightsail for Research virtual computer. A key pair consists of a public key and a private
key.

For more information about connecting to your virtual computer, see the following
documentation:

- Establish a remote display protocol connection:
  - [Access a Lightsail for Research virtual computer
    application](open-computer-application.md "open-computer-application.md")
  - [Access your Lightsail for Research virtual computer's
    operating system](access-computer-operating-system.md "access-computer-operating-system.md")

- Establish an SSH connection or transfer files using SCP:
  - [Get a key pair for a Lightsail for Research virtual computer](get-ssh-keys.md "get-ssh-keys.md")
  - [Connect to a Lightsail for Research virtual computer using Secure
    Shell](connect-using-ssh.md "connect-using-ssh.md")
  - [Transfer files to Lightsail for Research virtual computers using
    Secure Copy](connect-using-scp.md "connect-using-scp.md")

To learn about storage for your virtual computer, continue to the next step of this
tutorial.

## Step 5: Add storage to your virtual computer

Lightsail for Research provides block-level storage volumes (disks) that you can attach to a virtual
computer. Even though your virtual computer comes with a system disk, you can attach additional
disks to your virtual computer as your storage needs change. You can also detach a disk from a
virtual computer and attach it to another virtual computer.

When you attach a disk to your virtual computer using the console, Lightsail for Research automatically
formats and mounts the disk in your operating system. This process takes a few minutes, so you
should confirm that the disk is in _Mounted_ status before you start using
it.

For more information about creating, attaching, and managing a disk, see the following
documentation:

- [Create a storage disk in the Lightsail for Research console](create-disk.md "create-disk.md")
- [View storage disk details in the Lightsail for Research console](view-disk.md "view-disk.md")
- [Add storage to a virtual computer in Lightsail for Research](attach-disk.md "attach-disk.md")
- [Detach a disk from a virtual computer in Lightsail for Research](detach-disk.md "detach-disk.md")
- [Delete unused storage disks in Lightsail for Research](delete-disk.md "delete-disk.md")

To learn about backing up your virtual computer, continue to the next step of this
tutorial.

## Step 6: Create a snapshot

Snapshots are a point-in-time copy of your data. You can create snapshots of your virtual
computers and use them as baselines to create new computers or for data backup. A snapshot
contains all of the data that's needed to restore your computer (from the moment when the
snapshot was taken).

For more information about creating and managing snapshots, see the following
documentation:

- [Create snapshots of Lightsail for Research virtual computers or
  disks](create-snapshot.md "create-snapshot.md")
- [View and manage virtual computer and disk snapshots in
  Lightsail for Research](view-snapshots.md "view-snapshots.md")
- [Create a virtual computer or disk from a
  snapshot](create-computer-from-snapshot.md "create-computer-from-snapshot.md")
- [Delete a snapshot in the Lightsail for Research console](delete-snapshot.md "delete-snapshot.md")

To learn about cleaning up your virtual computer resources, continue to the next step of
this tutorial.

## Step 7: Clean up

After you're done with the virtual computer that you created for this tutorial, you can
delete it. This stops incurring charges for the virtual computer if you don't need it.

Deleting a virtual computer doesn't delete its associated snapshots or attached disks. If
you created snapshots and disks, you should delete those manually to stop incurring charges for
them.

To save your virtual computer for later, but to avoid incurring charges at standard hourly
prices, you can stop the virtual computer instead of deleting it. Then you can start it again
later. For more information, see [View Lightsail for Research virtual computer details](view-computer.md "view-computer.md").
For more information about pricing, see [Lightsail for Research pricing](https://aws.amazon.com/lightsail/pricing/#lightsail-for-research "https://aws.amazon.com/lightsail/pricing/#lightsail-for-research").

###### Important

Deleting a Lightsail for Research resource is a permanent action. The deleted data cannot be recovered. If
you might need the data later, create a snapshot of your virtual computer before you delete it.
For more information, see [Create a snapshot](create-snapshot.md "create-snapshot.md").

1. Sign in to the [Lightsail for Research console](https://lfr.console.aws.amazon.com/ls/research "https://lfr.console.aws.amazon.com/ls/research").
2. Choose **Virtual computers** in the navigation pane.
3. Choose the virtual computer to delete.
4. Choose **Actions**, then choose **Delete virtual
   computer**.
5. Type **confirm** in the text block. Then, choose **Delete
   virtual computer.**
