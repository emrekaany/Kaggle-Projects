# Data and model provenance

No source dataset, competition file, source video, API credential, trained model, or model weight is intentionally distributed by this repository.

## Recorded Kaggle inputs

The following identifiers come from the committed notebook metadata and make the dependency boundary auditable. They are identifiers, not a grant of redistribution rights.

| Notebook | Recorded Kaggle source |
|---|---|
| `data_generating_with_gemini_for_sentiment_model.ipynb` | Dataset ID `7255304`, version/source ID `11574013` |
| `financial-news-sentiment-model.ipynb` | Dataset ID `7255304`, version/source ID `11572426` |
| `insurance-customer-review-analysis-baseline-work.ipynb` | Dataset ID `7274774`, version/source ID `11609426` |
| `preprocessing-object-speed-by-yolov8-deepsort.ipynb` | Competition ID `92399` |
| `try-usd-fx-rates-and-financials-eda.ipynb` | Dataset ID `7084827`, version/source ID `11479550` |
| `creating_insurance_customer_review_data_with_generative_ai_GeminiAPI.ipynb` | No attached Kaggle dataset is recorded; output is generated through a runtime API call. |

Before execution, open the linked Kaggle notebook or source page, confirm that it is still available, read its license/competition rules, and attach it through your own Kaggle account. Do not place restricted data in Git history.

## External services and models

- Gemini examples use the runner’s own `GEMINI_API_KEY_INSURANCE_REVIEW`. Generated text remains subject to the provider’s current terms and must be reviewed before downstream use.
- YOLOv8, DeepSORT, PyTorch, and any downloaded weights remain subject to their respective project and weight licenses.
- Financial or macroeconomic results are educational analysis, not financial advice.

## Publication checklist

Before adding a new notebook or data artifact:

1. Record the canonical source URL or Kaggle identifier.
2. Confirm redistribution and competition rules.
3. Remove credentials, personal data, machine-specific paths, and generated model artifacts.
4. State whether results are executed, reproducible, or exploratory.
5. Add only aggregate, non-sensitive evidence needed to explain the result.
