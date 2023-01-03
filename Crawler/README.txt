A. Use scripts in "Download and Merge DOI Index from WOS (Universal)" to first generate a DOI list for crawler to collect.
B. Place the DOI list file (i.e. HER_list.csv) in the same folder of corresponding crawler script.
C. This crawler version is programmed in Augst, 2022, element names are corresponding to WOS website elements at that time.
D. Installation of Chromedriver is available in the following tutorial: https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
E. The results given by web crawler script (i.e. result_HER1.csv) are not directly used as the input database for further data mining and machine learning modeling. 
    They would are proofread with very little manpower with the "Bug_Note" columns.