# ------------------------------------------------------------------------
# Trash Classifier ML Project (Updated)
# Using picamera2 and tflite_runtime
# Yara M. ElSakka, 30.04.2025
# Create your TFLite from https://teachablemachine.withgoogle.com/
# --------------------------------------------------------------------------

from gpiozero import Button, LED, PWMLED
from picamera2 import Picamera2
from libcamera import Transform
from time import sleep
import numpy as np
import tflite_runtime.interpreter as tflite
import os
from datetime import datetime
from PIL import Image

# GPIO setup
button = Button(2)
yellow_led = LED(17)  # garbage
blue_led = LED(27)    # recycle
green_led = LED(22)   # compost
red_led = LED(23)     # hazardous waste facility
white_led = PWMLED(24)  # Status light and retake photo

# LED self-test at startup
def led_self_test():
    print("Running LED self-test...")
    for led in [yellow_led, blue_led, green_led, red_led]:
        led.on()
        sleep(0.5)
        led.off()
    white_led.on()
    sleep(0.5)
    white_led.off()
    print("LED self-test complete.\n")

led_self_test()  # Run only once at startup

# Initialize camera
picam2 = Picamera2()
camera_config = picam2.create_still_configuration(transform=Transform(vflip=1, hflip=1))
picam2.configure(camera_config)
picam2.start()

# Load TFLite model
model_path = "/home/yara/Projects/test/ModelsV3/model.tflite"  # Change if needed
interpreter = tflite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Take Photo and return image path
def take_photo():
    white_led.blink(0.1, 0.1)
    sleep(2)
    print("Pressed")
    white_led.on()
    sleep(1)

    image_path = "/home/yara/Projects/test/test_images/image.jpg"
    picam2.capture_file(image_path)
    white_led.off()
    sleep(1)
    return image_path

# Preprocess image for TFLite model
def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')
    input_shape = input_details[0]['shape']
    image = image.resize((input_shape[2], input_shape[1]))  # (width, height)
    input_data = np.expand_dims(image, axis=0)

    if input_details[0]['dtype'] == np.uint8:
        input_data = np.array(input_data, dtype=np.uint8)
    else:
        input_data = np.array(input_data, dtype=np.float32) / 255.0

    return input_data

# Predict using TFLite
def predict(image_path):
    input_data = preprocess_image(image_path)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])[0]
    predicted_index = np.argmax(output_data)
    confidence = output_data[predicted_index]

    labels_path = os.path.join(os.path.dirname(model_path), "labels.txt")
    with open(labels_path, "r") as f:
        labels = [line.strip() for line in f.readlines()]

    predicted_label = labels[predicted_index]
    print(f"Prediction: {predicted_label} ({confidence:.2f})")
    return predicted_label

def led_select(label):
    print(f"Detected label: '{label}'")

    # Extract label by removing index and stripping whitespace
    parts = label.strip().lower().split(' ', 1)
    clean_label = parts[1] if len(parts) > 1 else parts[0]

    # Turn off all LEDs first
    yellow_led.off()
    blue_led.off()
    green_led.off()
    red_led.off()
    white_led.off()

    if clean_label == "garbage":
        yellow_led.on()
        green_led.on()
    elif clean_label == "recycle":
        blue_led.on()
    elif clean_label == "compost":
        green_led.on()
    elif clean_label == "hazardous waste facility":
        red_led.on()
    elif clean_label == "not trash":
        white_led.on()

    sleep(5)
    # Turn off all LEDs after 5 seconds

# Main Loop
while True:
    if button.is_pressed:
        image_path = take_photo()
        label = predict(image_path)
        led_select(label)
    else:
    # Turn off all LEDs first
        yellow_led.off()
        blue_led.off()
        green_led.off()
        red_led.off()
    #Flash only the white LED
        white_led.pulse(2, 1)
    sleep(1)

# end of code
