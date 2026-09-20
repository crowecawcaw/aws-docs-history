

# Creating a shared credentials file to use when sending email through Amazon SES using an AWS SDK
<a name="create-shared-credentials-file"></a>

The following procedure shows how to create a shared credentials file in your home directory. For the SDK sample code to function properly, you must create this file.

1. In a text editor, create a new file. In the file, paste the following code:

   ```
   1. [default]
   2. aws_access_key_id = YOUR_AWS_ACCESS_KEY_ID
   3. aws_secret_access_key = YOUR_AWS_SECRET_ACCESS_KEY
   ```

1. In the text file you just created, replace `YOUR_AWS_ACCESS_KEY` with your unique AWS access key ID, and replace `YOUR_AWS_SECRET_ACCESS_KEY` with your unique AWS secret access key.

1. Save the file. The following table shows the correct location and file name for your operating system.


<table>
<thead>
  <tr><th>If you're using...</th><th>Save the file as...</th></tr>
</thead>
<tbody>
  <tr><td>Windows</td><td><code>C:\Users\&lt;yourUserName&gt;\.aws\credentials</code></td></tr>
  <tr><td>Linux, macOS, or Unix</td><td><code>~/.aws/credentials</code></td></tr>
</tbody>
</table>

**Important**  
Don't include a file extension when saving the credentials file.