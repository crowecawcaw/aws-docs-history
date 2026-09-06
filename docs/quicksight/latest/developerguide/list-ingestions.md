

# ListIngestions
<a name="list-ingestions"></a>

Use the `ListIngestions` operation to list the history of SPICE ingestioned for a dataset.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-ingestions 
    --data-set-id {{DATASETID}} 
    --aws-account-id {{AWSACCOUNTID}} 
    --page-size {{10}}
    --max-items {{100}}
```

------

For more information about the `ListIngestions` operation, see [ListIngestions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListIngestions) in the *Quick Sight API Reference*.