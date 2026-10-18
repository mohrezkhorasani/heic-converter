# HEIC to JPG Converter

A lightweight batch converter to convert Apple HEIC photos to standard JPG format on Windows.

When transferring photos from an iPhone to a PC, Windows often struggles to open or preview `.heic` files natively without third-party codecs. This utility scans an input folder, auto-rotates the images according to their EXIF orientation metadata (so portrait shots don't get rotated sideways), and saves them as high-quality JPEGs.

---

## راهنمای فارسی

یک اسکریپت و برنامه ساده برای تبدیل دسته‌ای عکس‌های HEIC (فرمت پیش‌فرض آیفون) به JPG در ویندوز.

موقع انتقال عکس‌ها از گوشی آیفون به ویندوز، فرمت HEIC معمولاً در فتوشاپ، نرم‌افزارهای نمایش عکس و سایت‌های مختلف باز نمی‌شود یا نیاز به نصب اکستنشن‌های پولی مایکروسافت دارد. این ابزار بدون دستکاری کیفیت اصلی، عکس‌ها را به JPG تبدیل کرده و جهت تصویر (عمودی/افقی) را هم طبق متادیتای دوربین به درستی اصلاح می‌کند.

---

> You can download the pre-compiled standalone executable directly from the [Releases](https://github.com/mohrezkhorasani/heic-converter/releases) page without needing Python installed.

---

## نحوه استفاده (Usage)

### ۱. استفاده از فایل آماده (بدون نیاز به پایتون)
- فایل `HEIC_Converter.exe` را از بخش [Releases](https://github.com/mohrezkhorasani/heic-converter/releases) دانلود کنید.
- برنامه را اجرا کنید؛ در اولین اجرا به صورت خودکار دو پوشه به نام‌های **ورودی** و **خروجی** در کنار فایل ساخته می‌شود.
- عکس‌های `.heic` را در پوشه **ورودی** کپی کنید و برنامه را اجرا کنید.
- فایل‌های تبدیل شده با فرمت JPG در پوشه **خروجی** ذخیره می‌شوند.

### ۲. اجرا از طریق سورس پایتون

اگر می‌خواهید اسکریپت را مستقیماً با پایتون اجرا کنید:

```bash
# نصب پیش‌نیازها
pip install -r requirements.txt

# اجرای برنامه
python heic_converter.py
```

---

## ساخت فایل exe از سورس (Build Executable)

اگر تغییراتی در کد دادید و خواستید خروجی تک‌فایلی exe بگیرید:

```bash
pip install pyinstaller
pyinstaller --onefile heic_converter.py
```

یا با استفاده از فایل تنظیمات موجود:

```bash
pyinstaller HEIC_Converter.spec
```

---

## وابستگی‌ها (Dependencies)

- Python 3.8+
- [Pillow](https://python-pillow.org/)
- [pillow-heif](https://github.com/bigcat88/pillow_heif)

## لایسنس (License)

[MIT](LICENSE)
