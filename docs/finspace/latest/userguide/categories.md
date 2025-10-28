After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Configuring categories in Amazon FinSpace

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

**Categories** – Categories allow for cataloging of datasets by commonly used business terms.
Categories are hierarchical in nature, allowing for each node of the hierarchy to have a name and a description.
The order of the nodes within a level are defined when you define categories.
The **Categories** are displayed in the data browser when you choose **Catalog** on the left navigation bar.

###### Note

In order to create and manage categories, you must be a superuser or a member of a group with necessary permissions -
**Manage Categories and Controlled Vocabularies**.

## Create a category

###### To create a new category

1. Sign in to the FinSpace web application. For more information, see [Signing in to the Amazon FinSpace web application](signing-into-amazon-finspace.md "signing-into-amazon-finspace.md").
2. On the left navigation bar of the home page, choose **Manage Data**.
3. On the **Manage Data** page, choose **Manage Categories**.
4. Choose **Add New Top Level Category**.
5. Enter a name for the category. For example, `Asset Class`.
6. (Optional) Add a description for the category.
7. Choose **Add Sub-Category** to add one or more sub-categories. An addition of one category is required. You can add as many sub-categories as you like.
8. (Optional) Add a description for the sub-category.
9. Choose **Done** to add the sub-category.
10. Choose **Save**.

## Display category in the data browser

###### To display a category in the data browser

1. Sign in to the FinSpace web application. For more information, see [Signing in to the Amazon FinSpace web application](signing-into-amazon-finspace.md "signing-into-amazon-finspace.md").
2. On the left navigation bar of the home page, choose **Manage Data**.
3. On the **Manage Data** page, choose **Manage Categories**.
4. Identify the top level category that you want to make visible in the data browser.
5. Uncheck the eye (
   ![An image of the uncheck eye icon.](images/04a-configuring-the-catalog/uncheck-eye-icon.png)
   ) icon.
6. On the left navigation bar, choose **Catalog** and verify if the category is now visible in the data browser.

## Editing categories

###### To edit a category

1. Sign in to the FinSpace web application. For more information, see [Signing in to the Amazon FinSpace web application](signing-into-amazon-finspace.md "signing-into-amazon-finspace.md").
2. On the left navigation bar of the home page, choose **Manage Data**.
3. On the **Manage Data** page, choose **Manage Categories**.
4. From the list of categories, select a category to edit.
5. Choose **Edit**.
6. In the **Edit Category** section, make the required changes.
7. Choose **Save**.

## Deleting categories

###### To delete a category

1. Sign in to the FinSpace web application. For more information, see [Signing in to the Amazon FinSpace web application](signing-into-amazon-finspace.md "signing-into-amazon-finspace.md").
2. On the left navigation bar of the home page, choose **Manage Data**.
3. On the **Manage Data** page, choose **Manage Categories**.
4. From the list of categories, select a category that you want to delete.
5. Choose **Edit**.
6. Choose **Delete**.
7. On the dialog box that appears, choose **Remove** to confirm deletion.
