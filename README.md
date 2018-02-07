## Transit 

#### Transit is a MacOS IR tool kit that I've been writing while on the train. Most of the time this is done while delayed. 


Transit can pull the following information from a system. 


    1. Run a full informational scan:
    2. Gather preference lists for all users:
    3. Gather preference lists for one user:
    4. Gather all Root level preference lists: (May require root)
    5. Tar up log directories:
    6. Gather system information:

1. Well return a series of information about the system itself.
2. This option will return the plists for all users 
3. Option 3 will return plists for one user
4. This will return all of the root level plists
5. This feature will currently zip up the root log directory
6. Gather system info.


--

`helper.py` has a class `Gather_System_Info()` this class will be the most heavily used class in this code. This is what will be used to shell out and run any system info retreival. Ideally I would like to stick to python libraries to call this data. But once in a while we need to shell out to obtain the data or result we are looking for. 
Anytime we call `shell_cmd()` from the `Gather_System_Info()` class we log the command ran to disk. By default this will log to `./logging/incidentR.log`
