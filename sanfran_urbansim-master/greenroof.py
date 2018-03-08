import pandas as pd
data = pd.read_csv('data.csv')
##This is used to bound start and end of for loops
def my_range(start, end, step):
    while start <= end:
        yield start #keyword yield generates an interator
        start += step
        return 

def NoInterventionGreenRoof2():
    print("Howdy bang")
    return
    
    
############################
############################
#NO ACTION POLCIY TESTS
############################
############################

def NoInterventionGreenRoof():
    
    building_size_dict = {}
    roofins_dict = {}
    green_roof_ben_dict = {}
    green_roof_cost_dict = {}
    roof_cost_at_20yrs_dict = {}
    size_dict = {}

    for index in range(-1, 2000, 1):
        index = index + 1
        best_ben = 0
        building_size = (data['sq_ft'][index])/(data['stories'][index])
        roof_cost_at_20yrs = building_size * 6
        building_size_dict.update({index : building_size})

        for size_ratio in my_range (0, 1.01, .01):
            green_roof_cost = 23.907*(12**(-0.078)) *size_ratio * building_size + (40*.02*building_size*size_ratio) + (building_size*size*ratio*.21)
            green_roof_ben = .23 * size_ratio * building_size * 40 + (building_size * 6 * (1-size_ratio))
            if(green_roof_ben - green_roof_cost > best_ben):
                roof_ins = 1
                best_size = size_ratio * building_size
                size_dict.update({index : best_size})
                roofins_dict.update({index : roof_ins})
                green_roof_ben_dict.update({index : green_roof_ben})
                green_roof_cost_dict.update({index : green_roof_cost})
                roof_cost_at_20yrs = building_size * 6 * (1-size_ratio)            
                roof_cost_at_20yrs_dict.update({index : roof_cost_at_20yrs})

    buildings = pd.DataFrame({"building size" : building_size_dict, "best_size" : size_dict, "roofins" : roofins_dict, "green_ben" : green_roof_ben_dict, "green_cost" : green_roof_cost_dict, "cost_20yr" : roof_cost_at_20yrs_dict, })
    writer = pd.ExcelWriter('no_action.xlsx')
    buildings.to_excel(writer,'no_action')
    writer.save()
    return


############################
############################
#SAN FRAN STYLE POLCIY TESTS
############################
############################

