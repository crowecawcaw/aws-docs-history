# Container object in

ASFF

The following example shows the AWS Security Finding Format (ASFF) syntax for the
`Container` object. To view descriptions of `Container`
attributes, see [ContainerDetails](../../1.0/APIReference/API_ContainerDetails.md "../../1.0/APIReference/API_ContainerDetails.md") in
the _AWS Security Hub API Reference_. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

**Example**

```
"Container": {
    "ContainerRuntime": "docker",
    "ImageId": "image12",
    "ImageName": "1111111/knotejs@sha256:372131c9fef111111111111115f4ed3ea5f9dce4dc3bd34ce21846588a3",
    "LaunchedAt": "2018-09-29T01:25:54Z",
    "Name": "knote",
    "Privileged": true,
    "VolumeMounts": [{
        "Name": "vol-03909e9",
        "MountPath": "/mnt/etc"
    }]
}
```
