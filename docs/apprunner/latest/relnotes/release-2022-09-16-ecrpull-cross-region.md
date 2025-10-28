# Release: App Runner adds support for using Amazon ECR images from different regions on September 16, 2022

AWS App Runner now supports using Amazon Elastic Container Registry (Amazon ECR) images from any region without image replication. The Amazon ECR images no
longer need to be in the same region as your App Runner service.

**Release date:** September 16, 2022

## Changes

With this release, you can use Amazon ECR images from any AWS Region to create or update your App Runner service. For example, you can launch or update your
App Runner service in the US East (N. Virginia) Region referencing an Amazon ECR image
that's in the US West (Oregon) Region, without the need to store an Amazon ECR
image in US East (N. Virginia).

With this new feature, you can avoid additional costs and operational overhead caused by the Amazon ECR image replication that was required before this
launch.
