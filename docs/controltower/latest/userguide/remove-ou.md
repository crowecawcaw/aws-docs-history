# Remove an OU

AWS Control Tower supports separate console actions to _deregister_ an OU
and to _delete_ an OU.

Deleting an OU is final. It cannot be undone.

###### Considerations

- The OU must be empty of accounts for **Delete** and
  **Deregister** operations to succeed.
- All optional controls must be removed from the OU.
- You must deregister the OU before you delete it.
- You can remove an OU from AWS Control Tower by deregistering it, without deleting
  it.

###### To remove an OU from AWS Control Tower

1. Sign in to the AWS Control Tower console at [https://console.aws.amazon.com/controltower](https://console.aws.amazon.com/controltower "https://console.aws.amazon.com/controltower").
2. Navigate to the **Organization** page.
3. Select the name of the OU to view the **OU details** page,
   and be sure that all accounts are removed from the OU.
4. Also on the **OU details** page, be sure that all optional
   controls are removed from the OU.
5. Return to the **Organization** page and select the radio
   button next to the OU.
6. Select **Deregister organizational unit** from the
   **Actions** dropdown menu in the upper right.
7. **Stop here** if you do not wish to delete the OU
   entirely, only to deregister it from AWS Control Tower. To delete the OU completely,
   continue to the next step.
8. To continue, select **Delete** from the
   **Actions** dropdown menu in the upper right.
   You must wait until the deregistration process is complete before you can deregister
   another OU.

###### Note

To remove accounts managed by AWS Control Tower, you can navigate to **Account
factory** from the left navigation pane in the AWS Control Tower console. To
remove accounts in the OU that are not managed by AWS Control Tower, go to the AWS Organizations
console.

To deregister an OU programmatically, call the [`DisableBaseline` API](../APIReference/API_DisableBaseline.md "../APIReference/API_DisableBaseline.md").
