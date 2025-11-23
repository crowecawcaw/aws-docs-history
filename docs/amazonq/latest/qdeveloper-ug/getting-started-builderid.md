# Getting started with a personal account

(Builder ID)

If you want to use Amazon Q Developer for personal projects, and you don't need to administer other
users, you'll want to get started with a personal account, also known as a Builder ID. A
_Builder ID_ is a special type of AWS account that gives you the ability to
use Amazon Q in your Integrated Development Environment (IDE) and your terminal's command line. Unlike
a regular AWS account, a Builder ID is meant to be used by you and you alone, does not allow access
to the AWS Management Console, and cannot be assigned IAM roles or permissions.

You can set up a Builder ID for free to start. When you're ready, you can [upgrade to the Pro tier](upgrade-to-pro.md#upgrade-builder-id "upgrade-to-pro.md#upgrade-builder-id") by connecting your Builder ID to an
AWS account to take advantage of higher usage limits.

For a list of features available at the Pro tier, see the [Amazon Q Developer pricing](https://aws.amazon.com/q/developer/pricing "https://aws.amazon.com/q/developer/pricing") page.

###### To get started with a personal account (Builder ID) at the Free or Pro tier

- [Before you begin: Understand the limitations of
  personal accounts (Builder IDs)](#builder-id-limitations "#builder-id-limitations")
- [Step 1: Sign up](#builder-id-signup "#builder-id-signup")
- [Step 2: Install Amazon Q](#builder-id-install "#builder-id-install")
- [Step 3: (Optional) Upgrade to the Pro
  tier](#builder-id-upgrade-optional "#builder-id-upgrade-optional")

## Before you begin: Understand the limitations of

personal accounts (Builder IDs)

Before you create a personal account (Builder ID) for use with Amazon Q, understand its
limitations.

- With a Builder ID at the Free tier, you will be subject to usage limits. For information
  about what these limits are, see the [pricing page](https://aws.amazon.com/q/developer/pricing/ "https://aws.amazon.com/q/developer/pricing/"). If you
  need higher usage limits, subscribe your Builder ID to the Pro tier using the instructions
  that follow, or use IAM Identity Center following the guidance in [Getting started with IAM Identity Center](getting-started-idc.md "getting-started-idc.md").
- With a Builder ID at the Pro tier, you'll get _higher usage limits_,
  but you won't get all Pro tier-only _features_. For a list of Pro tier features
  that are not available to you, see the footnote at the bottom of the [Amazon Q Developer pricing page](https://aws.amazon.com/q/developer/pricing/ "https://aws.amazon.com/q/developer/pricing/").
  If you need Pro tier features, use IAM Identity Center. For more information, see [Getting started with IAM Identity Center](getting-started-idc.md "getting-started-idc.md").
- With a Builder ID at both the Free and Pro tiers, Amazon Q is only supported in the IDE and at
  the command line. It is not supported [in the AWS Management Console, and
  on AWS apps and websites](q-on-aws.md "q-on-aws.md"). If you need to use Q in the AWS Management Console, and on
  AWS apps and websites, use IAM Identity Center. For more information, see [Getting started with IAM Identity Center](getting-started-idc.md "getting-started-idc.md").

## Step 1: Sign up

Sign up for a free personal account (Builder ID). You can sign up using your email address or an
existing Google account. For more information, see [Create your AWS Builder ID](../../../signin/latest/userguide/create-aws_builder_id.md "../../../signin/latest/userguide/create-aws_builder_id.md") in the _AWS Sign-In User
Guide_.

## Step 2: Install Amazon Q

Install Amazon Q in your Integrated Development Environment (IDE) or at the command line, and
then authenticate using your personal account (Builder ID). For installation and authentication
information, see:

- [Installing the Amazon Q Developer extension or plugin in your IDE](q-in-IDE-setup.md "q-in-IDE-setup.md")
- [Install the Kiro CLI.](https://kiro.dev/docs/cli "https://kiro.dev/docs/cli")

## Step 3: (Optional) Upgrade to the Pro

tier

Upgrade to the Pro tier to take advantage of increased limits. See [Upgrading a personal account (Builder ID)](upgrade-to-pro.md#upgrade-builder-id "upgrade-to-pro.md#upgrade-builder-id").
