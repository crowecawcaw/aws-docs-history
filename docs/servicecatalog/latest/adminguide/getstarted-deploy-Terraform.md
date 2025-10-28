# Step 7: Grant end user access

After applying the launch constraint to your HashiCorp Terraform product, you are ready
to grant access to end users in the spoke account.

In this tutorial, you grant access to end users using Principal Name sharing. Principal Names are names for groups,
roles, and users that administrators can specify in a portfolio, and then share with the portfolio.
When you share the portfolio, AWS Service Catalog verifies if those Principal Names already exist. If they do exist, AWS Service Catalog automatically
associates the matching IAM principals with the shared portfolio to grant access to end users. Review
[Sharing a Portfolio](catalogs_portfolios_sharing_how-to-share.md "catalogs_portfolios_sharing_how-to-share.md")
for more information.

###### Prerequisites

If you haven't created an IAM group for the end users, see [Grant permissions to AWS Service Catalog end users](getstarted-iamenduser.md "getstarted-iamenduser.md").

###### To provide access to the portfolio

1. Navigate to the **Portfolio** page and choose the
   **S3 bucket** portfolio.
2. Choose the **Access** tab, and then choose **Grant access**.
3. In the **Access type** pane, choose **Principal name**.
4. In the **Principal name** pane, select the **Principal name** type,
   and then enter the principal **Name** of the desired end user in the spoke account.
5. Choose **Grant access**.
