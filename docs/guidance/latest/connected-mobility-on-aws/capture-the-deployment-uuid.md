

# Capture the deployment UUID
<a name="capture-the-deployment-uuid"></a>

Capture and store the deployment UUIDs (Universally Unique ID) of the guidance. This is used to look for any resources not destroyed by CloudFormation after teardown completes.

```
make get-deployment-uuid
make get-cms-deployment-uuid
```

The output will be uuidv4 strings, capture and store both:

```
XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
```