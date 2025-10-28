# Synchronizing data across clients

If you're new to Amazon Cognito Sync, use [AWS AppSync](https://aws.amazon.com/appsync/ "https://aws.amazon.com/appsync/"). Like Amazon Cognito Sync, AWS AppSync is
a service for synchronizing application data across devices.

It enables user data like app preferences or game state to be synchronized.
It also extends these capabilities by allowing multiple users to
synchronize and collaborate in real time on shared data.

With Amazon Cognito, you can save user data in datasets that contain key-value pairs. Amazon Cognito
associates this data with an identity in your identity pool so that your app can access it
across logins and devices. To sync this data between the Amazon Cognito service and an end user’s
devices, invoke the synchronize method. Each dataset can have a maximum size of 1 MB. You can
associate up to 20 datasets with an identity.

The Amazon Cognito Sync client creates a local cache for the identity data. When your app reads and
writes keys, it communicates with this local cache . This communication guarantees that all
changes you make on the device are immediately available on the device, even when you are
offline. When the synchronize method is called, changes from the service are pulled to the
device, and any local changes are pushed to the service. At this point, the changes are
available to other devices to synchronize.

## Initializing the Amazon Cognito Sync client

To initialize the Amazon Cognito Sync client, you must first create a credentials provider. The
credentials provider acquires temporary AWS credentials to make it possible for your app
to access your AWS resources. You also must import the necessary header files. Use the
following steps to initialize the Amazon Cognito Sync client.

### Android

1. Create a credentials provider, following the instructions in [Getting credentials](getting-credentials.md "getting-credentials.md").
2. Import the Amazon Cognito package as follows: `import
com.amazonaws.mobileconnectors.cognito.*;`
3. Initialize Amazon Cognito Sync. Pass in the Android app context, the identity pool ID, an
   AWS Region, and an initialized Amazon Cognito credentials provider as follows:

```
CognitoSyncManager client = new CognitoSyncManager(
    getApplicationContext(),
    Regions.YOUR_REGION,
    credentialsProvider);
```

### iOS - Objective-C

1. Create a credentials provider, following the instructions in [Getting credentials](getting-credentials.md "getting-credentials.md").
2. Import `AWSCore` and `Cognito`, and initialize
   `AWSCognito` as follows:

```
#import <AWSiOSSDKv2/AWSCore.h>
#import <AWSCognitoSync/Cognito.h>

AWSCognito *syncClient = [AWSCognito defaultCognito];
```

3. If you're using CocoaPods, replace
   `<AWSiOSSDKv2/AWSCore.h>` with `AWSCore.h`. Follow
   the same syntax for the Amazon Cognito import.

### iOS - Swift

1. Create a credentials provider, following the instructions in [Getting credentials](getting-credentials.md "getting-credentials.md").
2. Import and initialize `AWSCognito` as follows:

```
import AWSCognito
let syncClient = AWSCognito.default()!
```

### JavaScript

