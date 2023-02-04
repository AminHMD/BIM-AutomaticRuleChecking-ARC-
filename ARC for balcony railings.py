
#crtl + K ,  => fold codes
#crtl + /  => comment codes



from ast import IsNot, NotIn, Return, Str
from asyncio.base_futures import _FINISHED
from asyncio.windows_events import NULL
from cgi import print_arguments, print_directory
from doctest import REPORTING_FLAGS
from inspect import formatannotationrelativeto
from itertools import count
from multiprocessing import Value
from multiprocessing.resource_sharer import stop
from operator import index, indexOf
from pickle import TRUE
from re import X, template
from selectors import SelectSelector
import string
from tkinter import N


file = open('SampleFile.ifc')
f = file.readlines()


##max acceptable height for railings bellow 4th floor:
acceptable_height_1=950
##max acceptable height for railings above 4th floor:
acceptable_height_2=1100

# Number of lines
line_count = 0
for line in f:
    line_count += 1
print("no. of lines imported from ifc file :")    
print(line_count)

wanted_ifc=""





#### step 1:
# Search Wanted IFC
#list for the final results (list to list)
final_results_list_1=[]
def search_ifc1(wanted_ifc):
        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
                #list for each ifc that has been found to inject params:
                each_ifc_params_list=[]

                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
                #print("Line no. (#...):")
                #print(selected_line[line_no1:line_no2])
                each_ifc_params_list.append(selected_line[line_no1:line_no2])

                # get no. of params
                selected_line = founded_lines_list[count_wanted_ifc]
                comma = ","
                for_loop_counter=-1
                comma_counter = 0
                comma_indexes=[]
                for x in selected_line:
                    for_loop_counter+=1
                    if x == ",":
                        comma_counter += 1
                        comma_indexes.append(for_loop_counter)
                #print("no. of commas in the line: ")
                #print(comma_counter)
                #print("comma indexes in the line: ")
                #print(comma_indexes)
                #print(selected_line)

                # get first param
                if comma_counter>0:
                    selected_line = founded_lines_list[count_wanted_ifc]
                    param_1_1 = selected_line.index("('")
                    param_1_2 = selected_line.index("',")
                    #print("first param is: ")
                    #print(selected_line[param_1_1+2:param_1_2])
                    each_ifc_params_list.append(selected_line[param_1_1+2:param_1_2])


                # get secound param
                if comma_counter>=1:
                    selected_line = founded_lines_list[count_wanted_ifc]
                    #print("secound param is: ")
                    #print(selected_line[comma_indexes[0]+1:comma_indexes[1]])
                    each_ifc_params_list.append(selected_line[comma_indexes[0]+1:comma_indexes[1]])


                # get third param
                if comma_counter>=2:
                    selected_line = founded_lines_list[count_wanted_ifc]
                    #print("third param is: ")
                    #print(selected_line[comma_indexes[1]+1:comma_indexes[2]])
                    each_ifc_params_list.append(selected_line[comma_indexes[1]+1:comma_indexes[2]])


                # get fourth param
                if comma_counter>=3:
                    selected_line = founded_lines_list[count_wanted_ifc]
                    #print("fourth param is: ")
                    #print(selected_line[comma_indexes[2]+1:comma_indexes[3]])
                    each_ifc_params_list.append(selected_line[comma_indexes[2]+1:comma_indexes[3]])



                # get fifth param
                if comma_counter>=4:
                    selected_line = founded_lines_list[count_wanted_ifc]
                    #print("fifth param is: ")
                    #print(selected_line[comma_indexes[3]+1:comma_indexes[4]])
                    each_ifc_params_list.append(selected_line[comma_indexes[3]+1:comma_indexes[4]])


                # get sixth param
                if comma_counter>=5:
                    selected_line = founded_lines_list[count_wanted_ifc]
                    #print("sixth param is: ")
                    #print(selected_line[comma_indexes[4]:comma_indexes[4]+2])
                    each_ifc_params_list.append(selected_line[comma_indexes[4]+1:comma_indexes[5]])

                # get seventh param
                if comma_counter>=6:
                    selected_line = founded_lines_list[count_wanted_ifc]
                    #print("seventh param is: ")
                    #print(selected_line[comma_indexes[5]+1:comma_indexes[6]])
                    each_ifc_params_list.append(selected_line[comma_indexes[5]+1:comma_indexes[6]])

                # get eighth param
                if comma_counter>=7:
                    selected_line = founded_lines_list[count_wanted_ifc]
                    #print("eighth param is: ")
                    #print(selected_line[comma_indexes[6]+1:comma_indexes[7]])
                    each_ifc_params_list.append(selected_line[comma_indexes[6]+1:comma_indexes[7]])

                # get ninth param
                if comma_counter>=8:
                    selected_line = founded_lines_list[count_wanted_ifc]
                    #print("ninth param is: ")
                    #print(selected_line[comma_indexes[7]+1: -3])
                    each_ifc_params_list.append(selected_line[comma_indexes[7]+1: -3])


                #adding the founded ifc with its params in to list:
                final_results_list_1.append(each_ifc_params_list)


                
        # print("no. of wanted ifc founded: ")        
        #print(final_results_list_1)
        # print("as it can be seen in the following: ")   
        # for i in final_results_list_1:
        #         print(i) 







#### step 2:
# Search Wanted IFC
 #list for the final results (list to list)
final_results_list_2=[]
def search_ifc2(wanted_ifc):
        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        for line in f:





            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
                #list for each ifc that has been found to inject params:
                each_ifc_params_list=[]

                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
                #print("Line no. (#...):")
                #print(selected_line[line_no1:line_no2])
                each_ifc_params_list.append(selected_line[line_no1:line_no2])

                # get no. of params
                selected_line = founded_lines_list[count_wanted_ifc]
                comma = ","
                for_loop_counter=-1
                comma_counter = 0
                comma_indexes=[]
                for x in selected_line:
                    for_loop_counter+=1
                    if x == ",":
                        comma_counter += 1
                        comma_indexes.append(for_loop_counter)



                     
                      
                #print("no. of commas in the line: ")
                #print(comma_counter)
                #print("comma indexes in the line: ")
                #print(comma_indexes)
                

                # get first param
                if comma_counter>0:
                    selected_line = founded_lines_list[count_wanted_ifc]
                    param_1_1 = selected_line.index("('")
                    param_1_2 = selected_line.index("',")
                    #print("first param is: ")
                    #print(selected_line[param_1_1+2:param_1_2])
                    each_ifc_params_list.append(selected_line[param_1_1+2:param_1_2])


                # get secound param
                if comma_counter>=1:
                    selected_line = founded_lines_list[count_wanted_ifc]
                    #print("secound param is: ")
                    #print(selected_line[comma_indexes[0]+1:comma_indexes[1]])
                    each_ifc_params_list.append(selected_line[comma_indexes[0]+1:comma_indexes[1]])


                # get third param
                if comma_counter>=2:
                    selected_line = founded_lines_list[count_wanted_ifc]
                    #print("third param is: ")
                    #print(selected_line[comma_indexes[1]+1:comma_indexes[2]])
                    each_ifc_params_list.append(selected_line[comma_indexes[1]+1:comma_indexes[2]])


                # get fourth param
                if comma_counter>=3:
                    selected_line = founded_lines_list[count_wanted_ifc]
                    #print("fourth param is: ")
                    #print(selected_line[comma_indexes[2]+1:comma_indexes[3]])
                    each_ifc_params_list.append(selected_line[comma_indexes[2]+1:comma_indexes[3]])


                # get fifth param
                if comma_counter>=5:
                    selected_line = founded_lines_list[count_wanted_ifc]
                    #print("fifth param is: ")
                    #print(selected_line[comma_indexes[4]+1:comma_indexes[5]])
                #if added here to handle secound step, i read three letters to see if ( is included. remind that ( can not be recognized that is why i read 3 letters
                   
                    if comma_counter==6:
                            
                            # print("fifth param is: ")
                            # print(selected_line[comma_indexes[3]+2:comma_indexes[5]-1])
                            each_ifc_params_list.append(selected_line[comma_indexes[3]+2:comma_indexes[5]-1])
                            
                            # get sixth param
                            selected_line = founded_lines_list[count_wanted_ifc]
                            # print("sixth param is: ")
                            # print(selected_line[comma_indexes[5]+2:-3])
                            each_ifc_params_list.append(selected_line[comma_indexes[5]+2:-3])
                            
                        
                            
                    else:
                            # get fifth param
                            selected_line = founded_lines_list[count_wanted_ifc]
                            #print("fifth param is: ")
                            #print(selected_line[comma_indexes[4]+1:-3])
                            each_ifc_params_list.append(selected_line[comma_indexes[3]+2:comma_indexes[4]-1])

                            # get sixth param
                            selected_line = founded_lines_list[count_wanted_ifc]
                            #print("sixth param is: ")
                            #print(selected_line[comma_indexes[4]+1:-3])
                            each_ifc_params_list.append(selected_line[comma_indexes[4]+1:-3])
                    
               


                #adding the founded ifc with its params in to list:
                final_results_list_2.append(each_ifc_params_list)


        # print("no. of wanted ifc founded: ")        
        #print(final_results_list_2)
        # print("as it can be seen in the following: ")   
        # for i in final_results_list_2:
        #         print(i) 
       



