import pandas as pd

##This is used to bound start and end of for loops
def my_range(start, end, step):
    while start <= end:
        yield start #keyword yield generates an interator
        start += step
        return
    
#There are 147499 parcels to analyze with this code
#Bring in the indices sorted

############################
############################
#NO ACTION POLCIY TESTS
############################
############################

def NoInterventionGreenRoof():
    import pandas as pd
    index = 0
    data = pandas.read_csv('data.csv')
    for index in my_range(0, len(data.index), 1):
        building_size = (data['stories'][index])/(data['sq_ft'][index])     
        #Initialization of assumed and derived variables
        green_cost_per_sqft = 12
        green_roof_min = 0
        building_size = parcel_size * parcel_coverage
        conventional_cost_per_sqft = green_cost_per_sqft/2
        green_roof_benefits = 0
        building_age = 40
        annual_benefit_per_area = 1.23
        annual_maintenance_costs_per_area = 0.02 
        min_green_area = green_roof_min * building_size
        min_green_cost = green_roof_min * green_cost_per_sqft
        min_green_benefits= green_roof_min*building_size*annual_benefit_per_area*building_age
        best_size = green_roof_min
        best_benefit = min_green_benefits - min_green_cost
        best_conv = (building_size*(1-green_roof_min)*conventional_cost_per_sqft) #Avoid capital costs

        
        #Calculation of Output variables
        
        #If the building is large enough to allow bulk discounting to begin (happens in most cases)
        if (building_size > 500):
            green_cost_per_sqft = 23.907*(green_cost_per_sqft**(-0.078))
        
        for current_size in my_range(green_roof_min, 1, 0.01):
            roof_cost_at_20yrs = (building_size*(1-current_size)*conventional_cost_per_sqft) #Avoid capital costs
            green_roof_cost = current_size * building_size * green_cost_per_sqft + (building_age * annual_maintenance_costs_per_area * building_size * current_size)
            green_roof_benefits = building_age * annual_benefit_per_area * building_size * current_size + roof_cost_at_20yrs
            if(green_roof_benefits - green_roof_cost > best_benefit):
                best_size = current_size
                best_green_cost = green_roof_cost
                best_green_benefits = green_roof_benefits
                best__green_net_benefit = green_roof_benefits - green_roof_cost
                best_conv = roof_cost_at_20yrs
        
        if(best_benefit > 0):
            green_ins.update({index : 1}) #this green roof variable can be stored in the final
        else:
                green_ins.update({index : 1})
        
        
        roof_cost_at_20yrs_dict.update({index : best_conv})
        green_roof_benefit_dict.update({index : best_green_benefits})
        green_roof_cost_dict.update({index : best_green_cost})
        green_roof_net_benefit_dict.update({index : best__green_net_benefit})
        index = index +1
    
    #Print results
    
    roofinstalled = pd.Series(roofinstalled_dict)
    green_roof_benefit = pd.Series(green_roof_benefit_dict)
    green_roof_cost = pd.Series(green_roof_cost_dict)
    green_roof_net_benefit = pd.Series(green_roof_net_benefit_dict)
    conv_roof_maintenance = pd.Series(roof_cost_at_20yrs_dict)
    buildings = pd.DataFrame({"green ins" : roofinstalled_dict, "green ben" : green_roof_benefit_dict, "green cost" : green_roof_cost_dict, "green net": green_roof_net_benefit_dict, "conv maintain" :conv_roof_maintenance})
    buildings.to_csv("no_action.csv")
    return "Check no_action.csv"

    
    
############################
############################
#SAN FRAN STYLE POLCIY TESTS
############################
############################




