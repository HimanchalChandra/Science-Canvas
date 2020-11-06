#NASA Labs Facilities and create a visualization

#FOLLOWING ARE THE QUERY AND RESULTS EXECUTED USING MYSQL QUERIES IN MYSQL COMMAND LINE CLIENT
#1.The total number of records in this dataset.
#   Query - SELECT COUNT(SerialNo) FROM nasa_labs_facilities;
#   Result - +-----------------+
#            | COUNT(SerialNo) |
#            +-----------------+
#            |             439 |
#            +-----------------+
#
#2.Total of facilities per state.
#   Query - SELECT State, count(SerialNo) FROM nasa_labs_facilities GROUP BY State;
#   Result - +-------+-----------------+
#            | State | count(SerialNo) |
#            +-------+-----------------+
#            | AL    |             136 |
#            | AZ    |               1 |
#            | CA    |              83 |
#            | DC    |              23 |
#            | LA    |              17 |
#            | MD    |              32 |
#            | MS    |              27 |
#            | OH    |              35 |
#            | TN    |               3 |
#            | TX    |              10 |
#            | VA    |              60 |
#            | WA    |              12 |
#            +-------+-----------------+
#
#3.Latest facility
#   Query - SELECT MAX(Last_Update), Facility FROM nasa_labs_facilities;
#   Result - +------------------+---------------------------------------+
#            | MAX(Last_Update) | Facility                              |
#            +------------------+---------------------------------------+
#            | 31-03-2014       | Mach 6, High Reynolds Number Facility |
#            +------------------+---------------------------------------+
#
#4.Distribution of all active facilities per state.
#   Query - SELECT State, count(SerialNo) FROM nasa_labs_facilities WHERE Status= 'Active'  GROUP BY State;
#   Result - +-------+-----------------+
#            | State | count(SerialNo) |
#            +-------+-----------------+
#            | AL    |             118 |
#            | AZ    |               1 |
#            | CA    |              61 |
#            | DC    |              21 |
#            | LA    |              16 |
#            | MD    |              32 |
#            | MS    |              25 |
#            | OH    |              33 |
#            | TN    |               2 |
#            | TX    |               9 |
#            | VA    |              58 |
#            | WA    |              12 |
#            +-------+-----------------+
#
#5.Center names and their numbers. 
#   Query - SELECT DISTINCT Center, Phone FROM nasa_labs_facilities;
#   Result - +----------------------------------------------------+----------------+
#            | Center                                             | Phone          |
#            +----------------------------------------------------+----------------+
#            | Air Force Research Laboratory                      | 937 255-1689   |
#            | Arnold Engineering Development Center              | (931) 454-6513 |
#            | Pacific Northwest National Laboratory              | 509-372-6026   |
#            | Intelsat General                                   | 424 206-2725   |
#            | Ames Research Center                               | 650 603-9506   |
#            | Armstrong Flight Research Center                   | 661-276-2585   |
#            | Glenn Research Center                              | 216-433-9370   |
#            | Goddard Space Flight Center                        | 301 286 2520   |
#            | Jet Propulsion Lab                                 | 818.354.0701   |
#            | Johnson Space Center                               | 281.483.3219   |
#            | Langley Research Center                            | 757.864-3848   |
#            | Marshall Space Flight Center                       | 256-544-7795   |
#            | Michoud Assembly Facility                          | 504.257-2619   |
#            | NASA Aircraft Management Division                  | 202 358 4721   |
#            | Stennis Space Center                               | 601-688-1646   |
#            | Wallops Flight Facility/GSFC                       | 757-824-1120   |
#            | Orbital Satellite Manufacturing Facility - Arizona | 480 355 7275   |
#            | Raytheon Space and Airborne Systems - El Segundo   | 310-647-4171   |
#            +----------------------------------------------------+----------------+
#
#6.Distribution by year.
#   Query - SELECT Agency, Center, Facility, Occupied FROM nasa_labs_facilities WHERE OCCUPIED != 0;
#   Result - Showing part of the result (since there was large amount of data)
#            +----------+---------------------------------------+--------------------------------------------------------------------------------+------+
#            | Agency   | Center                                | Facility                                                                       | Year |
#            +----------+---------------------------------------+--------------------------------------------------------------------------------+------+
#            | DOD      | Air Force Research Laboratory         | Mach 6, High Reynolds Number Facility                                          | 1960 |
#            | DOD      | Air Force Research Laboratory         | Subsonic Aerodynamic Research Laboratory                                       | 1985 |
#            | DOD      | Air Force Research Laboratory         | Trisonic Gasdynamics Facility                                                  | 1960 |
#            | DOD      | Air Force Research Laboratory         | Vertical Wind Tunnel                                                           | 1960 |
#            | DOD      | Arnold Engineering Development Center | 10V Test Chamber                                                               | 1965 |
#            | DOD      | Arnold Engineering Development Center | 7V Sensor Test Facility                                                        | 1994 |
#            | DOD      | Arnold Engineering Development Center | Mark I Aerospace Chamber                                                       | 1963 |
#            | Intelsat | Intelsat General                      | Environmental Test Lab-Shaker                                                  | 1969 |
#            | Intelsat | Intelsat General                      | Environmental Test Lab-Test Chamber                                            | 1969 |
#            | Intelsat | Intelsat General                      | Large Anechoic Chamber                                                         | 1969 |
#            | Intelsat | Intelsat General                      | Outdoor Antenna Test Range                                                     | 1969 |
#            | Intelsat | Intelsat General                      | Scanning Auger Multiprobe; Electron Microscope                                 | 1969 |
#            | Intelsat | Intelsat General                      | Semiconductor Fabrication 1                                                    | 1969 |
#            | Intelsat | Intelsat General                      | Semiconductor Fabrication 2                                                    | 1969 |
#            | Intelsat | Intelsat General                      | Semiconductor Fabrication 3                                                    | 1969 |
#            | Intelsat | Intelsat General                      | Semiconductor Fabrication 4                                                    | 1969 |
#            | Intelsat | Intelsat General                      | Semiconductor Fabrication 5                                                    | 1969 |


