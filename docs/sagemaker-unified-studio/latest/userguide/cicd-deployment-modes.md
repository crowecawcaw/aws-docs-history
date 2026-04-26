# Deployment modes

## Direct deployment

Deploy directly from a local source directory:

```
aws-smus-cicd-cli deploy --manifest manifest.yaml --targets prod
```

## Bundle-based deployment

Package your application from the source target into an immutable artifact, then promote it to the destination:

```
# Create the bundle (reads from source target)
aws-smus-cicd-cli bundle --manifest manifest.yaml

# Deploy the bundle to production (deploys to destination target)
aws-smus-cicd-cli deploy --manifest app.tar.gz --targets prod
```