#def SanFranGreenRoof():
#    index = 0
#    for(all buildings in the table):
#        index += 1 #this is used as a tracker to create the data table
#        
#        #Initialization of assumed and derived variables
#        green_cost_per_sqft = 12
#        green_roof_min = 0
#        building_size = parcel_size * parcel_coverage
#        conventional_cost_per_sqft = green_cost_per_sqft/2
#        green_roof_benefits = 0
#        building_age = 40
#        annual_benefit_per_area = 1.23
#        annual_maintenance_costs_per_area = 0.02 
#        min_green_area = green_roof_min * building_size
#        min_green_cost = green_roof_min * green_cost_per_sqft
#        min_green_benefits= green_roof_min*building_size*annual_benefit_per_area*building_age
#        best_size = green_roof_min
#       best_benefit = min_green_benefits - min_green_cost
#      best_conv = (building_size*(1-green_roof_min)*conventional_cost_per_sqft) #Avoid capital costs
#
#        #If the building is large enough to allow bulk discounting to begin (happens in most cases)
#        if (building_size > 500):
#            green_cost_per_sqft = 23.907*(green_cost_per_sqft**(-0.078))
#
#        
#        if  (generaltype != 'Residential'): #This set of conditions only applies when the mandate applies
#            if parcel_coverage * parcel_size < 15625: #If the building size is less then the max green roof size allowed
#                green_roof_cost += green_cost_per_sqft * parcel_coverage * parcel_size #size of building (assume roof area is equal)
#                roof_cost_at_20yrs = building_size*conventional_cost_per_sqft
#                roof_benefits = building_age * annual_benefit_per_area * building_size + roof_cost_at_20yrs
#                else:
#                    roof_at_20yrs = 15625*conventional_cost_per_sqft
#                    green_roof_cost = 15625 *green_cost_per_sqft #max allowable
#                    green_roof_benefit = 156225 * building_age * annual_benefit_per_area + roof_cost_at_20yrs
#                    print("Upper limit reached")
#                    annual_benefit_per_area = 1.23
#                    green_roof_benefits += building_age * annual_benefit_per_area * parcel_coverage * parcel_size  + roof_cost_at_20yrs
#                    costs = costs + roof_cost - roof_benefits
#            else: #Otherwise we carry out the decision making process as if there were no policy
#                min_green_area = green_roof_min * building_size
#                min_green_cost = green_roof_min * green_cost_per_sqft
#                min_green_benefits = green_roof_min*building_size*annual_benefit_per_area*building_age
#                best_size = green_roof_min
#                best_benefit = min_green_benefits - min_green_cost
#                for current_size in my_range(green_roof_min, 1, 0.01):
#                    roof_cost_at_20yrs = (building_size*(1-current_size)*conventional_cost_per_sqft) #Avoid capital costs
#                    green_roof_cost = current_size * building_size * green_cost_per_sqft + (building_age * #annual_maintenance_costs_per_area * building_size * current_size)
#                    roof_benefits = building_age * annual_benefit_per_area * building_size * current_size + roof_cost_at_20yrs
#                    if(green_roof_benefits - green_roof_cost > best_benefit):
#                        best_size = current_size
#                        best_conv = roof_cost_at_20yrs
#                        best_green_roof_cost = green_roof_cost
#                        best_green_roof_benefit = green_roof_benefit
#                        best_net_benefit = green_roof_benefits - green_roof_cost
#        
#                if(best_benefit > 0):
#            green_ins.update{index : 1} #this green roof variable can be stored in the final
#            else:
#                green_ins.update{index : 1}
#        
#        
#        roof_cost_at_20yrs_dict.update({index : best_conv})
#        green_roof_benefit_dict.update({index : best_benefit})
#        green_roof_cost_dict.update({index : green_roof_cost})
#        green_roof_net_benefit_dict.update({index : green_roof_net_benefit})
               
    #Print results
#    employee = pd.Series(employed_dict)
#    rents = pd.Series(rent_dict)
#    vacancies = pd.Series(vacant_dict)
#    roofinstalled = pd.Series(roofinstalled_dict)
#    employment_density = pd.Series(employment_density_dict)
#    incomes = pd.Series(income_dict)
#    project_cost = pd.Series(project_cost_dict)
#    green_roof_benefit = pd.Series(green_roof_benefit_dict)
#    green_roof_cost = pd.Series(green_roof_cost_dict)
#    green_roof_net_benefit = pd.Series(green_roof_net_benefit_dict)
#    property_values = pd.Series(property_value_dict)
#    conv_roof_maintenance = pd.Series(roof_cost_at_20yrs_dict)
#    buildings = pd.DataFrame({"income": incomes, "job" : employed_dict,"job density": employment_density_dict, "prop val": #property_value_dict, "green ins" : roofinstalled_dict, "green ben" : green_roof_benefit_dict, "green cost" : green_roof_cost_dict, "green net": green_roof_net_benefit_dict, "rent": rent_dict, "vacant" : vacancies, "conv maintain" :conv_roof_maintenance})
#    buildings.to_csv("san_fran_greenroof.csv")
#    return "Check san_fran_greenroof.csv"

############################
############################
#TORONTO STYLE POLCIY TESTS
############################
############################




