# Delete domains

When deleting a domain, note that the act of deleting a domain is final. Another important
note to remember is that not all items created by Amazon SageMaker Unified Studio are deleted. The following items
can only be deleted in their service consoles:

- AWS resources - except for this domain - will NOT be deleted.
- Subscription grants will NOT be removed.
- Resource shares of this domain to associated accounts will NOT be deleted.
  To prevent someone from deleting a domain maliciously, deleting a domain requires
  administrative IAM permissions for Amazon SageMaker Unified Studio, which you can configure with IAM.

To delete a domain, complete the following procedure:

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and choose the domain’s name from the list.
   The name is a hyperlink.
3. On the details page for the domain, expand **Actions** and then
   choose **Delete**.
4. Note that deleting a domain cannot be undone and if you want to proceed, confirm the
   deletion by typing in the domain name in the text field, and then choose
   **Delete**.
