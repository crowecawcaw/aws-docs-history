

# Setting up the AWS CLI
<a name="setup-cli"></a>

Follow these steps to download and configure the AWS CLI to work with Amazon Polly.

**To set up the AWS Command Line Interface**

1. Download and configure the AWS CLI. For instructions, see the following topics in the *AWS Command Line Interface User Guide*: 
   + [Getting Set Up with the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html) 
   + [Configuring the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) 

1. Add a named profile for the administrator user in the AWS CLI AWS Config file. You can use this profile when running the AWS CLI commands. For more information about named profiles, see [Named Profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html) in the *AWS Command Line Interface User Guide*. 

   ```
   [profile adminuser]
       aws_access_key_id = {{adminuser access key ID}}
       aws_secret_access_key = {{adminuser secret access key}}
       region = {{aws-region}}
   ```

   For a list of available AWS Regions and those supported by Amazon Polly, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the *Amazon Web Services General Reference*. 
**Note**  
If you're using a Region supported by Amazon Polly that you specified when you configured the AWS CLI, omit the following line from the AWS CLI code examples.   

   ```
   --region {{aws-region}}
   ```

1. Verify the setup by typing the following help command at the command prompt. 

   ```
   aws help
   ```

   A list of valid AWS commands should appear in the AWS CLI window. 