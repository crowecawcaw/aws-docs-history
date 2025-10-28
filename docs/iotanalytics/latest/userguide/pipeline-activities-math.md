End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Math activity

A `math` activity computes an arithmetic expression using the message's
attributes. The expression must return a number. For example, given the following input
message:

```
{
    "tempF": 50,
}
```

after processing by the following `math` activity:

```
{
    "math": {
        "name": "MyMathActivity",
        "math": "(tempF - 32) / 2",
        "attribute": "tempC",
        "next": "MyDatastoreActivity"
    }
}
```

the resulting message looks like:

```

{
    "tempF" : 50,
    "tempC": 9
}

```
