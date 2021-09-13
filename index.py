#--------------imports--------------#
import pandas as panda, statistics as stats, plotly.express as plotly, plotly.figure_factory as graphs


#--------------code--------------#
# raw materials
data_frame = panda.read_csv(r"C:\Swarup\WhiteHat Jr\Python\Projects\PropertiesNormalDistribution\StudentsPerformance.csv");
math_scores_data = data_frame["math score"].tolist()

# averages
math_scores_mean  = stats.mean(math_scores_data)
math_scores_median  = stats.median(math_scores_data)
math_scores_mode = stats.mode(math_scores_data)
math_scores_deviated = stats.stdev(math_scores_data)

# deviated areas
area_1_start, area_1_end = math_scores_mean-(1*math_scores_deviated), math_scores_mean+(1*math_scores_deviated)
area_2_start, area_2_end = math_scores_mean-(2*math_scores_deviated), math_scores_mean+(2*math_scores_deviated)
area_3_start, area_3_end = math_scores_mean-(3*math_scores_deviated), math_scores_mean+(3*math_scores_deviated)

# deviated areas values
area_1_values = [value for value in math_scores_data if value > area_1_start and value < area_1_end]
area_2_values = [value for value in math_scores_data if value > area_2_start and value < area_2_end]
area_3_values = [value for value in math_scores_data if value > area_3_start and value < area_3_end]

# area percentages
area_1_perentage = len(area_1_values)*100/len(math_scores_data)
area_2_perentage = len(area_2_values)*100/len(math_scores_data)
area_3_perentage = len(area_3_values)*100/len(math_scores_data)

print("--------------- ------------ ------------ \n")
print("The Bell Curve Values of the Following Data Will Be: \n")
print(area_1_perentage, area_2_perentage, area_3_perentage, "\n")
print("--------------- ------------ ------------ \n")

