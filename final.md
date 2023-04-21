# Final Report

### Introduction:

Our project aimed to explore global patterns and correlates of happiness using the World Happiness Report 2015-2022 dataset. We investigated the relationship between happiness levels and economic and demographic variables, identified geographical variations, and pinpointed critical areas for intervention. The purpose of our project was to provide insights into the key factors that contribute to happiness levels and promote data-driven policy-making to improve well-being outcomes on a global scale. We believed that our project was important because it had the potential to inform policymakers and stakeholders about the critical elements that influence happiness levels and to identify areas for intervention to promote well-being outcomes.

Here are the links for the notebooks we used:
-  [Analysis 1](https://github.com/ubco-W2022T2-data301/project-group-group100/blob/main/analysis/student1/analysis1.ipynb)
-  [Analysis 2](https://github.com/ubco-W2022T2-data301/project-group-group100/blob/main/analysis/student2/analysis2.ipynb)

### Exploratory Data Analysis: 

Our initial exploratory data analysis revealed interesting patterns and trends in happiness levels across different countries and regions. We used various visualization techniques, such as bar charts, scatter plots, and choropleth maps, to explore the relationships between happiness scores and the different contributing factors included in the dataset. These visualizations allowed us to identify potential areas for further investigation.

First chart is a horizontal bar chart that groups the top 10 happiest countries by region and color-codes them accordingly. This chart is useful for gaining a deeper understanding of which regions have the highest levels of overall happiness and how the top 10 countries from each region compare to one another. By completing this task, we identified which regions may require more attention in terms of promoting overall well-being and identify key areas for intervention.

![](/images/1EDA1.png)

Second chart is a stacked horizontal bar chart that displays the factors that contribute to overall happiness in the top 10 happiest countries. By identifying the contributing factors that have the most impact on overall happiness, we gained insights into which areas require more attention and identify key areas for intervention. This chart wass useful for answering our research question by providing a visual representation of the contributing factors to overall happiness in the top 10 happiest countries.

![](/images/1EDA2.png)

After analyzing the available data, it can be inferred that social support is strongly and positively correlated with happiness score. The correlation between these two variables can be considered moderate to strong, as a significant number of data points fall within the range of 0.8 to 1.0.

Various studies have shown that social support is a critical determinant of individual well-being and happiness. Social support can be defined as the availability of emotional, instrumental, or informational resources provided by individuals' social networks. These resources can help individuals cope with stress and adversity, enhance their sense of belonging, and foster positive relationships.

![](/images/2EDA1.png)

Upon analyzing the chart, it is evident that mean happiness scores vary across regions over time, with North America and Western Europe exhibiting consistently high scores. To investigate the factors contributing to these regions' higher happiness levels, a comparative analysis of various metrics, such as economic indicators, social support systems, health outcomes, and environmental factors, will be conducted. This analysis can provide valuable insights into promoting well-being and happiness in other regions and potentially lead to more equitable global happiness levels.

![](/images/2EDA2.png)

### Question 1 + Results
**Is there a significant correlation between different factors that contribute to overall happiness, such as income, social support, freedom, generosity, and corruption, and how can this correlation be used to identify key areas for intervention? Additionally, what evidence-based interventions could be implemented to enhance these key areas and promote sustained and equitable well-being outcomes over time?**

We created visualizations, such as scatter plots and correlation matrices, to analyze the relationships between happiness scores and the contributing factors. Our findings indicated strong positive correlations between happiness levels and factors like income, social support, and freedom, while there were negative correlations with corruption. These results suggest that targeting these key areas for intervention could potentially lead to improved well-being outcomes. Evidence-based interventions could include implementing policies to reduce income inequality, promoting social cohesion, and addressing corruption.

The box plot displays the distribution of happiness scores across different regions. Each region is represented by a colored box, showing the interquartile range (IQR) and the median happiness score. Whiskers indicate the range of scores within 1.5 IQR from the box. The chart reveals that Northern America and ANZ has the highest median happiness score, while  Western Europe follows second with a 0.056 points difference in median score.
South Asia has the lowest. Notably, there is considerable variation in happiness scores within each region.

![](/images/1RQ1.png)

In this 3D scatter plot, K-means clustering has grouped countries into seven clusters based on generosity, healthy life expectancy, and perceptions of corruption. The distinct separation between clusters indicates that these features effectively capture variations in happiness across different countries. The more densely packed clusters, such as the one in the bottom left corner, suggest that countries within those groups exhibit similar levels of generosity, healthy life expectancy, and corruption perceptions. This is particularly relevant as it highlights the importance of these factors in shaping national happiness levels.

Countries in the densely packed cluster at the bottom left corner might include less developed countries or those facing social and economic challenges, such as Afghanistan, Yemen, or Haiti. These countries tend to exhibit lower levels of generosity, healthy life expectancy, and higher perceptions of corruption. In contrast, countries in the more dispersed clusters could include developed nations with better socioeconomic conditions, such as Norway, Switzerland, or Denmark. These countries generally have higher levels of generosity, healthy life expectancy, and lower perceptions of corruption.

![](/images/1RQ2.png)

The 3D scatter plot displays regions based on generosity, healthy life expectancy, and perceptions of corruption. North America and ANZ and Western Europe stands out with high healthy life expectancy, low corruption perception, and moderate generosity. Conversely, Sub-Saharan Africa has lower healthy life expectancy, higher corruption perception, and varied generosity levels. South Asia and the Middle East and North Africa share similar patterns, with low healthy life expectancy and high corruption perception. Central and Eastern Europe, and Latin America and the Caribbean demonstrate intermediate values, indicating regional differences in happiness determinants.

![](/images/1RQ3.png)

In conclusion, our analysis of the happiness dataset and various visualizations have shown a significant correlation between factors such as income, social support, freedom, generosity, and corruption, and overall happiness. The stacked bar chart of the 10 least happy countries provided insights into the contributing factors, highlighting the importance of GDP per capita, social support, and healthy life expectancy. The scatter plots and clustering further emphasized regional differences in these factors, revealing specific patterns and potential areas for intervention.

The K-means clustering and 3D scatter plots showcased distinct clusters, helping us identify countries and regions that share common characteristics in terms of happiness and its contributing factors. This knowledge can guide policymakers in designing targeted interventions to enhance key areas and promote equitable well-being outcomes.

Moreover, the linear regression model demonstrated a reasonably good performance in predicting happiness scores based on the selected features, which can be utilized to inform evidence-based interventions for future improvements in happiness.

To promote sustained well-being outcomes over time, it is essential to focus on a multi-faceted approach that encompasses economic development, social support systems, healthcare, education, and good governance. By understanding the correlations between these factors and happiness, policymakers can develop and implement more effective interventions, ultimately improving the quality of life for their citizens.


### Question 2 + Results
**How do different factors contributing to happiness, such as income, social support, freedom, and corruption, vary across different regions in the world, and how do these regional differences affect overall levels of happiness and life satisfaction?**

We used choropleth maps and regional box plots to visualize happiness levels and their associated factors across different regions of the world. Our analysis revealed substantial regional variations in happiness scores and the key influencing factors. For instance, we found that income and social support tend to be higher in Western countries, while freedom and corruption levels vary more widely across regions. These regional differences could affect overall levels of happiness and life satisfaction, highlighting the importance of considering regional contexts when designing interventions.

The bar graph depicting the Mean Logged GDP per capita score by region highlights North America and Western Europe as the leading regions in terms of economic prosperity. This observation aligns with previous research that has established a positive correlation between GDP per capita and overall well-being. While economic prosperity is an important determinant of happiness, it is essential to consider other factors such as social support, health outcomes, and environmental sustainability, which also contribute to well-being. Therefore, policymakers and stakeholders must strive for a comprehensive approach to promoting happiness and well-being, considering a range of factors that vary across regions.

![](/images/2RQ.png)

The world map visualization served as a powerful tool in our investigation of the variations in happiness levels across different regions of the world. Our analysis revealed that the regions of Western Europe and North America emerged as the frontrunners in terms of happiness levels. This discovery aligns with previous research that has identified a range of factors, such as robust social support systems, high GDP per capita, and personal freedom, as key contributors to overall well-being.

![](/images/2RQ2.png)

The bar graph showcasing the Mean Social Support Score by region serves as a testament to the integral role of social support systems in fostering overall well-being. Our analysis revealed that the regions of North America and Western Europe emerged as the leaders in social support scores, indicative of their robust social structures, emphasis on community engagement, and effective public policies. 

![](/images/2RQ3.png)

#### Results:

After a comprehensive analysis of the visualizations and bar graphs presented, it is clear that North America and Western Europe currently have the highest happiness levels among all the regions in the world. Our investigation revealed that this finding is attributed to several factors, including North America's leadership in Logged GDP per capita, Healthy Life Expectancy, Ladder Score in Dystopia, and Social Support. Additionally, Western Europe's top-ranking factors include Economy (GDP per capita), Health (Life Expectancy), and Trust in Government (perceptions of corruption).

These findings emphasize the significant role played by economic and social factors in determining the happiness levels of different regions. Policymakers and stakeholders can utilize this information to develop effective interventions that target the specific needs and challenges of different regions and promote overall well-being. Further research can shed more light on the specific factors driving these observed trends, contributing to the development of more comprehensive and targeted policy decisions aimed at improving the well-being of populations worldwide.

### Summary/Conclusion

Our analysis of the World Happiness Report 2015-2022 dataset revealed strong relationships between happiness levels and various contributing factors, such as income, social support, freedom, generosity, and corruption. We identified significant regional variations in happiness scores and their influencing factors, which could affect overall levels of happiness and life satisfaction. These insights can be used to guide data-driven policy-making to improve well-being outcomes for individuals and communities. Furthermore, we developed a user-facing dashboard that allows users to explore the dataset and discover patterns and trends related to happiness levels and their correlates
