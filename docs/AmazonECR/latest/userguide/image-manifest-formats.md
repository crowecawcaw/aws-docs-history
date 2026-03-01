# Container image manifest format support in Amazon ECR

Amazon ECR supports the following container image manifest formats:

- Docker Image Manifest V2 Schema 1 (used with Docker version 1.9 and
  older)
- Docker Image Manifest V2 Schema 2 (used with Docker version 1.10 and
  newer)
- Open Container Initiative (OCI) Specifications (v1.0 and v1.1)
  Support for Docker Image Manifest V2 Schema 2 provides the following
  functionality:

- The ability to use multiple tags for a singular image.
- Support for storing Windows container images.

## Amazon ECR image manifest conversion

When you push and pull images to and from Amazon ECR, your container engine client (for
example, Docker) communicates with the registry to agree on a manifest format that
is understood by the client and the registry to use for the image.

When you push an image to Amazon ECR with Docker version 1.9 or earlier, the image
manifest format is stored as Docker Image Manifest V2 Schema 1. When you push an
image to Amazon ECR with Docker version 1.10 or later, the image manifest format is
stored as Docker Image Manifest V2 Schema 2.

When you pull an image from Amazon ECR _by tag_, Amazon ECR returns the
image manifest format that is stored in the repository. The format is returned only
if that format is understood by the client. If the stored image manifest format
isn't understood by the client, Amazon ECR converts the image manifest into a format that
is understood. For example, if a Docker 1.9 client requests an image manifest that
is stored as Docker Image Manifest V2 Schema 2, Amazon ECR returns the manifest in the
Docker Image Manifest V2 Schema 1 format. The following table describes the
available conversions supported by Amazon ECR when an image is pulled _by
tag_:

| Schema requested by client | Pushed to ECR as V2, schema 1                                  | Pushed to ECR as V2, schema 2 | Pushed to ECR as OCI       |
| -------------------------- | -------------------------------------------------------------- | ----------------------------- | -------------------------- |
| V2, schema 1               | No translation required                                        | Translated to V2, schema 1    | No translation available   |
| V2, schema 2               | No translation available, client falls back to V2, schema<br>1 | No translation required       | Translated to V2, schema 2 |
| OCI                        | No translation available                                       | Translated to OCI             | No translation required    |

###### Important

If you pull an image _by digest_, there is no translation
available. Your client must understand the image manifest format that is stored
in Amazon ECR. If you request a Docker Image Manifest V2 Schema 2 image by digest on
a Docker 1.9 or older client, the image pull fails. For more information, see [Registry
compatibility](https://docs.docker.com/registry/compatibility/ "https://docs.docker.com/registry/compatibility/") in the Docker documentation.

In this example, if you request the same image _by tag_,
Amazon ECR translates the image manifest into a format that the client can
understand. The image pull succeeds.
