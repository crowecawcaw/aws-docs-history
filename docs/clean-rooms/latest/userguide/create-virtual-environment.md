# Creating a virtual environment

(optional)

If you have any additional libraries required by your user script, you have the option
to create a virtual environment to store those libraries. If you don't need additional
libraries, you can skip this step.

When working with libraries that have native extensions, keep in mind that PySpark in
AWS Clean Rooms operates on Linux with ARM64 architecture.

The following procedure demonstrates how to create a virtual environment using a basic
CLI command.

###### To create a virtual environment

1. Open a terminal or command prompt.
2. Add the following content:

```
# create and activate a python virtual environment
python3 -m venv pyspark_venvsource
source pyspark_venvsource/bin/activate

# install the python packages
pip3 install pandas # add packages here

# package the virtual environment into an archive
pip3 install venv-pack
venv-pack -f -o pyspark_venv.tar.gz


# optionally, remove the virtual environment directory
deactivate
rm -fr pyspark_venvsource
```

3. You are now ready to store this virtual environment in S3. For more information, see
   [Storing a user script and virtual environment in
   S3](store-artifacts-in-s3.md "store-artifacts-in-s3.md").
   For more information about working with Docker and Amazon ECR, see the [Amazon ECRUser Guide](../../../AmazonECR/latest/userguide.md "../../../AmazonECR/latest/userguide.md").
