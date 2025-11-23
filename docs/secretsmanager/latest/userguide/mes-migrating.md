# Migrating existing secrets

You have an option to migrate your existing partner secrets to managed external secrets.
This can be done with an [UpdateSecret](../apireference/API_UpdateSecret.md "../apireference/API_UpdateSecret.md") call. You must update the secret value and metadata as mentioned
in the guide. If you already have custom rotation logic set up for these secrets, you must first cancel
the rotation using a [CancelRotateSecret](../apireference/API_CancelRotateSecret.md "../apireference/API_CancelRotateSecret.md") call.
