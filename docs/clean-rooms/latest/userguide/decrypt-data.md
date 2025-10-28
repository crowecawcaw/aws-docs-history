# Decrypting data tables with the C3R encryption client

Follow this procedure for collaborations that use Cryptographic Computing for Clean Rooms and the C3R encryption client to
encrypt data tables. Use this procedure after you have [queried data in the collaboration](analyze-data.md "analyze-data.md").

The shared secret key and collaboration ID are required for this procedure.

The member who can receive results decrypts the data using the same shared secret key and
collaboration ID that was used to encrypt the data for the collaboration.

###### Note

AWS Clean Rooms collaborations already limit who can perform and view query results. To perform
the decryption, whoever has access to these results needs the same shared secret key and
collaboration ID that was used to encrypt the data.

###### To decrypt an encrypted data table

1. (Optional) [View the available commands in the
   C3R encryption client](view-commands.md "view-commands.md").
2. (Optional) Navigate to the desired directory and run `ls`
   (macOS) or `dir` (Windows).
   1. Verify that the c3r-cli.jar file and encrypted query results data file
      are in the desired directory.

   ###### Note

   If query results are downloaded from the AWS Clean Rooms console interface, they are
   likely in the **Downloads** folder for your user account. (For
   example, the **Downloads** folder in your user directory on
   Windows and macOS.) We recommend that you move the
   query results file to the same folder as the c3r-cli.jar.

3. Store the shared secret key in the `C3R_SHARED_SECRET` environment variable.
   For more information, see [Step 6: Store the shared secret key in an environment
   variable](store-key.md "store-key.md").
4. From the AWS Command Line Interface (AWS CLI), run the following command.

**java -jar c3r-cli.jar decrypt `<name of input .csv
 file>` --id=`<collaboration id>`
--output=`<output file name>`** 5. Replace each `user input placeholder` with your own
information:

    1. For `id=`, enter the collaboration ID.
    2. For `output=`, enter the name of the output file (for example,
     `results-decrypted.csv`).


    If you don't specify an output name, a default name is displayed in the terminal.
    3. View the decrypted data in the specified output file using your preferred CSV or
     Parquet viewing application (such as Microsoft
     Excel, a text editor, or other application).
