import os
import georinex as gr
import pyproj

"""user is required to change working directory to where the RINEX file is in"""

#prompts user to input directory names
print("-----\nRINEX Filename:\n-----")
rinex = input()

cwd = os.getcwd()
file = r'%s\%s'%(cwd,rinex)

#parses the rinex and grabs the satellite IDs using Georinex
header = gr.rinexheader(file)
ecefx = float(header['APPROX POSITION XYZ'].split()[0])
ecefy = float(header['APPROX POSITION XYZ'].split()[1])
ecefz = float(header['APPROX POSITION XYZ'].split()[2])
receiver = header["OBSERVER / AGENCY"]
recunit = header["REC # / TYPE / VERS"]


raw = pyproj.Transformer.from_crs("EPSG:4978","EPSG:4326")
lat, lon, alt = raw.transform(ecefx, ecefy, ecefz, radians=False)

print("\n-----\nSUMMARY\n-----")
print("ECEF POSITONS:","\nX: ",ecefx,"\nY: ",ecefy,"\nZ: ",ecefz)
print("\nGEOGRAPHIC POSITIONS (WGS84):","\nLON: ",lon,"\nLAT: ",lat,"\nALT: ",alt)
print("\nRECEIVER DETAILS:\n",receiver,"\n",recunit)