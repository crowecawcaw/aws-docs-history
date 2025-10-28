# Creating a shared credentials file to use when sending email through Amazon SES using an AWS SDK

The following procedure shows how to create a shared credentials file in your home
directory. For the SDK sample code to function properly, you must create this
file.

1. In a text editor, create a new file. In the file, paste the following code:

```
[default]
aws_access_key_id = YOUR_AWS_ACCESS_KEY_ID
aws_secret_access_key = YOUR_AWS_SECRET_ACCESS_KEY
```

2. In the text file you just created, replace `YOUR_AWS_ACCESS_KEY` with
   your unique AWS access key ID, and replace `YOUR_AWS_SECRET_ACCESS_KEY`
   with your unique AWS secret access key.
3. Save the file. The following table shows the correct location and file name for
   your operating system.

| If you're using...    | Save the file as...                        |
| --------------------- | ------------------------------------------ | --------------------------------------------------------------------------------- |
| Windows               | `C:\Users\<yourUserName>\.aws\credentials` |
| Linux, macOS, or Unix | `~/.aws/credentials`                       | ###### Important Don't include a file extension when saving the credentials file. |
