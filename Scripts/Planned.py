import json
import os

print("start")

def CompleteVersion(version_code):
    path = os.path.realpath(__file__)
    dir = os.path.dirname(path)
    dir = dir.replace('Scripts', 'Missions') 
    os.chdir(dir)
    print(version_code)
    complete = open(f'Complete/{version_code}.json')
    data_complete = json.load(complete)
    planned = []

    for m in data_complete:
       if "guard_mission" in m["additional"]:
           planned.append(m)


    with open(f'Planned/{version_code}.json', 'w+') as outfile:
        json.dump(planned, outfile)

    complete.close()


versions = open("Stats.json")
versions_data = json.load(versions)

for version in versions_data: 
    CompleteVersion(version["code"])

versions.close()

print("finished")