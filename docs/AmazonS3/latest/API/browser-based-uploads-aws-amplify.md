# Browser-based uploads to Amazon S3 using
 the AWS Amplify library

This section describes how to upload files to Amazon S3 using the AWS Amplify JavaScript
 library.

For information about setting up the AWS Amplify library, see [AWS Amplify
 Installation and Configuration](https://aws.github.io/aws-amplify/ "https://aws.github.io/aws-amplify/").


## Using the AWS Amplify JavaScript
 library to Upload Files to Amazon S3


The AWS Amplify library `Storage` module gives a simple browser-based
 upload mechanism for managing user content in public or private Amazon S3 storage. 


###### Example : AWS Amplify Manual Setup

The following example shows the manual setup for using the AWS Amplify Storage module. The
 default implementation of the Storage module uses Amazon S3. 


```
import Amplify from 'aws-amplify';
Amplify.configure(
    Auth: {
        identityPoolId: 'XX-XXXX-X:XXXXXXXX-XXXX-1234-abcd-1234567890ab', //REQUIRED - Amazon Cognito Identity Pool ID
        region: 'XX-XXXX-X', // REQUIRED - Amazon Cognito Region
        userPoolId: 'XX-XXXX-X_abcd1234', //OPTIONAL - Amazon Cognito User Pool ID
        userPoolWebClientId: 'XX-XXXX-X_abcd1234', //OPTIONAL - Amazon Cognito Web Client ID
    },
    Storage: {
        bucket: '', //REQUIRED -  Amazon S3 bucket
        region: 'XX-XXXX-X', //OPTIONAL -  Amazon service region
    }
);
```

###### Example : Put data into Amazon S3

The following example shows how to `put` public data into
 Amazon S3.


```
Storage.put('test.txt', 'Hello')
        .then (result => console.log(result))
        .catch(err => console.log(err));
```
The following example shows how to `put` private data into
 Amazon S3.


```
Storage.put('test.txt', 'Private Content', {
        level: 'private',
        contentType: 'text/plain'
    })
    .then (result => console.log(result))
    .catch(err => console.log(err));
```

For more information about using the AWS Amplify Storage module, see [AWS Amplify
 Storage](https://aws.github.io/aws-amplify/media/storage_guide.html "https://aws.github.io/aws-amplify/media/storage_guide.html").


## More Info


[AWS Amplify
 Quick Start](https://aws.github.io/aws-amplify/ "https://aws.github.io/aws-amplify/")
