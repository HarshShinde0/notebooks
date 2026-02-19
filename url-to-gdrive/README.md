# url-to-gdrive

A simple Python script to download a file from a URL with progress display and upload it directly to Google Drive.

---

## Features

- Download any file from a given URL with a progress bar
- Upload the downloaded file to Google Drive
- Makes the uploaded file publicly accessible with a shareable link
- Works seamlessly in Google Colab or local Python environments

---

## Requirements

- Python 3.x
- `requests` library
- `tqdm` library
- Google Colab (optional but recommended for easy Google Drive authentication)
- Google API Python client libraries (`google-auth`, `google-api-python-client`)

Install dependencies via:

```bash
pip install requests tqdm google-auth google-api-python-client google-colab
```

---

## Usage

### 1. Download the file

Run the script, input the file URL when prompted:

```bash
python download_and_upload.py
```

### 2. Upload to Google Drive

The script will ask for the downloaded filename and upload it to your Google Drive.

---

## Google Drive Authentication

The script uses Google OAuth credentials to authenticate.  
- On Google Colab, authentication happens automatically via `google.colab.auth`.  
- Locally, you need to set up OAuth credentials or use a service account.

---

## Example

```plaintext
Enter the download URL: https://example.com/file.zip
Downloading file.zip...
100%|██████████████████████████████████| 50.0M/50.0M [00:10<00:00, 4.7MB/s]
✅ Download complete: file.zip

Enter the filename to upload to Google Drive: file.zip
Uploading file.zip...
✅ Upload complete!
🔗 File link: https://drive.google.com/file/d/FILE_ID/view
```

---

## License

MIT License © 2025 Your Name

---

## Contributions

Feel free to open issues or submit pull requests!
