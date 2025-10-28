Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Importing into notebooks

You can import an entire notebook or individual SQL cells into a query editor v2
notebook.

To import an entire notebook from a local file to **My notebooks**,
choose
![Import](images/qev2-import.png)

**Import**, then choose **Import notebook**. Navigate
to the `.ipynb` file that contains your notebook. The notebook is imported
into the currently open notebook folder. You can then open the notebook in the notebook
editor.

To import a query from a local file into a SQL cell in a notebook, choose
![Import](images/qev2-import.png)

**Import**, then choose **Import query**. On the
**Import query** window, follow the directions on the screen to
choose file and folders that can be imported as a query into a new notebook or an
existing notebook. The files must have an extension of `.sql` or
`.txt`. Each query can be up to 10,000 characters. When you add
to an existing notebook, you choose which notebook from all notebooks in your
**Saved notebooks** list. The imported queries are added as SQL
cells at the end of the notebook. When you choose a new notebook, you choose the name of
the notebook and it is created in the currently open saved notebooks folder.

###### Note

When creating `.sql` files on macOS using the TextEdit
application, you might encounter an issue where an additional hidden extension is
added to the file. For instance, a file named `Test.sql` created
in TextEdit might end up being saved as `Test.sql.rtf`. The
query editor v2 does not support files with the `.rtf` extension. However,
if you create a `.sql` file using TextEdit, and save it as a
plain text file, the file has an additional hidden `.txt`
extension. For example, a file named `Text.sql` might be saved as
`Text.sql.txt`. Unlike the `.rtf`
extension, query editor v2 does support files with the `.txt` extension,
so `Text.sql.txt` is supported when importing queries to
notebooks.