#### step 3:
## in this step i ignored the ones that they have two parameters for 5th value. in case that i face to them i have to handle it from here
final_results_list_3=[]
def search_ifc3():
     
      for x in final_results_list_2:
        #print(x)
        for y in final_results_list_1:
            #print(y)
            if str(x[5])==str(y[0]):
                #print(x)
                final_results_list_3.append(x)
                

    #   for r in final_results_list_3:
    #  print(final_results_list_3)
    

#### step 4:
##select the one with pset_railingcommon from other two:
everything="#"
final_results_list_4=[]

def search_ifc4():
        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []
        founded_lines_list.clear()

        #list for each ifc that has been found to inject params:
        each_ifc_params_list_4=[]

        for line in f:
            if everything in line:
                
                count_wanted_ifc += 1
                founded_lines_list.append(line)

                

                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
                #print("Line no. (#...):")
                #print(selected_line[line_no1:line_no2])
              


                for x in final_results_list_3:
                    
                    if x[6]==selected_line[line_no1:line_no2]:
                         #print(selected_line)
                         ## I have added the line no of elelments in final_results_list_3 to founded equal lines ---- lasr param in line no of main ifc_railing 
                         selected_line= "main_ifc_line_no:"+(x[5])+selected_line
                         each_ifc_params_list_4.append(selected_line)
                 
        ## here we have list of lines that is equal to the 6th parameter of each_ifc_params_list_3:
        # for i in final_results_list_44:
        #     print(i)
        
        m="Pset_RailingCommon"
        for t in each_ifc_params_list_4:
    
             if m in t:
                ##print(t)
                final_results_list_4.append(t)


        # for b in final_results_list_4:
        #print(final_results_list_4)

              

    




#### step 5:
## reading the whole last param 

final_results_list_5=[]
test_list=[]


def search_ifc5():

    sharp="#"
    
    sharp_index_no_total=[]
    
    ## to extrct the no. of the main ifc line:
    for line in final_results_list_4:
         sharp_index_no=[]
         count_sharp=-1
         
         
         for n in line:
             count_sharp=count_sharp+1
             if n==sharp:
                 
                 sharp_index_no.append(count_sharp)
                 
                 
         sharp_index_no_total.append(sharp_index_no)
        


    ### here I will get the height and internal external position of the 
    counter=-1
    counter1=-1
    for q in final_results_list_4:


            ##print (q)

            temp_list=[0,0,0]
            counter=counter+1
            temp_list=[0,0,0]
            ##main line no.
            #print(q[sharp_index_no_total[counter][0]:sharp_index_no_total[counter][1]])
            a=q[sharp_index_no_total[counter][0]:sharp_index_no_total[counter][1]]
            temp_list[0]=a

            ##last param in the list
            ##list[-1] : get the last param in list

            m=q.index("Pset_RailingCommon")
            m=m+21
            x=sharp_index_no_total[counter]
            
            for p in x:
                 ##print(sharp_index_no_total[counter])
                 counter1=counter1+1
                 #print(p)
                 index=x.index(p)+1
                 ##print(counter1)
                 if p>m:
                     
                     ##getting first, secound,.. param in cell
                     ##print(len(x),index)
                     if index<len(x):
                         ## u is the #.. read from the params
                         u=q[p:x[index]-1]
                        


                         ###it will check to see if the lines has "IFCPOSITIVELENGTHMEASURE" or not. if they have it, it will be added to list
                         # number of the results 
                         count_wanted_ifc = -1

                         # get the lines content
                         founded_lines_list = []
                         founded_lines_list.clear()
                         everything="#"
                         

                         for line in f:
                                if everything in line:
                                    
                                    count_wanted_ifc += 1
                                    founded_lines_list.append(line)

                                    

                                    # get line no.
                                    selected_line = founded_lines_list[count_wanted_ifc]
                                    line_no1 = selected_line.index("#")
                                    line_no2 = selected_line.index("=")
                                    #print("Line no. (#...):")
                                    #print(selected_line[line_no1:line_no2])
                                    
                                    if u==selected_line[line_no1:line_no2]:
                                        
                                        ##check if the line contains the word of "IFCPOSITIVELENGTHMEASURE", then it will be the secound element in the list:
                                        if "IFCPOSITIVELENGTHMEASURE" in selected_line:
                                            ##print(selected_line)
                                            
                                            temp_list[1]=u


                                          ##check if the line contains the word of "IsExternal", then it will be the third element in the list::
                                        if "IsExternal" in selected_line:
                                            ##print(selected_line)
                                            
                                            temp_list[2]=u






                         
                        # print(u)
                 if index==len(x):
                     #print (index,len(x))
                     ##getting last param in last cell
                     b=q[sharp_index_no_total[counter][-1]:-4]
                     

                      ###it will check to see if the lines has "IFCPOSITIVELENGTHMEASURE" or not. if they have it, it will be added to list
                     # number of the results 
                     count_wanted_ifc = -1

                     # get the lines content
                     founded_lines_list = []
                     founded_lines_list.clear()
                     everything="#"
                    

                     for line in f:
                        if everything in line:
                                                    
                            count_wanted_ifc += 1
                            founded_lines_list.append(line)

                            

                            # get line no.
                            selected_line = founded_lines_list[count_wanted_ifc]
                            line_no1 = selected_line.index("#")
                            line_no2 = selected_line.index("=")
                            #print("Line no. (#...):")
                            #print(selected_line[line_no1:line_no2])
                            #print(b)
                            if b==selected_line[line_no1:line_no2]:
                                
                                ##check if the line contains the word of "IFCPOSITIVELENGTHMEASURE", then it will be the secound element in the list:
                                if "IFCPOSITIVELENGTHMEASURE" in selected_line:
                                   # print(selected_line)
                                    temp_list[1]=b

                                ##check if the line contains the word of "IsExternal", then it will be the third element in the list:
                                if "IsExternal" in selected_line:
                                   # print(selected_line)
                                    temp_list[2]=b



                       
                    
               

            #print(q[sharp_index_no_total[counter][-1]:-4])
            final_results_list_5.append(temp_list)
        
       
    #print(final_results_list_5)
      
 
####step 5_1
## finding the base point coordinates for Slab from slab line no.

def Railing_Bottom_Elevation(Line_no):




   ## getting first value - IFCLOCALPLACEMENT:
        Railing_Basepoint_height_1=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                
                if selected_line[line_no1:line_no2] == Line_no:
                         
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                         
                        ## here we are storing the first value
                         temp_list.append(selected_line[comma_indexes[4]+1 :comma_indexes[5]])
                         Railing_Basepoint_height_1.append(temp_list)
                         
        #print(Railing_Basepoint_height_1)



 ## getting secound value - IFCLOCALPLACEMENT:
        Railing_Basepoint_height_2=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                #print(Railing_Basepoint_height_1[0])
                #print(Railing_Basepoint_height_1[0][0])
                if selected_line[line_no1:line_no2] == Railing_Basepoint_height_1[0][0]:
                         
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                         
                        ## here we are storing the first value
                         temp_list.append(selected_line[selected_line.index("(#")+1 :comma_indexes[0]])
                         Railing_Basepoint_height_2.append(temp_list)
                         
        #print(Railing_Basepoint_height_2)

    

     ## getting third value - IFCLOCALPLACEMENT:
        Railing_Basepoint_height_3=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                #print(Railing_Basepoint_height_1[0])
                #print(Railing_Basepoint_height_1[0][0])
                if selected_line[line_no1:line_no2] == Railing_Basepoint_height_2[0][0]:
                         
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                         
                        ## here we are storing the first value
                         temp_list.append(selected_line[comma_indexes[0]+1 :selected_line.index(");")])
                         Railing_Basepoint_height_3.append(temp_list)
                         
        #print(Railing_Basepoint_height_3)





     ## getting fourth value - IFCAXISTOPLACEMENT:
        Railing_Basepoint_height_4=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                #print(Railing_Basepoint_height_1[0])
                #print(Railing_Basepoint_height_1[0][0])
                if selected_line[line_no1:line_no2] == Railing_Basepoint_height_3[0][0]:
                         
                         #print(selected_line[line_no1:line_no2])
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                        
                        ## here we are storing the first value
                         temp_list.append(selected_line[ selected_line.index("(#")+1:comma_indexes[0]])
                         Railing_Basepoint_height_4.append(temp_list)
                         
                         
        #print(Railing_Basepoint_height_4)






     ## getting fourth value - IFCCARTESIANPOINT:
        Railing_Basepoint_height_5=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                #print(Railing_Basepoint_height_1[0])
                #print(Railing_Basepoint_height_1[0][0])
                if selected_line[line_no1:line_no2] == Railing_Basepoint_height_4[0][0]:
                         
                         #print(selected_line[line_no1:line_no2])
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                        
                        ## here we are storing the first value
                         temp_list.append(selected_line[ comma_indexes[1]+1:selected_line.index("));")])
                         Railing_Basepoint_height_5.append(temp_list)
                         
                         
        #print(Railing_Basepoint_height_5)
        return Railing_Basepoint_height_5











