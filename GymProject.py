#Mohamad Mehdi Gym Project
import xlsxwriter
import sqlite3
import random

try:
    import tkinter as tk                # python 3   
except ImportError:
    import Tkinter as tk     # python 2

class Scrollbox(tk.Listbox):

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set
        

class OptionMenu(tk.Frame):

   def __init__(self, master, status, *options):

       super().__init__(master)

       self.status = tk.StringVar()
       self.status.set(status) #shows dropdown menu title

       self.dropdown = tk.OptionMenu(self, self.status, *options)
       self.dropdown.grid()
       
def workoutExp(row,col,worksheet):
    tempynDef = str(ynDef.get())
    if tempynDef == "Beginner":
        worksheet.write(row,col, 4)              
    elif tempynDef == "Intermediate":
        worksheet.write(row,col, 6)     
    elif tempynDef == "Advanced":
        worksheet.write(row,col, 8) 
    
def workOutGoals(row,col,worksheet):
    tempwgDef = str(wgDef.get())
    if tempwgDef == "Strength":
        worksheet.write(row,col, 6)
    elif tempwgDef == "Size":
        worksheet.write(row,col, 8)
    elif tempwgDef == "Stamina":   
        worksheet.write(row,col, 12)

def twoDayF(row,col,worksheet,FBF,FBA,n):
    col=0
    worksheet.write(row, col, "DAY " + str(n))
    row+=1    
    #prints the titls Exercises, sets, reps
    worksheet.write(row,col, "Exercises")
    col+=1
    worksheet.write(row,col, "Sets")
    col+=1
    worksheet.write(row,col,"Reps")
    row+=1
    indices = [ int(x) for x in muscleGroupList.curselection() ]
    for upperFree in conn.execute("SELECT UpperLower.upperFree FROM UpperLower"):
        FBF.append(upperFree)
    for i in indices:
        col=0
        temp=FBF[i]
        print(temp)
        if temp[0] != "NULL":
            temp=temp[0].split(",")
            worksheet.write(row,col,random.choice(temp))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1
    col=0
    row+=1
    n+=1
    worksheet.write(row, col, "DAY " + str(n))
    col=0
    row+=1
    worksheet.write(row,col, "Exercises")
    worksheet.write(row,col+1, "Sets")
    worksheet.write(row,col+2,"Reps")
    row+=1
            
    for lowerFree in conn.execute("SELECT UpperLower.lowerFree FROM UpperLower"):
        FBA.append(lowerFree)
    for i in indices:
        col=0
        temp1=FBA[i]
        if temp1[0] != "NULL":
            temp1=temp1[0].split(",")  
            worksheet.write(row,col,random.choice(temp1))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1   
    return(row+1,n+1)
    
def twoDayA(row,col,worksheet,FBF,FBA,n):
    col=0
    worksheet.write(row, col, "DAY " + str(n))
    row+=1    
    #prints the titls Exercises, sets, reps
    worksheet.write(row,col, "Exercises")
    col+=1
    worksheet.write(row,col, "Sets")
    col+=1
    worksheet.write(row,col,"Reps")
    row+=1
    indices = [ int(x) for x in muscleGroupList.curselection() ]
    for upperAssisted in conn.execute("SELECT UpperLower.upperAssisted FROM UpperLower"):
        FBF.append(upperAssisted)
    for i in indices:
        col=0
        temp=FBF[i]
        if temp[0] != "NULL":
            temp=temp[0].split(",")
            worksheet.write(row,col,random.choice(temp))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1
    col=0
    n+=1
    row+=1
    worksheet.write(row, col, "DAY " + str(n))
    col=0
    row+=1
    worksheet.write(row,col, "Exercises")
    worksheet.write(row,col+1, "Sets")
    worksheet.write(row,col+2,"Reps")
    row+=1
            
    for lowerAssisted in conn.execute("SELECT UpperLower.lowerAssisted FROM UpperLower"):
        FBA.append(lowerAssisted)
    for i in indices:
        col=0
        temp1=FBA[i]
        if temp1[0] != "NULL":
            temp1=temp1[0].split(",")  
            worksheet.write(row,col,random.choice(temp1))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1  
    return(row+1,n+1)
            
