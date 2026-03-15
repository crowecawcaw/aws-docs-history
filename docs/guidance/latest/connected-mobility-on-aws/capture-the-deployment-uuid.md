# Capture the deployment UUID

Capture and store the deployment UUIDs (Universally Unique ID) of the guidance. This is used to look for any resources not destroyed by CloudFormation after teardown completes.

```
make get-acdp-deployment-uuid
make get-cms-deployment-uuid
```

The output will be uuidv4 strings, capture and store both:

```
XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
```