##here i will get the base coordinate for the slab
def search_ifc5_2(Line_no):




   ## getting first value - IFCLOCALPLACEMENT:
        Slab_Basepoint_height_1=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                
                if selected_line[line_no1:line_no2] == Line_no:
                         
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                         
                        ## here we are storing the first value
                         temp_list.append(selected_line[comma_indexes[4]+1 :comma_indexes[5]])
                         Slab_Basepoint_height_1.append(temp_list)
                         
        #print(Slab_Basepoint_height_1)



 ## getting secound value - IFCLOCALPLACEMENT:
        Slab_Basepoint_height_2=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                #print(Railing_Basepoint_height_1[0])
                #print(Railing_Basepoint_height_1[0][0])
                if selected_line[line_no1:line_no2] == Slab_Basepoint_height_1[0][0]:
                         
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                         
                        ## here we are storing the first value
                         temp_list.append(selected_line[selected_line.index("(#")+1 :comma_indexes[0]])
                         Slab_Basepoint_height_2.append(temp_list)
                         
        #print(Slab_Basepoint_height_2)

    

     ## getting third value - IFCLOCALPLACEMENT:
        Slab_Basepoint_height_3=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                #print(Railing_Basepoint_height_1[0])
                #print(Railing_Basepoint_height_1[0][0])
                if selected_line[line_no1:line_no2] == Slab_Basepoint_height_2[0][0]:
                         
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                         
                        ## here we are storing the first value
                         temp_list.append(selected_line[comma_indexes[0]+1 :selected_line.index(");")])
                         Slab_Basepoint_height_3.append(temp_list)
                         
        #print(Slab_Basepoint_height_3)





     ## getting fourth value - IFCAXISTOPLACEMENT:
        Slab_Basepoint_height_4=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                #print(Railing_Basepoint_height_1[0])
                #print(Railing_Basepoint_height_1[0][0])
                if selected_line[line_no1:line_no2] == Slab_Basepoint_height_3[0][0]:
                         
                         #print(selected_line[line_no1:line_no2])
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                        
                        ## here we are storing the first value
                         temp_list.append(selected_line[ selected_line.index("(#")+1:comma_indexes[0]])
                         Slab_Basepoint_height_4.append(temp_list)
                         
                         
        #print(Slab_Basepoint_height_4)






     ## getting fourth value - IFCCARTESIANPOINT:
        Slab_Basepoint_height_5=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                #print(Railing_Basepoint_height_1[0])
                #print(Railing_Basepoint_height_1[0][0])
                if selected_line[line_no1:line_no2] == Slab_Basepoint_height_4[0][0]:
                         
                         #print(selected_line[line_no1:line_no2])
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                        
                        ## here we are storing the first value
                         temp_list.append(selected_line[ comma_indexes[1]+1:selected_line.index("));")])
                         Slab_Basepoint_height_5.append(temp_list)
                         
                         
        #print(Slab_Basepoint_height_5[0][0])
        return Slab_Basepoint_height_5[0][0]




















#### step 6:
##searching for lines containing height and checking it

