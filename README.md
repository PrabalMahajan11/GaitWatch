# GaitWatch Wearable Sensory System on Footwear for Detecting Abnormal Gaits

![WhatsApp Image 2024-02-02 at 11 21 32 PM](https://github.com/PrabalMahajan11/GaitWatch/assets/100370090/233ecfba-739f-4bf3-8186-cda9554a0c48)

![architectural block diagram](https://github.com/PrabalMahajan11/GaitWatch/assets/100370090/da7fe0c2-0f7b-41bc-a048-49921f36257e)

![circuit](https://github.com/PrabalMahajan11/GaitWatch/assets/100370090/12e4e02d-aa05-44dc-aae6-3edad986df8c)



In this work, we demonstrate a wearable sensor system
using accelerometers, gyroscopes and range sensors that can
automatically detect intra-individual gait anomalies during
daily activities. The system employs machine learning al-
gorithms trained on labeled normal and abnormal gait data.
We validate the system’s accuracy in distinguishing abnormal
gait and test its performance under real-world scenarios. The
wearable gait analysis system is expected to provide clinicians
and researchers with an objective and easy-to-use tool for
ubiquitous gait monitoring and early detection of movement
disorders.


We utilize one ESP32 development module for
the wireless transmission of data acquired from four sensors
(two range sensors and two MPU6050 units). The ESP32
is a low-cost, low-power system on a chip (SoC) module
that integrates Wi-Fi and Bluetooth connectivity, making it well-suited for wireless communication in Internet of Things
(IoT) systems. The use of two MPU6050 sensors, where in
each contain a 3-axis accelerometer and 3-axis gyroscope,
enables improved accuracy through sensor fusion algorithms
that combine the data from multiple motion sensors.
Two lithium polymer (LiPo) batteries are employed to
power different components of the system - one LiPo battery is
connected to a buck converter to maintain a steady voltage of
approximately 3.4-3.6 V for the operation of the velostat pres-
sure sensors. Velostat pressure sensors operate on the principle
of piezo-resistivity, whereby the electrical resistivity changes
in response to an applied mechanical pressure. The second
LiPo battery directly powers the ESP32 module. Additionally,
a multiplexer integrated circuit is implemented for sequentially
supplying the data from all four sensors over common buses
to the analog inputs of the ESP32. The multiplexer enables the
connection of multiple analog signals to the limited number
of ESP32 analog inputs for data acquisition.