import mysql.connector
from mysql.connector import Error
import matplotlib.pyplot as plt

#Function to connect to the database, analysis and visualization
def connect():
        print("Connecting to database")
        try:
            #defining the configuration
            config = {
              'user': 'ank99',
              'password': '1010101010',
              'host': 'localhost',
              'port': '3306',
              'database': 'nasa_lab_facilities',
              'raise_on_warnings': True,
            }

            conn = mysql.connector.connect(**config) 
            
            if conn.is_connected():
                print("Connection established")
                
                #Total number of records in the dataset
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(SerialNo) FROM nasa_labs_facilities")
                value = cursor.fetchall()
                print("----------------------------------------------------")
                print("")
                print("Total number of records:")
                print("")
                print(value[0][0])
                print("----------------------------------------------------")
                print("")
                
                #Total of facilities per state
                cursor.execute("SELECT State, count(SerialNo) FROM nasa_labs_facilities GROUP BY State")                
                values = cursor.fetchall()
                print("States with their no of facilities:")
                print("")
                print(values)
                print("----------------------------------------------------")
                print("")
                
                #Latest facility
                cursor.execute("SELECT MAX(Last_Update), Facility FROM nasa_labs_facilities")
                values = cursor.fetchall()
                print("Latest Facility:")
                print("")
                print(values)
                print("----------------------------------------------------")
                print("")
           
                #Distribution of active facilities per state
                cursor.execute("SELECT State, count(SerialNo) FROM nasa_labs_facilities WHERE Status= 'Active'  GROUP BY State")
                values = cursor.fetchall()
                print("States with their no of active facilities:")
                print("")
                print(values)
                print("----------------------------------------------------")
                print("")
                
                #Center names and their numbers
                cursor.execute("SELECT DISTINCT Center, Phone FROM nasa_labs_facilities")
                values = cursor.fetchall()
                print("Centers with their phone numbers:")
                print("")
                print(values)
                print("----------------------------------------------------")
                print("")
                
                #Distribution by year
                cursor.execute("SELECT Agency, Center, Facility, Occupied FROM nasa_labs_facilities WHERE OCCUPIED != 0")
                values = cursor.fetchall()
                print("Some Facilities with their Centers, Agencies and with the year Occupied:")
                print("")
                for index, value in enumerate(values):#Showing only limited values to prevent crowding in output
                    print(value)
                    if (index==12):
                        break
                print("----------------------------------------------------")
                print("")
                
                
                #VISUALISATION
                print ("")
                print ("")
                print ("")
                print ("----------------VISUALISATION-------------------")

                
                #Scatter plot and line plot for no of facilities in different states
                cursor.execute("SELECT COUNT(SerialNo), State FROM nasa_labs_facilities GROUP BY State")
                count_state = cursor.fetchall()
                cuts = [count_state[i][0] for i in range(0,len(count_state))]
                names = [count_state[i][1] for i in range(0,len(count_state))]                                
                plt.scatter(names, cuts)
                plt.title('No of facilities in different state')
                plt.show()
                plt.plot(names, cuts)
                plt.title('No of facilities in different state')
                plt.show()

                
                #Scatter plot and line plot for status of different facilities
                cursor.execute("SELECT COUNT(SerialNo), Status FROM nasa_labs_facilities WHERE Status!='0' GROUP BY Status ")
                count_status = cursor.fetchall()
                cuts = [count_status[i][0] for i in range(0,len(count_status))]
                names = [count_status[i][1] for i in range(0,len(count_status))]                
                cuts.remove(1)
                names.remove('Under')
                plt.scatter(names, cuts, color = 'orange')
                plt.title('Status of facilities')
                plt.show()
                plt.plot(names, cuts, color = 'orange')
                plt.title('Status of facilities')
                plt.show()
                
                #Extracting data for further analysis
                cursor.execute("SELECT State FROM nasa_labs_facilities")
                State = cursor.fetchall()
                cursor.execute("SELECT Status FROM nasa_labs_facilities WHERE Status != '0' AND Status != 'Under'")
                Status = cursor.fetchall()
                cursor.execute("SELECT State FROM nasa_labs_facilities WHERE Status = 'Active'")
                State_Active = cursor.fetchall()
                cursor.execute("SELECT State FROM nasa_labs_facilities WHERE Status = 'Inactive'")
                State_Inactive = cursor.fetchall()
                cursor.execute("SELECT Agency FROM nasa_labs_facilities")
                Facilities_per_agency = cursor.fetchall()
                
                #Pie chart analysis for No of facilties per state                    
                cursor.execute("SELECT COUNT(SerialNo), State FROM nasa_labs_facilities GROUP BY State")
                count_state = cursor.fetchall()
                cuts = [count_state[i][0] for i in range(0,len(count_state))]
                names = [count_state[i][1] for i in range(0,len(count_state))]                                
                plt.pie(cuts, labels = names, autopct = '%1.1f%%')
                plt.title('No of facilities in different state')
                plt.show()
                
                #Pie chart analysis for Status of different facilities
                cursor.execute("SELECT COUNT(SerialNo), Status FROM nasa_labs_facilities WHERE Status!='0' GROUP BY Status ")
                count_status = cursor.fetchall()
                cuts = [count_status[i][0] for i in range(0,len(count_status))]#creating values for pie chart
                names = [count_status[i][1] for i in range(0,len(count_status))]#creating labels for pie chart
                #Just formatting the output a bit
                cuts.remove(1)
                names.remove('Under')
                temp1, temp2 = cuts[3], names[3]
                cuts[3] = cuts[0]
                names[3] = names[0]
                cuts[0] = temp1
                names[0] = temp2
                plt.pie(cuts, labels = names, autopct = '%1.1f%%')
                plt.title('Status of facilities')
                plt.show()
                
                #Plotting histograms for the data
                
                #Histogram for no of facilties per state
                plt.hist(State, label = 'No of facilities per state', histtype = 'stepfilled', color = 'lightseagreen')
                plt.legend()
                plt.show()
                
                #Histogram for no of active facilties per state
                plt.hist(State_Active, label = 'No of active facilities per state', histtype = 'stepfilled', color = 'pink')
                plt.legend()
                plt.show()
                
                #Histogram for no of inactive facilties per state
                plt.hist(State_Inactive, label = 'No of inactive facilities per state', histtype = 'bar', color = 'palegreen')
                plt.legend()
                plt.show()
                
                #Histogram for no of facilties per agency
                plt.hist(Facilities_per_agency, label = 'No of facilities per agency', histtype = 'bar', color = 'lightcoral')
                plt.legend()
                plt.show()                
                
                #Histogram for status of different facilities
                plt.hist(Status, label = 'Status of facilities', histtype = 'stepfilled', color = 'orange')
                plt.legend()
                plt.show()
                

    
            else:
                print('Connection failed.')

            conn.close()            
            print('Connection closed.')
            
        except Error as exception:
            print(exception)
            
connect()