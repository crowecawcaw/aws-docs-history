# Renaming the customer managed configuration

recorder

You must use the AWS CLI to rename the customer managed configuration recorder. To change
the name of the customer managed configuration recorder, you must delete it and create a new
configuration recorder with your specified name.

###### Renaming the customer managed configuration recorder using the AWS CLI

1. Use the [`describe-configuration-recorders`](../../../cli/latest/reference/configservice/describe-configuration-recorders.md "../../../cli/latest/reference/configservice/describe-configuration-recorders.md") command to look up the name
   of your current customer managed configuration recorder:

```
$ **aws configservice describe-configuration-recorders**
{
    "ConfigurationRecorders": [
        {
            "roleARN": "arn:aws:iam::012345678912:role/myConfigRole",
            "name": "default"
        }
    ]
}
```

2. Use the [`delete-configuration-recorder`](../../../cli/latest/reference/configservice/delete-configuration-recorder.md "../../../cli/latest/reference/configservice/delete-configuration-recorder.md") command to delete your
   customer managed current configuration recorder:

```
$ **aws configservice delete-configuration-recorder --configuration-recorder-name `default`**
```

3. Use the [`put-configuration-recorder`](../../../cli/latest/reference/configservice/put-configuration-recorder.md "../../../cli/latest/reference/configservice/put-configuration-recorder.md") command to create a customer
   managed configuration recorder with the new name:

```
$ **aws configservice put-configuration-recorder --configuration-recorder name=`configRecorderName`,roleARN=`arn:aws:iam::012345678912:role/myConfigRole`**
```

4. Use the [`start-configuration-recorder`](../../../cli/latest/reference/configservice/start-configuration-recorder.md "../../../cli/latest/reference/configservice/start-configuration-recorder.md") command to resume
   recording:

```
$ **aws configservice start-configuration-recorder --configuration-recorder-name `configRecorderName`**
```
