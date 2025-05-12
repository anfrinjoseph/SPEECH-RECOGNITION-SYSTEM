# SPEECH RECOGNITION SYSTEM

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: ANFRIN JOSEPH

*INTERN I D*: CT12WVKV

*DOMAIN*: EMBEDDED SYSTEMS

*DURATION*: 12 WEEKS

*MENTOR*: NEELA SANTOSH

This project implements a basic Speech Recognition System for command-based control of devices using the Raspberry Pi. It enables hands-free control of hardware components connected via GPIO pins, like lights and fans, using natural voice commands.

The system architecture consists of three main components: audio input via a microphone, speech processing, and device control. The microphone captures spoken commands, which are processed using the Google Web Speech API through the Python SpeechRecognition library. This cloud-based API efficiently converts speech to text, allowing quick and accurate command recognition.

The software listens continuously and supports several basic voice commands, including "turn on light," "turn off fan," and "exit" to terminate the program. When a valid command is recognized, the program activates or deactivates the corresponding GPIO pins on the Raspberry Pi to power the connected devices. If the speech is unclear or the command unrecognized, the system provides console feedback, prompting the user to repeat.

Key features include ambient noise adjustment to improve speech recognition accuracy in diverse environments, error handling for network or recognition failures, and graceful shutdown on user interruption. The program's simplicity and modular design allow easy customization and extension to support additional devices and commands.

To use this system, a Raspberry Pi with microphone input, an internet connection, and devices connected to designated GPIO pins are needed. The Python script requires libraries such as SpeechRecognition, PyAudio, and RPi.GPIO, and can be run directly on the Pi.

This project serves as a practical introduction to integrating voice control with embedded hardware, suitable for prototyping home automation projects or learning embedded system programming.
