# listOfficialImages

Retrieve the list of AWS ParallelCluster official images.

###### Topics

- [Request syntax](#list-official-images-request "#list-official-images-request")
- [Request body](#list-official-images-request-body "#list-official-images-request-body")
- [Response syntax](#list-official-images-response "#list-official-images-response")
- [Response body](#list-official-images-response-body "#list-official-images-response-body")
- [Example](#list-official-images-example "#list-official-images-example")

## Request syntax

```
GET /v3/images/official
{
  "architecture": "string",
  "os": "string",
  "region": "string"
}
```

## Request body

**architecture**

Filter by architecture. The default is no filtering.

Type: string

Valid values: `x86_64 | arm64`

Required: No

**os**

Filter by OS distribution. The default is no filtering.

Type: string

Valid values: `alinux2 | alinux2023 | ubuntu2404 | ubuntu2204 | rhel8 | rhel9`

Required: No

**region**

The AWS Region in which official images are listed.

Type: string

Required: No

## Response syntax

```
{
  "images": [
    {
      "architecture": "string",
      "amiId": "string",
      "name": "string",
      "os": "string",
      "version": "string"
    }
  ]
}
```

## Response body

**images**

**amiId**

The ID of the AMI.

Type: string

**architecture**

The AMI architecture.

Type: string

**name**

The name of the AMI.

Type: string

**os**

The AMI operating system.

Type: string

**version**

The AWS ParallelCluster version.

Type: string

## Example

Python
Request

```
`$` `list_official_images()`
```

200 Response

```
`{
 'images': [
 {
 'ami_id': 'ami-015cfeb4e0d6306b2',
 'architecture': 'x86_64',
 'name': 'aws-parallelcluster-3.2.1-ubuntu-2204-lts-hvm-x86_64-202202261505 '
 '2022-02-26T15-08-34.759Z',
 'os': 'ubuntu2204',
 'version': '3.2.1'
 },
 ...
 ]
}`
```
