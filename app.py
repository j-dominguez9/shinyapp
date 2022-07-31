from shiny import ui, render, App
import pandas as pd
import seaborn as sns


choices = {"a": "Age", "b": "Income", "c": "Hours Worked", "d": "Education", "e": "Race", "f": "Marital Status", "g": "Gender", "h": "Work Class"}

app_ui = ui.page_fluid(
    ui.h2({"style": "text-align: center;"}, "Cluster Analysis"),
   
   ui.layout_sidebar(
   
    ui.panel_sidebar(
        ui.input_select("x1", "Select Attribute", choices),
        ui.row(
        ui.column(
            12,
            ui.div(
                {"class": "app-col"},
                """
                To obtain a better understanding of how
                the clusters are grouping different attributes, please 
                explore the most important 
                variables in the logistic regression classification of income.
                """,
            ),
        ),
    )
      ),
    
    ui.panel_main(
        ui.output_plot("plot")
    ),
   ),
)


def server(input, output, session):
    @output
    @render.plot
    def plot():
        df_clean = pd.read_csv('https://raw.githubusercontent.com/j-dominguez9/ML1_Proj1/main/Data/census_clean.csv')
        
        df_viz = df_clean.copy()

        X = pd.read_csv('https://raw.githubusercontent.com/j-dominguez9/ML1_Proj1/main/Data/X.csv')
        combinedDf = pd.read_csv('https://raw.githubusercontent.com/j-dominguez9/ML1_Proj1/main/Data/combinedDf.csv')

        if input.x1() == "a":
            fig = sns.boxplot(x=combinedDf['cluster_predicted'],y = combinedDf['age'])
            return fig

        elif input.x1() == "b":
            fig2 = sns.countplot(x=combinedDf['income'],order=combinedDf['income'].value_counts().index,hue=combinedDf['cluster_predicted'])
            return fig2

        elif input.x1() == "c":
            fig3 = sns.boxplot(x=combinedDf['cluster_predicted'],y = combinedDf['hours-per-week'])
            return fig3

        elif input.x1() == "d":
            fig4 = sns.countplot(x=combinedDf['educational-num'],order=combinedDf['educational-num'].value_counts().index,hue=combinedDf['cluster_predicted'])
            return fig4

        elif input.x1() == "e":
            fig5 = sns.countplot(x=combinedDf['race'],order=combinedDf['race'].value_counts().index,hue=combinedDf['cluster_predicted'])
            return fig5
        
        elif input.x1() == "f":
            fig6 = sns.countplot(x=combinedDf['marital-status'],order=combinedDf['marital-status'].value_counts().index,hue=combinedDf['cluster_predicted'])
            return fig6

        elif input.x1() == "g":
            fig7 = sns.countplot(x=combinedDf['gender'],order=combinedDf['gender'].value_counts().index,hue=combinedDf['cluster_predicted'])
            return fig7

        elif input.x1() == "h":
            fig8 = sns.countplot(x=combinedDf['workclass'],order=combinedDf['workclass'].value_counts().index,hue=combinedDf['cluster_predicted'])
            return fig8



app = App(app_ui, server)