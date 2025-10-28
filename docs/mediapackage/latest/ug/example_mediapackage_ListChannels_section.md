# Use `ListChannels` with an AWS SDK or CLI

The following code examples show how to use `ListChannels`.

CLI

**AWS CLI**

**To list all channels**

The following `list-channels` command lists all of the channels that are configured on the current AWS account.

```
`aws mediapackage list-channels`

```

Output:

```
{
    "Channels": [
        {
            "Arn": "arn:aws:mediapackage:us-west-2:111222333:channels/584797f1740548c389a273585dd22a63",
            "HlsIngest": {
                "IngestEndpoints": [
                    {
                        "Id": "584797f1740548c389a273585dd22a63",
                        "Password": "webdavgeneratedpassword1",
                        "Url": "https://9be9c4405c474882.mediapackage.us-west-2.amazonaws.com/in/v2/584797f1740548c389a273585dd22a63/584797f1740548c389a273585dd22a63/channel",
                        "Username": "webdavgeneratedusername1"
                    },
                    {
                        "Id": "7d187c8616fd455f88aaa5a9fcf74442",
                        "Password": "webdavgeneratedpassword2",
                        "Url": "https://7bf454c57220328d.mediapackage.us-west-2.amazonaws.com/in/v2/584797f1740548c389a273585dd22a63/7d187c8616fd455f88aaa5a9fcf74442/channel",
                        "Username": "webdavgeneratedusername2"
                    }
                ]
            },
            "Id": "test",
            "Tags": {}
        }
    ]
}
```

For more information, see [Viewing Channel Details](channels-view.md "channels-view.md") in the _AWS Elemental MediaPackage User Guide_.

- For API details, see
  [ListChannels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/list-channels.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/list-channels.html")
  in _AWS CLI Command Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/mediapackage#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/mediapackage#code-examples").

List channel ARNs and descriptions.

```
async fn show_channels(client: &Client) -> Result<(), Error> {
    let list_channels = client.list_channels().send().await?;

    println!("Channels:");

    for c in list_channels.channels() {
        let description = c.description().unwrap_or_default();
        let arn = c.arn().unwrap_or_default();

        println!("  Description : {}", description);
        println!("  ARN :         {}", arn);
        println!();
    }

    Ok(())
}


```

- For API details, see
  [ListChannels](https://docs.rs/aws-sdk-mediapackage/latest/aws_sdk_mediapackage/client/struct.Client.html#method.list_channels "https://docs.rs/aws-sdk-mediapackage/latest/aws_sdk_mediapackage/client/struct.Client.html#method.list_channels")
  in _AWS SDK for Rust API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
