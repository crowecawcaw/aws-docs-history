

# Getting started with AWS Coding Plugin for SAP ABAP
<a name="getting-started"></a>

This tutorial takes you from an empty Eclipse workspace to your first spec running against your SAP system. The setup takes a few minutes, not counting Kiro CLI installation and sign-in if you have not done those already.

Completing this setup requires a Kiro plan. There is no charge for the plug-in; running it consumes Kiro credits from your plan. See [Pricing](pricing.md).

**Topics**
+ [Prerequisites](#getting-started-prerequisites)
+ [Install the plug-in and run your first spec](#getting-started-procedure)
+ [Troubleshooting installation issues](#getting-started-troubleshooting)

## Prerequisites
<a name="getting-started-prerequisites"></a>

Before you start, make sure you have:
+ An SAP ABAP system. Coding Plugin is tested with SAP ERP 6.0 EHP7, SAP S/4HANA 2025, and the SAP BTP ABAP environment. Available ABAP Development Tools (ADT) functions vary by `SAP_BASIS` release. Older systems support reading and writing code but might lack some advanced functions. See [Limitations](abap-capabilities.md#abap-capabilities-cannot).
+ Eclipse 2026-06 or later, with SAP ADT 3.60.0 or later.
+ An SAP connection already defined and open in ADT.
+  [Kiro CLI](https://kiro.dev/cli/) 2.19.0 or later, installed and signed in to Kiro.
+ A Kiro plan.

## Install the plug-in and run your first spec
<a name="getting-started-procedure"></a>

1.  **Install the plug-in.** 

   1. In Eclipse, choose **Help**, **Install New Software**.

   1. In **Work with**, enter `https://downloads.aws.com/sap/aws-coding-plugin-for-sap-abap/current`.

   1. Select the AWS Coding Plugin for SAP ABAP feature, then choose **Next**.

   1. Accept the license terms, then choose **Finish**.

   1. Restart Eclipse when prompted.

      The plug-in loads and the onboarding wizard opens.

1.  **Complete the onboarding wizard.** The wizard checks your prerequisites and locates Kiro CLI.

   1. If the wizard reports that Kiro CLI is not found, install it from [Kiro CLI](https://kiro.dev/cli/) on the Kiro website, then choose **Check Again**.

   1. When the wizard starts Kiro sign-in, sign in with your Kiro account.

      The wizard reports that all prerequisites are satisfied.

1.  **Open the chat panel.** 

   1. Press  Ctrl 3  (macOS:  Cmd 3 ) and open the AWS Coding Plugin Chat view.

1.  **Automatic project configuration.** 

   1. The first time you open the plug-in, it creates a project that holds a `.kiro/` folder (with `settings/`, `skills/`, `specs/`, and `steering/`). This project is the agent’s working directory and can be committed to Git.

   1. The plug-in also runs two setup commands automatically:
      +  `/workspace-init` interviews you about your organization’s standards and writes them as steering.
      +  `/sap-discover` interviews you about the connected SAP system and writes system-specific steering.

        Both can be run again later to update what they wrote. For more information, see [Steering](steering.md).

1.  **Run your first spec.** 

   1. In the chat, describe the change you want to make in your SAP ABAP system.

   1. When Kiro proposes a spec, review the generated requirements, design, and tasks.

   1. At the top of the chat tab, choose **Run All Tasks**.

   1. Approve each tool call when its prompt appears.

Coding Plugin opens a new tab and reports progress one task at a time. Your spec is saved under `.kiro/specs/` in the project.

By default, Kiro gates each tool call behind an approval prompt that you accept or decline (Kiro Permissions). For how approvals work, see [Kiro Permissions](kiro-permissions.md).

## Troubleshooting installation issues
<a name="getting-started-troubleshooting"></a>
+  **The wizard cannot find Kiro CLI.** Install Kiro CLI, then choose **Check Again** in the wizard.
+  **The SAP features do not appear.** Your SAP ADT is older than 3.60.0. Update ADT to 3.60.0 or later.