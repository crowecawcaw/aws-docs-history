# Deploying SPEKE

Your digital rights management (DRM) system provider can help you get set up to use DRM
encryption in MediaConvert. Generally, the provider gives you a SPEKE gateway to deploy in your
AWS account in the same AWS Region where MediaConvert is running.

If you must build your own API Gateway to connect MediaConvert to your key service, you can use the
[SPEKE Reference
Server](https://github.com/awslabs/speke-reference-server "https://github.com/awslabs/speke-reference-server") available on GitHub as a starting point.
