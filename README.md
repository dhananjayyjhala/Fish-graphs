**1. What figure did you set out to make? In words, what do you want this figure to show?**

I wanted to create grouped bar charts comparing the recorded abundance of different fish species between reefs during 
January. Species appear on the horizontal axis, abundance on the vertical axis, and different colours distinguish the reefs.

Code 1 creates a separate panel for each transect, allowing comparisons between reefs within each transect and showing
whether patterns differ across transects. Code 2 combines all January observations into one chart, showing the total
recorded abundance of each species at each reef. Together, the figures provide both a detailed view and an overall summary.
The bars represent summed counts, rather than averages or estimates of fish density.

**2. How easy or hard was it to actually make this figure? What went smoothly, what didn’t? How were you able to solve
any difficulties?**
Over all the process was smooth, with constant comments mentioning exactly what each line was doing, it was relatively easy 
to follow, and understand the working of the code. There were a few small issues that arose, such as the code output being 
exactly the same even after changing the month from January to February in the loop, this was sorted by attributing this to a 
specific month variable at the start (could not figure out why this happened though). 


**3. How much do you feel like you understand the code used to generate the figure? Was anything particularly useful 
for better understanding the code that was generated?**

I understand the main sequence: read the dataset, select the relevant month, add abundance values into the appropriate 
groups, and plot those totals. I also understand how the titles, axis labels, colours, and legend communicate the 
comparisons.

The nested dictionaries, set comprehensions, and calculations used to position the grouped bars required closer reading.
The explanatory comments were particularly useful because they connected each section of code to its purpose.
Comparing the two scripts also helped: the overall chart groups observations by reef and species, while the more detailed 
version adds transect as another grouping level.

**4. What steps did you use to try and verify for yourself that the figure you created is correctly showing what you 
want it to?**

I checked the month filter and grouping instructions to confirm that the scripts select January observations and 
sum abundance into the intended categories. I also checked that the species labels and plotted values use the same 
species order, and that the legend identifies each reef.

For a numerical check, I would manually sum a few species’ January counts from the CSV and compare them with the
corresponding bars. I would also check that adding a species’ counts across the transect panels gives its total 
in the combined chart for the same reef.

An additional consideration is that the code assigns zero to combinations without a recorded value. I would check
whether these represent genuine non-detections or missing sampling before interpreting them as absence. Likewise, 
comparisons of total counts between reefs require consideration of whether sampling effort was comparable.
