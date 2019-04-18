# PDF Merge

A desktop tool to allow PDFs to be merged together in a custom order. Built using Python

### CLI version

##### Demo

<p align="center">
  <img alt="PDF Merge CLI" src='https://user-images.githubusercontent.com/39765499/56249196-c524c300-60a2-11e9-853b-a3b335e1811a.gif'>
</p>

##### Features

* Select documents to be merged
* Basic input validation
* Set page range
* Set and save merged file name
* Supports an infinite number of PDFs


### How to Run

```
$ git clone https://github.com/barclayd/PDF-Merge
$ cd PDF-Merge
$ pip install PyPDF2
$ python command-line-pdf-merge.py
```

### GUI version

##### Demo

<p align="center">
  <img alt="PDF Merge GUI" src='https://user-images.githubusercontent.com/39765499/56248547-52b2e380-60a0-11e9-934c-dc1541d0c723.gif'>
</p>

##### Features

* Select documents to be merged
* Specify a page range to be merged for each PDF
* Supports an infinite number of PDFs to be merged
* Remove a PDF from the list after adding it
* Supports drag and drop to re-organise structure of merged PDF document
* Save the merged PDF document anywhere within your directory
* Improved display of PDF documents

### How to Run

```
$ git clone https://github.com/barclayd/PDF-Merge
$ cd PDF-Merge
$ pip install PyPDF2
$ python pdf_merge_v2.py
```


### Future improvements

* Input validation for page range
* Option to duplicate a specific document and its selected page range
* Sort PDF list by date added, name, number of pages and more
* Option to preview pages being merged for each document and preview merged document before saving
