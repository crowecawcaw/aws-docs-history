# Using Terraform to create tags for AMS Accelerate

If you don't want to use AMS Accelerate Resource Tagger, you can apply your own tags using Terraform. However, if you
don't want to use Resource Tagger because of its drift from your Terraform definitions, there is a way for you to use
the Resource Tagger and ignore the drift it causes; see [Configuring Terraform to ignore Resource Tagger tags](acc-rt-using.md#acc-rt-ignore-tags "acc-rt-using.md#acc-rt-ignore-tags").

###### Important

Some AMS Accelerate service components require tags with the **ams:rt:** prefix.
Resource Tagger believes that it owns these tags, and deletes them if no Resource Tagger configuration rules permit them.
You must deploy a Resource Tagger configuration profile for these tags, even if you are using AWS CloudFormation or Terraform.

The following is an example of how you can apply the tag **ams:rt:ams-managed** with the
value **true** to an Amazon EC2 instance managed by Terraform. The **ams:rt:ams-managed** tag
opts you in to having your resources monitored by AMS Accelerate.

```

  resource "aws_instance" "sample_linux_instance" {
    # ...ami and other properties...

    instance_type = "t3.micro"

    tags = {
        "ams:rt:ams-managed" = "true"
    }
}

```

The following is an example of how you can apply the tag
**ams:rt:ams-managed** with the value **true** to an Auto Scaling group managed by Terraform. Note that the Auto Scaling group propagates its
tags to the Amazon EC2 instances that are created by it. The **ams:rt:ams-managed** tag opts you in to having your resources monitored by AMS Accelerate.

```

  resource "aws_autoscaling_group" "sample_asg" {
    # ...other properties...

    name = "terraform-sample"

    tags = {
        "ams:rt:ams-managed" = "true"
    }
}

```

For a description of how to manage Terraform-created resource tags, see
[Configuring Terraform to ignore Resource Tagger tags](acc-rt-using.md#acc-rt-ignore-tags "acc-rt-using.md#acc-rt-ignore-tags").
