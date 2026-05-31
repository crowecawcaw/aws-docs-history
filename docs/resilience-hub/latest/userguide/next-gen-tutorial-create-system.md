# Create a system

**Console:**

1. Open the the next generation of Resilience Hub console.
2. Choose **Systems** > **Create
   system**.
3. Enter a name (for example, `My Application`) and an optional
   description.
4. Choose **Create**.
   **AWS CLI:**

```
aws resiliencehubv2 create-system \
  --name "my-application" \
  --description "My first application in Resilience Hub"
```
