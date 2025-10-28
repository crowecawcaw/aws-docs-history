# Share conda

environments between instance types

You can share conda environments by saving them to an Amazon EFS directory outside of
your Amazon EBS volume. Another user can access the environment in the directory where
you saved it.

###### Important

There are limitations with sharing your environments. For example, we don't
recommend an environment meant to run on a GPU Amazon EC2 instance over an
environment running on a CPU instance.

Use the following commands as a template to specify the target directory where
you’re creating a custom environment. You’re creating a conda within a particular
path. You create it within the Amazon EFS directory. You can spin up a new instance and
do conda activate path and do it within the Amazon EFS.

```

# if you know your environment path for your conda environment
conda create --prefix /home/sagemaker-user/my-project/py39-test python=3.9

# activate the env with full path from prefix
conda activate home/sagemaker-user/my-project/py39-test

# parse env name information from your new environment
export CURRENT_ENV_NAME=$(conda info | grep "active environment" | awk -F' : ' '{print $2}' | awk -F'/' '{print $NF}')

# register your new environment as Jupyter Kernel for execution
python3 -m ipykernel install --user --name $CURRENT_ENV_NAME --display-name "user-env-prefix:($CURRENT_ENV_NAME)"

# deactivate your conda environment
conda deactivate

```
