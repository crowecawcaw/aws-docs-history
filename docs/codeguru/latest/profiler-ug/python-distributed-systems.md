# Profiling Distributed systems

Amazon CodeGuru Profiler offers limited support when implemented on distributed systems like Spark on
EMR or Glue jobs running across clusters. In such cases, Profiler is able to profile the
application running on the manager node; however, it may not be able to profile the part of
the application running on the worker nodes. Please consult with your local technical
representative for further clarifications.