#def TorontoGreenRoof(): 
#    index = 0
#    for(all buildings in the table):
#        index += 1 #this is used as a tracker to create the data table
#        
#        #Initialization of assumed and derived variables
#        green_cost_per_sqft = 12
#        green_roof_min = 0
#        building_size = parcel_size * parcel_coverage
#        conventional_cost_per_sqft = green_cost_per_sqft/2
#        green_roof_benefits = 0
#        building_age = 40
#        annual_benefit_per_area = 1.23
#        annual_maintenance_costs_per_area = 0.02 
#            
#        #Computation of Output variables
#        
#        #If the building is large enough to allow bulk discounting to begin (happens in most cases)
#        if (building_size > 500):
#            green_cost_per_sqft = 23.907*(green_cost_per_sqft**(-0.078))
#        
#        #comparison values from policy and converted into sq. ft.
#        if  not residential or (residential and stories > 6): #This set of conditions only applies when the mandate applies
#            green_roof = 1
#            mandate = 1
#            if(building_size > 21525 and building_size <= 53800):
#                green_roof_min = .2
#            elif(building_size > 53800 and building_size <= 107625):
#                green_roof_min = .3 
#            elif(building_size > 107625 and building_size <= 161450):
#                green_roof_min = .4 
#            elif(building_size > 161450 and building_size <= 215275):
#                green_roof_min = .5 
#            elif (building_size > 215275):
#                green_roof_min = .6
#            else:
#                green_roof_min = 0
#
#        min_green_area = green_roof_min * building_size
#        best_conv = (building_size*(1-green_roof_min)*conventional_cost_per_sqft) #Avoid capital costs
#        min_green_cost = min_green_area * green_cost_per_sqft
#        min_green_benefits = green_roof_min*building_size*annual_benefit_per_area*building_age + roof_cost_at_20yrs
#        best_size = green_roof_min
#        best_benefit = min_green_benefits - min_green_cost
#        
#        for current_size in my_range(green_roof_min, 1, 0.01):
#            green_roof_cost = current_size * building_size * green_cost_per_sqft + (building_age * annual_maintenance_costs_per_area * #building_size * current_size)
#            roof_cost_at_20yrs = (building_size*(1-current_size)*conventional_cost_per_sqft) #Avoid capital costs
#            green_roof_benefits = building_age * annual_benefit_per_area * building_size * current_size + roof_cost_at_20yrs
#            if(green_roof_benefits - green_roof_cost > best_benefit):
#                best_size = current_size
#                best_green_cost = green_roof_cost
#                best_green_benefits = green_roof_benefits
#                best__green_net_benefit = green_roof_benefits - green_roof_cost
#                best_conv = roof_cost_at_20yrs
#
#        
#        if(best_benefit > 0):
#            green_ins.update{index : 1} #this green roof variable can be stored in the final
#            else:
#                green_ins.update{index : 1}
#             
#        roof_cost_at_20yrs_dict.update({index : best_conv})
#        green_roof_benefit_dict.update({index : best_green_benefits})
#        green_roof_cost_dict.update({index : best_green_cost})
#        green_roof_net_benefit_dict.update({index : best__green_net_benefit})
#    
    #Print results
#    employee = pd.Series(employed_dict)
#    rents = pd.Series(rent_dict)
#    vacancies = pd.Series(vacant_dict)
#    roofinstalled = pd.Series(roofinstalled_dict)
#    employment_density = pd.Series(employment_density_dict)
#    incomes = pd.Series(income_dict)
#    project_cost = pd.Series(project_cost_dict)
#    green_roof_benefit = pd.Series(green_roof_benefit_dict)
#    green_roof_cost = pd.Series(green_roof_cost_dict)
#    green_roof_net_benefit = pd.Series(green_roof_net_benefit_dict)
#    property_values = pd.Series(property_value_dict)
#    conv_roof_maintenance = pd.Series(roof_cost_at_20yrs_dict)
#    buildings = pd.DataFrame({"income": incomes, "job" : employed_dict,"job density": employment_density_dict, "prop val": property_value_dict, "green ins" : roofinstalled_dict, "green ben" : green_roof_benefit_dict, "green cost" : green_roof_cost_dict, "green net": green_roof_net_benefit_dict, "rent": rent_dict, "vacant" : vacancies, "conv maintain" :conv_roof_maintenance})
#        buildings.to_csv("tornoto_greenroof.csv")
#    return "Check tornoto_greenroof.csv"



