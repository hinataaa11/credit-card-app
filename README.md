# 信用卡帳單管理 PWA（GitHub Pages 版）

這個專案是你目前 Google Apps Script 信用卡管理網站的「APP 外殼」。

- GitHub Pages：負責 PWA / APP 圖示 / 加入手機主畫面
- Google Apps Script：繼續負責原本的畫面、Google Sheet 資料、新增與還款功能
- GitHub **不會存放你的信用卡帳單資料**

## 1. 上傳到 GitHub

1. GitHub 建立一個新 repository，例如 `credit-card-app`
2. 把這個 ZIP 解壓縮後的 **全部檔案**上傳到 repository 根目錄
3. 確認預設 branch 是 `main`
4. 到 `Settings → Pages`
5. `Build and deployment → Source` 選 **GitHub Actions**
6. 到 `Actions` 等 `Deploy PWA to GitHub Pages` 完成
7. 回到 `Settings → Pages` 就會看到 APP 網址

## 2. APP 圖示

部署流程會自動從這個 Google Drive 檔案抓圖：

`https://drive.google.com/file/d/1dY17XUanKaZeuvKA5sj9UqNayqbuqhoe/view?usp=sharing`

請確認 Drive 分享權限為：**知道連結的任何人 → 檢視者**。

部署時會自動產生：

- `assets/icon-192.png`
- `assets/icon-512.png`
- `assets/icon-maskable-512.png`

如果 Drive 暫時抓不到圖片，APP 仍會使用專案內附的備用 icon，不會部署失敗。

## 3. 第一次開啟 APP

第一次打開 GitHub Pages 網址時，畫面會要求你貼上目前的 Apps Script 網頁應用程式網址：

`https://script.google.com/macros/s/XXXXXXXXXXXX/exec`

貼上後按「開啟 APP」。網址只儲存在該手機/電腦的 localStorage，不會寫回 GitHub。

你目前的 Apps Script `Code.gs` 已使用 `XFrameOptionsMode.ALLOWALL`，所以可以被這個 APP 外殼載入。

要更換 Apps Script 網址：

- 點 APP 右下角 `⚙︎`
- 或在 GitHub Pages 網址後加 `?setup=1`

## 4. 手機安裝

### iPhone / iPad
Safari 開啟 GitHub Pages 網址 → 分享 → **加入主畫面**。

### Android
Chrome 開啟 GitHub Pages 網址 → 選單 → **安裝應用程式 / 加到主畫面**。

## 注意

- APP 外殼可以快取，但 Google Sheet 資料與 Apps Script 功能仍需要網路。
- 不要把 Google Sheet ID、私人帳務資料或帳號密碼寫進 GitHub repository。
- Repository 就算公開也只會看到 APP 外殼；真正帳務資料仍在你的 Google Sheet 裡。
