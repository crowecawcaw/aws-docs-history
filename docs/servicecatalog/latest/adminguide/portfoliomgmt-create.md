

# Creating and Deleting Portfolios
<a name="portfoliomgmt-create"></a>

Use the **Portfolios** page to create and delete portfolios. 

**To create a new portfolio**

1. In the left navigation menu, choose **Portfolios**.

1. Choose **Create portfolio**. 

1. On the **Create portfolio** page, enter the requested information.

1. Choose **Create**. AWS Service Catalog creates the portfolio and displays the portfolio details.

**To delete a portfolio**
**Note**  
You can only delete *local* portfolios. You can remove *imported* (shared) portfolios, but you cannot delete imported portfolios. 

Before you can delete a portfolio, you must remove all its products, constraints, groups, roles, users, shares, and TagOptions. To do so, open a portfolio to display **Portfolio details**. Then choose a tab to remove them.
**Note**  
To avoid errors, remove the constraints from the portfolio *before* you remove any products. 

1. In the left navigation menu, choose **Portfolios**.

1. Select the portfolio you want to delete.

1. Choose **Delete**. You can only delete *local* portfolios. If you are attempting to delete an *imported* (shared) portfolio, the **Actions** menu is not available. 

1. In the confirmation window, choose **Delete**.