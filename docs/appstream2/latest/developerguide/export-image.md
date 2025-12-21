# Export Image

You can export your images to create EC2 AMIs. Later you can [Import Image](import-image.md "import-image.md") those AMIs back to create WorkSpaces Applications images. This helps you to use your own AMI customization tools for customizing of your images.

###### Note

During export following components will be removed from your images

- WorkSpaces Applications agent
- Microsoft license included applications, which were added using Image Builder
- Only Microsoft Windows Server 2022 and 2025 images can be exported.

## IAM Role Requirements

###### Important

Create an IAM role with the following permissions to use for export import:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCopyImage",
            "Effect": "Allow",
            "Action": "ec2:CopyImage",
            "Resource": "*"
        },
        {
            "Sid": "AllowDescribeImages",
            "Effect": "Allow",
            "Action": "ec2:DescribeImages",
            "Resource": "*"
        },
        {
            "Sid": "AllowCreateTags",
            "Effect": "Allow",
            "Action": "ec2:CreateTags",
            "Resource": "*"
        }
    ]
}
```

Add the following trust relationship for this IAM role

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "appstream.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

## To export an image

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the navigation pane, choose **Images**, **Image Registry**.
3. In the image list, select the private image you want to export.
4. Choose **Actions**, **Export**.
5. In the **Export image** dialog box, type a unique **AMI name** and optionally **AMI Description** for the AMI.
6. **IAM Role** - Select the IAM role that you have created for image export.
7. You optionally copy tags from your Image to AMI by checking the **Copy tags in export** checkbox.
8. Choose **Export Image**.
