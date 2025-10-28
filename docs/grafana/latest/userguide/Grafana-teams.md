# Managing teams

Using _teams_ enables you to grant permissions to a group of users
at the same time. You can also set up team sync to automatically synchronize team
membership between your Grafana workspace and your authorization provider.

## Creating or removing a team

Create teams to manage users in groups.

###### To create a team

1. In the sidebar, choose the **Configuration**(gear) icon,
   and choose **Teams**.
2. Choose **New team**.
3. For **Name**, enter a name for the new team, and then
   choose **Create**.

###### To remove a team

1. In the sidebar, choose the **Configuration** (gear) icon,
   and choose **Teams**.
2. To the right of the team's name, choose **X**.
3. To confirm, choose **Delete**.

## Adding or removing a user from a team

Use these steps to add users to teams or remove them from teams.

###### To add a user to a team

1. In the sidebar, choose the **Configuration** (gear) icon,
   and choose **Teams**.
2. Choose the team that you want to add the user to.
3. Choose **Add member**.
4. In the **Add team member** box, select the user to add to
   the team, and then choose **Add to team**.

###### To remove a user from a team

1. In the sidebar, choose the **Configuration** (gear) icon,
   and choose **Teams**.
2. Choose the team that you want to remove the user from.
3. To the right of the user's name, choose **X**.
4. To confirm, choose **Delete**.

## Using team sync

With _team sync_, you can set up synchronization between your
authorization provider’s groups and the teams in Grafana. The authorization
providers currently supported are IAM Identity Center and SAML.

###### To synchronize a Grafana team with an external group.

1. In the Grafana console, navigate to **Configuration**,
   **Teams**.
2. To synchronize with an IAM Identity Center group, enter the IAM Identity Center group ID. To
   synchronize with a group from a SAML based identity provider, enter the
   value of the attribute name entered in the **Assersion attribute
   groups** field in SAML configuration section on the Amazon Managed Grafana
   workspace configuration page.
3. Choose **Add group**.
