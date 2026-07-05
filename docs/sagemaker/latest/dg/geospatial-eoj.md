# Earth Observation Jobs

###### Note

Amazon SageMaker geospatial capabilities will no longer be open to new customers starting on 7/30/26. Offboard any
previously saved jobs to Amazon S3 by using the [ExportEarthObservationJob](../APIReference/API_geospatial_ExportEarthObservationJob.md "../APIReference/API_geospatial_ExportEarthObservationJob.md") and [ExportVectorEnrichmentJob](../APIReference/API_geospatial_ExportVectorEnrichmentJob.md "../APIReference/API_geospatial_ExportVectorEnrichmentJob.md") API operations.

Using an Earth Observation job (EOJ), you can acquire, transform, and visualize
geospatial data to make predictions. You can choose an operation based on your use case from a wide range of operations and models.
You get the flexibility of choosing your area of interest, selecting the data providers, and setting time-range based and cloud-cover-percentage-based filters.
After SageMaker AI creates an EOJ for you, you can visualize the inputs and outputs of the job using the visualization functionality.
An EOJ has various use cases that include comparing deforestation over time and diagnosing plant health.
You can create an EOJ by using a SageMaker notebook with a SageMaker geospatial image. You can also access the SageMaker geospatial UI as a part of Amazon SageMaker Studio Classic UI to view the list of all your jobs.
You can also use the UI to pause or stop an ongoing job. You can choose a job from the list of available EOJ to view the
**Job summary**, the **Job details** as well as visualize the **Job output**.

###### Topics

- [Create an Earth Observation Job Using a Amazon SageMaker Studio Classic Notebook with a SageMaker geospatial Image](geospatial-eoj-ntb.md "geospatial-eoj-ntb.md")
- [Types of Operations](geospatial-eoj-models.md "geospatial-eoj-models.md")
