# python-server-side-assignment-AayushSigdel
# HTTP Request & Response Analysis

## Screenshot Context
This analysis is based on inspecting a network request triggered by clicking a "Get Image" button on a webpage. The image was fetched using the [Picsum Photos](https://picsum.photos) API.

---

## 📌 Request Details

### ✅ Request URL
https://fastly.picsum.photos/id/1075/600/400.jpg?hmac=9i5i5fFgBNfMg5fu-Nxz9gepLu-kv95P3CWLWDtFXkY

- The browser requested a **600x400 JPEG image** with ID `1075`.
- The `hmac` parameter ensures the URL is authorized and untampered.

### ✅ Request Method
GET

- The browser uses the `GET` method to retrieve the image.

### ✅ Status Code
200 OK

- This means the request was successful and the image was returned correctly.

### ✅ Referrer Policy
strict-origin-when-cross-origin

- Limits the amount of referrer information sent in cross-origin requests, improving privacy.

---

## 📥 Response Headers (from Server)

| Header                | Description                                                   |
|-----------------------|---------------------------------------------------------------|
| `Content-Type`        | `image/jpeg` – The returned content is a JPEG image.          |
| `Content-Length`      | `20257` – The image file size in bytes.                        |
| `Cache-Control`       | Allows caching the image for efficiency (`max-age=2592000`).  |
| `Content-Disposition` | Instructs the browser to display the image inline with a filename. |
| `Age`                 | Time in seconds the image has been cached (`302509`).         |
| `X-Cache`             | `HIT` – The image was served from a cache.                     |
| `Server`              | `nginx` – The server software handling the request.            |

---

## 📤 Request Headers (from Browser)

| Header                | Description                                                |
|-----------------------|------------------------------------------------------------|
| `Accept`              | Specifies the file types the browser can handle (e.g., image/webp). |
| `Accept-Encoding`     | Lists compression formats supported by the browser (`gzip`, `br`). |
| `Accept-Language`     | Preferred language set in the browser (`en-US`).            |
| `User-Agent`          | Identifies the browser and platform (e.g., Chrome on Android). |
| `Sec-Fetch-*`         | Security and context-related headers for the image request. |

---

## 📝 Summary

When the user clicks the button, the browser sends a `GET` request to the Picsum API to fetch a random image. The request is successfully processed (`200 OK`), and the image is returned as a JPEG. The server allows the image to be cached, and in this case, it was served from a cache (faster). Request and response headers include useful metadata about browser capabilities, image format, caching policy, and network context.

---

If you want, I can save this as a `README.md` file for you to download. Just let me know!

