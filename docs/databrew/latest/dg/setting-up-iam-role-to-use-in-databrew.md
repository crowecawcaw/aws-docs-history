# Adding an IAM role with data resource

permissions

You use IAM roles to manage policies that are assigned together. An IAM role can be used by someone acting
in a particular role, such as a DataBrew user or DataBrew itself. For more information, see [IAM Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the _IAM User Guide._

Use the following procedure to create an IAM role that is required for DataBrew projects to access data.

###### To attach the required IAM policy to a new IAM role for DataBrew

1. In the navigation pane, choose **Roles**, **Create Role**.
2. For **Select type of trusted entity**, choose the card labeled **AWS
   service**.
3. Choose **DataBrew** from the list, then choose **Next:
   Permissions**.
4. Enter `AwsGlueDataBrewDataResourcePolicy` in the search box (the IAM policy
   you created in an earlier step). Select the policy and choose **Next:
   Tags**.
5. Choose **Next: Review**.
6. For **Role name**, enter `AwsGlueDataBrewDataAccessRole`,
   and choose **Create role**.
