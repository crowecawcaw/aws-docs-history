# Deleting virtual tapes from your

Tape Gateway

You can delete virtual tapes from your Tape Gateway by using the Storage Gateway
console.

###### Note

If the tape you want to delete from your Tape Gateway has a status of RETRIEVED,
you must first eject the tape using your backup application before deleting the
tape. For instructions on how to eject a tape using the Symantec NetBackup software,
see [Archiving the Tape](backup_netbackup-vtl.md#GettingStarted-archiving-tapes-vtl "backup_netbackup-vtl.md#GettingStarted-archiving-tapes-vtl"). After the tape is ejected, the tape status changes
back to ARCHIVED. You can then delete the tape.

Make copies of your data before you delete your tapes. After you delete a tape, you
can't get it back.

###### To delete a virtual tape

###### Warning

This procedure permanently deletes the selected virtual tape.

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the navigation pane, choose **Tape Library > Tapes** to
   see your tapes. By default, this list displays up to 1,000 tapes at a time, but
   the searches that you perform apply to all of your tapes. You can use the search
   bar to find tapes that match a specific criteria, or to reduce the list to less
   than 1,000 tapes. When your list contains 1,000 tapes or fewer, you can then
   sort your tapes in ascending or descending order by various properties.
3. Select one or more tapes to delete.
4. For **Actions** choose **Delete tape**. The
   confirmation dialog box appears.
5. Verify that you want to delete the specified tapes, then type the word
   _delete_ in the confirmation box and choose
   **Delete**.
   After the tape is deleted, it disappears from the Tape Gateway.
