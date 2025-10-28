# Managing membership with organizational units (OUs) for AWS Security Incident Response

AWS Security Incident Response supports membership coverage for individual organizational units (OUs). You can update your membership to cover
specific OUs at any time. All accounts within the selected OUs, including accounts under child OUs, will be covered by your membership.

When updating your membership association, updates can be applied for up to 5 OUs at a time.
If you wish to make changes to more than 5 OUs, complete association changes in batches of 5 OUs until all updates are completed.

Console

1. Open the Security Incident Response console at https://console.aws.amazon.com/security-ir/

To sign in, use the management credentials for your AWS Organizations organization. 2. Navigate to **Manage membership** > Accounts 3. Click **Update association** 4. Select **Choose organizational units (OUs)** 5. Select **Add OUs** or **Remove OUs** 6. Select up to 5 OUs you wish to update. You cannot add and remove OUs at the same time.

###### Note

All accounts and child OUs under a selected OU will be associated. 7. Click **Update association** 8. ###### Note

If you wish to make changes to more than 5 OUs, repeat steps 5 and 6 until all OUs have been associated.

To learn more about making OU changes within your AWS organization, please see [Managing organizational units (OUs) with AWS Organizations](../../../organizations/latest/userguide/orgs_manage_ous.md "../../../organizations/latest/userguide/orgs_manage_ous.md").
