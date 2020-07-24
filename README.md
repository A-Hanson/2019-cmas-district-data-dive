# 2019 District Level Science CMAS Data EDA

## Background and Motivation
Each spring, students from around Colorado sit in silent classrooms; taking standardized tests for hours, days on end, over several weeks. These tests are created in a collaboration between the Colorado Department of Education (CDE), Pearson Learning, and educators. Students test on Math and English Language arts every year, and Science in grades 5, 8, and 11. The results come back usually by late Summer, and then 'data dives' into their schools' scores are part of a teacher's professional development week before students return. 

How a school performs on these tests affects how they are [graded by the CDE](https://www.cde.state.co.us/accountability/2019-framework-scoring-guide_080319). Schools that continuously fail to meet certain benchmarks can be in danger of being [shut down](https://co.chalkbeat.org/2020/1/9/21109391/state-delays-final-decision-on-hope-online-but-steers-away-from-closure) or intervention from the state. The overall performance of a school is one of the metrics that is used to evaluate principals, which they then use to strategize how to run their schools.
<p align="center">
    <img src = "images/CMAS_overall_score_ranges.png">
</p>

**Personal bias:** I have taught in mainly low-performing schools. My very first year teaching was in a school that was being phased out due to its low performance. It is difficult to get buy-in from the students to perform well when there is no actual application to their life. How can I tell Student X that this is important to him? I know it isn't. It's important to my boss, who then makes it important in my life. 

---

## Data
The CDE releases the yearly results on their [website](https://www.cde.state.co.us/assessment/cmas-dataandresults-2019). I downloaded the 2019 CMAS Science District and School Overall Results in an excel file.

*Snapshot of the data the excel format:*
<p align="center">
    <img src="images/raw_excel_data_1.png">
</p>

The original dataset has more than 4,700 rows of data on State, District, and School level data. Certain data was obsurced using '< 16' or '- -' for student privacy if there were less than 16 values. 

*Snapshot of the data the excel format with '< 16' values:*
<p align="center">
    <img src="images/raw_excel_data_2.png">
</p>

Most of the records include information such as:
* Participation Rate
* Mean Scale Score for 2019 and 2018
* Change in Percent Met or Exceeded Expectations from 2018 to 2019
* Number and Percentage of Scores in each of the following categories:

<center>

| Partially Met Expectations | Approached Expectations | Met Expectations | Exceeded Expectations |
| -------------------------- | ----------------------- | ---------------- | ------------ |

</center>

<p>&nbsp;</p>
<p>&nbsp;</p>

*Snapshot of the School District Level data:*
<p align="center">
    <img src="images/district_raw_data_snapshot.png">
</p>


---

# Exploratory Data Analysis
## Looking for patterns in the data
To get an idea if there were any correlations between participation rate and the different test scores, I did a PairPlot Analysis. Since four of the variables were related through them being percentages of the overall performance, I didn't really see anything that jumped out at me initially. 
<p align="center">
    <img src="images/district_pair_plot_participation_and_scores.png">
</p>


## Participation Rate and Test Scores
Next, I set out to explore the relationship between a district's participation rate and their test scores. I set each district's All School Participation Rate against their Mean Scaled Score. In order to see clearly which districts were performing well, I set a horizontal line at the minimum overall score (650) for the Met Expectations category.
<p align="center">
    <img src="images/district_participation_mean_scores.png">
</p>

---

# Binomial Tests

Seeing the graph showing so few districts having their average score place at or above the bench mark for meeting grade level expectations got me thinking about just the scores. 
What we know:
* There are four categories in which scores can fall
* To be considered at or above grade level, students must score in the Met or Exceeded Expectations category.
    * 650 or higher

What we assume:
* If the test is representative of the population, then 50 percent of districts should meet or exceed expectations.

I perfomed a Binomial Test using the Mean Scale Score for each district, passing if it was greater than or equal to 650. My null hypothesis was that the **probability of a district passing or not being 0.5**. I set an **alpha of 0.2.**
<p align="center">
    <img src="images/FiftyFiftyBinomialTest.png">
</p>

*My p-value returned at 1.0, leading me to reject my null hypothesis.*
<p>&nbsp;</p>

---

<p>&nbsp;</p>
Curious now what a reasonable probability might be, I set out to find the probability that I could fail to reject my null hypothesis.
<p align="center">
    <img src="https://media.giphy.com/media/lTdjcxRUQXeqPfMtpc/giphy.gif">
</p>
<p>&nbsp;</p>

---

<p>&nbsp;</p>

At a probability of **0.019**, I had a **p-value of 0.199** and was able to reject my null hypothesis.
<p align="center">
    <img src="images/FinalBinomialTest.png">
</p>

#### Who were these high performing districts?
* Cheyenne Mountain 12
* Swink 33
* Ridgeway R-2
* Steamboat Springs RE-2
* Idalia RJ-3

# Next Steps
Given more time I would like to expand this initial dive into the following areas:
* Use the passing value of 50% or more Met or Exceeded expectations on the district level data
* Investigate using the Binomial test on the the individual schools' mean scores
* Compare the schools within each district to one another