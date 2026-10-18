import os
import sys
from pathlib import Path
from PIL import Image, ImageOps
import pillow_heif

# فعال‌سازی پشتیبانی از فرمت HEIC در Pillow
pillow_heif.register_heif_opener()

def get_base_path():
    """
    مسیر پایه را تعیین می‌کند.
    اگر برنامه به exe تبدیل شده باشد، مسیر پوشه‌ی exe را برمی‌گرداند.
    در غیر این صورت، مسیر پوشه‌ی اسکریپت را برمی‌گرداند.
    """
    if getattr(sys, 'frozen', False):
        # اگر برنامه frozen شده باشد (تبدیل به exe شده باشد)
        return Path(sys.executable).parent
    else:
        # اگر به صورت اسکریپت پایتون اجرا شود
        return Path(__file__).parent

def main():
    base_path = get_base_path()
    input_dir = base_path / "ورودی"
    output_dir = base_path / "خروجی"

    # ایجاد پوشه‌ها در صورت عدم وجود
    input_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)

    # پیدا کردن تمام فایل‌های HEIC (بدون حساسیت به حروف بزرگ و کوچک)
    heic_files = []
    for ext in ['*.heic', '*.HEIC', '*.Heic']:
        heic_files.extend(input_dir.glob(ext))

    if not heic_files:
        print(f"هیچ فایل HEIC در پوشه '{input_dir}' پیدا نشد.")
        return

    print(f"در حال تبدیل {len(heic_files)} فایل...")

    for heic_path in heic_files:
        # نام فایل خروجی با پسوند .jpg (نام اصلی حفظ می‌شود)
        output_path = output_dir / (heic_path.stem + ".jpg")

        try:
            # باز کردن تصویر HEIC
            with Image.open(heic_path) as img:
                # اصلاح جهت تصویر بر اساس اطلاعات EXIF (برای عکس‌های گوشی)
                img = ImageOps.exif_transpose(img)
                
                # تبدیل به حالت RGB (برای ذخیره به صورت JPEG ضروری است)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # ذخیره به صورت JPEG با کیفیت بالا
                # اگر فایل از قبل وجود داشته باشد، به صورت خودکار جایگزین می‌شود
                img.save(output_path, "JPEG", quality=95)
                
            print(f"تبدیل شد: {heic_path.name} -> {output_path.name}")

        except Exception as e:
            print(f"خطا در تبدیل {heic_path.name}: {e}")

    print("عملیات تبدیل به پایان رسید.")

if __name__ == "__main__":
    main()
    # جلوگیری از بسته شدن پنجره کنسول در ویندوز (اختیاری)
    input("برای خروج کلید Enter را فشار دهید...")