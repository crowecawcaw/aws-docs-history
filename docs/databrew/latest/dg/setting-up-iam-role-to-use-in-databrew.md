

# Adding an IAM role with data resource permissions
<a name="setting-up-iam-role-to-use-in-databrew"></a>

You use IAM roles to manage policies that are assigned together. An IAM role can be used by someone acting in a particular role, such as a DataBrew user or DataBrew itself. For more information, see [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the *IAM User Guide.*

Use the following procedure to create an IAM role that is required for DataBrew projects to access data. 

**To attach the required IAM policy to a new IAM role for DataBrew**

1. In the navigation pane, choose **Roles**, **Create Role**. 

1. For **Select type of trusted entity**, choose the card labeled **AWS service**.

1. Choose **DataBrew** from the list, then choose **Next: Permissions**.

1. Enter **AwsGlueDataBrewDataResourcePolicy** in the search box (the IAM policy you created in an earlier step). Select the policy and choose **Next: Tags**.

1. Choose **Next: Review**.

1. For **Role name**, enter **AwsGlueDataBrewDataAccessRole**, and choose **Create role**.