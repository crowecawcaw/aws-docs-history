# Creating and Deleting Portfolios

Use the **Portfolios** page to create and delete portfolios.

###### To create a new portfolio

1. In the left navigation menu, choose **Portfolios**.
2. Choose **Create portfolio**.
3. On the **Create portfolio** page, enter the requested information.
4. Choose **Create**. AWS Service Catalog creates the portfolio and displays the portfolio
   details.

###### To delete a portfolio

###### Note

You can only delete _local_ portfolios. You can remove _imported_ (shared) portfolios, but you cannot
delete imported portfolios.

Before you can delete a portfolio, you must remove all its products, constraints, groups,
roles, users, shares, and TagOptions. To do so, open a portfolio to display **Portfolio details**. Then choose a tab to remove them.

###### Note

To avoid errors, remove the constraints from the portfolio _before_ you remove any products.

1. In the left navigation menu, choose **Portfolios**.
2. Select the portfolio you want to delete.
3. Choose **Delete**. You can only delete _local_ portfolios. If you are attempting to
   delete an _imported_ (shared) portfolio, the **Actions**
   menu is not available.
4. In the confirmation window, choose **Delete**.