def twoDayB(row,col,worksheet,FBF,FBA,n):
    col=0
    worksheet.write(row, col, "DAY " + str(n))
    row+=1    
    #prints the titls Exercises, sets, reps
    worksheet.write(row,col, "Exercises")
    col+=1
    worksheet.write(row,col, "Sets")
    col+=1
    worksheet.write(row,col,"Reps")
    row+=1
    indices = [ int(x) for x in muscleGroupList.curselection() ]
    for upperFree in conn.execute("SELECT UpperLower.upperFree FROM UpperLower"):
        FBF.append(upperFree)
    for i in indices:
        col=0
        temp=FBF[i]
        if temp[0] != "NULL":
            temp=temp[0].split(",")
            print(len(temp))
            worksheet.write(row,col,random.choice(temp))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1
    col=0
    row+=1
    n+=1
    worksheet.write(row, col, "DAY " + str(n))
    col=0
    row+=1
    worksheet.write(row,col, "Exercises")
    worksheet.write(row,col+1, "Sets")
    worksheet.write(row,col+2,"Reps")
    row+=1
            
    for lowerAssisted in conn.execute("SELECT UpperLower.lowerAssisted FROM UpperLower"):
        FBA.append(lowerAssisted)
    for i in indices:
        col=0
        temp1=FBA[i]
        if temp1[0] != "NULL":
            temp1=temp1[0].split(",")  
            worksheet.write(row,col,random.choice(temp1))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1  
    return(row+1,n+1)

def threeDayF(row,col,worksheet,FBF,FBA,FBL,n):
    col=0
    worksheet.write(row, col, "DAY " + str(n))
    row+=1    
    #prints the titls Exercises, sets, reps
    worksheet.write(row,col, "Exercises")
    col+=1
    worksheet.write(row,col, "Sets")
    col+=1
    worksheet.write(row,col,"Reps")
    row+=1
    indices = [ int(x) for x in muscleGroupList.curselection() ]
    for pushFree in conn.execute("SELECT PushPullLegs.pushFree FROM PushPullLegs"):
        FBF.append(pushFree)
    for i in indices:
        col=0
        temp=FBF[i]
        if temp[0] != "NULL":
            temp=temp[0].split(",")
            worksheet.write(row,col,random.choice(temp))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1
    col=0
    row+=1
    n+=1
    worksheet.write(row, col, "DAY " + str(n))
    col=0
    row+=1
    worksheet.write(row,col, "Exercises")
    worksheet.write(row,col+1, "Sets")
    worksheet.write(row,col+2,"Reps")
    row+=1
            
    for pullFree in conn.execute("SELECT PushPullLegs.pullFree FROM PushPullLegs"):
        FBA.append(pullFree)
    for i in indices:
        col=0
        temp1=FBA[i]
        if temp1[0] != "NULL":
            temp1=temp1[0].split(",")  
            worksheet.write(row,col,random.choice(temp1))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1    

    col=0
    row+=1
    n+=1
    worksheet.write(row, col, "DAY " + str(n))
    col=0
    row+=1
    worksheet.write(row,col, "Exercises")
    worksheet.write(row,col+1, "Sets")
    worksheet.write(row,col+2,"Reps")
    row+=1
    
    for legsFree in conn.execute("SELECT PushPullLegs.legsFree FROM PushPullLegs"):
        FBL.append(legsFree)
    for i in indices:
        col=0
        temp2=FBL[i]
        if temp2[0] != "NULL":
            temp2=temp2[0].split(",")  
            worksheet.write(row,col,random.choice(temp2))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1
    return(row+1,n+1)
        
