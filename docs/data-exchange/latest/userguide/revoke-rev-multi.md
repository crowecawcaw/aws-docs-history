# Revoking multiple AWS Data Exchange asset revisions as a provider

(console)

As a provider of AWS Data Exchange data products, you can use the AWS Data Exchange console to revoke subscriber
access to multiple revisions using the following instructions.

###### To revoke multiple revisions as a provider (console)

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, for **Publish data**, choose
   **Owned data sets**.
3. In **Owned data sets**, choose the data set that has the revisions
   you want to revoke.
4. On the **Revisions** tab, choose up to 10 revisions.
5. Choose **Revoke**.
6. In the **Revoke {x} revisions** dialog box, enter a short
   description of your reason for revoking the revisions. Subscribers will see this
   description. Then, choose **Revoke**.

The **Status** of the revisions are set to
**Revoked**.

###### Warning

This revokes the revisions and all of the assets. Subscribers can view the reason
for revocation but can’t access or export the assets. This action can't be
undone. 7. After a revision is revoked, you can delete the assets of the revision by navigating
to the revision page, selecting the assets you want to delete in the **Imported
assets** table, and then choosing **Delete**.
To edit the reason for a revoked revision, see [Editing an AWS Data Exchange asset revocation reason as a provider
(console)](edit-revoked-rev.md "edit-revoked-rev.md").
