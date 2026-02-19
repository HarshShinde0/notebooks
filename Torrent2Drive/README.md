# Torrent2Drive

**Download magnet links in Google Colab and auto-transfer to Google Drive**

Torrent2Drive is a lightweight Google Colab-based solution that allows you to download content via magnet links using `aria2c`, and automatically transfer the files to your Google Drive for easy access and long-term storage.

---

## 🚀 Features

- ✅ Supports magnet links  
- ✅ Runs entirely in Google Colab (no local setup required)  
- ✅ Uses `aria2c` for fast and efficient downloading  
- ✅ Automatically uploads to your Google Drive  
- ✅ Free to use with your Google account  

---

## 📓 How to Use

### 1. Open the Colab Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HarshShinde0/Torrent2Drive/blob/main/Torrent2Drive.ipynb)
> _Paste the notebook code here or link to your own repo._

---

### 2. Install and Set Up

The notebook will:

- Install `aria2`
- Ask for a magnet URI
- Start the download to `/content/downloads`
- Mount your Google Drive
- Transfer files to `MyDrive/TorrentDownloads`

---

### 3. Example Magnet Link (✅ Open-Source Only!)

```python
magnet_uri = "https://cdimage.kali.org/kali-2025.1c/kali-linux-2025.1c-installer-amd64.iso.torrent"  # OR magnet:?xt=urn:btih:..
```

> ⚠️ Only use legal or open-source torrents (e.g., Linux ISOs, Creative Commons media, public datasets).

---

## 🛠️ Dependencies

- Google Colab  
- `aria2c`  
- Python:  
  - `shutil`  
  - `os`  
  - `google.colab.drive`

---

## 📁 Output Location

Your downloaded files will be available in:

```
/content/drive/MyDrive/TorrentDownloads/
```

---

## ⚖️ Legal Disclaimer

This tool is intended for **educational and legal use only**.  
Downloading or sharing copyrighted material without proper authorization is illegal and against Google Colab's terms of service.

---

## 🤝 Contributing

Pull requests and improvements are welcome! Feel free to fork and extend the functionality — such as:

- `.torrent` file support  
- Status dashboards  
- Web UI integration (e.g., with qBittorrent-nox)

---

## 💬 Contact

Open an issue or discussion on GitHub if you have questions or suggestions.
