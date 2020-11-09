# CSV importer


Library deisgned for the persons working under the supervision of Paul-Arthur Dreyfus, ICST4SM lab, EPFL.
Will import the project dataset into nicely organized nested dictionnaries and named panda DataFrame.

you may describe your pathToDataset variable as such:
**pathToDataset**/Noise_1/1121.csv

Data is saved in the following structure:
- Dict for the noise type
	- Dict for the noise sub-variants
		- pandas dataframe (1 per csv file)
			- x serie
			- y serie

Dependency:
- matplotlib
- pandas