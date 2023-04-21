# Final Report

### Introduction:

Our project aimed to analyze global happiness patterns and correlates using the World Happiness Report 2015-2022 dataset. We examined the relationship between happiness levels, economic factors, and demographic variables, identified geographical variations, and pinpointed critical intervention areas. Our goal was to offer insights into key happiness-contributing factors and promote data-driven policy-making to enhance well-being outcomes worldwide. We deemed our project significant due to its potential to inform policymakers and stakeholders about critical happiness-influencing elements and identify intervention areas to promote well-being outcomes.

Here are the links for the notebooks we used:
-  [Analysis 1](https://github.com/ubco-W2022T2-data301/project-group-group100/blob/main/analysis/student1/analysis1.ipynb)
-  [Analysis 2](https://github.com/ubco-W2022T2-data301/project-group-group100/blob/main/analysis/student2/analysis2.ipynb)

### Exploratory Data Analysis: 

During our initial exploratory data analysis, we uncovered interesting happiness patterns and trends across various countries and regions. We utilized visualization techniques, such as bar charts, scatter plots, and choropleth maps, to investigate the relationships between happiness scores and the dataset's different contributing factors. These visualizations enabled us to identify potential areas for further investigation.

The first chart is a horizontal bar chart that groups the top 10 happiest countries by region and color-codes them accordingly. This chart helps us understand which regions exhibit the highest overall happiness levels and compare the top 10 countries from each region. By doing so, we identified regions that may require more attention regarding overall well-being and key intervention areas.

![](/images/1EDA1.png)

The second chart is a stacked horizontal bar chart displaying the factors contributing to overall happiness in the top 10 happiest countries. Identifying the most impactful contributing factors allowed us to gain insights into which areas require more attention and key intervention areas. This chart was useful for answering our research question by visually representing overall happiness contributing factors in the top 10 happiest countries. 

![](/images/1EDA2.png)

Upon analyzing the available data, we inferred that social support is positively and strongly correlated with happiness scores. The correlation between these two variables can be considered moderate to strong, with a significant number of data points ranging from 0.8 to 1.0.Numerous studies have demonstrated that social support is a critical determinant of individual well-being and happiness. Social support can be defined as emotional, instrumental, or informational resources provided by individuals' social networks. These resources can help individuals cope with stress and adversity, enhance their sense of belonging, and foster positive relationships.

![](/images/2EDA1.png)

By analyzing the chart, it is clear that mean happiness scores vary across regions over time, with North America and Western Europe consistently exhibiting high scores. To investigate the factors contributing to these regions' higher happiness levels, we conducted a comparative analysis of various metrics, such as economic indicators, social support systems, health outcomes, and environmental factors. This analysis can provide valuable insights into promoting well-being and happiness in other regions and potentially leading to more equitable global happiness levels.

![](/images/2EDA2.png)

### Question 1 + Results
**Is there a significant correlation between different factors that contribute to overall happiness, such as income, social support, freedom, generosity, and corruption, and how can this correlation be used to identify key areas for intervention? Additionally, what evidence-based interventions could be implemented to enhance these key areas and promote sustained and equitable well-being outcomes over time?**

We created visualizations, such as scatter plots and correlation matrices, to analyze the relationships between happiness scores and contributing factors. Our findings indicated strong positive correlations between happiness scores and GDP per capita, social support, and life expectancy. Conversely, weaker correlations were found between happiness and generosity or perceptions of corruption.

The box plot displays the distribution of happiness scores across different regions. Each region is represented by a colored box, showing the interquartile range (IQR) and the median happiness score. The chart reveals that Northern America and ANZ has the highest median happiness score, while  Western Europe follows second with a 0.056 points difference in median score. South Asia has the lowest. Notably, there is considerable variation in happiness scores within each region.

![](/images/1RQ1.png)

In this 3D scatter plot, K-means clustering has grouped countries into seven clusters based on generosity, healthy life expectancy, and perceptions of corruption. The distinct separation between clusters indicates that these features effectively capture variations in happiness across different countries. The more densely packed clusters, such as the one in the bottom left corner, suggest that countries within those groups exhibit similar levels of generosity, healthy life expectancy, and corruption perceptions. This is particularly relevant as it highlights the importance of these factors in shaping national happiness levels.

Countries in the densely packed cluster at the bottom left corner might include less developed countries or those facing social and economic challenges, such as Afghanistan, Yemen, or Haiti. These countries tend to exhibit lower levels of generosity, healthy life expectancy, and higher perceptions of corruption. In contrast, countries in the more dispersed clusters could include developed nations with better socioeconomic conditions, such as Norway, Switzerland, or Denmark. These countries generally have higher levels of generosity, healthy life expectancy, and lower perceptions of corruption.

![](/images/1RQ2.png)

The 3D scatter plot displays regions based on generosity, healthy life expectancy, and perceptions of corruption. North America and ANZ and Western Europe stands out with high healthy life expectancy, low corruption perception, and moderate generosity. Conversely, Sub-Saharan Africa has lower healthy life expectancy, higher corruption perception, and varied generosity levels. South Asia and the Middle East and North Africa share similar patterns, with low healthy life expectancy and high corruption perception. Central and Eastern Europe, and Latin America and the Caribbean demonstrate intermediate values, indicating regional differences in happiness determinants.

![](/images/1RQ3.png)

In conclusion, our analysis of the happiness dataset and various visualizations have shown a significant correlation between factors such as income, social support, freedom, generosity, and corruption, and overall happiness. The stacked bar chart of the 10 least happy countries provided insights into the contributing factors, highlighting the importance of GDP per capita, social support, and healthy life expectancy. The scatter plots and clustering further emphasized regional differences in these factors, revealing specific patterns and potential areas for intervention.

The K-means clustering and 3D scatter plots showcased distinct clusters, helping us identify countries and regions that share common characteristics in terms of happiness and its contributing factors. This knowledge can guide policymakers in designing targeted interventions to enhance key areas and promote equitable well-being outcomes.

Our analysis suggests that interventions focusing on enhancing economic prosperity, social support networks, and health outcomes can significantly improve overall happiness levels. Some evidence-based interventions to consider include:

1. **Economic prosperity**: Implementing policies that promote economic growth, job creation, and social mobility can improve living standards and enhance overall well-being.
2. **Social support networks**: Strengthening social connections through community-based programs, mental health support, and social services can foster a sense of belonging and enhance well-being.
3. **Health outcomes**: Investing in quality healthcare, health promotion, and preventive measures can lead to improved physical and mental health, contributing to higher happiness levels.

To promote sustained well-being outcomes over time, it is essential to focus on a multi-faceted approach that encompasses economic development, social support systems, healthcare, education, and good governance. By understanding the correlations between these factors and happiness, policymakers can develop and implement more effective interventions, ultimately improving the quality of life for their citizens.


### Question 2 + Results
**How do different factors contributing to happiness, such as income, social support, freedom, and corruption, vary across different regions in the world, and how do these regional differences affect overall levels of happiness and life satisfaction?**

We used choropleth maps to visualize the geographical distribution of happiness levels. The maps demonstrated that regions such as North America, Western Europe, and Oceania consistently exhibit high happiness scores, whereas regions like Sub-Saharan Africa, South Asia, and parts of Eastern Europe and Central Asia display lower scores.

The bar graph depicting the Mean Logged GDP per capita score by region highlights North America and Western Europe as the leading regions in terms of economic prosperity. This observation aligns with previous research that has established a positive correlation between GDP per capita and overall well-being. While economic prosperity is an important determinant of happiness, it is essential to consider other factors such as social support, health outcomes, and environmental sustainability, which also contribute to well-being. Therefore, policymakers and stakeholders must strive for a comprehensive approach to promoting happiness and well-being, considering a range of factors that vary across regions.

![](/images/2RQ.png)

The world map visualization served as a powerful tool in our investigation of the variations in happiness levels across different regions of the world. Our analysis revealed that the regions of Western Europe and North America emerged as the frontrunners in terms of happiness levels. This discovery aligns with previous research that has identified a range of factors, such as robust social support systems, high GDP per capita, and personal freedom, as key contributors to overall well-being.

![](/images/2RQ2.png)

The bar graph showcasing the Mean Social Support Score by region serves as a testament to the integral role of social support systems in fostering overall well-being. Our analysis revealed that the regions of North America and Western Europe emerged as the leaders in social support scores, indicative of their robust social structures, emphasis on community engagement, and effective public policies. 

![](/images/2RQ3.png)

After a comprehensive analysis of the visualizations and bar graphs presented, it is clear that North America and Western Europe currently have the highest happiness levels among all the regions in the world. Our investigation revealed that this finding is attributed to several factors, including North America's leadership in Logged GDP per capita, Healthy Life Expectancy, Ladder Score in Dystopia, and Social Support. Additionally, Western Europe's top-ranking factors include Economy (GDP per capita), Health (Life Expectancy), and Trust in Government (perceptions of corruption).

These findings emphasize the significant role played by economic and social factors in determining the happiness levels of different regions. Policymakers and stakeholders can utilize this information to develop effective interventions that target the specific needs and challenges of different regions and promote overall well-being. Further research can shed more light on the specific factors driving these observed trends, contributing to the development of more comprehensive and targeted policy decisions aimed at improving the well-being of populations worldwide.

### Summary/Conclusion

In conclusion, our project provided valuable insights into global happiness patterns and correlates, highlighting key areas for intervention. Our findings suggest that economic prosperity, social support networks, and health outcomes play significant roles in determining overall happiness levels. Therefore, evidence-based interventions targeting these key areas can promote sustained and equitable well-being outcomes worldwide. Additionally, the identified geographical disparities in happiness warrant region-specific interventions to address unique regional challenges and foster global happiness equity.

By using data-driven approaches, policymakers and stakeholders can make informed decisions to enhance well-being and improve the quality of life for individuals worldwide. Our project's findings contribute to the ongoing conversation around happiness and well-being, emphasizing the importance of addressing both global and regional factors that influence happiness levels.

### Future Research Directions

Although our project provided valuable insights, there are several opportunities for future research to explore further:

1. **Longitudinal analysis**: Examining trends in happiness and its correlates over time can provide insights into the temporal dynamics of happiness and its determinants. This can inform targeted interventions that adapt to evolving contexts and challenges.
2. **Subnational analysis**: Investigating happiness patterns and contributing factors at subnational levels (e.g., cities, states, provinces) can reveal additional insights into intra-country disparities and potential intervention points.
3. **Cultural factors**: Exploring the role of cultural factors in shaping happiness perceptions and experiences can offer a more nuanced understanding of well-being across different societies.
4. **Policy impact analysis**: Assessing the impact of specific policies and interventions on happiness outcomes can help identify best practices and refine policy recommendations.

### Limitations

Our study has several limitations that should be considered when interpreting the findings:

1. **Data quality**: The happiness scores and contributing factors are based on survey data, which may be subject to biases and measurement errors. Additionally, data availability varies across countries, which can affect the comprehensiveness of our analysis.
2. **Causality**: The correlations identified in our study do not imply causality. Further research is needed to establish causal relationships between the contributing factors and happiness outcomes.
3. **Unmeasured factors**: Our analysis focused on a limited set of factors, which may not capture the full complexity of happiness determinants. Other factors, such as political stability, environmental quality, and cultural values, could also play a role in shaping happiness levels.

Despite these limitations, our project contributes to a growing body of research on happiness and well-being, providing valuable insights for policymakers and stakeholders seeking to enhance quality of life worldwide.
