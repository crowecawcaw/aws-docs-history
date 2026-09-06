

# Renaming the customer managed configuration recorder
<a name="managing-recorder_console-rename"></a>

You must use the AWS CLI to rename the customer managed configuration recorder. To change the name of the customer managed configuration recorder, you must delete it and create a new configuration recorder with your specified name. 

**Renaming the customer managed configuration recorder using the AWS CLI**

1. Use the [`describe-configuration-recorders`](http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-configuration-recorders.html) command to look up the name of your current customer managed configuration recorder:

   ```
   $ aws configservice describe-configuration-recorders
   {
       "ConfigurationRecorders": [
           {
               "roleARN": "arn:aws:iam::012345678912:role/myConfigRole",
               "name": "default"
           }
       ]
   }
   ```

1. Use the [`delete-configuration-recorder`](http://docs.aws.amazon.com/cli/latest/reference/configservice/delete-configuration-recorder.html) command to delete your customer managed current configuration recorder:

   ```
   $ aws configservice delete-configuration-recorder --configuration-recorder-name {{default}}
   ```

1. Use the [`put-configuration-recorder`](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-configuration-recorder.html) command to create a customer managed configuration recorder with the new name:

   ```
   $ aws configservice put-configuration-recorder --configuration-recorder name={{configRecorderName}},roleARN={{arn:aws:iam::012345678912:role/myConfigRole}}
   ```

1. Use the [`start-configuration-recorder`](http://docs.aws.amazon.com/cli/latest/reference/configservice/start-configuration-recorder.html) command to resume recording:

   ```
   $ aws configservice start-configuration-recorder --configuration-recorder-name {{configRecorderName}}
   ```