final_results_list_6=[]
def search_ifc6 ():

        everything="#"
        
      
        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []
        founded_lines_list.clear()


        Final_result=[0,0,0,0,0,0,0]
        Final_Railing_Height=10000000
       
        w=0

        #list for each ifc that has been found to inject params:
        each_ifc_params_list_4=[]

        for line in f:
            if everything in line:
                
                count_wanted_ifc += 1
                founded_lines_list.append(line)

                

                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               # print(selected_line)
                # print("Line no. (#...):")
                # print(selected_line[line_no1:line_no2])
                for i in final_results_list_5:
                     ##print (final_results_list_5)

                     ## check to see if it is INTERMAL or EXTERNAL:
                     if i[2]==selected_line[line_no1:line_no2]:

                        #print(i[2],selected_line)
                        IsExternal_1= selected_line.index("IFCBOOLEAN(")
                        IsExternal_1=IsExternal_1+12
                        IsExternal_2=selected_line.index(".),")
                        ##print(selected_line[IsExternal_1:IsExternal_2])

                        ## check the height based on the input value in the beginig of the program:
                        if selected_line[IsExternal_1:IsExternal_2]=="T":
                               

                                 a= Railing_Story(str(i[0]));
                                 #print(a)
                                 if str(a).casefold() == "level -4" or str(a).casefold() == "level -3" or str(a).casefold() == "level -2" or str(a).casefold() == "level -1" or str(a).casefold() == "level 0" or str(a).casefold() == "level 1" or str(a).casefold() == "level 2" or str(a).casefold() == "level 3" or str(a).casefold()== "level 4" :
                                        






                                        ## see if the railing is in or near the slab:
                                        Railing_X_Y_Z=railing_x_y_z(i[0])
                                        Slab_X_Y_Z=Slab_x_y_z(i[0])
                                        #print(Slab_X_Y_Z)
                                        #print(Railing_X_Y_Z)
                                        # Slab_Xs=[]
                                        # Slab_Ys=[]
                                        # for o in range(0,len(Slab_X_Y_Z),1):

                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][2])
                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][4])
                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][6])
                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][8])
                                            
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][3])
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][5])
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][7])
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][9])      

                                        # #print(Slab_Ys)
                                             
                                        ##I did not read the last z here because the value was not in the range here, it may cause some problems in future
                                        Railing_Xs=[]
                                        Railing_Ys=[]
                                        Railing_Zs=[]
                                        for o in range(0,len(Railing_X_Y_Z)-1,1):
                                             
                                             Railing_Xs.append(Railing_X_Y_Z[o][0])
                                             Railing_Ys.append(Railing_X_Y_Z[o][1])
                                             Railing_Zs.append(Railing_X_Y_Z[o][2])
                                        #print(Railing_Xs)

                                        
                                        for o in range(0,len(Railing_Xs),1):

                                             for u in range(0, len(Slab_X_Y_Z), 1):
                                                 
                                                 
                                                 

                                                 
                                                
                                                 x_max_slab=max(float(Slab_X_Y_Z[u][2]),float(Slab_X_Y_Z[u][4]),float(Slab_X_Y_Z[u][6]),float(Slab_X_Y_Z[u][8]))
                                                 x_min_slab=min(float(Slab_X_Y_Z[u][2]),float(Slab_X_Y_Z[u][4]),float(Slab_X_Y_Z[u][6]),float(Slab_X_Y_Z[u][8]))
                                               
                                                 #print (x_min_slab,Slab_X_Y_Z[u][0])
                                                 y_min_slab=min(float(Slab_X_Y_Z[u][3]),float(Slab_X_Y_Z[u][5]),float(Slab_X_Y_Z[u][7]),float(Slab_X_Y_Z[u][9]))
                                                 y_max_slab=max(float(Slab_X_Y_Z[u][3]),float(Slab_X_Y_Z[u][5]),float(Slab_X_Y_Z[u][7]),float(Slab_X_Y_Z[u][9]))
                                                 #print(min(Railing_Xs))
                                                 


                                                 if float(Railing_Xs[o]) >= float(x_min_slab)-500  and float(Railing_Xs[o]) <= float(x_max_slab)+500:
                                                     #print(float(Railing_Xs[o]),"minnn:"+x_min_slab,"Maxxx:"+x_max_slab)
                                                     #print(Slab_X_Y_Z[u][0])
                                                     if float(Railing_Ys[o]) >= float(y_min_slab)-500  and float(Railing_Ys[o]) <= float(y_max_slab)+500:
                                                         #print(float(Railing_Ys[o]),"YYYminnn:"+y_min_slab,"YYYMaxxx:"+y_max_slab)
                                                            ##print(Slab_X_Y_Z[u][0])
                                                         if float(Slab_X_Y_Z[u][1])>=float(Railing_Zs[o]):
                                                                #print(Slab_X_Y_Z[u][1],Railing_Zs[o])


                                                                
                                                                everything_loop_2="#"
                                
                                                                # number of the results
                                                                count_wanted_ifc_loop_2 = -1

                                                                # get the lines content
                                                                founded_lines_list_loop_2 = []
                                                                founded_lines_list_loop_2.clear()


                                                                for line in f:
                                                                    if everything_loop_2 in line:
                                                                        
                                                                        count_wanted_ifc_loop_2 += 1
                                                                        founded_lines_list_loop_2.append(line)

                                                                        

                                                                        # get line no.
                                                                        selected_line_loop_2 = founded_lines_list_loop_2[count_wanted_ifc_loop_2]
                                                                        line_no1_loop_2 = selected_line_loop_2.index("#")
                                                                        line_no2_loop_2 = selected_line_loop_2.index("=")


                                                                        ## check the height based on the input value in the beginig of the program:
                                                                        if i[1]==selected_line_loop_2[line_no1_loop_2:line_no2_loop_2]:
                                                                            
                                                                        # print(i[1], selected_line_loop_2)
                                                                            Height_1= selected_line_loop_2.index("IFCPOSITIVELENGTHMEASURE")
                                                                            Height_1=Height_1+25
                                                                            Height_2= selected_line_loop_2.index("),")
                                                                     
                                                                           
                                                                            if float(Slab_X_Y_Z[u][1]) - float(Railing_X_Y_Z[o][2]) >=0:
                                                                                    p=float(Slab_X_Y_Z[u][1]) - float(Railing_X_Y_Z[o][2])
                                                                                    Final_Height_Railing=float(selected_line_loop_2[Height_1:Height_2]) - p 
                                                                                    if Final_Height_Railing < acceptable_height_2:
                                                                                            
                                                                                            ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is ---NOT Acceptable--- based on 'REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                           

                                                                                    if  Final_Height_Railing >= acceptable_height_2:
                                                                                         ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is Acceptable based on 'REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                          
                                                                                        

                                                                                
                                                                            


                                                                            if float(Slab_X_Y_Z[u][1]) - float(Railing_X_Y_Z[o][2]) <0:
                                                                                    
                                                                                    Final_Height_Railing=float(selected_line_loop_2[Height_1:Height_2]) 
                                                                                    if Final_Height_Railing < acceptable_height_2:
                                                                                            
                                                                                            ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is ---NOT Acceptable--- based on 'REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                          

                                                                                    if Final_Height_Railing >= acceptable_height_2:
                                                                                        ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is Acceptable based on 'REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                       



                                                         else:

                                                              Final_result[0]="Error in Design for railing with GUID "+railing_Guid(str(i[0])) +"!  -- the railing is not attached to the slab!--"+"\n"+"\n"+"\n"+"\n"
                                                                                

                                        print("\n"+"\n"+str(Final_result[0])+ str(Final_result[3]) + str(Final_result[2])+str(Final_result[4])+ str(Final_result[1]))
                                        Final_result[0]=""
                                        Final_result[1]=""
                                        Final_result[2]=""
                                        Final_result[3]=""
                                        Final_result[4]=""










                                 else:

                             


                                        ## see if the railing is in or near the slab:
                                        Railing_X_Y_Z=railing_x_y_z(i[0])
                                        Slab_X_Y_Z=Slab_x_y_z(i[0])
                                        #print(Slab_X_Y_Z)
                                        #print(Railing_X_Y_Z)
                                        # Slab_Xs=[]
                                        # Slab_Ys=[]
                                        # for o in range(0,len(Slab_X_Y_Z),1):

                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][2])
                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][4])
                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][6])
                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][8])
                                            
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][3])
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][5])
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][7])
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][9])      

                                        # #print(Slab_Ys)
                                             
                                        ##I did not read the last z here because the value was not in the range here, it may cause some problems in future
                                        Railing_Xs=[]
                                        Railing_Ys=[]
                                        Railing_Zs=[]
                                        for o in range(0,len(Railing_X_Y_Z)-1,1):
                                             
                                             Railing_Xs.append(Railing_X_Y_Z[o][0])
                                             Railing_Ys.append(Railing_X_Y_Z[o][1])
                                             Railing_Zs.append(Railing_X_Y_Z[o][2])
                                        #print(Railing_Xs)

                                        
                                        for o in range(0,len(Railing_Xs),1):

                                             for u in range(0, len(Slab_X_Y_Z), 1):
                                                 
                                                 
                                                 

                                                 
                                                
                                                 x_max_slab=max(float(Slab_X_Y_Z[u][2]),float(Slab_X_Y_Z[u][4]),float(Slab_X_Y_Z[u][6]),float(Slab_X_Y_Z[u][8]))
                                                 x_min_slab=min(float(Slab_X_Y_Z[u][2]),float(Slab_X_Y_Z[u][4]),float(Slab_X_Y_Z[u][6]),float(Slab_X_Y_Z[u][8]))
                                               
                                                 #print (x_min_slab,Slab_X_Y_Z[u][0])
                                                 y_min_slab=min(float(Slab_X_Y_Z[u][3]),float(Slab_X_Y_Z[u][5]),float(Slab_X_Y_Z[u][7]),float(Slab_X_Y_Z[u][9]))
                                                 y_max_slab=max(float(Slab_X_Y_Z[u][3]),float(Slab_X_Y_Z[u][5]),float(Slab_X_Y_Z[u][7]),float(Slab_X_Y_Z[u][9]))
                                                 #print(min(Railing_Xs))
                                                 


                                                 if float(Railing_Xs[o]) >= float(x_min_slab)-500  and float(Railing_Xs[o]) <= float(x_max_slab)+500:
                                                    
                                                     #print(Slab_X_Y_Z[u][0])
                                                     if float(Railing_Ys[o]) >= float(y_min_slab)-500  and float(Railing_Ys[o]) <= float(y_max_slab)+500:
                                                         #print(float(Railing_Ys[o]),"YYYminnn:"+y_min_slab,"YYYMaxxx:"+y_max_slab)
                                                            ##print(Slab_X_Y_Z[u][0])
                                                         if float(Slab_X_Y_Z[u][1])>=float(Railing_Zs[o]):
                                                                #print(Slab_X_Y_Z[u][1],Railing_Zs[o])


                                                                
                                                                everything_loop_2="#"
                                
                                                                # number of the results
                                                                count_wanted_ifc_loop_2 = -1

                                                                # get the lines content
                                                                founded_lines_list_loop_2 = []
                                                                founded_lines_list_loop_2.clear()


                                                                for line in f:
                                                                    if everything_loop_2 in line:
                                                                        
                                                                        count_wanted_ifc_loop_2 += 1
                                                                        founded_lines_list_loop_2.append(line)

                                                                        

                                                                        # get line no.
                                                                        selected_line_loop_2 = founded_lines_list_loop_2[count_wanted_ifc_loop_2]
                                                                        line_no1_loop_2 = selected_line_loop_2.index("#")
                                                                        line_no2_loop_2 = selected_line_loop_2.index("=")


                                                                        ## check the height based on the input value in the beginig of the program:
                                                                        if i[1]==selected_line_loop_2[line_no1_loop_2:line_no2_loop_2]:
                                                                            
                                                                        # print(i[1], selected_line_loop_2)
                                                                            Height_1= selected_line_loop_2.index("IFCPOSITIVELENGTHMEASURE")
                                                                            Height_1=Height_1+25
                                                                            Height_2= selected_line_loop_2.index("),")
                                                                           

                                                                            if float(Slab_X_Y_Z[u][1]) - float(Railing_X_Y_Z[o][2]) >=0:
                                                                                    p=float(Slab_X_Y_Z[u][1]) - float(Railing_X_Y_Z[o][2])
                                                                                    Final_Height_Railing=float(selected_line_loop_2[Height_1:Height_2]) - p 
                                                                                    if Final_Height_Railing < acceptable_height_2:
                                                                                            
                                                                                            ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is ---NOT Acceptable--- based on 'REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                         

                                                                                    if  Final_Height_Railing >= acceptable_height_2:
                                                                                         ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is Acceptable based on 'REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                        

                                                                                
                                                                            


                                                                            if float(Slab_X_Y_Z[u][1]) - float(Railing_X_Y_Z[o][2]) <0:
                                                                                    
                                                                                    Final_Height_Railing=float(selected_line_loop_2[Height_1:Height_2]) 
                                                                                    if Final_Height_Railing < acceptable_height_2:
                                                                                            
                                                                                            ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is ---NOT Acceptable--- based on 'REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                            

                                                                                    if Final_Height_Railing >= acceptable_height_2:
                                                                                        ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is Acceptable based on 'REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                        


                                                         else:
                                                              Final_result[0]="Error in Design for railing with GUID "+railing_Guid(str(i[0])) +"!  -- the railing is not attached to the slab!--"+"\n"+"\n"+"\n"+"\n"
                        


                                        print("\n"+"\n"+str(Final_result[0])+ str(Final_result[3]) + str(Final_result[2])+str(Final_result[4])+ str(Final_result[1]))
                                        Final_result[0]=""
                                        Final_result[1]=""
                                        Final_result[2]=""
                                        Final_result[3]=""
                                        Final_result[4]=""

                               



                                 






                             

                       




                        if selected_line[IsExternal_1:IsExternal_2]=="F":
                               




                                 a= Railing_Story(str(i[0]));
                                 #print(a)
                                 #str(a[0]).casefold() == "Level -4" or str(a[0]).casefold() == "Level -3" or str(a[0]).casefold() == "Level -2" or str(a[0]).casefold() == "Level -1" or str(a[0]).casefold() == "Level 0" or str(a[0]).casefold() == "Level 1" or str(a[0]).casefold() == "Level 2" or str(a[0]).casefold() == "Level 3" or 
                                 
                                 if str(a).casefold() == "level -4" or str(a).casefold() == "level -3" or str(a).casefold() == "level -2" or str(a).casefold() == "level -1" or str(a).casefold() == "level 0" or str(a).casefold() == "level 1" or str(a).casefold() == "level 2" or str(a).casefold() == "level 3" or str(a).casefold()== "level 4" :
                                        






                                        
                                        ## see if the railing is in or near the slab:
                                        Railing_X_Y_Z=railing_x_y_z(i[0])
                                        Slab_X_Y_Z=Slab_x_y_z(i[0])
                                        #print(Slab_X_Y_Z)
                                        #print(Railing_X_Y_Z)
                                        # Slab_Xs=[]
                                        # Slab_Ys=[]
                                        # for o in range(0,len(Slab_X_Y_Z),1):

                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][2])
                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][4])
                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][6])
                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][8])
                                            
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][3])
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][5])
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][7])
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][9])      

                                        # #print(Slab_Ys)
                                             
                                        ##I did not read the last z here because the value was not in the range here, it may cause some problems in future
                                        Railing_Xs=[]
                                        Railing_Ys=[]
                                        Railing_Zs=[]
                                        for o in range(0,len(Railing_X_Y_Z)-1,1):
                                             
                                             Railing_Xs.append(Railing_X_Y_Z[o][0])
                                             Railing_Ys.append(Railing_X_Y_Z[o][1])
                                             Railing_Zs.append(Railing_X_Y_Z[o][2])
                                        #print(Railing_Xs)

                                        
                                        for o in range(0,len(Railing_Xs),1):

                                             for u in range(0, len(Slab_X_Y_Z), 1):
                                                 
                                                 
                                                 

                                                 
                                                
                                                 x_max_slab=max(float(Slab_X_Y_Z[u][2]),float(Slab_X_Y_Z[u][4]),float(Slab_X_Y_Z[u][6]),float(Slab_X_Y_Z[u][8]))
                                                 x_min_slab=min(float(Slab_X_Y_Z[u][2]),float(Slab_X_Y_Z[u][4]),float(Slab_X_Y_Z[u][6]),float(Slab_X_Y_Z[u][8]))
                                               
                                                 #print (x_min_slab,Slab_X_Y_Z[u][0])
                                                 y_min_slab=min(float(Slab_X_Y_Z[u][3]),float(Slab_X_Y_Z[u][5]),float(Slab_X_Y_Z[u][7]),float(Slab_X_Y_Z[u][9]))
                                                 y_max_slab=max(float(Slab_X_Y_Z[u][3]),float(Slab_X_Y_Z[u][5]),float(Slab_X_Y_Z[u][7]),float(Slab_X_Y_Z[u][9]))
                                                 #print(min(Railing_Xs))
                                                 


                                                 if float(Railing_Xs[o]) >= float(x_min_slab)-500  and float(Railing_Xs[o]) <= float(x_max_slab)+500:
                                                   
                                                     #print(Slab_X_Y_Z[u][0])
                                                     if float(Railing_Ys[o]) >= float(y_min_slab)-500  and float(Railing_Ys[o]) <= float(y_max_slab)+500:
                                                       
                                                        #print((Slab_X_Y_Z[u][1]),float(Railing_Zs[o]))
                                                         if float(Slab_X_Y_Z[u][1])>=float(Railing_Zs[o]):
                                                            


                                                                
                                                                everything_loop_2="#"
                                
                                                                # number of the results
                                                                count_wanted_ifc_loop_2 = -1

                                                                # get the lines content
                                                                founded_lines_list_loop_2 = []
                                                                founded_lines_list_loop_2.clear()


                                                                for line in f:
                                                                    if everything_loop_2 in line:
                                                                        
                                                                        count_wanted_ifc_loop_2 += 1
                                                                        founded_lines_list_loop_2.append(line)

                                                                        

                                                                        # get line no.
                                                                        selected_line_loop_2 = founded_lines_list_loop_2[count_wanted_ifc_loop_2]
                                                                        line_no1_loop_2 = selected_line_loop_2.index("#")
                                                                        line_no2_loop_2 = selected_line_loop_2.index("=")


                                                                        ## check the height based on the input value in the beginig of the program:
                                                                        if i[1]==selected_line_loop_2[line_no1_loop_2:line_no2_loop_2]:
                                                                            
                                                                           # print(i[1], selected_line_loop_2)
                                                                            Height_1= selected_line_loop_2.index("IFCPOSITIVELENGTHMEASURE")
                                                                            Height_1=Height_1+25
                                                                            Height_2= selected_line_loop_2.index("),")
                                                                           
                                                                            #print((Slab_X_Y_Z[u][1]) , float(Railing_X_Y_Z[o][2]))
                                                                            if float(Slab_X_Y_Z[u][1]) - float(Railing_X_Y_Z[o][2]) >=0:
                                                                                    
                                                                                    p=float(Slab_X_Y_Z[u][1]) - float(Railing_X_Y_Z[o][2])
                                                                                    Final_Height_Railing=float(selected_line_loop_2[Height_1:Height_2]) - p 
                                                                                    
                                                                                    if Final_Height_Railing < acceptable_height_1:
                                                                                            
                                                                                            ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is ---NOT Acceptable--- 'based on REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                         
                                                                                            

                                                                                    if  Final_Height_Railing >= acceptable_height_1:
                                                                                         ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is Acceptable based on 'REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                           
                                                                                           

                                                                                
                                                                            


                                                                            if float(Slab_X_Y_Z[u][1]) - float(Railing_X_Y_Z[o][2]) <0:
                                                                                
                                                                                    
                                                                                    Final_Height_Railing=float(selected_line_loop_2[Height_1:Height_2]) 
                                                                                    if Final_Height_Railing < acceptable_height_1:
                                                                                            
                                                                                            ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is ---NOT Acceptable--- based on 'REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                           

                                                                                    if Final_Height_Railing >= acceptable_height_1:
                                                                                        ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is Acceptable based on 'REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                           


                                                         else:
                                                            
                                                              Final_result[0]="Error in Design for railing with GUID "+railing_Guid(str(i[0])) +"!  -- the railing is not attached to the slab!--"+"\n"+"\n"+"\n"+"\n"
                                                              

                                        print("\n"+"\n"+str(Final_result[0])+ str(Final_result[3]) + str(Final_result[2])+str(Final_result[4])+ str(Final_result[1]))
                                        Final_result[0]=""
                                        Final_result[1]=""
                                        Final_result[2]=""
                                        Final_result[3]=""
                                        Final_result[4]=""



                                 else:

                             


                                        ## see if the railing is in or near the slab:
                                        Railing_X_Y_Z=railing_x_y_z(i[0])
                                        Slab_X_Y_Z=Slab_x_y_z(i[0])
                                        #print(Slab_X_Y_Z)
                                        #print(Railing_X_Y_Z)
                                        # Slab_Xs=[]
                                        # Slab_Ys=[]
                                        # for o in range(0,len(Slab_X_Y_Z),1):

                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][2])
                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][4])
                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][6])
                                        #      Slab_Xs[1].append(Slab_X_Y_Z[o][8])
                                            
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][3])
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][5])
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][7])
                                        #      Slab_Ys.append(Slab_X_Y_Z[o][9])      

                                        # #print(Slab_Ys)
                                             
                                        ##I did not read the last z here because the value was not in the range here, it may cause some problems in future
                                        Railing_Xs=[]
                                        Railing_Ys=[]
                                        Railing_Zs=[]
                                        for o in range(0,len(Railing_X_Y_Z)-1,1):
                                             
                                             Railing_Xs.append(Railing_X_Y_Z[o][0])
                                             Railing_Ys.append(Railing_X_Y_Z[o][1])
                                             Railing_Zs.append(Railing_X_Y_Z[o][2])
                                        #print(Railing_X_Y_Z[o])

                                        
                                        for o in range(0,len(Railing_Xs),1):

                                             for u in range(0, len(Slab_X_Y_Z), 1):
                                                 
                                                 
                                                 

                                                 
                                                
                                                 x_max_slab=max(float(Slab_X_Y_Z[u][2]),float(Slab_X_Y_Z[u][4]),float(Slab_X_Y_Z[u][6]),float(Slab_X_Y_Z[u][8]))
                                                 x_min_slab=min(float(Slab_X_Y_Z[u][2]),float(Slab_X_Y_Z[u][4]),float(Slab_X_Y_Z[u][6]),float(Slab_X_Y_Z[u][8]))
                                               
                                                 #print (x_min_slab,Slab_X_Y_Z[u][0])
                                                 y_min_slab=min(float(Slab_X_Y_Z[u][3]),float(Slab_X_Y_Z[u][5]),float(Slab_X_Y_Z[u][7]),float(Slab_X_Y_Z[u][9]))
                                                 y_max_slab=max(float(Slab_X_Y_Z[u][3]),float(Slab_X_Y_Z[u][5]),float(Slab_X_Y_Z[u][7]),float(Slab_X_Y_Z[u][9]))
                                                 #print(min(Railing_Xs))
                                                 


                                                 if float(Railing_Xs[o]) >= float(x_min_slab)-500  and float(Railing_Xs[o]) <= float(x_max_slab)+500:
                                                  
                                                     #print(Slab_X_Y_Z[u][0])
                                                     if float(Railing_Ys[o]) >= float(y_min_slab)-500  and float(Railing_Ys[o]) <= float(y_max_slab)+500:
                                                       
                                                            ##print(Slab_X_Y_Z[u][0])
                                                         if float(Slab_X_Y_Z[u][1])>=float(Railing_Zs[o]):
                                                                #print(Slab_X_Y_Z[u][1],Railing_Zs[o])


                                                                
                                                                everything_loop_2="#"
                                
                                                                # number of the results
                                                                count_wanted_ifc_loop_2 = -1

                                                                # get the lines content
                                                                founded_lines_list_loop_2 = []
                                                                founded_lines_list_loop_2.clear()


                                                                for line in f:
                                                                    if everything_loop_2 in line:
                                                                        
                                                                        count_wanted_ifc_loop_2 += 1
                                                                        founded_lines_list_loop_2.append(line)

                                                                        

                                                                        # get line no.
                                                                        selected_line_loop_2 = founded_lines_list_loop_2[count_wanted_ifc_loop_2]
                                                                        line_no1_loop_2 = selected_line_loop_2.index("#")
                                                                        line_no2_loop_2 = selected_line_loop_2.index("=")


                                                                        ## check the height based on the input value in the beginig of the program:
                                                                        if i[1]==selected_line_loop_2[line_no1_loop_2:line_no2_loop_2]:
                                                                            
                                                                        # print(i[1], selected_line_loop_2)
                                                                            Height_1= selected_line_loop_2.index("IFCPOSITIVELENGTHMEASURE")
                                                                            Height_1=Height_1+25
                                                                            Height_2= selected_line_loop_2.index("),")
                                                                           



                                                                            if float(Slab_X_Y_Z[u][1]) - float(Railing_X_Y_Z[o][2]) >=0:
                                                                                    p=float(Slab_X_Y_Z[u][1]) - float(Railing_X_Y_Z[o][2])
                                                                                    Final_Height_Railing=float(selected_line_loop_2[Height_1:Height_2]) - p 
                                                                                    if Final_Height_Railing < acceptable_height_2:
                                                                                            
                                                                                            ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is ---NOT Acceptable--- based on 'REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                           

                                                                                    if  Final_Height_Railing >= acceptable_height_2:
                                                                                         ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is Acceptable based on 'REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                          

                                                                                
                                                                            


                                                                            if float(Slab_X_Y_Z[u][1]) - float(Railing_X_Y_Z[o][2]) <0:
                                                                                    
                                                                                    Final_Height_Railing=float(selected_line_loop_2[Height_1:Height_2]) 
                                                                                    if Final_Height_Railing < acceptable_height_2:
                                                                                            
                                                                                            ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is ---NOT Acceptable--- based on 'REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                          

                                                                                    if Final_Height_Railing >= acceptable_height_2:
                                                                                        ##line no. of railing
                                                                                            Final_result[0]="Ralining Type Name => "+ railing_Name(str(i[0])) +"\n"
                                                                                            Final_result[3]="Ralining GUID => "+ railing_Guid(str(i[0])) +"\n"
                                                                                            Final_result[2]="Final Height => "+str(Final_Height_Railing)+"\n"
                                                                                            Final_result[4]="Railing Level => "+a+"\n"
                                                                                            Final_result[1]="Status of Railing => Is Acceptable based on 'REGLEMENT SUR LES BATISSES VILLE DE LUXEMBOURG, SECTION 8'"+"\n"+"\n"+"\n"

                                                                                         

                                                         else:
                                                              Final_result[0]="Error in Design for railing with GUID "+railing_Guid(str(i[0])) +"!  -- the railing is not attached to the slab!--"+"\n"+"\n"+"\n"+"\n"


                                        print("\n"+"\n"+str(Final_result[0])+ str(Final_result[3]) + str(Final_result[2])+str(Final_result[4])+ str(Final_result[1]))
                                        Final_result[0]=""
                                        Final_result[1]=""
                                        Final_result[2]=""
                                        Final_result[3]=""
                                        Final_result[4]=""


                                                                     







