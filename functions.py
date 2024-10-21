import os
import json

def file_read(filename):
    with open (filename, "r") as f:
        temp = json.load (f)
    return temp

def file_write(filename, data):
    with open (filename, "w") as f:
        json.dump(data, f, indent = 4)


def lijst(filename):
    temp = file_read(filename)
    for entry in temp:
        for key in entry:
            print (key,":", entry[key])
        print ("==================") 

def toevoegen(filename, ID, schakel, *attributes):
    new_data = {}
    temp = file_read(filename)
    i = len(temp) - 1
    new_data[ID] = i + 1
    new_data[schakel] = False
    for i in attributes:
        temp_in = input (i + ": ")
        if temp_in == "true":
            new_data[i] = True
        elif temp_in == "false":
            new_data[i] = False
        else:
            new_data[i] = temp_in
    temp.append(new_data)
    file_write(filename, temp)

def verwijderen(filename, tekst):
    lijst(filename)
    temp = file_read(filename)
    new_data = []
    keuze = input (tekst)
    for entry in temp:
        if list(entry.values())[0] == int(keuze):
            pass
        else:
            new_data.append(entry)
    file_write(filename, new_data)


def schakel(filename, attribute, tekst, *IDS):
    new_data = []
    temp = file_read(filename)
    i = 0
    IDS_l = []
    for IDS in IDS:
        i += 1
        IDS_l.append(IDS)
    if i == 0:
        lijst(filename)
        keuze = input (tekst)
    else:
        keuze = IDS_l[0]
    for entry in temp:
        ID = list(entry.values())[0]
        if ID == int(keuze):
            entry.update({attribute: not list(entry.values())[1]})
            new_data.append(entry)
        else:
            new_data.append(entry)
    file_write(filename, new_data)

def aanpassen(filename, tekst):
    lijst(filename)
    new_data = []
    temp = file_read(filename)
    keuze = input (tekst)
    for entry in temp:
        if list(entry.values())[0] == int(keuze):
            i = 0
            for key in entry:
                if i > 1:
                    entry.update({key: input (f"{key}: ")})
                    i = i + 1
                else:
                    i = i + 1
            new_data.append(entry)
        else:
            new_data.append(entry)
    file_write(filename, new_data)

def enkel_tovoegen(filename, new_lijst, tekst_1):
    lijst(filename)
    temp = file_read(filename)
    keuze = input (tekst_1)
    for entry in temp:
        ID = list(entry.values())[0]
        if ID == int(keuze):
            if list(entry.values())[1] == False:
                new_lijst.update({list(entry.keys())[0]: ID})
                break
            else:
                pass
        else:
            pass
    return new_lijst

def samenvoegen(filename, filename_1, filename_2, tekst_1, tekst_2, tekst_3):
    new_entry = {}
    while True:
        new_entry = enkel_tovoegen(filename_1, new_entry, tekst_1)
        if new_entry == {}:
            print (tekst_3)
            input ("druk op <enter> om door te gaan...")
            continue
        else:
            schakel(filename_1, "uitgeschakeld", tekst_1,list(new_entry.values())[0]) #niet ideaal
            os.system('cls' if os.name == 'nt' else 'clear')
            new_entry = enkel_tovoegen(filename_2, new_entry, tekst_2)
            temp = file_read(filename)
            temp.append(new_entry)
            file_write(filename, temp)
            break