############################
############################
#CHICAGO STYLE POLCIY TESTS
############################
############################



#def ChicagoGreenRoof():
#    index = 0
#    for(all buildings in the table):
#        index += 1 #this is used as a tracker to create the data table
#        
        #Initialization of assumed and derived variables
#        green_cost_per_sqft = 12
#        green_roof_min = 0
#        building_size = parcel_size * parcel_coverage
#        conventional_cost_per_sqft = green_cost_per_sqft/2
#        green_roof_benefits = 0
#        building_age = 40
#        annual_benefit_per_area = 1.23
#        annual_maintenance_costs_per_area = 0.02 
#        min_green_area = green_roof_min * building_size
#        min_green_cost = green_roof_min * green_cost_per_sqft
#        min_green_benefits= green_roof_min*building_size*annual_benefit_per_area*building_age
#        best_size = green_roof_min
#        best_benefit = min_green_benefits - min_green_cost
#        best_conv = (building_size*(1-green_roof_min)*conventional_cost_per_sqft) #Avoid capital costs
#        discount = 0.05 #Chicago offers $0.05 off building fees per sqft of green roofing
#
#        #If the building is large enough to allow bulk discounting to begin (happens in most cases)
#        if (building_size > 500):
#            green_cost_per_sqft = 23.907*(green_cost_per_sqft**(-0.078))


#        min_green_area = green_roof_min * building_size 
#        min_green_cost = green_roof_min * green_cost_per_sqft 
#        min_green_benefits = green_roof_min*building_size*annual_benefit_per_area*green_roof_life
#        best_size = green_roof_min
#        best_benefit = min_green_benefits - min_green_cost
#
#        for current_size in my_range(green_roof_min, 1.01, 0.01):
#            initial_benefit = discount*current_size*building_size #Discounts from Chicago
#            roof_cost_at_20yrs = (building_size*(1-current_size)*conventional_cost_per_sqft) #Avoid capital costs
#            green_roof_cost = current_size * building_size * green_cost_per_sqft + (green_roof_life * annual_maintenance_costs_per_area * #building_size * current_size)
#            green_roof_benefit = (green_roof_life * annual_benefit_per_area * building_size * current_size) + initial_benefit  + roof_cost_at_20yrs
#            if(green_roof_benefits - green_roof_cost > best_benefit): 
#                best_size = current_size
#                best_benefit = green_roof_benefit - green_roof_cost
#                roof_cost_at_20yrs_dict[index] = roof_cost_at_20yrs
#                green_roof_benefit_dict[index] = best_benefit
#                green_roof_cost_dict[index] = green_roof_cost
#        
#        if(best_benefit > 0):
#            green_ins.update{index : 1} #this green roof variable can be stored in the final
#            else:
#                green_ins.update{index : 1}
#            
#
#        roof_cost_at_20yrs_dict.update({index : best_conv})
#        green_roof_benefit_dict.update({index : best_benefit})
#        green_roof_cost_dict.update({index : green_roof_cost})
#        green_roof_net_benefit_dict.update({index : green_roof_net_benefit})
# 
#    #Print results
#    employee = pd.Series(employed_dict)
#    rents = pd.Series(rent_dict)
#    vacancies = pd.Series(vacant_dict)
#    roofinstalled = pd.Series(roofinstalled_dict)
#    employment_density = pd.Series(employment_density_dict)
#    incomes = pd.Series(income_dict)
#    project_cost = pd.Series(project_cost_dict)
#    green_roof_benefit = pd.Series(green_roof_benefit_dict)
#    green_roof_cost = pd.Series(green_roof_cost_dict)
#    green_roof_net_benefit = pd.Series(green_roof_net_benefit_dict)
#    property_values = pd.Series(property_value_dict)
#    conv_roof_maintenance = pd.Series(roof_cost_at_20yrs_dict)
#    buildings = pd.DataFrame({"income": incomes, "job" : employed_dict,"job density": employment_density_dict, "prop val": #property_value_dict, "green ins" : roofinstalled_dict, "green ben" : green_roof_benefit_dict, "green cost" : green_roof_cost_dict, "green net": green_roof_net_benefit_dict, "rent": rent_dict, "vacant" : vacancies, "conv maintain" :conv_roof_maintenance})
#    buildings.to_csv("chicago_greenroof.csv")
#    return "Check chicago_greenroof.csv"
#    