#### step 7:
#### getting the x y z of the railing:

def railing_x_y_z(line_num_of_railing) :


        ## getting 7th cell:
        seventh_cell_value=""



        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                
                if selected_line[line_no1:line_no2] == line_num_of_railing:
                     x=","
                     y=-1
                     comma_indexes=[]
                     for i in selected_line:
                        y=y+1

                        if x==i:
                           
                            comma_indexes.append(y)

                     seventh_cell_value=selected_line[comma_indexes[5]+1:comma_indexes[6]]
                     #print(seventh_cell_value)




        ##getting the third value:

      
        third_cell_value=""

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                
                if selected_line[line_no1:line_no2] == seventh_cell_value:
                     x=","
                     y=-1
                     comma_indexes=[]
                     for i in selected_line:
                        y=y+1

                        if x==i:
                           
                            comma_indexes.append(y)
                     
                     third_cell_value=selected_line[comma_indexes[1]+2:selected_line.index("));")]
                     #print(third_cell_value)

                        



        ## getting all fourth values:
        fourth_cell_value=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                
                if selected_line[line_no1:line_no2] == third_cell_value:
                     x=","
                     y=-1
                     comma_indexes=[]
                     for i in selected_line:
                        y=y+1

                        if x==i:
                           
                            comma_indexes.append(y)


                     ##Adding all fouth cell parameters in a list
                     
                     i=0
                     for i in range(2,len(comma_indexes),1):
                        
                        if i+1<len(comma_indexes):
                            ##following if is only for reading first value then the rest:
                            if i+1==3:
                                fourth_cell_value.append(selected_line[comma_indexes[i]+2:comma_indexes[i+1]])
                            else:    
                                fourth_cell_value.append(selected_line[comma_indexes[i]+1:comma_indexes[i+1]])                        

                            
                        if i+1==len(comma_indexes):
                            fourth_cell_value.append(selected_line[comma_indexes[i]+1:selected_line.index("));")])
                            
                    
                     #print(fourth_cell_value)







        ##getting the secound value:

      
        secound_cell_value=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                for j in range(0,len(fourth_cell_value),1):

                    if selected_line[line_no1:line_no2] == fourth_cell_value[j]:
                        #print(selected_line)                 
                        x=","
                        y=-1
                        comma_indexes=[]
                        for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                        #print(selected_line[comma_indexes[0]+1:comma_indexes[1]])
                        secound_cell_value.append(selected_line[comma_indexes[0]+1:comma_indexes[1]])


        #print(secound_cell_value)




        ## get the first value:
        
        first_cell_value=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                for u in range(0,len(secound_cell_value),1):

                     if selected_line[line_no1:line_no2] == secound_cell_value[u]:
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                        
                         first_cell_value.append(selected_line[selected_line.index("(#")+1:comma_indexes[0]])
        #print(first_cell_value)

              

 ## get x y z for each part of the railing:
        
        x_y_z=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                for u in range(0,len(first_cell_value),1):

                     if selected_line[line_no1:line_no2] == first_cell_value[u]:
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                         #print(selected_line)
                         temp_list.append(selected_line[selected_line.index("((")+2:comma_indexes[0]])
                         temp_list.append(selected_line[comma_indexes[0]+1:comma_indexes[1]])
                         temp_list.append(selected_line[comma_indexes[1]+1:selected_line.index("))")])
                         x_y_z.append(temp_list)


        #print(x_y_z)


        ##now i will use ifc_search5_1 to add the base height to height of railing to find the global bottom height:
       
        a=Railing_Bottom_Elevation(line_num_of_railing)
        
       
       
        for u in range(0,len(x_y_z),1):

            x_y_z[u][2]=float(x_y_z[u][2])+float(a[0][0])

        #print(x_y_z)
        return x_y_z




