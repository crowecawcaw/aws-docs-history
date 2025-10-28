# Modifying

targets

When you set up just-in-time node access, you choose the
_targets_ where you want to set up just-in-time node access.
Targets consist of AWS Organizations organizational units (OUs) and AWS Regions. By
default, the same targets you chose when setting up the unified Systems Manager console are
selected for just-in-time node access. You can choose to set up just-in-time node
access for all of the same targets, or a subset of the targets you specified when
setting up the unified Systems Manager console. Adding new targets that weren't selected when
you set up the unified Systems Manager console isn't supported. You can change the targets you
selected after setting up just-in-time node access.

The following procedure describes how to modify the targets for just-in-time node
access.

###### To modify targets

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Select **Settings** in the navigation pane.
3. Select the **Just-in-time node access** tab.
4. In the **Targets** section, select
   **Edit**.
5. Select the **Organizational units** and
   **Regions** where you want to use just-in-time node
   access.
6. Select **Save**.
