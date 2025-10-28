# Reconfiguring the AWS CLI

If you've previously downloaded and configured the AWS CLI, Amazon Polly might be
unavailable unless you reconfigure the AWS CLI. The following procedure checks to
see if this is necessary.

###### To reactivate Amazon Polly from the AWS CLI

1. Verify the availability of Amazon Polly by typing the following help
   command at the AWS CLI command prompt.

```
aws polly help
```

If you see a description of Amazon Polly and a list of valid commands
appears in the AWS CLI window, you can use Amazon Polly from the AWS CLI
immediately. In this case, you can skip the rest of this procedure. If
this is not displayed, continue with Step 2. 2. Activate Amazon Polly using one of the two following options:

    1. Uninstall and reinstall the AWS CLI.


    For instructions, see [Installing the AWS Command Line Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md") in the
     *AWS Command Line Interface User Guide*.




    or
    2. Download the file [service-2.json.](https://github.com/boto/botocore/blob/develop/botocore/data/polly/2016-06-10/service-2.json "https://github.com/boto/botocore/blob/develop/botocore/data/polly/2016-06-10/service-2.json")


    At the command prompt, run the following command.



    ```
    aws configure add-model --service-model `file://service-2.json` --service-name polly
    ```

3. Reverify the availability of Amazon Polly.

```
aws polly help
```

The description of Amazon Polly should be visible.