#### Step 8:
##getting slabs x,y,z:
                      
def Slab_x_y_z(Line_no):


        ##getting all IFCRELCONTAINEDINSPATIALSTRUCTURE:

        fifth_cell_value0=[]
        fifth_cell_value1=[]
  

        ifc_slabs=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"

        
        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                selected_line = founded_lines_list[count_wanted_ifc]

                ##getting all "," indexes:
                
                if "IFCRELCONTAINEDINSPATIALSTRUCTURE" in selected_line:
                     
                     
                     # get line no. of related slabs:
                     
                     line_no1 = selected_line.index("#")
                     line_no2 = selected_line.index("=")
                     

                     x=","
                     y=-1
                     comma_indexes=[]
                     tempL=[]
                     for i in selected_line:
                        y=y+1

                        if x==i:
                           
                            comma_indexes.append(y)




                     #fifth_cell_value0.append(selected_line[comma_indexes[3]+1:comma_indexes[-1]])
                     tempL.append((selected_line[comma_indexes[3]+1:comma_indexes[-1]]))
                     fifth_cell_value0.append(tempL)

        #print(fifth_cell_value0)     
                   
                    





        



        


        #print(Line_no)

        for u in range(0,len(fifth_cell_value0),1):

             if Line_no in str(fifth_cell_value0[u]):
                     #print(fifth_cell_value0[u])
                


                     x="#"
                     y=-1
                     hashtag_indexes=[]
                     temp=[]
                     for i in str(fifth_cell_value0[u]):
                        y=y+1
                    

                        if x==i:
                           
                            hashtag_indexes.append(y)


                     #print(hashtag_indexes)



                     for o in range(0,len(hashtag_indexes),1):

                         if o==len(hashtag_indexes)-1:
                             
                             if str(fifth_cell_value0[u])[hashtag_indexes[o]:str(fifth_cell_value0[u]).index(")")] != Line_no:
                                 fifth_cell_value1.append(str(fifth_cell_value0[u])[hashtag_indexes[o]:str(fifth_cell_value0[u]).index(")")])
                            # print(str(fifth_cell_value0[u])[hashtag_indexes[o]:str(fifth_cell_value0[u]).index(")")])


                         else:
                            m=hashtag_indexes[o+1]-1
                            if str(fifth_cell_value0[u])[hashtag_indexes[o]:m] != Line_no:
                                fifth_cell_value1.append(str(fifth_cell_value0[u])[hashtag_indexes[o]:m])

                             #print(str(fifth_cell_value0[u])[hashtag_indexes[o]:hashtag_indexes[o+1]])
                            





       # print(fifth_cell_value1)




        fifth_cell_value=[]

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
            
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
            

                ##getting all "," indexes:
                for u in range(0,len(fifth_cell_value1),1):

                    if selected_line[line_no1:line_no2] == fifth_cell_value1[u]:

                        if "IFCSLAB" in selected_line:
                            
                            ifc_slabs.append(fifth_cell_value1[u])
                                



   




        ## getting 7th value:
        slab_7_value=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                for u in range(0,len(ifc_slabs),1):

                     if selected_line[line_no1:line_no2] == ifc_slabs[u]:
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                        
                        ## we have line no. for the slab then the 7th value of that
                         temp_list.append(ifc_slabs[u])
                         temp_list.append(selected_line[comma_indexes[5]+1:comma_indexes[6]])
                         slab_7_value.append(temp_list)
                         
        #print(slab_7_value)





     ## getting 3th value:
        slab_3_value=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                for u in range(0,len(slab_7_value),1):
                     #print(slab_7_value)

                     if selected_line[line_no1:line_no2] == slab_7_value[u][1]:
                         
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                         #print(selected_line)
                        ## here we are storing the 3th value which containes 2 values
                         temp_list.append(slab_7_value[u][0])
                         temp_list.append(selected_line[comma_indexes[1]+2:comma_indexes[2]])
                         temp_list.append(selected_line[comma_indexes[2]+1:selected_line.index("));")])
                         slab_3_value.append(temp_list)
                         
       # print(slab_3_value)


   ## getting last cell value if the line containes "footprint":
        slab_last_value=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                for u in range(0,len(slab_3_value),1):
                     ## finding the ones containing "footprint":
                     ##first checking the first one:
                     if selected_line[line_no1:line_no2] == slab_3_value[u][1] :
                         
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                        
                        ## here we are storing the last cell value if the line containes "footprint"
                         d="FootPrint"
                         if d in selected_line:
                             #print(selected_line)
                             temp_list.append(slab_3_value[u][0])
                             temp_list.append(selected_line[comma_indexes[2]+1:selected_line.index("));")])
                             slab_last_value.append(temp_list)


                            
                             ##using function "slab_z" to add the height to last cell
                             t=Slab_z(slab_3_value[u][2])
                             temp_list.append(t)

                             slab_last_value.append(temp_list)


                             
                             




                        ##then checking the secound one:
                     if selected_line[line_no1:line_no2] == slab_3_value[u][2] :
                         
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                        
                        ## here we are storing the last cell value if the line containes "footprint"
                         d="FootPrint"
                         if d in selected_line:
                             #print(selected_line)
                             temp_list.append(slab_3_value[u][0])
                             temp_list.append(selected_line[comma_indexes[2]+2:selected_line.index("));")])
                             
                            ##using function "slab_z" to add the height to last cell
                             t=Slab_z(slab_3_value[u][1])
                             temp_list.append(t)

                             slab_last_value.append(temp_list)



                         
                         
        #print(slab_last_value)




        


        ## getting first value:
        slab_1_value=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                for u in range(0,len(slab_last_value),1):

                     if selected_line[line_no1:line_no2] == slab_last_value[u][1]:
                         
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                         
                        ## here we are storing the first value
                         temp_list.append(slab_last_value[u][0])
                         temp_list.append(selected_line[selected_line.index("(#")+1 :comma_indexes[0]])
                         temp_list.append(slab_last_value[u][2])
                         slab_1_value.append(temp_list)
                         
        #print(slab_1_value)

                                            




        ## getting X and Y of slab:
        slab_xy_value=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                for u in range(0,len(slab_last_value),1):
                    
 
                     if selected_line[line_no1:line_no2] == slab_1_value[u][1]:
                        # print(selected_line,slab_1_value[u][1])
                         
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                        
                        ## here we are storing the line no., X and Y values of slabs
                         temp_list.append(slab_1_value[u][0])
                         ##height of surface slab
                         temp_list.append(slab_1_value[u][2])
                         temp_list.append(selected_line[selected_line.index("(((")+3 :comma_indexes[0]])
                         temp_list.append(selected_line[comma_indexes[0]+1 :comma_indexes[1]-1])
                         temp_list.append(selected_line[comma_indexes[1]+2 :comma_indexes[2]])
                         temp_list.append(selected_line[comma_indexes[2]+1 :comma_indexes[3]-1])
                         temp_list.append(selected_line[comma_indexes[3]+2 :comma_indexes[4]])
                         temp_list.append(selected_line[comma_indexes[4]+1 :comma_indexes[5]-1])
                         temp_list.append(selected_line[comma_indexes[5]+2 :comma_indexes[6]])
                         temp_list.append(selected_line[comma_indexes[6]+1 :comma_indexes[7]-1])
                         slab_xy_value.append(temp_list)
                         
        #print(slab_xy_value)


        ## here i will add the base point height to the thickness of the slab to get the global top point heght of the slab
        for u in range(0,len(slab_xy_value),1):

            slab_xy_value[u][1]=float(slab_xy_value[u][1])+float(search_ifc5_2(slab_xy_value[u][0]))
            #print(slab_xy_value[u][1])



        #print(slab_xy_value)
        return slab_xy_value

                        

                    


    #geting the z value of the slab from IFCSHAPEREPRESENTATION step

