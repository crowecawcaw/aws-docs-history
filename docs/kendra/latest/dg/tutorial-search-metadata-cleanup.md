# Step 6: Cleaning up

## Cleaning up your files

To stop incurring charges in your AWS account after you complete this tutorial, you
can take the following steps:

1. **Delete your Amazon S3 bucket**

For information about deleting a bucket, see [Deleting a bucket](../../../AmazonS3/latest/userguide/delete-bucket.md "../../../AmazonS3/latest/userguide/delete-bucket.md"). 2. **Delete your Amazon Kendra index**

For information about deleting an Amazon Kendra index, see [Deleting an
index](delete-index.md "delete-index.md"). 3. **Delete `converter.py`**

    * **For Console:** Go to [AWS CloudShell](https://console.aws.amazon.com/cloudshell/ "https://console.aws.amazon.com/cloudshell/"), and make sure
     the region is set to your AWS region. After the bash shell has loaded, type the
     following command into the environment and press enter.



    ```
    rm converter.py
    ```
    * **For AWS CLI:** Run the following command on a
     terminal window.



    Linux

    ```
    rm `file/`converter.py
    ```

    Where:




    	+ `file/` is the filepath to
    	 `converter.py` on your local device.

    macOS

    ```
    rm `file/`converter.py
    ```

    Where:




    	+ `file/` is the filepath to
    	 `converter.py` on your local device.

    Windows

    ```
    rm `file/`converter.py
    ```

    Where:




    	+ `file/` is the filepath to
    	 `converter.py` on your local device.

## Learn more

To learn more about integrating Amazon Kendra into your workflow, you can check out the
following blogposts:

- [Content
  metadata tagging for enhanced search](https://comprehend-immersionday.workshop.aws/lab8.html "https://comprehend-immersionday.workshop.aws/lab8.html")
- [Build an intelligent search solution with automated content
  enrichment](https://aws.amazon.com/blogs/machine-learning/build-an-intelligent-search-solution-with-automated-content-enrichment/ "https://aws.amazon.com/blogs/machine-learning/build-an-intelligent-search-solution-with-automated-content-enrichment/")

To learn more about Amazon Comprehend, you can look at the [_Amazon Comprehend
Developer Guide_](../../../comprehend/index.md "../../../comprehend/index.md").
