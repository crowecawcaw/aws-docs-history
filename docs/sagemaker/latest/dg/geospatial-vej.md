# Vector Enrichment Jobs

A Vector Enrichment Job (VEJ) performs operations on your vector data.
Currently, you can use a VEJ to do reverse geocoding or map matching.

###### Reverse Geocoding

With a reverse geocoding VEJ, you can convert geographic coordinates (latitude, longitude) to human-readable addresses powered by Amazon Location Service.
When you upload a CSV file containing the longitude and latitude coordinates, a it returns the address number,
country, label, municipality, neighborhood, postal code and region of that location. The output file consists of your input data
along with columns containing these the values appended at the end. These jobs are optimized to
accept tens of thousands of GPS traces.

###### Map Matching

Map matching allows you to snap GPS coordinates to road segments. The input should
be a CSV file containing the trace ID (route), longitude, latitude and the timestamp attributes.
There can be multiple GPS co-ordinates per route. The input can contain multiple routes too.
The output is a GeoJSON file that contains links of the predicted route. It also has the snap points provided
in the input. These jobs are optimized to accept tens of thousands of drives in one request.
Map matching is supported by [OpenStreetMap](https://www.openstreetmap.org/ "https://www.openstreetmap.org/").
Map matching fails if the names in the input source field don't match the ones in `MapMatchingConfig`.
The error message you receive contains the the field names present in the input file and the expected field name
that is not found in `MapMatchingConfig`.

The input CSV file for a VEJ must contain the following:

- A header row
- Latitude and longitude in separate columns
- The ID and Timestamp columns can be in numeric or string format. All other column data must be in numeric format only
- No miss matching quotes
  For the timestamp column, SageMaker geospatial capabilities supports epoch time in seconds and milliseconds (long integer). The string formats supported are as follows:

- "dd.MM.yyyy HH:mm:ss z"
- "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'"
- "yyyy-MM-dd'T'HH:mm:ss"
- "yyyy-MM-dd hh:mm:ss a"
- "yyyy-MM-dd HH:mm:ss"
- "yyyyMMddHHmmss"
  While you need to use an Amazon SageMaker Studio Classic notebook to execute a VEJ, you can view
  all the jobs you create using the UI. To use the visualization in the notebook,
  you first need to export your output to your S3 bucket. The VEJ actions you can perform are as follows.

- [StartVectorEnrichmentJob](../APIReference/API_geospatial_StartVectorEnrichmentJob.md "../APIReference/API_geospatial_StartVectorEnrichmentJob.md")
- [GetVectorEnrichmentJob](../APIReference/API_geospatial_GetVectorEnrichmentJob.md "../APIReference/API_geospatial_GetVectorEnrichmentJob.md")
- [ListVectorEnrichmentJobs](../APIReference/API_geospatial_ListVectorEnrichmentJobs.md "../APIReference/API_geospatial_ListVectorEnrichmentJobs.md")
- [StopVectorEnrichmentJob](../APIReference/API_geospatial_StopVectorEnrichmentJob.md "../APIReference/API_geospatial_StopVectorEnrichmentJob.md")
- [DeleteVectorEnrichmentJob](../APIReference/API_geospatial_DeleteVectorEnrichmentJob.md "../APIReference/API_geospatial_DeleteVectorEnrichmentJob.md")
