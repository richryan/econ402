Class materials for the Winter 2018 semester of Intermediate Macroeconomics, ECON 402.
This repository mainly catalogues notes and R code used throughout the semester.

The R project is contained in the main directory.
The GitHub project page is read from the `docs` directory.

Here are a few useful remarks for creating the project page:

- Guidelines for basic writing and formatting syntax on GitHub pages are available [here](https://help.github.com/articles/basic-writing-and-formatting-syntax/)
- To have the project page read from the `docs` directory, from [GitHub pages](https://github.com/richryan) navigate to the **Settings** tab and select **master branch/docs folder**
- Render the **.Rmd** file with the command `rmarkdown::render("my-file.Rmd", encoding = "UTF-8")`, the `encoding` option allows for the inclusion of emojis
- **_ALL_** **.Rmd** files need to be rendered
- To convert a `.Rmd` file to pdf use the command `rmarkdown::render("my-file.Rmd", pdf_document())`.
See the documentation for the R package "rmarkdown".