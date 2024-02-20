# CapstonePDr.Brown
Option 8 - Capstone Project - CS490 ERAU
			      EE421/CS491

Vision Statement

Produce a handheld ultrasound inspection device for inspecting a bridge/structural component for faults in the field. This handheld unit gathers and stores test data collected over time for 48 to 72 hours.

Product Backlog
(current status shown in the issues tab)

Hardware:
	•	Design an outer casing to contain the electronics and test equipment.
	•	Requirements: the case must be able to withstand a fall from 3 ft and protect the contents of the case, the case must be water resistant and be able to protect the contents from water penetration from rain, 				      the case must have a handle and or strap for operator use, the case shall have all required penetrations for equipment to run wires and status lights (if applicable). The case shall be resistant/ 			      shielded from outside radio interference.
	•	Design an electrical system to support the unit’s operation.
	•	Requirements: The power supply shall support equipment normal operating use for greater than or equal to 48 hours (Ideally 72hrs), the electrical system shall be reusable, the electrical system shall have wires 			      secured to the casing or sheathed to prevent damage, the electrical system shall alert the user when power is low. Some portions of the system will operate at 500v and require verification that 			      wire insulation is sufficient for safe operation. 
	•	(TX) Design a smaller equivalent to the signal generator for the transistors operating frequencies.
	•	Requirements: able to produce required frequency for transducer 500kHz, able to produce required frequency for transducer 50kHz, able to switch between the two frequencies, Able to adjust the amplitude of 			              the signal (if required) Transmitter output: pulse 500V, 2microseconds. (Similar system) or Excitation: HV 1000v at 5us, LV 600v at 5us (data sheet)
	•	(RX) Design a smaller equivalent to the oscilloscope for the transistors operating frequencies.
	•	Requirements: able to receive required frequency for transducer 500kHz, able to receive required frequency for transducer 50kHz, able to switch between the two frequencies, Amplifier to boost amplitude of signal. 			      (If required)
	•	Produce attachable extensions to the test equipment leads to extend the test length or assist in accessibility for operator (if required) (not to exceed 20 ft)
	•	Design the memory storage and access hardware
	•	Requirements: minimum storage of “The current data files contain 40000 double-precision numbers and are approx. 1.6 MB” sampling at 10 min interval over 72-hour period, must be computer accessible. 					      (Estimated 691.2MB)
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
	•	The unit altogether shall not exceed 25 pounds 
	•	The unit shall be usable by a single operatior in the field.
	•	The unit should be corrosion resistant
	•	The unit should have safety features to shut down the unit if a fault in the system is detected
	•	The unit budget shall not exceed 2000$

Client request:
	•	The unit shall store data to be processed using a computer at a later time.
	•	Recording triggered/start when transmission starts

 
 
 
 2024 update for Backlog

To Do
Develop system to prevent frequent OS errors to allow program to run continuously #55
Design program to monitor charge voltage #54
Create system trigger to shutdown and light "overtemp protection" LED in case of uncontrolled temp overrun #53
Create system trigger to run "charging" fans if temps exceed operational max for parts #52
Wire "charging" fans to main circuit #51
Determine fan mounting positions #50
Install cooling fans #49
Apply sealant to the exterior casing #48
Purchase waterproof sealant #47
Label exterior LED's, switches, and components #46
Create cover plates (if applicable) #45
Create an operators manual (if time available) #44
Purchase 12 to 19.5 v power converter #43
Mount and Install RTD #42
Purchase RTD (resistance temperature detector) #41
Connect capacitor electrically HVS #40
Mount and install relay HVS #39
Purchase Relay for HVS #38
Test fan controllers via Arduino [Sprint 1 2024] #23
Design software to perform a self-check of the system and determine if the unit has a fault. #14
Develop software to store oscilloscope data on computer #13
Develop software to monitor remaining memory space and project how much longer the device can record (use minutes and seconds remaining for recording) #12
Develop software to monitor battery life and project remaining life #11
Test new data recording system with old Matlab program #10
Design the memory storage and access hardware #7

In Progress
Produce drip cover for exterior casing #56
Install electrical system HVS part 8 (resistors) #37
Install electrical system HVS part 7 (coaxial connection port) #36
Install electrical system LVS part 6 (battery) #35
Install electrical system HVS part 6 (12v to 500v power converter) #34
Install electrical system HVS part 5 (Fuses) #33
Install electrical system HVS part 4 (exterior operated switches) #32
Install electrical system HVS part 3 (Capacitor) #31
Install electrical system HVS part 2 (wiring) #30
Install electrical system HVS part 1 (circuit boards) #29
Install electrical system LVS part 5 (Fuses) #28
Install electrical system LVS part 4 (exterior operated switches) #27
Install electrical system LVS part 3 (LED) #26
Install electrical system LVS part 2 (wiring) #25
Install electrical system LVS part 1 (circuit boards) #24
Test electrical systems #21
code for led indicating lights/alarms #18
verify design criteria met #17

Finished
Program LUT for fan controllers [Sprint 1 2024] #22
Verify components electrically #20
connect/solder electrical system components #19
Design a GUI (graphical user interface) to quickly check calculated values and for maintenance purposes to display system data. #16
Design software to monitor temperature and activate the cooling system. Or shut down if the temperature exceeds 150 F (arbitrary value that may be changed) #15
Design a cooling system for the unit in the case of an overtemperature event. (If applicable) #9
Design an alarm/status system. #8
Produce attachable extensions to the test equipment leads to extend the test length or assist in accessibility for operator (if required) #6
(RX) Design a smaller equivalent to the oscilloscope for the transistors operating frequencies. #5
(TX) Design a smaller equivalent to the signal generator for the transistors operating frequencies. #4
Perform research to determine if the equipment can be miniaturized from the lab environment. #3
Design an electrical system to support the unit’s operation. #2
Design an outer casing to contain the electronics and test equipment. #1

	•	50 pulses sent each transmission (100 µsec interval in example)
	•	The revived 50 pulses are averaged together and displayed.
	•	The unit battery shall last for 48-72 hours or greater with samples being taken every 10 min.
	•	Budget less than or equal to 2000$
	•	MATLAB used to process data into usable form and graphed for analysis.

