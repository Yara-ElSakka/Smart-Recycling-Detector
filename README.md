# 🌟 Yara's Smart Recycling Detector! 🤖📊

Welcome to **Yara ElSakka's awesome AI recycling project**! 🚀 This fun little program helps us figure out where trash should go — using a camera 📷, some blinking lights 💡, and smart brainy AI 🧠 on a Raspberry Pi! 🤖

---

## 🚀 What Does It Do?

1. 💪 Press a button to start!
2. 📸 It takes a picture of the item.
3. 🧠 AI decides what kind of waste it is.
4. 💡 Lights show you the right bin to use!

---

## 🚀 What is the Project Anwayways ? 

![IMG_5545(1)](https://github.com/user-attachments/assets/4ae9fbd9-6b20-47ba-ba7f-dbf15ef2dda3)

---

## 🔧 What You Need

- Raspberry Pi 4 🧸
- Raspberry Pi Camera (using Picamera2) 📷
- GPIO connected LEDs:
  - 🟡 Yellow (Garbage)
  - 🔵 Blue (Recycle)
  - 💚 Green (Compost)
  - 🔴 Red (Hazardous)
  - ⚪ White (Not trash / status)
- Button 🎁
- Pre-trained `.tflite` model (TensorFlow Lite) 🎓
- Python libraries:
  - `picamera2`
  - `gpiozero`
  - `tflite_runtime`
  - `numpy`

---

## 💡 How It Works (Code Summary)

- At start: 🔄 All LEDs flash to show they work.
- When the button is pressed:
  - ⏳ Status light turns on.
  - 📷 Camera takes a picture.
  - 🧠 AI model analyzes the photo.
  - 💡 The correct LED lights up to tell you what kind of waste it is!

---

## 🔍 Example Labels

- **"recycle"** ➡️ Blue light
- **"garbage"** ➡️ Yellow light
- **"compost"** ➡️ Green light
- **"hazardous waste facility"** ➡️ Red light
- **"not trash!"** ➡️ White light

---

## 🚀 Run the Code

```bash
source venv/bin/activate
python main.py
```

Make sure your `.tflite` model is in the correct folder and the path is updated in the code! 📑

---

## 💼 Project By

**Yara ElSakka** ✨  
Grade 5 Student 🏫  
The International School of Choueifat – Ajman 🇦🇪

---

## 🌿 Let’s Be Recycling Heroes!

Help the Earth one smart step at a time! 🌍♻️🌟