def Slab_z (Line_no):




   ## getting first value:
        slab_z_value_lastcell=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
               

                ##getting all "," indexes:
                
                if selected_line[line_no1:line_no2] == Line_no:
                         
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                         
                        ## here we are storing the first value
                         temp_list.append(selected_line[comma_indexes[2]+2 :selected_line.index("));")])
                         slab_z_value_lastcell.append(temp_list)
                         
        #print(slab_z_value_lastcell)





        ## Getting IFCAXISTOPLACEMENT
        ## getting first value:
        slab_z_value_IFCAXISTOPLACEMENT=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
                
               

                ##getting all "," indexes:
                for u in range(0,len(slab_z_value_lastcell),1):
                    
                     if selected_line[line_no1:line_no2] == slab_z_value_lastcell[u][0]:
                         
                        
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                         
                        ## here we are storing the first value
                         
                         temp_list.append(selected_line[comma_indexes[0]+1 :comma_indexes[1]])
                         slab_z_value_IFCAXISTOPLACEMENT.append(temp_list)
                         
        #print(slab_z_value_IFCAXISTOPLACEMENT)


    




        ## Getting IFCCARTESIANPOINT
        ## getting first value:
        slab_z_value_IFCCARTESIANPOINT=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
                
               

                ##getting all "," indexes:
                for u in range(0,len(slab_z_value_IFCAXISTOPLACEMENT),1):
                    
                     if selected_line[line_no1:line_no2] == slab_z_value_IFCAXISTOPLACEMENT[u][0]:
                         
                        
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                         
                        ## here we are storing the first value
                         
                         temp_list.append(selected_line[selected_line.index("(#")+1 :comma_indexes[0]])
                         slab_z_value_IFCCARTESIANPOINT.append(temp_list)
                         
        #print(slab_z_value_IFCCARTESIANPOINT)









        ## Getting slab top hight
        ## getting first value:
        slab_z_value_ontop=[]

        # number of the results
        count_wanted_ifc = -1

        # get the lines content
        founded_lines_list = []

        wanted_ifc="#"


        for line in f:
            if wanted_ifc in line:
                count_wanted_ifc += 1
                founded_lines_list.append(line)
            
              
                # get line no.
                selected_line = founded_lines_list[count_wanted_ifc]
                line_no1 = selected_line.index("#")
                line_no2 = selected_line.index("=")
                
               

                ##getting all "," indexes:
                for u in range(0,len(slab_z_value_IFCCARTESIANPOINT),1):
                     
                     if selected_line[line_no1:line_no2] == slab_z_value_IFCCARTESIANPOINT[u][0]:
                         
                         
                         x=","
                         y=-1
                         comma_indexes=[]
                         temp_list=[]
                         for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                comma_indexes.append(y)
                         
                        ## here we are storing the first value
                         
                         temp_list.append(selected_line[comma_indexes[1]+1 :selected_line.index("));")])
                         slab_z_value_ontop.append(temp_list)
        #print(slab_z_value_ontop)                 
        return slab_z_value_ontop[0][0]
        