def SanFranGreenRoof():
    building_size_dict = {}
    roofins_dict = {}
    green_roof_ben_dict = {}
    green_roof_cost_dict = {}
    roof_cost_at_20yrs_dict = {}
    size_dict = {}
    mandated_dict = {}
    for index in range(-1, 2000, 1):
        index = index + 1
        best_ben = 0
        building_size = (data['sq_ft'][index])/(data['stories'][index])
        roof_cost_at_20yrs = building_size * 6
        building_size_dict.update({index : building_size})

        if(data['building_type_id'][index] != 'Residential' and building_size < 15625):
            mandated_dict.update({index : 1})
            green_roof_cost = 23.907*(12**(-0.078)) *size_ratio * building_size + (40*.02*building_size*size_ratio) + (building_size*size*ratio*.21)
            green_roof_ben = .23 * size_ratio * building_size * 40 + (building_size * 6 * (1-size_ratio))
            roof_ins = 1
            best_size = building_size
            size_dict.update({index : 1})
            roofins_dict.update({index : roof_ins})
            green_roof_ben_dict.update({index : green_roof_ben})
            green_roof_cost_dict.update({index : green_roof_cost})
            roof_cost_at_20yrs_dict.update({index : 0})

        elif(data['building_type_id'][index] != 'Residential' and building_size >= 15625):
            mandated_dict.update({index : 1})
            green_roof_ben = .23 * size_ratio * building_size * 40 + (building_size * 6 * (1-size_ratio))
            green_roof_cost = 23.907*(12**(-0.078)) *size_ratio * building_size + (40*.02*building_size*size_ratio) +(building_size*size*ratio*.21)
            roof_ins = 1
            best_size = 15625
            size_dict.update({index : 1})
            roofins_dict.update({index : roof_ins})
            green_roof_ben_dict.update({index : green_roof_ben})
            green_roof_cost_dict.update({index : green_roof_cost})
            roof_cost_at_20yrs_dict.update({index : 0})

        else:
            mandated_dict.update({index : 0})
            for size_ratio in my_range (0, 1.01, .01):
            green_roof_cost = 23.907*(12**(-0.078)) *size_ratio * building_size + (40*.02*building_size*size_ratio) + (building_size*size*ratio*.21)  
            green_roof_ben = .23 * size_ratio * building_size * 40 + (building_size * 6 * (1-size_ratio))
                if(green_roof_ben - green_roof_cost > best_ben):
                    roof_ins = 1
                    best_size = size_ratio * building_size
                    size_dict.update({index : best_size})
                    roofins_dict.update({index : roof_ins})
                    green_roof_ben_dict.update({index : green_roof_ben})
                    green_roof_cost_dict.update({index : green_roof_cost})
                    roof_cost_at_20yrs = building_size * 6 * (1-size_ratio)            
                    roof_cost_at_20yrs_dict.update({index : roof_cost_at_20yrs})

    buildings = pd.DataFrame({"building size" : building_size_dict, "best_size" : size_dict, "roofins" : roofins_dict, "green_ben" : green_roof_ben_dict, "green_cost" : green_roof_cost_dict, "cost_20yr" : roof_cost_at_20yrs_dict, "mandated" : mandated_dict})
    writer = pd.ExcelWriter('san_fran.xlsx')
    buildings.to_excel(writer,'san_fran')
    writer.save()
    return
    

############################
############################
#TORONTO STYLE POLCIY TESTS
############################
############################


def TorontoGreenRoof(): 
    building_size_dict = {}
    roofins_dict = {}
    green_roof_ben_dict = {}
    green_roof_cost_dict = {}
    roof_cost_at_20yrs_dict = {}
    size_dict = {}
    mandated_dict = {}
    green_roof_min_dict = {}
    for index in range(-1, 2000, 1):
        index = index + 1
        best_ben = 0
        building_size = (data['sq_ft'][index])/(data['stories'][index])
        roof_cost_at_20yrs = building_size * 6
        building_size_dict.update({index : building_size})
        if(data['building_type_id'][index] != 'Residential' or ((data['building_type_id'][index] == 'Residential' and data['stories'][index] > 6))):
            mandated_dict.update({index : 1})
            if(building_size > 21525 and building_size <= 53800):
                green_roof_min = .2
            elif(building_size > 53800 and building_size <= 107625):
                green_roof_min = .3 
            elif(building_size > 107625 and building_size <= 161450):
                green_roof_min = .4 
            elif(building_size > 161450 and building_size <= 215275):
                green_roof_min = .5 
            elif (building_size > 215275):
                green_roof_min = .6
            else:
                green_roof_min = 0

            green_roof_min_dict.update( {index : green_roof_min})
            green_roof_cost = 23.907*(12**(-0.078)) * building_size + (40*.02*building_size*green_roof_min)
            green_roof_ben = 1.23 * building_size * 40 + (building_size * 6 * (1-green_roof_min))
            roof_ins = 1
            best_size = building_size * green_roof_min
            size_dict.update({index : 1})
            roofins_dict.update({index : roof_ins})
            green_roof_ben_dict.update({index : green_roof_ben})
            green_roof_cost_dict.update({index : green_roof_cost})
            roof_cost_at_20yrs_dict.update({index : 0})

            for size_ratio in my_range (green_roof_min, 1.01, .01):
                green_roof_cost = 23.907*(12**(-0.078)) *size_ratio * building_size + (40*.02*building_size*size_ratio)
                green_roof_ben = 1.23 * size_ratio * building_size * 40 + (building_size * 6 * (1-size_ratio)) + (.05*size_ratio*building_size)
                if(green_roof_ben - green_roof_cost > best_ben):
                    roof_ins = 1
                    best_size = size_ratio * building_size
                    size_dict.update({index : best_size})
                    roofins_dict.update({index : roof_ins})
                    green_roof_ben_dict.update({index : green_roof_ben})
                    green_roof_cost_dict.update({index : green_roof_cost})
                    roof_cost_at_20yrs = building_size * 6 * (1-size_ratio)            
                    roof_cost_at_20yrs_dict.update({index : roof_cost_at_20yrs})

        else:
            mandated_dict.update({index : 0})
            green_roof_min_dict.update( {index : 0})
            for size_ratio in my_range (0, 1.01, .01):
                green_roof_cost = 23.907*(12**(-0.078)) *size_ratio * building_size + (40*.02*building_size*size_ratio)
                green_roof_ben = 1.23 * size_ratio * building_size * 40 + (building_size * 6 * (1-size_ratio)) + (.05*size_ratio*building_size)
                if(green_roof_ben - green_roof_cost > best_ben):
                    roof_ins = 1
                    best_size = size_ratio * building_size
                    size_dict.update({index : best_size})
                    roofins_dict.update({index : roof_ins})
                    green_roof_ben_dict.update({index : green_roof_ben})
                    green_roof_cost_dict.update({index : green_roof_cost})
                    roof_cost_at_20yrs = building_size * 6 * (1-size_ratio)            
                    roof_cost_at_20yrs_dict.update({index : roof_cost_at_20yrs})

    buildings = pd.DataFrame({"building size" : building_size_dict, "best_size" : size_dict, "roofins" : roofins_dict, "green_ben" : green_roof_ben_dict, "green_cost" : green_roof_cost_dict, "cost_20yr" : roof_cost_at_20yrs_dict, "mandated" : mandated_dict, "green_min" : green_roof_min_dict})
    writer = pd.ExcelWriter('toronto.xlsx')
    buildings.to_excel(writer,'toronto')
    writer.save()
    return
    
