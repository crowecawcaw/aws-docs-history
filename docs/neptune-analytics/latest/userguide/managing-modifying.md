# Modifying a Neptune Analytics graph

You can change the settings of a Neptune Analytics graph to accomplish tasks such as changing public connectivity or its
provisioned-memory.

It is recommended that you test any changes using a test graph before modifying any production graphs, so that
you are able to fully understand the impact of each change.

**Memory scaling**

Neptune Analytics is a memory-optimized graph database engine for analytics, which stores data in-memory to enable optimal
performance for algorithmic and analytical workflows. A Neptune Analytics graph can have the instance size upscaled or
downscale the database to a smaller or larger memory size by updating the graph to higher m-NCU. The minimum
size of the mNCU chosen must be capable of storing all the data in the graph, smaller mNCU values than that
required by the graph will result in `ValidationException` errors.
