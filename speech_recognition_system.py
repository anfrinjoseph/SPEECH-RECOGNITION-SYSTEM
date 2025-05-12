import speech_recognition as sr
import RPi.GPIO as GPIO
import time

# GPIO setup for devices
LIGHT_PIN = 17  # GPIO pin for light control 
FAN_PIN = 27    # GPIO pin for fan control 

# Setup GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.setup(FAN_PIN, GPIO.OUT)

# Initialize devices to OFF state
GPIO.output(LIGHT_PIN, GPIO.LOW)
GPIO.output(FAN_PIN, GPIO.LOW)

def turn_on(pin, device_name):
    GPIO.output(pin, GPIO.HIGH)
    print(f"{device_name} turned ON")

def turn_off(pin, device_name):
    GPIO.output(pin, GPIO.LOW)
    print(f"{device_name} turned OFF")

def parse_command(command):
    command = command.lower()
    if "turn on light" in command:
        turn_on(LIGHT_PIN, "Light")
    elif "turn off light" in command:
        turn_off(LIGHT_PIN, "Light")
    elif "turn on fan" in command:
        turn_on(FAN_PIN, "Fan")
    elif "turn off fan" in command:
        turn_off(FAN_PIN, "Fan")
    elif "exit" in command or "quit" in command or "stop" in command:
        print("Exit command received. Quitting...")
        return "exit"
    else:
        print("Command not recognized. Please try again.")

def main():
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    mic = sr.Microphone()

    print("Speech Recognition Device Control System")
    print("Say commands like 'turn on light', 'turn off fan', or 'exit' to quit.")
    print("Listening...")

    with mic as source:
        # Adjust for ambient noise for 1 second
        recognizer.adjust_for_ambient_noise(source, duration=1)

    try:
        while True:
            with mic as source:
                print("Please speak your command:")
                audio = recognizer.listen(source, phrase_time_limit=5)

            try:
                # recognize speech using Google Speech Recognition
                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")
                result = parse_command(command)
                if result == "exit":
                    break

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nProgram interrupted by user")

    finally:
        GPIO.cleanup()
        print("GPIO cleaned up, program terminated.")

if __name__ == "__main__":
    main()

