# Associating Library with a Project

To use custom vocabulary, associate your library with a BDA project. This can be done in two ways:

## Option 1: Create Project with Library:

**AWS CLI Example:**

```
aws bedrock-data-automation create-data-automation-project \
    --project-name "audio-transcription-project" \
    --standard-output-configuration '{
        "audio": {
            "extraction": {
                "category": {
                    "state": "ENABLED",
                    "types": ["TRANSCRIPTION"]
                }
            }
        }
    }' \
    --data-automation-libraries '[{
        "libraryArn": "arn:aws:bedrock:us-east-1:123456789012:data-automation-library/healthcare-vocabulary"
    }]'
```

**AWS Console Example:**

1. Navigate to the Bedrock "Data Automation" page
2. Create a project
3. Navigate to the project detail page
4. Choose "Associated library" tab
5. Choose "Associate a library" button
6. Choose a library by selecting the radio button next to it and choose the "Associate library" button

![Create library dialog with fields for library name, description, KMS key, and tags.](images/bda/library-associate-from-project-console.png)

## Option 2: Update Existing Project with library:

```
aws bedrock-data-automation update-data-automation-project \
    --project-arn "arn:aws:bedrock:us-east-1:123456789012:data-automation-project/audio-transcription-project" \
    --data-automation-libraries '[{
        "libraryArn": "arn:aws:bedrock:us-east-1:123456789012:data-automation-library/healthcare-vocabulary"
    }]'
```

**AWS Console Example:**

1. Navigate to the "Library details" page for your library
2. Expand "Associated projects"
3. Choose "Associate projects"
4. Choose the projects to associate and choose "Associate project"

![Associated projects table showing no projects with Associate projects button available.](images/bda/library-associate-from-library-console.png)
