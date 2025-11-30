# Amazon S3 policies

Amazon S3 policies allow you to centrally manage configurations for Amazon S3 resources at scale across the accounts in an organization. Amazon S3 policies currently support settings for blocking public access.

You can use an Amazon S3 policy to specify whether to enable or disable all four Block Public Access settings, and that specification will apply to all Amazon S3 resources within selected accounts. You can use Block Public Access settings in an Amazon S3 policy to enforce consistent security posture across your organization and eliminate the operational overhead of managing individual account configurations.

## How it works

When you attach an Amazon S3 policy to an organizational entity, it defines settings that apply to all Amazon S3 resources within accounts in that scope. These configurations override account-level settings, allowing you to centrally manage Amazon S3 settings.

Amazon S3 policies can be applied to an entire organization, organizational units (OUs), or individual accounts. Accounts joining an organization will automatically inherit any Amazon S3 policies based on their location in the organization hierarchy.

Detachment behavior: If an Amazon S3 policy is detached, accounts automatically revert to their previous account-level configuration. Amazon S3 preserves the original account-level settings to enable seamless restoration.

## Key features

- Unified control: All four Block Public Access settings (BlockPublicAcls, BlockPublicPolicy, IgnorePublicAcls, RestrictPublicBuckets) are controlled together as a single configuration
- Automatic inheritance: New accounts automatically inherit policies based on their organizational placement
- Override protection: Prevents account-level modifications when organization policies are active
- Seamless restoration: Original account settings are preserved and restored when policies are detached

## Prerequisites

Before using Amazon S3 policies, ensure you have:

- An AWS organization in all features mode
- Permissions to manage AWS Organizations policies (organizations:CreatePolicy, organizations:AttachPolicy, etc.)
- The Amazon S3 policy type enabled for your organization
