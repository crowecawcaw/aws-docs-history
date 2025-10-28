# Delete unused resources

To avoid incurring additional costs running JupyterLab, we recommend deleting unused
resources in the following order:

1. JupyterLab applications
2. Spaces
3. User profiles
4. domains
   Use the following AWS Command Line Interface (AWS CLI) commands to delete resources within a
   domain:

Delete a JupyterLab application

```
aws --region `AWS Region` sagemaker delete-app --domain-id `example-domain-id` --app-name default --app-type JupyterLab --space-name `example-space-name`
```

Delete a space

###### Important

If you delete a space, you delete the Amazon EBS volume associated with it.
We recommend backing up any valuable data before you delete your
space.

```
aws --region `AWS Region` sagemaker delete-space --domain-id `example-domain-id`  --space-name `example-space-name`
```

Delete a user profile

```
aws --region `AWS Region` sagemaker delete-user-profile --domain-id `example-domain-id` --user-profile `example-user-profile`
```
