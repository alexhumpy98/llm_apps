# Build and deploy

Streamlit App Link:
<br>

https://streamlit-talk-to-crm-full-data-app-v4k6nqvaka-ew.a.run.app

<br>

Command to build the application.
```
gcloud builds submit --tag gcr.io/annular-form-389809/streamlit-talk-to-crm-full-data-app  --project=annular-form-389809
```

Command to deploy the application
```
gcloud run deploy --image gcr.io/annular-form-389809/streamlit-talk-to-crm-full-data-app --platform managed  --project=annular-form-389809 --allow-unauthenticated
```


<br>
<br>

# GCP Resources Used

<br>

**GCP Project:** 
- annular-form-389809

**BigQuery:** 
- annular-form-389809.merged_data.crm_ga4

**CloudRun**
- streamlit-talk-to-crm-full-data-app
