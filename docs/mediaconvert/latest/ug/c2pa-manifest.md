# Content authenticity with C2PA manifests

When you create MP4 outputs with AWS Elemental MediaConvert, you can optionally embed a C2PA manifest to
provide content provenance and authenticity for your media. C2PA (Coalition for Content
Provenance and Authenticity) is a standardized method for providing verifiable information about
the origin and history of digital content.

C2PA manifests help address the growing issue of misinformation and deepfakes by embedding verifiable information into media files. This information creates a traceable record of the content's origin and modifications.

Some reasons to include C2PA manifests in your workflow might include:

- Provide verifiable information about a media file's transcoding history.
- Allow downstream systems to verify the authenticity of your content.
- Support transparency initiatives for digital media.
  For more information about content authenticity and C2PA, see: [Content Authenticity Initiative](https://contentauthenticity.org/ "https://contentauthenticity.org/") and [C2PA
  specification](https://c2pa.org/specifications/specifications/2.2/index.html "https://c2pa.org/specifications/specifications/2.2/index.html")

###### Topics

- [Configuring a job with a C2PA manifest](c2pa-manifest-use.md "c2pa-manifest-use.md")
- [Requirements for C2PA manifests](c2pa-manifest-requirements.md "c2pa-manifest-requirements.md")
- [C2PA manifest structure](c2pa-manifest-structure.md "c2pa-manifest-structure.md")
- [Verifying C2PA manifests](c2pa-manifest-verification.md "c2pa-manifest-verification.md")