1. Download the [Amazon Cognito Sync
   Manager for JavaScript](https://github.com/aws/amazon-cognito-js "https://github.com/aws/amazon-cognito-js").
2. Include the Sync Manager library in your project.
3. Create a credentials provider, following the instructions in [Getting credentials](getting-credentials.md "getting-credentials.md").
4. Initialize the Sync Manager as follows:

```
var syncManager = new AWS.CognitoSyncManager();
```

### Unity

1. Create an instance of `CognitoAWSCredentials`, following the
   instructions in [Getting credentials](getting-credentials.md "getting-credentials.md").
2. Create an instance of `CognitoSyncManager`. Pass the
   `CognitoAwsCredentials` object and a
   `AmazonCognitoSyncConfig`, and include at least the Region set, as follows:

```
AmazonCognitoSyncConfig clientConfig = new AmazonCognitoSyncConfig { RegionEndpoint = REGION };
CognitoSyncManager syncManager = new CognitoSyncManager(credentials, clientConfig);
```

### Xamarin

1. Create an instance of `CognitoAWSCredentials`, following the
   instructions in [Getting credentials](getting-credentials.md "getting-credentials.md").
2. Create an instance of `CognitoSyncManager`. Pass the
   `CognitoAwsCredentials` object and a
   `AmazonCognitoSyncConfig`, and include at least the Region set, as follows:

```
AmazonCognitoSyncConfig clientConfig = new AmazonCognitoSyncConfig { RegionEndpoint = REGION };
CognitoSyncManager syncManager = new CognitoSyncManager(credentials, clientConfig);
```

## Understanding datasets

Amazon Cognito organizes user profile data into datasets. Each dataset can contain up to 1MB of
data in the form of key-value pairs. A dataset is the most granular entity that you can
synchronize. Read and write operations performed on a dataset only affect the local store
until the synchronize method is invoked. Amazon Cognito identifies a dataset by a unique string. You
can create a new dataset or open an existing one as follows.

### Android

```
Dataset dataset = client.openOrCreateDataset("datasetname");
```

To delete a dataset, first call the method to remove it from local storage, then call
the `synchronize` method to delete the dataset from Amazon Cognito as follows:

```
dataset.delete();
dataset.synchronize(syncCallback);
```

### iOS - Objective-C

```
AWSCognitoDataset *dataset = [syncClient openOrCreateDataset:@"myDataSet"];

```

To delete a dataset, first call the method to remove it from local storage, then call
the `synchronize` method to delete the dataset from Amazon Cognito as follows:

```
[dataset clear];
[dataset synchronize];
```

### iOS - Swift

```
let dataset = syncClient.openOrCreateDataset("myDataSet")!
```

To delete a dataset, first call the method to remove it from local storage, then call
the `synchronize` method as follows: to delete the dataset from Amazon Cognito:

```
dataset.clear()
dataset.synchronize()
```

### JavaScript

```
syncManager.openOrCreateDataset('myDatasetName', function(err, dataset) {
   // ...
});
```

### Unity

```
string myValue = dataset.Get("myKey");
dataset.Put("myKey", "newValue");
```

To delete a key from a dataset, use `Remove` as follows:

```
dataset.Remove("myKey");
```

### Xamarin

```
Dataset dataset = syncManager.OpenOrCreateDataset("myDatasetName");
```

To delete a dataset, first call the method to remove it from local storage, then call
the `synchronize` method to delete the dataset from Amazon Cognito as follows:

```
dataset.Delete();
dataset.SynchronizeAsync();
```

## Reading

and writing data in datasets

Amazon Cognito datasets function as dictionaries, with values accessible by key. You can read,
add, or modify keys and values of a dataset just as if the dataset were a dictionary, as
shown in the following examples.

Note that values you write to a dataset only affect the local cached copy of the data
until you call the synchronize method.

### Android

```
String value = dataset.get("myKey");
dataset.put("myKey", "my value");
```

### iOS - Objective-C

```
[dataset setString:@"my value" forKey:@"myKey"];
NSString *value = [dataset stringForKey:@"myKey"];
```

### iOS - Swift

```
dataset.setString("my value", forKey:"myKey")
let value = dataset.stringForKey("myKey")
```

### JavaScript

```
dataset.get('myKey', function(err, value) {
  console.log('myRecord: ' + value);
});

dataset.put('newKey', 'newValue', function(err, record) {
  console.log(record);
});

dataset.remove('oldKey', function(err, record) {
  console.log(success);
});
```

### Unity

```
string myValue = dataset.Get("myKey");
dataset.Put("myKey", "newValue");
```

### Xamarin

```
//obtain a value
string myValue = dataset.Get("myKey");

// Create a record in a dataset and synchronize with the server
dataset.OnSyncSuccess += SyncSuccessCallback;
dataset.Put("myKey", "myValue");
dataset.SynchronizeAsync();

void SyncSuccessCallback(object sender, SyncSuccessEventArgs e) {
  // Your handler code here
}
```

### Android

To remove keys from a dataset, use the `remove` method as follows:

```
dataset.remove("myKey");
```

### iOS - Objective-C

To delete a key from a
dataset,
use `removeObjectForKey` as follows:

```
[dataset removeObjectForKey:@"myKey"];
```

### iOS - Swift

To
delete a key from a dataset, use `removeObjectForKey` as follows:

```
dataset.removeObjectForKey("myKey")
```

### Unity

To delete a key from a dataset, use `Remove` as follows:

```
dataset.Remove("myKey");
```

### Xamarin

You can use `Remove` to delete a key from a dataset:

```
dataset.Remove("myKey");
```

## Synchronizing local data with the sync store

### Android

The `synchronize` method compares local cached data to the data stored in
the Amazon Cognito Sync store. Remote changes are pulled from the Amazon Cognito Sync store; conflict
resolution is invoked if any conflicts occur; and updated values on the device are pushed
to the service. To synchronize a dataset, call its `synchronize` method:

```
dataset.synchronize(syncCallback);
```

The `synchronize` method receives an implementation of the
`SyncCallback` interface, discussed below.

The `synchronizeOnConnectivity()` method attempts to synchronize when
connectivity is available. If connectivity is immediately available,
`synchronizeOnConnectivity()` behaves like `synchronize()`.
Otherwise it monitors for connectivity changes and performs a sync once connectivity is
available. If `synchronizeOnConnectivity()`is called multiple times, only the
last synchronize request is kept, and only the last callback will fire. If either the
dataset or the callback is garbage-collected, this method won't perform a sync, and the
callback won't fire.

To learn more about dataset synchronization and the different callbacks, see [Handling event callbacks](handling-callbacks.md "handling-callbacks.md").

### iOS - Objective-C

The `synchronize` method compares local cached data to the data stored in
the Amazon Cognito Sync store. Remote changes are pulled from the Amazon Cognito Sync store; conflict
resolution is invoked if any conflicts occur; and updated values on the device are pushed
to the service. To synchronize a dataset, call its `synchronize` method:

The `synchronize` method is asynchronous and returns an
`AWSTask` object to handle the response:

```
[[dataset synchronize] continueWithBlock:^id(AWSTask *task) {
    if (task.isCancelled) {
        // Task cancelled.
    } else if (task.error) {
        // Error while executing task.
    } else {
        // Task succeeded. The data was saved in the sync store.
    }
    return nil;
}];
```

The `synchronizeOnConnectivity` method attempts to synchronize when the
device has connectivity. First, `synchronizeOnConnectivity` checks for
connectivity and, if the device is online, immediately invokes synchronize and returns the
`AWSTask` object associated with the attempt.

If the device is offline, `synchronizeOnConnectivity` 1) schedules a
synchronize for the next time the device comes online and 2) returns an
`AWSTask` with a nil result. The scheduled synchronize is only valid for the
lifecycle of the dataset object. The data will not be synchronized if the app is exited
before connectivity is regained. If you want to be notified when events occur during the
scheduled synchronize, you must add observers of the notifications found in
`AWSCognito`.

