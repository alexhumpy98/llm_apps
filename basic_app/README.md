# Build and deploy

Command to build the application. PLease remeber to change the project name and application name
```
gcloud builds submit --tag gcr.io/annular-form-389809/streamlit-basic-app  --project=annular-form-389809
```

Command to deploy the application
```
gcloud run deploy --image gcr.io/annular-form-389809/streamlit-basic-app --platform managed  --project=annular-form-389809 --allow-unauthenticated
```

# Service Link

https://streamlit-basic-app-v4k6nqvaka-ew.a.run.app