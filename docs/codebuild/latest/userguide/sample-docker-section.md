# Docker samples for CodeBuild

This section describes sample integrations between Docker and AWS CodeBuild.

| Sample                                                                                                                      | Description                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Docker in custom image sample for CodeBuild](sample-docker-custom-image.md "sample-docker-custom-image.md")                | This sample builds and runs a Docker image by using CodeBuild and a custom Docker build image (`docker:dind` in Docker Hub).                                |
| [Docker image build server sample for CodeBuild](sample-docker-server.md "sample-docker-server.md")                         | This sample offloads your Docker builds to a managed image build server.                                                                                    |
| [Windows Docker builds sample for CodeBuild](sample-windows-docker-custom-image.md "sample-windows-docker-custom-image.md") | This sample builds and runs a Windows Docker image by using CodeBuild.                                                                                      |
| ['Publish Docker image to an Amazon ECR image repository' sample for CodeBuild](sample-docker.md "sample-docker.md")        | This sample produces as build output a Docker image and then pushes the Docker image to an Amazon Elastic Container Registry (Amazon ECR) image repository. |
| [Private registry with AWS Secrets Manager sample for CodeBuild](sample-private-registry.md "sample-private-registry.md")   | This sample shows you how to use a Docker image that is stored in a private registry as your CodeBuild runtime environment.                                 |
