

# Renaming an organizational unit (OU) with AWS Organizations
<a name="rename_ou"></a>

When you sign in to your organization's management account, you can rename an OU. To do this, complete the following steps.

**Minimum permissions**  
To rename an OU within a root in your organization, you must have the following permissions:  
`organizations:DescribeOrganization` – required only when using the Organizations console
`organizations:UpdateOrganizationalUnit`

------
#### [ AWS Management Console ]

**To rename an OU**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts)** page, [navigate to the OU](navigate_tree.md) that you want to rename, and then do one of the following steps:
   + Choose the radio button ![Blue circular icon with a white checkmark symbol in the center.](http://docs.aws.amazon.com/organizations/latest/userguide/images/radio-button-selected.png) next to the OU that you want to rename. Then, on the **Actions** menu, under **Organizational unit**, choose **Rename**.
   + Choose the OU's name, to access the OU's detail page. Then, at the top of the page choose **Rename**.

1. In the **Rename organizational unit** dialog box, enter a new name, and then choose **Save changes**.

------
#### [ AWS CLI & AWS SDKs ]

**To rename an OU**  
You can use one of the following commands to rename an OU:
+ AWS CLI: [update-organizational-unit](https://docs.aws.amazon.com/cli/latest/reference/organizations/update-organizational-unit.html)

  The following example shows how to rename an OU.

  ```
  $ aws organizations update-organizational-unit \
      --organizational-unit-id ou-a1b2-f6g7h222 \
      --name "Renamed-OU"
  {
      "OrganizationalUnit": {
          "Id": "ou-a1b2-f6g7h222",
          "Arn": "arn:aws:organizations::123456789012:ou/o-aa111bb222/ou-a1b2-f6g7h222",
          "Name": "Renamed-OU",
          "Path": "o-aa111bb222/r-a1b2/ou-a1b2-f6g7h222/"
      }
  }
  ```
+ AWS SDKs: [UpdateOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UpdateOrganizationalUnit.html)

------