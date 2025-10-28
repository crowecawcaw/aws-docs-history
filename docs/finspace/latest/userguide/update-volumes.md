After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Updating a Managed kdb volume

You can only edit the description and size of a volume. When you update a volume,
you can only increase the volume size but cannot reduce it. During the update process, the
filesystem might be unavailable for a few minutes. You can retry any operations after the
update is complete.

###### To update a Managed kdb volume

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. In the left pane, under **Managed kdb Insights**, choose **Kdb
   environments**.
3. From the list of environments, choose a kdb environment.
4. On the environment details page, choose the **Volumes** tab.
5. From the list of clusters, choose the one that you want to edit. The volume details page opens.
6. Choose **Edit** and update the required details.
7. Choose **Save changes**.