############################
############################
#CHICAGO STYLE POLCIY TESTS
############################
############################



def ChicagoGreenRoof():
    building_size_dict = {}
    roofins_dict = {}
    green_roof_ben_dict = {}
    green_roof_cost_dict = {}
    roof_cost_at_20yrs_dict = {}
    size_dict = {}
    for index in range(-1, 2000, 1):
        index = index + 1
        best_ben = 0
        building_size = (data['sq_ft'][index])/(data['stories'][index])
        roof_cost_at_20yrs = building_size * 6
        building_size_dict.update({index : building_size})
        for size_ratio in my_range (0, 1.01, .01):
            green_roof_cost = 23.907*(12**(-0.078)) *size_ratio * building_size + (40*.02*building_size*size_ratio)
            green_roof_ben = 1.23 * size_ratio * building_size * 40 + (building_size * 6 * (1-size_ratio)) + (.05*size_ratio*building_size)
            if(green_roof_ben - green_roof_cost > best_ben):
                roof_ins = 1
                best_size = size_ratio * building_size
                size_dict.update({index : best_size})
                roofins_dict.update({index : roof_ins})
                green_roof_ben_dict.update({index : green_roof_ben})
                green_roof_cost_dict.update({index : green_roof_cost})
                roof_cost_at_20yrs = building_size * 6 * (1-size_ratio)            
                roof_cost_at_20yrs_dict.update({index : roof_cost_at_20yrs})

    buildings = pd.DataFrame({"building size" : building_size_dict, "best_size" : size_dict, "roofins" : roofins_dict, "green_ben" : green_roof_ben_dict, "green_cost" : green_roof_cost_dict, "cost_20yr" : roof_cost_at_20yrs_dict})
    writer = pd.ExcelWriter('chicago.xlsx')
    buildings.to_excel(writer,'chicago')
    writer.save()