To learn more about dataset synchronization and the different callbacks, see [Handling event callbacks](handling-callbacks.md "handling-callbacks.md").

### iOS - Swift

The `synchronize` method compares local cached data to the data stored in
the Amazon Cognito Sync store. Remote changes are pulled from the Amazon Cognito Sync store; conflict
resolution is invoked if any conflicts occur; and updated values on the device are pushed
to the service. To synchronize a dataset, call its `synchronize` method:

The `synchronize` method is asynchronous and returns an
`AWSTask` object to handle the response:

```
dataset.synchronize().continueWith(block: { (task) -> AnyObject? in

            if task.isCancelled {
                // Task cancelled.
            } else if task.error != nil {
                // Error while executing task
            } else {
                // Task succeeded. The data was saved in the sync store.
            }
            return task
})
```

The `synchronizeOnConnectivity` method attempts to synchronize when the
device has connectivity. First, `synchronizeOnConnectivity` checks for
connectivity and, if the device is online, immediately invokes `synchronize`
and returns the `AWSTask` object associated with the attempt.

If the device is offline, `synchronizeOnConnectivity` 1) schedules a
synchronize for the next time the device comes online and 2) returns an
`AWSTask` object with a nil result. The scheduled synchronize is only valid
for the lifecycle of the dataset object. The data will not be synchronized if the app is
exited before connectivity is regained. If you want to be notified when events occur
during the scheduled synchronize, you must add observers of the notifications found in
`AWSCognito`.

To learn more about dataset synchronization and the different callbacks, see [Handling event callbacks](handling-callbacks.md "handling-callbacks.md").

### JavaScript

The `synchronize` method compares local cached data to the data stored in
the Amazon Cognito Sync store. Remote changes are pulled from the Amazon Cognito Sync store; conflict
resolution is invoked if any conflicts occur; and updated values on the device are pushed
to the service. To synchronize a dataset, call its `synchronize` method:

```
dataset.synchronize();
```

To learn more about dataset synchronization and the different callbacks, see [Handling event callbacks](handling-callbacks.md "handling-callbacks.md").

### Unity

The synchronize method compares local cached data to the data stored in the Amazon Cognito Sync
store. Remote changes are pulled from the Amazon Cognito Sync store; conflict resolution is invoked
if any conflicts occur; and updated values on the device are pushed to the service. To
synchronize a dataset, call its `synchronize` method:

```
dataset.Synchronize();
```

Synchronize will run asynchronously and will end up calling one of the several
callbacks you can specify in the Dataset.

To learn more about dataset synchronization and the different callbacks, see [Handling event callbacks](handling-callbacks.md "handling-callbacks.md").

### Xamarin

The `synchronize` method compares local cached data to the data stored in
the Amazon Cognito Sync store. Remote changes are pulled from the Amazon Cognito Sync store; conflict
resolution is invoked if any conflicts occur; and updated values on the device are pushed
to the service. To synchronize a dataset, call its `synchronize` method:

```
dataset.SynchronizeAsync();
```

To learn more about dataset synchronization and the different callbacks, see [Handling event callbacks](handling-callbacks.md "handling-callbacks.md").
