import os
import georinex as gr
import pyproj

"""user is required to change working directory to where the RINEX file is in"""

#prompts user to input directory names
print("-----\nBase Station RINEX Filename:\n-----")
base = input()
print("-----\nRover RINEX Filename:\n-----")
rover = input()

cwd = os.getcwd()
baser = r'%s\%s'%(cwd,base)
roverr = r'%s\%s'%(cwd,rover)

#parses the rinex and grabs the satellite IDs using Georinex
headerbase = gr.rinexheader(baser)
ecefxb = float(headerbase['APPROX POSITION XYZ'].split()[0])
ecefyb = float(headerbase['APPROX POSITION XYZ'].split()[1])
ecefzb = float(headerbase['APPROX POSITION XYZ'].split()[2])
receiverbase = headerbase["OBSERVER / AGENCY"]
recunitbase = headerbase["REC # / TYPE / VERS"]

#parses the rinex and grabs the satellite IDs using Georinex
headerrover = gr.rinexheader(roverr)
ecefxr = float(headerrover['APPROX POSITION XYZ'].split()[0])
ecefyr = float(headerrover['APPROX POSITION XYZ'].split()[1])
ecefzr = float(headerrover['APPROX POSITION XYZ'].split()[2])
receiverrover = headerrover["OBSERVER / AGENCY"]
recunitrover = headerrover["REC # / TYPE / VERS"]


rawb = pyproj.Transformer.from_crs("EPSG:4978","EPSG:4326")
latb, lonb, altb = rawb.transform(ecefxb, ecefyb, ecefzb, radians=False)

rawr = pyproj.Transformer.from_crs("EPSG:4978","EPSG:4326")
latr, lonr, altr = rawr.transform(ecefxr, ecefyr, ecefzr, radians=False)

print("\n-----\nSUMMARY : BASE STATION\n-----")
print("ECEF POSITONS:","\nX: ",ecefxb,"\nY: ",ecefyb,"\nZ: ",ecefzb)
print("\nGEOGRAPHIC POSITIONS (WGS84):","\nLON: ",lonb,"\nLAT: ",latb,"\nALT: ",altb)
print("\nRECEIVER DETAILS:\n",receiverbase,"\n",recunitbase)

print("\n-----\nSUMMARY : ROVER\n-----")
print("ECEF POSITONS:","\nX: ",ecefxr,"\nY: ",ecefyr,"\nZ: ",ecefzr)
print("\nGEOGRAPHIC POSITIONS (WGS84):","\nLON: ",lonr,"\nLAT: ",latr,"\nALT: ",altr)
print("\nRECEIVER DETAILS:\n",receiverrover,"\n",recunitrover)

baseline = round(float((((ecefxr-ecefxb)**2 + (ecefyr-ecefyb)**2)**0.5)/1000),4)

print("\n-----\nBASELINE DISTANCE\n-----")
print(baseline," kilometers")