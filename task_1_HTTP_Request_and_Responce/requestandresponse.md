# HTTP Request & Response Analysis

Expnalation: Here while analyzing request and response, from the html/js file that fetches the image from (fastly.picsum), We can see Several Panels that display some unique information.Such As. 

## Request Details

**Request URL:**

`https://fastly.picsum.photos/id/1075/600/400.jpg?hmac=9i5i5fFgBNfMg5fu-Nxz9gepLu-kv95P3CWLWDtFXkY`

- The browser requested a 600x400 JPEG image with ID `1075`.
- The `hmac` parameter ensures the URL is authorized and hasn’t been tampered with.

**Request Method:**

`GET`  
- The browser uses the GET method to retrieve the image.

**Status Code:**

`200 OK`  
- The request was successful and the image was returned correctly.

**Referrer Policy:**

`strict-origin-when-cross-origin`  
- This improves privacy by limiting what referrer information is shared across different origins.

---

## Response Headers (from Server)

- `Content-Type`: The server returned a JPEG image.
- `Content-Length`: The image size is 20,257 bytes.
- `Cache-Control`: The image can be cached for 30 days.
- `Content-Disposition`: The browser is instructed to display the image inline.
- `Age`: The image has been cached for over 300,000 seconds.
- `X-Cache`: The image was served from a cache (faster).
- `Server`: The request was handled by an nginx server.

---

## Request Headers (from Browser)

- `Accept`: The browser accepts formats like image/webp.
- `Accept-Encoding`: The browser supports compression like gzip and br.
- `Accept-Language`: The browser’s preferred language is English (en-US).
- `User-Agent`: Identifies the browser and device (e.g., Chrome on Android).
- `Sec-Fetch-*`: These provide security context for the request.

---

## Summary

When the user clicks the button, the browser sends a `GET` request to the Picsum API to fetch a random image. The request is successful (`200 OK`), and a JPEG image is returned. The server allows the image to be cached, and in this case, it was served from the cache. The headers show metadata about the request, the image format, and browser capabilities.

