

AWS Well-Architected Agent is in preview release and is subject to change.

# Viewing your agent profiles
<a name="agent-view-profiles"></a>

## Console
<a name="agent-view-profiles-console"></a>

To view a list of your profiles, choose **Agent profiles** in the left-hand navigation.

This view lists all of your configured AWS WA Agent profiles, along with action required notices for misconfigured profiles. From this page, you can:
+ Choose **Go to Dashboard** to view recommendations for a profile.
+ Choose **See profile details** to view the profile details page.
+ Choose **Actions** to edit the profile, copy the profile ARN, or delete the profile.

The profile details page displays:
+ **Profile summary:** Host account, goals, accounts in the profile, AWS Regions, optimization pillars, applications, termination protection status, and a copiable **Execution role ARN** for the profile.
+ **Next steps (optional):** Provides optional next steps for the profile when the particular actions haven't been taken. You can choose **Provide profile access to team members** to share a profile with team members, or choose **Create applications with context** to define application context in the profile.

The profile details page has four tabs:
+ **Accounts in profile:** Lists accounts configured for the profile. You can edit accounts and filter by Region.
+ **Profile Access:** Shows AWS accounts with access to this profile and their access level (read or read/write). You can provide access to additional accounts or remove access.
+  **Applications:** Lists application contexts defined for the profile. You can add, edit, or delete application contexts, and search or filter by Region. 
+ **Schedule** Displays your chosen refresh schedule for how often AWS WA Agent generates scheduled recommendations. You can also update your refresh schedule here by choosing a new schedule period, and then choosing **Save**.

## CLI
<a name="agent-view-profiles-cli"></a>

To list all agent profiles in your account:

```
aws wellarchitected list-agent-profiles
```

To view details for a specific profile:

```
aws wellarchitected get-agent-profile \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}"
```