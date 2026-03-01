# File format for key-value pairs

When you create a UTF-8 encoded file, use the following JSON format:

```
{
  "data":[
    {
      "key":"`key1`",
      "value":"`value`"
    },
    {
      "key":"`key2`",
      "value":"`value`"
    }
  ]
}
```

Your file can't include duplicate keys. If you specified an invalid file in your
Amazon S3 bucket, you can update the file to remove any duplicates and then try creating
your key value store again.

For more information, see [Create a key value store](kvs-with-functions-create.md "kvs-with-functions-create.md").

###### Note

The file for your data source and its key-value pairs have the following
limits:

- File size – 5 MB
- Key size – 512 characters
- Value size – 1024 characters
