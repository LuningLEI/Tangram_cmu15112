import os
os.getcwd()
os.name
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

thyroid_default_data = pd.read_csv("Thyroid_Diff.csv")
data = thyroid_default_data

##### OverView ######

# size 
def get_size(data):
    number_of_columns = len(data.columns)
    number_of_rows = data.Gender.value_counts()
    return number_of_columns, number_of_rows

numerical = data.select_dtypes(exclude=['object']).columns.tolist()
categorical = data.select_dtypes(include=['object']).columns.tolist()

# column distribution 
def column_distribution(data):
    for column in data.columns:
        series = data[column]
        if column in numerical: 
            # PLOT
            sns_plot = sns.histplot(series, kde= True)
            sns_plot.figure.savefig(f'Figure/OverView/{column}.png',bbox_inches='tight',dpi=300)
            # Info
            information = series.describe()
            print(information)
        elif column in categorical:
            # PLOT
            drawPie(data, column)
            # Info
            information = series.value_counts()
            print(information)
            drawPie(data, column)

def drawPie(data, column):
    value_counts = data[column].value_counts()
    labels = value_counts.index.tolist()
    sizes = value_counts.values.tolist()
    fig, ax = plt.subplots()
    patches, texts= plt.pie(sizes,startangle=140)
    # Creat the Legend
    total = sum(sizes)
    percentages = [(i / total) * 100 for i in sizes]
    legend_labels = ['{0} - {1:1.1f} %'.format(i, j) for i, j in zip(labels, percentages)]
    plt.legend(patches, legend_labels, title = column, loc=0, bbox_to_anchor=(1, 0, 0.5, 1))
    ax.axis('equal') 
    fig.set_size_inches(4, 3)
    plt.savefig(f'Figure/OverView/{column}.png',bbox_inches='tight',dpi=300)
    plt.close()

# column_distribution(data)

############## Relationship with Response Variable ##################
def potential_explanatory_variable(data):
    for column in data.columns[:-1]:
        if column in numerical: 
            figure = sns.boxplot(data = data, x = "Recurred", y = column)
            figure.set_title(f'Bar plot of {column} vs Recurred')
            figure.set_xlabel('Recurred')
            figure.set_ylabel(column)
            plt.savefig(f'Figure/Relationship/Boxplot/{column} vs Recurred.png',bbox_inches='tight',dpi=300)
            plt.close()
        elif column in categorical:
            print(column)
            # Percentage Plot
            percentage_df = data.groupby(column)['Recurred'].mean()*100
            percentage_df = percentage_df.reset_index()
            percentage_df.columns = ['Category', 'Percentage']
            plt.figure(figsize=(10, 6))
            sns.barplot(x='Category', y='Percentage', data=percentage_df)
            plt.xlabel(column)
            plt.ylabel('Percentage of Yes (%)')
            plt.title(f'Percentage of Yes by Category in {column}')
            plt.savefig(f'Figure/Relationship/Percentage/{column} vs Recurred.png',bbox_inches='tight',dpi=300)
            plt.close()
        # #Heatmap
        # contingency_table= pd.crosstab(data["Recurred"],data[column])
        # figure = sns.heatmap(contingency_table, annot=True, cmap="coolwarm", fmt="d", linewidths=.5)
        # figure.set_title(f'Heatmap of {column} vs Recurred')
        # figure.set_ylabel('Recurred')
        # figure.set_xlabel(column)
        # plt.savefig(f'Figure/Relationship/Heatmap/{column} vs Recurred.png',bbox_inches='tight',dpi=300)
        # plt.close()



###############
Recurred = data.Recurred.replace("No",0)
data["Recurred"] = Recurred
Recurred = data.Recurred.replace("Yes",1)
data["Recurred"] = Recurred
potential_explanatory_variable(data)

data = thyroid_default_data.rename(columns={"Physical Examination":"Physical_Examination","Thyroid Function":"Thyroid_Function","Hx Radiothreapy":"Hx_Radiothreapy","Hx Smoking":"Hx_Smoking"})
data.to_csv("renamed_thyroid.csv",index = False)

