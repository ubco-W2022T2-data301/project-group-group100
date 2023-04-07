import pandas as pd
import os

def load_and_process(file_path):
    # Use os.path.join() to build file path on any operating system
    full_file_path = os.path.join(os.getcwd(), file_path)
    
    # Load data from CSV file
    df = pd.read_csv(full_file_path)
    
    # Extract year from file_path
    year = int(os.path.basename(file_path).split('.')[0][-4:])
    
    # Clean and preprocess data
    if year in [2015, 2016]:
        df = df.drop(['Standard Error'], axis=1)
    elif year == 2017:
        df = df.drop(['Whisker.high', 'Whisker.low'], axis=1)
        df = df.rename(columns={'Happiness.Rank': 'Happiness Rank' , 'Happiness.Score': 'Happiness Score'
                                ,'Economy..GDP.per.Capita.': 'Economy (GDP per Capita)', 'Health..Life.Expectancy.': 'Health (Life Expectancy)'
                                , 'Trust..Government.Corruption.': 'Trust (Government Corruption)', 'Dystopia.Residual': 'Dystopia Residual',
                                'Freedom': 'Freedom to make life choices'})
        df['Region'] = df['Country'].map(pd.read_csv('country_regions.csv').set_index('Country')['Region'])
    elif year in [2018, 2019]:
        df = df.rename(columns={'Country or region': 'Country', 'GDP per capita': 'Economy (GDP per Capita)',
                                'Healthy life expectancy':'Health (Life Expectancy)', 'Score': 'Happiness Score',
                                'Overall rank': 'Happiness Rank'})
        df['Region'] = df['Country'].map(pd.read_csv('country_regions.csv').set_index('Country')['Region'])
    elif year in [2020, 2021]:
        df = df.drop(['upperwhisker', 'lowerwhisker','Standard error of ladder score'], axis=1)
        df = df.rename(columns={'Country name' : 'Country', 'Ladder score': 'Happiness Score', 'Regional indicator': 'Region',
                                'Overall rank': 'Happiness Rank'})
    elif year == 2022:
        df = df.drop(['Whisker-high', 'Whisker-low'], axis=1)
        df = df.rename(columns={'RANK': 'Happiness Rank','Happiness score': 'Happiness Score'})
        df['Dystopia (1.83) + residual'] = df['Dystopia (1.83) + residual'].str.replace(',', '.').astype(float)
        df['Explained by: GDP per capita'] = df['Explained by: GDP per capita'].str.replace(',', '.').astype(float)
        df['Explained by: Healthy life expectancy'] = df['Explained by: Healthy life expectancy'].str.replace(',', '.').astype(float)
        df['Explained by: Freedom to make life choices'] = df['Explained by: Freedom to make life choices'].str.replace(',', '.').astype(float)
        df['Explained by: Generosity'] = df['Explained by: Generosity'].str.replace(',', '.').astype(float)
        df['Explained by: Perceptions of corruption'] = df['Explained by: Perceptions of corruption'].str.replace(',', '.').astype(float)
        df['Explained by: Social support'] = df['Explained by: Social support'].str.replace(',', '.').astype(float)
        df['Region'] = df['Country'].map(pd.read_csv('country_regions.csv').set_index('Country')['Region'])
        
    df.insert(2, 'year', year)
    df['Country'] = df['Country'].replace('United States', 'United States of America')

    return df

