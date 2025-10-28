# Deleting products

When you delete a product, AWS Service Catalog removes all product versions from every portfolio
containing the product.

AWS Service Catalog allows you to delete a product using the AWS Service Catalog console or AWS CLI. To successfully delete a product,
you must disassociate all resources associated with the product first.
Examples of product resource associations include portfolio associations, budgets, TagOptions, and
Service Actions.

###### Important

You cannot recover a product after it is deleted.

######

To delete a product using the AWS Service Catalog console

1. Navigate to the **Portfolios** page and select the portfolio containing the product
   you want to delete.
2. Select the product that you want to delete, and then choose **Delete** on
   the upper right of the product pane.
3. For products _without associated resources_, confirm the product you
   want to delete by entering **delete** in the text box, and then
   choose **Delete**.

For products _with associated resources_, continue to step 4. 4. In the **Delete product** window, review the **Associations** table,
which displays all of the product's associated resources. AWS Service Catalog attempts to disassociate these resources
when you delete the product. 5. Confirm you want to delete the product and remove all of its associated resources by entering **delete**
in the text box. 6. Choose **Disassociate and delete**.
If AWS Service Catalog is unable to disassociate all of the product's resources, the product is not deleted. The
**Delete product** window displays the number of failed disassociations and
a description for each failure.
For more information about resolving failed resource disassociations when deleting a product, see
_Resolving failed resource disassociations when deleting a product_ below.

###### Topics

- [Deleting products using the AWS CLI](product-delete-cli.md "product-delete-cli.md")
- [Resolving failed resource disassociations when deleting a product](product-delete-exception.md "product-delete-exception.md")
