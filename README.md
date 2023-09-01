# UV-Vis-plot-automation

UV-Vis plot by Tauc plot method can be tedious when we have many absorption spectra to plot. Here, I automated the Tauc plot for all txt files contained in a folder. 
Observe the type of the file and the way it should be right the one below:

300.00	1.032
300.50	1.029
301.00	1.034
301.50	1.029
302.00	1.028
302.50	1.030
303.00	1.027
303.50	1.029
304.00	1.029
304.50	1.027
305.00	1.027
305.50	1.035
306.00	1.030

If your file is different, please rewrite.
These Tauc plots don't consider the baseline of the intermediate states. If you want to plot like that, a different algorithm should be written.