def threeDaysA(row,col,worksheet,FBF,FBA,FBL,n):
    col=0
    worksheet.write(row, col, "DAY " + str(n))
    row+=1    
    #prints the titls Exercises, sets, reps
    worksheet.write(row,col, "Exercises")
    col+=1
    worksheet.write(row,col, "Sets")
    col+=1
    worksheet.write(row,col,"Reps")
    row+=1
    indices = [ int(x) for x in muscleGroupList.curselection() ]
    for pushAssisted in conn.execute("SELECT PushPullLegs.pushAssisted FROM PushPullLegs"):
        FBF.append(pushAssisted)
    for i in indices:
        col=0
        temp=FBF[i]
        if temp[0] != "NULL":
            temp=temp[0].split(",")
            worksheet.write(row,col,random.choice(temp))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1
    col=0
    row+=1
    n+=1
    worksheet.write(row, col, "DAY " + str(n))
    col=0
    row+=1
    worksheet.write(row,col, "Exercises")
    worksheet.write(row,col+1, "Sets")
    worksheet.write(row,col+2,"Reps")
    row+=1
            
    for pullAssisted in conn.execute("SELECT PushPullLegs.pullAssisted FROM PushPullLegs"):
        FBA.append(pullAssisted)
    for i in indices:
        col=0
        temp1=FBA[i]
        if temp1[0] != "NULL":
            temp1=temp1[0].split(",")  
            worksheet.write(row,col,random.choice(temp1))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1    

    col=0
    row+=1
    n+=1
    worksheet.write(row, col, "DAY " + str(n))
    col=0
    row+=1
    worksheet.write(row,col, "Exercises")
    worksheet.write(row,col+1, "Sets")
    worksheet.write(row,col+2,"Reps")
    row+=1
    
    for legsAssisted in conn.execute("SELECT PushPullLegs.legsAssisted FROM PushPullLegs"):
        FBL.append(legsAssisted)
    for i in indices:
        col=0
        temp2=FBL[i]
        if temp2[0] != "NULL":
            temp2=temp2[0].split(",")  
            worksheet.write(row,col,random.choice(temp2))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1
    return(row+1,n+1)
            
def threeDaysB(row,col,worksheet,FBF,FBA,FBL,n):
    col=0
    worksheet.write(row, col, "DAY " + str(n))
    row+=1    
    #prints the titls Exercises, sets, reps
    worksheet.write(row,col, "Exercises")
    col+=1
    worksheet.write(row,col, "Sets")
    col+=1
    worksheet.write(row,col,"Reps")
    row+=1
    indices = [ int(x) for x in muscleGroupList.curselection() ]
    for pushAssisted in conn.execute("SELECT PushPullLegs.pushAssisted FROM PushPullLegs"):
        FBF.append(pushAssisted)
    for i in indices:
        col=0
        temp=FBF[i]
        if temp[0] != "NULL":
            temp=temp[0].split(",")
            worksheet.write(row,col,random.choice(temp))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1
    col=0
    row+=1
    n+=1
    worksheet.write(row, col, "DAY " + str(n))
    col=0
    row+=1
    worksheet.write(row,col, "Exercises")
    worksheet.write(row,col+1, "Sets")
    worksheet.write(row,col+2,"Reps")
    row+=1
            
    for pullFree in conn.execute("SELECT PushPullLegs.pullFree FROM PushPullLegs"):
        FBA.append(pullFree)
    for i in indices:
        col=0
        temp1=FBA[i]
        if temp1[0] != "NULL":
            temp1=temp1[0].split(",")  
            worksheet.write(row,col,random.choice(temp1))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1    

    col=0
    row+=1
    n+=1
    worksheet.write(row, col, "DAY " + str(n))
    col=0
    row+=1
    worksheet.write(row,col, "Exercises")
    worksheet.write(row,col+1, "Sets")
    worksheet.write(row,col+2,"Reps")
    row+=1
    
    for legsAssisted in conn.execute("SELECT PushPullLegs.legsAssisted FROM PushPullLegs"):
        FBL.append(legsAssisted)
    for i in indices:
        col=0
        temp2=FBL[i]
        if temp2[0] != "NULL":
            temp2=temp2[0].split(",")  
            worksheet.write(row,col,random.choice(temp2))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1            
    return(row+1,n+1)
    
def pageOne():
    #What to forget from page 2
    mgLabel.grid_forget()
    page2text.grid_forget()
    muscleGroupList.grid_forget()
    mglabel2.grid_forget()
    
    #grid positions of all widgets on page 1
    page1text.grid(column=6,row=6,sticky='sw') 
    workOutGoaltext.grid(row=1, column=2, sticky='w')
    yNtext.grid(row=2, column=2, sticky='w')
    howManyDaystext.grid(row=3, column=2, sticky='w')
    assistedOrUntext.grid(row=4, column=2, sticky='w')
       
    workOutGoal.grid(row=1, column=3,sticky='w')
    yN.grid(row=2, column=3,sticky='w')
    howManyDays.grid(row=3, column=3,sticky='w')
    assistedOrUn.grid(row=4, column=3, sticky='w')
    
