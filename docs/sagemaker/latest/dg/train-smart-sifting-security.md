# Security in SageMaker smart sifting

Because the SageMaker smart sifting library runs processes of removing less valuable training
samples, it requires full access to training datasets as they are produced by the data
loader. This access is not different than the access already provided to PyTorch in
normal training scenario.

SageMaker smart sifting has built-in logging with security implications. By default, SageMaker smart sifting
logs are only application-level logs containing metrics, latencies, and user errors or
warnings. Users can, however, choose to enable verbose logs, which log full batch data
to show which samples were removed from a given batch. These logs are emitted using
Python loggers and are not uploaded or stored anywhere by the library. In the case of
automatic log uploading to CloudWatch or similar services, please note that using
verbose logs may result in sensitive training data being uploaded off of the training
instance.

Beyond the aforementioned logging, SageMaker smart sifting does not have any network functionality
nor does it interact with the local file system. User data is stored as in-memory
objects for the entirety of the time it is used by the library.
