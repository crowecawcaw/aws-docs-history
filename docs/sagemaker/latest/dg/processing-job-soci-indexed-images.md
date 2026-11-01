

# Speed up processing job startup with SOCI-indexed images
<a name="processing-job-soci-indexed-images"></a>

A processing job downloads its container image before it runs your script. For large images, such as images that bundle deep learning frameworks or many data-processing libraries, this adds minutes to every processing job.

Seekable OCI (SOCI) is an open-source technology from AWS for loading container images on demand (*lazy loading*). For the project, see [soci-snapshotter](https://github.com/awslabs/soci-snapshotter) on the GitHub website.

How it works:
+ Most container runtimes download the whole image before they start the container, even though the container needs only a small part of it to start.
+ A SOCI index maps the files inside each layer of the image, so the runtime can read one file without downloading the whole layer.
+ You create the index from your existing image. You don't rebuild the image. The index is stored next to the image in Amazon ECR.
+ When the processing job starts, the runtime downloads only the files needed to start the container. The rest is downloaded in the background as your script uses it.

To use it, reference a SOCI-indexed image in your `CreateProcessingJob` request. Nothing else in the processing job changes.
+ Processing and training jobs use SOCI-indexed images the same way.
+ This page covers what is specific to processing jobs. For creating and verifying an index, see [Speed up training job startup with SOCI-indexed images](train-soci-indexed-images.md).

**Topics**
+ [How it works](#processing-job-soci-indexed-images-how)
+ [Considerations](#processing-job-soci-indexed-images-considerations)
+ [Get a SOCI-indexed image](#processing-job-soci-indexed-images-get)
+ [Use a SOCI-indexed image in a processing job](#processing-job-soci-indexed-images-use)
+ [Permissions](#processing-job-soci-indexed-images-permissions)
+ [Prevent job failures: check your code for Docker-specific assumptions](#processing-job-soci-indexed-images-docker-assumptions)
+ [Related resources](#processing-job-soci-indexed-images-related)

## How it works
<a name="processing-job-soci-indexed-images-how"></a>

When you create a processing job, SageMaker AI checks whether the image you specified has a SOCI index and behaves accordingly:


| Scenario | What happens | 
| --- | --- | 
| The image includes a SOCI index | SageMaker AI lazy-loads the image and starts your container before the full download completes | 
| The image has no SOCI index | Normal download - no change in behavior | 
| The index can't be read, or lazy loading doesn't succeed | The processing job falls back to a standard download and continues running | 

Adding an index never prevents a processing job from running. In either case the image download is reported in the processing job's `Downloading` secondary status.

## Considerations
<a name="processing-job-soci-indexed-images-considerations"></a>
+ **Where the image is stored**
  + Store the image (`AppSpecification.ImageUri`) in an Amazon ECR **private** repository.
  + Reference the image by **tag** (`repository:tag`). An image referenced by digest (`repository@sha256:…`) is downloaded normally.
+ **Which index format is detected**
  + The tag must point to an image that contains a SOCI index v2. For the index formats that are detected, see [Considerations](train-soci-indexed-images.md#train-soci-indexed-images-considerations) on the training page.
+ **When the time saved is smaller**
  + Files are downloaded the first time your script opens them.
  + If your script reads a large part of the image before it starts work (for example, a model or large library stored in the image), that time moves from the download to the start of your script.
+ **Large inputs**
  + With `S3InputMode` set to `File`, the processing job also waits for the input download. With a very large input, that wait can take longer than the image download.
  + Use `Pipe` input mode, or read directly from Amazon S3 in your script, to keep the benefit.
+ **SageMaker AI-managed processing images**
  + SageMaker AI-managed processing images, such as the Spark and scikit-learn processing containers, aren't published with SOCI indexes.
  + To use lazy loading, build your own image (for example, `FROM` one of them) and index it.

## Get a SOCI-indexed image
<a name="processing-job-soci-indexed-images-get"></a>
+ **AWS Deep Learning Containers:** SOCI-indexed variants have a `-soci` tag suffix. A DLC can be the image of a processing job; the container runs the command in `AppSpecification.ContainerEntrypoint`. See [Use a Deep Learning Container that includes a SOCI index](train-soci-indexed-images.md#train-soci-indexed-images-dlc).
+ **Your own image:** the procedure is the same as for training. See [Create a SOCI index for your own image](train-soci-indexed-images.md#train-soci-indexed-images-create) and [Verify that an image includes a SOCI index](train-soci-indexed-images.md#train-soci-indexed-images-verify).

## Use a SOCI-indexed image in a processing job
<a name="processing-job-soci-indexed-images-use"></a>

Set the indexed image as `ImageUri` in [AppSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AppSpecification.html):

```
"AppSpecification": {
  "ImageUri": "111122223333.dkr.ecr.us-east-1.amazonaws.com/repository-name:soci-indexed-image-tag",
  "ContainerEntrypoint": ["python3", "/opt/ml/processing/input/code/preprocessing.py"]
}
```

With the SageMaker Python SDK:

```
from sagemaker.core.processing import ScriptProcessor

processor = ScriptProcessor(
    image_uri="111122223333.dkr.ecr.us-east-1.amazonaws.com/repository-name:soci-indexed-image-tag",
    command=["python3"],
    role="arn:aws:iam::111122223333:role/execution-role-name",
    instance_type="ml.m5.4xlarge",
    instance_count=1,
)
processor.run(code="preprocessing.py")
```

## Permissions
<a name="processing-job-soci-indexed-images-permissions"></a>
+ **To run a processing job:** the execution role needs the same Amazon ECR actions as for any other image, listed in [CreateProcessingJob API: Execution Role Permissions](sagemaker-roles.md#sagemaker-roles-createprocessingjob-perms). Lazy loading needs no additional permissions.
  + `ecr:GetAuthorizationToken`
  + `ecr:BatchCheckLayerAvailability`
  + `ecr:GetDownloadUrlForLayer`
  + `ecr:BatchGetImage`
+ **To create and push indexes:** see [Permissions](train-soci-indexed-images.md#train-soci-indexed-images-permissions) on the training page.

## Prevent job failures: check your code for Docker-specific assumptions
<a name="processing-job-soci-indexed-images-docker-assumptions"></a>

SOCI-indexed images run on a containerd-based runtime, not on Docker:
+ Container behavior is the same.
+ Code that detects a container by looking for Docker-specific files can take a different path.
+ Review your entry point and setup scripts for the patterns in the following table.


| Pattern | Why it matters | Recommendation | 
| --- | --- | --- | 
| Checking for the /.dockerenv file | Created by the Docker daemon; not part of any container standard | Set your own environment variable, or detect containerization without depending on a runtime | 
| Matching docker in /proc/self/cgroup or /proc/1/cgroup | Cgroup paths differ between runtimes and cgroup versions | Don't branch on the runtime name | 
| Deriving a container ID from a cgroup path or the host name format | Runtime-specific formats | Pass identifiers in as environment variables | 
| Calling the docker CLI or /var/run/docker.sock inside the container | Not available | Remove the dependency; SageMaker AI manages the container lifecycle | 

SageMaker AI mounts a `/.dockerenv` marker in the container so that existing checks keep working; don't add new dependencies on it.

## Related resources
<a name="processing-job-soci-indexed-images-related"></a>
+ [Speed up training job startup with SOCI-indexed images](train-soci-indexed-images.md) - the same feature for training jobs, including how to create and verify an index
+ [Speed up container startup with SOCI](soci-indexing.md) - SOCI indexing for Studio
+ [AppSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AppSpecification.html) in the API reference and [How to Build Your Own Processing Container (Advanced Scenario)](build-your-own-processing-container.md)
+ [SOCI index for AWS Deep Learning Containers](https://aws.github.io/deep-learning-containers/tutorials/SOCI/) on the GitHub website