def pageTwo():
    #what to forget from page1
    workOutGoal.grid_forget()
    yN.grid_forget()
    howManyDays.grid_forget()

    page1text.grid_forget()
    assistedOrUn.grid_forget()
    workOutGoaltext.grid_forget()
    yNtext.grid_forget()
    howManyDaystext.grid_forget()
    assistedOrUntext.grid_forget()
    
    #the grid position of all widgets on page 2
    page2text.grid(column=6,row=6,sticky='se')
    mgLabel.grid(row=0, column=2, sticky='nsew')
    muscleGroupList.grid(row=1, column=2, sticky='nsew', rowspan=2, padx=(30, 0))
    mglabel2.grid(row=4, column=4)

def createWP():
    workbook = xlsxwriter.Workbook('WorkoutProgram.xlsx')
    worksheet = workbook.add_worksheet()
    temphmdlDef = int(hmdlDef.get())
    #prints week1 to week10
    row=0
    col=3
    x=1
    for i in range (10):
        worksheet.write(row+1,col, "Week {}".format(x))
        x+=1
        col+=1
    
    FBF=[]
    FBA=[]
    FBL=[]
    temphmdlDef = hmdlDef.get()
    tempaoulDef = aoulDef.get()
    row=4
    col=0 
    n=1
    #=========================ONE DAY A WEEK===============================#
    if (temphmdlDef == "1" and tempaoulDef == "Free Weight Focused"):
        col=0
        worksheet.write(row, col, "DAY " + str(n))
        row+=1    
        #prints the titls Exercises, sets, reps
        worksheet.write(row,col, "Exercises")
        col+=1
        worksheet.write(row,col, "Sets")
        col+=1
        worksheet.write(row,col,"Reps")
        row+=1
        indices = [ int(x) for x in muscleGroupList.curselection() ]
        for fullBodyFree in conn.execute("SELECT FullBody.fullBodyFree FROM FullBody"):
            FBF.append(fullBodyFree)
        for i in indices:
            col=0
            temp=FBF[i]
            temp=temp[0].split(",")
            worksheet.write(row,col,random.choice(temp))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1
            
    elif (temphmdlDef == "1" and tempaoulDef == "Smith Machine Focused"):
        col=0
        worksheet.write(row, col, "DAY " + str(n))
        row+=1    
        #prints the titls Exercises, sets, reps
        worksheet.write(row,col, "Exercises")
        col+=1
        worksheet.write(row,col, "Sets")
        col+=1
        worksheet.write(row,col,"Reps")
        row+=1
        indices = [ int(x) for x in muscleGroupList.curselection() ]
        for fullBodyAssisted in conn.execute("SELECT FullBody.fullBodyAssisted FROM FullBody"):
            FBA.append(fullBodyAssisted)
        for i in indices:
            col=0
            temp=FBA[i]
            temp=temp[0].split(",")
            worksheet.write(row,col,random.choice(temp))
            col+=1
            workoutExp(row,col,worksheet)
            col+=1
            workOutGoals(row,col,worksheet)
            row+=1   
            
    elif (temphmdlDef == "1" and tempaoulDef == "Both"):
        col=0
        worksheet.write(row, col, "DAY " + str(n))
        row+=1    
        #prints the titls Exercises, sets, reps
        worksheet.write(row,col, "Exercises")
        col+=1
        worksheet.write(row,col, "Sets")
        col+=1
        worksheet.write(row,col,"Reps")
        row+=1
        indices = [ int(x) for x in muscleGroupList.curselection() ]
        for fullBodyAssisted in conn.execute("SELECT FullBody.fullBodyAssisted FROM FullBody"):
            FBA.append(fullBodyAssisted)
        for fullBodyFree in conn.execute("SELECT FullBody.fullBodyFree FROM FullBody"):
            FBF.append(fullBodyFree)
        for index,i in enumerate(indices):
            if index % 2 == 0:
                col=0
                temp=FBA[i]
                temp=temp[0].split(",")
                worksheet.write(row,col,random.choice(temp))
                col+=1
                workoutExp(row,col,worksheet)
                col+=1
                workOutGoals(row,col,worksheet)
                row+=1   
            
            else:
                col=0
                temp=FBF[i]
                temp=temp[0].split(",")
                worksheet.write(row,col,random.choice(temp))
                col+=1
                workoutExp(row,col,worksheet)
                col+=1
                workOutGoals(row,col,worksheet)
                row+=1  
            
    #=========================TWO DAYS A WEEK==============================#
    elif (temphmdlDef == "2" and tempaoulDef == "Free Weight Focused"):
        row,n=twoDayF(row,col,worksheet,FBF,FBA,n)

    elif (temphmdlDef == "2" and tempaoulDef == "Smith Machine Focused"):
        row,n=twoDayA(row, col, worksheet, FBF, FBA,n)
    
    elif (temphmdlDef == "2" and tempaoulDef == "Both"):
        row,n=twoDayB(row, col, worksheet, FBF, FBA,n)  
    
                          
    #=========================THREE DAYS A WEEK==============================#
    elif (temphmdlDef == "3" and tempaoulDef == "Free Weight Focused"):
        row,n=threeDayF(row,col,worksheet,FBF,FBA,FBL,n)
    
    elif (temphmdlDef == "3" and tempaoulDef == "Smith Machine Focused"):
        row,n=threeDaysA(row,col,worksheet,FBF,FBA,FBL,n)      

    elif (temphmdlDef == "3" and tempaoulDef == "Both"):
        row,n=threeDaysB(row, col, worksheet, FBF, FBA, FBL, n)   
              
    #=========================FOUR DAYS A WEEK==============================#    
    elif (temphmdlDef == "4" and tempaoulDef == "Free Weight Focused"):
        row,n=twoDayF(row,col,worksheet,FBF,FBA,n)
        row,n=twoDayF(row,col,worksheet,FBF,FBA,n)
        
    elif (temphmdlDef == "4" and tempaoulDef == "Smith Machine Focused"): 
        row,n=twoDayA(row,col,worksheet,FBF,FBA,n)
        row,n=twoDayA(row,col,worksheet,FBF,FBA,n)
        
    elif (temphmdlDef == "4" and tempaoulDef == "Both"):  
        row,n=twoDayF(row,col,worksheet,FBF,FBA,n)
        row,n=twoDayA(row,col,worksheet,FBF,FBA,n)
        
    #====================FIVE DAYS A WEEK==================================#
    elif (temphmdlDef == "5" and tempaoulDef == "Free Weight Focused"):
        row,n=twoDayF(row,col,worksheet,FBF,FBA,n)
        row,n=threeDayF(row,col,worksheet,FBF,FBA,FBL,n)
    
    elif (temphmdlDef == "5" and tempaoulDef == "Smith Machine Focused"):
        row,n=twoDayA(row,col,worksheet,FBF,FBA,n)
        row,n=threeDaysA(row,col,worksheet,FBF,FBA,FBL,n)
    
    elif (temphmdlDef == "5" and tempaoulDef == "Both"):
        row,n=twoDayA(row,col,worksheet,FBF,FBA,n)
        row,n=threeDayF(row,col,worksheet,FBF,FBA,FBL,n)
    
   #=======================SIX DAYS A WEEK==================================#
    elif (temphmdlDef == "6" and tempaoulDef == "Free Weight Focused"):
        row,n=threeDayF(row,col,worksheet,FBF,FBA,FBL,n)
        row,n=threeDayF(row,col,worksheet,FBF,FBA,FBL,n)
    
    elif (temphmdlDef == "6" and tempaoulDef == "Smith Machine Focused"):
        row,n=threeDaysA(row,col,worksheet,FBF,FBA,FBL,n)
        row,n=threeDaysA(row,col,worksheet,FBF,FBA,FBL,n)
    
    elif (temphmdlDef == "6" and tempaoulDef == "Both"):
        row,n=threeDaysA(row,col,worksheet,FBF,FBA,FBL,n)
        row,n=threeDayF(row,col,worksheet,FBF,FBA,FBL,n)
   
    worksheet.set_column('A:A', 30)
    worksheet.set_column('B:C', 10)
        
    workbook.close()
    
