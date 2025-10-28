# Windows EC2 Instance Deployment

Deciding the right storage layout is important to ensure you are able to meet required IO. Amazon EBS general purpose volume (gp2) provides 3 IOPS per GB whereas provisioned IOPS (io1) provide a max of 50 IOPS per GB. See [EBS features](https://aws.amazon.com/ebs/features/?nc=sn&loc=1 "https://aws.amazon.com/ebs/features/?nc=sn&loc=1") for details. If you decide to separate SQL data, log, and tempdb to different volumes, consider these aspects.

For gp2, with one volume for all (data, log, and tempdb). Create storage config file as below. Replace placeholder `<size>` as per your requirement.

```
[
    {
        "DeviceName": "xvdb",
        "Ebs": {
            "VolumeSize": <size>,
            "VolumeType": "gp2",
            "DeleteOnTermination": true
        }
    }
]
```

For separate volumes, gp2 (data), io1 (log) and io1 (tempdb) create storage configuration file as below. Replace placeholders `<size>` and `<IOPS Required>` with size of the disk and IOPS you need.

```
[
    {
        "DeviceName": "xvdb",
        "Ebs": {
            "VolumeSize": <size>,
            "VolumeType": "gp2",
            "DeleteOnTermination": true
        }
    },
    {
        "DeviceName": "xvdc",
        "Ebs": {
            "VolumeSize": <size>,
            "VolumeType": “io1",
            "Iops": <IOPS Required>,
            "DeleteOnTermination": true
        }
    },
    {
        "DeviceName": "xvdd",
        "Ebs": {
            "VolumeSize": <size>,
            "VolumeType": “io1",
            "Iops": <IOPS Required>,
            "DeleteOnTermination": true
        }
    }
]
```
