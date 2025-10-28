End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Creating a data store

A data store receives and stores your messages. It is not a database but a scalable and
queryable repository of your messages. You can create multiple data stores to store
messages that comes from different devices or locations, or your can use a single data
store to receive all of your AWS IoT messages.

```
aws iotanalytics create-datastore --datastore-name mydatastore
```

To list the data stores you have already created.

```
aws iotanalytics list-datastores
```

To get more information about a data store.

```
aws iotanalytics describe-datastore --datastore-name mydatastore
```
