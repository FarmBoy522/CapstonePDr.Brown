# CapstonePDr.Brown
Option 8 - Capstone Project - CS490 ERAU

Vision Statement

Produce a handheld ultrasound inspection device for inspecting a bridge/structural component for faults in the field. This handheld unit will have an independent power supply and have the ability to gather/store test data. The device will be rugged enough to withstand field conditions such as shock from a fall, rain, and dust and dirt. Ideally the unit will operate over the period of 72 hours, while collecting and storing data for the duration of the test.

Product Backlog

Hardware:
	•	Design an outer casing to contain the electronics and test equipment.
	•	Requirements: the case must be able to withstand a fall from 3 ft and protect the contents of the case, the case must be water resistant and be able to protect the contents from water penetration from rain, the case must have a handle and or strap for operator use, the case shall have all required penetrations for equipment to run wires and status lights (if applicable). The case shall be resistant/ shielded from outside radio interference.
	•	 Design an electrical system to support the unit’s operation.
	•	Requirements: The power supply shall support equipment normal operating use for greater than or equal to 48 hours (Ideally 72hrs), the electrical system shall be reusable, the electrical system shall have wires secured to the casing or sheathed to prevent damage, the electrical system shall alert the user when power is low. Some portions of the system will operate at 500v and require verification that wire insulation is sufficient for safe operation. (The power supply may be exterior if required)
	•	Perform research to determine if the equipment can be miniaturized from the lab environment.
	•	(TX) Design a smaller equivalent to the signal generator for the transistors operating frequencies.
	•	Requirements: able to produce required frequency for transducer 500kHz, able to produce required frequency for transducer 50kHz, able to switch between the two frequencies, Able to adjust the amplitude of the signal (if required) Transmitter output: pulse 500V, 2microseconds. (Similar system) or Excitation: HV 1000v at 5us, LV 600v at 5us (data sheet)
	•	(RX) Design a smaller equivalent to the oscilloscope for the transistors operating frequencies.
	•	Requirements: able to receive required frequency for transducer 500kHz, able to receive required frequency for transducer 50kHz, able to switch between the two frequencies, Amplifier to boost amplitude of signal. (If required)
	•	Produce attachable extensions to the test equipment leads to extend the test length or assist in accessibility for operator (if required) (not to exceed 20 ft)
	•	Design the memory storage and access hardware
	•	Requirements: minimum storage of “The current data files contain 40000 double-precision numbers and are approx. 1.6 MB” sampling at 10 min interval over 72-hour period, must be computer accessible. (Estimated 691.2MB)
	•	Design an alarm/status system.
	•	Requirement: low battery/power light or alarm, self-check light or alarm, operating/on light or alarm, transmitting/testing light or alarm, memory full light or alarm, high temperature alarm light or alarm.
	•	Design a cooling system for the unit in the case of an overtemperature event. (If applicable)
	•	Requirement: temperature sensor inside the unit (RTD and fan recommended)

Software:
	•	Design/ program/find compatible software to process recorded signal. (MATLAB used previously)
	•	Requirements: must display the captured signal, alert the user if a fault is detected and where (if applicable)
	•	Develop software to monitor battery life and project remaining life 
	•	Develop software to monitor remaining memory space and project how much longer the device can record (use minutes and seconds remaining for recording)
	•	Develop software to pull data overtime from a signal to be used in other programs.
	•	Design software to perform a self-check of the system and determine if the unit has a fault.
	•	Design software to monitor temperature and activate the cooling system. Or shut down if the temperature exceeds 150 F (arbitrary value that may be changed)
	•	Design a GUI (graphical user interface) to quickly check calculated values and for maintenance purposes to display system data.
	
Other:
	•	The unit altogether shall not exceed 17 pounds 
	•	The unit shall be similar or smaller in size to that of a car battery
	•	The unit should be corrosion resistant
	•	The unit should have safety features to shut down the unit if a fault in the system is detected
	•	The unit budget shall not exceed 2000$

Client request:
	•	The unit shall store data to be processed using a computer at a later time.
	•	Recording triggered/start when transmission starts
	•	50 pulses sent each transmission (100 µsec interval in example)
	•	The revived 50 pulses are averaged together and displayed.
	•	The unit battery shall last for 48-72 hours or greater with samples being taken every 10 min.
	•	Budget less than or equal to 2000$
	•	MATLAB used to process data into usable form and graphed for analysis.

