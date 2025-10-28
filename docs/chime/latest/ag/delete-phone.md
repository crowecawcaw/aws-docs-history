**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Deleting phone numbers

###### Important

Only Amazon Chime system administrators can complete these steps. Also, you must unassign phone
numbers before you can delete them.

When you provision a phone number, you order it from a pool of numbers that Amazon Chime maintains. Deleting a number moves it back into the pool.
When you delete a number, it first goes to your deletion queue where it's held for 7 days. During that time, you can move the number back to your inventory.
After 7 days, the system automatically deletes the number from the holding queue and disassociates it from your account. That returns the number to
the number pool. If you need to reclaim a number after the system deletes it from the holding queue, follow the steps in
[Provisioning phone numbers](provision-phone.md "provision-phone.md"), but be aware that the number may not be available.

###### To delete unassigned phone numbers

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com "https://chime.aws.amazon.com").
2. In the navigation pane, under **Calling**, choose **Phone number
   management**.
3. Choose the **Inventory** tab, then select the phone number or numbers that
   you want to delete.
4. Open the **Actions** list and choose **Delete phone
   number(s)**.
5. Select the check box, then choose **Delete**.
   Deleted phone numbers are held in the **Deletion queue** for 7
   days before they are deleted from your inventory permanently.
