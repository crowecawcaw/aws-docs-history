# Use `ListImages` with an AWS SDK or CLI

The following code examples show how to use `ListImages`.

CLI

**AWS CLI**

**To list the images in a repository**

The following `list-images` example displays a list of the images in the `cluster-autoscaler` repository.

```
`aws ecr list-images \
 --repository-name `cluster-autoscaler``

```

Output:

```
{
    "imageIds": [
        {
            "imageDigest": "sha256:99c6fb4377e9a420a1eb3b410a951c9f464eff3b7dbc76c65e434e39b94b6570",
            "imageTag": "v1.13.8"
        },
        {
            "imageDigest": "sha256:99c6fb4377e9a420a1eb3b410a951c9f464eff3b7dbc76c65e434e39b94b6570",
            "imageTag": "v1.13.7"
        },
        {
            "imageDigest": "sha256:4a1c6567c38904384ebc64e35b7eeddd8451110c299e3368d2210066487d97e5",
            "imageTag": "v1.13.6"
        }
    ]
}
```

- For API details, see
  [ListImages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/list-images.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/list-images.html")
  in _AWS CLI Command Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ecr#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ecr#code-examples").

```
async fn show_images(
    client: &aws_sdk_ecr::Client,
    repository: &str,
) -> Result<(), aws_sdk_ecr::Error> {
    let rsp = client
        .list_images()
        .repository_name(repository)
        .send()
        .await?;

    let images = rsp.image_ids();

    println!("found {} images", images.len());

    for image in images {
        println!(
            "image: {}:{}",
            image.image_tag().unwrap(),
            image.image_digest().unwrap()
        );
    }

    Ok(())
}


```

- For API details, see
  [ListImages](https://docs.rs/aws-sdk-ecr/latest/aws_sdk_ecr/client/struct.Client.html#method.list_images "https://docs.rs/aws-sdk-ecr/latest/aws_sdk_ecr/client/struct.Client.html#method.list_images")
  in _AWS SDK for Rust API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon ECR with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