if __name__ == '__main__':
    conn = sqlite3.connect('Exercises.db')
    
    window = tk.Tk()
    window.geometry('700x608')
    window.title('Workout Plan Creator')
    
    #Setting the columns for UI
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    window.columnconfigure(3, weight=1)
    window.columnconfigure(4, weight=1)
    window.columnconfigure(5, weight=1)
    window.columnconfigure(6, weight=1)

    #Setting the rows for UI
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)
    window.rowconfigure(3, weight=1)
    window.rowconfigure(4, weight=1)
    window.rowconfigure(5, weight=1)
    window.rowconfigure(6, weight=1)
    
    #=======Labels and buttons=========#
    pageOnebtn = tk.Button(window, text="Page 1", command=pageOne)
    pageTwobtn = tk.Button(window, text="Page 2", command=pageTwo)
    
    mgLabel = tk.Label(window, text="Muscle Groups")
    page2text = tk.Label(window, text="This is page 2")
    page1text = tk.Label(window, text="This is page 1")
    
    pageOnebtn.grid(column=4,row=6,sticky='se')
    pageTwobtn.grid(column=5,row=6,sticky='sw')
    page1text.grid(column=6,row=6,sticky='sw')
    page2text.grid(column=6,row=6,sticky='sw')
    #===============================#
    
    # ===== Muscle Groups Listbox =====#
    muscleGroupList = Scrollbox(window, selectmode = 'multiple')
    
    for muscleGroup in conn.execute("SELECT sheet1.muscleGroup FROM sheet1 ORDER BY sheet1.muscleGroup"):
        muscleGroupList.insert(tk.END, muscleGroup[0])
    
    mglDef = tk.StringVar(window)
    mglDef.set("Back")
    
    mglabel2 = tk.Label(window, text="Please select the muscle groups you would like to include in your workout")
    
    #========================================#
    
    #=========Page One Drop Down Menus and labels for them==========#
    workOutGoalList = ["Strength", 
                       "Size",
                       "Stamina",
                       ]
    
    yNList = ["Beginner", 
              "Intermediate",
              "Advanced"
              ]
    
    howManyDaysList = ["1",
                       "2", 
                       "3",
                       "4",
                       "5", 
                       "6",
                       ]
    
    assistedOrUnList = ["Smith Machine Focused", 
                        "Free Weight Focused", 
                        "Both",
                        ]  
    
    wgDef = tk.StringVar(window)
    wgDef.set("Size")
    ynDef = tk.StringVar(window)
    ynDef.set("Beginner")
    hmdlDef = tk.StringVar(window)
    hmdlDef.set("5")
    aoulDef = tk.StringVar(window)
    aoulDef.set("Both")
    
    workOutGoal = tk.OptionMenu(window, wgDef, *workOutGoalList)
    yN = tk.OptionMenu(window, ynDef, *yNList)
    howManyDays = tk.OptionMenu(window, hmdlDef, *howManyDaysList)
    assistedOrUn = tk.OptionMenu(window, aoulDef, *assistedOrUnList)   

    workOutGoaltext = tk.Label(window, text = "What is your main goal when working out?")
    yNtext = tk.Label(window, text = "What is your level of experience with working out?")
    howManyDaystext = tk.Label(window, text = "How many days a week would like you workout?")
    assistedOrUntext = tk.Label(window, text = "What type of Exercises would you like in your workout?")
    
    workOutGoal.grid(row=1, column=3,sticky='w')
    yN.grid(row=2, column=3,sticky='w')
    howManyDays.grid(row=3, column=3,sticky='w')
    assistedOrUn.grid(row=4, column=3, sticky='w')
    
    workOutGoaltext.grid(row=1, column=2, sticky='w')
    yNtext.grid(row=2, column=2, sticky='w')
    howManyDaystext.grid(row=3, column=2, sticky='w')
    assistedOrUntext.grid(row=4, column=2, sticky='w')
    
    createSheet_button = tk.Button(window, text = 'Create', command=createWP)
    createSheet_button.grid(row=6, column = 1, sticky='sew')
    #================================================================#
    window.mainloop()
    print("closing database connection")
    conn.close()