# Viewing tape usage statistics

When you write data to a tape, you can view the amount of data stored on the tape in
the Storage Gateway console. The **Details** tab for each tape shows the tape
usage information.

###### To view the amount of data stored on a tape

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the navigation pane, choose **Tape Library > Tapes** to
   see your tapes. By default, this list displays up to 1,000 tapes at a time, but
   the searches that you perform apply to all of your tapes. You can use the search
   bar to find tapes that match a specific criteria, or to reduce the list to less
   than 1,000 tapes. When your list contains 1,000 tapes or fewer, you can then
   sort your tapes in ascending or descending order by various properties.
3. Choose the tape you are interested in.
4. The page that appears provides various details and information about the tape,
   including the following:
   - **Size:** The total capacity of the selected
     tape.
   - **Used:** The size of data written to the tape by
     your backup application.

   ###### Note

   This value is not available for tapes created before May 13, 2015.
