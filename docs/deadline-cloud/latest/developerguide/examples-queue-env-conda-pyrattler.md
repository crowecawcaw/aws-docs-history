# py-rattler conda queue environment for Deadline Cloud

The
[conda_queue_env_pyrattler.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_pyrattler.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_pyrattler.yaml")
queue environment provides the same functionality as the inline conda
queue environments but uses the
[py-rattler](https://conda.github.io/rattler/py-rattler/ "https://conda.github.io/rattler/py-rattler/")
library. Rattler is written in Rust and provides common functionality
used in the conda ecosystem.

Testing has shown that this queue environment generally runs faster
than the inline conda queue environments on the same instance types. The
environments it creates are nearly the same. Two differences:

- py-rattler doesn't include `pip` alongside
  `python` by default, so you must add
  `pip` explicitly when you need it.
- py-rattler raises an error for a subset of syntax that conda
  accepts, such as `colmap=*=gpu*`.
  The error messages py-rattler produces when failing to solve for a
  virtual environment don't include as much detail as conda's. If you need
  more detailed solver errors during development, switch to one of the
  inline conda queue environments.
