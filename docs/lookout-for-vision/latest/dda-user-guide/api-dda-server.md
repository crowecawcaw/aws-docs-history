Defect Detection App is in preview release and is subject to change.

# Defect Detection App API

The Defect Detection App API provides HTTP requests that you use to configure and use
workflows. You can also query the models on a station and list of images saved to the
station. The API is available from the local station once it is provisioned. It is
accessible from port 5000. For example, the following request returns the list of available cameras:

```
curl -X GET `0.0.0.0`:5000/cameras
```

The Defect Detection App API reference is also available in OpenAPI format. Open a browser and
navigate to `x.x.x.x:5000/docs`, where x.x.x.x is the IP address of the station.

###### Note

Currently, calling the Defect Detection App API doesn't require authentication.

###### Topics

- [Actions](api-actions.md "api-actions.md")
- [Data types](api-data-types.md "api-data-types.md")
