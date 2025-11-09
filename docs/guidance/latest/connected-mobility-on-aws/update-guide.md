# Update the Guidance

## Version updates

To update to a newer version of the Guidance:

### Step 1: Backup current configuration

```
aws cloudformation describe-stacks --stack-name cms-<stage>-storage > backup-config.json
```

### Step 2: Pull latest changes

```
git pull origin main
cd deployment
```

### Step 3: Deploy updates

```
make deploy
```
