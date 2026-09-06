

# Working with origin endpoints in AWS Elemental MediaPackage
<a name="endpoints"></a>

An origin endpoint is part of a channel and represents the packaging aspect of MediaPackage. When you create an endpoint on a channel, you indicate what streaming format, packaging parameters, and features the output stream will use. Downstream devices request content from the endpoint. Direct your CDNs to the channel group egress domain for stream delivery from MediaPackage. A channel can have multiple endpoints.

Additionally, the endpoint holds information about digital rights management (DRM) and encryption integration, stream bitrate presentation order, and more.

**Topics**
+ [Creating an origin endpoint](endpoints-create.md)
+ [Viewing an origin endpoint](endpoints-view.md)
+ [Editing an endpoint](endpoints-edit.md)
+ [Resetting an endpoint](endpoint-reset.md)
+ [Deleting an endpoint](endpoints-delete.md)
+ [Previewing a manifest](endpoints-preview.md)