def Railing_Story (Line_no):




   ## getting first value:
        Railing_story=[]
        Railing_story2=0
        Railing_story3=0

        # number of the results
        count_wanted_ifc = -1
        count_wanted_ifc1 = -1
        # get the lines content
        founded_lines_list = []
        founded_lines_list1 = []

        wanted_ifc="#"
        IFC="IFCRELCONTAINEDINSPATIALSTRUCTURE"


        for line in f:
            if IFC in line:


              
                      count_wanted_ifc += 1
                      founded_lines_list.append(line)
            
              
                        # get line no.
                      selected_line = founded_lines_list[count_wanted_ifc]
                   
                      x=","
                      y=-1
                      comma_indexes=[]
                      temp_list1=[]
                      for i in selected_line:
                            y=y+1

                            if x==i:
                            
                                 comma_indexes.append(y)
                                 #print(selected_line)
                                 #print(comma_indexes)
                     ## here we are storing the first value
                      temp_list1.append(selected_line[selected_line.index("#"):selected_line.index("=")])
                      temp_list1.append(selected_line[comma_indexes[3]+2 :selected_line.index("),")])
                      Railing_story.append(temp_list1)

                      #print(Railing_story)

                      i1=-1
                      for i in range (0,len(Railing_story),1):
                         i1=i1+1
                         for p in range (0,len(Railing_story[i]),1):
                             #print(Railing_story[i][p])
                             if Line_no in  Railing_story[i][p]:
                                 #print(Railing_story[i][p],"77777")








                                   ## Getting slab top hight
                                    ## getting first value:
                                    

                                    # number of the results
                                    count_wanted_ifc1 = -1

                                    # get the lines content
                                    founded_lines_list1 = []

                                    wanted_ifc="#"


                                    for line in f:
                                        if wanted_ifc in line:
                                            count_wanted_ifc1 += 1
                                            founded_lines_list1.append(line)
                                        
                                        
                                            # get line no.
                                            selected_line1 = founded_lines_list1[count_wanted_ifc1]
                                            line_no1 = selected_line1.index("#")
                                            line_no2 = selected_line1.index("=")
                                            
                                        

                                            ##getting all "," indexes:
                                            
                                                
                                            if selected_line1[line_no1:line_no2] == Railing_story [i1][0]:
                                                
                                                
                                                x=","
                                                y=-1
                                                comma_indexes1=[]
                                                temp_list1=[]
                                                for i in selected_line1:
                                                    y=y+1

                                                    if x==i:
                                                    
                                                        comma_indexes1.append(y)
                                                
                                                ## here we are storing the first value
                                                
                                                Railing_story2=(selected_line1[selected_line1.index("),")+2 :selected_line1.index(");")])
                                                #print(Railing_story2)







                                                
                                            ## Getting slab top hight
                                                ## getting first value:
                                                

                                                # number of the results
                                                count_wanted_ifc11 = -1

                                                # get the lines content
                                                founded_lines_list11 = []

                                                wanted_ifc="#"


                                                for line in f:
                                                    if wanted_ifc in line:
                                                        count_wanted_ifc11 += 1
                                                        founded_lines_list11.append(line)
                                                    
                                                    
                                                        # get line no.
                                                        selected_line11 = founded_lines_list11[count_wanted_ifc11]
                                                        line_no11 = selected_line11.index("#")
                                                        line_no22 = selected_line11.index("=")
                                                        
                                                    

                                                        ##getting all "," indexes:
                                                        
                                                            
                                                        if selected_line11[line_no1:line_no22] == Railing_story2:
                                                            
                                                            
                                                            x=","
                                                            y=-1
                                                            comma_indexes11=[]
                                                            temp_list11=[]
                                                            for i in selected_line11:
                                                                y=y+1

                                                                if x==i:
                                                                
                                                                    comma_indexes11.append(y)
                                                            
                                                            ## here we are storing the first value
                                                            
                                                            Railing_story3=(selected_line11[comma_indexes11[1]+2 :comma_indexes11[2]-1])
                                                            #print(Railing_story3)







                             
    
        # print(Railing_story)
        # print(Railing_story2)
        #print(Railing_story3)
        return Railing_story3




def railing_Guid(Line_no):

      # number of the results
        count_wanted_ifc = -1
        Railing_Guid=[]
        # get the lines content
        founded_lines_list = []
        

        wanted_ifc="#"
   


        for line in f:
            if wanted_ifc in line:


              
                      count_wanted_ifc += 1
                      founded_lines_list.append(line)
            
              
                        # get line no.
                      selected_line = founded_lines_list[count_wanted_ifc]

                      
                     # get line no.
                    
                      line_no1 = selected_line.index("#")
                      line_no2 = selected_line.index("=")

                      if selected_line[line_no1:line_no2]==Line_no:
                        
                            x=","
                            y=-1
                            comma_indexes=[]
                            temp_list=[]
                            for i in selected_line:
                                    y=y+1

                                    if x==i:
                                    
                                        comma_indexes.append(y)
                                        #print(selected_line)
                                        #print(comma_indexes)
                            ## here we are storing the first value
                            #temp_list.append(selected_line[selected_line.index("(")+1:comma_indexes[0]])
                            Railing_Guid=selected_line[selected_line.index("(")+1:comma_indexes[0]]
            


        #print(Railing_Guid)
        return Railing_Guid








def railing_Name(Line_no):

      # number of the results
        count_wanted_ifc = -1
        Railing_Name=[]
        # get the lines content
        founded_lines_list = []
        

        wanted_ifc="#"
   


        for line in f:
            if wanted_ifc in line:


              
                      count_wanted_ifc += 1
                      founded_lines_list.append(line)
            
              
                        # get line no.
                      selected_line = founded_lines_list[count_wanted_ifc]

                      
                     # get line no.
                    
                      line_no1 = selected_line.index("#")
                      line_no2 = selected_line.index("=")

                      if selected_line[line_no1:line_no2]==Line_no:
                        
                            x=","
                            y=-1
                            comma_indexes=[]
                            temp_list=[]
                            for i in selected_line:
                                    y=y+1

                                    if x==i:
                                    
                                        comma_indexes.append(y)
                                        #print(selected_line)
                                        #print(comma_indexes)
                            ## here we are storing the first value
                            #temp_list.append(selected_line[selected_line.index("(")+1:comma_indexes[0]])
                            Railing_Name=selected_line[comma_indexes[1]+2:comma_indexes[3]-3]
            


        #print(Railing_Name)
        return Railing_Name


###ALL Functions:

search_ifc1("IFCRAILING")
search_ifc2("IFCRELDEFINESBYPROPERTIES")
search_ifc3()
search_ifc4()
search_ifc5()
##Railing_Bottom_Elevation("#1047")  ##this one is used in ==> railing_x_y_z()
#search_ifc5_2("#795")   ##this one is used in ==> Slab_z
search_ifc6()


#railing_x_y_z("#690")
#Slab_x_y_z("#1329")

## this has been used in the "slab_x_y_z"
#Slab_z("#437")

##getting the story level
#Railing_Story("#1329") 

#railing_Guid("#1329")

#railing_Name("#1129")