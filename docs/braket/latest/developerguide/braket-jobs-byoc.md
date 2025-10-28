# Bring your own container (BYOC)

Amazon Braket Hybrid Jobs provides three pre-built containers for running code in different
environments. If one of these containers supports your use case, you only have to provide
your algorithm script when you create a hybrid job. Minor missing dependencies can be added
from your algorithm script or from a `requirements.txt` file using
`pip`.

If none of these containers support your use case, or if you wish to expand on them,
Braket Hybrid Jobs supports running hybrid jobs with your own custom Docker
container image, or bring your own container (BYOC). Make sure
it is the right feature for your use case.

###### In this section:

- [When is bringing my own container the right decision?](#bring-own-container-decision "#bring-own-container-decision")
- [Recipe for bringing your own container](bring-own-container-recipe.md "bring-own-container-recipe.md")
- [Running Braket hybrid jobs in your own container](running-hybrid-jobs-in-own-container.md "running-hybrid-jobs-in-own-container.md")

## When is bringing my own container the right decision?

Bringing your own container (BYOC) to Braket Hybrid Jobs offers the flexibility to use
your own software by installing it in a packaged environment. Depending on your specific needs,
there may be ways to achieve the same flexibility without having to go through the full
BYOC Docker build - Amazon ECR upload - custom image URI cycle.

###### Note

BYOC may not be the right choice if you want to add a small number of additional Python packages
(generally fewer than 10) which are publicly available. For example, if you're using PyPi.

In this case, you can use one of the pre-built Braket images, and then include a
`requirements.txt` file in your source directory at the job submission. The file
is automatically read, and `pip` will install the packages with the specified versions
as normal. If you're installing a large number of packages, the runtime of your jobs may be
substantially increased. Check the Python and, if applicable, CUDA version of the prebuilt
container you want to use to test if your software will work.

BYOC is necessary when you want to use a non-Python language (like C++ or Rust) for your job
script, or if you want to use a Python version not available through the Braket pre-built
containers. It is also a good choice if:

- You're using software with a license key, and you need to authenticate that key against
  a licensing server to run the software. With BYOC, you can embed the license key
  in your Docker image and include code to authenticate it.
- You are using software that is not publicly available. For example, the software is hosted
  on a private GitLab or GitHub repository that you need a particular SSH key to access.
- You need to install a large suite of software that is not packaged in the Braket provided
  containers. BYOC will allow you to eliminate long startup times for your hybrid jobs containers due
  to software installation.

BYOC also enables you to make your custom SDK or algorithm available to customers by building a
Docker container with your software and making it available to your users. You can do
this by setting appropriate permissions in Amazon ECR.

###### Note

You must comply with all applicable software licenses.
