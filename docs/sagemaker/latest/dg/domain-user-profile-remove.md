# Remove user profiles

All apps launched by a user profile and all spaces owned by the user profile must be deleted to delete the user profile. The
following section shows how to remove user profiles from a domain using the SageMaker AI console or
AWS CLI.

## Remove user profiles from the

console

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose
   **domains**.
4. From the list of domains, select the domain that you want to remove a user
   profile from.
5. On the **domain details** page, choose the **User
   profiles** tab.
6. Select the user profile that you want to delete.
7. On the **User Details** page, for each non-failed app in the
   **Apps** list, choose **Action**.
8. From the dropdown list, choose **Delete**.
9. On the **Delete app** dialog box, choose **Yes, delete
   app**. Then enter _delete_ in the confirmation field, and
   choose **Delete**.
10. When **Status** shows as **Deleted** for all apps,
    navigate back to the **domain details** page and choose the **Space
    management** tab.
11. Delete any spaces owned by the user profile. For each space where the user profile is the owner,
    select the space and choose **Delete**. For detailed steps, see
    [Delete a Studio space](studio-updated-running-stop.md#studio-updated-running-stop-space "studio-updated-running-stop.md#studio-updated-running-stop-space").
12. Return to the **User profiles** tab and choose **Edit**.
13. On the **Edit User** page, choose **Delete
    user**.
14. On the **Delete user** pop-up, choose **Yes, delete
    user**.
15. Enter _delete_ in the field to confirm deletion.
16. Choose **Delete**.

## Remove user profiles from the AWS CLI

To delete a user profile from the AWS CLI, first delete any spaces owned by the user profile,
then delete the user profile. Run the following commands from the terminal of your local machine.

```
# Delete spaces owned by the user profile
aws sagemaker delete-space \
--region `region` \
--domain-id `domain-id` \
--space-name `space-name`

# Delete the user profile
aws sagemaker delete-user-profile \
--region `region` \
--domain-id `domain-id` \
--user-profile-name `user-name`
```
